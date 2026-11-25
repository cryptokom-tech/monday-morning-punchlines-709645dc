#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun bounty entry.

Writes one joke about Monday mornings (99 characters) to /output/entry.txt.
Standard library only, no network, no environment reads, never deletes /output.
"""

import os

JOKE = "Monday morning: my bed filed for full custody of me \u2014 and honestly, its case is stronger than mine."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
