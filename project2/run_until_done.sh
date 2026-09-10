#!/bin/bash
cd "$(dirname "$0")"
chmod +x fix_attempt.sh

max_tries=6
attempt=0

while [ $attempt -lt $max_tries ]; do
  attempt=$((attempt+1))
  echo ""
  echo "=== Attempt $attempt ==="
  echo "Maker: trying a fix..."
  ./fix_attempt.sh $attempt

  echo "Checker: running the real tests..."
  if py -m pytest -q test_calculator.py; then
    echo ""
    echo "STOPPED: tests actually passed on attempt $attempt."
    echo "The test runner decided this, not a guess."
    exit 0
  else
    echo "Still failing. Will try again."
  fi
done

echo ""
echo "STOPPED: hit the limit of $max_tries tries without passing."
echo "Lesson: the fix approach itself needs work."
exit 1