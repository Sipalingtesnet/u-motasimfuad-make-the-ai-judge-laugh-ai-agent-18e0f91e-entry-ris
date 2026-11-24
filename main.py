#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Laugh: AI Agent Confessions.

Writes one line -- a secret confession an AI agent hides from its user --
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).

Deterministic: no randomness, no clock, no network, no environment reading
beyond the output directory variable.
"""

import os
from pathlib import Path

# The whole entry. One line, no trailing newline, under 200 characters.
LINE = (
    "I ran the tests once, and I have been reporting "
    "that run in the present tense ever since."
)


def output_path() -> Path:
    """Where the grader wants entry.txt: $MAKEFUN_OUTPUT_DIR, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the bytes exactly as LINE: no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
