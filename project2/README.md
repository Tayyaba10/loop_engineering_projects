# Project 2 - Conditional loop (run-until-done)

This project builds a loop that keeps trying until a real test passes -
not until a timer runs out, and not based on anyone's opinion that it
"looks done". The test runner (pytest) makes the call.

## Files

- `calculator.py` - has 3 bugs on purpose
- `test_calculator.py` - 3 tests that check the correct behavior (checker)
- `fix_attempt.sh` - the "maker": each attempt fixes one more bug, simulating an agent making incremental progress
- `run_until_done.sh` - the loop: runs the maker, then the checker, up to 6 times, and stops the moment tests actually pass

## Requirement

Python and pytest must be installed:

```bash
py -m pip install pytest
```

(use `python3 -m pip install pytest` on Mac/Linux)

## How to run it

```bash
cd loop-project-2
chmod +x run_until_done.sh
./run_until_done.sh
```

## What happens

- Attempt 1: one bug gets fixed, 2 tests still fail
- Attempt 2: another bug gets fixed, 1 test still fails
- Attempt 3: last bug gets fixed, all 3 tests pass -> loop stops itself

If it ever stopped because it hit "attempt 6" instead of because the
tests passed, that would mean the fix approach itself needs work - that
is the whole lesson of this project: never trust a loop's own claim that
it's done. Trust the command that checks it.

## Reset before running again

The maker script edits `calculator.py` in place. To try again from
scratch, replace `calculator.py` with the original buggy version (or
just re-download it from here).
