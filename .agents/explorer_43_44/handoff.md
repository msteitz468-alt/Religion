# Handoff Report: Analysis of mapping.json Items 43 & 44

## 1. Observation
- `mapping.json` items 43 and 44 (0-indexed lines 518 and 535) map to Douglas J. Moo's *The Letter of James* (PNTC) and Karen H. Jobes's *1 Peter* (BECNT) respectively.
- Raw files `The Letter of James (PNTC) - Douglas J. Moo.txt` and `1 Peter (BECNT) - Karen H. Jobes.txt` are present in `raw/commentaries/`.
- `1-peter.md` already contains a "Narrative Frameworks and Typology" section referencing Noah and Enoch, but `james.md` lacks a narrative section.
- Figure pages `james-the-just.md`, `peter-apostle.md`, `abraham.md`, `rahab.md`, `job.md`, `elijah.md`, `noah.md`, and `enoch.md` already exist in `wiki/figures/`.
- Moo's commentary highlights James's address to Jewish Christians facing economic distress and persecution, utilizing figures like Abraham and Rahab to illustrate justification by works, and Job and Elijah to model perseverance and prayer.
- Jobes's commentary emphasizes that 1 Peter addresses Christians (likely from Rome, displaced to Asia Minor) suffering as "foreigners and resident aliens," utilizing Christ's suffering and the Enoch-Noah traditions as typological templates for enduring social ostracism. Jobes also argues for Petrine authorship based on bilingual interference (Semitic syntax in Greek).

## 2. Logic Chain
- Since the commentaries focus heavily on the socio-historical narrative of the original readers (displaced, persecuted minorities) and the typological narrative of major figures (Christ, Noah, Enoch, Abraham, Rahab, Job, Elijah), this narrative information must be integrated into the respective text pages.
- `james.md` completely lacks a narrative framework section. It needs to be updated to include the socio-economic context of the readers and the narrative use of OT figures.
- `1-peter.md` has some narrative info, but should be expanded to include Jobes's specific thesis on the readers' origins (displaced from Rome) and the syntax/authorship arguments.
- The `wiki/figures/` pages for these major figures must be updated to include their tradition-specific reception and typological deployment in James and 1 Peter, according to the `CLAUDE.md` schema.
- To make these updates discoverable, the `wiki/index.md` must be updated to cross-reference the newly injected narrative sections and updated figure pages.

## 3. Caveats
- The full depth of narrative extraction was limited by context bounds; further reading of specific chapters in the commentaries (e.g., James 2 for Abraham/Rahab, 1 Peter 3 for Noah/Enoch) may yield deeper typological nuances.
- We assume 0-indexing for items 43 and 44 in `mapping.json` based on the correlation with figure pages listed in the JSON.
- `CLAUDE.md` strictly dictates that we do not adjudicate historical-critical disputes, so Jobes's authorship theory and Moo's early-date theory must be presented alongside critical consensus views on the respective pages.

## 4. Conclusion
We must execute a multi-file update strategy:
1. **Primary Text Pages (`wiki/texts/`)**:
   - Inject a "Narrative Frameworks and Typology" section into `james.md`.
   - Expand the existing narrative section in `1-peter.md` with Jobes's "displaced from Rome" thesis and syntax arguments.
2. **Figure Pages (`wiki/figures/`)**:
   - Update `abraham.md`, `rahab.md`, `job.md`, and `elijah.md` to detail their specific typological usage in James.
   - Update `noah.md`, `enoch.md`, and `peter-apostle.md` to reflect Jobes's insights in 1 Peter.
   - Update `james-the-just.md` with his socio-economic and wisdom emphases.
3. **Master Index (`wiki/index.md`)**:
   - Append links and summaries of the updated figure pages and narrative sections to maintain the wiki's cross-referencing structure.

## 5. Verification Method
- **Method**: Run `cat wiki/texts/james.md` and `cat wiki/texts/1-peter.md` to verify the presence of narrative framework sections. Inspect the updated figure pages (e.g., `cat wiki/figures/abraham.md`) to confirm the inclusion of reception history specific to James or 1 Peter.
- **Invalidation**: If the text or figure pages lack explicit headings for "Narrative Frameworks and Typology" or "Tradition-Specific Reception" (as mandated by `CLAUDE.md`), the strategy was not fully implemented.
