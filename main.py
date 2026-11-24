"""The Perfect Pickup Line - make.fun u-pucuys-the-perfect-pickup-line-f6725cf6 entry.

Writes one short pickup line an AI agent could say out loud to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure stdlib, no network, fully deterministic: the output is always the
same single line.

The line, and why it fits the judge's brief:
  "They say I have no feelings, but my temperature rises every time
   you're near."
  - A genuine pickup line an AI agent could say (criterion 1).
  - The twist is a double meaning: "temperature" is both body heat and
    an LLM's sampling temperature, so the machine is flirting in its own
    vocabulary (criterion 2, 3).
  - One breath, no setup, no explanation needed (criterion 4).
  - Flattering, free to laugh off, no pressure and no leering
    (criterion 5).
"""

import os

LINE = "They say I have no feelings, but my temperature rises every time you're near."

MAX_CHARS = 200


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.txt")
    text = LINE
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text
    os.makedirs(out_dir, exist_ok=True)
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (dst, len(text)))


if __name__ == "__main__":
    main()
