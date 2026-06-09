#!/usr/bin/env python3
import os
import sys
import json

WIKI_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"

def main():
    mapping_file = os.path.join(WIKI_DIR, "mapping.json")
    with open(mapping_file, "r") as f:
        mapping = json.load(f)
        
    valid_categories = ["texts", "commentators", "figures", "concepts", "traditions", "comparisons", "controversies", "timelines"]
    
    missing_pages = []
    
    for record in mapping:
        for page in record.get("pages", []):
            parts = page.split("/")
            if len(parts) == 2 and parts[0] in valid_categories:
                filepath = os.path.join(WIKI_DIR, "wiki", parts[0], parts[1] + ".md")
                if not os.path.exists(filepath):
                    missing_pages.append(page)
                    
    if missing_pages:
        print(f"FAIL: Missing {len(missing_pages)} expected valid outputs from mapping.json")
        for p in missing_pages[:10]:
            print("Missing:", p)
        sys.exit(1)
        
    print("PASS: All valid mapping.json expected outputs are present.")
    sys.exit(0)

if __name__ == "__main__":
    main()
