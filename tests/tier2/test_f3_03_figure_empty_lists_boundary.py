#!/usr/bin/env python3
import os
import sys
import glob

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
FIGURES_DIR = os.path.join(BASE_DIR, "wiki", "figures")

def test():
    files = glob.glob(os.path.join(FIGURES_DIR, "*.md"))
    for fpath in files:
        with open(fpath, 'r') as f:
            content = f.read()
            parts = content.split('---')
            if len(parts) >= 3:
                fm = parts[1]
                for line in fm.split('\n'):
                    if ':' in line:
                        _, val = line.split(':', 1)
                        val = val.strip()
                        if val.startswith('[') and not val.endswith(']'):
                            print(f"Malformed list in {fpath}: {line}")
                            sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
