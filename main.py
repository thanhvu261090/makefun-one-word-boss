#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt.

The word: Ghostboss — the boss who is never there when you need them,
and only materialises to haunt you at review time.
"""

import os

ENTRY = "Ghostboss"

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 30


def gate_check(word: str) -> None:
    """Enforce the kit's entry gate exactly.

    The sealed scorer requires /output/entry.txt to be UTF-8 text of
    1 to 30 characters, not only white space. The brief adds: a single
    word, no spaces, no sentence, no explanation.
    """
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(word) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1 to {MAX_CHARS} characters, got {len(word)}"
        )
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("entry must contain no control characters")
    if not any(ch.isalpha() for ch in word):
        raise ValueError("entry must contain at least one letter")
    word.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    gate_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"Wrote {len(ENTRY)}-character entry to {OUTPUT_PATH}: {ENTRY}")


if __name__ == "__main__":
    main()
