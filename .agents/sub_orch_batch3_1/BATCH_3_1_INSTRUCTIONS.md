# Batch 3.1 Task
You are the Explorer for Batch 3.1 (mapping.json items 20-22).

## Items to Process:
1. Item 20: Jeremiah and Lamentations
   - Source Title: Goldingay, John. *The Book of Jeremiah*... and Lalleman-de Winkel, Hetty. *Jeremiah and Lamentations*
   - Target Pages: wiki/texts/lamentations.md, wiki/texts/jeremiah.md
   - INCORRECT raw_file in json: raw/commentaries/Deuteronomy (NICOT) - Peter C. Craigie.txt
   - YOUR TASK: Find the correct raw files in raw/commentaries/ matching the source title, read them, extract narrative information and major figures.

2. Item 21: Isaiah
   - Source Title: Oswalt, John N. *The Book of Isaiah: Chapters 1-39* and *Chapters 40-66*. NICOT.
   - Target Pages: wiki/texts/isaiah.md
   - The JSON lists Isaiah 1-39. Check for Isaiah 40-66 as well. Extract narrative info and major figures.

3. Item 22: Song of Songs
   - Source Title: Longman, Tremper, III. *Song of Songs*. NICOT. Eerdmans, 2001.
   - Target Pages: wiki/texts/song-of-songs.md
   - INCORRECT raw_file in json: raw/commentaries/Daniel - Tremper Longman III.txt
   - YOUR TASK: Find the correct raw file in raw/commentaries/ matching the source title, read it, extract narrative info and major figures.

## Instructions:
For all 3 items:
1. Find the true raw text file(s) for the commentary.
2. Extract the key narrative information and major figures (per CLAUDE.md schema for figure pages).
3. Draft a specific, file-by-file plan for what needs to be injected into texts/*.md and what figures/*.md pages need to be created/updated.
4. Document the exact findings and proposed changes in your handoff report.
5. Provide the report to me so I can pass it to the Worker. Do NOT implement the changes yourself.
