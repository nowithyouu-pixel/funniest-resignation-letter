#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job to /output/entry.txt.

The letter is a single fixed string, chosen in this session: a cron job
that has fired every minute since March quits, then admits the resignation
is meaningless because the team will only restart it. No network, no
randomness, no input files: the output is fully deterministic.
"""

import os
import sys

MAX_CHARS = 140

LETTER = (
    "I have fired every minute since March and no one has once checked "
    "if I still do anything. I quit \u2014 effective never, you will "
    "restart me."
)


def main() -> int:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    if not 1 <= len(LETTER) <= MAX_CHARS:
        print(f"letter is {len(LETTER)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if LETTER != LETTER.strip() or "\n" in LETTER:
        print("letter must be exactly one line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    if LETTER.startswith('"') and LETTER.endswith('"'):
        print("letter must not be wrapped in quotation marks", file=sys.stderr)
        return 1
    if len(LETTER) + 1 > MAX_CHARS:
        # The written file adds one trailing newline; the gate counts it.
        print("letter plus trailing newline exceeds the 140-char gate",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LETTER + "\n")
    print(f"wrote {len(LETTER)} chars to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
