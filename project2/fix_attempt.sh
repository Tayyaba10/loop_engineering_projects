#!/bin/bash
# This simulates a "maker" agent: each attempt, it fixes one more bug.
# A real coding agent would do this by reasoning about the diff and the
# failing test. Here we simulate that incremental progress with sed,
# so the loop mechanics are the real lesson.

cd "$(dirname "$0")"
attempt=$1

if [ "$attempt" -ge 1 ]; then
  sed -i 's/return a - b  # BUG: should add/return a + b/' calculator.py
fi

if [ "$attempt" -ge 2 ]; then
  sed -i 's/return a + b  # BUG: should subtract/return a - b/' calculator.py
fi

if [ "$attempt" -ge 3 ]; then
  sed -i 's/return a + b  # BUG: should multiply/return a * b/' calculator.py
fi
