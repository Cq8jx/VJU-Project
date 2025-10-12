import glob
import os
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import yaml

CONFIG = [
    {
        "directory": Path("Quality Assurance/English"),
        "data_file": Path("_data/quality_assurance_en.yml"),
    },
    {
        "directory": Path("Quality Assurance/Japanese"),
        "data_file": Path("_data/quality_assurance_ja.yml"),
    },
    {
        "directory": Path("Quality Assurance/Vietnamese"),
        "data_file": Path("_data/quality_assurance_vi.yml"),
    },
    {
        "directory": Path("University Regulations/English"),
        "data_file": Path("_data/university_regulations_en.yml"),
    },
    {
        "directory": Path("University Regulations/Japanese"),
        "data_file": Path("_data/university_regulations_ja.yml"),
    },
    {
        "directory": Path("University Regulations/Vietnamese"),
        "data_file": Path("_data/university_regulations_vi.yml"),
    },
    {
        "directory": Path("Public Report 2025/English"),
        "data_file": Path("_data/public_report_2025_en.yml"),
    },
    {
        "directory": Path("Public Report 2025/Japanese"),
        "data_file": Path("_data/public_report_2025_ja.yml"),
    },
    {
        "directory": Path("Public Report 2025/Vietnamese"),
        "data_file": Path("_data/public_report_2025_vi.yml"),
    },
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


def build_index_for_directory(directory: Path, data_file: Optional[Path] = None) -> None:
    entries = []
    rows = []
    for file_path in sorted(glob.glob(str(directory / "*.md"))):
        path_obj = Path(file_path)
        if path_obj.name.lower() == "index.md":
            continue
        meta = extract_front_matter(path_obj)
        file_name = path_obj.name
        link_text = meta.get("id", file_name)
        title = meta.get("title", "(no title)")
        rows.append(f"- [{link_text}]({make_link(path_obj)}) — {title}")
        entries.append(
            {
                "id": link_text,
                "title": title,
                "url": f"/{directory.as_posix()}/{file_name}",
            }
        )
    output_path = directory / "index.md"
    header = "# Index\n\n" if rows else "# Index\n\n_No documents available._\n"
    content = header + "\n".join(rows) + ("\n" if rows else "")
    output_path.write_text(content, encoding="utf-8")
    if data_file is not None:
        data_file.parent.mkdir(parents=True, exist_ok=True)
        data_file.write_text(
            yaml.safe_dump(entries, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )


def main() -> None:
    for item in CONFIG:
        directory = item["directory"]
        data_file = item.get("data_file")
        if not directory.exists():
            continue
        build_index_for_directory(directory, data_file)


if __name__ == "__main__":
    main()
