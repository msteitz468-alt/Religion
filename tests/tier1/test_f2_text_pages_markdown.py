#!/usr/bin/env python3
import os
import sys
import glob

def test_text_pages_markdown():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    texts_dir = os.path.join(wiki_root, "wiki", "texts")
    
    # Verify no unexpected non-markdown files in this content directory
    all_files = glob.glob(os.path.join(texts_dir, "*"))
    for file_path in all_files:
        if os.path.isfile(file_path):
            if not file_path.endswith(".md"):
                print(f"Error: Non-markdown file found in texts directory: {file_path}")
                sys.exit(1)
                
    print("All files in texts/ are valid markdown files.")
    sys.exit(0)

if __name__ == "__main__":
    test_text_pages_markdown()
