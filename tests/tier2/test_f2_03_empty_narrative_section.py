#!/usr/bin/env python3
import os
import sys
import glob
import re

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
TEXTS_DIR = os.path.join(BASE_DIR, "wiki", "texts")

def test():
    files = glob.glob(os.path.join(TEXTS_DIR, "*.md"))
    for fpath in files:
        with open(fpath, 'r') as f:
            content = f.read()
            if re.search(r'(?i)##\s*narrative[^\n]*\n+\s*##', content):
                print(f"Empty narrative section in {fpath}")
                sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
