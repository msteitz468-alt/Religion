import os
import re
import json

log_file = "wiki/log.md"
raw_dir = "raw/commentaries"

# 1. Get raw files
raw_files = os.listdir(raw_dir)

# 2. Parse log.md
mapping = []

with open(log_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split log by ingest events
events = re.split(r'\n## \[?\d{4}-\d{2}-\d{2}\]? ingest \| ', content)

for event in events[1:]:
    lines = event.strip().split('\n')
    source_title = lines[0].strip()
    
    # Try to find matching raw file based on simple keywords
    matched_file = None
    keywords = [w.lower() for w in re.findall(r'\w+', source_title) if len(w) > 3]
    for rf in raw_files:
        rf_lower = rf.lower()
        # if a couple keywords match, we assume it's the file
        matches = sum(1 for k in keywords if k in rf_lower)
        if matches >= 2:
            matched_file = os.path.join(raw_dir, rf)
            break
            
    # Find pages updated/created
    pages = []
    for line in lines:
        if "Pages created/updated:" in line or "Pages created:" in line or "Pages updated:" in line or "Pages updated/created:" in line:
            # extract anything looking like a path (e.g. texts/romans, commentators/thomas-schreiner)
            paths = re.findall(r'([a-z-]+/[a-z-]+)', line)
            pages.extend(paths)
            
    if matched_file and pages:
        # deduplicate
        pages = list(set(pages))
        mapping.append({
            "source_title": source_title,
            "raw_file": matched_file,
            "pages": pages
        })

with open('mapping.json', 'w') as f:
    json.dump(mapping, f, indent=2)

print(f"Mapped {len(mapping)} ingest events.")
