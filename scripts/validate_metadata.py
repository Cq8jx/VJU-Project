#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
LANGUAGE_DIR_CODES = {"English": "en", "Vietnamese": "vi", "Japanese": "ja"}
NAME_SUFFIX_CODES = {" - English": "en", " - Vietnamese": "vi", " - Japanese": "ja"}
LANGUAGE_ORDER = ["vi", "en", "ja"]
ALLOWED_STATUS = {"active", "amended", "repealed"}


def detect_language(path: Path):
    for part in path.parts:
        if part in LANGUAGE_DIR_CODES:
            return LANGUAGE_DIR_CODES[part]
    stem = path.stem
    for suffix, code in NAME_SUFFIX_CODES.items():
        if stem.endswith(suffix):
            return code
    return None


def parse_document(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing front matter start")
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        raise ValueError("missing front matter end")
    fm_raw = text[4:end_idx]
    data = yaml.safe_load(fm_raw) or {}
    body = text[end_idx + 5 :]
    return data, body


def collect_documents():
    documents: Dict[str, List[Path]] = defaultdict(list)
    info = {}
    for path in REPO_ROOT.rglob("*.md"):
        if path.name.lower() == "index.md":
            continue
        data, body = parse_document(path)
        doc_id = data.get("id")
        if not doc_id:
            raise ValueError(f"missing id in {path}")
        language = detect_language(path)
        if not language:
            continue
        documents[doc_id].append(path)
        info[path] = (data, language)
    return documents, info


def validate_languages(documents, info, errors):
    for doc_id, paths in documents.items():
        available = sorted({info[path][1] for path in paths}, key=lambda code: LANGUAGE_ORDER.index(code))
        for path in paths:
            data, _ = info[path]
            if data.get("languages") != available:
                errors.append(f"languages mismatch in {path}")


def slugify(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").upper()


def validate_ids(info, errors):
    for path, (data, _) in info.items():
        doc_id = data.get("id")
        if not doc_id:
            continue
        stem_slug = slugify(path.stem)
        doc_slug = slugify(doc_id)
        if not (
            stem_slug == doc_slug
            or stem_slug.startswith(doc_slug)
            or doc_slug.startswith(stem_slug)
            or stem_slug.endswith(doc_slug)
            or doc_slug.endswith(stem_slug)
        ):
            errors.append(f"id '{doc_id}' does not align with filename '{path.name}'")


def validate_status(info, errors):
    for path, (data, _) in info.items():
        status = data.get("status")
        if status not in ALLOWED_STATUS:
            errors.append(f"invalid status '{status}' in {path}")


def validate_source(documents, info, errors):
    for doc_id, paths in documents.items():
        for path in paths:
            data, _ = info[path]
            source = data.get("source_pdf")
            relative = path.relative_to(REPO_ROOT)
            if len(relative.parts) < 2:
                continue
            source_dir = REPO_ROOT / relative.parts[0] / "Source"
            expected = []
            if source_dir.exists():
                expected.extend(source_dir.glob(f"{doc_id}*.pdf"))
                expected.extend(source_dir.glob(f"{doc_id}*.docx"))
                expected.extend(source_dir.glob(f"{doc_id}*.doc"))
            if expected:
                if not source:
                    errors.append(f"missing source_pdf link in {path}")
                else:
                    target = (path.parent / Path(source)).resolve()
                    if not target.exists():
                        errors.append(f"source_pdf path not found for {path}")


def main():
    documents, info = collect_documents()
    errors = []
    validate_languages(documents, info, errors)
    validate_ids(info, errors)
    validate_status(info, errors)
    validate_source(documents, info, errors)
    if errors:
        for err in errors:
            print(err)
        sys.exit(1)
    print("All metadata checks passed.")


if __name__ == "__main__":
    main()
