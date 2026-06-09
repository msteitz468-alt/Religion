#!/usr/bin/env python3
import os
import sys

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
WIKI_DIR = os.path.join(BASE_DIR, "wiki")

def test():
    index_file = os.path.join(WIKI_DIR, "index.md")
    if not os.path.exists(index_file):
        print("index.md not found")
        sys.exit(1)
    
    bad_dir = os.path.join(WIKI_DIR, "-wisdom")
    if os.path.exists(bad_dir):
        print("Wiki created a malformed directory '-wisdom' from bad JSON!")
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__":
    test()
