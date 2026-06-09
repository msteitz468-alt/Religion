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
        texts = [p for p in mapping.get('pages', []) if p.startswith('texts/')]
        for text in texts:
            path = os.path.join('wiki', text + '.md')
            if not os.path.exists(path):
                print(f"F2 failed: File {path} missing")
                sys.exit(1)
            with open(path, 'r') as f:
                content = f.read()
                if len(content) < 50:
                    print(f"F2 failed: File {path} might be destructively modified")
                    sys.exit(1)

    print("test_f1_f2 passed")

if __name__ == '__main__':
    main()
