# Scope: Isaiah Commentary Processing

## Architecture
- Source files: `raw/commentaries/Isaiah 1-39 (NICOT) - John N. Oswalt.txt` and `raw/commentaries/Isaiah 40-66 (NICOT) - John N. Oswalt.txt`
- Target text page: `wiki/texts/isaiah.md`
- Target figures pages: `wiki/figures/*.md`
- Target index page: `wiki/index.md`

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Isaiah Processing | Extract narrative info/figures from NICOT Isaiah 1-66, inject into `wiki/texts/isaiah.md`, update/create `wiki/figures/*.md` (following CLAUDE.md schema), append new figures to `wiki/index.md` cleanly. | none | PLANNED |

## Interface Contracts
### Raw Text ↔ Wiki
- Must extract verifiable narrative info.
- Inject non-destructively.
- Figure schema from CLAUDE.md.
