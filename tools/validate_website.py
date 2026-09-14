#!/usr/bin/env python3
"""Check objective properties of the cumulative Markdown website."""

from __future__ import annotations

import argparse
import ast
import re
from dataclasses import dataclass
from pathlib import Path

from build_handouts import FENCE, ROOT


LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
ATX_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
SETEXT = re.compile(r"^(=+|-+)\s*$")


@dataclass
class CheckResult:
    errors: list[str]
    warnings: list[str]


def local_target(raw: str) -> str | None:
    target = raw.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http:", "https:", "mailto:", "data:")):
        return None
    return target.split("#", 1)[0]


def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    found: list[tuple[int, int, str]] = []
    fence_char = ""
    for number, line in enumerate(lines, start=1):
        fence = FENCE.match(line)
        if fence:
            if not fence_char:
                fence_char = fence.group(1)[0]
            elif fence.group(1)[0] == fence_char and not fence.group(2):
                fence_char = ""
            continue
        if fence_char:
            continue
        atx = ATX_HEADING.match(line)
        if atx:
            found.append((number, len(atx.group(1)), atx.group(2)))
            continue
        if number < len(lines) and line.strip() and SETEXT.match(lines[number]):
            found.append((number, 1 if lines[number].lstrip().startswith("=") else 2, line.strip()))
    return found


def python_fences(lines: list[str]) -> list[tuple[int, str]]:
    blocks: list[tuple[int, str]] = []
    opening: tuple[str, str, int, list[str]] | None = None
    for number, line in enumerate(lines, start=1):
        fence = FENCE.match(line)
        if opening is None:
            if fence:
                opening = (fence.group(1)[0], fence.group(2), number, [])
            continue
        marker, language, start, content = opening
        if fence and fence.group(1)[0] == marker and not fence.group(2):
            if language == "python":
                blocks.append((start + 1, "".join(content)))
            opening = None
        else:
            content.append(line)
    return blocks


def validate_page(path: Path) -> CheckResult:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    errors: list[str] = []
    warnings: list[str] = []
    liquid_raw = False
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped == "{% raw %}":
            if liquid_raw:
                errors.append(f"line {number}: nested Liquid raw wrapper")
            liquid_raw = True
            continue
        if stripped == "{% endraw %}":
            if not liquid_raw:
                errors.append(f"line {number}: Liquid endraw has no matching raw wrapper")
            liquid_raw = False
            continue
        if "{{" in line and not liquid_raw:
            errors.append(f"line {number}: Jekyll Liquid delimiter must be inside a raw wrapper")
        if "handout-only:" in line:
            errors.append(f"line {number}: handout-only wrapper leaked into docs")
        for match in LINK.finditer(line):
            target = local_target(match.group(1))
            if target and not (path.parent / target).resolve().is_file():
                errors.append(f"line {number}: internal Markdown link not found: {target}")
        for match in IMAGE.finditer(line):
            target = local_target(match.group(1))
            if target and not (path.parent / target).resolve().is_file():
                errors.append(f"line {number}: local image not found: {target}")
    if liquid_raw:
        errors.append("end of file: unclosed Liquid raw wrapper")
    page_headings = headings(lines)
    if not page_headings:
        warnings.append("no Markdown heading found")
    else:
        previous = page_headings[0][1]
        if previous > 2:
            warnings.append(f"line {page_headings[0][0]}: page starts at heading level {previous}")
        for number, level, title in page_headings:
            if title.strip().lower() == "exercises":
                errors.append(f"line {number}: Exercises content leaked into docs")
            if level > previous + 1:
                warnings.append(f"line {number}: heading level jumps from {previous} to {level}")
            previous = level
    for start, code in python_fences(lines):
        try:
            ast.parse(code, filename=str(path))
        except SyntaxError as exc:
            errors.append(f"line {start + (exc.lineno or 1) - 1}: invalid python fence: {exc.msg}")
    return CheckResult(errors, warnings)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the cumulative Markdown website under docs/.")
    parser.add_argument("--docs", type=Path, default=ROOT / "docs", help="website root (default: docs)")
    args = parser.parse_args()
    docs = args.docs.resolve()
    index = docs / "index.md"
    if not index.is_file():
        print(f"ERROR: missing site navigation page: {index}")
        return 1
    pages = sorted(docs.rglob("*.md"))
    if not pages:
        print(f"ERROR: no Markdown pages found under {docs}")
        return 1
    errors = 0
    warnings = 0
    for page in pages:
        result = validate_page(page)
        relative = page.relative_to(ROOT)
        for error in result.errors:
            errors += 1
            print(f"ERROR {relative}: {error}")
        for warning in result.warnings:
            warnings += 1
            print(f"WARN {relative}: {warning}")
    if errors:
        print(f"Website validation failed: {errors} error(s), {warnings} warning(s).")
        return 1
    print(f"Validated {len(pages)} website page(s) with {warnings} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
