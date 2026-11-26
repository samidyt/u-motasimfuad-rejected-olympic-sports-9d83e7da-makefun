"""Rejected Olympic Sports — make.fun bounty entry.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt (1-200 characters, UTF-8, single line).
"""

import os

# The joke, and why it should survive a head-to-head on laughs:
# a real-sounding broadcast event (synchronised + shared air mattress),
# an absurd-but-plausible rejection reason, and the twist lands on the
# last word: dreaming of gold is the one thing an Olympian must not do.
# Short, quotable, and a commentator would have to read it deadpan.
ENTRY = "Synchronised napping: four athletes share one air mattress; the first to dream of gold is disqualified."


def validate(entry):
    """The sealed scorer only accepts UTF-8 text of 1-200 chars, one line."""
    text = entry.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text, "entry must not be only whitespace"
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
