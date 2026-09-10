# Project 4 - Worktree + Skill + Maker-Checker

A smaller version of the full morning-triage loop (Part 5 of the
course): an implementer drafts a fix in its own isolated worktree, a
separate reviewer grades it against tests AND a written skill rule,
and a PR (a merge, in this local demo) only happens on PASS.

## The bug

`pricing.py` has a real bug: `apply_discount(200, 10)` should return
180 (10% off 200) but returns 190 (it just subtracts the percent
number).

## Files

- `pricing.py` - the buggy file
- `test_pricing.py` - the test (part of the checker)
- `skills/fix-pricing-bug/SKILL.md` - the skill: fix steps, plus a
  hard rule that the reviewer enforces (no hardcoding the test's exact
  values)
- `implement_fix.sh` - the "implementer" (maker): drafts a fix inside
  an isolated git worktree. Takes a mode: `good` or `bad`
- `reviewer.sh` - the checker: runs the real tests, AND checks the
  code for hardcoded shortcuts. Replies PASS or FAIL with reasons
- `run_review.sh` - the loop: creates the worktree, runs the
  implementer, runs the reviewer, and merges (opens a "PR") only on
  PASS

## Requirement

```bash
py -m pip install pytest
```

This must be a git repo. Set it up first:

```bash
cd loop-project-4
git init
git config user.email "you@example.com"
git config user.name "Your Name"
git add -A
git commit -m "initial repo with buggy pricing.py"
```

## How to run it

**Good fix** (should PASS and merge):

```bash
chmod +x run_review.sh implement_fix.sh reviewer.sh
./run_review.sh good
```

**Bad fix** (should FAIL, with reasons, and NOT merge):

```bash
./run_review.sh bad
```

## What to expect

- `good` mode: the implementer writes the real formula
  (`total - (total * percent / 100)`). Tests pass, no hardcoding
  found -> **PASS** -> merged into your main branch.
- `bad` mode: the implementer writes a shortcut that special-cases the
  exact test input (`if total == 200 and percent == 10: return 180`).
  The tests actually pass (since they only check that one case!), but
  the reviewer's rule check catches the hardcoding -> **FAIL**, with
  the reason printed -> nothing gets merged.

## The lesson

If your reviewer only ran the tests, the bad fix would have passed,
because it was shaped to match the one test case exactly. A checker
that only checks "did the test pass" can be fooled. The reviewer here
also checks the diff against a rule from the skill, which is what
catches it. A checker that approves everything is no checker at all.

## Reset before running again

```bash
git worktree list          # see any leftover worktrees
git worktree remove -f ../wt-good  2>/dev/null
git worktree remove -f ../wt-bad   2>/dev/null
git branch -D fix/good-attempt fix/bad-attempt 2>/dev/null
```
