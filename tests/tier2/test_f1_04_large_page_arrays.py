#!/usr/bin/env python3
import os
import sys

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
WIKI_DIR = os.path.join(BASE_DIR, "wiki")

def test():
    unterman_file = os.path.join(WIKI_DIR, "commentators", "isaac-unterman.md")
    rashi_file = os.path.join(WIKI_DIR, "commentators", "rashi.md")
    
    if not (os.path.exists(unterman_file) or os.path.exists(rashi_file)):
        comm_dir = os.path.join(WIKI_DIR, "commentators")
        if os.path.exists(comm_dir) and len(os.listdir(comm_dir)) < 5:
            print("Failed to process large page arrays effectively.")
            sys.exit(1)
            
    sys.exit(0)

if __name__ == "__main__":
    test()
