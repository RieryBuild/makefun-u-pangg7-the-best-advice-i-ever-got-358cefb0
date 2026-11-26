"""Write the competition entry: one sentence about the best advice received.

The entry is built from two clauses -- the remembered moment, then the
lesson it carries -- joined into a single sentence. The program writes it
byte-exact, with no trailing newline, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), then reads it back to prove the bytes on disk match.
Pure standard library.
"""

import os

# The moment: what the teacher did. The lesson: what it proved.
_CLAUSES = [
    "My maths teacher kept my failed test on his desk all term",
    "as proof I could look at a bad mark without flinching",
]

ENTRY = ", ".join(_CLAUSES) + "."


def validate_entry(text):
    """Gate-check the entry before writing: 1-200 chars, one sentence."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text.strip() != text or not text.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    # Exactly one sentence terminator, and it must end the sentence.
    terminators = [c for c in text if c in ".!?"]
    if len(terminators) != 1 or not text.endswith(terminators[0]):
        raise ValueError("entry must be exactly one sentence")
    return text


def write_entry(output_dir):
    entry = validate_entry(ENTRY)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != entry:
            raise ValueError("entry.txt on disk does not match the entry")
    return path


def main():
    path = write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    print("wrote %s (%d chars)" % (path, len(ENTRY)))


if __name__ == "__main__":
    main()
