#!/usr/bin/env python3
import os
import sys
import glob
import re

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
FIGURES_DIR = os.path.join(BASE_DIR, "wiki", "figures")

def test():
    files = glob.glob(os.path.join(FIGURES_DIR, "*.md"))
    for fpath in files:
        with open(fpath, 'r') as f:
            content = f.read()
            m = re.search(r'^tags:\s*\[?(.*?)\]?$', content, re.MULTILINE)
            if m:
                tags = m.group(1).lower()
                if 'figure' not in tags:
                    print(f"Missing 'figure' tag in {fpath}")
                    sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
