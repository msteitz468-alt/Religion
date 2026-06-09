#!/usr/bin/env python3
import os
import sys
import glob

def test_text_pages_narrative():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    texts_dir = os.path.join(wiki_root, "wiki", "texts")
    md_files = glob.glob(os.path.join(texts_dir, "*.md"))
    
    # We expect text pages to contain narrative content, so size should be reasonable
    # and they should contain substantial text, not just frontmatter.
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parts = content.split("---")
        body = parts[2] if len(parts) >= 3 else content
        
        # Expecting at least 100 characters of body text for narrative info
        if len(body.strip()) < 100:
            print(f"Error: {md_file} body is suspiciously short, lacking narrative info.")
            sys.exit(1)
            
    print("All text pages contain substantive narrative info.")
    sys.exit(0)

if __name__ == "__main__":
    test_text_pages_narrative()
