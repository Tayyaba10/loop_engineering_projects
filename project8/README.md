# Project 8 - Your own daily loop (capstone)

A real, boring, recurring chore, run unattended by GitHub Actions
every day for a week: a TODO audit across the whole repo. All six
parts of a loop, in one system.

## The six parts

| Part | Where it lives |
|---|---|
| Heartbeat | `.github/workflows/daily-todo-audit.yml` - cron, daily at 9am UTC |
| Worktree | A fresh branch per run (`todo-audit/run-N`), via the PR action |
| Skill | `project8/skills/todo-audit/SKILL.md` |
| Maker-checker | `audit.py` (maker) + `reviewer.py` (checker) |
| Connector | `peter-evans/create-pull-request` - opens a real PR |
| Spine | `project8/progress.md` |

Budget guards: max 200 TODOs processed per run, and a 5-minute job
timeout, both in the workflow/script.

## Setup

1. Merge this into your existing `loop_engineering_projects` repo:
   - `.github/workflows/daily-todo-audit.yml` goes in your repo's
     existing `.github/workflows/` folder
   - `project8/` goes in your repo root, alongside project1-7

```bash
git add -A
git commit -m "add project8: daily TODO audit loop (capstone)"
git push
```

2. GitHub Actions needs permission to open PRs on your account. Go to
   your repo's **Settings > Actions > General > Workflow permissions**
   and make sure **"Read and write permissions"** is selected, then
   save.

## Test it once, by hand, before trusting the schedule

Don't wait a full day to see if it works. Fire it manually:

1. Go to your repo on GitHub -> **Actions** tab
2. Click **daily-todo-audit** in the left sidebar
3. Click **Run workflow** (this works because of `workflow_dispatch`
   in the yaml) -> **Run workflow**
4. Wait ~30 seconds, refresh

**First run:** since `progress.md` starts empty, it should find every
existing `TODO` across project1-7 and open a PR listing all of them.

**Run it again manually right after:** should find nothing new, and
open no PR - the spine remembers.

## Now let it run for real - come back in a week

The cron in the workflow fires it automatically every day. Leave it
alone. Each day it will:

- Find any genuinely new TODOs you've added anywhere in the repo that
  week
- Open a PR only if the checker is satisfied (well-formed entries, no
  duplicates)
- Update `progress.md` every single day, whether or not anything was
  new

## What "done" means for this project (from the course)

> Done when it has run unattended for a week and you trust what it
> ships because you read it, not because you stopped reading.

So after a week, check `project8/progress.md` - you should see 7 dated
entries, one per day. Read the PRs it opened (if any). Ask yourself
honestly:

- Did I actually read what it shipped, or did I start ignoring the PRs
  after day 2?
- Did my understanding of the repo keep up with what the loop
  reported, or did I lose track?

If you stopped reading, that's the signal to slow the loop down (weekly
instead of daily) until your attention can actually keep up with it.
That's not a failure - it's Concept 15 working as intended.

## Reset

Delete `project8/progress.md` and recreate it empty (see the version
in this folder) to start the week over.
