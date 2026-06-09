# Handoff Report: Narrative Information in 1 Peter, 2 Peter, and Jude

## 1. Observation
- `mapping.json` items 45 and 46 map to Jobes on 1 Peter and Green on Jude and 2 Peter. (Note: `mapping.json` has a typo pointing Green to the Jobes file, but I located the correct raw file: `raw/commentaries/Jude and 2 Peter (BECNT) - Gene Green.txt`).
- `raw/commentaries/1 Peter (BECNT) - Karen H. Jobes.txt` highlights narrative connections to the Passion narrative (2:22-25 sequence modeling Christ's trial and crucifixion) and the Days of Noah (3:19-20), relying heavily on the Enoch-Noah tradition of the Watchers (fallen angels) from 1 Enoch and Genesis 6.
- `raw/commentaries/Jude and 2 Peter (BECNT) - Gene Green.txt` details heavy usage of typological narratives:
  - **Jude**: Employs "Text and Comment" structures based on the Exodus rebellion (Num 14), angelic fall (Gen 6 / 1 Enoch), Sodom & Gomorrah (Gen 19), Michael's dispute over Moses' body (Assumption of Moses), and the typological triad of Cain, Balaam, and Korah.
  - **2 Peter**: Contrasts judgment and rescue using the Flood (Noah) and Sodom (Lot), characterizing Noah as a "herald of righteousness" and Lot as a "righteous man" (borrowing from Wisdom 10:6). Also references the Transfiguration narrative (1:16-18) to anchor apostolic eyewitness authority regarding the coming Day of the Lord.

## 2. Logic Chain
- Based on `CLAUDE.md`, primary texts (`wiki/texts/*.md`) must include narrative summaries and interpretive cruxes. The Enoch/Noah connections, the Transfiguration, and the typological use of OT/Pseudepigraphal events are the defining narrative cruxes of these three epistles.
- `CLAUDE.md` specifies that major biblical figures who generate sustained commentary require a `wiki/figures/` page. The figures of Noah, Lot, Enoch, Michael the Archangel, Cain, Balaam, and Korah are explicitly identified in these commentaries as archetypal models of righteousness or rebellion, warranting their own figure pages or substantive updates.
- The strategy for implementing these updates requires targeting three specific text pages (`texts/1-peter.md`, `texts/2-peter.md`, `texts/jude.md`) and creating/updating the corresponding figure pages following the YAML schema in `CLAUDE.md`.

## 3. Caveats
- Investigation of the raw files was performed via targeted grep searches for terms like "Contents" and "narrative". I did not read the entirety of the ~1,000 page commentaries. 
- The schema requires tradition-specific tracking (e.g., how the Enoch tradition developed); the implementer will need to synthesize these specific paragraphs based on further reading of the commentary text.
- I am constrained to a read-only investigation, so I have provided the plan without executing the actual file creation/modifications in the `wiki/` directory.

## 4. Conclusion
**Strategy for Wiki Injection:**
1. **Primary Text Pages (`wiki/texts/*.md`)**:
   - `1-peter.md`: Inject the narrative sequence of the Passion (Christ as examplar) and the Enoch-Noah tradition (preaching to spirits in prison / the flood as a type of baptism).
   - `jude.md`: Outline the "Text and Comment" rhetorical structure. Summarize the narrative use of the Exodus generation, Sodom & Gomorrah, rebellious angels, and the Cain-Balaam-Korah triad. Highlight the interpretive crux of citing pseudepigrapha (1 Enoch, Assumption of Moses).
   - `2-peter.md`: Add the Transfiguration narrative as the apostolic guarantee of the Parousia. Outline the judgment/rescue narratives of the Flood and Sodom & Gomorrah.
2. **Figure Pages (`wiki/figures/*.md`)**:
   - Update/Create pages for **Noah**, **Lot**, **Enoch**, **Michael the Archangel**, **Balaam**, **Cain**, and **Korah**.
   - Use the `CLAUDE.md` schema. Include biographical overviews, textual sources, and specifically detail their typological reception in these epistles (e.g., Lot as a "righteous man" distressed by sin; Balaam as an archetype for greed/heresy).
   - Ensure Peter and Jude have their own pages, highlighting their self-presentation and apostolic authority in the epistles.
3. **Master Index (`wiki/index.md`)**:
   - Append links to the newly modified/created text and figure pages under their respective "Texts" and "Figures" headings to maintain the wiki directory map.

## 5. Verification Method
- Ensure the implementer reviews the exact line references extracted in this agent's `progress.md` or logs.
- The implementer can run `grep_search` on the raw Green and Jobes files for "Sodom", "Enoch", or "Balaam" to verify the exegetical points before writing the wiki content.
