#!/usr/bin/env python3
import os
import sys
import json

WIKI_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
MAPPING_FILE = os.path.join(WIKI_DIR, "mapping.json")

def test_mapping_exhaustive():
    if not os.path.exists(MAPPING_FILE):
        print("SKIP: mapping.json not found for exhaustive processing verification.")
        return 0
        
    with open(MAPPING_FILE, 'r') as f:
        try:
            mapping = json.load(f)
        except Exception:
            print("FAIL: mapping.json invalid JSON.")
            return 1
            
    failures = 0
    checked = 0
    for k, v in mapping.items():
        def check_paths(val):
            nonlocal failures, checked
            if isinstance(val, str) and (val.endswith('.md') or val.endswith('.json')):
                full_path = os.path.join(WIKI_DIR, val)
                if not os.path.exists(full_path):
                    print(f"FAIL: Mapped output {val} is missing.")
                    failures += 1
                checked += 1
            elif isinstance(val, dict):
                for sub_v in val.values():
                    check_paths(sub_v)
            elif isinstance(val, list):
                for item in val:
                    check_paths(item)
                    
        check_paths(v)

    if failures == 0:
        print(f"PASS: Mapping exhaustive verification succeeded. Checked {checked} expected outputs.")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(test_mapping_exhaustive())
