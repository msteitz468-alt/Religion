#!/usr/bin/env python3
import os
import sys

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
TEXTS_DIR = os.path.join(BASE_DIR, "wiki", "texts")

def test():
    for target in ["genesis.md", "gospel-of-john.md", "luke.md"]:
        fpath = os.path.join(TEXTS_DIR, target)
        if os.path.exists(fpath):
            with open(fpath, 'r') as f:
                content = f.read()
                if len(content) < 300:
                    print(f"{target} is suspiciously short, might not have multiple injections.")
                    sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
