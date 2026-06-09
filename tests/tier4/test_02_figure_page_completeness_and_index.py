#!/usr/bin/env python3
import os
import sys

WIKI_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"

def main():
    figures_dir = os.path.join(WIKI_DIR, "wiki", "figures")
    index_path = os.path.join(WIKI_DIR, "wiki", "index.md")
    
    with open(index_path, "r") as f:
        index_content = f.read()
        
    md_files = [f for f in os.listdir(figures_dir) if f.endswith(".md")]
    
    for md_file in md_files:
        filepath = os.path.join(figures_dir, md_file)
        with open(filepath, "r") as f:
            content = f.read()
            
        if not content.startswith("---"):
            print(f"File {md_file} lacks frontmatter")
            sys.exit(1)
            
        parts = content.split("---", 2)
        if len(parts) < 3 or len(parts[2].strip()) == 0:
            print(f"File {md_file} has no narrative body")
            sys.exit(1)
            
        basename = md_file[:-3]
        if basename not in index_content:
            print(f"File {basename} not linked in index.md")
            sys.exit(1)

    print("PASS: Figure page completeness and index presence validated.")
    sys.exit(0)

if __name__ == "__main__":
    main()
