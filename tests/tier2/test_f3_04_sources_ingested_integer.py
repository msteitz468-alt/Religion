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
            m = re.search(r'^sources_ingested:\s*"?(\d+)"?', content, re.MULTILINE)
            if not m:
                empty_m = re.search(r'^sources_ingested:\s*$', content, re.MULTILINE)
                if not empty_m:
                    print(f"Invalid or missing sources_ingested in {fpath}")
                    sys.exit(1)
            else:
                count = int(m.group(1))
                if count < 0:
                    sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
