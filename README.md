# EART40003 Programming for Geoscientists

## Handout authoring and builds

Weekly canonical Markdown handouts belong in `sessions/`; generated PDFs go to the ignored `build/` directory. See [AUTHORING.md](AUTHORING.md) for the source format.

Validate one handout with `python tools/build_handouts.py validate sessions/week-01.md`, build one with `python tools/build_handouts.py build sessions/week-01.md`, or build every session with `python tools/build_handouts.py build-all`. PDF builds require [Pandoc](https://pandoc.org/) and [WeasyPrint](https://weasyprint.org/).

The canonical handouts are not transformed automatically into the website.

## Cumulative website integration

The website under `docs/` is a cumulative concept-based reference, not a sequence of weekly handouts. It currently contains only the material integrated from Session 1. The previous whole-course site is preserved under `legacy-site/` and is not published.

See [INTEGRATION.md](INTEGRATION.md) for the editorial contract and review workflow. Use `python tools/session_inventory.py sessions/session-01.md` to inspect the web-eligible content of one canonical session, and `python tools/validate_website.py` after website edits.
