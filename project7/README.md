# Project 7 - Break it on purpose

Two exercises: measure your loop's cost, then deliberately sabotage it
and diagnose the failure using only what it left behind - the spine.

## Files

- `src/app.py`, `src/utils.py` - sample source files (same as Project 3)
- `scan_progress.py` - Project 3's loop, now with proper error handling built in
- `progress.md` - the spine, seeded with one earlier run
- `measure_cost.py` - Part A: estimates token cost per beat and monthly cost

## Part A - Measure the cost

Since this loop is a deterministic script (no AI model call), its real
cost is $0. But most loops in the course call an agent every beat, so
here's how you'd measure it if this one did:

```bash
py measure_cost.py
```

This estimates tokens from the actual file sizes involved (progress.md
+ source files), then applies the course's example pricing ($3 per
million input tokens, $15 per million output tokens) at a few
different schedules. Compare the "weekdays" number with the "every
hour" number - this is Concept 13's lesson: frequency drives cost far
more than the task itself.

## Part B - Sabotage it

**Step 1 - See the working version:**

```bash
py scan_progress.py
```

Should say "no new TODOs" (or find new ones, depending on progress.md).

**Step 2 - Break it.** Open `scan_progress.py` and change this line:

```python
SRC = os.path.join(ROOT, "src")
```

to:

```python
SRC = os.path.join(ROOT, "srcc")   # deliberate typo
```

**Step 3 - Run it and watch it fail LOUDLY (this version already has
the fix built in):**

```bash
py scan_progress.py
```

You should see:

```
ERROR: Expected source folder not found: .../srcc

progress.md updated with a clear failure note.
```

**Step 4 - Diagnose from the spine alone.** Without looking at the
code or re-running anything, open `progress.md` and look at the last
line of the Run log. It should clearly say what failed and when:

```
- 2026-09-11: FAILED - Expected source folder not found: .../srcc - NEEDS A HUMAN
```

That's the whole exercise: you can tell exactly what broke, and when,
from one file.

## What would have happened without the fix

If you remove the `try/except` block and the `isdir` check from
`find_todos()`, and run the sabotaged version, it does NOT crash.
`os.walk()` on a folder that doesn't exist just returns nothing, so
the script happily reports "No new TODOs since last run" - a
completely normal-looking success message. That entry in `progress.md`
would be indistinguishable from a genuine day with no new TODOs. This
is a **silent failure**, and it's the dangerous kind: nobody would
notice for weeks.

The fix here is one `if not os.path.isdir(SRC): raise ...` check. That
single check is the difference between a loop that tells you it's
broken and one that quietly stops doing its job forever.

## Reset before running again

```bash
git checkout -- scan_progress.py    # if this is a git repo, restores the working version
```

Or just re-download `scan_progress.py` from here.
