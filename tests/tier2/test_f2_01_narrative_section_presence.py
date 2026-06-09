#!/usr/bin/env python3
import os
import sys
import glob

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
TEXTS_DIR = os.path.join(BASE_DIR, "wiki", "texts")

def test():
    files = glob.glob(os.path.join(TEXTS_DIR, "*.md"))
    if not files:
        sys.exit(0)
        
    missing_narrative = []
    for fpath in files:
        with open(fpath, 'r') as f:
            content = f.read().lower()
            if "narrative" not in content and "structure" not in content:
                missing_narrative.append(os.path.basename(fpath))
                
    if len(files) > 0 and len(missing_narrative) / len(files) > 0.3:
        print(f"Too many texts missing narrative info: {len(missing_narrative)}")
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__":
    test()
