# Scope: Batch 3 (mapping.json items 20-29)

## Architecture
- Process items 20-29 in mapping.json.
- Extract narrative information and major figures.
- Inject narrative info into primary text pages.
- Create/update figure pages per CLAUDE.md schema.
- Append new figure pages to wiki/index.md.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Batch 3.1 | mapping.json items 20-22 | none | IN_PROGRESS |
| 2 | Batch 3.2 | mapping.json items 23-25 | none | IN_PROGRESS |
| 3 | Batch 3.3 | mapping.json items 26-29 | none | IN_PROGRESS |

## Interface Contracts
### wiki/index.md update
- Figure pages MUST be appended to wiki/index.md. Concurrent access should be managed by having workers update the file cleanly.
