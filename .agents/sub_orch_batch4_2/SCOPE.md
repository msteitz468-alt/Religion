# Scope: Batch 4.2 (mapping.json items 35-39)

## Architecture
- 5 commentaries to be processed: items 35-39 from mapping.json.
- Task: For each item, extract narrative info and major figures from its raw_file. Non-destructively inject the narrative info into the corresponding primary text pages (e.g. wiki/texts/*.md). Create or update wiki/figures/ pages for major figures per the CLAUDE.md schema. Append new figure pages to wiki/index.md.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Item 35 | Marshall/Kruse, Epistles of John | none | PLANNED |
| 2 | Item 36 | Seifrid, 2 Corinthians | none | PLANNED |
| 3 | Item 37 | Ciampa/Rosner, 1 Corinthians | none | PLANNED |
| 4 | Item 38 | Schreiner, Romans | none | PLANNED |
| 5 | Item 39 | Michaels, Gospel of John | none | PLANNED |

## Interface Contracts
### wiki/index.md update
- Figure pages MUST be appended to wiki/index.md. Concurrent access should be managed by having workers update the file cleanly.
