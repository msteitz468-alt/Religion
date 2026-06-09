import os
import re

def extract_yaml(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    yaml_text = match.group(1)
    
    # simple yaml parser
    result = {}
    for line in yaml_text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            result[key.strip()] = val.strip()
    return result

schemas = {
    'texts': ['title', 'tradition', 'canon_status', 'language_original', 'date_range', 'sources_ingested', 'last_updated', 'tags'],
    'commentators': ['title', 'full_name', 'dates', 'tradition', 'affiliation', 'primary_texts_commented', 'sources_ingested', 'last_updated', 'tags'],
    'concepts': ['title', 'domain', 'traditions_using', 'sources_ingested', 'last_updated', 'tags'],
    'comparisons': ['title', 'entities_compared', 'generated_from_query', 'date', 'tags'],
    'controversies': ['title', 'text_locus', 'positions', 'traditions_involved', 'resolution_status', 'last_updated', 'tags'],
}

results = {}
total_files = 0

for root, _, files in os.walk('wiki'):
    if 'queries' in root: continue
    
    category = os.path.basename(root)
    if category == 'wiki':
        continue # skip top level index.md, etc.
        
    required_keys = schemas.get(category, [])
    
    for file in files:
        if file.endswith('.md'):
            total_files += 1
            filepath = os.path.join(root, file)
            frontmatter = extract_yaml(filepath)
            
            if not frontmatter:
                results[filepath] = "No YAML frontmatter found."
                continue
            
            missing_keys = []
            for key in required_keys:
                if key not in frontmatter:
                    missing_keys.append(key)
            
            if missing_keys:
                results[filepath] = f"Missing keys: {', '.join(missing_keys)}"

for filepath, issue in results.items():
    print(f"{filepath}: {issue}")

print(f"Total files checked: {total_files}")
print(f"Total files with issues: {len(results)}")
