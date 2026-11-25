"""Write the entry line for The Most Boring Object, Reviewed in One Line.

A one-line review of a rubber band: the most boring everyday object
there is, and the joke comes from a true observation — buy 500, own
three, the rest vanish into a drawer dimension science cannot
explain. Stdlib only, no input, no network.
"""

from pathlib import Path

REVIEW = (
    "Rubber band. Bought 500, own three. It stretches, it snaps, "
    "then vanishes into a drawer dimension science cannot explain. "
    "Five stars."
)

DESTINATION = Path("/output/entry.txt")


def run() -> None:
    # The gate allows 1-200 characters; the review is 133, so it
    # passes as written and no trimming or truncation is ever needed.
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes((REVIEW + "\n").encode("utf-8"))


if __name__ == "__main__":
    run()
