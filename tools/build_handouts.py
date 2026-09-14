#!/usr/bin/env python3
"""Validate and render Markdown session handouts without modifying sources."""

from __future__ import annotations

import argparse
import ast
import os
import re
import shutil
import subprocess
import sys
import warnings
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SESSIONS = ROOT / "sessions"
DEFAULT_OUTPUT = ROOT / "build"
MAJOR_HEADINGS = {"Definitions", "Functions", "Methods", "Topics", "Exercises"}
WRAPPER = re.compile(r"^\s*<!--\s*(handout-only|web-only):(start|end)\s*-->\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})\s*([^\s]*)")
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


@dataclass
class ValidationResult:
    errors: list[str]
    text: str


def source_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    path = path.resolve()
    try:
        path.relative_to(SESSIONS.resolve())
    except ValueError as exc:
        raise argparse.ArgumentTypeError("session sources must be beneath sessions/") from exc
    if path.suffix.lower() != ".md":
        raise argparse.ArgumentTypeError("session sources must be Markdown files")
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"session source does not exist: {path}")
    return path


def parse_wrappers(lines: list[str], output: str) -> tuple[list[str], list[str]]:
    """Return selected lines and wrapper-structure errors for one output."""
    errors: list[str] = []
    selected: list[str] = []
    active: str | None = None
    fence_char = ""
    for number, line in enumerate(lines, start=1):
        fence = FENCE.match(line)
        if not fence_char:
            match = WRAPPER.match(line)
            if match:
                kind, action = match.groups()
                if action == "start":
                    if active:
                        errors.append(f"line {number}: {kind}:start overlaps active {active} wrapper")
                    else:
                        active = kind
                elif active != kind:
                    errors.append(f"line {number}: {kind}:end has no matching open wrapper")
                else:
                    active = None
                continue
            if "handout-only:" in line or "web-only:" in line:
                errors.append(f"line {number}: malformed output wrapper")
        if active is None or active == f"{output}-only":
            selected.append(line)
        if fence:
            if not fence_char:
                fence_char = fence.group(1)[0]
            elif fence.group(1)[0] == fence_char and not fence.group(2):
                fence_char = ""
    if active:
        errors.append(f"end of file: unclosed {active}:start wrapper")
    return selected, errors


def check_fences(lines: list[str]) -> tuple[list[str], list[tuple[int, str]]]:
    """Check ordinary Python fences and return fenced-content masking metadata."""
    errors: list[str] = []
    python_blocks: list[tuple[int, str]] = []
    opening: tuple[str, str, int, list[str]] | None = None
    for number, line in enumerate(lines, start=1):
        match = FENCE.match(line)
        if not opening:
            if match:
                marker, language = match.groups()
                opening = (marker[0], language, number, [])
            continue
        char, language, start, content = opening
        if match and match.group(1)[0] == char and not match.group(2):
            if language == "python":
                python_blocks.append((start + 1, "".join(content)))
            opening = None
        else:
            content.append(line)
    if opening:
        errors.append(f"line {opening[2]}: unclosed fenced code block")
    return errors, python_blocks


def check_major_headings(lines: list[str], required: set[str]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    in_fence = False
    fence_char = ""
    for number, line in enumerate(lines, start=1):
        fence = FENCE.match(line)
        if fence:
            if not in_fence:
                in_fence, fence_char = True, fence.group(1)[0]
            elif fence.group(1)[0] == fence_char and not fence.group(2):
                in_fence = False
            continue
        if in_fence:
            continue
        heading = re.match(r"^#\s+(.+?)\s*#*\s*$", line)
        if heading:
            name = heading.group(1)
            if name not in MAJOR_HEADINGS:
                errors.append(f"line {number}: unsupported H1 {name!r}")
            elif name in seen:
                errors.append(f"line {number}: duplicate H1 {name!r}")
            else:
                seen.add(name)
    for name in sorted(required - seen):
        errors.append(f"missing required H1 {name!r}")
    return errors


def check_images(path: Path, lines: list[str]) -> list[str]:
    errors: list[str] = []
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
        for match in IMAGE.finditer(line):
            target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
            if not target or re.match(r"^(https?:|data:|#)", target):
                continue
            image = (path.parent / target.split("#", 1)[0]).resolve()
            if not image.is_file():
                errors.append(f"line {number}: local image not found: {target}")
    return errors


def validate(path: Path, required: set[str]) -> ValidationResult:
    try:
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    except UnicodeDecodeError:
        return ValidationResult(["file is not valid UTF-8"], "")
    handout_lines, wrapper_errors = parse_wrappers(lines, "handout")
    errors = wrapper_errors
    # Check semantic source blocks in both outputs.  Wrapper selection only affects rendering.
    fence_errors, python_blocks = check_fences(lines)
    errors.extend(fence_errors)
    errors.extend(check_major_headings(handout_lines, required))
    errors.extend(check_images(path, lines))
    for start, code in python_blocks:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                ast.parse(code, filename=str(path))
        except SyntaxError as exc:
            errors.append(f"line {start + (exc.lineno or 1) - 1}: invalid python fence: {exc.msg}")
    return ValidationResult(errors, "".join(handout_lines))


def output_pdf(path: Path, output_dir: Path) -> Path:
    return output_dir / path.relative_to(SESSIONS).with_suffix(".pdf")


def render(path: Path, rendered_markdown: str, output_dir: Path, pdf_engine: str) -> None:
    pandoc = os.environ.get("PANDOC") or shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("Pandoc was not found. Install it or set the PANDOC environment variable.")
    weasyprint = os.environ.get("WEASYPRINT") or shutil.which("weasyprint")
    if not weasyprint:
        raise RuntimeError("WeasyPrint was not found. Install it or set the WEASYPRINT environment variable.")
    target = output_pdf(path, output_dir)
    temporary = output_dir / ".tmp" / path.relative_to(SESSIONS)
    html = temporary.with_suffix(".html")
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary.parent.mkdir(parents=True, exist_ok=True)
    temporary.write_text(rendered_markdown, encoding="utf-8")
    resources = os.pathsep.join((str(path.parent), str(SESSIONS), str(ROOT)))
    command = [
        pandoc, str(temporary), "--from", "markdown+raw_html", "--to", "html5",
        "--standalone", "--output", str(html),
        "--template", str(ROOT / "templates" / "handout.html"),
        "--css", str(ROOT / "templates" / "handout.css"),
        "--lua-filter", str(ROOT / "tools" / "handout.lua"),
        "--toc", "--toc-depth=2", "--metadata", "toc-title=Table of contents",
        "--syntax-highlighting=none", "--embed-resources", f"--resource-path={resources}",
    ]
    subprocess.run(command, check=True)
    subprocess.run([weasyprint, str(html), str(target)], check=True)
    print(f"Built {target.relative_to(ROOT)}")


def discover_sources() -> list[Path]:
    return sorted(path.resolve() for path in SESSIONS.rglob("*.md") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and render canonical session handouts.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def shared(subparser: argparse.ArgumentParser, with_source: bool) -> None:
        if with_source:
            subparser.add_argument("source", type=source_path)
        subparser.add_argument("--require-major", action="append", default=[], choices=sorted(MAJOR_HEADINGS),
                               help="H1 that this non-empty handout is expected to contain; repeat as needed.")

    validate_parser = subparsers.add_parser("validate", help="validate one session source")
    shared(validate_parser, True)
    build_parser = subparsers.add_parser("build", help="validate and render one PDF")
    shared(build_parser, True)
    build_parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    build_parser.add_argument("--pdf-engine", default="xelatex", help=argparse.SUPPRESS)
    all_parser = subparsers.add_parser("build-all", help="validate and render every session PDF")
    shared(all_parser, False)
    all_parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    all_parser.add_argument("--pdf-engine", default="xelatex", help=argparse.SUPPRESS)
    args = parser.parse_args()
    sources = [args.source] if hasattr(args, "source") else discover_sources()
    if not sources:
        print("No canonical session Markdown sources found under sessions/.")
        return 0
    required = set(args.require_major)
    results = [(path, validate(path, required)) for path in sources]
    failed = False
    for path, result in results:
        if result.errors:
            failed = True
            for error in result.errors:
                print(f"{path.relative_to(ROOT)}: {error}", file=sys.stderr)
        else:
            print(f"Validated {path.relative_to(ROOT)}")
    if failed:
        return 1
    if args.command == "validate":
        return 0
    try:
        output_dir = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
        for path, result in results:
            render(path, result.text, output_dir.resolve(), args.pdf_engine)
    except (RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
