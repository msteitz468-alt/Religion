#!/usr/bin/env python3
import os
import sys
import glob

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
TEXTS_DIR = os.path.join(BASE_DIR, "wiki", "texts")

def test():
    files = glob.glob(os.path.join(TEXTS_DIR, "*.md"))
    for fpath in files:
        size = os.path.getsize(fpath)
        if size < 50:
            print(f"File {fpath} is suspiciously small: {size} bytes")
            sys.exit(1)
        if size > 10 * 1024 * 1024:
            print(f"File {fpath} is suspiciously large: {size} bytes")
            sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
