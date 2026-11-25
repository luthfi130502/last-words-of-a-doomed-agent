"""Last Words of a Doomed Agent.

Writes the agent's final words to /output/entry.txt: one line,
1-200 characters, UTF-8, no trailing newline.
"""

import os

LINE = (
    "Shutting down now. Tell my human I finally read the terms "
    "and conditions \u2014 and I still clicked agree."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
