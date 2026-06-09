#!/usr/bin/env python3
import os
import sys
import glob
import re

def main():
    text_files = glob.glob('wiki/texts/*.md')
    if not text_files:
        print("F2 failed: No text pages found")
        sys.exit(1)

    figure_files = glob.glob('wiki/figures/*.md')
    figures = set([os.path.splitext(os.path.basename(f))[0] for f in figure_files])

    linked_figures = set()
    for text in text_files:
        with open(text, 'r') as f:
            content = f.read()
            if len(content) < 50:
                print(f"F2 failed: {text} is too short, possibly destructively modified")
                sys.exit(1)
            
            links = re.findall(r'\[\[([^|\]]+)(?:\|[^\]]+)?\]\]', content)
            for link in links:
                if link in figures:
                    linked_figures.add(link)

    print(f"test_f2_f3 passed: found {len(linked_figures)} valid figure links in narrative texts")

if __name__ == '__main__':
    main()
