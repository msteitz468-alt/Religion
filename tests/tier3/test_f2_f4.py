#!/usr/bin/env python3
import os
import sys
import glob

def main():
    try:
        with open('wiki/index.md', 'r') as f:
            index_content = f.read()
    except Exception as e:
        print("Failed to read index.md:", e)
        sys.exit(1)

    text_files = glob.glob('wiki/texts/*.md')
    if not text_files:
        print("F2 failed: No text files found")
        sys.exit(1)

    for text in text_files:
        with open(text, 'r') as f:
            if len(f.read()) < 50:
                print(f"F2 failed: Text file {text} might be destroyed")
                sys.exit(1)

    if "## Texts" not in index_content or "## Figures" not in index_content:
        print("F4 failed: index.md missing essential sections")
        sys.exit(1)

    print("test_f2_f4 passed")

if __name__ == '__main__':
    main()
