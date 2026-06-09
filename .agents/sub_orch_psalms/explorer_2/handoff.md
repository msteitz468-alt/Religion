# Handoff Report

## Observation
- The NICOT Psalms commentary by deClaissé-Walford et al. notes that while the Psalter lacks a linear plot, it incorporates narrative in two key ways:
  1. **Historical Superscriptions**: Thirteen psalms of David (Pss. 3, 7, 18, 34, 51, 52, 54, 56, 57, 59, 60, 63, and 142) contain brief narratives tying the psalm to specific events in David's life. The commentary treats these not as compositional timestamps, but as "the earliest commentary" that anchors the prayers in a narrative context.
  2. **Historical Psalms**: Psalms 78, 105, and 106 narrate Israel's history (the Exodus, wilderness wanderings, and conquest) to highlight God's covenant fidelity versus Israel's infidelity.
- Major figures identified in connection with the Psalms are: David, Asaph (Levite musician, head of a guild linked to Pss 50, 73–83), the Sons of Korah (temple singers linked to Pss 42–49, 84–85, 87–88, descendants of the rebellious Korah of Num 16), Solomon (Pss 72, 127), Moses (Ps 90), Heman the Ezrahite (Ps 88), and Ethan the Ezrahite (Ps 89).
- The `wiki/texts/psalms.md` file contains a detailed breakdown of canonical shape, form criticism, and theology, but currently lacks explicit discussion of the 13 historical superscriptions as early narrative commentary and the function of the historical psalms.
- The `wiki/figures/` directory does not yet contain pages for David, Asaph, Korah, Heman, or Ethan. Existing pages for Moses and Solomon do not yet prominently feature their Psalms attributions.
- `wiki/index.md` has an empty `### Hebrew Bible / Old Testament` section under the `## Figures` heading.

## Logic Chain
- To non-destructively inject the narrative information into `wiki/texts/psalms.md`, we should insert a discrete new subsection rather than rewriting existing analytical paragraphs.
- To represent the figures accurately, we need to create new `wiki/figures/` pages for David, Asaph, Korah, Heman, and Ethan, formatting them according to the schema in `CLAUDE.md`. Existing pages for Moses and Solomon need brief updates to mention their connections to the Psalter.
- To append the new figure pages to `wiki/index.md`, they must be inserted under the designated, currently empty subheading `### Hebrew Bible / Old Testament` in the Figures section.

## Caveats
- The commentary is 2.6 MB; the investigation relied on targeted searches for "narrative", "superscriptions", and figure names rather than a full linear reading.
- "Sons of Korah" represents a guild rather than a single individual, but per the wiki schema, it is best placed under a `korah.md` figure page that bridges the ancestral figure (Numbers 16) and his descendants' liturgical role in the Psalms.
- Heman and Ethan are minor figures compared to David or Asaph, but they are named in superscriptions (Pss 88 and 89) and fulfill the criteria for a figure page.

## Conclusion (Concrete Strategy for the Worker)
1. **Update `wiki/texts/psalms.md`**: Insert a new subsection (e.g., `### Narrative Elements in the Psalter`) into the `## Canon and Textual History` or `## The Canonical Shape` section. Detail the dual narrative aspects: (a) the 13 historical superscriptions acting as early narrative commentary on David's life, and (b) the "historical psalms" (78, 105, 106) recounting the Exodus/wilderness narratives.
2. **Create/Update `wiki/figures/`**:
   - Create `david.md` (highlighting his role as the focal figure of Books 1-2 and the subject of the 13 historical superscriptions).
   - Create `asaph.md` (eponymous head of the Asaphite temple musicians).
   - Create `korah.md` (covering the Numbers 16 rebellion and the later Sons of Korah temple singer guild).
   - Create `heman.md` and `ethan.md` (Ezrahite musicians).
   - Update `moses.md` and `solomon.md` to reference their respective Psalm attributions (Ps 90 for Moses, Pss 72, 127 for Solomon).
3. **Append to `wiki/index.md`**: Add links for `[[david|David]]`, `[[asaph|Asaph]]`, `[[korah|Korah / Sons of Korah]]`, `[[heman|Heman the Ezrahite]]`, and `[[ethan|Ethan the Ezrahite]]` to the `### Hebrew Bible / Old Testament` subheading under `## Figures`. Ensure alphabetical or chronological order as appropriate.

## Verification Method
- **`view_file` on `wiki/texts/psalms.md`**: Verify the new subsection is present and the old text is completely intact.
- **`list_dir` on `wiki/figures/`**: Confirm the creation of the new `.md` files.
- **`view_file` on `wiki/index.md`**: Verify the new figure links are properly placed under the `### Hebrew Bible / Old Testament` heading.
