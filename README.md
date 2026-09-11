# Loop Engineering - Practice Projects

This folder holds hands-on projects for the Loop Engineering course. Each project lives in its own subfolder and builds a real, working loop - not just a read-through of the concept.

## Folder structure

```
loop-engineering/
  project1/   - in-session loop (done)
  project2/   - conditional loop (run-until-done)
  project3/   - scheduled loop (needs memory / spine)
  project6/   - event-driven loop (the "doorbell")
  ...
```

Each project folder has its own README with exact run instructions.

## Two rules, every project

1. **Use a throwaway repo.** A loop edits files on its own - never point it at work you actually care about.
2. **Set a limit first.** Max tries, max minutes, or max spend - before letting anything run unattended.

## Project status

| # | Project | Heartbeat type | Status |
|---|---|---|---|
| 1 | Watch loop (overnight log processor) | In-session | Done |
| 2 | Run-until-done (make a condition pass, then stop) | Conditional | Done |
| 3 | Morning brief with memory | Scheduled | Done |
| 6 | The Doorbell (reacts to an event) | Event-driven | Done |

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
