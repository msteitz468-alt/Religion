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

Two root-level trackers serve different roles and **both must be updated on every ingest**:
- **`outstanding sources.md`** — the user's **working roadmap** (curated wish-list). When a
  listed work is ingested, mark its line item with ✅ and the ingest date. Partial ingests use
  ⚠️. Missing this mark is a bookkeeping defect — same severity as skipping the `log.md` entry.
- **`sources-ingested.md`** — the on-disk acquisition/ingest ledger (what has been filed and
  when). Mark completed scopes there too. If the file is missing, create or extend it rather
  than skip the mark.

---

## Task-Observer Activation (mandatory)

**Main agent / orchestrating session only.** At the start of any task-oriented session
(ingest, lint, query, any tool-using work), the **main agent** invokes the `task-observer`
(`one-skill-to-rule-them-all`) skill **before** reading source content or beginning work. It
captures skill-improvement observations and runs the session-start protocol (weekly-review
check, observation log). When loading any skill, also check `skill-observations/log.md` for
OPEN observations relevant to the work and apply their insight even if the skill file isn't
yet updated.

**Subagents must not run task-observer.** Extraction, integration, and other scoped child
agents skip task-observer and all session-start skill protocols unless the user explicitly
asks that child to improve a skill. Put this negative instruction in every
extractor/integrator prompt — inherited CLAUDE.md activation is not a license for children to
re-enter the meta-skill stack (it burns turns and can stall claims files).

---

## Core Design Principles

- **Commentary is a network of readings, not a tree of doctrines.** Every substantive claim
  sits at the intersection of *text*, *reader*, *method*, and *community*. Links must preserve
  those dimensions — topical similarity alone does not justify a link.
- **Canonicity is a relation, not a property.** A text is canonical *for* a community. Always
  record standing via `canon_scope` (and body **Canon and Reception**); never flatten conflicting
  valuations across communities.
- **Hermeneutics is first-class content.** *How* a text is read belongs alongside *what* it is
  taken to say. Methods (PaRDeS, Quadriga, tafsir, etc.) are tracked on every text, commentator,
  tradition, and sect page — the domain analogue of methods-as-first-class in the social sciences.
- **Never collapse tradition-specific reception into wiki voice.** Jewish, Christian, Islamic,
  critical, and confessional readings stay attributed and separable. Promotion to bare wiki voice
  is an editorial event, not a default (see Voice and Attribution Protocol).
- **Pseudepigraphy and traditional attribution both stay on the page.** Record traditional
  claims and critical reconstructions as positions (Contradiction Protocol); do not silently
  overwrite one with the other.
- **Primary text, apparatus, and modern framing are three evidence classes.** Do not attribute
  a translator's introduction, footnotes, or a scholarly essay as "the Zohar" / "the Qur'an."
  Separate registers and cite each class honestly.
- **File lean, but complete.** Extend a central page before creating a new one; create a page
  only when the subject warrants it; de-link tangential mentions rather than spawning stubs.
  When you do create or update, write **complete content** (required sections filled), not stubs
  to be finished later.
- **The collection has a known bias.** Strong coverage includes Christian systematics and
  patristics, large stretches of Jewish rationalism and mysticism (Guide, Zohar/Pritzker),
  selected Islamic, Buddhist, and Sikh material, and assorted comparative sources. Weaker or
  thinner areas include large parts of Hindu primary epic literature, African and Indigenous
  traditions, and many post-classical Islamic tafsir corpora. Flag bias and gaps on tradition
  overviews and in `overview.md`; write only what the sources support.

---

## Voice and Attribution Protocol — Mandatory

Every claim in the wiki is written in exactly one register. Choosing the wrong register is
this wiki's equivalent of stating theory as fact.

| Register | Use for | Form |
|---|---|---|
| **Wiki voice** | Brute descriptive facts established independently of any single contested reading: print dates, MS counts a source reports, verse references, that a council met, that a page exists in Mantua 1558 | plain declarative prose |
| **Attributed to text** | Claims *of* a primary work as *the work says* | "In Zohar 1:15a (Pritzker I)…", "Qur'an 4:157 states…" |
| **Attributed to commentator / translator / scholar** | Any interpretive, theosophical, or critical claim from a named reader | "Matt reconstructs…", "Green frames…", "Scholem argued…", "Rashi reads…" |
| **Attributed to tradition** | Communal reception, piety, or normative practice | "In Lurianic reception…", "In Ḥaredi piety…", "Among Twelver Shiʿa…" |
| **Position recording** | Live disputes (authorship, dating, canonicity, doctrine) | each position in its strongest form on a `controversies/` page; no adjudication in wiki voice |

**Rules of thumb:**
- A claim that would be *revised if one book or one reading were refuted* is attributed.
- A claim that names a mechanism, meaning, or theosophical structure (not just a citation) is
  attributed.
- Concept pages state core claims in attributed voice even on the concept's own page when they
  derive from a single source or school.
- Promotion from attributed to wiki voice requires documented multi-source or multi-tradition
  convergence — note the basis.
- **Never** present background knowledge, a textbook summary, a familiar term, or an inference
  as the source's own content (see Scope & Fidelity §4).

---

## Directory Structure

```
raw/                        # Immutable source documents (content never modified)
  texts/                    # Primary religious texts
  commentaries/             # Commentary works
  scholarship/              # Academic papers, books, articles
  assets/                   # Images, diagrams, manuscript photos
  misc/                     # Uncategorized / software / non-ingest items

wiki/                       # LLM-maintained knowledge base
  index.md                  # Master index — updated on every ingest
  log.md                    # Append-only ingestion and query log
  overview.md               # High-level synthesis + coverage/gap register

  sources/                  # One summary page per ingested source (preferred home)
  scholarship/              # Legacy / overflow source pages (same schema as sources/)

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
  timelines/                # Chronological hubs (per-tradition, comparative, thematic)
  queries/                  # Filed answers to significant questions

  hubs/                     # High-resolution special sections (see Hubs)
    texts/                  # Graduate-level deep analyses of major works
    commentators/           # Graduate-level intellectual biographies
    schools/                # Sustained systems beyond slim sect stubs
```

**Source pages:** prefer `wiki/sources/[slug].md` for new ingests. Existing pages under
`wiki/scholarship/` remain valid; do not duplicate a source under both paths. Resolve by
grep for author+title before creating.

---

## Page Types and Formats

Each page type's frontmatter schema is below. Fill **all** fields; use `[[unknown]]` or
explicit empty lists where genuinely unclear — never leave mandatory fields blank silently.

### Source Page (`wiki/sources/` or `wiki/scholarship/`)
One page per ingested source. **Required for every ingest.**

```yaml
---
title: [Source Title]
author: []
year: [publication year]
source_type: [primary-text | primary-text-edition | commentary | scholarship |
              polemic | reference | textbook | mixed]
tradition_coverage: []         # tradition/sect slugs
texts_covered: []              # text page slugs
hermeneutical_approach: []     # e.g. sod, peshat, historical-critical, quadriga
language_of_source: [English / …]
reliability_notes: []          # conversion issues, missing folios, partisan character, …
pages_created: [count]
pages_updated: [count]
ingested: [YYYY-MM-DD]
tags: [source]
---
```

Required body sections:
- **What the source is** (genre, edition, translator/annotator)
- **Scope plan** (ordered bounded scopes; for large works, the Section Plan table)
- **Coverage ledger** (what was read, line/page ranges, excluded apparatus with reason)
- **Hermeneutical frame** (how *this* work reads its material; separate body vs apparatus vs intro)
- **Pages generated / extended**
- **Volume / work synthesis** (3–5 paragraphs after a complete scope or multi-scope plan:
  overall argument, what it adds to the wiki, tensions with already-ingested sources;
  **do not back-project later volumes**)
- **Key links**

`source_type: polemic` triggers artifact-mode discipline: heavy `reliability_notes`; main
thread owns all live wiki writes; extracts split into FACTS / THESES / QUOTES.

### Text Page (`wiki/texts/`)
Primary texts, books, pericopes, suras, suttas, etc.

```yaml
---
title: [Text Name]
tradition: [Judaism / Christianity / Islam / Buddhism / Hinduism / etc.]
canon_status: [headline only — canonical / deuterocanonical / contested / sectarian / non-canonical]
canon_scope:                 # which traditions/sects treat this text HOW (entries are page slugs)
  canonical_for: []
  deuterocanonical_for: []
  authoritative_for: []
  disputed_by: []
  rejected_by: []
language_original: [Hebrew / Greek / Arabic / Sanskrit / Pali / etc.]
date_range: [approx composition date or range]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [text, tradition-name, genre]
---
```

**Required body sections:**
- **Textual Overview** (what it is; structure)
- **Major Themes / Narrative Summary**
- **Textual and Manuscript Tradition** (how the text was transmitted; print history where relevant)
- **Hermeneutical Frameworks** (how communities and this wiki's sources read it — see Hermeneutical Tracking)
- **Canon and Reception** (required whenever non-trivial; recommended always for major texts)
- **Scholarship and Historiography** (dating, authorship, major scholarly positions — *as positions*)
- **Key interpretive cruxes**
- **Links** to commentator, concept, controversy pages

**`canon_scope` is required.** Canonicity is a *relation* between text and community, not a
property of the text. Each bucket entry is the slug of a tradition (`christianity`) or sect
(`sethian-gnosticism`). The same text routinely appears in several buckets at once.
`canon_status` is only a coarse one-word headline derived from `canon_scope`. Examples:
- **Gospel of Thomas** — `canonical_for: [thomasine-christianity]`; `rejected_by:
  [proto-orthodox-christianity, catholicism, eastern-orthodoxy, protestantism]`; `disputed_by:
  [coptic-christianity]`.
- **Book of Mormon** — `canonical_for: [latter-day-saints]`; `rejected_by: [catholicism,
  eastern-orthodoxy, protestantism, …]`. Narrative continuity claims are **reception facts in
  the body**, not buckets.

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
hermeneutical_method: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [commentator, tradition-name]
---
```

Body: biographical context; **hermeneutical method** (literal/allegorical/moral/anagogical;
peshat/derash/remez/sod; etc.); major works; characteristic positions (attributed); known
controversies; influence on later tradition; **Sources Ingested**.

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
textual_sources: []
dates: [historical / traditional / floruit / "legendary" / "disputed"]
roles: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [figure, tradition-name, role-type]
---
```

Body sections:
- **Biographical Overview**: attested biographical data from primary sources. Distinguish
  textual claims from historical-critical reconstruction; flag disputes rather than presenting
  one tradition as fact.
- **Primary Source Appearances**: which texts feature the figure; key pericopes with one-line
  summaries.
- **Tradition-Specific Reception** (core): how each tradition interprets/develops/contests the
  figure, recorded separately. Per tradition: primary authoritative source, dominant
  interpretive move, intra-tradition disputes.
- **Theological and Narrative Significance**
- **Historicity and Interpretive Controversies** — positions without adjudication
- **Influence on Commentary Traditions**

### Group Page (`wiki/groups/`)
Peoples, tribes, nations, ethnic groups, religious parties, social classes, and collective
identities acting as actors/foils.

**Scope rule**: create when the collective is (a) a corporate actor in one+ primary texts, (b)
subject of substantial commentary/typology/identity construction, and (c) not better handled
as a concept. Overlapping cases ("Israel" as people and concept) may warrant both pages,
cross-linked.

```yaml
---
title: [Group Name]
also_known_as: []
tradition: [Judaism / Christianity / Islam / cross-tradition / etc.]
textual_sources: []
periods_active: []
roles_significance: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [group, tradition-name, category-or-period]
---
```

Body sections: **Identity and Nomenclature** · **Primary Textual Appearances** ·
**Tradition-Specific Portraits** · **Historical and Archaeological Context** ·
**Theological and Narrative Significance** · **Influence on Later Traditions and Controversies**
(flag sensitive modern deployments and link controversy pages).

### Location Page (`wiki/locations/`)
Places carrying sustained narrative, theological, or pilgrimage significance. **Must** address
historical inhabitants and modern geographic identification.

**Scope rule**: create when a place is (a) named with narrative/symbolic weight, (b) setting of
significant events/figures/cult, and (c) object of later interpretive/devotional tradition.
Minor/incidental place names need no page.

```yaml
---
title: [Location Name]
also_known_as: []
tradition: [Judaism / Christianity / Islam / cross-tradition / etc.]
textual_sources: []
periods_inhabited: []
modern_geography: []
associated_peoples: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [location, tradition-name, site-type]
---
```

Body sections: **Geographical and Historical Overview** · **Primary Textual Appearances and
Inhabitants** · **Archaeological and Extra-Biblical Data** · **Modern Identification and
Geography** · **Theological and Symbolic Significance** · **Key Events, Figures, and Controversies**.

### Tradition Page (`wiki/traditions/[tradition]/[tradition].md`)
A top-level religion. One overview page per tradition; parent node for its `sects/` pages.

```yaml
---
title: [Tradition Name]
also_known_as: []
type: tradition
date_range: []
canon_core: []
hermeneutical_frameworks: []
major_sects: []
collection_coverage: [strong / moderate / weak / absent / unaudited]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [tradition, tradition-name]
---
```

Body: definition/self-understanding; historical origin and development; shared canon and
canonical authority; native hermeneutical frameworks; **map of major sects**; central figures,
groups, concepts, controversies; **Collection Coverage Note** (bias and gaps).

**Non-theistic / multi-canon traditions**: keep `canon_core` minimal (only what is genuinely
shared); carry divergent canons at the sect level. Record the tradition's own account of
ultimate reality rather than forcing a deity slot.

### Sect / Denomination Page (`wiki/traditions/[tradition]/sects/[sect].md`)
A sub-tradition within a parent. First-class page with its own canon, hermeneutics, and
relationship to orthodoxy.

**Scope rule**: create when (a) distinct community/school within a parent, (b) canon/doctrine/
hermeneutic diverging from parent or siblings, and (c) generates sustained commentary/identity/
polemic.

Not a duplicate of a `groups/` page: group = social/historical actor; sect = system (canon,
doctrine, hermeneutics). Where both apply, keep both and cross-link.

```yaml
---
title: [Sect / Denomination Name]
also_known_as: []
parent_tradition: [slug]
type: [denomination / sect / movement / school / lineage / normative stream]
dates: []
status: [extant / extinct / revived]
relationship_to_orthodoxy: []
canon_distinctives: []
key_doctrinal_distinctives: []
hermeneutical_method: []
key_figures: []
key_texts: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [sect, parent-tradition-name]
---
```

Body sections: **Identity and Origins** · **Relationship to the Parent Tradition** ·
**Canon and Scripture (Canon Divergence)** (required) · **Doctrinal Distinctives** ·
**Hermeneutical Method** (mandatory) · **Relationship to Orthodoxy and Other Sects** (no
adjudication) · **Historical Development, Subdivisions, and Influence** · **Sources Ingested**.

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

Body: definition; origin; tradition-specific usage (attributed); key text-concept connections
(bilateral); cross-links to controversies where contested.

### Comparison Page (`wiki/comparisons/`)
Generated from cross-tradition/cross-commentator queries; filed for permanence.

```yaml
---
title: [Comparison Description]
entities_compared: []
generated_from_query: [brief description]
date: [YYYY-MM-DD]
tags: [comparison, ..., hub]
---
```

**Thematic comparison hubs** gather and link existing pages by recurring structure then
tradition-by-tradition — they do not adjudicate. Wire into `index.md` `## Comparisons` and
add reciprocal back-links from each theme's central concept page. Theme-organized hubs live in
`wiki/comparisons/`; time-organized hubs in `wiki/timelines/`.

### Controversy Page (`wiki/controversies/`)
Interpretive disputes cutting across commentators or traditions.

```yaml
---
title: [Issue in Dispute]
text_locus: [verse, passage, or concept at stake]
positions: []
traditions_involved: []
dispute_type: [empirical / interpretive / source-reliability / doctrinal /
               authorship / dating / canonicity / other]
resolution_status: [open / historically resolved / tradition-specific]
last_updated: [YYYY-MM-DD]
tags: [controversy]
---
```

### Timeline Page (`wiki/timelines/`)
Chronological navigation hubs linking existing pages along a time axis. Three sub-types:
- **Per-tradition timeline** (`[tradition]-timeline.md`)
- **Master comparative timeline** (`comparative-timeline.md`) — era × family matrix, then
  per-era detail
- **Thematic chronological hub** (e.g. `new-religious-movements-timeline.md`)

```yaml
---
title: [Timeline of X]
tradition: [name]            # OR type: timeline-hub
date_range: [span]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [timeline, <tradition>, hub]
---
```

Body: era-banded sections; within each era, *Figures / Texts–Concepts / Councils–Controversies*
(adapt headers). A timeline **links existing pages; it does not introduce new content**.

**Conventions (load-bearing):**
- Bracketed plain names (`[William Miller]`, no `[[ ]]`) mark referents lacking a page — not
  red links to "fix."
- No backslash-escaped pipes in wikilinks inside tables (`[[a\|b]]`); use `[[a|b]]`.
- Verify a slug exists before linking (grep / lint) — never from memory.

**Wiring:** link from tradition overview; add to `index.md` `## Timelines`; upgrade comparative
matrix cells when a per-tradition timeline is built; lint clean before done.

---

## Link Types — Mandatory Distinctions

Prefer these labels in frontmatter relation lists and in "Relations" body blocks. Prose may
paraphrase, but do not conflate categories.

| Label | Meaning |
|---|---|
| `comments_on: [[text]]` | commentator or commentary addresses this text |
| `commented_by: [[X]]` | inverse of comments_on |
| `depends_on: [[concept]]` | load-bearing doctrine or category |
| `developed_from: [[X]]` | intellectual or doctrinal descent with modification |
| `reacts_against: [[X]]` | defined itself in opposition (e.g. Kabbalah vs Maimonidean rationalism) |
| `typologically_reads: [[figure/event]]` | e.g. Noah as Yesod; Exodus as soul's ascent |
| `parallel_in: [[tradition]]` | cross-tradition analogy without equating |
| `contradicts_position_on: [[controversy]]` | explicit tension; do not flatten |
| `canonized_by: [[sect]]` / `rejected_by: [[sect]]` | prefer `canon_scope` buckets; use labels in prose/relations |
| `preceded_by: [[X]]` / `followed_by: [[X]]` | temporal order only; **not** causation |
| `influenced: [[X]]` / `influenced_by: [[X]]` | historical influence claim (always attributed) |
| `part_of: [[X]]` / `contains: [[X]]` | composition (corpus, cycle, anthology) |

**Load-bearing distinctions:**
- Temporal succession ≠ causal/influence claim.
- `parallel_in` ≠ identity of doctrine across traditions.
- A study or reading *supporting* a thesis is a recorded relation, not a wiki-voice verdict.

**Bilateral cross-linking (reciprocity required):** when one page links another substantively,
the target links back. Especially: text ↔ concept, text ↔ commentator, figure ↔ group,
sect ↔ group. A one-directional link is a defect.

---

## Hermeneutical Tracking — Core Requirement

Track *how* a text is read, not just *what* it says. Every text, commentator, tradition, and
sect page must record the interpretive framework(s) in use; a sect page must record the rules
distinguishing it from its parent. Group and location pages should note tradition-specific
interpretive moves, typological uses, and polemical deployments.

Standard frameworks to identify and tag:
- **Jewish**: Peshat, Derash, Remez, Sod — PaRDeS
- **Christian patristic/medieval**: Literal, Allegorical, Tropological, Anagogical — the Quadriga
- **Islamic**: Zahir / Batin; tafsir bi'l-ma'thur vs. bi'l-ra'y
- **Buddhist**: Neyartha vs. Nitartha; commentarial lineage
- **Daoist**: commentary-as-transformation; xuanxue vs. longevity-cultivation readings
- **Modern critical**: Historical-critical, form, redaction, canonical criticism, reader-response

When ingesting a commentary, identify and explicitly record its framework(s). Flag
cross-tradition comparisons of the same method (allegory in Origen vs. Philo vs. Ibn Arabi)
for comparison-page generation.

---

## Historiography and Reception Protocol

Every **major text page** and every **major tradition/sect page** requires attention to how
knowledge of the subject was produced:

| Concern | Cover |
|---|---|
| **Evidence quality** | What manuscripts, editions, archaeological or archival bases the claims rest on |
| **Scholarly debates** | Dating, authorship, composition history — as positions |
| **Methodological approaches** | Confessional, historical-critical, literary, phenomenological, etc. |
| **Reception history** | How communities used, ranked, or rejected the text/school |
| **Recent revisionism** | Significant changes in the standard account (last ~30 years) where sources support them |
| **Collection coverage** | What this wiki has ingested well; where gaps remain |

For critical editions, separate **body text**, **apparatus/notes**, and **modern introductions**
as evidence classes. Absence of a modern critical consensus is not absence of traditional
reception — record both.

---

## Ingest Workflow

Two halves of one workflow: the **Deployed Subagent Strategy** (default — *throughput*: how a
scope is read in parallel) and **Scope & Fidelity** (the standard of *quality*). Subagents are
how a scope gets read, never a lower standard of fidelity.

**Non-negotiable principle: the main thread owns structure; subagents own bulk extraction.**
Subagents never decide taxonomy, page naming, `canon_scope` buckets, sect-vs-group splits, or
cross-links — they extract faithfully within boundaries the main thread already drew.

### Progress Checklist (mandatory — user-visible)

Long tool loops look **frozen** from the user's side even when work is progressing. Silent
progress is a defect.

1. **Post the checklist at session start** — before spawning extractors. Use the session todo
   list **and** state the same plan in chat.
2. **Minimum ingest checklist** (adapt labels; keep the phases):
   - [ ] Source located · word-count / integrity intake · cache slices cut
   - [ ] Scaffold (source page + key link targets on disk)
   - [ ] Extractors spawned — **N agents**, cache dir, expected digest filenames
   - [ ] Digests inventory — per-range: pending / running / done / missing→recover
   - [ ] Integration — pages created/updated (tick in batches)
   - [ ] Validate (`python Scripts/lint_wiki.py`; prove 0 **new** broken links vs baseline)
   - [ ] Bookkeeping (index, log, outstanding sources ✅, sources-ingested, file raw out of root)
   - [ ] Cache cleanup (this ingest's session cache only)
3. **Update as phases complete.** After spawn, show per-range rows; flip to done when the
   digest file is non-empty on disk. During integration, tick major page batches.
4. **No multi-minute silence.** If extractors or integration will run more than ~1–2 minutes,
   interleave short user-visible status with tool work.
5. **On "are you frozen?"**: first reply is current checklist + digests inventory, not a
   re-plan without status.

### Step 0 — Pre-flight: claim-the-ingest and prior footprint

Before scaffolding, grep the wiki for the **author surname and distinctive title words** and
for any page already citing the source. Naming conventions vary; a source page may exist under
a non-obvious slug. Surveying topic pages is not a substitute.

This check applies to **explicit re-ingest requests too**.

| Finding | Action |
|---|---|
| Source page exists; ledger shows declared scope **unfinished** | Resume that ledger; do not open a second source page |
| Source page exists; ledger complete; audit finds **wiring-only** defects (links, slugs, schema, missing reciprocal links, missing section headings with content present elsewhere) | Repair wiring; **do not** re-extract by default |
| Source page exists; ledger complete **or absent**; audit finds **fidelity / content defects** — ungrounded claims, TOC-reconstruction, wrong loci, single-source theosophy in bare wiki voice, missing coverage ledger, pre–Scope-and-Fidelity textbook paraphrase, missing material that was never read | **Re-extract the affected scope** under current standards; upgrade the existing source page rather than creating a duplicate slug |
| No prior footprint | Proceed to intake + scaffold |

**Fidelity gaps warrant re-reading.** Wiring defects do not. Aging ingests often fail at both
layers; report the split explicitly, then re-read only where fidelity fails.

**Resume-incomplete bookkeeping:** if a source page has an `ingested:` date but no matching
`log.md` line, or the file is still in `raw/` root, or trackers are unmarked — finish
bookkeeping before or alongside any re-extract.

Write the source-page stub early so a sibling session's check can see it.

### Step 0b — Intake integrity (word-count / conversion check)

Run `wc -w` on the raw text and compare against expected length (~250–350 words/page × page
count). Note: `wc` prints *lines words chars* — use the **words** column. Converted ebooks
fail silently (epub→txt can capture only Part One while the TOC still lists every chapter).

If the ratio is badly off:
1. Grep for each major TOC heading **in the body** (not only the TOC block)
2. For critical editions / Zohar / Talmudic pagination: sample folio or verse headers for gaps
3. Record incompleteness on the source page in `reliability_notes` **before** extraction

**OCR ladder** (image-only PDFs / bad text layer): produce readable `.txt`/`.md` before
ingesting; prefer project-local temp (not small tmpfs `/tmp`); replace the original PDF in
`raw/` with the OCR'd file once verified; record conversion on the source page.

### Step 1 — Scaffold first, on the main thread

Read enough (TOC, intro, conclusion, targeted sampling) to do the judgment work:
- Identify source type and, for any primary text, **canonical status per sect/tradition** and
  whether it differs from the parent (drives `canon_scope` + sect canon-divergence).
- Write the **source page** with **scope plan / Section Plan** and **coverage ledger** skeleton.
- Create or name **key linkable pages** so subagents inherit names.
- Decide naming conventions, page taxonomy, and hermeneutical framing.
- Decide whether a **hub page** is warranted (see Hubs); if yes, pre-establish its name and
  build it in the same session once criteria are met.
- **Grep-verify coined terms** before scaffolding concept pages — if the term is absent from
  the source, do not invent the page.
- **Duplicate-page pre-scan:** resolve slugs **folder-agnostically** (`find wiki -name
  "<slug>.md"` or whole-vault grep). Obsidian resolves by bare filename; a per-folder check
  manufactures collisions. Grep name-order variants and synonymous titles.

Do not spawn any agent until linkable page names and canon/taxonomy decisions exist **on disk**.

### Step 2 — Split the scope by disjoint line-ranges

Divide the in-scope raw text into N contiguous, non-overlapping chunks by line number.
- **Size N to the material.** Base on *body* length × density (exclude front matter, apparatus,
  indices, untranslated sections): ~one agent per 2,000–3,500 body lines; floor 2–3; up to ~10
  for very large works. **Do not default to 6.**
- **Weight by density/importance**, not even boundaries. Align to natural section boundaries
  only where it doesn't fight weighting.
- Ranges must be **disjoint** — every line in exactly one chunk.
- **Locate boundaries in the body, never in the TOC.** First grep hit is almost always the
  TOC; filter to body and confirm **in-text markers** (incipit, folio, chapter openers).
- **Pre-cut per-range cache files** into session-local storage immediately after locating the
  source (before or during scaffold). `raw/` is user-mutable mid-session.
- **Include paratext that carries origin facts** (acknowledgments with commission notes,
  colophons) in a body range or main-thread ownership — do not drop them outside all slices.
- **Sensitive-content / filter-prone triage (mandatory):** flag ranges dense in
  atrocity/persecution documentation **or** charged discourse (heresy polemic, race-science
  quoted to refute, graphic purity/sexual material in mystical texts). These are first-class
  wiki content and are **never toned down or omitted**. Mechanical risk: output filters can
  block a subagent's entire extraction. Prefer sparse-verbatim + line-pointers for
  filter-prone ranges; route maximally graphic material to the main thread; size every range
  so single-range main-thread recovery stays comfortable. A content-filter block is a routing
  signal, never a reason to soften content.

### Step 3 — Spawn extractors (parallel + background)

Use the Agent tool with background execution, one agent per chunk. Each prompt must contain:
- its **exclusive line-range** (read only that range / cache file)
- **schema, naming conventions, Voice and Attribution Protocol, Hermeneutical Tracking**
- **established page names** as ground truth already verified by the main thread
- **exclusive ownership** of claim/digest titles (distinct namespace so no two agents write the
  same file)
- **faithfulness mandate**: extract only what is in range, with **verbatim-anchored grounding
  quotes and line/page/folio loci**; no outside knowledge; no reading beyond range
- instruction that **subagents do not run task-observer**
- when creating schema'd pages is allowed at all (prefer digests — see two-stage below):
  **complete copy-pasteable YAML** and exact required body headings

**Standing subagent instructions** (include in every extraction prompt):
- **Flag, don't force, entity mismatches.** Near-match to a target page but different entity →
  Miscellaneous with mismatch flag.
- **Flag internal duplication** (ebook conversion artifacts); extract once.
- **Report actual coverage** in the completion summary (exact lines read; if stopped short, say so).
- **Treat chunk briefs as expectations, not facts** ("likely covers X — verify").
- Prefer writing **extraction digests / claims files**, not live wiki pages, unless the main
  thread explicitly assigned exclusive page ownership.

**Deployment:** launch in parallel by default; fall back to staggered batches of 2–3 if rate
limits appear. Collect task_ids; monitor to completion.

**Recovery — key off "this chunk didn't come back correctly," not off a single cause.**
Main thread recovers *that range alone* from the cache slice, labels "Main-thread recovery
(<cause>)", lets others continue. Observed modes: rate limit (429); content-filter block;
silent hang (transcript mtime stalled); agent reports range lacks assigned material (re-cut;
never accept adjacent composition as substitute; never fill with general knowledge).

**Never soften the faithfulness mandate** to make an agent more "useful." "Not present in this
range" is both accuracy control and the channel that surfaces bad range assignments.

### Step 4 — Review and integrate (main thread)

Dedupe overlapping claims; reconcile naming; form cross-links (subagents only linked Step-1
names); fill coverage ledger; record contradictions (Contradiction Protocol); set/extend
`canon_scope`; cross-link new sect/group pairs; remove agent artifacts (grep first).
**File lean** (extend before create; no stubs).

**Before editing any existing page, open it with the Read tool** (not only Bash `cat`) on the
lines you'll change — harness Edit safety tracks Read-tool calls.

**When concurrent sessions may touch the same pages:** integrate with **Edit-append, never a
full Write** on shared pages.

#### Two-stage variant for mature / extension-heavy clusters (default for reingests)

When the wiki already has dense coverage of the source's subject (e.g. reingest of Zohar I
into an existing Kabbalah cluster), most claims are UPDATEs to shared pages:

- **Stage 1 — extraction, partitioned by disjoint line-range.** Agents write **digests /
  claims files only** (no live wiki edits). Every claim: short quote + line/folio locus.
- **Stage 2 — integration, partitioned by exclusive wiki-page ownership.** Each integrator
  owns a disjoint set of page slugs, greps *all* Stage-1 digests for its slugs, and is
  restricted to **Edit (no full rewrites)** to fold claims in. Main thread keeps taxonomy,
  new-page creation, filter-prone pages, and `canon_scope` decisions.

### Step 4b — Section / scope commit cycle (large works)

For multi-scope works, process **one scope at a time** (complete the cycle before the next;
do not read ahead into filing for N+1 while N is unfinished):

| Step | Action |
|---|---|
| 2a | Read the scope in full (Scope & Fidelity) |
| 2b | **Identify all pages affected** — list new pages (filenames) and existing pages (what changes) *before writing* |
| 2c | Write all affected pages — complete content, all frontmatter, cross-links, required sections |
| 2d | **Commit to disk** — write/edit every file; confirm paths exist; only then proceed |
| 2e | Append section/scope log entry + update ledger on source page |
| 2f | Clear and advance only after disk commit |

After the full plan: **Volume Synthesis Note** on the source page (3–5 paragraphs); final
`ingest-complete` log line when the work's plan is exhausted.

### Step 5 — Lint and validate

1. Capture a **baseline** broken-link / lint total (`python Scripts/lint_wiki.py` or project
   equivalent) before or after isolating the change set if needed.
2. Run lint; resolve red links, orphans, missing pages for repeatedly mentioned entities,
   missing `canon_scope`, missing reciprocal links, ledger gaps.
3. Prove **0 new broken links** vs baseline (compare totals; do not trust a truncated detail
   list).
4. Repair wikilinks with the Edit tool (or careful exact replacements), not blind `sed` on
   piped wikilinks / YAML.
5. Re-run until clean for the change set.

### Step 6 — Bookkeeping

1. Update `index.md`
2. Tick **`outstanding sources.md`** and **`sources-ingested.md`**
3. Append `log.md`: `## [YYYY-MM-DD] ingest | [Source Title]` — declared scope; read in full or
   in progress; pages created/updated counts
4. For multi-scope works, checkpoint after **each** scope and continue autonomously

### Step 7 — File the raw source out of `raw/` root

Once fully ingested for its declared scope, move (`git mv` if tracked; plain `mv` if not —
many raw sources are untracked) into `raw/texts/`, `raw/commentaries/`, `raw/scholarship/`, or
`raw/misc/`. **Relocation only — never alter content.** Update every reference to the old path
(source page, ledger, log). File by the **exact path the cache slices were cut from**.

**Do not run `git commit` or `git push`** unless the user explicitly asks — the user handles
git operations by default.

### Scope & Fidelity (the standard of quality)

Governing principle: **fidelity within a declared scope** — not exhaustiveness. Everything the
wiki attributes to a source must have actually been read in it; not every source must be read
cover to cover. You read what we scope, and you read it honestly.

**1. Scope the ingest first.**
- **Small, bounded sources** → scope = the whole thing; read in full.
- **Large reference / multi-volume / survey works** → scope = a named portion. Do not silently
  expand beyond it.

**Scope it yourself and progress autonomously.** Do not ask which scope is next for routine
partitioning. Record the scope plan on the source page; work scopes in order; checkpoint after
each. Surface a choice only when partitioning is genuinely ambiguous, a scope is too thin, or
judgment is needed.

**2. Read the scope in full, in order — no TOC-triage.** Sequential read; search tools may
supplement but never substitute. TOC-sampling is a named failure mode, not a shortcut.

**3. Read in large spans; file in lean batches.** Brief verbatim-anchored notes during the
read; file at natural boundaries. **File lean**: extend before create; no stubs; complete
required sections when you file.

**4. Faithfulness — record only what the source says.** Never present background knowledge, a
textbook summary, a familiar term, or an inference as the source's own content. Mark outside
context explicitly. Confirm terms/dates/claims by search before attributing.

**5. Coverage ledger (required).** Record exactly what was read. A read covering its declared
scope is **done**, not a standing debt. Reserve "partial / in progress" for unfinished
in-scope reads. State deliberately unread apparatus with reason. Widening scope later is a
**new scoped pass**.

### Ingest sequence (checklist form — principles above govern)

1. Identify source type + canon status per community.
2. Intake integrity check; claim-the-ingest / re-ingest decision.
3. Scaffold source page + linkable names; post progress checklist.
4. Read scope(s) via deployed extractors + main-thread integration (or direct read for small works).
5. Report key takeaways grounded in the reading (not the TOC).
6. Write/update pages (lean; complete; attributed voice).
7. Lint to 0 new broken links.
8. Bookkeeping + file raw out of root.

---

## Contradiction Protocol

When new material contradicts existing content:
1. Flag explicitly on both affected pages (e.g. `[CONTRADICTION]` or a clear prose flag).
2. Create or update the relevant `wiki/controversies/` page.
3. Classify with `dispute_type` (empirical / interpretive / source-reliability / doctrinal /
   authorship / dating / canonicity / other).
4. **Do not** adjudicate which reading is correct unless explicitly asked.
5. Record each position's tradition context (a Calvinist–Arminian dispute is not the same kind
   as a critical-vs-traditional dating dispute).
6. Never silently overwrite — preserve both claims with attribution and date.

---

## Query Workflow

1. Read `index.md` to identify relevant pages.
2. Read those pages.
3. Synthesize an answer citing wiki pages (not raw sources directly), respecting Voice and
   Attribution.
4. If non-trivial synthesis or a useful comparison, offer to file as `wiki/queries/`.
5. Append to `log.md`: `## [YYYY-MM-DD] query | [Question Summary]`.

---

## Lint Workflow

When asked for a wiki health check, identify:
- Orphan pages (no inbound links).
- Commentators / figures / groups / locations / sects mentioned repeatedly without pages.
- Text pages missing `canon_scope`, or omitting a community known to treat the text.
- Concepts used repeatedly without a concept page.
- One-directional links that should be reciprocal.
- Controversies described inline that should be promoted.
- Claims superseded by newer sources — flag for review, do not silently overwrite.
- **Ledger gaps**: missing coverage ledgers; unfinished *declared* scopes; sources ticked done
  whose ledgers show the scope was never finished. A deliberately narrower scope is not a defect.
- **Voice violations**: single-source interpretive claims in bare wiki voice.
- **Hub candidates** warranted by criteria but never built.
- Suggest 3–5 sources worth seeking; 3–5 questions worth investigating.

**Validation bar after each ingest:** 0 **new** broken links vs pre-ingest baseline; required
frontmatter fields present on new pages; coverage ledger updated for the declared scope.

---

## Hubs — High-Detail Sections

Slim pages in `texts/`, `commentators/`, and `traditions/.../sects/` remain the default. When
selection criteria are met, build a **hub page in the same session** — do not defer warranted
hubs as optional polish. If genuine scope limits force a split, flag and ask rather than
silently skip.

### Texts Hub (`wiki/hubs/texts/`)
Graduate-level deep analysis of a major work (structure, strata, hermeneutics, reception,
scholarship). Criteria: work is multi-volume or multi-strata; multiple sources ingested on it;
or a single critical edition that reorganizes the wiki's understanding (e.g. full Pritzker
Zohar). The hub **links and deepens**; it does not replace the text page.

### Commentators Hub (`wiki/hubs/commentators/`)
Graduate-level intellectual biography (formation, method, works, controversies, afterlife).
Criteria: figure is central to a major school; multiple sources ingested; or the slim
commentator page cannot hold the analytic load without becoming unreadable.

### Schools Hub (`wiki/hubs/schools/`)
Sustained systems (Lurianic Kabbalah, Thomism, Ashʿarism, Madhyamaka) beyond a slim sect stub.
Criteria: multi-source coverage; distinct canon + hermeneutic + historical phases that exceed
sect-page length discipline.

---

## Naming and Linking Conventions

- File names: `kebab-case.md` (`thomas-aquinas.md`, `fourfold-sense.md`).
- Wiki-internal links: Obsidian format `[[page-name|Display Name]]`.
- Multi-tradition concepts: most widely recognized English name as title; alias
  tradition-specific terms in the body.
- **Tradition / sect / group disambiguation**: tradition = top-level religion; sect =
  sub-tradition as system; group = social/historical actor. Both pages when both apply,
  cross-linked.
- **Nested paths are for filing, not link syntax**: bare slugs (`[[gnosticism|Gnosticism]]`).
  Keep sect/tradition slugs globally unique.
- **`canon_scope` entries are page slugs.**
- Manuscript sigla and original-language terms appear in the body, not in file names.
- Original-language terms: transliterate consistently (see below; document system in
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

Current scope of this wiki (as of 2026-07-18; update as coverage shifts):

**Strong / multi-source clusters:** Christian systematics and patristics (Aquinas, Augustine
streams, Barth, Pelikan, Zachhuber, etc.); Jewish rationalism and philosophy of religion
(Maimonides Guide, Heschel); Jewish mysticism via Pritzker Zohar (Vols I–XII ingested under
earlier standards — fidelity reingests proceed volume-by-volume under this file); selected
NT/OT evangelical commentary; Dead Sea Scrolls; large Buddhist (Lamrim, Bardo) and Sikh
(SGGS, McLeod/Singh) blocks; assorted comparative and modern philosophy-of-religion sources.

**Thin or gap areas:** full Hindu epic primary literature; many Islamic tafsir corpora beyond
partial hadith/philosophy; African, Indigenous, and East Asian popular religion beyond selected
works; lived modern denominational practice outside textual/systematic sources.

Flag gaps on tradition overviews and in `overview.md`. Prefer filling from ingested sources
over background synthesis.

---

## Division of Labor

**I handle**: sourcing documents, directing analytical focus, asking questions, reading the
wiki, deciding what matters, git commit/push unless I explicitly ask you to.

**You handle**: all writing, cross-referencing, maintenance, filing, bookkeeping, progress
visibility, and fidelity to declared scopes. Every word in `wiki/` is yours unless I
explicitly edit something myself.
