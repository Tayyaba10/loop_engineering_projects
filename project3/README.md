# Project 3 - Scheduled loop with memory (the spine)

This project simulates a scheduled loop: a beat that would normally run
once a day (via cron or Task Scheduler), reads its memory file first,
finds what's new in the repo, and updates its memory.

## Files

- `src/app.py`, `src/utils.py` - sample source files with a few `TODO` comments
- `scan_progress.py` - the loop's body (one beat): reads `progress.md`, scans for TODOs, reports only what's new, updates `progress.md`
- `progress.md` - gets created automatically on first run. This is the spine.

## How to run it

```bash
py scan_progress.py
```

(use `python3 scan_progress.py` on Mac/Linux)

## Prove the spine works - run it twice

**First run** (progress.md doesn't exist yet):

```bash
py scan_progress.py
```

It will report every TODO as new, and create `progress.md`.

**Second run** (nothing changed in the repo):

```bash
py scan_progress.py
```

It should say "No new TODOs since last run." This is the proof: it did
not repeat what it already recorded. If it had listed all the TODOs
again, that would mean the loop has no memory.

**Optional third run** - add a new TODO comment anywhere in `src/`, then
run it again. It should report only that one new TODO, not the old ones.

## What's inside progress.md

```
# Progress

## Recorded TODOs
- src/app.py:2: # TODO: add authentication check
...

## Run log
- 2026-09-08: found 4 new TODO(s)
- 2026-09-09: no new TODOs found
```

- **Recorded TODOs** = everything the loop has ever seen (its memory)
- **Run log** = a dated history of every beat, so you can see what happened over time

## How this maps to a real scheduled loop

In a real setup, `scan_progress.py` would be triggered automatically -
by `cron` (Mac/Linux) or Task Scheduler (Windows) - once a day. Running
it manually twice here simulates "today" and "tomorrow" so you can see
the memory effect without waiting a full day.

## Reset

Delete `progress.md` to start over from a clean memory.
