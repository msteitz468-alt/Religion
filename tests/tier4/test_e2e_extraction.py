#!/usr/bin/env python3
import os
import sys
import json

WIKI_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
MAPPING_FILE = os.path.join(WIKI_DIR, "mapping.json")

def test_e2e_extraction():
    if not os.path.exists(MAPPING_FILE):
        print("SKIP: mapping.json not found.")
        return 0
    
    with open(MAPPING_FILE, 'r') as f:
        try:
            mapping = json.load(f)
        except Exception:
            print("FAIL: mapping.json is invalid JSON.")
            return 1
            
    failures = 0
    for raw_file, outputs in mapping.items():
        if isinstance(outputs, dict):
            fig_path = outputs.get("figure")
            narr_path = outputs.get("narrative")
            
            if fig_path and not os.path.exists(os.path.join(WIKI_DIR, fig_path)):
                print(f"FAIL: Expected figure {fig_path} for raw file {raw_file} does not exist.")
                failures += 1
                
            if narr_path and not os.path.exists(os.path.join(WIKI_DIR, narr_path)):
                print(f"FAIL: Expected narrative {narr_path} for raw file {raw_file} does not exist.")
                failures += 1

    if failures == 0:
        print("PASS: E2E extraction validated based on mapping.json.")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(test_e2e_extraction())
