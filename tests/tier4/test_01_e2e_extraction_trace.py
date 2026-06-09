#!/usr/bin/env python3
import json
import os
import sys

WIKI_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"

def main():
    mapping_file = os.path.join(WIKI_DIR, "mapping.json")
    with open(mapping_file, "r") as f:
        mapping = json.load(f)

    # Find the record for "Moo, Douglas J. *The Letter of James*"
    record = next((r for r in mapping if "The Letter of James" in r.get("source_title", "") and "Moo" in r.get("source_title", "")), None)
    if not record:
        print("Record not found in mapping.json")
        sys.exit(1)

    # Trace 1: Mapping says it maps to figures/james-the-just
    if "figures/james-the-just" not in record["pages"]:
        print("Mapping does not list figures/james-the-just")
        sys.exit(1)

    # Trace 2: Figure file exists
    figure_path = os.path.join(WIKI_DIR, "wiki", "figures", "james-the-just.md")
    if not os.path.exists(figure_path):
        print("Figure page does not exist")
        sys.exit(1)

    # Trace 3: Narrative includes Moo
    with open(figure_path, "r") as f:
        content = f.read()
    if "Moo" not in content:
        print("Narrative does not mention Moo")
        sys.exit(1)

    # Trace 4: Index contains james-the-just
    index_path = os.path.join(WIKI_DIR, "wiki", "index.md")
    with open(index_path, "r") as f:
        index_content = f.read()
    
    if "james-the-just" not in index_content.lower():
        print("Index does not contain james-the-just")
        sys.exit(1)

    print("PASS: E2E extraction trace validated.")
    sys.exit(0)

if __name__ == "__main__":
    main()
