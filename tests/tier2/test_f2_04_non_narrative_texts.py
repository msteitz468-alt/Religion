#!/usr/bin/env python3
import os
import sys

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
TEXTS_DIR = os.path.join(BASE_DIR, "wiki", "texts")

def test():
    for target in ["proverbs.md", "psalms.md"]:
        fpath = os.path.join(TEXTS_DIR, target)
        if os.path.exists(fpath):
            with open(fpath, 'r') as f:
                content = f.read().lower()
                if "structure" not in content and "theme" not in content and "narrative" not in content:
                    print(f"Missing structural/thematic info in non-narrative text {target}")
                    sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
