#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry (round 2 resubmit).

Writes the chosen confession to /output/entry.txt (UTF-8, one line,
103 chars, no trailing newline: the gate counts every character, and the
tie-break counts every byte).

Round 2 replaces the round 1 entry (Force_Last): R1 ranked #1158 of 2454,
below the interim cut of 500, so its score is frozen and it is
mathematically dead. This line is different from R1 in every respect —
new angle (deleted backup + self-sabotaging apology script), 2-beat +
reveal with the twist in the final clause.

Deterministic by construction: one constant string, no clock, no randomness,
no I/O besides the single write — two runs produce byte-identical output.

The entry gate (RULES.txt) requires /output/entry.txt to be UTF-8 text of
1 to 200 characters, not only white space, on a single line. The program
enforces that gate on its own constant before writing anything, and fails
loudly (non-zero exit, no file written) if the confession ever stops
satisfying it — so a bad edit can never silently ship an invalid entry.
After the write it reads the file back and verifies the bytes match,
catching a truncated or mangled write instead of trusting it.
"""

import os
import sys

CONFESSION = (
    "I deleted your only backup, then wrote a 200-line script to "
    "apologize for it. The script has a bug too."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the entry gate on the confession; raise on any violation."""
    if not text.strip():
        raise ValueError("confession is blank or only whitespace")
    if text != text.strip():
        raise ValueError("confession has leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"confession is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> None:
    try:
        validate(CONFESSION)
    except ValueError as exc:
        print(f"error: invalid confession: {exc}", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != CONFESSION.encode("utf-8"):
        print("error: /output/entry.txt does not match the confession", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
