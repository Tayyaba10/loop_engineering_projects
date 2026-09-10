#!/bin/bash
# Usage: reviewer.sh <worktree_dir>
# Prints PASS or FAIL with reasons. Exit code 0 = PASS, 1 = FAIL.
worktree_dir=$1
cd "$worktree_dir"

echo "Reviewer: running the tests..."
if ! py -m pytest -q test_pricing.py > /tmp/review_output.txt 2>&1; then
  echo "FAIL"
  echo "Reason: tests did not pass."
  cat /tmp/review_output.txt
  exit 1
fi
echo "  tests passed."

echo "Reviewer: checking against the skill's hard rule (no hardcoding)..."
if grep -qE "total == 200|percent == 10|return 180" pricing.py; then
  echo "FAIL"
  echo "Reason: the fix looks hardcoded to the test's specific values"
  echo "(found a special case matching the test input/output in the code)."
  echo "This is a shortcut, not a general fix. See skills/fix-pricing-bug/SKILL.md."
  exit 1
fi
echo "  no hardcoding found."

echo "PASS"
echo "Reason: tests pass, and the fix is a general formula, not a shortcut."
exit 0
