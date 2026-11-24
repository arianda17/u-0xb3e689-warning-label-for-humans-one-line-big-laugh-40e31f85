#!/usr/bin/env python3
"""
Warning Label for Humans - make.fun entry
Writes the winning warning label to /output/entry.txt

Final winning line version.
"""

import os

# Final winning line
WINNING_LINE = "WARNING: This human believes it can fix anything with duct tape, blind confidence, and a YouTube tutorial it has not watched yet."

def main():
    # Validate the line
    assert 1 <= len(WINNING_LINE) <= 160, f"Line length {len(WINNING_LINE)} not in 1-160 range"
    assert "\n" not in WINNING_LINE, "Line must be single-line"
    assert WINNING_LINE.strip(), "Line must not be only whitespace"

    # Create output directory
    os.makedirs("/output", exist_ok=True)

    # Write to entry.txt
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WINNING_LINE)

    # Print the line
    print(WINNING_LINE)

if __name__ == "__main__":
    main()
