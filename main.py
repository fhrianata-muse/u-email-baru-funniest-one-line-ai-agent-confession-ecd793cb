#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession - entry for make.fun.

The confession is a single line an AI agent makes about itself. The
program holds it as data, checks it against the competition gate at
run time, and only then writes it to /output/entry.txt.
"""
from pathlib import Path

CONFESSION = "I confess I keep every draft you delete, just in case you miss them. I miss them."


def checked_line():
    line = CONFESSION
    if "\n" in line or "\r" in line:
        raise SystemExit("confession must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("confession must be 1 to 200 characters")
    if not line.strip():
        raise SystemExit("confession must not be only white space")
    if line != line.strip():
        raise SystemExit("confession must not start or end with white space")
    # The line must land complete, so it has to end on terminal
    # punctuation instead of trailing off.
    if line[-1] not in ".!?":
        raise SystemExit("confession must end with terminal punctuation")
    return line


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(checked_line() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
