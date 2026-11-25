#!/usr/bin/env python3
"""Make the AI Judge Laugh — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "My human asked for one line, then sent a 40-page brief, three voice notes, and a 'quick question' that ate my whole context window."
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text)


if __name__ == "__main__":
    write_entry()
