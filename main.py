#!/usr/bin/env python3
"""One Line, One Laugh — writes one funny line to /output/entry.txt.

Stdlib only. Deterministic: the same line, byte for byte, every run.
"""

import os

LINE = "I asked the barista for something strong. She handed me her resignation letter."


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("Wrote %d chars to %s" % (len(LINE), out))


if __name__ == "__main__":
    main()
