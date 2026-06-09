# Project: Religion Wiki Extraction
# Scope: Extract narrative information and major figures from 47 commentaries

## Architecture
- 47 commentaries defined in mapping.json.
- Each commentary needs extraction of narrative info and major figures.
- Updates go to wiki/texts/*.md, wiki/figures/*.md, and wiki/index.md.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Batch 1 | mapping.json items 0-9 | none | PLANNED |
| 2 | Batch 2 | mapping.json items 10-19 | none | PLANNED |
| 3 | Batch 3 | mapping.json items 20-29 | none | PLANNED |
| 4 | Batch 4 | mapping.json items 30-39 | none | PLANNED |
| 5 | Batch 5 | mapping.json items 40-46 | none | PLANNED |

## Interface Contracts
### wiki/index.md update
- Figure pages MUST be appended to wiki/index.md. Concurrent access should be managed by having workers update the file cleanly.
