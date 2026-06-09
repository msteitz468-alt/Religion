import os
import re
from collections import defaultdict

# 1. Gather all existing pages
existing_pages = set()
page_paths = {}
for root, dirs, files in os.walk('wiki'):
    for file in files:
        if file.endswith('.md'):
            page_name = file[:-3]
            existing_pages.add(page_name)
            page_paths[page_name] = os.path.join(root, file)

# 2. Extract all inbound links
# format: [[page-name|Display Name]] or [[page-name]]
link_pattern = re.compile(r'\[\[(.*?)(?:\|.*?)?\]\]')
inbound_links = defaultdict(set)
outbound_links = defaultdict(set)
content_by_page = {}

for page_name, path in page_paths.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        content_by_page[page_name] = content
        links = link_pattern.findall(content)
        for link in links:
            # normalize link (remove anchor tags if any)
            target = link.split('#')[0]
            outbound_links[page_name].add(target)
            inbound_links[target].add(page_name)

# Find Orphans (pages with no inbound links, OR only linked by index.md/log.md/overview.md)
orphans = []
for page in existing_pages:
    if page in ['index', 'log', 'overview', 'CLAUDE']: continue
    inbound = inbound_links.get(page, set())
    # filter out index, log, overview
    meaningful_inbound = inbound - {'index', 'log', 'overview'}
    if not meaningful_inbound:
        orphans.append(page)

# Find Missing Pages (links to pages that don't exist)
missing_pages = defaultdict(set) # missing_page -> set of pages linking to it
for source_page, targets in outbound_links.items():
    for target in targets:
        if target not in existing_pages:
            missing_pages[target].add(source_page)

print("=== LINT REPORT ===")
print(f"Total Pages: {len(existing_pages)}")
print("\n--- ORPHANS (0 meaningful inbound links) ---")
for o in sorted(orphans):
    print(f"- {o}")

print("\n--- MISSING PAGES (Red Links) ---")
for missing, sources in sorted(missing_pages.items()):
    print(f"- {missing} (linked from: {', '.join(sources)})")

# Let's do a simple heuristic for mentioned commentators:
# "Commentary by X" or "X notes that"
print("\n--- POTENTIAL MISSING COMMENTATORS/CONCEPTS ---")
# This requires semantic analysis, but we can list the missing pages which are likely commentators/concepts
