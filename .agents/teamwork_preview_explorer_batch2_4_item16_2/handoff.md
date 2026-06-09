# Investigation Report: Item 16 Commentaries (Nogalski)

## Observation
I reviewed Nogalski's commentaries on Joel, Obadiah, Jonah, and Micah from the `raw/commentaries/` directory. 
1. **Obadiah**: The commentary notes Obadiah reflects on Edom's betrayal of Judah in 587 BCE, with Edom's subsequent loss of territory to Nabonidus and Arabian tribes. The author is likely a 5th-century BCE scribal prophet who drew from Jeremiah 49 and Amos 9, rather than an earlier cult prophet (lines 4376-4600).
2. **Jonah**: The commentary defines Jonah as a 4th-century BCE satirical fiction starring an obscure 8th-century prophet (Jonah ben Amittai from 2 Kgs 14:25). It uses humor to critique the theology of exclusion (specifically satirizing Joel's use of Exod 34:6). The thanksgiving psalm in chapter 2 is widely seen as a later insertion to "rehabilitate" the prophet's piety (lines 5730-5852).
3. **Micah**: The book was compiled over three phases. The historical Micah was an 8th-century prophet from Moresheth active during Sennacherib's 701 BCE siege. Chapters 1-3 form this early core. Chapters 6-7 are a 6th-5th century exilic update blaming leaders for Jerusalem's destruction. Chapters 4-5 are a postexilic addition providing eschatological hope for Zion (lines 977-1181).

I checked the `wiki/texts/` pages and found them to be largely populated with this information already. However, the corresponding figure pages for Obadiah, Jonah, and Micah do not exist in `wiki/figures/`.

## Logic Chain
- The `wiki/texts/` pages for Obadiah, Jonah, and Micah contain excellent overviews based on Nogalski's work but could be lightly updated to ensure the specific historical details (e.g., Obadiah as a Persian-period scribal prophet; Jonah's composition as a late Persian/early Hellenistic satire against Joel's theology; Micah's 3-phase redaction) are maximally clear. 
- According to `CLAUDE.md`, major biblical figures should have dedicated pages in `wiki/figures/`. 
- Therefore, we must create new figure pages for **Obadiah**, **Jonah**, and **Micah**, structuring them according to the `CLAUDE.md` template (Biographical Overview, Primary Source Appearances, Tradition-Specific Reception, Theological/Narrative Significance, Historicity/Interpretive Controversies).

## Caveats
- The text pages (`wiki/texts/*.md`) already contain strong summaries. The implementer should review them to avoid redundancy when "injecting" narrative information. The main task is generating the new figure pages.
- "Obadiah" has no biographical details in the text; his page will mostly discuss his role as a scribal prophet. 

## Conclusion
We need to create three new figure pages (`wiki/figures/obadiah.md`, `wiki/figures/jonah.md`, `wiki/figures/micah.md`) and verify the narrative alignments in the text pages. The specific data to inject into the figure pages includes:
- **Obadiah**: Unknown biography; name means "servant of Yahweh"; 5th-century BCE scribal prophet; compiled existing anti-Edomite sources (Jer 49) to address Edom's 587 BCE betrayal.
- **Jonah**: Historical 8th-century prophet from 2 Kgs 14:25 repurposed in a 4th-century BCE satire. Used as a comedic foil to critique exclusivist theology and extend divine grace to foreigners.
- **Micah**: 8th-century Judean from Moresheth. Delivered fierce social justice critiques against wealthy elites during the Assyrian crisis (701 BCE). His historical words (chs 1-3) were updated by exilic and postexilic scribes.

## Verification Method
- Read `wiki/figures/obadiah.md`, `wiki/figures/jonah.md`, and `wiki/figures/micah.md` to confirm they follow the `CLAUDE.md` figure template and incorporate the historical-critical perspectives from Nogalski's commentaries.
