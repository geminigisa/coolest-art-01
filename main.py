"""Coolest Art entry: copy the bundled art to the output directory.

Deterministic: a plain byte copy, no network, no clock, no randomness.
The art (entry.png, a JPEG file) sits beside this file in the repo.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

src = os.path.join(HERE, "entry.png")
dst = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(src, dst)

# Fail loudly instead of silently shipping a partial file: the output
# must be byte-identical to the bundled art.
if os.path.getsize(dst) != os.path.getsize(src):
    print("error: output size differs from bundled art", file=sys.stderr)
    sys.exit(1)
