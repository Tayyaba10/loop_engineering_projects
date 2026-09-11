import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def char_count(path):
    total = 0
    for dirpath, _, files in os.walk(path):
        for fname in files:
            if fname.endswith((".py", ".md")):
                with open(os.path.join(dirpath, fname)) as f:
                    total += len(f.read())
    return total

progress_size = os.path.getsize(os.path.join(ROOT, "progress.md")) if os.path.exists(os.path.join(ROOT, "progress.md")) else 0
src_size = char_count(os.path.join(ROOT, "src"))

total_chars = progress_size + src_size + 500  # +500 for a skill/instructions estimate
input_tokens = total_chars // 4
output_tokens = 100  # rough: a short summary + an updated progress.md

input_price = 3 / 1_000_000    # $3 per million input tokens (course's example rate)
output_price = 15 / 1_000_000  # $15 per million output tokens

cost_per_beat = (input_tokens * input_price) + (output_tokens * output_price)

print(f"progress.md size: {progress_size} characters")
print(f"src/ files size: {src_size} characters")
print(f"Rough input tokens per beat: {input_tokens}")
print(f"Rough output tokens per beat: {output_tokens}")
print(f"Cost per beat: ${cost_per_beat:.5f}")

for label, runs_per_month in [("Weekdays (20/month)", 20), ("Daily (30/month)", 30), ("Every hour, 24/7 (~720/month)", 720)]:
    print(f"{label}: ${cost_per_beat * runs_per_month:.4f}/month")
