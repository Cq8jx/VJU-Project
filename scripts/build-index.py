#!/usr/bin/env python3
"""Generate University Regulations indexes and data files.

This script scans the language-specific directories under
`University Regulations/` and produces two artifacts per language:

1. `index.md` files listing all documents for that language.
2. `_data/university_regulations_<lang>.yml` for site-wide consumption.

The existing Markdown files are expected to include YAML front matter
with at least the `id` and `title` fields.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import quote

import yaml


LANGUAGE_MAP: Dict[str, str] = {
    "English": "en",
    "Japanese": "ja",
    "Vietnamese": "vi",
}


@dataclass
class DocumentEntry:
    identifier: str
    title: str
    filename: str
    url: str


def read_front_matter(path: Path) -> Optional[dict]:
    """Extract front matter from a Markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None

    try:
        _, front_matter, _ = text.split("---\n", 2)
    except ValueError:
        return None

    data = yaml.safe_load(front_matter)
    if not isinstance(data, dict):
        return None
    return data


def build_document_list(base_dir: Path, language: str) -> List[DocumentEntry]:
    """Collect document metadata for a language."""
    docs: List[DocumentEntry] = []
    language_dir = base_dir / "University Regulations" / language

    if not language_dir.is_dir():
        raise FileNotFoundError(f"Missing directory: {language_dir}")

    for path in sorted(language_dir.glob("*.md")):
        if path.name == "index.md":
            continue

        front = read_front_matter(path)
        if not front:
            print(f"Warning: {path} has no readable front matter; skipped.", file=sys.stderr)
            continue

        identifier = str(front.get("id", path.stem))
        title = str(front.get("title", path.stem))

        relative_url = f"/University Regulations/{language}/{path.name}"
        docs.append(
            DocumentEntry(
                identifier=identifier,
                title=title,
                filename=path.name,
                url=relative_url,
            )
        )

    docs.sort(key=lambda item: (item.identifier.lower(), item.title.lower()))
    return docs


def write_index(language_dir: Path, documents: List[DocumentEntry]) -> None:
    """Write the language index.md file."""
    lines = ["# Index", ""]
    for doc in documents:
        encoded_filename = quote(doc.filename)
        suffix = doc.title
        if doc.title.lower().startswith(doc.identifier.lower()):
            suffix = doc.title[len(doc.identifier):].lstrip(" -—–")

        line = f"- [{doc.identifier}]({encoded_filename})"
        if suffix:
            line += f" — {suffix}"
        lines.append(line)

    lines.append("")
    index_path = language_dir / "index.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")


def write_data_file(data_dir: Path, language_code: str, documents: List[DocumentEntry]) -> None:
    """Write the Jekyll data file."""
    payload = [
        {"id": doc.identifier, "title": doc.title, "url": doc.url}
        for doc in documents
    ]

    yaml_text = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True)
    data_path = data_dir / f"university_regulations_{language_code}.yml"
    data_path.write_text(yaml_text, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build University Regulations indexes and data files.")
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path("."),
        help="Repository root that contains the 'University Regulations' directory (default: current directory).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base_dir: Path = args.base_dir.resolve()
    data_dir = base_dir / "_data"

    for language, code in LANGUAGE_MAP.items():
        documents = build_document_list(base_dir, language)
        write_index(base_dir / "University Regulations" / language, documents)
        write_data_file(data_dir, code, documents)

    return 0


if __name__ == "__main__":
    sys.exit(main())
