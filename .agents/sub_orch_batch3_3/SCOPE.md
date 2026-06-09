# Scope: Batch 3.3 (mapping.json items 26-29)

## Architecture
- Process items 26, 27, 28, and 29 in mapping.json.
- Extract narrative information and major figures from their raw_file.
- Inject narrative info into the corresponding primary text pages (e.g., wiki/texts/*.md).
- Create or update wiki/figures/ pages for major figures per the CLAUDE.md schema.
- Append new figure pages to wiki/index.md.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Item 26 | mapping.json item 26 | none | PLANNED |
| 2 | Item 27 | mapping.json item 27 | none | PLANNED |
| 3 | Item 28 | mapping.json item 28 | none | PLANNED |
| 4 | Item 29 | mapping.json item 29 | none | PLANNED |

## Interface Contracts
### wiki/index.md update
- Figure pages MUST be appended to wiki/index.md. Concurrent access should be managed by having workers update the file cleanly.
