# Handoff Report: Leviticus and Exodus Narrative Extraction

## 1. Observation
- Analyzed `raw/commentaries/Leviticus (NICOT) - Gordon J. Wenham.txt` and `raw/commentaries/Exodus (Understanding the Bible Commentary - James K. Bruckner.txt`.
- In Leviticus, the narrative elements are scarce but pivot heavily on Chapters 8-10, encompassing the ordination of Aaron and his sons, and the deaths of Nadab and Abihu due to unauthorized ("strange") fire. Wenham stresses this as an illustration of the severe consequences of violating holiness boundaries (line 1686, 2332).
- In Exodus, narrative dominates. Bruckner highlights Moses' calling, his initial resistance, and intercession during the Golden Calf crisis (Chs 32-34). Aaron is presented as an ambivalent figure: a necessary prophetic voice for Moses (Chs 4-7) but deeply culpable in making the golden calf (Ch 32). Miriam is significant as a savior of baby Moses (Ch 2) and as a prophetess leading the Song of the Sea (Ch 15).
- Existing files `wiki/texts/leviticus.md`, `wiki/texts/exodus.md`, and `wiki/figures/moses.md` do not currently capture these specific narrative and character insights from Wenham and Bruckner. Aaron, Miriam, and Nadab & Abihu do not have their own figure pages.

## 2. Logic Chain
- To fulfill the requirement of injecting narrative information into `wiki/texts/leviticus.md` and `wiki/texts/exodus.md`, the narrative events (the Golden Calf, the Red Sea victory, Nadab & Abihu) must be explicitly tied to their respective thematic discussions.
- To follow the `CLAUDE.md` schema for major figures, pages for `aaron.md`, `miriam.md`, and `nadab-and-abihu.md` must be created. They need YAML frontmatter (title, roles, tradition, etc.) and sections on Biography, Primary Source Appearances, Tradition-Specific Reception, and Theological Significance.
- `moses.md` must be updated to include his Exodus role as the reluctant leader, intercessor during the Golden Calf crisis, and mediator of the Sinai covenant.
- The new figures must be indexed in `wiki/index.md`.

## 3. Caveats
- Detailed historical-critical source discussions (J, E, P sources) were observed but deprioritized in favor of canonical narrative theological themes as emphasized by Bruckner.
- Nadab and Abihu are placed on a single shared page due to their inseparable narrative function, which is non-standard but appropriate given their coupled treatment in the text.

## 4. Conclusion
**Plan for Implementation:**
1. **`wiki/texts/leviticus.md`**: Add a "Narrative Interludes" subsection noting Wenham's reading of chapters 8-10 (strict obedience, divine judgment on Nadab and Abihu).
2. **`wiki/texts/exodus.md`**: Expand on the "Crisis at Sinai: The Golden Calf" section incorporating Bruckner's 4 divine decisions and Moses' intercession. Detail Miriam's and Aaron's roles in the "Major Themes" or a new "Key Figures" section.
3. **`wiki/figures/aaron.md`**: Create page. Focus on his role as Moses' mouthpiece, the High Priest, and his failure in the Golden Calf crisis.
4. **`wiki/figures/miriam.md`**: Create page. Focus on her role in saving Moses and as a prophetess leading the women in worship.
5. **`wiki/figures/nadab-and-abihu.md`**: Create page. Focus on their tragic death emphasizing God's uncompromising holiness.
6. **`wiki/figures/moses.md`**: Update to include Bruckner's theological insights (reluctant leader, friend of God, covenant mediator).
7. **`wiki/index.md`**: Append links to Aaron, Miriam, and Nadab & Abihu under a "Figures" index.

## 5. Verification Method
- Ensure the newly created figure pages follow the `CLAUDE.md` figure schema.
- Run `cat wiki/figures/aaron.md` and `cat wiki/index.md` to verify the presence and indexing of the new content.
- Check that `wiki/texts/leviticus.md` and `wiki/texts/exodus.md` successfully incorporate the new narrative and commentator (Wenham/Bruckner) references.
