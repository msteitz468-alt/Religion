#!/usr/bin/env python3
import os
import sys
import re

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
INDEX_FILE = os.path.join(BASE_DIR, "wiki", "index.md")
WIKI_DIR = os.path.join(BASE_DIR, "wiki")

def test():
    if not os.path.exists(INDEX_FILE):
        sys.exit(0)
        
    with open(INDEX_FILE, 'r') as f:
        content = f.read()
        
    links = re.findall(r'\[\[(figures/[^|\]]+)(?:\|.*?)?\]\]', content)
    for link in links:
        fpath = os.path.join(WIKI_DIR, f"{link}.md")
        if not os.path.exists(fpath):
            print(f"Broken link in index: {link}")
            sys.exit(1)
            
    sys.exit(0)

if __name__ == "__main__":
    test()
