# Observation
- Verified target `texts/*.md` pages (`jeremiah.md`, `lamentations.md`, `isaiah.md`, `song-of-songs.md`). They already contain substantial theological and structural content, but lack explicit "Major Figures" sections to cross-reference character pages.
- Verified `wiki/figures/` directory. Found `solomon.md`, but missing key figures from these commentaries: `jeremiah-prophet.md`, `isaiah-prophet.md`, `baruch.md`, `josiah.md`, `jehoiakim.md`, `zedekiah.md`, `hezekiah.md`, `ahaz.md`, `cyrus.md`, `shulammite.md`.
- Read introductions and outlines of Oswalt's *Isaiah*, Lalleman & Goldingay's *Jeremiah & Lamentations*, and Longman's *Song of Songs*. 
- Extracted narrative information and figure roles based on commentary introductions.

# Logic Chain
1. To integrate the extracted commentary material with the wiki architecture (per `CLAUDE.md`), we must ensure that all prominent named figures have dedicated `figures/*.md` pages and are explicitly linked from their respective `texts/*.md` pages.
2. **Jeremiah**: The narrative covers the decline and fall of Judah. Major figures are Jeremiah himself, his scribe Baruch, and the kings Josiah (reformer), Jehoiakim (burned the scroll), and Zedekiah (last king).
3. **Isaiah**: The narrative context centers on the Assyrian crisis (Ahaz and Hezekiah) and the later Babylonian/Persian transitions (Cyrus). Isaiah is the central prophetic figure.
4. **Song of Songs**: Longman explicitly identifies "The Woman" (the Shulammite) and "The Man". He treats Solomon not as the author/lover, but as a negative foil attempting to buy love (8:11-12).
5. Therefore, we must create new figure pages, update the existing `solomon.md` page with his specific role in the Song of Songs, and inject "Major Figures" linking sections into the 4 text pages.

# Caveats
- Detailed biographical data for some kings (Josiah, Hezekiah) also draws heavily on 2 Kings/2 Chronicles, though their pages here are scoped to their significance in these specific prophetic books.
- The "Shulammite" is treated as the central figure of Song of Songs per Longman, though Longman notes it may simply be a title/wordplay rather than a proper name.

# Conclusion
The Worker should execute the following file-by-file plan:

**1. Update `wiki/texts/isaiah.md`**
- Add a "## Major Figures" section linking to `[[isaiah-prophet|Isaiah]]`, `[[hezekiah|Hezekiah]]`, `[[ahaz|Ahaz]]`, and `[[cyrus|Cyrus]]`.

**2. Update `wiki/texts/jeremiah.md`**
- Add a "## Major Figures" section linking to `[[jeremiah-prophet|Jeremiah]]`, `[[baruch|Baruch]]`, `[[josiah|Josiah]]`, `[[jehoiakim|Jehoiakim]]`, and `[[zedekiah|Zedekiah]]`.

**3. Update `wiki/texts/lamentations.md`**
- Add a note under "Composition and Authorship" linking to `[[jeremiah-prophet|Jeremiah]]` as the traditional (though critically debated) author.

**4. Update `wiki/texts/song-of-songs.md`**
- Add a "## Major Figures" section linking to `[[solomon|Solomon]]` and `[[shulammite|The Shulammite]]`.

**5. Update `wiki/figures/solomon.md`**
- Add a section on his role in the Song of Songs. Note that per Longman, he is an object of the poem, not the composer, and serves as a negative foil (a king whose wealth cannot buy love).

**6. Create new figure pages in `wiki/figures/` (using CLAUDE.md schema)**
- `isaiah-prophet.md`: 8th-century prophet, son of Amoz. Key actor in the Assyrian crisis.
- `hezekiah.md`: King of Judah. Reverted Ahaz's pro-Assyrian policy, leading to Sennacherib's siege. Miraculously delivered but failed the Babylonian test.
- `ahaz.md`: King of Judah. Adopted pro-Assyrian policy against Isaiah's advice during Syro-Ephraimite war. Recipient of the Immanuel sign.
- `cyrus.md`: Persian Emperor. Conquered Babylon. Uniquely identified as YHWH's "shepherd" and "anointed" (*mashiach*) in Isaiah 44-45.
- `jeremiah-prophet.md`: The "weeping prophet", from Anathoth. Ministry from Josiah to the exile. Embodied the message through his "Confessions".
- `baruch.md`: Scribe of Jeremiah, wrote the scroll that Jehoiakim burned and its expanded replacement.
- `josiah.md`: King of Judah. Initiated major reforms, killed at Megiddo. His reign marks the beginning of Jeremiah's ministry.
- `jehoiakim.md`: King of Judah. Burned Jeremiah's scroll, rejecting the call to repentance.
- `zedekiah.md`: Last king of Judah. Weak ruler who rebelled against Babylon, leading to Jerusalem's destruction.
- `shulammite.md`: The primary female voice and protagonist in Song of Songs. Initiator of love, resisting societal constraints. Name likely a feminine wordplay on Solomon.

**7. Update `wiki/index.md`**
- Append the newly created figure pages to the index.

# Verification Method
- `ls wiki/figures/` to verify the creation of the 10 new figure pages.
- `grep -r "Major Figures" wiki/texts/` to ensure the text pages have been updated with cross-links.
- Review `wiki/index.md` to confirm the figure pages are indexed.
