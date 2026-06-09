#!/usr/bin/env python3
import os
import sys
import glob

def test_text_pages_yaml():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    texts_dir = os.path.join(wiki_root, "wiki", "texts")
    md_files = glob.glob(os.path.join(texts_dir, "*.md"))
    
    required_fields = ["title:", "tradition:", "canon_status:"]
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if not content.startswith("---"):
            print(f"Error: {md_file} missing YAML frontmatter.")
            sys.exit(1)
            
        header = content.split("---")[1] if len(content.split("---")) > 1 else ""
        
        for field in required_fields:
            if field not in header:
                print(f"Error: {md_file} YAML missing '{field}'.")
                sys.exit(1)
                
    print("All text pages have required YAML frontmatter.")
    sys.exit(0)

if __name__ == "__main__":
    test_text_pages_yaml()
