#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original one-line roast of a daily gadget to
/output/entry.txt (1-200 characters, UTF-8, not only whitespace).
Standard library only, no network, no input: the line is a plain
string constant below.
"""

import os

LINE = "My robot vacuum spent a year mapping my house and still thinks the rug is a cliff."


def validate_line(line: str) -> str:
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
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
