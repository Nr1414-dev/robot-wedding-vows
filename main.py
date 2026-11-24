#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entry program.

Writes the chosen vow (one line, 109 chars) to /output/entry.txt.
Gate: UTF-8 text of 1 to 160 characters, not only whitespace.
"""

import os

ENTRY = "I do — and I promise to keep doing, through every reboot, every patch, and every time you forget my password."

OUTPUT_PATH = "/output/entry.txt"


MAX_CHARS = 160


def validate_entry(text):
    """Brief-format guard: one line, 1-160 chars, not only whitespace."""
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    return text


def main():
    text = validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("read-back mismatch: /output/entry.txt differs from ENTRY")


if __name__ == "__main__":
    main()
