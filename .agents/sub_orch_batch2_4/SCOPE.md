# Scope: Batch 2.4 (Items 16-17)

## Architecture
- Module/package boundaries: Wiki texts (`wiki/texts/*.md`), Wiki figures (`wiki/figures/*.md`), Wiki index (`wiki/index.md`).

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Analyze Items 16 & 17 | Extract narrative and figures from raw text | none | PLANNED |
| 2 | Worker execution | Update texts, figures, index | M1 | PLANNED |
| 3 | Reviewer validation | Verify accurate and non-destructive injection | M2 | PLANNED |

## Interface Contracts
### Raw Text ↔ Wiki
- Inject narrative details into existing Markdown texts under `## Narrative` (or similar appropriate headers).
- Create figure pages following the CLAUDE.md schema.
- Update `wiki/index.md` with links to new figure pages.
