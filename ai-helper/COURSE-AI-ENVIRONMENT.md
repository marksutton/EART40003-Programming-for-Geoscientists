# Course environment briefing for an AI tutor

**Module:** Programming for Geoscientists (EART40003 / ESE 40003; both codes are used)
**Environment:** Thonny 5.0.0 with the ESE Teaching Tools plug-in
(`thonny-teaching-tools` 1.0.1)
**Repository revision inspected:** `eb84cdd`
**Date inspected:** 2026-09-27

Imported from the briefing prepared by the agent working in the Thonny plug-in
repository. Verification labels and test results below describe that agent's
inspection, not an independent verification in this repository. This copy
incorporates the module coordinator's decisions of 2026-09-27 (§8).

This document describes a **customised** Thonny. Several behaviours below differ
from stock Thonny and from ordinary Python at a terminal. Advice that is correct
for generic Python may be wrong here; §7 lists the specific traps.

Status of each claim is marked:
**[V]** verified (by running code, reading installed source, or the repository's
own recorded test results) · **[I]** intended, implemented, but not directly
observed by the author of this document · **[?]** unknown.

---

## 1. Environment and installation

### Versions

| Component | Version | Notes |
|---|---|---|
| Thonny | **5.0.0** | Pinned. Students install the copy distributed with the course, not the current release from thonny.org. **[V]** |
| Python (student code) | **3.14.4** | Bundled inside Thonny; students do **not** install Python separately. **[V]** |
| Plug-in | **thonny-teaching-tools 1.0.1** | **[V]** |
| Ruff | **0.16.7** exactly | Pinned to an exact version, not a range. **[V]** |
| Pillow | ≥ 9 | **[V]** |

The plug-in's own metadata permits `thonny>=5,<6` and Python ≥ 3.9
(`pyproject.toml:10,24`). Treat that as the theoretical floor, **not** as
support: the only configuration tested and distributed is Thonny 5.0.0 with its
bundled Python 3.14.4. If a student reports a different Python version, they are
probably not running Thonny's own interpreter (see §2).

### Operating systems

| Platform | Status |
|---|---|
| Windows x86-64 | Supported; fresh install fully tested 2026-09-25 **[V]** |
| macOS Apple Silicon | Supported; fully tested 2026-09-23 **[V]** |
| macOS Intel | Best effort; never tested **[?]** |
| Linux | Not supported by the course **[?]** |

Behaviour is the same on Windows and macOS. The differences students will meet
are conventional platform ones, not plug-in ones:

* **Options** is `Tools → Options...` on both, and on macOS **also**
  `Thonny → Settings` / <kbd>⌘,</kbd> **[V]** (`workbench.py:614-615`).
* Windows may show a blue "Windows protected your PC" SmartScreen box during
  installation — expected, because the installer is unsigned.

### Installation

Students receive **two files** from ESESIS: the Thonny installer, and the
plug-in as a `.whl` file. The plug-in is **not** on PyPI and cannot be found by
searching. The procedure is in the course's own setup guide (see §8); in short:

1. Run the Thonny installer, accept defaults, and launch Thonny once. At first
   launch, leave language on **English (US)** and settings on **Standard**.
2. `Tools → Manage plug-ins...` → click **here** under *Install from local
   file* → choose the downloaded `thonny_teaching_tools-…-py3-none-any.whl`.
3. **Restart Thonny.** Plug-ins load only at startup.

> **This is the single most important installation fact.** The plug-in must be
> installed through **Manage plug-ins**, *not* **Manage packages**. The two
> menu items sit together, look almost identical, and both report success — but
> `Manage packages` installs into the interpreter that runs student code, where
> the plug-in has no effect whatsoever. Thonny then discards the failure
> silently (`workbench.py:397-401` catches `ImportError` and does nothing), so
> there is no error message anywhere. **[V]** This mistake has occurred in
> practice.

Installing requires **internet access**: even from a local `.whl`, pip fetches
Ruff and Pillow from PyPI. **[V]**

### Confirming the plug-in is installed and active

In order of reliability:

1. **A `Code Check` tab appears beside `Shell`** at the bottom of the window.
   This is the course's own acceptance check. **[V]**
2. `Tools → Options → Code Check` exists, and shows the plug-in version at the
   bottom of the page. **[V]** Ask for this version in any support exchange.
3. For a definitive answer, `Tools → Open Thonny data folder...` and open
   `frontend.log`. A working install logs a line containing
   `thonny-teaching-tools 1.0.1 loaded`. **[V]** Its **absence** means the
   plug-in did not load — most often the `Manage packages` mistake above.

If a student reports "installed but nothing appears", 3 distinguishes "did not
load" from "loaded but misbehaving" in one step.

### Course configuration applied automatically

The **first** time the plug-in runs on a machine it applies a set of
course-recommended settings, then never re-applies them automatically, so a
student's later changes are respected. A **Reset to course defaults** button on
`Tools → Options → Code Check` reapplies them on demand. **[V]**
(`course_defaults.py`)

Settings applied: Code Check profile = *Course*; check on open/switch/save = on;
check while typing = on; mark problems in editor = on; editor right margin =
80 columns; Assistant opens on errors = on, on warnings = off; Assistant's
Pylint = off; Assistant's MyPy = off; automatic calltips = on; automatic
completions = on; completion details = on.

Three of these differ from stock Thonny, so a student's environment will **not**
match generic Thonny documentation: automatic calltips and automatic
completions are **off** by default in stock Thonny (`plugins/calltip.py:154`,
`plugins/autocomplete.py:537`) but **on** here. **[V]**

No other setup is required. Students do not create virtual environments, set
`PATH`, or install Python, Ruff or Pillow themselves.

---

## 2. Running programs

### The basics

| Action | Control | Verified |
|---|---|---|
| Run the current script | <kbd>F5</kbd>, or <kbd>Ctrl</kbd>+<kbd>R</kbd> / <kbd>⌘</kbd>+<kbd>R</kbd>, or the **Run** toolbar button | **[V]** `running.py:174-186` |
| Interrupt a running program | <kbd>Ctrl</kbd>+<kbd>C</kbd>, or `Run → Interrupt execution` | **[V]** `running.py:87,214-224` |
| Stop and restart the interpreter | <kbd>Ctrl</kbd>+<kbd>F2</kbd>, or `Run → Stop/Restart backend` | **[V]** |
| Auto-complete | <kbd>Ctrl</kbd>+<kbd>Space</kbd> | **[V]** `plugins/autocomplete.py` |
| Focus the editor / the Shell | <kbd>Alt</kbd>+<kbd>E</kbd> / <kbd>Alt</kbd>+<kbd>S</kbd> | **[V]** |

Opening and saving are conventional (`File` menu, <kbd>Ctrl</kbd>+<kbd>S</kbd>).
Re-running is simply pressing **Run** again; Thonny restarts the interpreter
first, so no state survives between runs unless the program recreates it.

A program does **not** have to be saved to be run — Thonny permits running
unsaved editor content (`run.allow_running_unnamed_programs` defaults true,
`running.py:134`). **[V]** Code Check also works on an unsaved buffer. **[V]**

### Editor, Shell, and interpreter

The **editor** holds the program text. The **Shell** is both the output area and
a live Python prompt attached to the **same** interpreter that runs the script.
After a run finishes, the Shell prompt can inspect variables the program left
behind — a genuinely useful debugging move to suggest.

Student code runs in a **separate process** from Thonny's own interface. This
matters more than it sounds and explains several things at once:

* `input()` is typed **into the Shell**, not into the editor.
* Thonny's interface cannot be broken by a student's program.
* Packages for student code (NumPy, matplotlib) are installed with
  `Tools → Manage packages...`; plug-ins that extend Thonny itself are installed
  with `Tools → Manage plug-ins...`. **These are different environments.** A
  library installed in the wrong one appears to install successfully and then is
  not found. **[V]**

The status bar bottom-right shows the interpreter in use; the course expects
**Local Python 3 · Thonny's Python**. It can be changed at
`Tools → Options → Interpreter`, but on this course it should not be — a student
who has pointed Thonny at a separate Python installation will lose access to
whatever they installed through `Manage packages`. **[I]**

### Working directory and relative paths

When a script is run, Thonny changes the working directory to **the folder
containing that script** (`run.auto_cd` defaults true, `running.py:135,479-480`).
**[V]**

So `open("data.csv")` finds a file sitting beside the `.py` file. This is the
single most common source of confusion with file paths, and the advice follows
from it:

* Keep the data file in the same folder as the program.
* To check, have the student run `import os; print(os.getcwd())` — in the
  script, or at the Shell prompt after a run.
* The Shell echoes a `%cd` line whenever the directory actually changes
  (`running.py:362-374`) **[V]** — a useful thing to ask a student to read back.

An **unsaved** program has no folder, so relative paths have nowhere sensible to
resolve from. "Save the file first, into the same folder as the data" fixes a
surprising proportion of file-not-found problems. **[I]**

### What the plug-in changes about normal operation

Only one thing affects running: **matplotlib plots are redirected into a Plots
panel instead of opening separate windows** (§5). Running, stopping, the Shell
and the interpreter are otherwise stock Thonny.

---

## 3. Debugging

### Starting a debugger

Thonny has two debuggers. **[V]** (`plugins/debugger.py:1288-1330`)

| Mode | Control |
|---|---|
| Debug current script (nicer) | <kbd>Ctrl</kbd>+<kbd>F5</kbd> |
| Debug current script (faster) | <kbd>Shift</kbd>+<kbd>F5</kbd> |
| **Debug** toolbar button | Runs whichever is preferred — **"nicer"** by default |

The "nicer" debugger visualises expression evaluation step by step, which is the
one worth teaching; "faster" behaves more like a conventional debugger.

### Breakpoints, stepping, variables

* **Set a breakpoint** by clicking in the **line-number gutter** to the left of
  the code. The line number turns crimson. Click again to remove.
  **[V]** (`codeview.py:171-176`)
* **Step over** <kbd>F6</kbd>, **Step into** <kbd>F7</kbd>. **Step out** exists
  on the `Run` menu but has **no default keyboard shortcut**. **[V]**
* **Run to cursor** <kbd>Ctrl</kbd>+<kbd>F8</kbd>; **Step back**
  <kbd>Ctrl</kbd>+<kbd>B</kbd> / <kbd>⌘</kbd>+<kbd>B</kbd> (nicer debugger).
  **[V]**
* **Resume** continues to the next breakpoint (the toolbar button changes to
  *Resume* while paused). **[V]**

### Plug-in feature: the Type column

The plug-in adds a **`Type` column** showing each variable's real runtime type
(`int`, `str`, `list`, `numpy.ndarray`, …) — not a guess, but the actual type
from the running program. It appears in **two** places: **[V]**

1. The docked **Variables** pane, refreshed after each run and each debugger
   step.
2. The debugger's **floating "Local variables" window**.

The floating window matters: `debugger.frames_in_separate_windows` defaults to
**true** in standard mode (`plugins/debugger.py:1289-1291`) **[V]**, so a
stepping student sees their locals in that floating box, *not* the docked pane.
If a tutor tells a student to "look at the Variables pane" while they are
stepping, they may be looking at the wrong thing entirely.

The Type column is worth using for teaching: `"5"` versus `5`, or a list versus
a NumPy array, become visible rather than inferred.

### Stopping an infinite loop or a stuck program

In order of escalation:

1. <kbd>Ctrl</kbd>+<kbd>C</kbd>, or `Run → Interrupt execution`.
2. <kbd>Ctrl</kbd>+<kbd>F2</kbd> (`Stop/Restart backend`) — kills and restarts
   the interpreter. All variables are lost; the editor is untouched.
3. Close and reopen Thonny.

A program waiting at `input()` looks identical to a hung program. Check whether
the Shell is waiting for typed input **before** suggesting an interrupt — this
is a common misdiagnosis.

### Limitations

Code Check does not run during debugging, and provides no debugger integration.
It analyses code without executing it, so it cannot see runtime values. **[I]**

---

## 4. Editor assistance

### Autocomplete and calltips

Both are **on** by default here, unlike stock Thonny (§1). Suggestions appear as
the student types; <kbd>Ctrl</kbd>+<kbd>Space</kbd> requests them explicitly.
**[V]** Calltips show a function's parameters while typing a call.

### Code Check (linting)

Checking is performed by **Ruff 0.16.7**, run over the buffer the student is
looking at — saved or not. **[V]** The messages shown are **not** raw Ruff
output: the plug-in rewrites them into teaching-oriented wording. "math is
imported but never used" is the plug-in's phrasing, not Ruff's. **[V]**

**When it runs** (all automatic, no button needed): **[V]**

* about **1 second** after the student stops typing (`IDLE_DELAY_MS = 1000`);
* shortly after a file is opened, switched to, or saved
  (`FILE_EVENT_DELAY_MS = 200`);
* on demand via the **Check now** button in the pane's own status bar.

**What it checks.** The course profile contains **152 rules** **[V]**, drawn from
a catalogue of three profiles — Essential (58), Course (152), Full (365) —
selectable at `Tools → Options → Code Check`. It enforces a **80-column** line
length, matching the editor's right margin. **[V]**

The tutor should understand the differences between these profiles, but
encourage students to leave the **Course** setting unchanged. Do not suggest
switching profiles to suppress feedback; follow the module coordinator's
instructions if a change is needed.

**How results appear.** Two places, simultaneously:

* the **Code Check pane**, one row per problem, with a coloured severity swatch;
  clicking a row jumps to that line and shows a fuller explanation beneath;
* **underlines in the editor itself**, coloured by seriousness — red for code
  Python cannot parse, orange for likely bugs, goldenrod for taught style, grey
  for the rest. **[V]**

The underlines keep working even if the Code Check pane is closed. **[V]**

### The three kinds of problem — a critical distinction

This is the distinction a tutor most needs to keep straight, and it was verified
directly by running the checker:

| Kind | Example | Does Code Check see it? |
|---|---|---|
| **Style / quality** | `import math` unused; `x=1` missing spaces; `print( x )` | **Yes** — 4 diagnostics on that example **[V]** |
| **Syntax error** | `def f(:` | **Yes**, reported as `invalid-syntax`, most severe, red **[V]** |
| **Runtime error** | `x = 1 / 0` | **No — zero diagnostics.** **[V]** |

**Code Check cannot predict runtime errors.** A `ZeroDivisionError`,
`FileNotFoundError`, `IndexError` or a wrong numerical answer will pass Code
Check silently. "The Code Check pane is empty, so my program is correct" is a
misconception worth correcting early: an empty pane means *no style or syntax
problems were found*, nothing more.

Conversely, a style warning is **not** an error — the program runs perfectly
well with unused imports and irregular spacing. Students who treat every
underline as a bug get stuck; those who ignore the red ones stay stuck.

Runtime errors surface as a **traceback in the Shell**, and Thonny's separate
**Assistant** pane opens automatically to help interpret them (a stock Thonny
feature, deliberately left on).

---

## 5. Plotting and images

The plug-in substantially changes matplotlib's behaviour. A tutor unaware of
this will give wrong advice.

### What happens on `plt.show()`

Thonny's interpreter is switched to matplotlib's **Agg** (non-interactive)
backend. When a student calls `plt.show()`: **[V]** for the mechanism as
implemented; **[I]** for end-to-end behaviour, per the repository's recorded
tests

* **no separate window opens**;
* the figure appears in a **Plots** panel docked inside Thonny;
* **`plt.show()` returns immediately — it does not block.** The program keeps
  running and finishes normally.

This last point is the important one. In ordinary Python, `plt.show()` blocks
until the window is closed, and a great deal of standard advice is built on that
assumption. Here:

* `plt.show()` at the end of a script is **not** required to keep a window open,
  and does not pause anything;
* advice such as "use `plt.ion()`", "call `plt.show(block=False)`", "add
  `plt.pause()`", or "the window will stay open until you close it" is **wrong
  or pointless** in this environment;
* a figure the student builds but never calls `show()` on is **still captured**
  at the end of the run, so it appears anyway. **[I]**

### Multiple plots and repeated runs

* Each `show()` hands over the figures currently open and then closes them, so a
  later `plt.plot()` starts a fresh figure rather than silently adding to the
  old one. **[V]** (mechanism in `thonnycontrib/backend/teaching_tools_plots.py`)
* Plots **accumulate across runs** — they are not cleared when a program is
  re-run. Students viewing an old plot and believing it is the new one is a
  predictable confusion; the position indicator (e.g. `3 of 7`) tells them where
  they are.
* The panel retains at most **100** plots, discarding oldest first. **[V]**
* The panel opens itself the first time a plot arrives, even if the student has
  never opened it. **[V]**

### Controls in the Plots panel

**[V]** (`plots_view.py`)

* **< Prev** / **Next >** with an `n of m` position indicator
* **Zoom −** / **Zoom +** stepping 25 / 50 / 75 / 100 / 150 / 200 / 300 / 400 %
* **Fit** checkbox — on by default, rescales as the pane is resized, and
  disables the manual zoom buttons while ticked
* **Save...** (one plot) / **Save all...** (a folder) — PNG
* **Delete** / **Delete all**

There is **no copy-to-clipboard button**, deliberately. If a student needs a
plot in a report, the answer is **Save...**. **[V]**

### Other images

The Plots panel handles matplotlib figures only. Pillow's `Image.show()` and
other image-display routes are **not** redirected and are not part of the course
environment. **[?]**

---

## 6. Common problems

| Symptom | Likely cause | How to check | Next step |
|---|---|---|---|
| No `Code Check` tab after installing | Not restarted, or installed via **Manage packages** instead of **Manage plug-ins** | Restart first. Then `Tools → Manage packages...` — is `thonny-teaching-tools` listed *there*? | If listed under packages, remove it and reinstall via `Manage plug-ins... → Install from local file`. Otherwise check `frontend.log` for `thonny-teaching-tools … loaded` |
| Install failed, or mentioned a network problem | pip could not reach PyPI for Ruff/Pillow | Ask what the progress box said | Retry on a different network |
| `"Already installed with the same version"` | The same version is already present | Compare the version in the filename with `Tools → Options → Code Check` | Nothing to do, unless a *newer* file was expected — then download it again |
| Plots panel stays empty | matplotlib not installed, or installed into the wrong environment | `Tools → Manage packages...` — is `matplotlib` listed? | Install it there (**not** via Manage plug-ins) |
| `ModuleNotFoundError` for a library the student installed | Installed via `Manage plug-ins`, or into a different interpreter | `Tools → Manage packages...` for the listing; check interpreter in the status bar | Reinstall via `Manage packages`; confirm interpreter is Thonny's own |
| `FileNotFoundError` on a data file | Working directory is the **script's** folder; file elsewhere, or script unsaved | `import os; print(os.getcwd())` | Save the script into the same folder as the data |
| Program appears frozen | Waiting at `input()`, or an infinite loop | Is the Shell awaiting input? | Type the input; otherwise <kbd>Ctrl</kbd>+<kbd>C</kbd>, then <kbd>Ctrl</kbd>+<kbd>F2</kbd> |
| Variables pane empty while debugging | Locals are in the **floating** frame window, not the docked pane | Look for the separate "Local variables" window | Read values there; the `Type` column is present in both |
| Plot looks wrong / is an old one | Plots accumulate across runs | Read the `n of m` indicator | **Next >** to the newest, or **Delete all** and re-run |
| Boxes (□□□) instead of Chinese text in a plot | matplotlib's default font has no CJK glyphs | Are the labels non-Latin? | Use English labels, or set a CJK font in `matplotlib.rcParams` |
| Code Check finds nothing but the program crashes | Working as designed — runtime errors are invisible to it | Read the Shell traceback | Debug the runtime error; see §4 |

### Evidence to request when the cause is unclear

1. The plug-in version, from `Tools → Options → Code Check`.
2. Operating system.
3. The **exact** text of any error, and the full Shell traceback.
4. Whether the file is saved, and where it sits relative to any data file.
5. For install problems, `frontend.log` via `Tools → Open Thonny data folder...`.

---

## 7. Guidance for the tutor

### Generic advice that is wrong here

* **"Install Python from python.org", "use pip from the command line", "create a
  virtual environment", "activate your venv."** None apply. Python is inside
  Thonny; packages go through `Tools → Manage packages...`; there is no command
  line in this workflow.
* **"Run `pip install ruff`."** Ruff is supplied at an exact pinned version by
  the plug-in. A student installing another copy could change the feedback they
  get.
* **Anything premised on `plt.show()` blocking** — `plt.ion()`,
  `show(block=False)`, `plt.pause()`, "close the window to continue". See §5.
* **"Your editor's linter…"** — the checker is Ruff with a course-specific rule
  set and rewritten messages. It is not Pylint, not Flake8, and not PyCharm's
  inspector. Pylint and MyPy are deliberately **off**.
* **"An empty problems list means your code is correct."** It means no style or
  syntax problems. Runtime errors are invisible to it (§4).
* **"Look at the Variables pane"** while the student is *stepping* — they are
  probably looking at the floating frame window (§3).
* **Menu paths from Thonny's online documentation** may not match: this Thonny
  has extra panes, and several defaults differ from stock (§1).

### Useful things students can do themselves

* `print(type(x))`, or simply read the **Type** column.
* `import os; print(os.getcwd())` when a file will not open.
* Use the Shell prompt *after* a run to inspect what the program left behind.
* Click a Code Check row to jump to the line and read the fuller explanation.
* Set a breakpoint in the gutter and step with <kbd>F6</kbd>/<kbd>F7</kbd>.
* <kbd>Ctrl</kbd>+<kbd>F2</kbd> to get back to a clean interpreter.

### When to refer to teaching staff

For suspected plug-in faults or unresolved environment problems, ask students
to contact **the module coordinator (Mark Sutton)** by email. Do not invent an
email address; use the contact details supplied through the course.

* The plug-in will not install, or `Code Check` never appears after a restart
  and reinstall.
* Anything suggesting a damaged Thonny installation, or a changed interpreter
  the student cannot restore.
* Suspected faults in the plug-in itself — wrong or confusing Code Check
  messages, plots not appearing, incorrect types — these are course-maintained
  software and should be reported, not worked around.
* Assessment, marks, deadlines, and permitted use of AI are covered separately.
  Follow the supplied course policy; refer unresolved questions to the module
  coordinator. **No policy on those is stated in this document, and none should
  be inferred.**

---

## 8. Evidence and uncertainty

### What was inspected

Repository at revision `eb84cdd`, plug-in version 1.0.1, on 2026-09-27;
Thonny 5.0.0's own installed source; and the course setup guide
`ThonnySetup.pdf`.

### What was actively verified on 2026-09-27

* Ruff 0.16.7 run through the plug-in's own code paths on three samples,
  confirming the style / syntax / runtime distinction in §4 — including that
  `x = 1 / 0` yields **zero** diagnostics.
* Profile sizes (58 / 152 / 365 rules), default profile `course`, line length 80.
* The repository's test suite: **53 tests, all passing**.
* Menu labels, keyboard shortcuts, and default settings quoted in §§2–4, read
  from Thonny 5.0.0's installed source rather than from general knowledge.

### Recorded in the repository, not re-verified here

* Full manual passes on macOS Apple Silicon (2026-09-23) and a clean Windows
  x86-64 machine (2026-09-25), both reported as passing.
* Plots behaviour end to end against a live matplotlib backend (recorded under
  ADR-025).

Items marked **[I]** above are implemented and documented, but not observed
running by the author of this document.

### Known unknowns

* **macOS Intel** — never tested.
* **The college teaching network** — installation needs PyPI access for Ruff and
  Pillow, and had not been tested on the teaching network at the time of
  writing. A test on college-imaged machines was scheduled for early October
  2026.
* **Pillow / NumPy image display** outside matplotlib — not part of the tested
  environment.

### A note on citations

Source references are given as file paths with line numbers rather than URLs.
The repository is **internal** to Imperial College London, so links would not
resolve for readers of the published version of this document. Paths are
relative to the plug-in repository, except those named as Thonny's own
(`workbench.py`, `running.py`, `plugins/…`), which are in the installed Thonny
5.0.0 package. Line numbers are accurate at revision `eb84cdd` and Thonny 5.0.0.

### Existing material worth including in the tutor pack

| Item | Location | Comment |
|---|---|---|
| **`ThonnySetup.pdf`** | Course materials (`26-27`) | The authoritative student setup guide. Annotated screenshots of the Tools menu, the plug-ins dialog, and the expected result. Already warns against `Manage packages`. **Recommended.** |
| `ThonnySetup.docx` | Course materials | Editable source of the above |
| `InstallingThonnyAndPython.docx` | Course materials | Confirmed obsolete by the module coordinator; not being distributed. **Exclude from the tutor pack.** |
| `docs/STUDENT_INSTALL.md` | Plug-in repository | Explicitly marked *not* the published instructions; retained as source material. Its worked example was verified against the real checker. Do **not** distribute as guidance |

**One caution before publishing.** A screenshot in `ThonnySetup.pdf` shows a
plug-ins dialog containing a personal filesystem path beginning
`C:\Users\<name>\…`. It is innocuous, but the brief for this document excludes
personal paths from public material — worth a glance before the PDF goes into a
public tutor pack.

### Course organiser decisions (2026-09-27)

1. **Module code.** Both **ESE 40003** and **EART40003** are used for this
   course; the difference does not need resolving.
2. **Old installation guide.** `InstallingThonnyAndPython.docx` is not current
   and is not being distributed. Do not include it in the tutor pack.
3. **Code Check profiles.** The tutor should understand Essential / Course /
   Full, but encourage students not to change the course setting (§4).
4. **Assessment and permitted AI use.** These are covered elsewhere; this
   environment briefing does not define policy.
5. **Fault reporting.** Students should email **the module coordinator
   (Mark Sutton)** about suspected faults.
6. **Updates during term.** No routine plug-in changes are planned; updates
   are expected only if a problem is found. If an update is issued, refresh
   this briefing's version details and the tutor pack to match.
