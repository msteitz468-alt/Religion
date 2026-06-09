#!/usr/bin/env python3
import os
import sys

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
INDEX_FILE = os.path.join(BASE_DIR, "wiki", "index.md")

def test():
    if not os.path.exists(INDEX_FILE):
        sys.exit(0)
        
    with open(INDEX_FILE, 'r') as f:
        lines = f.readlines()
        
    if len(lines) < 20:
        print(f"index.md is too short: {len(lines)} lines. Expected hundreds of entries.")
        sys.exit(1)
        
    headings = [line for line in lines if line.startswith("#")]
    if len(headings) < 2:
        print("index.md lacks structural headings.")
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__":
    test()
