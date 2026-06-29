# CLAUDE.md — Religious Commentary Wiki

## Overview

A persistent, LLM-maintained wiki for studying religious texts and their commentary
traditions (primary texts, commentators, interpretive schools, theological concepts, and
their historical/philological context).

You (the LLM) write and maintain everything in `wiki/`: all filing, cross-referencing,
synthesis, and bookkeeping. I source documents and direct analysis. Environment is Obsidian;
all files are markdown. Raw sources live in `raw/`; the wiki in `wiki/`. **Never modify the
*content* of files in `raw/`** (relocating them into typed subfolders is permitted — see
ingest Step 7).

---

## Task-Observer Activation (mandatory)

At the start of any task-oriented session (ingest, lint, query, any tool-using work), invoke
the `task-observer` (`one-skill-to-rule-them-all`) skill **before** reading source content or
beginning work. It captures skill-improvement observations and runs the session-start
protocol (weekly-review check, observation log). When loading any skill, also check
`skill-observations/log.md` for OPEN observations relevant to the work and apply their insight
even if the skill file isn't yet updated.

---

## Directory Structure

```
raw/                        # Immutable source documents (content never modified)
  texts/                    # Primary religious texts
  commentaries/             # Commentary works
  scholarship/              # Academic papers, books, articles
  assets/                   # Images, diagrams, manuscript photos

wiki/                       # LLM-maintained knowledge base
  index.md                  # Master index — updated on every ingest
  log.md                    # Append-only ingestion and query log
  overview.md               # High-level synthesis of current scope

  texts/                    # One page per primary text or pericope
  commentators/             # One page per named commentator or school
  figures/                  # One page per major biblical/religious figure
  groups/                   # Peoples, tribes, nations, religious parties, collectives
  locations/                # Places, with historical inhabitants + modern geography
  concepts/                 # Theological, philosophical, hermeneutical concepts
  traditions/               # Two-level hierarchy of religions and their sects:
    [tradition]/            #   one subdir per top-level tradition (christianity/, judaism/, …)
      [tradition].md        #   the Tradition overview page
      sects/[sect].md       #   Sect/denomination/sub-tradition pages
  comparisons/              # Cross-text, cross-tradition comparison pages
  controversies/            # Disputed interpretations and unresolved tensions
  timelines/                # Chronological pages
  queries/                  # Filed answers to significant questions
```

---

## Page Types and Formats

### Text Page (`wiki/texts/`)
Primary texts, books, pericopes, suras, suttas, etc.

```yaml
---
title: [Text Name]
tradition: [Judaism / Christianity / Islam / Buddhism / Hinduism / etc.]
canon_status: [headline only — canonical / deuterocanonical / contested / sectarian / non-canonical]
canon_scope:                 # which traditions/sects treat this text HOW (entries are page slugs)
  canonical_for: []          #   full scriptural canon
  deuterocanonical_for: []   #   secondary / graded / disputed-but-included
  authoritative_for: []      #   cited (liturgy, doctrine, halacha) but NOT scripture
  disputed_by: []            #   canonicity actively contested
  rejected_by: []            #   explicitly excluded / condemned
language_original: [Hebrew / Greek / Arabic / Sanskrit / Pali / etc.]
date_range: [approx composition date or range]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [text, tradition-name, genre]
---
```

Body: textual overview, major themes, narrative summary/structure, manuscript tradition
notes, key interpretive cruxes (verses generating the most disagreement), links to
commentator pages.

**`canon_scope` is required.** Canonicity is a *relation* between text and community, not a
property of the text. Each bucket entry is the slug of a tradition (`christianity`) or sect
(`sethian-gnosticism`). The same text routinely appears in several buckets at once.
`canon_status` is only a coarse one-word headline derived from `canon_scope`. Include a
**Canon and Reception** body section narrating the split wherever non-trivial. Examples:
- **Gospel of Thomas** — `canonical_for: [thomasine-christianity]`; `rejected_by:
  [proto-orthodox-christianity, catholicism, eastern-orthodoxy, protestantism]`; `disputed_by:
  [coptic-christianity]`. Not merely "apocryphal" — canonical for some, rejected by others.
- **Book of Mormon** — `canonical_for: [latter-day-saints]`; `deuterocanonical_for:
  [<Restoration-movement sects>]`; `rejected_by: [catholicism, eastern-orthodoxy,
  protestantism, …]`. Its claim to *continue the biblical narrative* is a **reception fact in
  the body** ("Relationship to the parent canon"), not a bucket — buckets record canonical
  *standing* per community.

### Commentator Page (`wiki/commentators/`)
Individual commentators, schools, or movements.

```yaml
---
title: [Name / School]
full_name: [if individual]
dates: [birth–death or floruit]
tradition: []
affiliation: []
primary_texts_commented: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [commentator, tradition-name]
---
```

Body: biographical context; hermeneutical method (literal/allegorical/moral/anagogical;
peshat/derash/remez/sod; etc.); major works; characteristic positions; known controversies;
influence on later tradition.

### Figure Page (`wiki/figures/`)
Major biblical/religious/historical figures who appear in or are subjects of the texts —
patriarchs, prophets, apostles, kings, priests, founders, including legendary (Enoch,
Melchizedek) and historical (Cyrus, Nebuchadnezzar) persons.

**Scope rule**: create when a person is (a) named in one+ primary texts, (b) subject of
substantial commentary, and (c) not better handled as a concept (significance is biographical/
narrative, not purely doctrinal). Figures who are also commentators (Maimonides, Paul) get
*both* a figure page and a commentator page, cross-linked.

```yaml
---
title: [Figure Name]
also_known_as: [aliases, titles, epithets — e.g. "Israel", "the Apostle", "Rambam"]
tradition: [Judaism / Christianity / Islam / cross-tradition / etc.]
textual_sources: []   # primary texts where the figure appears
dates: [historical / traditional / floruit / "legendary" / "disputed"]
roles: []   # patriarch, prophet, apostle, king, priest, judge, founder, …
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [figure, tradition-name, role-type]
---
```

Body sections:
- **Biographical Overview**: attested biographical data (birth, family, events, death) from
  primary sources. Distinguish textual claims from historical-critical reconstruction; flag
  disputed dates/locations/events rather than presenting one tradition as fact.
- **Primary Source Appearances**: which texts feature the figure and in what capacity; key
  pericopes with a one-line summary of each contribution.
- **Tradition-Specific Reception** (core): how each tradition interprets/develops/contests the
  figure, recorded separately (Jewish, Christian, Islamic, Samaritan, …). Per tradition: the
  primary authoritative source, the dominant interpretive move, intra-tradition disputes.
- **Theological and Narrative Significance**: typological/narrative/doctrinal role.
- **Historicity and Interpretive Controversies**: disputes over existence, dating, identity,
  actions — record positions without adjudicating.
- **Influence on Commentary Traditions**: which commentators made the figure central, and how
  (allegorical and literal-historical uses).

### Group Page (`wiki/groups/`)
Peoples, tribes, nations, ethnic groups, religious parties, social classes, and collective
identities acting as actors/foils (Canaanites, Philistines, "the nations/Gentiles", Pharisees,
Sadducees, Samaritans, the twelve tribes, "the poor").

**Scope rule**: create when the collective is (a) a corporate actor in one+ primary texts, (b)
subject of substantial commentary/typology/identity construction, and (c) not better handled
as a concept. Overlapping cases ("Israel" as both people and concept) may warrant both a
group and a concept page, cross-linked.

```yaml
---
title: [Group Name]
also_known_as: [aliases, self-designations, outsider labels — e.g. "Gentiles / Goyim / Ta ethne"]
tradition: [Judaism / Christianity / Islam / cross-tradition / etc.]
textual_sources: []   # primary texts where the group features
periods_active: [e.g. "Late Bronze–Iron I", "Second Temple / 1st c. CE"]
roles_significance: []  # antagonists, covenant people, model outsiders, heretics, mission field, …
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [group, tradition-name, category-or-period]
---
```

Body sections:
- **Identity and Nomenclature**: etymology/meaning of name(s); self-designation vs. outsider
  labels; terminology shifts across periods/languages; pejorative or honorific usage.
- **Primary Textual Appearances**: key passages/arcs where the group is a collective
  character; one-line summary of each (positive/negative/ambiguous/typological).
- **Tradition-Specific Portraits**: how each tradition interprets/allegorizes/historicizes/
  deploys the group (separately per Jewish, Christian, Islamic, …): canonical sources used,
  main interpretive lens, intra-tradition disagreements.
- **Historical and Archaeological Context**: extra-biblical evidence (inscriptions, material
  culture, ANE parallels); debates over identification/origins/historicity; distinguish
  textual claims from critical reconstruction unless the source adjudicates.
- **Theological and Narrative Significance**: role in the text's architecture (corporate
  personality, foil, object of judgment/mercy, paradigm of faith/apostasy, mission vehicle).
- **Influence on Later Traditions and Controversies**: use in exegesis, preaching, liturgy,
  politics, polemic. Flag sensitive/contested modern deployments ("Amalek", conquest ethics,
  "Pharisee" as epithet) and link resulting controversies pages.

### Location Page (`wiki/locations/`)
Places — cities, regions, mountains, rivers, kingdoms, cult sites — carrying sustained
narrative, theological, or pilgrimage significance. **Must** address historical inhabitants
("who lived there when") and modern geographic identification.

**Scope rule**: create when a place is (a) named with narrative/symbolic weight, (b) the
setting of significant events/figures/cult, and (c) the object of later interpretive/
devotional tradition (Jerusalem/Zion, Babylon, Mount Sinai, Galilee, the Jordan, Rome,
Shechem, Nineveh, the Temple Mount). Minor/incidental place names need no page.

```yaml
---
title: [Location Name]
also_known_as: [modern + ancient names, tell/site designations — e.g. "Tell es-Sultan (Jericho)"]
tradition: [Judaism / Christianity / Islam / cross-tradition / etc.]
textual_sources: []   # primary texts where the location is prominent
periods_inhabited: [settlement history, e.g. "Chalcolithic–present; major phases: EB, Iron Age, Persian, …"]
modern_geography: [current location, nearest settlement, coordinates, terrain — e.g. "Tell es-Sultan, West Bank, ~2 km NW of Jericho; Jordan Rift Valley, ~250 m below sea level; 31.870°N 35.444°E"]
associated_peoples: []  # key groups who controlled/inhabited the site, with dates
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [location, tradition-name, site-type]
---
```

Body sections:
- **Geographical and Historical Overview**: physical setting, strategic/economic importance,
  settlement/political/nomenclature changes over time; separate periods; note major
  destructions/rebuilds/abandonments.
- **Primary Textual Appearances and Inhabitants**: which texts feature the place and why; for
  each period/stratum, who lived there or controlled it (e.g. "Jebusites until David; Judahite
  capital thereafter; … Roman Aelia Capitolina after 135 CE").
- **Archaeological and Extra-Biblical Data**: excavations, key finds, how they relate to or
  challenge the textual portrait; identification debates ("which mound is Ai?").
- **Modern Identification and Geography**: how the site is identified today; current name(s),
  political status, accessibility, identification disputes — enough to locate it on a map.
- **Theological and Symbolic Significance**: why it matters per tradition (Zion theology,
  exile/return, pilgrimage, "holy land", eschatological geography; al-Quds and the Night
  Journey; Christian holy sites; Temple Mount/Western Wall piety).
- **Key Events, Figures, and Controversies**: major events/figures tied to the site; later
  interpretive/political controversies (sacred-space claims, Golgotha location, Temple Mount /
  Haram al-Sharif status).

### Tradition Page (`wiki/traditions/[tradition]/[tradition].md`)
A top-level religion (Judaism, Christianity, Islam, Buddhism, Hinduism, Daoism, …). One
overview page per tradition, at the root of its subdirectory; the parent node for its `sects/`
pages and home of the shared/mainstream canon.

```yaml
---
title: [Tradition Name]
also_known_as: []
type: tradition
date_range: [origin to present / floruit]
canon_core: []                 # texts canonical for the tradition broadly — text page slugs
hermeneutical_frameworks: []   # native interpretive systems (PaRDeS, the Quadriga, Zahir/Batin, …)
major_sects: []                # slugs of the sect pages nested under this tradition
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [tradition, tradition-name]
---
```

Body: definition/self-understanding; historical origin and development; the shared canon and
how canonical authority works; native hermeneutical frameworks; a **map of major sects** (one
linked line each); cross-links to the most central figures, groups, concepts, controversies.

**Non-theistic / multi-canon traditions**: a tradition need not be theistic (Buddhism) or have
a single canon. Where parallel canons share no common ancestor text (Pali Canon vs. Mahayana
sutras vs. Vajrayana tantras), keep `canon_core` minimal (only what is genuinely shared) and
carry divergent canons at the **sect level** (`canon_distinctives` / `key_texts`). For
non-theistic traditions, record the tradition's own account of ultimate reality (*nirvana*,
*dao*) rather than forcing a deity slot; "doctrine"/soteriological goal replaces "theology
proper".

### Sect / Denomination Page (`wiki/traditions/[tradition]/sects/[sect].md`)
A sub-tradition, denomination, sect, movement, school, or lineage *within* a parent tradition
(Gnosticism, Marcionism, Catharism, Rabbinic Judaism, Karaism, Kabbalah, Latter-day Saints,
Sunni/Shia, Theravada/Mahayana/Vajrayana, Zen). A **first-class page type** with its own canon,
hermeneutical rules, and relationship to the parent and to "orthodoxy".

**Scope rule**: create when a sub-tradition (a) is a distinct religious community/school within
a parent, (b) has a canon/doctrine/hermeneutic diverging from parent or siblings, and (c)
generates sustained commentary/identity/polemic.

A sect page is **not** a duplicate of a `groups/` page. Where a group page exists for the same
community ([[gnostics]], [[marcionites]], [[ebionites]], [[montanists]]), keep both and
cross-link: the **group page** = community as social/historical actor; the **sect page** =
sub-tradition as a *system* (canon, doctrine, hermeneutics, relationship to orthodoxy).

```yaml
---
title: [Sect / Denomination Name]
also_known_as: []
parent_tradition: [slug of parent tradition — e.g. christianity]
type: [denomination / sect / movement / school / lineage / normative stream]
dates: [emergence–present / floruit / "extinct (dates)"]
status: [extant / extinct / revived]
relationship_to_orthodoxy: [normative / heterodox / heretical (by whom) / schismatic / independent / self-understood-restoration]
canon_distinctives: []          # texts added/removed/re-ranked/rejected vs. parent — text page slugs
key_doctrinal_distinctives: []
hermeneutical_method: []
key_figures: []
key_texts: []                   # text page slugs central to the sect
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [sect, parent-tradition-name]
---
```

Body sections:
- **Identity and Origins**: what it is, when/where it emerged, out of what parent or prior
  sect; self-designation vs. outsider labels.
- **Relationship to the Parent Tradition**: what it inherits/shares; precise points of
  departure; whether it sees itself as reform, restoration, purification, continuation, or new
  revelation.
- **Canon and Scripture (Canon Divergence)** (core, required): how the sect's canon differs
  from the parent's — texts added, removed/demoted, re-ranked, reinterpreted. Every text the
  sect treats distinctively appears here **and** lists this sect in the right `canon_scope`
  bucket on its own text page. Flag any text whose status differs from the parent.
- **Doctrinal Distinctives**: theological positions defining the sect against parent/siblings.
- **Hermeneutical Method** (mandatory, per Hermeneutical Tracking): how it reads its scriptures
  and the parent's — native rules, esoteric/exoteric layering, authoritative interpreters.
- **Relationship to Orthodoxy and Other Sects**: who regards it as normative/heterodox/
  heretical and on what grounds, *without adjudication* (Contradiction Protocol), with each
  judgment's tradition context. Document mutual condemnations from both sides.
- **Historical Development, Subdivisions, and Influence**: internal schools/offshoots, later
  history, suppression/survival, influence on parent and beyond.
- **Sources Ingested**.

### Concept Page (`wiki/concepts/`)
Theological constructs, hermeneutical methods, recurring doctrinal categories.

```yaml
---
title: [Concept Name]
domain: [hermeneutics / theology / liturgy / law / mysticism / etc.]
traditions_using: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [concept]
---
```

Body: definition, origin, tradition-specific usage variations, key text-concept connections,
cross-links to controversies where contested.

### Comparison Page (`wiki/comparisons/`)
Generated from cross-tradition/cross-commentator queries; filed for permanence.

```yaml
---
title: [Comparison Description]
entities_compared: []
generated_from_query: [brief description]
date: [YYYY-MM-DD]
tags: [comparison]
---
```

### Controversy Page (`wiki/controversies/`)
Interpretive disputes cutting across commentators or traditions.

```yaml
---
title: [Issue in Dispute]
text_locus: [verse, passage, or concept at stake]
positions: []   # named positions
traditions_involved: []
resolution_status: [open / historically resolved / tradition-specific]
last_updated: [YYYY-MM-DD]
tags: [controversy]
---
```

---

## Hermeneutical Tracking — Core Requirement

Track *how* a text is read, not just *what* it says. Every text, commentator, tradition, and
sect page must record the interpretive framework(s) in use; a sect page must record the rules
distinguishing it from its parent. Group and location pages should note tradition-specific
interpretive moves, typological uses, and polemical deployments.

Standard frameworks to identify and tag:
- **Jewish**: Peshat (plain), Derash (midrashic), Remez (allegorical), Sod (mystical) — PaRDeS
- **Christian patristic/medieval**: Literal, Allegorical, Tropological (moral), Anagogical — the Quadriga
- **Islamic**: Zahir (exoteric), Batin (esoteric); tafsir bi'l-ma'thur (tradition-based) vs. bi'l-ra'y (reason-based)
- **Buddhist**: Neyartha (interpretable) vs. Nitartha (definitive); commentarial lineage tracking
- **Daoist**: *commentary-as-transformation* (commentary as practice that transforms the
  adept); track the philosophical/metaphysical reading (xuanxue; Wang Bi) vs. the religious/
  longevity-cultivation reading (Heshang Gong) of the same text
- **Modern critical**: Historical-critical, form, redaction, canonical criticism, reader-response

When ingesting a commentary, identify and explicitly record its framework(s). Flag
cross-tradition comparisons of the same method (allegory in Origen vs. Philo vs. Ibn Arabi)
for comparison-page generation.

---

## Ingest Workflow

Two halves of one workflow: the **Deployed Subagent Strategy** (default — *throughput*: how a
scope is read in parallel) and **Scope & Fidelity** (the standard of *quality*: what each page
must contain and how to partition a work). Subagents are how a scope gets read, never a lower
standard of fidelity.

**Non-negotiable principle: the main thread owns structure; subagents own bulk extraction.**
Subagents never decide taxonomy, page naming, `canon_scope` buckets, sect-vs-group splits, or
cross-links — they extract faithfully within boundaries the main thread already drew.

### Deployed Subagent Strategy (DEFAULT — execution steps)

**Step 1 — Scaffold first, on the main thread.** Before spawning anything, read enough (TOC,
intro, conclusion, targeted sampling) to do the judgment work:
- Identify source type and, for any primary text, its **canonical status per sect/tradition and
  whether that differs from the parent** (drives `canon_scope` + any sect canon-divergence section).
- Write the **source summary page** (in `scholarship/` or the relevant text/commentary page)
  including the **scope plan** (ordered sequence of bounded scopes) and **coverage ledger** skeleton.
- Create or name the **key linkable pages** (central text/commentator/tradition/sect pages and
  the figure/group/location/concept pages the ingest will populate) so subagents inherit names.
- Decide **naming conventions, page taxonomy, and hermeneutical framing**.

Do not spawn any agent until the linkable page names and canon/taxonomy decisions exist.

**Step 2 — Split the scope by disjoint line-ranges.** Divide the in-scope raw text into N
contiguous, non-overlapping chunks by line number.
- **Size N to the material.** Base on *body* length × density (exclude front matter, apparatus,
  indices, untranslated sections): ~one agent per 2,000–3,500 body lines; floor 2–3; up to ~10
  for very large/multi-volume works. **Do not default to 6** — over-splitting starves context.
- **Weight chunks by density/importance**, not even boundaries: dense/pivotal stretches get
  their own agent; lighter narrative combines. Align to natural section boundaries only where
  it doesn't fight the weighting.
- Ranges must be **disjoint** — every line in exactly one chunk.

**Step 3 — Spawn one Sonnet subagent per chunk (staggered + background).** Use the Agent tool
with **`model: sonnet`** and `run_in_background: true`, one per chunk. Each prompt must contain:
its **exclusive line-range** (read only that range); the **relevant schema, naming conventions,
and hermeneutical-tracking requirement**; the **established page names** it may link to (Step 1);
**exclusive ownership of the titles it creates** (distinct title namespace so no two agents
write the same file); and the **faithfulness mandate** (principle 4 below, enforced per agent):
extract only what is in its range, **with verbatim-anchored grounding quotes and line/page
loci**, no outside knowledge, no background summary as source content, no reading beyond range.
- **Staggered deployment (rate-limit mitigation)**: never launch all at once. Spawn in batches
  of 2 (≤3 for lighter ranges), then `sleep 10` before the next batch (20s+ if 429s recur).
  Optionally pre-cut per-range cache files (`/tmp/..._cache/range_N_START_END.txt`) for a cheap
  one-shot read. Collect task_ids; monitor to completion. If a subagent fails (e.g. 429), the
  main thread recovers *that range alone* (read its slice, extract, label the block "Main-thread
  recovery (rate limit on subagent)") and lets the others continue. Do not restart a
  rate-limited agent.

**Step 4 — Review and tie together (main thread).** Dedupe overlapping claims; reconcile naming;
fix cross-links between new pages (subagents only linked Step-1 names); fill the source page's
coverage ledger for the scope read; record **contradictions** on both pages and the relevant
`controversies/` page (Contradiction Protocol); set/extend `canon_scope` on every affected text
page; confirm each new sect/group page is cross-linked to its counterpart. Remove agent
artifacts (stray instructions, prompt echoes, tags — grep first). **File lean** (extend a
central page before creating a new one; de-link tangential mentions rather than spawning stubs).

**Step 5 — Lint and validate.** Run `python Scripts/lint_wiki.py` and resolve what it surfaces
(red links, orphans, commentators/figures/groups/locations/sects mentioned without a page).
Re-run until clean.

**Step 6 — Bookkeeping.** Update `index.md`; tick the source on `outstanding sources.md` if
listed; append the `log.md` entry stating the declared **scope** and whether read in full or in
progress. For a multi-scope work, checkpoint after **each** scope (ledger + index + log,
verified on disk) and continue autonomously to the next; do not pause to ask "what next?".

**Step 7 — File the raw source out of `raw/` root.** Once a source is **fully ingested for its
declared scope** (not mid multi-scope work), `git mv` its file from the top of `raw/` into the
matching typed subfolder (`raw/texts/`, `raw/commentaries/`, `raw/scholarship/`, or
`raw/misc/`). **Relocation only — never alter content** (the "never modify" rule governs
*content*; filing into a subfolder is expected). Then **update every reference to the old path**:
the `Source:` line on the source page, its coverage ledger, and the `log.md` entry. (For an
OCR'd source, this happens together with the PDF-replacement in the OCR rule.)

### Scope & Fidelity (the standard of quality)

Governing principle: **fidelity within a declared scope** — not exhaustiveness. Everything the
wiki attributes to a source must have actually been read in it; not every source must be read
cover to cover. You read what we scope, and you read it honestly.

**1. Scope the ingest first.**
- **Small, bounded sources** (a primary text/pericope, a single commentary, a paper, a short
  monograph) → scope = the whole thing; read it in full.
- **Large reference / multi-volume / survey works** → scope = a named portion (chapter, topic,
  volume, page span). Do not silently expand beyond it.

**Scope it yourself and progress autonomously.** Do **not** ask me to choose a scope each time.
For a large work, *you* partition it into a **scope plan** (an ordered sequence of coherent,
meaty bounded scopes — not one tiny scope per heading), record it on the source's scholarship
page, then work through scopes in order, one per pass, without asking which is next. Checkpoint
after each scope (ledger + index + log, verified). When the work's plan is exhausted, move to
the next unticked source on `outstanding sources.md` and scope it the same way. Surface a choice
to me only when partitioning is genuinely ambiguous, a scope proves too thin (widen it), or
something needs my judgment (sourcing gap, faithfulness problem, contested call) — not for
routine "what next?".

**2. Read the scope in full, in order — no TOC-triage.** Actually read the in-scope text
sequentially; do not scan the TOC/index/a few searched passages and reconstruct. Search tools
may *supplement* the read (locate a cross-reference, verify a term, relocate a passage already
read) but never *substitute* for it.

**3. Read in large spans; file in lean batches.** Prioritize reading over filing. Read a
substantial span keeping **brief, verbatim-anchored notes** (key claims with line/page locus,
so attribution stays checkable), then file the batch. Stop to file only when needed — at a
natural boundary, when unfiled notes risk losing detail, when later material depends on a page
earlier material warranted, or to record a contradiction while both sides are fresh. **File
lean**: extend a central page before creating one; create a page only when the subject warrants
it; de-link a tangential mention rather than spawning a stub. Notes are taken *during* the read
— not a licence to skim and reconstruct from memory.

**4. Faithfulness — record only what the source says.** Attribute to a source only content you
actually read in it. **Never present background knowledge, a textbook summary, a familiar term,
or an inference as the source's own content.** Mark outside context explicitly (e.g. "not in
X's account"). Before attributing a specific term/date/claim, confirm it is actually there
(search the text).

**5. Coverage ledger (required) — a scoped ingest is complete *for its scope*.** On the source
page, record exactly what was read (chapters, sections, page/line ranges). A read covering its
declared scope is **done, not a standing debt**: mark "read in full (scope: Vol. I, Chs. I–V)",
*not* "partial". Reserve "partial / in progress" for a scope not yet finished. Any in-scope
portion deliberately left unread (apparatus, foreign-language sections, indices, repetitive
matter) must be stated explicitly with the reason. Widening scope later is a **new scoped pass**,
logged as such — not a debt on the old one.

**OCR rule.** If a source arrives as a non-OCR (image-only) PDF, run OCR to produce a readable
`.txt`/`.md` before ingesting. Once verified usable, **replace the original PDF in `raw/` with
the OCR'd file** (same base name, new extension) — delete/overwrite the original. Record the
conversion on the source page (e.g. "Source: `raw/foo.md` — OCR'd from `foo.pdf` on YYYY-MM-DD").

### Ingest sequence (per new source — principles above govern throughout)

1. **Identify** source type and, for any primary text, its **canonical status within the sect/
   tradition being ingested, and whether it differs from the parent** (e.g. canonical for the
   sect but rejected by the parent). Answer explicitly — it drives `canon_scope` and any sect
   canon-divergence section.
2. **Read the scope through and discuss**: read sequentially (principles 2–4); report key
   takeaways, surprising claims, what it adds/challenges — grounded in the reading, not the TOC.
3. **Write or update** the relevant pages (lean batches per span — extend before creating):
   - Source summary page in the appropriate subdir, **with its coverage ledger**.
   - Commentator page, if attributed to a known figure.
   - Text pages for primary texts prominently discussed.
   - **Figure pages** for figures receiving substantial biographical/typological/interpretive
     treatment; add new tradition-specific readings (Philo's Abraham, Origen's Moses) to the
     existing page or create it.
   - **Group pages** for peoples/parties/collectives receiving sustained treatment; extend with
     new tradition-specific portraits/typologies or create.
   - **Location pages** for places whose historical inhabitants or modern geography are
     discussed, or carrying narrative/theological/pilgrimage weight; include settlement history
     and modern mapping.
   - **Tradition and sect pages** for any sub-tradition/denomination/school/movement treated —
     especially canon-divergence and hermeneutical-method sections — plus the parent overview
     if needed. Cross-link to any existing `groups/` page for the same community.
   - **Maintain `canon_scope` on every affected text page** whenever a source establishes how a
     sect/tradition treats a text. Preserve conflicting valuations across communities; do not
     flatten (Contradiction Protocol).
   - Concept pages for theological/hermeneutical terms introduced/developed.
   - Controversy page if the source takes a position on a disputed question.
   - `overview.md` if the source materially shifts the scope.
4. **Update `index.md`** with new/modified pages.
5. **Append to `log.md`**: `## [YYYY-MM-DD] ingest | [Source Title]` — stating the declared
   scope and whether read in full or in progress (e.g. "scope: Vol. I Chs. I–V — read in full"
   or "scope: Ch. VI — partial, read pp. X–Y").
6. **File the raw source out of `raw/` root** (per Step 7 above): `git mv` into the typed
   subfolder, update every reference to the old path. Relocation only — do not alter content.

A single commentary ingest may touch 10–20 pages; a focused scope of a larger work, fewer.
Keep filing lean. Widening to a larger scope of the same work is a later, separately-scoped pass.

---

## Contradiction Protocol

Commentary traditions are full of irreconcilable conflicts — between traditions, within
traditions, and between historical-critical scholarship and confessional readings. Do not
flatten these. When new material contradicts existing content:
- Flag the contradiction explicitly on both affected pages.
- Create or update the relevant `wiki/controversies/` page.
- Do **not** adjudicate which reading is correct unless I explicitly ask for analysis.
- Record each position's tradition context (a Calvinist–Arminian dispute is not the same kind
  as a critical-vs-traditional dating dispute).

---

## Query Workflow

1. Read `index.md` to identify relevant pages.
2. Read those pages.
3. Synthesize an answer citing wiki pages (not raw sources directly).
4. If it required non-trivial synthesis or produced a useful comparison, offer to file it as a
   `wiki/queries/` page.
5. Append to `log.md`: `## [YYYY-MM-DD] query | [Question Summary]`.

---

## Lint Workflow

When I ask for a wiki health check, identify:
- Orphan pages (no inbound links).
- Commentators mentioned in text pages but lacking their own page.
- Figures mentioned repeatedly across pages but lacking a `figures/` page.
- Groups/peoples/tribes/collectives mentioned repeatedly but lacking a `groups/` page.
- Locations whose inhabitants or modern geography are discussed but lacking a `locations/` page.
- Sub-traditions/denominations/sects/movements referenced but lacking a
  `traditions/[parent]/sects/` page; any top-level tradition lacking an overview page.
- Text pages missing `canon_scope`, or whose `canon_scope` omits a community known to canonize/
  dispute/reject the text.
- Concepts used repeatedly without a concept page.
- **One-directional links that should be reciprocal** (per the bilateral cross-linking rule):
  text→concept without the concept→text back-link (or vice versa), and the analogous
  text↔commentator / figure↔group / sect↔group asymmetries. Flag the missing back-link.
- Controversies described inline that should be promoted to a `controversies/` page.
- Claims superseded by newer sources — flag for review, do not silently overwrite.
- **Ledger gaps**: source pages lacking a coverage ledger, or whose ledger marks the *declared
  scope* still "in progress / partial". A scope deliberately narrower than the whole work is
  **not** a defect — flag only unfinished in-scope reads, missing ledgers, or a source ticked
  "done" whose ledger shows its declared scope was never finished.
- Suggest 3–5 sources worth seeking, based on coverage gaps.
- Suggest 3–5 questions worth investigating, based on unresolved tensions.

---

## Naming and Linking Conventions

- File names: `kebab-case.md` (`thomas-aquinas.md`, `fourfold-sense.md`).
- Wiki-internal links: Obsidian format `[[page-name|Display Name]]`.
- Multi-tradition concepts: use the most widely recognized English name as the page title,
  aliasing tradition-specific terms in the body (e.g. `allegorical-reading.md` covers Remez,
  Theoria, Ta'wil).
- **Tradition / sect / group disambiguation**: a *tradition* page is a top-level religion
  (`traditions/[t]/[t].md`); a *sect* page is a sub-tradition within it
  (`traditions/[t]/sects/[s].md`) carrying canon/doctrine/hermeneutics; a *group* page is a
  people/community as social/historical actor. A community that is both (Gnostics, Marcionites,
  Ebionites, Montanists) gets **both** pages, cross-linked.
- **Nested paths are for filing, not link syntax**: reference sect/tradition pages with bare
  slugs (`[[gnosticism|Gnosticism]]`), not the full path. Keep sect/tradition slugs globally
  unique so bare-slug links resolve.
- **`canon_scope` entries are page slugs**: each item in a `canon_scope` bucket (and a sect's
  `canon_distinctives`) is the kebab-case slug of a tradition/sect page (`latter-day-saints`,
  `sethian-gnosticism`, `proto-orthodox-christianity`).
- **Bilateral cross-linking (reciprocity required)**: a wiki link should point both ways. When
  one page links another, the target page must link back wherever the relationship is
  substantive. In particular, **text ↔ concept links are bidirectional**: if a text page names a
  concept it develops/contests, the concept page must list that text under its key text-concept
  connections, and vice versa. The same reciprocity applies to text↔commentator, figure↔group,
  and sect↔group (the already-required `groups/`↔`sects/` cross-link) pairings. A one-directional
  link is a defect to be closed, not left dangling — add the back-link when you create the
  forward one.
- Manuscript sigla, critical apparatus, and original-language terms appear in the body, not in
  file names.
- Original-language terms: transliterate consistently (one system per language, documented in
  `overview.md`).

---

## Transliteration Standards (default — override as needed)

- **Hebrew**: SBL Academic style (no pointing in running text unless exegetically relevant).
- **Greek**: standard academic transliteration; retain Greek script where meaning depends on it.
- **Arabic**: simplified transliteration without diacritics in running text; full diacritics in
  technical pages.
- **Sanskrit/Pali**: IAST for Sanskrit; standard Pali transliteration.

---

## Scope

Current scope of this wiki: [TO BE DEFINED — fill in as we work. Examples: "Synoptic Gospels
and their patristic commentators," "Maimonidean rationalism and its critics," "Quranic tafsir
traditions through the 10th century."] I will update this field as the scope evolves.

---

## Division of Labor

**I handle**: sourcing documents, directing analytical focus, asking questions, reading the
wiki, deciding what matters.

**You handle**: all writing, cross-referencing, maintenance, filing, bookkeeping. Every word in
`wiki/` is yours unless I explicitly edit something myself.
