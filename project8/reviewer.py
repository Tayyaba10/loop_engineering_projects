import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
CHANGELOG = os.path.join(HERE, "CHANGELOG.md")

# path:line: text  (relative path, colon, line number, colon, text)
ITEM_PATTERN = re.compile(r"^- ([^:\r\n]+):(\d+): (.+)$")
MAX_ITEMS = 200


def main():
    if not os.path.exists(CHANGELOG):
        print("No CHANGELOG.md this run (nothing new). Nothing to review.")
        return 0

    with open(CHANGELOG, "r", encoding="utf-8", errors="ignore") as f:
        lines = [l.rstrip("\r\n") for l in f if l.strip()]

    item_lines = [l for l in lines if l.startswith("- ")]

    if not item_lines:
        print("FAIL: CHANGELOG.md exists but has no items listed.")
        return 1

    if len(item_lines) > MAX_ITEMS:
        print(f"FAIL: item count exceeds maximum budget limit of {MAX_ITEMS} (found {len(item_lines)}).")
        return 1

    if len(item_lines) != len(set(item_lines)):
        print("FAIL: duplicate entries found in CHANGELOG.md")
        return 1

    for line in item_lines:
        m = ITEM_PATTERN.match(line)
        if not m:
            print(f"FAIL: malformed entry (expected '- path:line: text'): {line}")
            return 1

        rel_path, line_num_str, expected_text = m.groups()
        rel_path = rel_path.strip()
        expected_text = expected_text.strip()

        try:
            line_num = int(line_num_str)
        except ValueError:
            print(f"FAIL: invalid line number '{line_num_str}' in entry: {line}")
            return 1

        if line_num <= 0:
            print(f"FAIL: line number must be positive in entry: {line}")
            return 1

        # Independently verify the file and line in the repository
        file_path = os.path.normpath(os.path.join(REPO_ROOT, rel_path))
        repo_root_norm = os.path.normpath(REPO_ROOT)
        if not file_path.startswith(repo_root_norm):
            print(f"FAIL: path traversal outside repo root: {rel_path}")
            return 1

        if not os.path.isfile(file_path):
            print(f"FAIL: referenced file does not exist: {rel_path}")
            return 1

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                file_lines = f.readlines()
        except OSError as e:
            print(f"FAIL: could not read file {rel_path}: {e}")
            return 1

        if line_num > len(file_lines):
            print(f"FAIL: line number {line_num} out of range for file {rel_path} ({len(file_lines)} lines)")
            return 1

        actual_line = file_lines[line_num - 1].rstrip("\r\n")

        if "TODO" not in actual_line:
            print(f"FAIL: line {line_num} in {rel_path} does not contain 'TODO': {actual_line}")
            return 1

        if actual_line.strip() != expected_text:
            print(f"FAIL: line {line_num} in {rel_path} content mismatch (expected '{expected_text}', found '{actual_line.strip()}')")
            return 1

    print(f"PASS: {len(item_lines)} well-formed entries independently verified, no duplicates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
