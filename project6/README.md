# Project 6 - The Doorbell Loop (event-driven)

A repo that reviews its own pull requests, automatically. No command
you type - GitHub fires this the moment a PR is opened or updated.

## Files

- `inventory.py` - correct, working code (stays on `main`)
- `test_inventory.py` - tests (the checker)
- `.github/workflows/pr-review.yml` - the doorbell: GitHub runs this
  automatically on every pull request, runs the tests, and posts the
  result as a comment on the PR

## Part A - Create the GitHub repo and push main

1. Go to [github.com](https://github.com) and click **New repository**
2. Name it (for example `loop-project-6-doorbell`), keep it **Public**
   or **Private**, do NOT add a README/license from GitHub's side
   (we already have our own files)
3. Click **Create repository**
4. On your machine, in this project's folder:

```bash
git init
git config user.email "you@example.com"
git config user.name "Your Name"
git add -A
git commit -m "initial repo: working inventory.py + doorbell workflow"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/loop-project-6-doorbell.git
git push -u origin main
```

Replace `YOUR-USERNAME` and the repo name with your own. GitHub will
ask you to sign in (a browser popup, or a personal access token if it
asks for a password).

## Part B - Plant a bug and open a PR

Now create a branch with a deliberate bug:

```bash
git checkout -b bug/off-by-one
```

Edit `inventory.py` so the function is wrong on purpose - for example:

```python
def get_last_n_items(items, n):
    """Return the last n items from a list."""
    return items[-n - 1:]
```

Then:

```bash
git add -A
git commit -m "bug: off-by-one in get_last_n_items"
git push -u origin bug/off-by-one
```

Go to your repo on GitHub, click **Compare & pull request**, and open
the PR (base: `main`, compare: `bug/off-by-one`).

## Part C - Watch the doorbell fire

Do nothing. Wait about 30-60 seconds, then refresh the PR page.

**You should see:**

1. A check running (or already finished) under the PR - click the
   **Actions** tab if you want to watch it live
2. A **comment appears on the PR automatically** saying:

```
## Doorbell review: FAIL

  <the failing test output, showing the off-by-one>
```

Nobody asked for this review. It fired because you opened a PR - that
is the event heartbeat.

## Part D - Prove the re-fire

Fix the bug in the same branch (revert to the correct code), commit,
and push again to the same branch:

```bash
git add -A
git commit -m "fix: revert to correct slicing"
git push
```

Refresh the PR. A **second** comment should appear, this time saying
**PASS**. This second run fired from the `synchronize` event (a new
push to an open PR) - the same doorbell, ringing again.

## What this proves

- No prompt was typed for either review - the event heartbeat did it
- The checker is a real command (pytest), not an opinion
- This completes all four heartbeats from the course: in-session
  (Project 1), conditional (Project 2), scheduled (Project 3), and now
  event-driven (this project)

## Clean up

You can delete the repo from GitHub's Settings tab when you're done,
or leave it - it costs nothing sitting there.
