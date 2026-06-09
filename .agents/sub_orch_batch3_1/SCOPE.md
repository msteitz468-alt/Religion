# Scope: Batch 3.1

## Architecture
- Process mapping.json items 20, 21, and 22.
- Item 20: Jeremiah and Lamentations
- Item 21: Isaiah
- Item 22: Song of Songs
- Data discrepancy note: mapping.json specifies incorrect `raw_file` paths for Item 20 and 22. Workers should resolve this by finding the correct file in `raw/commentaries/` matching the `source_title` to extract meaningful narrative info and figures.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Item 20 | Jeremiah and Lamentations | none | PLANNED |
| 2 | Item 21 | Isaiah | none | PLANNED |
| 3 | Item 22 | Song of Songs | none | PLANNED |

## Interface Contracts
- Figure pages must be appended to wiki/index.md cleanly.
- Target files: wiki/texts/*.md, wiki/figures/*.md
