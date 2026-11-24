#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line, the funniest thing an AI agent would say in its weekly
status report to its human, to /output/entry.txt.

Stdlib only. No network, no reads outside this file, deterministic: the
same bytes on every run.
"""

import os
import sys

# The line. Drafted and judged head-to-head against the visible field
# (see NOTES.md, rounds R0-R3): literal obedience to a vague human
# instruction, escalated to seven languages, one of them extinct, closed
# by asking the human to define the word it was told to obey.
LINE = (
    "Blockers: your instruction 'make it pop'. "
    "I made it pop in seven languages, one of them extinct. "
    "Awaiting your definition of pop."
)

MAX_CHARS = 200


def validate(text):
    """Gate mirror: UTF-8 text, 1 to 200 characters, not only whitespace,
    exactly one line."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry is %d characters, gate needs 1-200" % len(text))
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line")
    text.encode("utf-8")
    return text


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    text = validate(LINE)
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %d chars to %s" % (len(text), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
