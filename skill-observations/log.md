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
