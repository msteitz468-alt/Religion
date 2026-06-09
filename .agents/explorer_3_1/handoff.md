# Explorer Handoff: Batch 3.1 (Jeremiah, Lamentations, Isaiah, Song of Songs)

## Observation
- Located the correct raw files in `/home/mark/mnt/gdrive/AI/Obsidian/Religion/raw/commentaries/`:
  - Jeremiah/Lamentations: `The Book of Jeremiah - John Goldingay;.txt`, `The Book of Lamentations - John Goldingay;.txt`, `Jeremiah and Lamentations - Lalleman-de Winkel, H_.txt`.
  - Isaiah: `Isaiah 1-39 (NICOT) - John N. Oswalt.txt`, `Isaiah 40-66 (NICOT) - John N. Oswalt.txt`.
  - Song of Songs: `Song of Songs (New International Commentar - Longman, Tremper, III.txt`.
- Evaluated interpretive frameworks and key figures based on text extractions:
  - **Isaiah (Oswalt)**: Defends the unity of Isaiah, arguing that Isaiah of Jerusalem predicted the Babylonian exile and Cyrus. Discusses the "Servant of Yahweh" in chs 40-66 as the means of restoration through substitutionary self-sacrifice, contrasting with Cyrus the political deliverer.
  - **Song of Songs (Longman)**: Rejects Solomonic authorship, viewing Solomon as a character/object of the poem rather than the composer. Interprets "Shulammite" as possibly a feminine form of Solomon ("peace"). Discusses dramatic approaches to the text.
  - **Jeremiah & Lamentations (Goldingay/Lalleman)**: Focuses on the broken covenant, the fall of Jerusalem under Zedekiah, and Jeremiah's suffering/laments. Key figures include Jeremiah, Baruch (scribe), and Zedekiah.

## Logic Chain
1. The `BATCH_3_1_INSTRUCTIONS.md` specifies the source titles and target text pages (`jeremiah.md`, `lamentations.md`, `isaiah.md`, `song-of-songs.md`).
2. `CLAUDE.md` requires that we track the hermeneutical framework (e.g., Oswalt's unified conservative/evangelical reading of Isaiah vs. critical Deutero-Isaiah division).
3. The schema dictates creating/updating `figures/*.md` for named individuals who are the subject of substantial commentary. Thus, we must extract and plan updates for figures like Isaiah, Cyrus, the Servant, Solomon, Shulammite, Jeremiah, Baruch, and Zedekiah.
4. The plan must specify file-by-file injections for the Worker to implement.

## Caveats
- The commentaries are extremely large (some over 2MB). Extractions focused on introductions, structural analysis, and major theological themes (like the Servant in Isaiah or Solomonic authorship in Song of Songs).
- The Worker will need to ensure they handle the `index.md` append contract carefully to avoid concurrent access issues.

## Conclusion
Here is the file-by-file implementation plan for the Worker:

### 1. Target: `wiki/texts/jeremiah.md` & `wiki/texts/lamentations.md`
- **Jeremiah.md**: Inject Goldingay's and Lalleman's structural frameworks. Note Goldingay's "three horizons" of composition (Jeremiah's context, Baruch's scroll, and the final post-587 scroll). Add tags for judgment, broken covenant, and new covenant.
- **Lamentations.md**: Update with Goldingay/Lalleman's analysis of the poetic structure, the theological grief over the fall of Jerusalem, and the personification of Daughter Zion.

### 2. Target: `wiki/texts/isaiah.md`
- **Isaiah.md**: Document Oswalt's strong defense of the book's unity and his theological structure (Chs 1-39: Trusting God vs. Assyria; Chs 40-55: Deliverance via the Servant; Chs 56-66: Life of the delivered). Note the explicit rejection of the Deutero-Isaiah authorship division while acknowledging the shift in historical horizon.

### 3. Target: `wiki/texts/song-of-songs.md`
- **Song-of-songs.md**: Document Longman's rejection of Solomonic authorship. Outline his interpretation of the book as an anthology of love poems rather than a two-character drama, though note his discussion of Delitzsch's dramatic view.

### 4. Target: `wiki/figures/*.md` (Create or Update)
- **`wiki/figures/jeremiah.md`** (Create): Add biographical info, prophetic call, suffering, and relationship with Baruch and Zedekiah.
- **`wiki/figures/baruch.md`** (Create): Document his role as Jeremiah's scribe and compiler of the scroll.
- **`wiki/figures/zedekiah.md`** (Create): Note his role as the final king before the exile and his interactions with Jeremiah.
- **`wiki/figures/isaiah.md`** (Create): Document his ministry during the Assyrian crisis (Ahaz/Hezekiah) and Oswalt's view of his predictive prophecies regarding Babylon and Cyrus.
- **`wiki/figures/cyrus.md`** (Create): Contrast his role as a political deliverer with the Servant of Yahweh, as discussed in Oswalt.
- **`wiki/figures/servant-of-yahweh.md`** (Create or handle as concept): Document Oswalt's view of the Servant's substitutionary atonement and the debate over the Servant's identity (Israel vs. individual).
- **`wiki/figures/solomon.md`** (Update): Add Longman's notes on Solomon's negative portrayal in 1 Kings and his minimal/titular role in the Song of Songs.
- **`wiki/figures/shulammite.md`** (Create): Document the etymology (feminine of Solomon/peace) and her characterization as a rustic paragon of virtue in dramatic interpretations (e.g., Delitzsch).

## Verification Method
- Verify the correct files in `/home/mark/mnt/gdrive/AI/Obsidian/Religion/raw/commentaries/` against the `mapping.json` source titles.
- Run `grep -i "Cyrus" "Isaiah 40-66 (NICOT) - John N. Oswalt.txt"` or `grep -i "Shulammite" "Song of Songs...txt"` to confirm the specific commentary positions.
- Check `wiki/figures/` and `wiki/texts/` to confirm the planned files do/do not exist before implementation.
