"""The Meeting That Should Have Been One Line — the single sentence
that could have replaced an entire pointless meeting.

Pure Python stdlib. Writes exactly one line (131 characters) to
/output/entry.txt.
"""

import os

# The competition gate: the entry must be 1-200 characters.
MAX_LEN = 200

LINE = (
    "We're pushing the launch by two weeks because nobody in this meeting "
    "has the authority to approve anything, including this meeting."
)


def main():
    assert 1 <= len(LINE) <= MAX_LEN, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
