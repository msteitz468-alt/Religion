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
