"""Small regression tests for the handout validator (standard library only)."""

import tempfile
import unittest
from pathlib import Path

import build_handouts


class HandoutValidationTests(unittest.TestCase):
    def write(self, directory: Path, name: str, content: str) -> Path:
        path = directory / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_semantic_blocks_and_image(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory / "diagram.png").write_bytes(b"not a rendered image, but it exists")
            source = self.write(directory, "week.md", """# Topics

![Diagram](diagram.png)

```python
# <!-- handout-only:start --> is an ordinary Python comment here
for number in range(3):
    print(number)
```

```python-invalid
if broken
```

::: syntax-template
for item in <collection>:
    <body>
:::
""")
            self.assertEqual(build_handouts.validate(source, {"Topics"}).errors, [])

    def test_non_exact_wrapper_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = self.write(Path(temporary), "week.md", "# Topics\n<!-- handout-only:start --> trailing\n")
            errors = build_handouts.validate(source, set()).errors
            self.assertTrue(any("malformed output wrapper" in error for error in errors))

    def test_malformed_wrapper_and_invalid_python_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = self.write(Path(temporary), "week.md", """# Topics

<!-- handout-only:start -->
```python
if broken
```
""")
            errors = build_handouts.validate(source, set()).errors
            self.assertTrue(any("unclosed handout-only" in error for error in errors))
            self.assertTrue(any("invalid python fence" in error for error in errors))

    def test_duplicate_and_missing_major_headings_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = self.write(Path(temporary), "week.md", "# Topics\n# Topics\n")
            errors = build_handouts.validate(source, {"Definitions"}).errors
            self.assertTrue(any("duplicate H1" in error for error in errors))
            self.assertTrue(any("missing required H1" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
