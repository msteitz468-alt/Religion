#!/usr/bin/env python3
import os
import sys
import glob

def test_text_pages_exist():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    texts_dir = os.path.join(wiki_root, "wiki", "texts")
    
    if not os.path.exists(texts_dir):
        print(f"Error: {texts_dir} does not exist.")
        sys.exit(1)
        
    md_files = glob.glob(os.path.join(texts_dir, "*.md"))
    if len(md_files) == 0:
        print(f"Error: No markdown files found in {texts_dir}.")
        sys.exit(1)
        
    print(f"Found {len(md_files)} text pages.")
    sys.exit(0)

if __name__ == "__main__":
    test_text_pages_exist()
