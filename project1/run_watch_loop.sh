#!/bin/bash
# Starts the background processing job AND the monitoring loop
# in the same shell session, so the background job doesn't die.

set -e
cd "$(dirname "$0")"

rm -f report.md process.log

echo "Generating fake overnight logs..."
py generate_logs.py

echo ""
echo "Starting processing in the background (takes about 60 seconds)..."
chmod +x process_logs.sh
./process_logs.sh &
bg_pid=$!
echo "Background PID: $bg_pid"
echo ""

# Heartbeat loop
attempt=0
max_attempts=10   # limit -- never loop forever

while [ $attempt -lt $max_attempts ]; do
  if [ -f report.md ]; then
    echo "Done! Here is the report:"
    echo "-----------------------------------"
    cat report.md
    break
  else
    attempt=$((attempt+1))
    echo "Still processing... (check #$attempt)"
    sleep 15
  fi
done

if [ ! -f report.md ]; then
  echo "Reached the limit, report was not ready yet"
fi