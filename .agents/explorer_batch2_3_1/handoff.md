# Handoff Report: Leviticus and Exodus Narrative & Figures

## 1. Observation
- Investigated Item 14: `raw/commentaries/Leviticus (NICOT) - Gordon J. Wenham.txt`.
  - Found that while Leviticus is heavily legal, it has a narrative framework: God speaks to Moses in the wilderness.
  - Chs. 8-9 detail the ordination of Aaron and his sons.
  - Ch. 10 details the death of Nadab and Abihu by divine fire for offering "strange" (unauthorized) fire. Aaron, Eleazar, and Ithamar are forbidden to mourn. Mishael and Elzaphan bury the bodies.
- Investigated Item 15: `raw/commentaries/Exodus (Understanding the Bible Commentary - James K. Bruckner.txt`.
  - The TOC and text reveal the overarching narrative: oppression in Egypt, Moses' call, conflict with Pharaoh, plagues, Passover, Red Sea crossing, wilderness journey with Jethro's counsel, Sinai covenant, Golden Calf crisis, and Tabernacle construction led by Bezalel.
- Reviewed `CLAUDE.md` and `wiki/index.md` to confirm the schema for figure pages and current index structure.

## 2. Logic Chain
- The user requested narrative information and major figures for Leviticus and Exodus.
- By extracting the narrative portions from the commentaries (Lev 8-10 framework, Exod historical flow), we identify the key actors: Moses, Aaron, Nadab, Abihu, Eleazar, Ithamar, Mishael, Elzaphan, Pharaoh, Jethro, Bezalel.
- The `CLAUDE.md` schema requires a YAML frontmatter block for `wiki/figures/*.md` pages and tracking the domain and traditions.
- To fulfill the request without violating the "read-only investigation" constraint, I am providing a detailed, step-by-step injection plan instead of making the modifications directly.

## 3. Caveats
- I did not extract the entire text of the Exodus commentary due to its length; I relied on its detailed Table of Contents and standard biblical narrative structure to confirm the major figures.
- Some minor figures (like Eleazar, Ithamar, Mishael, Elzaphan) may not warrant their own individual pages immediately, but Nadab and Abihu definitely do (either combined or separate). The plan proposes a combined or focused approach.

## 4. Conclusion
Here is the concrete plan for the Implementer agent:

**A. Updates to `wiki/texts/leviticus.md`:**
- Add a `## Narrative Context` section after `## Structure`. Summarize the wilderness setting, the ordination of Aaron and his sons (chs. 8-9), and the critical episode of Nadab and Abihu's death for offering strange fire (ch. 10), noting the roles of Eleazar, Ithamar, Mishael, and Elzaphan.
- Add a `## Major Figures` section with links to: `[[moses|Moses]]`, `[[aaron|Aaron]]`, `[[nadab-and-abihu|Nadab and Abihu]]`.

**B. Updates to `wiki/texts/exodus.md`:**
- Add a `## Narrative Summary` section (or enhance `Structure`) outlining Moses' call, the plagues and Pharaoh's hardened heart, the Passover, the Red Sea, Jethro's judicial advice, the Sinai covenant, the Golden Calf, and Bezalel's Tabernacle construction.
- Add a `## Major Figures` section with links to: `[[moses|Moses]]`, `[[aaron|Aaron]]`, `[[pharaoh|Pharaoh]]`, `[[jethro|Jethro]]`, `[[bezalel|Bezalel]]`.

**C. Create new pages in `wiki/figures/` (following CLAUDE.md schema):**
1. `aaron.md` (Domain: biblical. Key roles: First High Priest, Moses' spokesman, Golden Calf involvement).
2. `nadab-and-abihu.md` (Domain: biblical. Key roles: Aaron's eldest sons, judged for strange fire).
3. `pharaoh.md` (Domain: biblical/historical. Key roles: Oppressor, hardening of heart).
4. `jethro.md` (Domain: biblical. Key roles: Midianite priest, Moses' father-in-law, judicial advisor).
5. `bezalel.md` (Domain: biblical. Key roles: Spirit-empowered artisan for the Tabernacle).
*(Note: `moses.md` already exists).*

**D. Updates to `wiki/index.md`:**
- Append the newly created figure links to the existing list under the `## Figures` heading.

## 5. Verification Method
- The next agent can verify the proposed text structure by checking `wiki/texts/leviticus.md` and `wiki/texts/exodus.md`.
- They can read `CLAUDE.md` to ensure the new figure pages match the `wiki/figures/` schema exactly.
- After implementation, verify that all internal Obsidian links (`[[name|Display]]`) resolve correctly across the text, figure, and index pages.
