#!/usr/bin/env python3
"""Wrap transcription cautions with a shared markup block."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

PREFIX_CONFIG: List[Tuple[str, Dict[str, str]]] = [
    (
        "This file is a transcription",
        {"lang": "en", "label": "Source note.", "aria": "Source note"},
    ),
    (
        "Recognizing tables encountered technical difficulties",
        {"lang": "en", "label": "Source note.", "aria": "Source note"},
    ),
    (
        "Layout and table contents",
        {"lang": "en", "label": "Source note.", "aria": "Source note"},
    ),
    (
        "Because recognizing tables",
        {"lang": "en", "label": "Source note.", "aria": "Source note"},
    ),
    (
        "Because the original document",
        {"lang": "en", "label": "Source note.", "aria": "Source note"},
    ),
    (
        "このファイル",
        {"lang": "ja", "label": "出典メモ。", "aria": "出典メモ"},
    ),
    (
        "本ファイル",
        {"lang": "ja", "label": "出典メモ。", "aria": "出典メモ"},
    ),
    (
        "Tệp này",
        {"lang": "vi", "label": "Ghi chú nguồn.", "aria": "Ghi chú nguồn"},
    ),
]

ARIA_TO_LANG = {
    "Source note": "en",
    "出典メモ": "ja",
    "Ghi chú nguồn": "vi",
}

NOTE_BLOCK_RE = re.compile(r'(<div class="source-note"[^>]*>)(.*?)(</div>)', re.DOTALL)


def detect_config(text: str) -> Optional[Dict[str, str]]:
    stripped = text.strip()
    for prefix, cfg in PREFIX_CONFIG:
        if stripped.startswith(prefix):
            return cfg
    return None


def split_paragraphs(lines: List[str]) -> List[str]:
    """Treat each non-empty line as a separate paragraph."""
    return [line.strip() for line in lines if line.strip()]


def split_sentences(text: str, lang: str) -> List[str]:
    text = text.strip()
    if not text:
        return []
    if lang == "ja":
        parts = re.split(r"(?<=。)\s*", text)
    else:
        parts = re.split(r"(?<=[.!?])\s+", text)
    return [part.strip() for part in parts if part.strip()]


def normalize_existing_notes(text: str) -> Tuple[str, bool]:
    changed = False

    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        start_tag, inner, end_tag = match.groups()
        first_para = re.search(r"<p><strong>(?P<label>.*?)</strong>\s*(?P<body>.*?)</p>", inner, re.DOTALL)
        if not first_para:
            return match.group(0)

        aria_match = re.search(r'aria-label="([^"]+)"', start_tag)
        aria_value = aria_match.group(1) if aria_match else "Source note"
        lang = ARIA_TO_LANG.get(aria_value, "en")

        label = first_para.group("label")
        body = first_para.group("body").strip()
        rest_html = inner[first_para.end():].strip("\n")

        sentences = split_sentences(body, lang) or [body]
        new_lines = [f'  <p><strong>{label}</strong> {sentences[0]}</p>']

        existing_rest = rest_html.splitlines()
        rest_text = "\n".join(existing_rest)

        for sentence in sentences[1:]:
            if sentence and sentence not in rest_text:
                new_lines.append(f"  <p><em>{sentence}</em></p>")
                changed = True

        for raw_line in existing_rest:
            line = raw_line.rstrip()
            if not line:
                continue
            if not line.startswith("  "):
                line = f"  {line.strip()}"
            new_lines.append(line)

        changed = True
        return f"{start_tag}\n" + "\n".join(new_lines) + f"\n{end_tag}"

    new_text = NOTE_BLOCK_RE.sub(replace, text)
    return new_text, changed


def transform_content(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    text, normalized = normalize_existing_notes(text)
    if normalized:
        path.write_text(text, encoding="utf-8")
        return True

    lines = text.splitlines()
    if not lines or not lines[0].startswith("---"):
        return False

    fm_end: Optional[int] = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            fm_end = idx
            break
    if fm_end is None:
        return False

    content = lines[fm_end + 1 :]
    if not content:
        return False

    hr_index: Optional[int] = None
    for idx, line in enumerate(content):
        if line.strip() == "---":
            hr_index = idx
            break
    if hr_index is None:
        return False

    block_lines = content[:hr_index]
    if not block_lines:
        return False

    start = 0
    while start < len(block_lines) and not block_lines[start].strip():
        start += 1
    end = len(block_lines) - 1
    while end >= start and not block_lines[end].strip():
        end -= 1
    if start > end:
        return False

    focus_lines = block_lines[start : end + 1]
    cfg = detect_config(focus_lines[0])
    if not cfg:
        return False

    paragraphs = split_paragraphs(focus_lines)
    if not paragraphs:
        return False

    note_lines = [
        f'<div class="source-note" role="note" aria-label="{cfg["aria"]}">',
        f'  <p><strong>{cfg["label"]}</strong> {paragraphs[0]}</p>',
    ]
    for para in paragraphs[1:]:
        note_lines.append(f"  <p><em>{para}</em></p>")
    note_lines.append("</div>")

    new_content = (
        content[:start]
        + note_lines
        + [""]
        + content[end + 1 :]
    )

    new_lines = lines[: fm_end + 1] + new_content
    Path(path).write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    return True


def gather_files(base: Path) -> List[Path]:
    return [p for p in base.rglob("*.md") if p.is_file()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply source note markup to Markdown files.")
    parser.add_argument("paths", nargs="*", type=Path, help="Files or directories to process.")
    args = parser.parse_args()

    if args.paths:
        files: List[Path] = []
        for path in args.paths:
            path = path.resolve()
            if path.is_dir():
                files.extend(gather_files(path))
            elif path.is_file():
                files.append(path)
    else:
        files = gather_files(Path.cwd())

    changed = 0
    for file_path in files:
        if transform_content(file_path):
            changed += 1

    print(f"Updated {changed} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
