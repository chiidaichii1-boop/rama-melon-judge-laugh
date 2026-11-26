#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office joke, one line.

Writes a single office joke (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
Python 3 standard library only; no network, no third-party imports.
The output is fully deterministic: the same line every run.
"""

import os

JOKE = (
    "I asked my calendar for a break, so it booked a meeting "
    "called 'Break' and invited the whole team."
)


def get_joke() -> str:
    """Return the entry line, enforcing the gate: 1-200 chars, one line."""
    line = JOKE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("joke must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    return line


def main() -> None:
    line = get_joke()

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
