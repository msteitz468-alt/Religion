#!/usr/bin/env python3
import json
import os
import sys

def main():
    try:
        with open('mapping.json', 'r') as f:
            mappings = json.load(f)
    except Exception as e:
        print("Failed to load mapping.json:", e)
        sys.exit(1)

    if len(mappings) != 47:
        print(f"F1 failed: Expected 47 mappings, got {len(mappings)}")
        sys.exit(1)

    for mapping in mappings:
        figures = [p for p in mapping.get('pages', []) if p.startswith('figures/')]
        for fig in figures:
            path = os.path.join('wiki', fig + '.md')
            if not os.path.exists(path):
                print(f"F3 failed: Missing figure file {path}")
                sys.exit(1)
            with open(path, 'r') as f:
                content = f.read()
                if 'tags:' not in content or 'title:' not in content:
                    print(f"F3 failed: Figure {path} violates schema")
                    sys.exit(1)

    print("test_f1_f3 passed")

if __name__ == '__main__':
    main()
