#!/usr/bin/env python3
import os
import sys
import glob

def test_text_pages_links():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    texts_dir = os.path.join(wiki_root, "wiki", "texts")
    md_files = glob.glob(os.path.join(texts_dir, "*.md"))
    
    # Test that pages contain internal wiki links like [[something]]
    # Since they should link to commentators or figures
    pages_with_links = 0
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "[[" in content and "]]" in content:
            pages_with_links += 1
            
    # At least most texts should have cross-references
    if pages_with_links < len(md_files) * 0.8:
        print(f"Error: Too few text pages have internal links. Found links in {pages_with_links}/{len(md_files)}")
        sys.exit(1)
        
    print("Text pages contain appropriate cross-references.")
    sys.exit(0)

if __name__ == "__main__":
    test_text_pages_links()
