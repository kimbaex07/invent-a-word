#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes the one-line entry (word + part of speech + definition) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python 3 stdlib, deterministic,
no network access.
"""

import os

ENTRY = "miswave (n.) — the hot-cheeked moment you wave back at someone who was waving at the person behind you."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
