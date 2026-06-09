#!/usr/bin/env python3
import os
import sys
import re

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
WIKI_DIR = os.path.join(BASE_DIR, "wiki")

def test():
    genesis_file = os.path.join(WIKI_DIR, "texts", "genesis.md")
    if os.path.exists(genesis_file):
        with open(genesis_file, 'r') as f:
            content = f.read()
        m = re.search(r'sources_ingested:\s*(\d+)', content)
        if m:
            count = int(m.group(1))
            if count < 1:
                print("sources_ingested should be >= 1")
                sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
