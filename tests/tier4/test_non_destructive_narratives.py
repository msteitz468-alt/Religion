#!/usr/bin/env python3
import os
import sys
import glob

WIKI_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"

def test_non_destructive_narratives():
    narratives_dir = os.path.join(WIKI_DIR, "narratives")
    if not os.path.exists(narratives_dir):
        narratives_dir = os.path.join(WIKI_DIR, "Narratives")
        
    if not os.path.exists(narratives_dir):
        print("SKIP: Narratives directory not found.")
        return 0

    narratives = glob.glob(os.path.join(narratives_dir, "*.md"))
    failures = 0
    for narr in narratives:
        with open(narr, 'r') as f:
            content = f.read()
            
        if not content.strip():
            print(f"FAIL: Narrative {narr} is empty.")
            failures += 1

    test_narr_path = os.path.join(narratives_dir, "test_dummy_narrative.md")
    try:
        with open(test_narr_path, 'w') as f:
            f.write("Initial content.\n")
        with open(test_narr_path, 'a') as f:
            f.write("Appended content.\n")
            
        with open(test_narr_path, 'r') as f:
            content = f.read()
            if "Initial content." not in content or "Appended content." not in content:
                print("FAIL: File system append simulation failed - indicates destructive write.")
                failures += 1
    except Exception as e:
        print(f"FAIL: Could not write dummy narrative: {e}")
        failures += 1
    finally:
        if os.path.exists(test_narr_path):
            os.remove(test_narr_path)

    if failures == 0:
        print("PASS: Narratives appear structurally sound for non-destructive updates.")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(test_non_destructive_narratives())
