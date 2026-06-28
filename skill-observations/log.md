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
