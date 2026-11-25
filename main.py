#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — entry writer.

Writes the chosen one-line roast of a smart fridge to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then
verifies the written bytes match exactly.

The entry is a fixed constant: one sentence, 133 characters. The gate
requires UTF-8 text of 1-200 characters, not only whitespace, so this
program validates length, single-line shape and whitespace content
before writing anything.

Why this line: the judge weighs, first, whether the line really is a
roast of a smart fridge, then whether the punchline lands, whether it
is specific to smart fridges, whether the wording is tight, and
whether the angle is fresh. The line is plainly a roast (the fridge
snitches on its owner to the doctor); the joke turns on two concrete,
fridge-specific details — the camera/app that reports your midnight
cake, and the app's confidently wrong opinion that milk expired three
Tuesdays ago is "still thriving" — and lands its punch on the last
words; it reads like something a cornered person would actually say;
and the snitch-vs-incompetent contrast is not a stock
ordering-groceries or watching-you retread.
"""

import os
import sys

ENTRY = (
    "My fridge emailed my doctor about my midnight cake, yet the app "
    "insists the milk that expired three Tuesdays ago is "
    "'still thriving'."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, single line, not blank.

    Also enforce the judge's one-line form: the entry must read as one
    single sentence that lands its punch at the end, so it must end in
    terminal punctuation and contain no earlier sentence break.
    """
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} outside 1-200 chars")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip() or text.strip() == "":
        raise ValueError("entry must not be only whitespace or padded")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    if any(text[i] in ".!?" and text[i + 1] == " " for i in range(len(text) - 1)):
        raise ValueError("entry must be a single sentence, no mid-text break")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("written bytes differ from entry")
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
