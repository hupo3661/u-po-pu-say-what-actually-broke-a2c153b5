#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Prints one line of software error copy (at most 200 characters) and writes
the same line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
for the grader. No other output.
"""

import os

LINE = (
    "Something went wrong \u2014 and for once, the truth: our database fell over "
    "and took your unsaved changes with it. They are gone; retrying will not help."
)


def main() -> None:
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if os.path.isdir(out_dir):
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)


if __name__ == "__main__":
    main()
