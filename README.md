# Loop Engineering - Practice Projects

This folder holds hands-on projects for the Loop Engineering course. Each project lives in its own subfolder and builds a real, working loop - not just a read-through of the concept.

## Folder structure

```
loop-engineering/
  .github/
    workflows/
      pr-review.yml     - the doorbell (Project 6)
  project1/   - in-session loop (done)
  project2/   - conditional loop / maker-checker (done)
  project3/   - scheduled loop / spine (done)
  project4/   - worktree + skill + maker-checker (done)
  project5/   - dynamic workflow (done)
  project6/   - event-driven loop, the "doorbell" (done)
  project7/   - cost + observability + breaking a loop on purpose (done)
```

Each project folder has its own README with exact run instructions.

## Two rules, every project

1. **Use a throwaway repo.** A loop edits files on its own - never point it at work you actually care about.
2. **Set a limit first.** Max tries, max minutes, or max spend - before letting anything run unattended.

## Project status

| # | Project | Heartbeat / Concept | Status |
|---|---|---|---|
| 1 | Watch loop (overnight log processor) | In-session | Done |
| 2 | Run-until-done (calculator + failing tests, maker-checker) | Conditional | Done |
| 3 | Morning brief with memory | Scheduled + spine | Done |
| 4 | A fix loop with a real checker | Worktree + skill + maker-checker | Done |
| 5 | Codify the body | Dynamic workflow (not a loop) | Done |
| 6 | The Doorbell | Event-driven | Done |
| 7 | Break it on purpose | Cost + observability | Done |

## The six parts of any loop (quick reference)

| Part | What it does |
|---|---|
| Heartbeat | What starts a beat - a timer, a condition, a schedule, or an event |
| Worktree | Isolated folder/branch so parallel work doesn't collide |
| Skill | Project knowledge written down once, reused every run |
| Subagent (maker-checker) | One agent does the work, a separate one checks it |
| Connector | Lets the loop actually act (open a PR, send a message, etc.) |
| Spine (memory) | A file that remembers what happened between runs |

## Key lesson from Project 1

An in-session loop lives and dies with its own shell session. If the background job and the monitoring loop run in separate sessions, the background job gets killed. They must run together, in the same session.

## Key lesson from Project 2

The loop stopped because `pytest` (the checker - a real command) reported PASS, not because the maker claimed it was done. When the loop first kept hitting its 6-try cap, the cause wasn't the fix logic - it was that `pytest` wasn't on PATH, so the checker itself never ran. This is exactly the failure mode the project warns about: if a loop keeps hitting its limit, check whether the stopping condition can even fire before assuming the fix approach is wrong.

## Key lesson from Project 3

The spine (`progress.md`) is what lets the second run build on the first instead of repeating itself. Proven by running the loop twice: run 1 found 4 TODOs, run 2 correctly reported "no new TODOs" because they were already recorded.

## Key lesson from Project 4

A checker that only runs tests can be fooled. A deliberately bad fix was shaped to match the one test case exactly and technically passed pytest - but the reviewer also checked the diff against a rule from the skill (no hardcoding test values), which is what caught it. A checker that approves everything is no checker.

## Key lesson from Project 5

A dynamic workflow is the body of one beat, not a loop. Running it twice proved it: the second run redid all the same work from scratch (visible as duplicate commits in git log), with zero awareness that the first run had already succeeded. It has no heartbeat (nothing fires it automatically) and no spine (nothing on disk remembers what it already did).

## Key lesson from Project 6

The event heartbeat needs no prompt from a person at all. Opening a pull request with a planted bug triggered GitHub Actions automatically, which ran the real test suite and posted a review comment - PASS or FAIL with reasons - with nobody typing a command. This completed all four heartbeats: in-session, conditional, scheduled, and event-driven.

## Key lesson from Project 7

A loop can fail completely silently. The first sabotage (pointing at a non-existent folder) was already handled by a loud error check we had built in. But a second, unplanned failure appeared for real: on Windows, file paths use backslashes, while the original spine was written with forward slashes, so the loop couldn't recognize its own previously-recorded TODOs and started silently duplicating them - no crash, no error, just quietly wrong. A single `os.path.isdir()` check turns a silent failure into a loud one; the spine alone was enough to diagnose both failures without re-running anything.