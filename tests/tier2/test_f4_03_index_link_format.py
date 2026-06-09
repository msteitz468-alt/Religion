#!/usr/bin/env python3
import os
import sys
import re

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
INDEX_FILE = os.path.join(BASE_DIR, "wiki", "index.md")

def test():
    if not os.path.exists(INDEX_FILE):
        sys.exit(0)
        
    with open(INDEX_FILE, 'r') as f:
        content = f.read()
        
    links = re.findall(r'\[\[(.*?)\]\]', content)
    for link in links:
        if '|' in link:
            parts = link.split('|')
            if len(parts) > 2:
                print(f"Malformed link with multiple pipes: {link}")
                sys.exit(1)
            if not parts[0].strip() or not parts[1].strip():
                print(f"Malformed link with empty parts: {link}")
                sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
