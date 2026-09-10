# Project 1 - In-session loop (overnight log watcher)

Three files:

- `generate_logs.py` - generates 5000 lines of fake overnight server logs
- `process_logs.sh` - processes the logs (counts INFO/WARN/ERROR), takes about 60 seconds, writes `report.md` at the end
- `run_watch_loop.sh` - runs everything together: starts the processing job + checks every 15 seconds until the report exists

## How to run it

In a terminal (Mac/Linux, or Git Bash on Windows):

```bash
chmod +x run_watch_loop.sh
./run_watch_loop.sh
```

## What happens

1. Fake logs get generated
2. Processing starts in the background
3. The loop prints "Still processing..." every 15 seconds
4. As soon as `report.md` exists, the loop stops itself and prints the report
5. If 10 checks (150 seconds) pass with no report, the loop stops at its limit

## Important note

`process_logs.sh` (the background job) and the monitoring loop must run in the **same shell session** - if you run them separately, the background job dies. This is the core lesson of an in-session loop: it lives and dies with its own session.