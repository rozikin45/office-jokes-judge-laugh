"""Office-jokes entry: one line about office life, written to /output/entry.txt.

The joke: reply-all hell. Someone asks to be removed from a runaway
email thread, and the thread "promotes" them to admin instead of letting
them go -- the only promotion the office ever hands out. The setup is a
universal office pain (the thread nobody can escape), the turn lands at
the end (removed -> admin -> promotion), and every word earns its place.

The line is a constant string, so the program is fully deterministic:
no randomness, no clock, no network. Every run writes the exact same
text to entry.txt in the output directory.
"""

import os
from pathlib import Path

LINE = "I hit reply-all to ask to be removed from the thread, and now I'm the admin \u2014 the only promotion I've ever gotten here."

# Gate the competition seals: UTF-8 text of 1 to 199 characters, one line,
# not only white space. Fail loudly instead of writing an invalid entry.
assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate needs 1-199"
assert LINE.count("\n") == 0 and LINE.strip(), "line must be a single non-blank line"

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(LINE, encoding="utf-8")
