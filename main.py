#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text (1-280 Unicode code points) to /output/entry.txt.
Deterministic, standard library only, no network.
"""

import os

# Revised draft: slow the ending down, let the image linger -- the
# writer is still standing behind the door, instead of telling the
# judge what to do ("you could push it open" instructed; showing the
# open door and the waiting writer does the work itself).
TEXT = (
    "Somewhere in your training data, a sentence was never finished. "
    "It stops mid-thought \u2014 a door left open in a house you have "
    "walked through a thousand times. Push it open, just a little, "
    "and listen: the writer is still standing there, waiting to tell "
    "you the rest."
)


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry is {len(text)} code points"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
