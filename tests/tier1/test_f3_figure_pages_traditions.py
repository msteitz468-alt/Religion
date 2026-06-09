#!/usr/bin/env python3
import os
import sys
import glob

def test_figure_pages_traditions():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    figures_dir = os.path.join(wiki_root, "wiki", "figures")
    md_files = glob.glob(os.path.join(figures_dir, "*.md"))
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            
        if "tradition" not in content and "reception" not in content:
            print(f"Error: {md_file} lacks tradition-specific reception section.")
            sys.exit(1)
            
    print("All figure pages contain tradition-specific sections.")
    sys.exit(0)

if __name__ == "__main__":
    test_figure_pages_traditions()
