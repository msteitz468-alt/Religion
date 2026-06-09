#!/usr/bin/env python3
import json
import os
import sys
import re

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
MAPPING_FILE = os.path.join(BASE_DIR, "mapping.json")
LOG_FILE = os.path.join(BASE_DIR, "wiki", "log.md")

def test():
    if not os.path.exists(MAPPING_FILE):
        print("mapping.json not found")
        sys.exit(1)
        
    with open(MAPPING_FILE, 'r') as f:
        mapping = json.load(f)
        
    if len(mapping) != 47:
        print(f"Expected 47 items in mapping.json, found {len(mapping)}")
        sys.exit(1)
        
    if not os.path.exists(LOG_FILE):
        print("log.md not found")
        sys.exit(1)
        
    with open(LOG_FILE, 'r') as f:
        log_content = f.read()
        
    ingest_count = len(re.findall(r'(?i)##.*?ingest', log_content))
    if ingest_count < 40:
        print(f"Boundary check failed: expected close to 47 ingests, found {ingest_count}")
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__":
    test()
