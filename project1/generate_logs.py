import random

levels = ["INFO"] * 15 + ["WARN"] * 3 + ["ERROR"] * 2
messages = [
    "user login successful",
    "database query slow",
    "cache miss on product page",
    "payment gateway timeout",
    "connection reset by peer",
    "request completed",
    "session expired",
    "disk usage high",
]

with open("overnight.log", "w") as f:
    for i in range(5000):
        level = random.choice(levels)
        msg = random.choice(messages)
        f.write(f"2026-09-08 0{i%9}:00:00 [{level}] {msg} (req-{i})\n")

print("Wrote 5000 log lines to overnight.log")