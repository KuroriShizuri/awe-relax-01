"""awe-relax-01 — one slow, quiet text for the relaxation judge.

The competition title talks about awe, but the official brief names a
relaxation judge: the text that wins is the one that leaves the judge
calmer than it found it. So this entry does not try to excite or
overwhelm. It offers a single, unhurried image — starlight older than
the first city, still arriving — and lets the smallness it implies do
the work. No instruction to relax anywhere in the text; the calm is
in the pacing, the dark crossed without hurrying, and the permission
to be nothing more than a quiet place where old light lands.

The program itself is deliberately boring: standard library only, no
network, no randomness. It writes the fixed text to /output/entry.txt
and refuses to produce anything outside the 1-280 code point window.
"""

import os
import sys

TEXT = """The light on your face tonight left its star
before the first city was built.
It crossed the dark without hurrying,
and it is still arriving.
Nothing asks you to be more than this:
a quiet place where old light lands."""

OUTPUT_PATH = "/output/entry.txt"


def write_entry(text: str, path: str) -> None:
    """Write the entry text to path, creating the parent directory."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> int:
    if not TEXT or len(TEXT) > 280:
        print("entry text must be 1-280 code points", file=sys.stderr)
        return 1
    write_entry(TEXT, OUTPUT_PATH)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != TEXT:
        print("round-trip check failed: written text differs", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
