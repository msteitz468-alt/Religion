# Original User Request

## Initial Request — 2026-06-06T21:08:44Z

# Teamwork Project Prompt

Re-process all 47 commentary files (including the first 5) to extract narrative information and major figures, adding them to the wiki per the updated `CLAUDE.md` schema.

Working directory: ~/mnt/gdrive/AI/Obsidian/Religion
Integrity mode: development

## Requirements

### R1. Process the Complete Workload
Read `mapping.json` to identify the 47 raw commentary files and their associated primary text pages. You must process ALL 47 entries, as the first 5 entries need to be re-run to extract the newly requested figures and narratives.

### R2. Extract and Inject Narrative Information
For each source, extract the narrative summary and structure of any stories discussed. Non-destructively inject this narrative information into the body of the corresponding primary text pages (e.g., `wiki/texts/*.md`), preserving all existing analysis.

### R3. Extract and Create Figure Pages
Identify major biblical or religious figures (patriarchs, prophets, apostles, kings, etc.) who receive substantial biographical, typological, or interpretive treatment in the commentary. Create or update `wiki/figures/` pages for these individuals. Follow the `CLAUDE.md` Figure Page schema strictly (including the specific YAML frontmatter and body sections like 'Tradition-Specific Reception' and 'Theological Significance').

### R4. Update the Index
Any newly created `figures/` pages must be appended to the master `wiki/index.md` so they are not orphaned.

## Acceptance Criteria

### Workload Completion
- [ ] All 47 entries in `mapping.json` have been processed.
- [ ] Narrative information has been added to the relevant primary text pages.

### Figure Pages
- [ ] New figure pages have been created in `wiki/figures/` for major individuals discussed in the commentaries.
- [ ] All new figure pages use the exact YAML frontmatter specified in `CLAUDE.md`.
- [ ] All new figure pages are properly linked and listed in `wiki/index.md`.
