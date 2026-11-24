#!/usr/bin/env python3
"""One-Star Review of Something Essential - make.fun entry.

Writes one deadpan one-star review (a single line, <= 160 characters)
of an everyday essential to /output/entry.txt.
"""

import os

ENTRY = (
    "One star. Gravity catches every phone, plate and cup I have ever "
    "dropped, instantly and without fail, yet has never once caught me."
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
