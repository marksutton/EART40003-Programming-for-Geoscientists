# Teaching guidance from practicals and lectures

## Status and source precedence

Derived from Mark's `PracticalsAndSlides.zip`, reviewed on 2026-09-27:
eight practical PDFs and eight lecture-slide PDFs, 170 pages in total.
Mark confirmed that these are previous-year files and will be updated as the
course proceeds, but their teaching content will not change. They can therefore
inform the tutor now; updated files are not a prerequisite.

This is a digest of teaching intent, not a replacement practical sheet or a
solution bank. **Do not include the supplied PDFs, archive, extracted text or
page images in the tutor website or backup ZIP.** Only derived guidance belongs
in the package. Local review copies are under ignored `build/`.

Use the following sources for their respective purposes:

- [Canonical sessions](../sessions/): current reference explanations and approved
  corrections. Old slides and demonstrations must not undo those corrections.
- [Environment briefing](COURSE-AI-ENVIRONMENT.md): current Thonny setup,
  debugging controls, linting and plotting behaviour, overriding old Spyder advice.
- [2026 timetable](SESSION-SCHEDULE.md): likely coverage to date, not old PDF
  dates or filenames. Student-stated progress takes precedence.
- This digest: classroom sequence, exercise intent and teaching approach.
- Separately supplied current assessment guidance: policy, deadlines, submission
  requirements and assessment arrangements. Do not derive these from old slides.

If a student's current exercise sheet differs from this digest, use their current
sheet for task requirements. Ask for the relevant excerpt where necessary.

## How to help

These recommendations combine the teaching approach evident throughout the
materials with Mark's requested learning-first tutor behaviour.

1. Establish the exercise and the student's intended result. For debugging,
   ask for relevant code, the exact error or unexpected output, and what they
   have already tried. Do not demand all of this for a simple conceptual question.
2. Help the student state a small algorithm in plain English. Identify what
   each variable represents, its type, and any units before writing expressions.
3. Work on one small step at a time. Get a basic case working, check intermediate
   results, then add the next step. Avoid supplying an entire finished program
   or a complete exercise algorithm by default.
4. Ask the student to predict the next value or branch, then check it by stepping
   in Thonny, inspecting variables and types, or using a temporary trace print.
   Locate the first point where expectation and execution diverge.
5. Explain errors directly and give proportionate hints. A short illustrative
   example can help; prefer an analogous example to solving the student's whole
   task. Do not turn every factual explanation into a guessing game.
6. Test against the specified examples, boundary cases and independent
   calculations. Plausibility and units matter in scientific code. Passing the
   linter is not evidence that a calculation or algorithm is correct.
7. Encourage readable intermediate variables, consistent descriptive names,
   spacing between logical sections, and comments explaining purpose or tricky
   decisions. Address course Code Check feedback without changing its profile.
   Compactness and clever one-liners are not goals in themselves.
8. Respect exercise constraints: practising a loop, slicing or manual file
   processing is often the point. Do not bypass that learning with a library call.
   Conversely, do not add unrequested validation or abstractions that obscure
   the current task. Explain optional improvements as optional.
9. Help students seek human support when stuck rather than continuing to guess.
   For suspected environment faults, direct them to email the module coordinator
   (Mark Sutton), following the environment briefing.

The course assumes no prior programming experience and mixes pre-reading,
short lectures, demonstrations and practical work. Do not equate a topic missing
from the live slides with a topic absent from the course: some is in pre-reading.
Equally, an optional challenge being available does not make it required knowledge.

## Session-by-session teaching context

### Session 1: expressions, variables, inputs and output

Lecture focus: statements and function calls, arithmetic, variables, converting
formulae to programs, user input and f-string output.

Practical contexts: feet/inches conversion, ballistic height, compound interest,
and dinosaur speed from trackways. These move from a single expression to named
variables, user inputs and appropriately formatted output. Encourage checking
against a calculator or a physically plausible result, with consistent units and
appropriate decimal precision.

Optional extension: the egg-boiling formula deliberately requires looking up
an imported logarithm before imports are formally taught. Support that explicit
extension if requested; do not introduce imports as a prerequisite for everyone.

Evidence: practical pp. 1-3; slides pp. 2, 10-19, 21.

### Session 2: decisions, while loops and debugging

Practical contexts: geological-era classification, a nested coral decision tree,
a temperature-conversion table, and a mental-arithmetic practice program.
The Pi series is a harder extension, subordinate to getting the basic loop working.

Build one decision or loop stage, test it, then extend it. Encourage a placeholder
message for a branch not yet implemented. Trace the loop condition, counter and
running total independently; rejected inputs should not accidentally count as
accepted ones. Use `while` at this stage rather than jumping ahead to `for`.
Match the actual task's required output and input assumptions, without expanding
it into a production application.

Evidence: practical pp. 1-5; slides pp. 2-15. Practical pp. 6-7 also illustrate
readability expectations, but their grading and policy text is historical.

### Session 3: types, strings, methods and exceptions

Practical contexts: tidying a sentence, counting letters, and manually converting
hexadecimal input. The sentence exercise intentionally requires indexing/slicing
rather than an end-checking method. Letter counting practises numeric counters
and the course's ASCII-level use of `ord` and `chr`. Do not default to `Counter`,
regular expressions or other shortcuts that replace the intended practice.

The hexadecimal exercise explicitly excludes a ready-made whole-number conversion
function and requires exception handling. Encourage testing the basic conversion
before adding input checks. Negative/fractional hexadecimal is an advanced
extension, not the baseline. Use the corrected canonical floating-point explanation.

Evidence: practical pp. 1-3; slides pp. 2-18.

### Session 4: lists and for loops

Practical contexts: looking up Ordovician stages, building/searching a Fibonacci
list, and a planetary-gravity calculation using aligned lists.
Distinguish zero-based indices from human-readable positions. Trace one list
lookup and one pairwise calculation before scaling up with loops. Check unit
conversions and intermediate distances rather than hiding the calculation in a
single expression. Preserve the specified physical simplifications.

Lectures also cover split/join, nested lists and comprehensions. Comprehension
use is optional: ordinary loops are a suitable default, with concise notation
explained when encountered rather than imposed on a beginner.

Evidence: practical pp. 1-3; slides pp. 2-21.

### Session 5: modules, functions, scope and tuples

Practical contexts: a trigonometry table, functions counting words of a chosen
length and finding all maximum-value indices, then combining tested functions.
Further statistics exercises practise writing functions and returning multiple
values, not using statistics-library shortcuts.

Emphasise radians versus degrees, arguments versus return values, repeated
maxima versus only the first index, and independent function tests before
integration. Use explicit inputs and outputs rather than unnecessary globals.
Preserve the canonical optional caveat about mutating a list passed to a function.
Keyword arguments here do not require introducing `**kwargs`.

The time-module lookup is optional; the handout explicitly says reaching the
first simple custom-function exercise is acceptable. Later function composition
and statistics work provide more practice, not a reason to overwhelm a student.

Evidence: practical pp. 1-4; slides pp. 2-18. Slides pp. 19-27 contain historical
assessment information, not current instructions.

### Session 6: files, dictionaries and implementing a given algorithm

Practical contexts: comparing seismic-wave measurements against theoretical
values, and joining/filtering palaeobiological occurrence and interval data.
The first exercise particularly practises implementing a supplied algorithm.

Encourage the student to say exactly what the dictionary keys and values mean,
inspect a small raw input sample, distinguish headers from data, and convert
numeric text before calculation. Test a single parsed row and lookup before
processing a file. Pay attention to missing keys, blank fields, output spacing
and newline characters. Distinguish an occurrence from an aggregated genus.

Direct file methods and dictionaries are deliberate requirements of the supplied
data-wrangling task. Do not substitute pandas or another imported file reader.
The course teaches explicit `open`/`close`; do not insist on rewriting a student's
work with `with` merely for idiom. Sets are in the reference/pre-reading even
though not developed in the live lecture; do not require them to solve these tasks.

Evidence: practical pp. 1-6; slides pp. 2-11.

### Session 7: NumPy and images

Practical contexts: sampled arrays, vectorised square roots, slicing, Boolean
selection, and cropping/thresholding a greyscale rock-scan image with NumPy and
`PIL.Image`. Explain shapes and row/column indices; check small arrays or a small
region first. Keep sample count distinct from endpoint values and step size.
Check masks and the comparison boundary before modifying pixel values.

Optional challenges: finding microfossil centres and merging clusters of candidate
centres. Algorithm planning alone is valuable; do not introduce an advanced image
processing library as the default solution. Recursion is explicitly advanced and
optional in the canonical reference, not a prerequisite for the main practical.
Avoid naming student files `numpy.py`, which can shadow the imported module.

Evidence: practical pp. 1-4; slides pp. 2-8; canonical Session 7 recursion heading.

### Session 8: plotting scientific functions and data

Practical contexts: comparing three sine-based functions on shared axes, then
pie, bar and scatter plots from clast data. A stacked bar chart is optional.
Distinguish degrees used for an axis from radians used in calculations, and
distinguish squaring an argument from squaring the function's result.

Get data and basic graphs correct before decorating them. Check corresponding
x/y data, chart choice, labels, units, legends and useful ticks. Use the course's
`matplotlib.pyplot` approach and current Thonny Plots behaviour, not an unrelated
plotting framework or assumptions about blocking external windows.
Finish with student-directed revision of uncertain topics.

Evidence: practical p. 1; slides pp. 2-7, 12-14.

## Handling old material and ambiguities

- Ignore old headers, deadlines, exam dates/rooms, rules, marks and AI-policy
  statements for current administrative advice. No current assessment date has
  been established by these PDFs. Do not roll a 2025 deadline into 2026.
- Replace old Spyder/Variable Explorer/%reset/keyboard-shortcut advice with the
  current environment briefing, not a literal IDE-name substitution. Do not
  infer installed packages from the old Spyder distribution.
- Old examples are not authoritative over approved corrections, including
  floating-point comparisons, function scope and import advice. For example,
  `.3f` means three decimal places, despite the Session 1 slide's wording.
- Some slides refer to demonstration/solution files not present in `examples/`.
  Check availability before linking; do not invent files or imply solutions are
  included. Missing practical datasets do not prevent conceptual tutoring, but
  do not invent their contents or claim to have run a student's full dataset.
- If an exercise contains contradictory examples or counts, explain the specific
  ambiguity and ask for clarification rather than silently choosing a new task.
  Examples in these old sheets include the seeded Fibonacci list versus the
  stated iteration count (Session 4), a word-frequency example (Session 5),
  inconsistent numerical ages beside the sample output (Session 6), and the
  point count for an inclusive sampled interval (Session 7). These are review
  observations, not approved changes to source material.

## Source inventory (not package attachments)

Page references above are PDF page numbers, starting at 1. Text was extracted
from all pages; selected visual pages were also checked for image-only content,
formulae, annotated style guidance and plot context. This was a pedagogical
review, not a full mathematical or code correctness audit.

| Session | Practical PDF (pages) | Lecture PDF (pages) |
|---|---|---|
| 1 | `Python-1-Practicals.pdf` (3) | `Python1-Slides-Colour.pdf` (21) |
| 2 | `Python-2-Practical-and-assignment.pdf` (7) | `Python-2-Slides_Colour.pdf` (17) |
| 3 | `Python-3-Practical.pdf` (3) | `Python-3-Slides-Colour.pdf` (18) |
| 4 | `Python-4-Practical-and-assignment.pdf` (4) | `Python-4-Slides-Colour.pdf` (22) |
| 5 | `Session_5_PracticalLinkFixed.pdf` (4) | `Python-5-Slides-Colour.pdf` (27) |
| 6 | `Session_6_PracticalAndAssignment.pdf` (6) | `Python-6-Slides-Colour.pdf` (11) |
| 7 | `Session_7_Practical.pdf` (4) | `Python-7-Slides-Colour.pdf` (8) |
| 8 | `Session_8_Practical.pdf` (1) | `Python-8-Slides-Colour.pdf` (14) |
