#!/usr/bin/env python3
import os
import json
import sys

def test_mapping_count():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    mapping_path = os.path.join(wiki_root, "mapping.json")
    
    with open(mapping_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    if len(data) != 47:
        print(f"Expected 47 items in mapping.json, found {len(data)}")
        sys.exit(1)
        
    print("mapping.json contains 47 items.")
    sys.exit(0)

if __name__ == "__main__":
    test_mapping_count()
