import os
from datetime import date

# Repo root is two levels up from this file (project8/audit.py -> repo root)
HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
PROGRESS = os.path.join(HERE, "progress.md")
CHANGELOG = os.path.join(HERE, "CHANGELOG.md")

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".github", "project8"}
MAX_ITEMS = 200  # budget guard: never process more than this in one run


def find_all_todos():
    todos = []
    for dirpath, dirnames, files in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in sorted(files):
            if fname.endswith((".py", ".sh")):
                path = os.path.join(dirpath, fname)
                rel = os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")
                try:
                    with open(path, errors="ignore") as f:
                        for i, line in enumerate(f, 1):
                            if "#" in line and "TODO" in line.split("#", 1)[1]:
                                todos.append(f"{rel}:{i}: {line.strip()}")
                except OSError:
                    continue
                if len(todos) >= MAX_ITEMS:
                    return todos[:MAX_ITEMS]
    return todos


def load_recorded():
    if not os.path.exists(PROGRESS):
        return [], []
    recorded, runlog = [], []
    section = None
    with open(PROGRESS) as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("## Recorded"):
                section = "recorded"
                continue
            if line.startswith("## Run log"):
                section = "runlog"
                continue
            if section == "recorded" and line.startswith("- "):
                recorded.append(line[2:])
            elif section == "runlog" and line.startswith("- "):
                runlog.append(line[2:])
    return recorded, runlog


def save_progress(recorded, runlog):
    with open(PROGRESS, "w") as f:
        f.write("# Progress - TODO audit\n\n")
        f.write("## Recorded TODOs\n")
        for item in recorded:
            f.write(f"- {item}\n")
        f.write("\n## Run log\n")
        for item in runlog:
            f.write(f"- {item}\n")


def main():
    today = date.today().isoformat()
    recorded, runlog = load_recorded()
    current = find_all_todos()
    new_items = [t for t in current if t not in recorded]

    if new_items:
        with open(CHANGELOG, "w") as f:
            f.write(f"# TODO audit - {today}\n\n")
            f.write(f"{len(new_items)} new TODO(s) found:\n\n")
            for item in new_items:
                f.write(f"- {item}\n")
        recorded = recorded + new_items
        runlog.append(f"{today}: found {len(new_items)} new TODO(s)")
        print(f"Found {len(new_items)} new TODO(s). Wrote CHANGELOG.md.")
    else:
        # Nothing new: remove any stale changelog so the connector
        # step sees no diff and opens no empty PR.
        if os.path.exists(CHANGELOG):
            os.remove(CHANGELOG)
        runlog.append(f"{today}: no new TODOs found")
        print("No new TODOs. Nothing to report.")

    save_progress(recorded, runlog)


if __name__ == "__main__":
    main()
