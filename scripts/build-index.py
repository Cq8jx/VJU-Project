import glob
import os
from pathlib import Path
from urllib.parse import quote

import yaml

LANG_DIRS = [
    "Quality Assurance/Vietnamese",
    "Quality Assurance/English",
    "Quality Assurance/Japanese",
]


def extract_front_matter(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        first_line = fh.readline()
        if first_line.strip() != "---":
            return {}
        meta_lines = []
        for line in fh:
            if line.strip() == "---":
                break
            meta_lines.append(line)
    if not meta_lines:
        return {}
    data = yaml.safe_load("".join(meta_lines))
    return data or {}


def make_link(path: Path) -> str:
    return quote(path.name)


def build_index_for_directory(directory: str) -> None:
    rows = []
    for file_path in sorted(glob.glob(os.path.join(directory, "*.md"))):
        if Path(file_path).name.lower() == "index.md":
            continue
        meta = extract_front_matter(Path(file_path))
        file_name = Path(file_path).name
        link_text = meta.get("id", file_name)
        title = meta.get("title", "(no title)")
        rows.append(f"- [{link_text}]({make_link(Path(file_path))}) — {title}")
    output_path = Path(directory) / "index.md"
    header = "# Index\n\n" if rows else "# Index\n\n_No documents available._\n"
    content = header + "\n".join(rows) + ("\n" if rows else "")
    output_path.write_text(content, encoding="utf-8")


def main() -> None:
    for directory in LANG_DIRS:
        build_index_for_directory(directory)


if __name__ == "__main__":
    main()
