#!/usr/bin/env python3
import os
import sys
import glob

BASE_DIR = "/home/mark/mnt/gdrive/AI/Obsidian/Religion"
FIGURES_DIR = os.path.join(BASE_DIR, "wiki", "figures")

def test():
    sections = [
        "biographical overview",
        "primary source appearances",
        "tradition-specific reception",
        "theological and narrative significance",
        "historicity and interpretive controversies",
        "influence on commentary traditions"
    ]
    files = glob.glob(os.path.join(FIGURES_DIR, "*.md"))
    if not files:
        sys.exit(0)
        
    for fpath in files:
        with open(fpath, 'r') as f:
            content = f.read().lower()
            missing_sections = [sec for sec in sections if sec not in content]
            if len(missing_sections) > 4:
                print(f"{os.path.basename(fpath)} is missing sections: {missing_sections}")
                sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    test()
