# Handout authoring

Canonical weekly handout sources live in `sessions/` as Markdown. PDFs in `build/` are generated artifacts: edit the Markdown, not the PDF.

## Structure

Use only these major H1 sections, omitting any that are empty:

- `# Definitions`
- `# Functions`
- `# Methods`
- `# Topics`
- `# Exercises`

Use H2 for major student-facing topics or subgroups, and H3/H4 for reference entries or local subsections. Handout tables of contents stop at H2. Functions are normally individual H3 entries, for example:

```markdown
### `range(start, stop, [step])`

**Returns:** iterable of integers  
**Origin:** built-in

Description...
```

Methods may instead be grouped under their class or type. Use Markdown tables only for genuinely tabular information, and use ordinary Markdown image syntax for images.

## Examples and emphasis

- `python` fences contain executable Python and are syntax-checked by the build tool.
- `python-invalid` fences deliberately contain invalid Python and are not checked.
- `text` fences contain output, tracebacks, or other textual material and are not checked.
- Use a `syntax-template` fenced div for schematic Python structures with explanatory placeholders. It is rendered in the normal proportional handout font while retaining indentation; it is not executable Python.

```markdown
::: syntax-template
for item in <collection>:
    <body>
:::
```

Give real code examples descriptive prose or an H3 heading outside the block. Do not use long explanatory comments as titles inside code. Preserve meaningful emphasis with `**bold**` and `*italics*`, but do not carry over formatting that was only structural in an old Word document. Write notes and warnings as blockquotes, for example `> **Important:** ...`; use a real heading such as `### Common errors` for common-error material. Exercises are flexible normal Markdown beneath `# Exercises`.

## Output-specific material

Use these exact wrappers on their own lines. Unmarked material appears in both outputs.

```markdown
<!-- handout-only:start -->
This appears in the PDF handout only.
<!-- handout-only:end -->

<!-- web-only:start -->
This appears in web output only.
<!-- web-only:end -->
```

Wrappers cannot overlap or nest. The current build produces PDFs; web integration will be added separately.

## Building and checking

Run `python tools/build_handouts.py validate sessions/week-01.md` to validate one source, `python tools/build_handouts.py build sessions/week-01.md` to produce `build/week-01.pdf`, and `python tools/build_handouts.py build-all` for every Markdown source under `sessions/`. `build` and `build-all` validate before rendering. Pandoc and WeasyPrint are required only for PDF rendering.

When a particular handout must contain certain non-empty major sections, declare that expectation at invocation time, for example: `python tools/build_handouts.py validate sessions/week-01.md --require-major Definitions --require-major Topics`.
