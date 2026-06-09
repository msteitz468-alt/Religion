# Scope: Batch 3.2

## Architecture
- Extract narrative info and major figures from raw files corresponding to mapping.json items 23-25.
- Non-destructively inject the narrative info into the corresponding primary text pages (e.g., wiki/texts/*.md).
- Create or update wiki/figures/ pages for major figures per the CLAUDE.md schema.
- Append new figure pages to wiki/index.md.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Process Items 23-25 | Extract, inject, update figure pages, append to index | none | PLANNED |

## Interface Contracts
- Figure pages follow CLAUDE.md schema.
- Primary texts injected non-destructively.
- wiki/index.md appended.
