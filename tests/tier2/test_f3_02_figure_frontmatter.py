#!/usr/bin/env python3
import os
import sys
import glob
import re

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
FIGURES_DIR = os.path.join(BASE_DIR, "wiki", "figures")

def test():
    files = glob.glob(os.path.join(FIGURES_DIR, "*.md"))
    required_keys = ["title", "also_known_as", "tradition", "textual_sources", "dates", "roles", "sources_ingested", "last_updated", "tags"]
    
    for fpath in files:
        with open(fpath, 'r') as f:
            content = f.read()
            m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not m:
                print(f"Missing frontmatter in {fpath}")
                sys.exit(1)
            
            fm = m.group(1)
            for key in required_keys:
                if not re.search(rf'^{key}:', fm, re.MULTILINE):
                    print(f"Missing key {key} in {fpath}")
                    sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
