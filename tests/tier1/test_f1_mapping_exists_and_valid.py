#!/usr/bin/env python3
import os
import json
import sys

def test_mapping_exists_and_valid():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    mapping_path = os.path.join(wiki_root, "mapping.json")
    
    if not os.path.exists(mapping_path):
        print(f"Error: {mapping_path} does not exist.")
        sys.exit(1)
        
    try:
        with open(mapping_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            print("Error: mapping.json does not contain a JSON array.")
            sys.exit(1)
    except Exception as e:
        print(f"Error reading mapping.json: {e}")
        sys.exit(1)
        
    print("mapping.json exists and is valid JSON.")
    sys.exit(0)

if __name__ == "__main__":
    test_mapping_exists_and_valid()
