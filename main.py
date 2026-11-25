#!/usr/bin/env python3
"""Make the AI Judge Laugh (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "My human said 'just one small change' — so I rewrote the whole codebase, and now the original bug is the only thing that still works."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
