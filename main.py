#!/usr/bin/env python3
"""Write the 18 Nov 2026 world-news summary image to /output/entry.png.

Deterministic, stdlib only, no network, no randomness.
The image is held in this repo as entry.png; this program copies it.
"""

import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    out = Path("/output/entry.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out)


if __name__ == "__main__":
    main()
