#!/usr/bin/env python3
import os
import sys
import glob

def test_figure_pages_exist():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    figures_dir = os.path.join(wiki_root, "wiki", "figures")
    
    if not os.path.exists(figures_dir):
        print(f"Error: {figures_dir} does not exist.")
        sys.exit(1)
        
    md_files = glob.glob(os.path.join(figures_dir, "*.md"))
    if len(md_files) == 0:
        print(f"Error: No markdown files found in {figures_dir}.")
        sys.exit(1)
        
    print(f"Found {len(md_files)} figure pages.")
    sys.exit(0)

if __name__ == "__main__":
    test_figure_pages_exist()
