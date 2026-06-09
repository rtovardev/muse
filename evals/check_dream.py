#!/usr/bin/env python3
"""Lightweight structural checker for Muse dream files.

This catches common contract failures. It does not judge idea quality and does
not replace manual scenario scoring.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RE_FILENAME = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<seq>\d{3})-dream\.md$")
RE_ID = re.compile(r"muse-(?P<date>\d{8})-(?P<seq>\d{3})-(?P<letter>[a-z])\b")
RE_ID_LABEL = re.compile(r"^\*\*Idea ID:\*\*\s*(?P<id>muse-\d{8}-\d{3}-[a-z])\b", re.MULTILINE)

REQUIRED_SECTIONS = [
    "## Insights",
    "## Ideas",
    "## Action for today",
    "## How I dreamed this",
]

REQUIRED_IDEA_LABELS = [
    "Idea ID",
    "What it is",
    "Why now",
    "How",
    "First step",
    "Effort / impact",
    "Risks",
    "Assumption",
    "Recombined nodes",
    "Confidence",
    "Falsifier",
    "Connects to",
    "Sources",
    "Route",
]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start == -1:
        return ""
    next_match = re.search(r"^## ", text[start + len(heading):], flags=re.MULTILINE)
    if not next_match:
        return text[start:]
    end = start + len(heading) + next_match.start()
    return text[start:end]


def idea_blocks(ideas_text: str) -> list[str]:
    matches = list(re.finditer(r"^### \d+\. .+", ideas_text, flags=re.MULTILINE))
    blocks: list[str] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(ideas_text)
        blocks.append(ideas_text[start:end])
    return blocks


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Muse dream structure")
    parser.add_argument("dream", type=Path, help="Path to dreams/YYYY-MM-DD-NNN-dream.md")
    args = parser.parse_args()

    path = args.dream
    errors: list[str] = []

    if not path.exists():
        print(f"FAIL: file not found: {path}", file=sys.stderr)
        return 2

    match = RE_FILENAME.match(path.name)
    if not match:
        fail("filename must match YYYY-MM-DD-NNN-dream.md", errors)
        file_date = None
        file_seq = None
    else:
        file_date = match.group("date")
        file_seq = match.group("seq")

    text = path.read_text(encoding="utf-8")

    for heading in REQUIRED_SECTIONS:
        if heading not in text:
            fail(f"missing required section: {heading}", errors)

    ideas_text = section(text, "## Ideas")
    blocks = idea_blocks(ideas_text)
    if not blocks:
        fail("no deep idea blocks found under ## Ideas", errors)

    seen_ids: set[str] = set()
    expected_date = file_date.replace("-", "") if file_date else None

    for n, block in enumerate(blocks, start=1):
        for label in REQUIRED_IDEA_LABELS:
            if f"**{label}:**" not in block:
                fail(f"idea {n} missing label: {label}", errors)

        label_matches = list(RE_ID_LABEL.finditer(block))
        if len(label_matches) != 1:
            fail(f"idea {n} must contain exactly one labelled Idea ID; found {len(label_matches)}", errors)
            continue

        idea_id = label_matches[0].group("id")
        if idea_id in seen_ids:
            fail(f"duplicate idea id: {idea_id}", errors)
        seen_ids.add(idea_id)

        id_match = RE_ID.search(idea_id)
        if id_match and expected_date and id_match.group("date") != expected_date:
            fail(f"idea {n} id date does not match filename: {idea_id}", errors)
        if id_match and file_seq and id_match.group("seq") != file_seq:
            fail(f"idea {n} id sequence does not match filename: {idea_id}", errors)

    if errors:
        print("FAIL")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"PASS: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
