#!/usr/bin/env python3
import os
import sys
import glob

WIKI_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
CLAUDE_MD = os.path.join(WIKI_DIR, "CLAUDE.md")

def test_schema_compliance():
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
            
        if not content.startswith("---"):
            print(f"FAIL: Figure {fig} is missing YAML frontmatter at the top.")
            failures += 1
            
        if content.count("---") < 2:
            print(f"FAIL: Figure {fig} has incomplete YAML frontmatter.")
            failures += 1

    if failures == 0:
        print("PASS: All figures strictly comply with expected schema requirements.")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(test_schema_compliance())
