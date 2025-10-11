#!/usr/bin/env python3
import os
from pathlib import Path
from urllib.parse import quote
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

LANGUAGE_DISPLAY = {
    "English": {"title_suffix": "(English)", "heading_suffix": "(English)"},
    "Japanese": {"title_suffix": "（日本語）", "heading_suffix": "（日本語）"},
    "Vietnamese": {"title_suffix": " (Tiếng Việt)", "heading_suffix": " (Tiếng Việt)"},
}

COLLECTION_TITLES = {
    "Quality Assurance": "Documents – Quality Assurance",
    "Public Report 2025": "Documents – Public Report 2025",
    "University Regulations": "Documents – University Regulations",
}

HEADING_TITLES = {
    "Quality Assurance": "# Quality Assurance Documents",
    "Public Report 2025": "# Public Report 2025 Documents",
    "University Regulations": "# University Regulations Documents",
}

LANGUAGE_ORDER = ["Vietnamese", "English", "Japanese"]


def parse_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, None
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, None
    fm_raw = parts[0][4:]
    data = yaml.safe_load(fm_raw) or {}
    return data, None


def iter_directories():
    for collection, base in COLLECTION_TITLES.items():
        collection_path = REPO_ROOT / collection
        if not collection_path.exists():
            continue
        for language in LANGUAGE_ORDER:
            lang_dir = collection_path / language
            if lang_dir.exists() and lang_dir.is_dir():
                yield collection, language, lang_dir


def build_rows(language_dir: Path):
    rows = []
    for path in sorted(language_dir.glob("*.md")):
        if path.name.lower() == "index.md":
            continue
        meta, _ = parse_front_matter(path)
        doc_id = meta.get("id") or path.stem
        title = meta.get("title", "(no title)")
        relative = quote(path.name)
        rows.append((doc_id, f"- [{doc_id}](./{relative}) — {title}"))
    rows.sort(key=lambda item: item[0])
    return [row for _, row in rows]


def write_index(collection: str, language: str, directory: Path):
    rows = build_rows(directory)
    title_base = COLLECTION_TITLES[collection]
    heading_base = HEADING_TITLES[collection]
    language_meta = LANGUAGE_DISPLAY[language]
    front_matter = {
        "title": f"{title_base} {language_meta['title_suffix']}",
        "layout": "folder-index",
    }
    heading = f"{heading_base} {language_meta['heading_suffix']}".strip()
    content_lines = ["---", yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=True).strip(), "---", heading, ""]
    content_lines.extend(rows)
    content = "\n".join(line for line in content_lines if line is not None)
    directory.joinpath("index.md").write_text(content + "\n", encoding="utf-8")


def main():
    for collection, language, directory in iter_directories():
        write_index(collection, language, directory)


if __name__ == "__main__":
    main()
