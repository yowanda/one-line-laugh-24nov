#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes one original one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
Deterministic: same bytes on every run. No network, no randomness.
"""

import os
import sys

JOKE = (
    "My fitness tracker says I burned 400 calories today, mostly by "
    "walking to the fridge to check whether anything new had arrived "
    "since lunch."
)


def main() -> int:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke out of gate range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
