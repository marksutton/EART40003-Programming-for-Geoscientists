#!/usr/bin/env python3
"""Build the browsable tutor area and its reproducible backup ZIP."""

from __future__ import annotations

import argparse
import io
import re
import sys
import zipfile
from pathlib import Path

from build_handouts import ROOT, parse_wrappers, validate


OUTPUT = ROOT / "docs" / "ai"
ARCHIVE = OUTPUT / "eart40003-ai-tutor.zip"
ZIP_TIME = (2026, 1, 1, 0, 0, 0)
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SESSION_FILES = sorted((ROOT / "sessions").glob("session-*.md"))
DEMO_FILES = sorted((ROOT / "examples").glob("*.py"))


def web_session(source: Path) -> bytes:
    lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"missing session metadata: {source}")
    try:
        metadata_end = next(
            i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ValueError(f"unclosed session metadata: {source}") from exc
    selected, errors = parse_wrappers(lines[metadata_end + 1 :], "web")
    if errors:
        raise ValueError(f"{source}: {'; '.join(errors)}")
    number = int(source.stem.split("-")[1])
    body = f"# Session {number} reference\n\n" + "".join(selected).lstrip()
    # Liquid raw guards literal {{ in Python examples. Jekyll removes the
    # markers before rendering Markdown. The ZIP gets marker-free Markdown.
    return ("---\n---\n{% raw %}\n" + body.rstrip() + "\n{% endraw %}\n").encode("utf-8")


def navigation(title: str, paths: list[Path]) -> bytes:
    lines = [f"# {title}", "", "Return to the [AI tutor start page](../index.md).", ""]
    for path in paths:
        label = path.stem.replace("-", " ").capitalize()
        lines.append(f"- [{label}]({path.name})")
    lines.append("")
    return "\n".join(lines).encode("utf-8")


def demo_navigation() -> bytes:
    lines = ["# Demonstration programs", "",
             "These are samples of Mark's code from last year's teaching.",
             "Some require data files; read the [demo notes](README.md) before using them.",
             "", "Return to the [AI tutor start page](../index.md).", ""]
    for number in range(1, 9):
        lines += [f"## Session {number}", ""]
        for path in DEMO_FILES:
            if path.name.startswith(f"demo_{number}_"):
                lines.append(f"- [{path.name}]({path.name})")
        lines.append("")
    return "\n".join(lines).encode("utf-8")


def content_map() -> dict[str, bytes]:
    content: dict[str, bytes] = {}
    index = OUTPUT / "index.md"
    if not index.is_file():
        raise ValueError(f"missing authored start page: {index}")
    content["index.md"] = index.read_bytes()

    for source in sorted((ROOT / "ai-helper").glob("*.md")):
        content[f"ai-helper/{source.name}"] = source.read_bytes()
    for source in SESSION_FILES:
        content[f"sessions/{source.name}"] = web_session(source)
    content["sessions/index.md"] = navigation("Session handouts", SESSION_FILES)
    for source in sorted((ROOT / "sessions" / "assets").rglob("*")):
        if source.is_file():
            relative = source.relative_to(ROOT / "sessions").as_posix()
            content[f"sessions/{relative}"] = source.read_bytes()

    source_readme = ROOT / "examples" / "README.md"
    content["examples/README.md"] = source_readme.read_bytes()
    content["examples/index.md"] = demo_navigation()
    for source in DEMO_FILES:
        content[f"examples/{source.name}"] = source.read_bytes()
    return content


def zip_bytes(content: dict[str, bytes]) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(content.items()):
            if name.startswith("sessions/") and name.endswith(".md") and name != "sessions/index.md":
                data = data.removeprefix(b"---\n---\n{% raw %}\n").removesuffix(b"{% endraw %}\n")
            info = zipfile.ZipInfo(name, ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return stream.getvalue()


def verify_links(content: dict[str, bytes]) -> list[str]:
    errors: list[str] = []
    for name, data in content.items():
        if not name.endswith(".md"):
            continue
        for target in LINK.findall(data.decode("utf-8")):
            target = target.strip().split(maxsplit=1)[0].strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http:", "https:", "mailto:", "data:")):
                continue
            path = (OUTPUT / Path(name).parent / target).resolve()
            if not path.is_relative_to(OUTPUT.resolve()):
                errors.append(f"{name}: link escapes tutor area: {target}")
                continue
            relative = path.relative_to(OUTPUT.resolve()).as_posix()
            if (relative != ARCHIVE.name and relative not in content
                    and f"{relative.rstrip('/')}/index.md" not in content):
                errors.append(f"{name}: missing link target: {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check generated files without changing them")
    args = parser.parse_args()
    if len(SESSION_FILES) != 8:
        print(f"Expected eight session sources, found {len(SESSION_FILES)}", file=sys.stderr)
        return 1
    for source in SESSION_FILES:
        result = validate(source, set())
        if result.errors:
            print(f"Invalid source {source}: {'; '.join(result.errors)}", file=sys.stderr)
            return 1
    content = content_map()
    problems = verify_links(content)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    content[ARCHIVE.name] = zip_bytes(content)
    stale: list[str] = []
    unexpected = sorted(
        path.relative_to(OUTPUT).as_posix()
        for path in OUTPUT.rglob("*")
        if path.is_file() and path.relative_to(OUTPUT).as_posix() not in content
    )
    if unexpected:
        print("Unexpected files in tutor area: " + ", ".join(unexpected), file=sys.stderr)
        return 1
    for name, data in content.items():
        path = OUTPUT / name
        if not path.is_file() or path.read_bytes() != data:
            if args.check:
                stale.append(name)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    if stale:
        print("Missing or stale tutor files: " + ", ".join(stale), file=sys.stderr)
        return 1
    action = "Checked" if args.check else "Built"
    print(f"{action} {len(SESSION_FILES)} sessions, {len(DEMO_FILES)} demos, "
          f"{len(content)} tutor files; ZIP {len(content[ARCHIVE.name])} bytes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
