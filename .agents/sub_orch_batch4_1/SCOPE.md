# Scope: Batch 4.1 (mapping.json items 30-34)

## Architecture
- 5 commentaries to be processed: items 30-34 from mapping.json.
- Task: For each item, extract narrative info and major figures from its raw_file. Non-destructively inject the narrative info into the corresponding primary text pages (e.g. wiki/texts/*.md). Create or update wiki/figures/ pages for major figures per the CLAUDE.md schema. Append new figure pages to wiki/index.md.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Item 30 | Tsumura, 2 Samuel | none | IN_PROGRESS (8c0fc279, 4fe35182, 32968403) |
| 2 | Item 31 | Tsumura, 1 Samuel | none | PLANNED |
| 3 | Item 32 | Lau, Ruth | none | PLANNED |
| 4 | Item 33 | Webb, Judges | none | PLANNED |
| 5 | Item 34 | Woudstra, Joshua | none | PLANNED |

## Interface Contracts
### wiki/index.md update
- Figure pages MUST be appended to wiki/index.md. Concurrent access should be managed by having workers update the file cleanly.
