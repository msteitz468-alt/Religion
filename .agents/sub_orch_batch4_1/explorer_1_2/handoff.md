# Handoff Report

## 1. Observation
- Read `mapping.json` and identified item 30 as `Tsumura, David Toshio. *The Second Book of Samuel*`. While the raw_file path in the JSON wrongly pointed to Psalms, I successfully located the actual raw text at `raw/commentaries/The Second Book of Samuel - David Toshio Tsumura;.txt`.
- Read the raw file's Table of Contents. The narrative outline is broken down into "Story of King David (1:1–12:31)" and "Story of Absalom's Revolt (13:1–20:26)", with an Epilogue in chapters 21-24.
- Extracted the major figures from this outline: David, Saul, Absalom, Mephibosheth, Nathan, Joab, and Bathsheba.
- Investigated `wiki/texts/2-samuel.md`, which already contains a rich narrative summary and structural breakdown based on Tsumura, but observed that it lacks internal wiki links to the major figures.
- Checked `wiki/figures/` and found that none of the Hebrew Bible/Old Testament figures currently have their own pages (e.g., David, Saul, Absalom are missing).
- Examined `wiki/index.md` and observed that under the section `## Figures > ### Hebrew Bible / Old Testament`, it currently says `*(none yet)*`.
- Read `CLAUDE.md` to understand the exact schema and requirements for creating `wiki/figures/` pages.

## 2. Logic Chain
- Since `wiki/texts/2-samuel.md` already contains Tsumura's comprehensive narrative structure, the most effective non-destructive injection of the extracted narrative info and major figures is to update `wiki/texts/2-samuel.md` to explicitly cross-link to newly created figure pages and potentially add a brief "Major Figures" sub-section outlining their roles.
- Per `CLAUDE.md`, any major figure named in primary texts and subject to significant commentary must have a figure page. Thus, we should create pages for `david.md`, `saul.md`, `absalom.md`, `nathan-prophet.md`, `joab.md`, `bathsheba.md`, and `mephibosheth.md`.
- To update the index and maintain navigation, these new pages must be appended under the currently empty `### Hebrew Bible / Old Testament` section in `wiki/index.md`.

## 3. Caveats
- I read the raw commentary's Table of Contents and introduction rather than parsing the entire 900+ KB text, which was sufficient to extract the primary narrative structure and major figures, aligning perfectly with Tsumura's commentary scope.
- Some secondary figures (e.g., Abner, Amnon, Shimei) were excluded from the figure generation plan to focus strictly on the truly "major" figures per `CLAUDE.md` guidelines.

## 4. Conclusion
**Proposed Plan:**
1. **Primary Text Update**: Non-destructively inject the narrative info into `wiki/texts/2-samuel.md` by wrapping the names of major characters in Obsidian links (e.g., `[[david|David]]`, `[[absalom|Absalom]]`) where they already appear in the existing tables and text. Optionally, add a brief "Major Figures" summary section at the bottom of the page linking to their respective pages.
2. **Figure Pages Creation**: Create the following files in `wiki/figures/` using the `CLAUDE.md` schema (including YAML frontmatter with tags and roles):
   - `david.md`: Focus on the Davidic Covenant, his repentance vs. Saul's failure, and his role as Israel's king.
   - `saul.md`: Focus on his death and the theological contrast with David.
   - `absalom.md`: Focus on his revolt as the fulfillment of Nathan's judgment on David's house.
   - `joab.md`: Focus on his role as military commander and violent enforcer of David's reign.
   - `nathan-prophet.md`: Focus on his dual role in delivering the covenant (2 Sam 7) and his rebuke (2 Sam 12).
   - `bathsheba.md`: Focus on the narrative of David's sin, Nathan's parable, and Solomon's birth.
   - `mephibosheth.md`: Focus on David's *ḥesed* (covenant kindness) to Jonathan's son.
3. **Index Update**: In `wiki/index.md`, replace the `*(none yet)*` text under `### Hebrew Bible / Old Testament` with a bulleted list of these newly created figures, providing a brief 1-line description for each (e.g., `- [[david|David]] — Second King of Israel; recipient of the Davidic Covenant`).

## 5. Verification Method
- Use `view_file` on `raw/commentaries/The Second Book of Samuel - David Toshio Tsumura;.txt` to confirm the extracted Table of Contents.
- Check `wiki/index.md` (around line 93) to confirm that `*(none yet)*` is still present under `### Hebrew Bible / Old Testament`.
- Review the `CLAUDE.md` figure schema to ensure the proposed figure pages contain the correct required YAML frontmatter (like `textual_sources`, `tradition`, `roles`).
