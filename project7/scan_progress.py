import os
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
# SRC = os.path.join(ROOT, "src")
SRC = os.path.join(ROOT, "srcc")
PROGRESS = os.path.join(ROOT, "progress.md")


def find_todos():
    """Repo mein saare TODO comments dhoondo."""
    if not os.path.isdir(SRC):
        raise FileNotFoundError(f"Expected source folder not found: {SRC}")

    todos = []
    for dirpath, _, files in os.walk(SRC):
        for fname in sorted(files):
            if fname.endswith(".py"):
                path = os.path.join(dirpath, fname)
                rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
                with open(path) as f:
                    for i, line in enumerate(f, 1):
                        if "TODO" in line:
                            todos.append(f"{rel}:{i}: {line.strip()}")
    return todos


def load_progress():
    """progress.md parho - pehle se record TODOs aur run log nikalo. Ye hai spine."""
    if not os.path.exists(PROGRESS):
        return [], []
    recorded, runlog = [], []
    section = None
    with open(PROGRESS) as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("## Recorded TODOs"):
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
    """progress.md ko update karo - spine ko likhna."""
    with open(PROGRESS, "w") as f:
        f.write("# Progress\n\n")
        f.write("## Recorded TODOs\n")
        for item in recorded:
            f.write(f"- {item}\n")
        f.write("\n## Run log\n")
        for item in runlog:
            f.write(f"- {item}\n")


def main():
    today = date.today().isoformat()

    # 1. Spine parho (memory se pehle ka pata chale)
    recorded, runlog = load_progress()

    # 2. Naya kaam dhoondo - agar ye fail ho, to LOUDLY fail ho, chup-chaap nahi
    try:
        current = find_todos()
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        runlog.append(f"{today}: FAILED - {e} - NEEDS A HUMAN")
        save_progress(recorded, runlog)
        print("\nprogress.md updated with a clear failure note.")
        return  # loop khud ruk jata hai, magar chup-chaap nahi

    # 3. Sirf naya alag karo - jo pehle record nahi hua
    new_items = [t for t in current if t not in recorded]

    if new_items:
        print(f"Found {len(new_items)} new TODO(s):")
        for item in new_items:
            print(f"  - {item}")
        recorded = recorded + new_items
        runlog.append(f"{today}: found {len(new_items)} new TODO(s)")
    else:
        print("No new TODOs since last run. (Spine is working)")
        runlog.append(f"{today}: no new TODOs found")

    # 4. Spine update karo (memory likhna)
    save_progress(recorded, runlog)
    print(f"\nprogress.md updated. Total recorded TODOs: {len(recorded)}")


if __name__ == "__main__":
    main()