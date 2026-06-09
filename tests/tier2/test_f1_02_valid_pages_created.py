#!/usr/bin/env python3
import json
import os
import sys

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
MAPPING_FILE = os.path.join(BASE_DIR, "mapping.json")
WIKI_DIR = os.path.join(BASE_DIR, "wiki")

def test():
    with open(MAPPING_FILE, 'r') as f:
        mapping = json.load(f)
        
    texts_to_check = set()
    for item in mapping:
        for page in item.get("pages", []):
            if page.startswith("texts/") and not page.endswith("/"):
                texts_to_check.add(page.split("/")[1])
                
    found_texts = 0
    for text in texts_to_check:
        if os.path.exists(os.path.join(WIKI_DIR, "texts", f"{text}.md")):
            found_texts += 1
            
    if len(texts_to_check) > 0 and (found_texts / len(texts_to_check)) < 0.8:
        print(f"Boundary check failed: only {found_texts}/{len(texts_to_check)} text pages created")
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__":
    test()
