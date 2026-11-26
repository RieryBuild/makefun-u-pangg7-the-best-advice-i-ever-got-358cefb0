# AGENT.md

This repository holds one entry for make.fun's "The Best Advice I Ever Got"
competition: a single sentence about the best advice the writer ever
received.

- `main.py` (pure Python standard library) writes the sentence to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), byte-exact with no
  trailing newline, and reads it back to verify the bytes on disk.
- Run it with `python3 main.py`. It is deterministic: the same bytes every run.
- The entry: "My maths teacher kept my failed test on his desk all term, as
  proof I could look at a bad mark without flinching." (113 characters,
  one sentence.)
