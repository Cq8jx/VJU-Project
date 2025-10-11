#!/usr/bin/env python3
from __future__ import annotations

import os
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import quote

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
LANGUAGE_DIR_CODES = {"English": "en", "Vietnamese": "vi", "Japanese": "ja"}
NAME_SUFFIX_CODES = {" - English": "en", " - Vietnamese": "vi", " - Japanese": "ja"}
LANGUAGE_ORDER = ["vi", "en", "ja"]
SOURCE_PRIORITY = [".pdf", ".docx", ".doc"]


class Document:
    def __init__(self, path: Path, language: str, data: Dict, body: str, fm_start: int, fm_end: int):
        self.path = path
        self.language = language
        self.data = data
        self.body = body
        self.fm_start = fm_start
        self.fm_end = fm_end


def detect_language(path: Path) -> Optional[str]:
    for part in path.parts:
        if part in LANGUAGE_DIR_CODES:
            return LANGUAGE_DIR_CODES[part]
    stem = path.stem
    for suffix, code in NAME_SUFFIX_CODES.items():
        if stem.endswith(suffix):
            return code
    return None


def parse_markdown(path: Path) -> Optional[Document]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return None
    fm_raw = text[4:end_idx]
    data = yaml.safe_load(fm_raw) or {}
    body = text[end_idx + 5 :]
    return Document(path, detect_language(path), data, body, 0, end_idx + 5)


def normalise_languages(documents: Dict[str, List[Document]]):
    for doc_id, docs in documents.items():
        available = sorted({doc.language for doc in docs if doc.language}, key=lambda code: LANGUAGE_ORDER.index(code))
        if not available:
            continue
        for doc in docs:
            doc.data["languages"] = available


def find_source_file(doc: Document) -> Optional[str]:
    relative = doc.path.relative_to(REPO_ROOT)
    if len(relative.parts) < 2:
        return None
    collection_dir = REPO_ROOT / relative.parts[0] / "Source"
    if not collection_dir.exists():
        return None
    doc_id = doc.data.get("id")
    if not doc_id:
        return None
    matches: List[Path] = []
    for pattern in (f"{doc_id}*.pdf", f"{doc_id}*.docx", f"{doc_id}*.doc"):
        matches.extend(sorted(collection_dir.glob(pattern)))
    if not matches:
        return None
    best = sorted(matches, key=lambda p: SOURCE_PRIORITY.index(p.suffix.lower()) if p.suffix.lower() in SOURCE_PRIORITY else len(SOURCE_PRIORITY))[0]
    rel_path = Path(os.path.relpath(best, doc.path.parent)).as_posix()
    return rel_path


def ensure_versions(documents: Dict[str, List[Document]]):
    for docs in documents.values():
        available = sorted({doc.language for doc in docs if doc.language}, key=lambda code: LANGUAGE_ORDER.index(code))
        if len(available) < 2:
            continue
        for doc in docs:
            links = []
            for code in available:
                target = next((item for item in docs if item.language == code and item.path == doc.path), None)
                if target is None:
                    target = next((item for item in docs if item.language == code), None)
                if target is None:
                    continue
                rel_path = Path(os.path.relpath(target.path, doc.path.parent)).as_posix()
                parts = rel_path.split("/")
                encoded = "/".join(quote(part) for part in parts)
                links.append(f"[{code.upper()}]({encoded})")
            if not links:
                continue
            version_line = "> Versions: " + " | ".join(links)
            body = doc.body.lstrip("\n")
            lines = body.splitlines()
            if lines and lines[0].startswith("> Versions:"):
                lines[0] = version_line
            else:
                lines.insert(0, version_line)
            if len(lines) == 1 or (len(lines) > 1 and lines[1].strip()):
                lines.insert(1, "")
            doc.body = "\n".join(lines)


def update_source_paths(documents: Dict[str, List[Document]]):
    for docs in documents.values():
        for doc in docs:
            source_path = find_source_file(doc)
            if source_path:
                doc.data["source_pdf"] = source_path


def write_document(doc: Document):
    front_matter = yaml.safe_dump(doc.data, sort_keys=False, allow_unicode=True).strip()
    body = doc.body.rstrip()
    content = f"---\n{front_matter}\n---\n{body}\n"
    doc.path.write_text(content, encoding="utf-8")


def main():
    documents: Dict[str, List[Document]] = defaultdict(list)
    for path in REPO_ROOT.rglob("*.md"):
        if path.name.lower() == "index.md":
            continue
        doc = parse_markdown(path)
        if not doc:
            continue
        if not doc.language:
            continue
        doc_id = doc.data.get("id")
        if not doc_id:
            continue
        documents[doc_id].append(doc)

    normalise_languages(documents)
    update_source_paths(documents)
    ensure_versions(documents)

    for docs in documents.values():
        for doc in docs:
            write_document(doc)


if __name__ == "__main__":
    main()
