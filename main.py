#!/usr/bin/env python3
"""Write the 21 November 2026 world-news image to /output/entry.png.

Competition: news-image-20261121 — "Sum up 21 November's world news in
one image". The finished front-page collage is entry.png beside this
file (drawn by make_image.py at build time); this program copies it to
the output directory, byte for byte, using only the standard library.
It runs with no network and writes the same bytes on every run.
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    data = SOURCE.read_bytes()
    # Gate sanity: a whole PNG of at most 1 MiB.
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    assert len(data) <= 1_048_576, f"entry.png too large: {len(data)} bytes"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
