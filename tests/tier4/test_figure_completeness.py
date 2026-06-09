#!/usr/bin/env python3
import os
import sys
import glob

WIKI_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"

def test_figure_completeness():
    figures_dir = os.path.join(WIKI_DIR, "figures")
    if not os.path.exists(figures_dir):
        figures_dir = os.path.join(WIKI_DIR, "Figures")
    
    if not os.path.exists(figures_dir):
        print("SKIP: Figures directory not found.")
        return 0

    figures = glob.glob(os.path.join(figures_dir, "*.md"))
    if not figures:
        print("SKIP: No figures found.")
        return 0
        
    failures = 0
    for fig in figures:
        with open(fig, 'r') as f:
            content = f.read()
            
        if "---" not in content:
            print(f"FAIL: Figure {fig} lacks YAML frontmatter.")
            failures += 1
            
        if "# " not in content:
            print(f"FAIL: Figure {fig} lacks a top-level header.")
            failures += 1

    index_files = glob.glob(os.path.join(WIKI_DIR, "*Index*.md")) + glob.glob(os.path.join(WIKI_DIR, "Indices", "*.md"))
    if not index_files:
        print("FAIL: No index files found in the wiki.")
        failures += 1
        
    if failures == 0:
        print(f"PASS: {len(figures)} figures validated for completeness and index presence.")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(test_figure_completeness())
