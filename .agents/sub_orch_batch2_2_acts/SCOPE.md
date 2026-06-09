# Scope: Acts Commentary Processing

## Architecture
- Read `raw/commentaries/Acts (BECNT) - Darrell L. Bock.txt` to extract narrative information and major figures.
- Target page: `wiki/texts/acts.md`
- Target figures: `wiki/figures/*.md`
- Index: `wiki/index.md`

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Extract | Extract narrative info and major figures from text | none | IN_PROGRESS |
| 2 | Inject Acts | Inject narrative info into `acts.md` | M1 | PLANNED |
| 3 | Create Figures| Create/update figure pages | M1 | PLANNED |
| 4 | Update Index | Append new figure pages to `index.md` | M3 | PLANNED |

## Interface Contracts
- Figure pages must follow CLAUDE.md schema.
- Changes to `acts.md` must be non-destructive.
- Changes to `index.md` must just append correctly.
