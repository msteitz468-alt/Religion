# Scripts

Maintenance and bootstrap tooling for the wiki. These were previously loose in the
project root; collected here on 2026-06-09.

## Run from the project root

Every script uses **CWD-relative paths** (`wiki/`, `mapping.json`, `raw/...`), so invoke
them from `Religion/`, not from inside `Scripts/`:

```bash
cd ~/Documents/Religion
python3 Scripts/lint_wiki.py
```

`mapping.json` deliberately stays in the project root — it is shared data consumed by the
`tests/` suite and (re)written by `parse_log.py`.

## Inventory

| Script | Kind | What it does |
|--------|------|--------------|
| `lint_wiki.py` | reusable | Walks `wiki/`, builds the page-name → path map, and reports link issues. Starting point for health checks. |
| `check_yaml.py` | reusable | Walks `wiki/`, validates each page's YAML frontmatter by category. |
| `append_index.py` | utility | Appends entries to `wiki/index.md`. |
| `parse_log.py` | utility | Parses `wiki/log.md`, matches raw source files, and writes `mapping.json`. |
| `make_stubs.py` | one-off (bootstrap) | Creates stub pages from a hardcoded list. **Caution:** its list still contains `wiki/concepts/abraham.md` and `wiki/concepts/melchizedek.md`, which were intentionally deleted in the 2026-06-09 duplicate-slug fix (they duplicated the figure pages). Re-running it as-is would recreate those stubs and reintroduce slug collisions — prune the list first. |
| `parse_moo.py` | one-off | Extracts text from the Moo *Galatians* (BECNT) commentary in `raw/commentaries/`. |
