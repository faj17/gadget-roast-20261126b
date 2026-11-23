#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original one-line roast of a daily gadget to
/output/entry.txt (1-200 characters, UTF-8, not only whitespace).
Standard library only, no network, no input.

The roast is built from two fragments: a setup (the vacuum's proudest
feature, a year spent mapping the house) and a punch (what it learned
— the rug is a cliff). ``assemble`` joins them into the single line.
"""

from pathlib import Path

SETUP = "My robot vacuum spent a year mapping my house"
PUNCH = "and still thinks the rug is a cliff."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one roast line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the roast meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
