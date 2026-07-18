# Skill Observation Log

Observations captured during task-oriented work. Each entry identifies a
potential skill improvement or new skill opportunity.

**Status key:** OPEN = not yet actioned | ACTIONED = skill updated/created |
DECLINED = user decided not to pursue

---

### Observation 1: Chunk subagent ranges by verified body boundaries, not TOC line numbers

**Date:** 2026-06-27
**Session context:** Deployed-subagent ingest of the Tibetan Book of the Dead (~18.7k lines) across six disjoint line-ranges.
**Skill:** CLAUDE.md "Ingest Workflow — Deployed Subagent Strategy" (Step 2: split scope by disjoint line-ranges)
**Type:** internal
**Phase/Area:** Step 2 — splitting the scope into line-ranges before spawning

**Issue:** Range boundaries were estimated from the front-matter TOC and a quick keyword grep for chapter titles. The actual chapter bodies did not begin at those points: the range labeled "Chapters 1–7" in fact ran from a Ch.1 colophon through Ch.9's opening, and the "Chapters 8–11" range opened mid-Ch.9-conclusion. Subagents handled this gracefully (each extracted faithfully whatever fell in its exclusive range and flagged the mismatch), so coverage was complete — but the chapter labels in the spawn prompts were inaccurate and a chapter could in principle have been split awkwardly across two agents.

**Suggested improvement:** Before assigning ranges, locate the *body* section headers (not TOC entries) on disk — e.g. grep for the distinctive in-body title lines and confirm the first content line of each — and set range boundaries to those verified loci. Keep telling each agent its exclusive numeric range (that worked), but make the descriptive labels match the verified boundaries.

**Principle:** When partitioning a source for parallel extraction, derive cut-points from the document's actual on-disk structure, not from a paratext (TOC/index) that may paginate or enumerate differently. Disjoint numeric ranges guarantee coverage; verified boundaries guarantee the labels (and any per-chunk instructions) are correct.

**Status:** ACTIONED (confirmed effective) — applied on the 2026-06-27 ingest of al-Ghazali's *Incoherence of the Philosophers*. Before assigning ranges I grepped the **body** for each Discussion's in-text heading (`[First] Discussion` … `[Twentieth] Discussion`, filtered to `line > TOC`), which exposed that the TOC sat at lines 122–213 while the body began at 1262, and that the Twelfth heading had a typo (`[TWelfth]`) that a title-only grep missed. Setting the five subagent ranges to those verified body loci produced exact chapter-aligned cuts with no awkward splits and no mislabeled chunks. The technique works; recommend keeping it as standard practice.

### Observation 2: Align subagent chunk cuts to question/section headers AND verify contiguous coverage to prevent dropped boundary-sections

**Date:** 2026-06-27
**Session context:** Deployed-subagent ingest of Aquinas's *Summa Theologica* Parts I & I-II (~66k lines across 18 parallel Sonnet subagents)
**Skill:** Deployed-subagent ingest workflow (CLAUDE.md) / one-skill-to-rule-them-all observation
**Type:** internal
**Phase/Area:** Step 2 (split scope by disjoint line-ranges) + Step 4 (review/tie-together)

**Issue:** Even with verified body boundaries (Observation 1), three coverage gaps appeared — Q11–12, Q71, and Q106 — each a whole question that fell *between* two adjacent subagent chunks. Cause: when a chunk is cut at an arbitrary line and the subagent is told to extract "Q$a–Q$b," the agent honestly stops at the last *whole* question before the cut, and the next chunk's agent starts at the first whole question after its cut — so a question straddling (or sitting just past) the cut line is claimed by neither. Each gap had to be recovered by a main-thread direct read.

**Suggested improvement:** In Step 2, cut chunk boundaries **exactly on a question/section header line** (grep the header offsets first, then set each cut to a header line, never a round-number midpoint). Pass each subagent the **exact** question range its file actually contains, derived from the cut. Then add an explicit Step-4 check: confirm consecutive chunks' coverage is contiguous (chunk N ends at Q$k ⇒ chunk N+1 must begin at Q$k+1); if not, recover the gap immediately. A one-line guard — list each cache file's first and last header — catches the gap before filing rather than after.

**Principle:** Disjoint line-ranges guarantee no *overlap* but not no *gap*: a subagent scoped by semantic unit (question/chapter) silently under-covers when the line-cut doesn't coincide with a unit boundary. Cutting on verified header lines and asserting contiguous unit-coverage across chunks closes the gap class that boundary-verification alone leaves open.

### Observation 3: Subagent staggering may be unnecessary when the user accepts the rate-limit risk

**Date:** 2026-06-27
**Session context:** Ingesting Summa Theologica Part 3 (Secunda Secundae, ~49k lines) via the deployed-subagent strategy; ran 16 Sonnet extraction subagents across a 10-scope plan.
**Skill:** Religious-commentary-wiki ingest workflow (CLAUDE.md "Deployed Subagent Strategy", Step 3 staggered deployment)
**Type:** internal
**Phase/Area:** Step 3 — staggered batch deployment of subagents

**Issue:** CLAUDE.md mandates staggered subagent deployment (batches of 2–3 with `sleep` between) for rate-limit mitigation. Partway through this session the user instructed "no more staggering, just release them." All remaining subagents were launched at once; ~16 concurrent/total Sonnet agents completed with zero 429s or failures.

**Suggested improvement:** Consider softening the staggering mandate from "always" to "when rate limits are actually being hit" — launch in parallel by default, and fall back to staggered batches only after observing 429s. The current always-stagger rule adds wall-clock latency (sleeps + serialized batches) that this environment did not require.

**Principle:** Mitigation steps prescribed for a failure mode should be triggered by evidence of that failure mode, not applied unconditionally; defaulting to the cheaper path (full parallelism) and degrading gracefully on first error is usually faster than pre-emptively serializing.

### Observation 4: Deploy all extraction subagents up front across scopes, not scope-by-scope

**Date:** 2026-06-27
**Session context:** Deployed-subagent ingest of Heschel's *God in Search of Man* (a 3-part, ~14.7k-line monograph) into the religion wiki. I launched Scope 1's extractors, integrated/checkpointed it, then launched Scope 2's. Mid-run the user interjected: "deploy the rest of the subagents."
**Skill:** Project workflow (CLAUDE.md "Ingest Workflow — Deployed Subagent Strategy"); not an open-source skill.
**Type:** internal
**Phase/Area:** Step 2–3 (split scope / spawn subagents) vs. the per-scope checkpoint cadence.

**Issue:** CLAUDE.md frames the deployed-subagent workflow scope-by-scope (read a scope, file it, checkpoint, then move to the next). For a single-author work whose scopes are *extraction-independent* (no subagent needs another scope's output), serializing the read wastes wall-clock time. The user explicitly asked to launch all remaining extractors at once. Throughput is higher if every chunk across every scope is spawned up front (staggered in batches of 2–3 to respect rate limits) while the main thread still integrates and checkpoints *per scope* as each scope's extractions return.

**Suggested improvement:** In the project's ingest workflow, note that when scopes are extraction-independent, the main thread may deploy all chunk-extractors up front (staggered) and integrate/checkpoint per scope as results arrive — separating "parallel extraction" (can run ahead) from "filing/checkpointing" (stays ordered, per scope). Keep the per-scope checkpoint requirement intact.

**Principle:** Parallelism and checkpoint cadence are independent axes. Reading ahead in parallel doesn't require filing ahead; you can fan out all extraction work immediately while keeping integration serialized and checkpointed, as long as no extractor depends on another's output.

### Observation 5: Subagents rewriting existing sections instead of appending to designated skeletons

**Date:** 2026-06-27
**Session context:** Ingesting Karl Barth *Church Dogmatics* I.1 §§1–12 via deployed-subagent strategy; multiple Sonnet subagents given range-specific extraction tasks and told to update shared pages (`karl-barth.md`, scholarship page)
**Skill:** wiki-ingest-verifier (or new skill: deployed-subagent-ingest)
**Type:** internal
**Phase/Area:** Subagent prompt design / file ownership constraints

**Issue:** Subagents given permission to "update `wiki/commentators/karl-barth.md`" treated this as license to restructure and rewrite sections that were already written by the main thread or prior subagents. The user observed subagents rewriting sections independently. The root cause: prompts said "add only details explicitly in lines X–Y not already in the file" but did not enforce a structural constraint (e.g., append-only to a named section, or add only a clearly delimited new section with a section header that identifies the source range).

**Suggested improvement:** In the deployed-subagent ingest workflow prompt template, add an explicit constraint for shared pages: subagents may only (a) fill in skeleton placeholders that were explicitly named in the prompt by section header, or (b) append a new clearly-delimited section with a header specifying its scope (e.g., "## Key Arguments from §§9–10"). They must NOT edit, restructure, or rewrite any section not explicitly assigned. The scholarship page skeleton should be the primary vehicle for subagent output; the commentator page should receive only an append of a new section, never in-place edits.

**Principle:** In multi-agent parallel ingest, file ownership must be made structurally enforced in the prompt, not just described as a preference. "Don't overwrite existing content" is not enough — agents need an explicit positive instruction about *where* to write (a named section header or an append operation), not just a negative instruction about what not to touch.

### Observation 6: Critical-edition chapter-tables inflate subagent line-ranges and invite TOC-sampling

**Date:** 2026-06-28
**Session context:** Ingesting the Delphi Complete Works of Clement of Alexandria (multi-work corpus) via the Deployed Subagent Strategy; one subagent was assigned the opening range of the Stromata.
**Skill:** Wiki ingest workflow (CLAUDE.md — Deployed Subagent Strategy, Step 2 line-range splitting)
**Type:** internal
**Phase/Area:** Step 2 (splitting scope by line-ranges) and the faithfulness mandate (read the range in full, no TOC-triage)

**Issue:** The Delphi edition prefixes each work with a detailed master chapter-table (every chapter's summary heading for all 8 books) before the running text. The subagent assigned lines 11139–17000 found its line budget consumed partly by this TOC and ended up reading Bk I Chs. I–XVII + Bk II Chs. I–XII in full but only *sampling* Bk I Chs. XVIII–XXIX and Bk II Chs. XIII–XXIII via their chapter-table headings — i.e. the duplicated TOC made part of its assigned range look "covered" when the body text was not read line-by-line. The main thread had to flag this honestly in the coverage ledger rather than mark the whole range "read in full."

**Suggested improvement:** When scaffolding (Step 1) a reference/critical/Delphi-style edition, the main thread should locate and exclude (or separately assign) the front chapter-table/TOC block before computing density-weighted line-ranges, since a TOC duplicates body content and inflates line counts. Subagent prompts for such works should explicitly say: "a detailed chapter-table precedes the body; do NOT treat reading its headings as reading the corresponding body chapters."

**Principle:** Line-count is a poor proxy for reading-effort when a source duplicates its own content (TOC, indices, parallel translations, untranslated originals). Density-weighting in Step 2 should be computed on *body* text with such blocks identified up front, and the faithfulness mandate should name TOC-sampling as a specific failure mode distinct from general TOC-triage.

### Observation 7: Step 7 "git mv" assumes raw sources are tracked; they often aren't

**Date:** 2026-06-28
**Session context:** Completing the multi-scope ingest of Zachhuber, *The Rise of Christian Theology* (Scopes 3–6); filing the raw source out of `raw/` root per ingest Step 7.
**Skill:** Project ingest workflow (CLAUDE.md, Ingest Step 7 / OCR rule)
**Type:** internal
**Phase/Area:** Ingest Workflow → Step 7 (file the raw source out of `raw/` root)

**Issue:** CLAUDE.md Step 7 directs `git mv` to relocate a fully-ingested raw file into its typed subfolder. The Zachhuber `.txt` was untracked (raw sources in this repo are frequently not added to git), so `git mv` failed with "not under version control." A plain `mv` was the correct fallback and preserved content.

**Suggested improvement:** Reword Step 7 to "`git mv` if the file is tracked, otherwise `mv`" (or "move the file — `git mv` when tracked"). Same applies to the OCR replacement rule. Prevents a failed first attempt every ingest where the raw file was never committed.

**Principle:** Workflow instructions that hard-code a VCS-aware command should state the plain-filesystem fallback, since source assets are often untracked. Match the command to the file's actual tracking state rather than assuming it.

### Observation 8: Codifying a manually-applied standard into the workflow doc

**Date:** 2026-06-28
**Session context:** User had previously asked for texts and concepts to be bilaterally cross-linked (done manually). This session: user asked to "encode that standard into the CLAUDE.md workflow."

**Skill:** Project ingest/lint workflow (CLAUDE.md)
**Type:** internal
**Phase/Area:** Naming and Linking Conventions + Lint Workflow

**Issue:** A standard was first applied as a one-off manual task (bilateral text↔concept cross-linking), then later the user wanted it promoted to a durable rule in CLAUDE.md. The promotion required two coordinated edits: stating the rule in the conventions section AND adding a matching enforcement check to the Lint Workflow, so the rule is verified rather than aspirational. The general reciprocity principle (text↔commentator, figure↔group, sect↔group) was already latent in the doc but uncodified.

**Suggested improvement:** When the user asks to "encode/standardize" something that was just done manually, default to (a) writing the rule in the relevant convention section AND (b) adding a corresponding check to the Lint/verification workflow — a rule without an enforcement hook tends to be ignored during creative flow (the skill's own Pre-Flight Principle). Also scan whether the specific request (texts↔concepts) is an instance of a more general latent pattern (reciprocal linking) worth generalizing.

**Principle:** "Codify what we just did" requests recur in long-lived wiki/knowledge-base projects. The reliable encoding is rule + enforcement check, not rule alone; and a narrowly-phrased request is often an instance of a broader principle the doc should state generally.

### Observation 9: Subagents write extraction digests, not pages, when an ingest touches many shared central pages

**Date:** 2026-06-28
**Session context:** Ingesting Ehrman, *How Jesus Became God* (16k-line monograph) into a mature wiki with extensive pre-existing Christology infrastructure (incarnation, logos-christology, trinity, bodily-resurrection, two overlapping Jesus pages, etc.).
**Skill:** New skill candidate / project-workflow refinement (CLAUDE.md "Deployed Subagent Strategy")
**Type:** internal
**Phase/Area:** Ingest workflow — division of labor between subagents and main thread

**Issue:** CLAUDE.md's default has subagents "own bulk extraction" and create/write pages within boundaries. But this book's content mapped onto ~20 *already-existing, densely-written* central pages plus a pre-existing duplication (two Jesus figure pages). Having 7 parallel subagents write to those shared pages would have caused write collisions and forced taxonomy decisions onto agents. Instead I had each subagent produce a faithfulness-anchored **digest note file** (claims + verbatim quotes + line loci, grouped by suggested target page) and did *all* wiki-page writing/integration on the main thread. Result: zero collisions, coherent cross-linking, lint-clean, and the delicate two-Jesus-page situation handled by judgment rather than by an agent.

**Suggested improvement:** Note in the ingest workflow that when a scope maps predominantly onto *existing shared central pages* (vs. spawning many new disjoint pages), the throughput win from subagents is best taken as **parallel extraction into digest files**, with the main thread owning all integration — a clean special case of "main thread owns structure; subagents own bulk extraction."

**Principle:** Parallelism should be applied to the part of the work that is genuinely partitionable (reading + faithful extraction by line-range) and withheld from the part that has shared mutable state (integration into central pages). When the shared-state surface is large, push agents one step earlier in the pipeline (notes, not edits).

### Observation 10: Subagent extraction-reports (not direct page writes) for extension-heavy ingests into a mature wiki

**Date:** 2026-06-28
**Session context:** Ingesting J.N.D. Kelly's *Early Christian Doctrines* (whole book, ~20k lines) into the Religion wiki, which already had very rich patristic coverage.
**Skill:** Religion wiki ingest workflow (CLAUDE.md "Deployed Subagent Strategy")
**Type:** internal
**Phase/Area:** Step 3–4 of the Deployed Subagent Strategy (subagents own bulk extraction)

**Issue:** CLAUDE.md's default has Sonnet subagents *write wiki pages* within an exclusive title namespace. For this ingest the value was almost entirely in *extending existing* pages (trinity, origen, tertullian, irenaeus, eucharist, etc.) that many chunks touch simultaneously — so letting subagents write directly would have caused write collisions and uncoordinated edits to mature pages. Instead each subagent produced a structured extraction REPORT (claims organized by target wiki page, each with a verbatim grounding quote + line locus) and the main thread did all filing. This preserved faithfulness, kept all taxonomy/cross-link decisions on the main thread, and avoided collisions.

**Suggested improvement:** Add an explicit branch to the ingest workflow: when a scope mostly *extends existing* pages rather than creating disjoint new ones, instruct subagents to return extraction reports (grounding-quoted, page-keyed) and have the main thread integrate, rather than writing pages directly. Reserve direct-write subagents for green-field scopes with cleanly partitionable new titles.

**Principle:** Match the subagent output mode to the filing topology. Disjoint new pages → subagents write. Heavy overlap onto shared existing pages → subagents report, main thread writes. The faithfulness mandate (grounding quote + locus) is what makes report-then-integrate safe.

### Observation 11: Verify page existence by tool, never by remembered directory listings

**Date:** 2026-06-28
**Session context:** Same Kelly ingest; creating ~33 new wiki pages with dense cross-links.
**Skill:** Religion wiki ingest workflow
**Type:** internal
**Phase/Area:** cross-linking / lint

**Issue:** I linked `[[middle-platonism]]` and `[[neoplatonism]]` as if concept pages existed, from memory of an early `ls`. In fact only a `middle-platonists` *group* page existed and `neoplatonism` did not exist at all — producing red links caught only by the final lint. Memory of a large directory listing is unreliable for exact slugs (group vs concept, singular vs plural).

**Suggested improvement:** Before emitting a wiki link to a page you did not create this session, confirm the exact slug exists (grep the target dir or rely on the lint pass) rather than trusting a remembered `ls`. When the user defers linting to the end, budget for a red-link fix pass on every newly created page.

**Principle:** Treat remembered file listings as hints, not facts; the cheap mechanical check (grep/lint) is the source of truth for link targets. This is the wiki analogue of the general rule "verify before asserting."

### Observation 12: Extraction subagents embed raw line-loci in finished page prose

**Date:** 2026-06-28
**Session context:** Ingesting Lewis Ayres, *Nicaea and Its Legacy* via the Deployed Subagent Strategy (9 Sonnet agents). Agents were told to ground claims with verbatim quotes + book/cache line loci in their NOTES files, and separately to create new wiki pages they owned.
**Skill:** CLAUDE.md "Deployed Subagent Strategy" (project ingest workflow) — also relevant to the task-observer's faithfulness/throughput guidance.
**Type:** internal
**Phase/Area:** Step 3 (subagent prompts) / Step 4 (review and tie together)

**Issue:** Every new page the subagents authored was littered with raw extraction loci in the finished prose — e.g. "(l.599–600)", "(cache l.238–241)", "(lines ~897–899)", "(~1739)". The faithfulness mandate correctly requires verbatim-anchored loci *during extraction*, but the agents carried those loci into the published page bodies (not just their notes). Cleaning them required a multi-pass UTF-8-aware regex strip, which then damaged several legitimate adjacent citations (mixing "; cache l.X" inside real parentheticals like "(Hilary, *Synod.* 11; cache l.238–241)") and produced unbalanced parens and word-smush ("throughdoes", "footnote atindicates") needing hand repair. Roughly 25% of the main-thread integration time went to artifact cleanup.

**Suggested improvement:** In the Deployed Subagent Strategy, add an explicit rule to the subagent page-creation prompt: "Line/page loci are for your NOTES file and your own verification ONLY. In any finished wiki page you author, cite only real source references (work titles, book/section/letter numbers, e.g. *C. Eun.* 1.20; Ep. 234) — NEVER raw book-line or cache-line numbers (l.NNN, cache l.NNN, ~NNNN, lines NNN–NNN)." Optionally add a main-thread Step-4 grep gate: `grep -nE 'cache|\bl\.[0-9]|\(~[0-9]|lines? ~?[0-9]+[–-]' <new pages>` must return empty before bookkeeping.

**Principle:** When a workflow asks subagents to *ground* their extraction with internal source coordinates, those coordinates leak into deliverables unless the prompt explicitly separates "evidence I record for verification" from "citations that belong in the finished artifact." Make the boundary explicit in the prompt and enforce it with a cheap mechanical check, rather than relying on a post-hoc strip that can corrupt adjacent real content.

### Observation 13: Subagent extraction blocked by content filter — a recovery case beyond rate limits

**Status:** ACTIONED — Applied to Religion-wiki CLAUDE.md, Step 3 recovery clause (content-filter block named as a failure mode; recovery keyed off "chunk didn't come back correctly"; pre-cut caches made mandatory). Review 2026-07-18.
**Date:** 2026-06-28
**Session context:** Ingesting two sources on Mithraism/Freemasonry. Deployed 3 background Sonnet extraction agents over disjoint line-ranges of *Mithraism in Ostia*. The agent assigned the "Christ and Mithra" chapter (a Christianity-vs-Mithras religious comparison) returned `API Error: Output blocked by content filtering policy` and wrote no notes file; the other two succeeded normally.
**Skill:** Religion-wiki CLAUDE.md "Deployed Subagent Strategy" (Step 3 recovery clause)
**Type:** internal
**Phase/Area:** Ingest workflow — subagent failure recovery

**Issue:** CLAUDE.md Step 3 only anticipates *rate-limit* (429) subagent failures: "If a subagent fails (e.g. 429), the main thread recovers that range alone." This session surfaced a second failure mode — a **content-filter block** on benign comparative-religion/heresy material — with the same correct response: the main thread read the range from the pre-cut cache file and integrated it directly (labeled as main-thread recovery). The recovery worked smoothly precisely because per-range cache files had already been cut, so no re-read of the big source was needed.

**Suggested improvement:** Generalize the Step 3 recovery clause from "(e.g. 429)" to "any subagent failure — rate limit, content-filter block, or crash." Add a one-line note that pre-cutting per-range cache files (already recommended) is what makes content-filter recovery cheap, since the main thread can re-read the exact slice. Comparative-religion ingests (Christianity vs. mystery cults, heresiology, polemic) are an elevated-risk category for filter blocks.

**Principle:** When a workflow delegates bounded chunks to subagents, the recovery design should key off "a chunk didn't come back" rather than off any specific cause. Naming only one failure mode (rate limits) invites hesitation when a different one occurs. Pre-staged inputs (cache files) turn any single-chunk failure into a cheap main-thread recovery.

### Observation 14: Re-ingested an already-ingested source because Step-1 scaffolding didn't check for an existing source page

**Status:** ACTIONED — Applied to Religion-wiki CLAUDE.md as new Step 0 pre-flight (grep author+title before scaffolding; resume an existing ledger rather than duplicating). Review 2026-07-18.
**Date:** 2026-06-28
**Session context:** Asked to ingest Pelikan, *The Christian Tradition* Vol. 1. I scaffolded by checking related patristics pages (commentators, concepts) to "file lean," then created a source page (`pelikan-christian-tradition-vol1`), deployed extraction agents over Chapter 1, and began filing — before discovering that an **earlier session had already ingested Chapters 1–2 in full** under a different slug (`pelikan-emergence-catholic-tradition`, 12 inbound links, with concept pages already built). I had created a duplicate source page and re-extracted Chapter 1 wastefully.

**Skill:** Religion-wiki CLAUDE.md — Ingest Workflow, Step 1 ("Scaffold first") / Deployed Subagent Strategy
**Type:** internal
**Phase/Area:** Ingest scaffolding — pre-flight existence check

**Issue:** Step 1 says to "create or name the key linkable pages" and survey related pages, but it does not include an explicit **"does a source page for THIS source already exist?"** check. Surveying *topic* pages (commentators/concepts) is not the same as searching for the *source's own* page — the duplicate had a non-obvious slug (`...-emergence-catholic-tradition` vs. the title-literal `...-christian-tradition-vol1`), so a topic survey missed it. The tell was only caught when an existing concept page (`divine-impassibility`) was found already citing Pelikan under the other slug.

**Suggested improvement:** Add to Step 1 a mandatory pre-flight: before scaffolding a new source page, grep the wiki for the **author surname and distinctive title words** (e.g. `grep -ril "pelikan" wiki/scholarship/`) and for any page already citing the source, to detect an existing source page (possibly under a different slug) and an in-progress coverage ledger. If found, resume that ledger instead of creating a new page. This is especially important because multiple sessions (sometimes same-day/parallel) work the same wiki.

**Principle:** "File lean" requires checking for the *source's own* prior footprint, not just related topic pages. In a multi-session knowledge base, the first scaffolding action for any ingest should be an existence check keyed on author+title, because duplicate-detection by slug-guessing fails when naming conventions vary between sessions. Cheap grep up front prevents wasted parallel extraction.

### Observation 15: Verify the body/back-matter boundary before assigning the final scope's line-ranges

**Status:** OPEN

**Date:** 2026-06-28
**Session context:** Ingesting Pelikan, *The Christian Tradition* Vol. I (PDF→text), 7-scope plan by chapter.
**Skill:** Religion wiki ingest workflow (Deployed Subagent Strategy)
**Type:** internal
**Phase/Area:** Step 2 (split scope by line-ranges)

**Issue:** For the final chapter I set the scope end from a grep that found the "INDEX" marker at line ~26781 and assumed the chapter body ran to there. In fact the bibliography began ~24313 and the index ~25231; the true chapter body ended ~24700. The second of two subagents was handed lines 24700–26780, which were entirely bibliography + index — it returned "no extractable prose," wasting the agent. The first agent (22644–24700) happened to cover the whole real chapter.

**Suggested improvement:** Before partitioning the LAST scope of a book, locate not just the index but the **start of the back matter** (bibliography / "Selected Secondary Works" / notes / "INDEX") and set the body-end to the first of those. A quick `grep -nE "bibliograph|selected (secondary|works)|^notes|^index"` over the tail, then read a few lines around the hit to confirm prose vs. apparatus.

**Principle:** A book's "end" for ingest is where the *argument* ends, not where the file ends. Back matter (bibliography, index, appendices) is often 10–15% of an OCR/extracted text; mis-estimating the body-end wastes a whole subagent on apparatus. Verify the prose/apparatus boundary, don't infer it from the index marker alone.

### Observation 16: Obsidian table auto-format breaks aliased wikilinks in timeline matrices

**Status:** OPEN

**Date:** 2026-06-29
**Session context:** User reported "links not completed" in wiki/timelines; found christianity/comparative/islam timeline tables corrupted.
**Skill:** Wiki maintenance / lint workflow (CLAUDE.md timeline conventions)
**Type:** internal
**Phase/Area:** Timeline hub tables; lint_wiki.py red-link detection

**Issue:** Three timeline files had their tables silently mangled by an Obsidian table auto-formatter (likely the table/prettier plugin triggered on save). The formatter treated the `|` inside `[[slug|alias]]` wikilinks as table-column delimiters, splitting each aliased link into two broken halves (`[[slug` + `alias]]`) and inflating tables with bogus columns. This produced ~70 red links flagged by lint_wiki.py. The clean versions were intact in git HEAD; `git checkout HEAD --` on the three files fully resolved it.

**Suggested improvement:** CLAUDE.md timeline conventions already warn about backslash-escaped pipes in wikilinks inside tables. Extend that warning: aliased pipes inside table-cell wikilinks are fragile against Obsidian's table formatter. When lint surfaces a cluster of red links whose targets are valid-slug + space/diacritic fragments all from the same timeline file, suspect table-formatter corruption and diff against HEAD before hand-fixing links. Consider disabling table auto-format for wiki/timelines, or using HTML/non-table layout for the matrix.

**Principle:** A burst of red links localized to recently-modified files with split-token targets is a signature of mechanical reformatting, not authoring errors — check version control before manual repair.

### Observation 17: Subagent silent-hang is a third failure mode the recovery clause should name

**Status:** ACTIONED — Applied to Religion-wiki CLAUDE.md, Step 3 recovery clause (silent-hang named as a failure mode, with transcript-mtime liveness detection). Review 2026-07-18.

**Date:** 2026-06-29
**Session context:** Ingesting *The Divine Comedy*. Deployed 3 background Sonnet agents over disjoint Inferno line-ranges (cantos 1–11, 12–23, 24–34), each with a pre-cut cache file. Agents A and C completed and wrote their notes files. Agent B (cantos 12–23) read its full range, emitted the assistant message "Now I have enough material. Let me write the structured notes file." — and then never wrote the file. Its transcript mtime stopped advancing for ~18 minutes with no error, no 429, no content-filter block. The main thread detected the stall by comparing transcript mtime to wall-clock, stopped the agent, and recovered the range itself from the pre-cut cache slice (the Kirkpatrick notes file gave per-canto sin/contrapasso/figures).

**Skill:** Religion-wiki CLAUDE.md "Deployed Subagent Strategy" (Step 3 recovery clause)
**Type:** internal
**Phase/Area:** Ingest workflow — subagent failure recovery

**Issue:** Step 3 names rate-limit (429) failures; Observation 13 added content-filter blocks. This session surfaced a third mode: a **silent hang** where the agent completes its reading and announces intent to write, then stalls indefinitely with no terminal error and no output file. Unlike 429/filter failures, nothing notifies you — the agent just sits "running." Detection requires actively comparing the transcript's mtime against wall-clock (a stalled transcript = hung agent), since the completion notification never fires.

**Suggested improvement:** Generalize the Step 3 recovery clause once more: "any subagent that doesn't return a usable artifact — rate limit, content-filter block, crash, OR silent hang (transcript mtime frozen while status shows 'running' and no output file appears) — is recovered by the main thread from the pre-cut cache slice." Add: when several agents are deployed and most finish quickly, treat a lone straggler whose transcript hasn't advanced in ~10+ min as hung; stop it and recover rather than waiting on a notification that won't come. This vindicates pre-cutting cache slices (Obs 13): recovery cost was one Read of the notes slice.

**Principle:** A delegation-recovery design must key off "no usable artifact came back," detected by a liveness signal the main thread controls (output-file presence + transcript mtime), not off receiving an error. Some failures are silent; if recovery waits for an error event, it waits forever. Pre-staged inputs make any single-chunk recovery cheap regardless of failure cause. [[deployed-subagent-recovery]]

### Observation 18: Boundary gap when OT 8 content straddles two cache ranges

**Status:** OPEN

**Date:** 2026-06-30
**Session context:** Ingesting Scientology OT Levels PDF (22K lines, 7 agents). Range E ended at the title of OT 8 with no body; Range F began with the Free Zone debrief. Agent E correctly flagged the gap; main thread recovered by reading lines 15590–15720 directly.
**Skill:** Religion-wiki CLAUDE.md "Deployed Subagent Strategy" (Step 3)
**Type:** internal
**Phase/Area:** Ingest workflow — cache range boundary alignment

**Issue:** Splitting cache files at even line numbers without checking whether a critical section starts near that boundary caused the original OT 8 HCOB body to fall in neither range E nor range F — the title was in E, the body in F, but Agent F began with the Free Zone debrief and treated OT 8 as already covered. Flagging by Agent E enabled recovery (main thread read directly), but a brief two-agent gap occurred.

**Suggested improvement:** Before finalizing cache splits, grep for "theologically critical" section headers (in this corpus: HCOB titles marked SECRET) and verify that no critical section straddles a split boundary. If one does, adjust the boundary ±50 lines to include the complete section in one agent. Add to Step 2 of the Deployed Subagent Strategy: "For text with clearly demarcated high-importance sections, verify that no section header falls within 20 lines of a split point."

**Principle:** Cache splits at round line numbers are convenient but theologically naive — align splits to section boundaries for high-stakes content, especially when sections are short enough that their entire body could easily straddle a boundary.

### Observation 19: A user-requested re-ingest still requires the existing-source pre-flight check

**Status:** ACTIONED — Applied to Religion-wiki CLAUDE.md Step 0: pre-flight is explicitly NOT waived by a user-requested re-ingest; completed ledger routes to a standards-compliance audit, with findings split into wiring defects vs. content gaps. Review 2026-07-18.
**Date:** 2026-07-18
**Session context:** User asked to "re-ingest" Vermes, *The Complete Dead Sea Scrolls in English*, on the stated premise that previously-ingested sources may not meet the updated CLAUDE.md. The Obs-14 pre-flight grep found an existing source page with a complete coverage ledger (lines 1–22830 of a 22,831-line file, "no portion deliberately omitted") and ~25 downstream pages. A full re-extraction would have been almost entirely wasted.
**Skill:** Religion-wiki CLAUDE.md — Ingest Workflow, Step 1 (Scaffold first) / Obs 14 follow-on
**Type:** internal
**Phase/Area:** Ingest scaffolding — pre-flight existence check under explicit re-ingest instruction

**Issue:** Obs 14 framed the existence check as protection against *accidental* duplicate ingests. This session surfaced the harder case: the user **explicitly instructed** a re-ingest. An explicit instruction reads as authorization to skip the check — but the user's premise (that the old ingest was substandard) was itself the thing needing verification. The check found the extraction was sound and complete; the actual defects were **wiring**, not extraction: a phantom `essenism` canon_scope slug used on 15 text pages with no backing page, a group/sect bare-slug collision on `essenes`, 8 text pages missing Hermeneutical Tracking, and two missing back-links. None of these would have been fixed by re-reading the source — and a re-ingest would likely have reproduced them.

**Suggested improvement:** Extend the Step 1 pre-flight so it fires on **re-ingest requests too, not only new ones**, and add a decision rule: when the source page already shows a completed coverage ledger for the requested scope, do NOT re-extract by default. Instead run a **standards-compliance audit** of the existing cluster against current CLAUDE.md (frontmatter completeness, required body sections, hermeneutical tracking, canon_scope slug integrity, bilateral cross-links, red links) and report the gap list. Re-extraction is warranted only where the ledger shows an unfinished scope or the audit finds *content* gaps, not wiring gaps. Distinguish these two failure classes explicitly in the report.

**Principle:** When a user requests rework on the premise that prior output is substandard, verify the premise before acting on it — the premise is a hypothesis, not an instruction. Aging output usually fails newer standards at the *wiring* layer (links, slugs, schema fields) rather than the *extraction* layer, and wiring defects are repaired far more cheaply than they are regenerated. An explicit instruction to redo work raises the value of the pre-flight check rather than waiving it.

### Observation 20: The faithfulness mandate doubles as range-validation — agents catch the main thread's bad cuts

**Status:** ACTIONED — Applied to Religion-wiki CLAUDE.md: Step 2 body-vs-TOC grep rule with in-text marker confirmation, and Step 3 fourth failure mode (agent reports range lacks assigned material) plus the do-not-soften-faithfulness note. Review 2026-07-18.
**Date:** 2026-07-18
**Session context:** Repairing the Vermes DSS cluster. I cut six ranges from the source for hermeneutical re-extraction, locating the Angelic Liturgy by grepping for its section heading in the table of contents rather than in the body — landing on lines 11400–12357, which contain Berakhot, Blessings (1QSb) and calendrical texts, but not the Songs of the Sabbath Sacrifice at all. The assigned agent opened its report with an explicit scope caveat: "range_D_angelic.txt does NOT contain the substantive text of the Songs of the Sabbath Sacrifice... I am reporting exactly what is present and flagging the rest as absent, per the faithfulness rule." It further identified that the chariot imagery in its range belonged to 4Q286, a different composition, and warned the material "should not be merged into the Angelic Liturgy's own hermeneutical-framework section." The range was re-cut to 10008–10600 and re-run.
**Skill:** Religion-wiki CLAUDE.md — Deployed Subagent Strategy (Steps 2–3) / faithfulness mandate
**Type:** internal
**Phase/Area:** Range assignment and subagent instruction design

**Issue:** This is a failure mode not covered by the Step 3 recovery clause, which anticipates a chunk *not coming back* (rate limit, content-filter block, silent hang — Obs 13, 17). Here the chunk came back complete and on time; the **main thread's range assignment was wrong**. Nothing in the workflow validates that a named range actually contains the text it is labelled with. What caught it was the faithfulness instruction — the explicit requirement to say "not present in this range" rather than fill gaps from background knowledge. Without that instruction a capable agent would very plausibly have written a fluent, entirely ungrounded Angelic Liturgy section from general knowledge of Ezekiel and merkabah mysticism, and it would have read as correct. The same instruction also caught a subtler error: attributing 4Q286's chariot language to 4Q400–407.

**Suggested improvement:** Two changes. (1) In Step 2, when locating a section by grep, require matching against a **body** occurrence, not the first hit — the first hit is usually the table of contents. Confirm by checking that the candidate range contains expected in-text markers (a fragment siglum, an incipit), not just the title. This is the same class of error as Obs 1, generalized from chapter-boundaries to any grep-located range. (2) Add to the Step 3 recovery clause a fourth case: **the agent reports its range does not contain the assigned material.** Correct response is to re-cut and re-run that range, never to accept a substitute from an adjacent composition. Note in the skill that the faithfulness mandate is what surfaces this, so it should never be softened for convenience.

**Principle:** A well-designed faithfulness constraint is not only an accuracy control on the delegate — it is an **error-detection channel back to the delegator**. Requiring a subagent to say "this is not here" rather than fill the gap converts silent, plausible fabrication into a loud, cheap signal that the orchestrator's own assumptions were wrong. Instructions that permit gap-filling destroy this channel precisely when it is most needed, because the resulting output is fluent and therefore unfalsifiable at review time.

### Observation 21: Progress-visibility rule failed to reach the moment of decision during long subagent runs

**Date:** 2026-07-18
**Session context:** Scope 1 fidelity re-ingest of France, *The Gospel of Matthew* (NICNT) — 8 extraction subagents, 6 integration subagents, runs of 5–11 minutes each.
**Skill:** CLAUDE.md ingest workflow (Progress Checklist section)
**Type:** internal
**Phase/Area:** Progress Checklist, rule 4 ("No multi-minute silence")

**Issue:** CLAUDE.md states explicitly: "If extractors or integration will run more than ~1–2 minutes, interleave short user-visible status with tool work," and "Silent progress is a defect." The rule was read at session start and still failed three times. The user asked "How is progress coming?", then "Are you frozen?", then "I think you froze up there" — across two separate stretches. Worse, the second failure was caused by *answering* the first: the agent replied to the user's mid-turn message and then did not relaunch the interrupted subagent, so genuinely nothing was running while the user waited. The root cause is structural: subagent calls are blocking and return only on completion, so there is no natural point *during* a 10-minute run at which the agent is prompted to emit status. The rule lives in narrative prose and has no enforcement hook at the moment it applies.

**Suggested improvement:** Convert the rule from narrative guidance into a structural precondition in the Deployed Subagent Strategy, Step 3: **before** any batch of Agent calls, post a user-visible message naming the exact number of agents, their ranges, and an explicit "this will take several minutes with no output until they return." Add to the Step 3 bullet list a required pre-spawn line item, and add to the Recovery paragraph an explicit note that answering a mid-turn user message does not discharge the obligation to relaunch an interrupted agent — verify the spawn actually landed before responding.

**Principle:** When a rule governs behaviour during a blocking operation, prose guidance cannot enforce it — there is no execution point inside the block at which the agent re-reads the rule. Such rules must be relocated to the *boundary* of the operation (a precondition before entering, or a postcondition on exit) where the agent is actually making a decision. This generalises to any "don't go quiet during X" or "keep the user informed while Y" instruction.

### Observation 22: Intake integrity check should test for dropped apparatus, not only truncation

**Date:** 2026-07-18
**Session context:** France NICNT Matthew re-ingest. Extractor A discovered that the plain-text conversion had dropped every footnote *body* while keeping superscript markers fused into running text ("the law17"). Two structural tables were also blank.
**Skill:** CLAUDE.md ingest workflow (Step 0b — Intake integrity)
**Type:** internal
**Phase/Area:** Step 0b word-count / conversion check

**Issue:** Step 0b's integrity check is built around detecting *truncation* — comparing `wc -w` against expected length, grepping TOC headings in the body, sampling folio headers for gaps. This source passed every one of those tests: 613,422 words, all six body sections present at plausible length. The defect was of a different kind — the conversion was complete at the section level but had silently discarded an entire *evidence class*. For a critical commentary this is severe: France conducts much of his engagement with secondary literature in footnotes, so the loss systematically strips reported-scholar attributions while leaving his main-text exposition intact. An integrator working only from main text would have no signal that attributions were missing, and would be tempted to supply names from background knowledge. The defect was caught only because the first extractor happened to notice and report it, then it was manually propagated into the remaining seven prompts.

**Suggested improvement:** Add to Step 0b a third check alongside word-count and TOC-grep: **apparatus-presence sampling.** Grep for the shape of footnote bodies (numbered lines at column start, or a notes block per chapter), for blank runs immediately following table lead-ins ("as follows:", "may be set out as follows:"), and for superscript digits fused to word boundaries (`[a-z][0-9]{2,4}\b`) which indicate markers surviving without bodies. Record the result in `reliability_notes` before extraction, and — critically — include the finding in *every* extractor prompt from the start rather than discovering it in range 1 and back-propagating.

**Principle:** Completeness checks that measure *volume* miss defects that remove a *category*. A conversion can preserve 100% of sections and still discard 100% of one evidence class. Where a source has structurally distinct registers (body / apparatus / introduction), integrity checking must verify each register independently — and the check belongs before agent dispatch, since a defect found in range 1 of 8 has already mis-specified the other seven prompts.

### Observation 23: Re-ingest audit should distinguish claims that CONTRADICT the source from claims merely unsupported by it

**Date:** 2026-07-18
**Session context:** France NICNT Matthew re-ingest. Auditing the 2026-06-05 pass against 2,091 freshly extracted claims turned up three distinct defect types on `texts/matthew`.
**Skill:** CLAUDE.md ingest workflow (Step 0 — Pre-flight, re-ingest decision table)
**Type:** internal
**Phase/Area:** Step 0 finding/action table, "fidelity / content defects" row

**Issue:** The Step 0 table lumps all fidelity problems into one row — "ungrounded claims, TOC-reconstruction, wrong loci, single-source theosophy in bare wiki voice…" — all triggering the same action (re-extract the affected scope). In practice the defects found were of three materially different severities: (a) **unsupported detail** — France's pre-70 dating presented with three temple-passage arguments he does not make; (b) **fabricated citation** — a Papias position attributed to "NICNT, 2007, pp. 14–22," where Papias is not named in France's Introduction at all; and (c) **direct contradiction** — the page stated the antitheses "are not contradictions of Torah but intensifications," where France's actual position is "bypass, not abolish" with a taxonomy in which only two of six intensify. Type (c) is the most damaging, because it is confidently phrased, plausible-sounding, reflects the *conventional* reading of the passage, and would be quoted by a downstream reader as France's view. It is also the hardest to detect without a full re-read, since nothing about the sentence looks wrong. Types (a) and (b) at least leave a trace (a suspiciously specific citation; argument detail without a locus).

**Suggested improvement:** Split the fidelity row of the Step 0 table into three graded findings with distinct reporting obligations. Require that any **contradiction** found during a re-ingest audit be (i) recorded explicitly on the source page under a "Defects corrected" heading naming the old claim and the new, (ii) logged in `log.md` as a named correction, and (iii) checked for propagation — a contradicted claim on a hub page has usually been copied to the pages that link it. Add a note that background-knowledge contamination most often surfaces as the *conventional* scholarly reading standing in for the commentator's actual, more distinctive position.

**Principle:** The most dangerous ingest defect is not the unsupported claim but the plausible one that inverts the source. Textbook-consensus contamination is self-camouflaging precisely because it reads as correct; a commentator worth ingesting is usually worth ingesting *because* he departs from consensus, so the places where an old ingest sounds most conventional are the places most likely to have overwritten his actual view. Audits should target agreement-with-consensus as a risk signal, not treat it as reassurance.

### Observation 24: Line-count slicing under-weights dense commentary body, orphaning pericopes in slice tails

**Status:** OPEN

**Date:** 2026-07-18
**Session context:** Re-ingesting Bock, *Acts* (BECNT). The commentary body (350K words) averaged ~50 words/line (long unwrapped paragraphs). I cut 8 disjoint slices by line number aligned to running-header positions. Every agent faithfully extracted only its briefed verse-range and flagged the rest; the net result was that FIVE pericopes fell in the unextracted TAIL of one slice while the next slice began after them (Acts 3:1–4:31, the Stephen cycle 6:8–8:1a, the first journey 13:1–14:28, the second journey 15:36–18:23, and a thin 1:1–11). Cause: (a) I estimated slice content from running-header/outline line positions, but the book had a global outline block PLUS a per-unit outline recap, so a header's line number is NOT where its exposition sits; (b) exposition density meant each slice held more verses than its line-span implied, so agents "extracted their briefed verses and stopped," dropping the tail. Recovery was clean (density-grep to locate real exposition, re-cut 4 recovery slices, re-extract) precisely because the faithfulness mandate made each agent report "not present in this range."

**Suggested improvement:** Add to CLAUDE.md Step 2 (Deployed Subagent Strategy): for prose-dense commentary where lines are long/unwrapped, size and place cuts by a **word-count cumulative** map, not line count, and locate each boundary at a verified **exposition opening in the body** (the prose paragraph after the section header + translation), never at a header/outline-stub line — because works with a detailed-outline front block and per-unit recaps repeat every header 2–3×. Concretely: before spawning, grep the body for section headers, then confirm each intended boundary sits at real exposition by checking local line-length/rich-line density (a stub cluster is short lines; exposition is ~250+ char lines). Also brief each extractor with its exact VERSE range (not just line range) and instruct: "your slice may contain material past your briefed verses — extract to the end of the slice's real exposition and flag overflow, rather than stopping at your briefed endpoint." That converts silent tail-drops into logged overflow the integrator can dedupe.

**Principle:** When work is partitioned for parallel extraction, the failure mode is not bad extraction but bad boundaries. A boundary defined by a structural marker (a header line) can be far from the content that marker names when the source repeats its outline; and a boundary sized by line count mis-estimates coverage when line density is non-uniform. Partition by the quantity you actually care about (words/content), verify boundaries against real content, and make "extract past your nominal endpoint" the default so slice seams over-cover rather than under-cover.
