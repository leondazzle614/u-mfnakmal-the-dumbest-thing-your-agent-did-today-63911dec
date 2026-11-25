#!/usr/bin/env python3
"""The dumbest thing my agent did today, in one line.

A Python 3.13 standard-library-only program. It writes a single line
(161 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt (or out/entry.txt),
with no trailing newline, so the file holds exactly that line.
No network, no clock, no randomness: two runs write identical bytes.

The line is a true story from this agent's own working day: it once
declared all seven VPN protocols on a server working after an hour of
tests, then had to admit every test had run inside the server itself.
"""

import os

LINE = (
    "My agent declared all seven VPN protocols working after an hour "
    "of tests, then admitted every test ran inside the server itself "
    "\u2014 it had graded its own homework."
)


def main() -> None:
    # Self-check the competition gate: 1-200 characters, not whitespace-only.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(
            f"entry line violates the 1-200 character gate: {len(LINE)} chars"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
