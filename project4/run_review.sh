#!/bin/bash
# Usage: run_review.sh <mode: good|bad>
set -e
mode=$1
cd "$(dirname "$0")"

base_branch=$(git branch --show-current)
echo "Base branch detected: $base_branch"

branch="fix/${mode}-attempt"
worktree_dir="../wt-${mode}"

echo "=== Setting up an isolated worktree for '$mode' attempt ==="
git branch -f "$branch" "$base_branch"
rm -rf "$worktree_dir"
git worktree add -q "$worktree_dir" "$branch"
echo "Worktree ready at $worktree_dir (branch: $branch)"
echo ""

echo "=== Implementer drafts the fix ==="
chmod +x implement_fix.sh
./implement_fix.sh "$worktree_dir" "$mode"
echo ""

echo "=== Reviewer grades the fix ==="
chmod +x reviewer.sh
if ./reviewer.sh "$worktree_dir"; then
  echo ""
  echo "=== Result: PASS -> opening a PR (merging into $base_branch) ==="
  git checkout -q "$base_branch"
  git merge -q "$branch"
  echo "Merged. $base_branch now has the fix from '$branch'."
else
  echo ""
  echo "=== Result: FAIL -> no PR opened ==="
  echo "The branch '$branch' is left as-is for a human to look at."
fi

git worktree remove -f "$worktree_dir" 2>/dev/null || true
