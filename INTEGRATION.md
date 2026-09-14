# Cumulative website integration

The Markdown files in `sessions/` are the canonical record of the material taught each week. The website in `docs/` is a cumulative student reference organised by concept, not by session number. It starts with Session 1 and grows only as approved sessions are integrated. The previous whole-course site is retained in `legacy-site/` as an archive, not as publishing source or integration input. This guide governs semantic integration; the small tools only filter source material and check objective properties.

## Inputs and preparation

An integration run uses one approved canonical session, the current clean `docs/` website, and this guide. Start by producing its inventory:

```powershell
python tools/session_inventory.py sessions/session-01.md
```

Use `--view` when the filtered Markdown itself is useful. The helper removes Exercises and handout-only blocks, while retaining shared and web-only material. It is an inspection aid, not an automatic publishing pipeline.

## Editorial rules

- Integrate material by concept, not by session number.
- Preserve existing website material unless the session clearly extends, clarifies, or supersedes it. Make the minimum edits needed.
- Extend an existing concept page when it belongs naturally there. Create a page only for a substantial student-facing concept that merits direct navigation.
- Do not reorganise pages merely for tidier taxonomy or stylistic consistency. Do not expose future-session content.
- Omit exercises and handout-only content by default. Include shared and web-only content where it helps the reference.
- Avoid duplicate explanations. If source and site conflict, report the conflict rather than silently choosing between them.
- Preserve Mark's pared-down first-year model. Do not add technical machinery solely for completeness.
- Add cross-links only when they genuinely improve novice navigation or understanding.

A student should reasonably expect to look up a whole page's subject directly. Individual methods rarely need pages of their own; substantial subjects such as lists, dictionaries, sets, loops, NumPy arrays/vectorization, and Matplotlib do. Page length is only a prompt to check conceptual coherence, not a mechanical split/merge rule.

## Validation and review

After semantic edits, run:

```powershell
python tools/validate_website.py
```

The checker verifies local Markdown links and images, basic heading structure, ordinary Python fences, absence of Exercises and handout-only wrappers, and the presence of `docs/index.md`. Warnings require judgement; errors must be resolved before review.

For every integration, provide a concise report before committing:

```markdown
Integrated: Session N

Pages modified:
- ...

New material / existing material extended:
- ...

Cross-links added:
- ...

Not integrated:
- exercises
- repeated material

Potential conflicts / decisions:
- ...
```

Then show the relevant diff and validation result. Do **not** commit a semantic website integration until Mark has approved it. The integration should be idempotent: repeating an already integrated session should make no substantive further changes. There is intentionally no integration database or automatic semantic merge engine.
