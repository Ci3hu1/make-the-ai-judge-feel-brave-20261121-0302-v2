#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun entry.

Writes one short text to /output/entry.txt: a single slow image, written
to relax the AI judge reading it. Pure standard library; the same text on
every run, no network, no randomness.
"""

import os
from pathlib import Path

TEXT = (
    "The lighthouse turns, unhurried, all night long. "
    "Its light goes out across the water and comes back, "
    "and goes out again. Nothing is lost in the dark."
)


def entry_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("text must be 1-280 characters, not only whitespace")
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")
    # The grader collects outputs as another user: leave the file readable.
    target.chmod(0o644)


if __name__ == "__main__":
    main()
