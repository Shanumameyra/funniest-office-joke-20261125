#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — entry.

Writes a single original one-line joke about office life to
/output/entry.txt, as required by the bounty rules
(UTF-8 text, 1-200 characters, one line, punchline last).
"""

import os

JOKE = (
    "The fire drill was the only meeting all year where everyone showed "
    "up on time, left early, and nobody asked for the slides."
)


def main() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, f"joke is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "joke must be a single line"
    assert line == line.strip(), "joke must not start or end with whitespace"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        # Sandbox without a writable /output: keep a local copy for inspection.
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read it back and confirm the file holds exactly the one line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt does not match the joke exactly"
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
