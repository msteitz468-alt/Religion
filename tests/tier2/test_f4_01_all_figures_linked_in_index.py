#!/usr/bin/env python3
import os
import sys
import glob

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
FIGURES_DIR = os.path.join(BASE_DIR, "wiki", "figures")
INDEX_FILE = os.path.join(BASE_DIR, "wiki", "index.md")

def test():
    if not os.path.exists(INDEX_FILE):
        sys.exit(0)
        
    with open(INDEX_FILE, 'r') as f:
        index_content = f.read()
        
    files = glob.glob(os.path.join(FIGURES_DIR, "*.md"))
    for fpath in files:
        basename = os.path.basename(fpath).replace('.md', '')
        if basename not in index_content:
            print(f"Figure {basename} not found in index.md")
            sys.exit(1)
            
    sys.exit(0)

if __name__ == "__main__":
    test()
