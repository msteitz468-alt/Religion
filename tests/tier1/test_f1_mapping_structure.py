#!/usr/bin/env python3
import os
import json
import sys

def test_mapping_structure():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    mapping_path = os.path.join(wiki_root, "mapping.json")
    
    with open(mapping_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for i, item in enumerate(data):
        for field in ["source_title", "raw_file", "pages"]:
            if field not in item:
                print(f"Item {i} is missing field '{field}'.")
                sys.exit(1)
        if not isinstance(item["pages"], list):
            print(f"Item {i} 'pages' field is not a list.")
            sys.exit(1)
            
    print("All items in mapping.json have the correct structure.")
    sys.exit(0)

if __name__ == "__main__":
    test_mapping_structure()
