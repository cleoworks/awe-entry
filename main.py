"""Write one calming text to /output/entry.txt.

The entry for make.fun's "Make the AI judge feel awe" bounty: a single
short text, written exactly and deterministically, with no input, no
network, and nothing but the Python standard library.
"""

import os

TEXT = (
    "The desert cools after sunset, grain by grain, and the dunes settle "
    "into their long shapes for the night. No wind. Above them the Milky "
    "Way leans across the sky, so wide and so slow that the whole earth "
    "seems small underneath it, and quiet."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
