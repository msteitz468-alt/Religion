# Scope: Batch 4 (mapping.json items 30-39)

## Architecture
- 10 commentaries to be processed: items 30-39 from mapping.json.
- Task: extract narrative info and major figures, inject narrative info into wiki/texts/*.md, create/update wiki/figures/*.md pages, append new figure pages to wiki/index.md.
- Because there are 10 items, we decompose into two milestones: Batch 4.1 (Old Testament) and Batch 4.2 (New Testament).

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Batch 4.1 | mapping.json items 30-34 | none | PLANNED |
| 2 | Batch 4.2 | mapping.json items 35-39 | none | PLANNED |

## Interface Contracts
### wiki/index.md update
- Figure pages MUST be appended to wiki/index.md. Concurrent access should be managed by having workers update the file cleanly.
