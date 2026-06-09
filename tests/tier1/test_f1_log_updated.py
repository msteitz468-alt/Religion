#!/usr/bin/env python3
import os
import json
import sys

def test_log_updated():
    wiki_root = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
    mapping_path = os.path.join(wiki_root, "mapping.json")
    log_path = os.path.join(wiki_root, "wiki", "log.md")
    
    if not os.path.exists(log_path):
        print(f"Error: {log_path} does not exist.")
        sys.exit(1)
        
    with open(log_path, 'r', encoding='utf-8') as f:
        log_content = f.read()
        
    with open(mapping_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Verify that the log has significant content (e.g. at least mentions multiple sources)
    sources_found = 0
    for item in data:
        # Just check a portion of the source title in case of slight changes
        short_title = item["source_title"].split('.')[0]
        if short_title in log_content:
            sources_found += 1
            
    if sources_found < len(data) // 2: # At least half should be explicitly named in log
        print(f"Error: Expected log to contain sources. Found {sources_found}/{len(data)}")
        sys.exit(1)
        
    print("log.md contains records of ingested sources.")
    sys.exit(0)

if __name__ == "__main__":
    test_log_updated()
