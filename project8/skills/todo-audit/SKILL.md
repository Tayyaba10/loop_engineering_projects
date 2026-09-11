# TODO audit

Use this skill for the daily TODO audit.

## Steps

1. Read `progress.md` first to know what was already recorded.
2. Walk the whole repo looking for `TODO` comments in `.py` and `.sh`
   files. Skip `.git`, `__pycache__`, and `node_modules`.
3. Compare against what's recorded. Only report genuinely new items.
4. Write a short changelog entry listing each new TODO as
   `path:line: text`.
5. Do not process more than 200 items in one run (budget guard).
6. Do not touch any file except `CHANGELOG.md` and `progress.md`.
