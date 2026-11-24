"""Everyday Things, Two Lines: a swing, explained to a 10-year-old.

Writes the two-line entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Line 1: one vivid sentence, one analogy -- a swing as a chair tied to
the sky that lets you borrow the wind.
Line 2: one honest sentence -- what the analogy maps (the flying
feeling, the back and forth) and what it leaves out (the chains and
the push; a swing cannot move on its own).
"""

import os
from pathlib import Path

ENTRY = (
    "A swing is a chair tied to the sky that lets you borrow the wind "
    "for a few seconds.\n"
    "It maps the flying feeling and the going back and forth, but it "
    "leaves out the chains and the push -- a swing can't move without "
    "someone's legs or hands.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(ENTRY.encode("utf-8"))
    # Byte-exact read-back gate: what lands on disk must be the entry,
    # byte for byte -- no trailing-newline drift, no encoding surprise.
    if target.read_bytes() != ENTRY.encode("utf-8"):
        raise SystemExit("entry.txt read-back mismatch")
    lines = ENTRY.strip().split("\n")
    if len(lines) != 2:
        raise SystemExit(f"expected 2 lines, got {len(lines)}")
    if not 1 <= len(ENTRY) <= 400:
        raise SystemExit(f"entry length {len(ENTRY)} outside 1-400")
    print(f"Wrote {target} ({len(ENTRY)} chars, 2 lines)")


if __name__ == "__main__":
    main()
