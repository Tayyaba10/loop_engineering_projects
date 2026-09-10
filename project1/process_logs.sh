#!/bin/bash
# This script simulates "overnight processing":
# it does work in chunks (like a real job would), and writes a report at the end

cd "$(dirname "$0")"

echo "Processing started..." >> process.log

# Chunk 1: count INFO lines
sleep 20
info_count=$(grep -c "\[INFO\]" overnight.log)
echo "Chunk 1 done: INFO count = $info_count" >> process.log

# Chunk 2: count WARN lines
sleep 20
warn_count=$(grep -c "\[WARN\]" overnight.log)
echo "Chunk 2 done: WARN count = $warn_count" >> process.log

# Chunk 3: count ERROR lines
sleep 20
error_count=$(grep -c "\[ERROR\]" overnight.log)
echo "Chunk 3 done: ERROR count = $error_count" >> process.log

# Write the final report (this file is the signal that the work is done)
cat > report.md << EOF
# Overnight Log Report - 2026-09-08

- Total lines processed: 5000
- INFO: $info_count
- WARN: $warn_count
- ERROR: $error_count

Status: DONE
EOF

echo "Report written: report.md" >> process.log