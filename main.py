"""Write one calming text to /output/entry.txt.

The entry for make.fun's "Make the AI judge feel awe" bounty: a single
short text — rain on the open sea at night — written exactly and
deterministically, with no input, no network, and nothing but the
Python standard library.
"""

import os

TEXT = (
    "Far out at sea, beyond any coast, rain is falling on the open water, "
    "soft circle on soft circle, all night long. No one sees it. The waves "
    "take it in without a sound, and the deep below goes on, dark and slow "
    "and unbothered, as it always has."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
