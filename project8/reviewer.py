import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHANGELOG = os.path.join(HERE, "CHANGELOG.md")

# path:line: text  (relative path, colon, line number, colon, text)
ITEM_PATTERN = re.compile(r"^- .+:\d+: .+$")


def main():
    if not os.path.exists(CHANGELOG):
        print("No CHANGELOG.md this run (nothing new). Nothing to review.")
        return 0

    with open(CHANGELOG) as f:
        lines = [l.rstrip("\n") for l in f if l.strip()]

    item_lines = [l for l in lines if l.startswith("- ")]

    if not item_lines:
        print("FAIL: CHANGELOG.md exists but has no items listed.")
        return 1

    for line in item_lines:
        if not ITEM_PATTERN.match(line):
            print(f"FAIL: malformed entry (expected 'path:line: text'): {line}")
            return 1

    if len(item_lines) != len(set(item_lines)):
        print("FAIL: duplicate entries found in CHANGELOG.md")
        return 1

    print(f"PASS: {len(item_lines)} well-formed entries, no duplicates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
