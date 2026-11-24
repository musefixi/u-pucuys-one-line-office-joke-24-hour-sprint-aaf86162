"""One-Line Office Joke: 24-Hour Sprint — entrypoint.

Writes a single one-line office joke to /output/entry.txt.
The sealed scorer requires UTF-8 text of 1 to 200 characters,
not only whitespace, on one line.
"""

import os

JOKE = (
    "Our office printer has printed more resignation letters than HR has ever read "
    "\u2014 and unlike HR, it never asks you to stay for the exit interview."
)


def main() -> None:
    text = " ".join(JOKE.split())  # guarantee a single line
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
