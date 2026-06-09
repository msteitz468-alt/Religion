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

    figure_files = glob.glob('wiki/figures/*.md')
    if not figure_files:
        print("F3 failed: No figure pages found")
        sys.exit(1)

    for fig in figure_files:
        basename = os.path.basename(fig)
        name = os.path.splitext(basename)[0]

        with open(fig, 'r') as f:
            content = f.read()
            if 'title:' not in content or 'tags:' not in content:
                print(f"F3 failed: Figure {fig} does not match schema")
                sys.exit(1)

        if f"[[{name}|" not in index_content and f"[[{name}]]" not in index_content:
            print(f"F4 failed: Figure {name} not found in index.md")
            sys.exit(1)

    print("test_f3_f4 passed")

if __name__ == '__main__':
    main()
