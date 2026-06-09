#!/usr/bin/env python3
import os
import sys

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
INDEX_FILE = os.path.join(BASE_DIR, "wiki", "index.md")

def test():
    if not os.path.exists(INDEX_FILE):
        sys.exit(0)
        
    with open(INDEX_FILE, 'r') as f:
        content = f.read().lower()
        
    if "figure" not in content:
        print("No figures section or figure links found in index.md")
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__":
    test()
