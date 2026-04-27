#!/usr/bin/env python3
"""
Basic markdown link checker for doc/README*.md.

Checks:
1. Relative markdown links resolve to existing files.
2. Discourage local machine paths (/home/...) in markdown links.
"""

from __future__ import annotations

import re
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOC_DIR = ROOT / "doc"
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def iter_markdown_files() -> list[Path]:
    return sorted(DOC_DIR.glob("README*.md"))


def is_external(link: str) -> bool:
    return link.startswith(("http://", "https://", "mailto:"))


def normalize_target(src: Path, link: str) -> Path:
    target = link.split("#", 1)[0].strip()
    return (src.parent / target).resolve()


def main() -> int:
    failures: list[str] = []
    files = iter_markdown_files()
    if not files:
        print("No README*.md files found in doc/.")
        return 0

    for md_file in files:
        text = md_file.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            link = raw.strip()
            if not link:
                continue
            if link.startswith("/home/"):
                failures.append(f"{md_file}: local path link forbidden -> {link}")
                continue
            if is_external(link):
                continue
            # Skip code references that are not expected to resolve as files.
            if link.startswith("python -m "):
                continue

            target = normalize_target(md_file, link)
            if not target.exists():
                failures.append(f"{md_file}: missing relative target -> {link}")

    if failures:
        print("Link check failed:")
        for item in failures:
            print(f"  - {item}")
        return 1

    print("Link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
