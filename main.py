"""Coolest Art entry: copy the bundled art to the output directory.

Deterministic: a plain byte copy, no network, no clock, no randomness.
The art (entry.png, a JPEG file) sits beside this file in the repo.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT_DIR, "entry.png"))
