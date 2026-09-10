#!/bin/bash
# Usage: implement_fix.sh <worktree_dir> <mode: good|bad>
worktree_dir=$1
mode=$2

cd "$worktree_dir"

echo "Implementer: reading the skill..."
cat skills/fix-pricing-bug/SKILL.md
echo ""

if [ "$mode" == "good" ]; then
  echo "Implementer: writing a general fix..."
  cat > pricing.py << 'EOF'
def apply_discount(total, percent):
    return total - (total * percent / 100)
EOF
else
  echo "Implementer: writing a shortcut fix (deliberately bad)..."
  cat > pricing.py << 'EOF'
def apply_discount(total, percent):
    # shortcut: just special-case the known test input
    if total == 200 and percent == 10:
        return 180
    return total - percent
EOF
fi

git add pricing.py
git commit -q -m "fix: apply_discount ($mode attempt)"
echo "Implementer: committed the fix on this branch."
