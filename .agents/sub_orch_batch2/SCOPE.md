# Scope: Batch 2 (mapping.json items 10-19)

## Architecture
- Process items 10-19 in mapping.json.
- Extract narrative information and major figures.
- Inject narrative info into primary text pages.
- Create/update figure pages per CLAUDE.md schema.
- Append new figure pages to wiki/index.md.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Batch 2.1 | mapping.json items 10-11 | none | PLANNED |
| 2 | Batch 2.2 | mapping.json items 12-13 | none | PLANNED |
| 3 | Batch 2.3 | mapping.json items 14-15 | none | PLANNED |
| 4 | Batch 2.4 | mapping.json items 16-17 | none | PLANNED |
| 5 | Batch 2.5 | mapping.json items 18-19 | none | PLANNED |

## Interface Contracts
### wiki/index.md update
- Figure pages MUST be appended to wiki/index.md. Concurrent access should be managed by having workers update the file cleanly.
