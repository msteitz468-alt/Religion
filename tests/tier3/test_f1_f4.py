#!/usr/bin/env python3
import json
import os
import sys

def main():
    try:
        with open('mapping.json', 'r') as f:
            mappings = json.load(f)
        with open('wiki/index.md', 'r') as f:
            index_content = f.read()
    except Exception as e:
        print("Failed to read files:", e)
        sys.exit(1)

    if len(mappings) != 47:
        print(f"F1 failed: Expected 47 mappings, got {len(mappings)}")
        sys.exit(1)

    for mapping in mappings:
        figures = [os.path.basename(p) for p in mapping.get('pages', []) if p.startswith('figures/')]
        for fig in figures:
            if f"[[{fig}|" not in index_content and f"[[{fig}]]" not in index_content:
                print(f"F4 failed: Figure {fig} not in index.md")
                sys.exit(1)

    print("test_f1_f4 passed")

if __name__ == '__main__':
    main()
