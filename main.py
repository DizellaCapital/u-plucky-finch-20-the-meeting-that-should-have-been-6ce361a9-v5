"""The Meeting That Should Have Been an Email — make.fun entry (v5).

Writes the entry's single joke line to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR, or /output when unset). Stdlib only.
Before writing, the line is validated: one line only, 1-200
characters, no tabs, ending with sentence punctuation. After writing,
the file is read back and compared to catch any write error.
"""

import os

LINE = (
    "Dave booked a 30-minute meeting to read the email he sent at 8:04, "
    "then spent 29 minutes apologizing for the email, which had already "
    "apologized better in writing."
)


def main() -> None:
    line = LINE
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert "\t" not in line, "entry must not contain tabs"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line[-1] in ".!?", "entry must end with sentence punctuation"
    # One joke, standing alone: no setup, no second line, no attachment.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == line, "read-back mismatch"
    print(f"wrote {len(line.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
