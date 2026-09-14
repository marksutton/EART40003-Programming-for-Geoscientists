#!/usr/bin/env python3
"""Prepare a canonical session Markdown file for cumulative-site integration."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from build_handouts import FENCE, ROOT, SESSIONS, parse_wrappers


H1 = re.compile(r"^#\s+(.+?)\s*#*\s*$")
HEADING = re.compile(r"^(#{1,4})\s+(.+?)\s*#*\s*$")


def session_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    path = path.resolve()
    try:
        path.relative_to(SESSIONS.resolve())
    except ValueError as exc:
        raise argparse.ArgumentTypeError("session sources must be beneath sessions/") from exc
    if path.suffix.lower() != ".md" or not path.is_file():
        raise argparse.ArgumentTypeError(f"session source does not exist: {path}")
    return path


def without_front_matter(lines: list[str]) -> list[str]:
    if not lines or lines[0].strip() != "---":
        return lines
    for number, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[number + 1 :]
    return lines


def without_exercises(lines: list[str]) -> list[str]:
    """Drop the Exercises H1 and anything following it, without parsing code as headings."""
    result: list[str] = []
    dropping = False
    fence_char = ""
    for line in lines:
        fence = FENCE.match(line)
        if fence:
            if not fence_char:
                fence_char = fence.group(1)[0]
            elif fence.group(1)[0] == fence_char and not fence.group(2):
                fence_char = ""
        if not fence_char:
            heading = H1.match(line)
            if heading and heading.group(1) == "Exercises":
                dropping = True
        if not dropping:
            result.append(line)
    return result


def web_view(path: Path) -> tuple[list[str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    selected, errors = parse_wrappers(lines, "web")
    return without_exercises(without_front_matter(selected)), errors


def inventory(path: Path, lines: list[str]) -> str:
    sections: list[str] = []
    entries: dict[str, list[str]] = {"Definitions": [], "Functions": [], "Methods": [], "Topics": []}
    current_h1: str | None = None
    fence_char = ""
    for line in lines:
        fence = FENCE.match(line)
        if fence:
            if not fence_char:
                fence_char = fence.group(1)[0]
            elif fence.group(1)[0] == fence_char and not fence.group(2):
                fence_char = ""
            continue
        if fence_char:
            continue
        match = HEADING.match(line)
        if not match:
            continue
        level, title = len(match.group(1)), match.group(2)
        if level == 1:
            current_h1 = title
            sections.append(title)
        elif current_h1 in entries and ((current_h1 == "Topics" and level == 2) or
                                        (current_h1 != "Topics" and level >= 3)):
            entries[current_h1].append(title)

    output = [f"# Integration inventory: {path.name}", "", f"Major sections: {', '.join(sections) or 'none'}"]
    for section in ("Definitions", "Functions", "Methods", "Topics"):
        if entries[section]:
            output.extend(("", f"## {section}", *[f"- {entry}" for entry in entries[section]]))
    output.extend(("", "Excluded automatically: Exercises, handout-only blocks."))
    return "\n".join(output) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Filter and inventory one canonical session for website integration.")
    parser.add_argument("source", type=session_path)
    parser.add_argument("--view", action="store_true", help="print filtered Markdown instead of an inventory")
    args = parser.parse_args()
    lines, errors = web_view(args.source)
    if errors:
        for error in errors:
            print(f"{args.source.relative_to(ROOT)}: {error}")
        return 1
    if args.view:
        print("".join(lines), end="")
    else:
        print(inventory(args.source, lines), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
