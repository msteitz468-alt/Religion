# CLAUDE.md — Religious Commentary Wiki

## Overview

This is a persistent, LLM-maintained wiki for the study of religious texts and their
commentary traditions. The wiki covers primary texts, commentators, interpretive schools,
theological concepts, and the historical and philological context surrounding them.

You (the LLM) write and maintain all wiki files. I source documents and direct analysis.
You do all filing, cross-referencing, synthesis, and bookkeeping.

The working environment is Obsidian. All files are markdown. The raw source collection
lives in `raw/`. The wiki lives in `wiki/`. Never modify files in `raw/`.

---

## Task-Observer Activation (mandatory)

At the start of any task-oriented session (ingest, lint, query, or any tool-using work),
invoke the `task-observer` (`one-skill-to-rule-them-all`) skill **before** reading source
content or beginning work. It captures skill-improvement observations and runs the
session-start protocol (weekly-review check, observation log). When loading any skill, also
check `skill-observations/log.md` for OPEN observations relevant to the work and apply their
insight even if the skill file isn't yet updated.

---

## Directory Structure

```
raw/                        # Immutable source documents
  texts/                    # Primary religious texts (canonical, apocryphal, deuterocanonical)
  commentaries/             # Commentary works (classical, medieval, modern)
  scholarship/              # Academic papers, books, articles
  assets/                   # Downloaded images, diagrams, manuscript photos

wiki/                       # LLM-maintained knowledge base
  index.md                  # Master index — updated on every ingest
  log.md                    # Append-only ingestion and query log
  overview.md               # High-level synthesis of the wiki's current scope

  texts/                    # One page per primary text or pericope
  commentators/             # One page per named commentator or school
  figures/                  # One page per major biblical or religious figure
  groups/                   # Peoples, tribes, nations, ethnic groups, religious parties, and cultural collectives mentioned across texts
  locations/                # Geographical places, cities, regions, and sites with historical inhabitants and modern geographic identification
  concepts/                 # Theological, philosophical, and hermeneutical concepts
  traditions/               # Two-level hierarchy of religions and their sub-traditions/sects:
    [tradition]/            #   one subdirectory per top-level tradition (christianity/, judaism/, buddhism/, …)
      [tradition].md        #   the Tradition overview page (e.g. christianity.md, judaism.md)
      sects/                #   Sect / denomination / sub-tradition pages, nested under the parent tradition
        [sect].md           #   e.g. gnosticism.md, marcionism.md, rabbinic-judaism.md, theravada.md
  comparisons/              # Cross-text, cross-tradition comparison pages
  controversies/            # Disputed interpretations and unresolved tensions
  timelines/                # Chronological pages (canonization, historical context, etc.)
  queries/                  # Filed answers to significant questions I've asked
```

---

## Page Types and Formats

### Text Page (`wiki/texts/`)
For primary texts, books, pericopes, suras, suttas, etc.

```yaml
---
title: [Text Name]
tradition: [Judaism / Christianity / Islam / Buddhism / Hinduism / etc.]
canon_status: [headline summary only — canonical / deuterocanonical / contested / sectarian / non-canonical]
canon_scope:                 # the structural canon dimension — WHICH traditions/sects treat this text HOW.
  canonical_for: []          #   full scriptural canon (entries are tradition or sect page slugs)
  deuterocanonical_for: []   #   secondary / graded / disputed-but-included canon
  authoritative_for: []      #   esteemed and cited (liturgy, doctrine, halacha) but NOT scripture
  disputed_by: []            #   canonicity actively contested or unsettled
  rejected_by: []            #   explicitly excluded, non-scriptural, or condemned
language_original: [Hebrew / Greek / Arabic / Sanskrit / Pali / etc.]
date_range: [approximate composition date or range]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [text, tradition-name, genre]
---
```

Body includes: textual overview, major themes, narrative summary and structure, manuscript tradition notes, key
interpretive cruxes (specific verses or passages that generate the most commentary
disagreement), and links to commentator pages.

**Canon scope (required).** `canon_scope` is the structural replacement for a single
`canon_status` value: canonicity is not a property of a text but a *relation* between a
text and a community. Each entry under a bucket is the page slug of a tradition (e.g.
`christianity`) or a sect (e.g. `sethian-gnosticism`, `latter-day-saints`). The same text
routinely appears in several buckets at once. `canon_status` is retained only as a coarse
one-word headline derived from `canon_scope`. The body must include a **Canon and
Reception** section narrating the split wherever it is non-trivial.

Worked examples the schema must handle:

- **Gospel of Thomas** — `canonical_for: [thomasine-christianity]`; `rejected_by:
  [proto-orthodox-christianity, catholicism, eastern-orthodoxy, protestantism]`;
  `disputed_by: [coptic-christianity]`. It is *not* merely "apocryphal": it is canonical
  within specific communities and explicitly rejected by others, and the structure must
  show that.
- **Book of Mormon** (taxonomy stress test) — `canonical_for: [latter-day-saints]`;
  `deuterocanonical_for: [<specific Restoration-movement sects>]`; `rejected_by:
  [catholicism, eastern-orthodoxy, protestantism, …]`. The same text is full scripture
  for one sect, graded/secondary canon for others, and non-scripture for everyone else.
  Its claim to *continue the biblical narrative* is a **reception fact recorded in the
  body** (a "Relationship to the parent canon" note), not a canon bucket — the buckets
  record only canonical *standing*, per community.

---

### Commentator Page (`wiki/commentators/`)
For individual commentators, schools, or movements.

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

Body includes: biographical context, hermeneutical method (literal/allegorical/moral/
anagogical; peshat/derash/remez/sod; etc.), major works, characteristic positions,
known controversies, and influence on later tradition.

---

### Figure Page (`wiki/figures/`)
For major biblical, religious, and historically significant figures who appear in or as
subjects of the texts — patriarchs, prophets, apostles, kings, priests, founders,
and other named individuals whose lives, acts, or identities generate sustained
commentary. This includes legendary or semi-legendary figures (Enoch, Melchizedek)
as well as historical persons (Cyrus, Nebuchadnezzar) who play significant textual
roles.

**Scope rule**: Create a figure page when a person is (a) named in one or more primary
texts, (b) the subject of substantial commentary or interpretive tradition, and (c)
not better handled as a concept (i.e., their significance is primarily biographical
and narrative rather than purely doctrinal). Figures who are themselves also
commentators (e.g., Maimonides, Paul) should have *both* a figure page and a
commentator page, cross-linked.

```yaml
---
title: [Figure Name]
also_known_as: [aliases, titles, epithets — e.g., "Israel", "the Apostle", "Rambam"]
tradition: [Judaism / Christianity / Islam / cross-tradition / etc.]
textual_sources: []   # primary texts where the figure appears
dates: [historical dates / traditional dates / floruit / "legendary" / "disputed"]
roles: []   # e.g., patriarch, prophet, apostle, king, priest, judge, founder
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [figure, tradition-name, role-type]
---
```

Body includes:

**Biographical Overview**: All known or traditionally attested biographical data —
birth, family, major life events, death — drawn from primary sources. Clearly
distinguish textual claims from historical-critical reconstructions. Where dates,
locations, or events are disputed, flag them explicitly rather than presenting one
tradition's account as fact.

**Primary Source Appearances**: Which texts feature this figure prominently, and in
what capacity? Include the key pericopes, chapters, or passages and a one-line
summary of what each contributes to the figure's portrait.

**Tradition-Specific Reception**: How do different religious traditions interpret,
develop, or contest this figure? This is the core of the page. For a figure like
Abraham or Moses, Jewish, Christian, Islamic, and Samaritan traditions each have
distinct portraits — record them separately. For each tradition note: the primary
canonical/authoritative source, the dominant interpretive move, and any significant
intra-tradition disputes.

**Theological and Narrative Significance**: What role does this figure play in the
theological structure of the text(s) — typologically, narratively, doctrinally?
Abraham as the father of faith; Moses as the mediator of the covenant; Melchizedek
as the type of the eternal priest; Paul as the apostle to the Gentiles.

**Historicity and Interpretive Controversies**: Where the figure's historical
existence, dating, identity, or actions are disputed, record the positions without
adjudicating. Examples: the historicity of the Exodus and Moses; the identity of
the Servant in Isaiah 40–55; the authorship of the Pauline epistles; whether
Melchizedek was human, angelic, or a pre-incarnate appearance of Christ.

**Influence on Commentary Traditions**: Which commentators have made this figure
central to their work, and in what ways? Note both allegorical uses (Philo on
Abraham as the soul's journey; Origen on Moses as the Christian teacher) and
literal-historical uses.

---

### Group Page (`wiki/groups/`)
For peoples, tribes, nations, ethnic groups, religious parties, social classes, and
other collective identities that appear as actors or foils in the primary texts and
generate sustained interpretive, theological, or polemical traditions (e.g. Canaanites,
Philistines, Moabites, the "nations/Gentiles", Pharisees, Sadducees, Samaritans, the
twelve tribes of Israel, "the poor", "the wise").

**Scope rule**: Create a group page when the collective is (a) named or treated as a
corporate actor in one or more primary texts, (b) the subject of substantial commentary,
typology, or identity construction across traditions, and (c) not better handled as a
concept (i.e., the page is primarily about a specific historical or textual people rather
than an abstract idea). Overlapping cases (e.g. "Israel" as both figure-like people and
theological concept) may warrant both a groups/ page and a concepts/ page, cross-linked.

```yaml
---
title: [Group Name]
also_known_as: [aliases, self-designations, outsider labels — e.g. "Gentiles / Goyim / Ta ethne", "Philistines / Peleset / Palastu"]
tradition: [Judaism / Christianity / Islam / cross-tradition / etc.]
textual_sources: []   # primary texts where the group features as actor or foil
periods_active: [e.g. "Late Bronze Age–Iron I", "Persian period", "Second Temple / 1st century CE"]
roles_significance: []  # e.g. antagonists, covenant people, model outsiders, heretics, mission field, etc.
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [group, tradition-name, category-or-period]
---
```

Body includes:

**Identity and Nomenclature**: Etymology and meaning of the primary name(s); how the
group names itself versus how outsiders label it; shifts in terminology across periods
and languages. Note cases of deliberate pejorative or honorific usage.

**Primary Textual Appearances**: Key passages, pericopes, or narrative arcs in which the
group appears as a collective character. One-line summaries of what each major locus
contributes to the overall portrait (positive, negative, ambiguous, or typological).

**Tradition-Specific Portraits**: How different religious traditions have interpreted,
allegorized, historicized, or deployed this group. Record separately for Jewish,
Christian, Islamic, and other relevant receptions. For each: dominant canonical sources
used, main interpretive lens (literal/historical, typological, moral exemplar, cautionary
tale, etc.), and notable intra-tradition disagreements or developments.

**Historical and Archaeological Context**: Extra-biblical evidence (inscriptions, material
culture, ANE parallels). Note debates over identification, origins, or historicity of
the group as presented in the texts. Distinguish textual claims from critical
reconstructions without adjudication unless the source itself does so.

**Theological and Narrative Significance**: The role the group plays in the theological
and narrative architecture of the text(s) — corporate personality, foil to the covenant
people, object of divine judgment and/or mercy, paradigm of faithfulness or apostasy,
vehicle for mission or inclusion, etc.

**Influence on Later Traditions and Controversies**: How the group has been used in
exegesis, preaching, liturgy, politics, and inter-religious polemic. Flag sensitive or
contested modern deployments (e.g. "Amalek", Canaanite conquest ethics, "Pharisee" as
epithet) and any resulting controversies pages.

---

### Location Page (`wiki/locations/`)
For geographical places — cities, regions, mountains, valleys, rivers, kingdoms, cult
sites, and other named spatial entities — that are more than incidental backdrops and
that carry sustained narrative, theological, or pilgrimage significance. The page must
explicitly address historical inhabitants ("who lived there when") and modern geographic
identification.

**Scope rule**: Create a location page when a place is (a) named in one or more primary
texts with narrative or symbolic weight, (b) the setting of significant events, figures,
or cultic activity, and (c) the object of later interpretive or devotional traditions
(e.g. Jerusalem/Zion, Babylon, Mount Sinai/Horeb, Galilee, the Jordan, Rome, Shechem,
Nineveh, the Temple Mount). Minor or purely incidental place names do not require pages.

```yaml
---
title: [Location Name]
also_known_as: [modern Arabic/Hebrew names, ancient variants, tell/site designations — e.g. "Tell es-Sultan (Jericho)", "Yerushalayim / al-Quds / Hierosolyma"]
tradition: [Judaism / Christianity / Islam / cross-tradition / etc.]
textual_sources: []   # primary texts in which the location is prominent
periods_inhabited: [summary of settlement history, e.g. "Chalcolithic–present; major phases: Early Bronze, Iron Age Israelite, Persian, Hellenistic-Roman, Byzantine, Islamic, modern"]
modern_geography: [current political/administrative location, nearest modern settlement, coordinates if known, terrain notes — e.g. "Tell es-Sultan, West Bank (Palestinian territories), ~2 km NW of modern Jericho (Ariha); Jordan Rift Valley, ~250 m below sea level; 31.870°N 35.444°E"]
associated_peoples: []  # key groups who controlled or inhabited the site in specific periods, with dates
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [location, tradition-name, site-type]
---
```

Body includes:

**Geographical and Historical Overview**: Physical setting, strategic or economic
importance, changes in settlement pattern, political control, and nomenclature over time.
Clearly separate periods and note major destructions, rebuilds, or abandonments.

**Primary Textual Appearances and Inhabitants**: Which texts feature the location
prominently and for what narrative or theological purposes. For each significant period
or textual stratum, record the groups explicitly or inferably living there or controlling
it (e.g. "Jebusites until David; Judahite capital thereafter; exilic and post-exilic
returns; Roman Aelia Capitolina after 135 CE").

**Archaeological and Extra-Biblical Data**: Major excavations, key finds (inscriptions,
destruction layers, cultic installations), and how they relate to (or challenge) the
textual portrait. Note ongoing identification debates (e.g. "which mound is Ai?").

**Modern Identification and Geography**: How the ancient site is identified today
(archaeological tell, village, city quarter, holy site). Current name(s) in local
languages, political status, accessibility, and any disputes over the identification
itself. Provide enough detail that a reader can locate the place on a modern map or in
person.

**Theological and Symbolic Significance**: Why the place matters theologically or
liturgically within each major tradition. Zion theology, exile and return motifs,
pilgrimage sites, "holy land" concepts, eschatological geography, etc. Record
tradition-specific developments (e.g. Islamic al-Quds and the Night Journey; Christian
holy sites and relic traditions; Jewish Temple Mount / Western Wall piety).

**Key Events, Figures, and Controversies**: Major biblical or traditional events tied to
the site; important figures associated with it; later interpretive or political
controversies (e.g. competing claims to sacred space, location-of-Golgotha debates,
modern Temple Mount / Haram al-Sharif status).

---

### Tradition Page (`wiki/traditions/[tradition]/[tradition].md`)
For a top-level religion or world tradition (Judaism, Christianity, Islam, Buddhism,
Hinduism, Daoism, etc.). One overview page per tradition, living at the root of that
tradition's subdirectory. The tradition page is the parent node for all of its `sects/`
pages and the home of the tradition's shared/mainstream canon.

```yaml
---
title: [Tradition Name]
also_known_as: []
type: tradition
date_range: [origin to present / floruit]
canon_core: []                 # texts canonical for the tradition broadly (the shared/mainstream canon) — text page slugs
hermeneutical_frameworks: []   # interpretive systems native to the tradition (PaRDeS, the Quadriga, Zahir/Batin, …)
major_sects: []                # slugs of the sect pages nested under this tradition
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [tradition, tradition-name]
---
```

Body includes: definition and self-understanding; historical origin and development; the
shared/mainstream canon and how canonical authority works in the tradition; the
tradition's native hermeneutical frameworks; a **map of major sects/sub-traditions** (one
line each, linked to their `sects/` pages); and cross-links to the figures, groups,
concepts, and controversies most central to the tradition.

**Non-theistic and multi-canon traditions**: a tradition need not be theistic (e.g.
Buddhism), and need not have a single canon. Where a tradition has **multiple parallel
canons with no common ancestor text** (the Pali Canon vs. the Mahayana sutra collections
vs. the Vajrayana tantras), keep `canon_core` minimal — listing only what is genuinely
shared — and carry the divergent canons at the **sect level** via each sect's
`canon_distinctives` / `key_texts`. For non-theistic traditions, "doctrine" and the
soteriological goal replace "theology proper" in the body; record the tradition's own
account of ultimate reality (e.g. *nirvana*, *dao*) rather than forcing a deity slot.

---

### Sect / Denomination Page (`wiki/traditions/[tradition]/sects/[sect].md`)
For a religious sub-tradition, denomination, sect, movement, school, or lineage *within* a
parent tradition — e.g. Gnosticism, Marcionism, Catharism, Rabbinic Judaism, Karaism,
Kabbalah, the Latter-day Saints, Sunni and Shia Islam, Theravada / Mahayana / Vajrayana
Buddhism, Zen. A sect is a **first-class page type**: it has its own canon, its own
hermeneutical rules, and its own relationship to the parent tradition and to "orthodoxy".

**Scope rule**: Create a sect page when a sub-tradition (a) is treated as a distinct
religious community or school within a parent tradition, (b) has a canon, doctrine, or
hermeneutic that diverges from the parent or from sibling sects, and (c) generates
sustained commentary, identity construction, or polemic.

A sect page is **not** a duplicate of a `groups/` page. Where a group page already exists
for the same community (e.g. [[gnostics]], [[marcionites]], [[ebionites]],
[[montanists]]), keep both and cross-link them: the **group page** treats the community as
a social/historical actor (who they were, where, when, archaeology, polemical reception);
the **sect page** treats the sub-tradition as a *system* (its canon, doctrine,
hermeneutics, and relationship to orthodoxy). See the disambiguation note under Naming and
Linking Conventions.

```yaml
---
title: [Sect / Denomination Name]
also_known_as: []
parent_tradition: [slug of the parent tradition page — e.g. christianity]
type: [denomination / sect / movement / school / lineage / normative stream]
dates: [emergence–present / floruit / "extinct (dates)"]
status: [extant / extinct / revived]
relationship_to_orthodoxy: [normative / heterodox / heretical (by whom) / schismatic / independent / self-understood-restoration]
canon_distinctives: []          # texts this sect adds, removes, re-ranks, or rejects vs. the parent canon — text page slugs
key_doctrinal_distinctives: []
hermeneutical_method: []
key_figures: []
key_texts: []                   # text page slugs central to the sect
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [sect, parent-tradition-name]
---
```

Body includes:

**Identity and Origins**: What the sect is, when and where it emerged, and out of what
parent tradition or prior sect. Self-designation versus outsider labels.

**Relationship to the Parent Tradition**: What it inherits and shares; the precise points
of departure; whether it understands itself as a reform, restoration, purification,
continuation, or new revelation.

**Canon and Scripture (Canon Divergence)** — the core required section: how this sect's
canon differs from the parent's — texts added (new revelation, recovered scripture), texts
removed or demoted, texts re-ranked, texts reinterpreted. This is the counterpart to the
`canon_scope` field on text pages: every text the sect treats distinctively should appear
here **and** list this sect in the appropriate `canon_scope` bucket on its own text page.
Flag any text whose status here differs from the parent tradition.

**Doctrinal Distinctives**: The theological positions that define the sect against the
parent and sibling sects.

**Hermeneutical Method**: How the sect reads its scriptures (and the parent's) — its native
interpretive rules, esoteric/exoteric layering, authoritative interpreters. Per the
Hermeneutical Tracking requirement this section is mandatory.

**Relationship to Orthodoxy and Other Sects**: Who regards this sect as normative,
heterodox, or heretical, and on what grounds — recorded *without adjudication* per the
Contradiction Protocol, with the tradition context of each judgment. Mutual condemnations
(e.g. proto-orthodox vs. Gnostic) are documented from both sides.

**Historical Development, Subdivisions, and Influence**: Internal schools and offshoots,
later history, suppression or survival, influence on the parent tradition and beyond.

**Sources Ingested**.

---

### Concept Page (`wiki/concepts/`)
For theological constructs, hermeneutical methods, and recurring doctrinal categories.

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

Body includes: definition, origin, tradition-specific usage variations, key
text-concept connections, and cross-links to controversies where the concept is
contested.

---

### Comparison Page (`wiki/comparisons/`)
Generated in response to cross-tradition or cross-commentator queries. Filed for
permanence.

```yaml
---
title: [Comparison Description]
entities_compared: []
generated_from_query: [brief description]
date: [YYYY-MM-DD]
tags: [comparison]
---
```

---

### Controversy Page (`wiki/controversies/`)
For interpretive disputes that cut across multiple commentators or traditions.

```yaml
---
title: [Issue in Dispute]
text_locus: [the specific verse, passage, or concept at stake]
positions: []   # list of named positions
traditions_involved: []
resolution_status: [open / historically resolved / tradition-specific]
last_updated: [YYYY-MM-DD]
tags: [controversy]
---
```

---

## Hermeneutical Tracking — Core Requirement

This wiki must track *how* a text is read, not just *what* it says. Every text page,
commentator page, tradition page, and sect page must record the interpretive
framework(s) in use — and a sect page must record the hermeneutical rules that
distinguish it from its parent tradition. Group pages and location pages should likewise
note tradition-specific interpretive moves, typological uses, and polemical deployments
of the collective or place in question.

Standard frameworks to identify and tag:

- **Jewish**: Peshat (plain), Derash (midrashic), Remez (allegorical), Sod (mystical) —
  collectively PaRDeS
- **Christian patristic/medieval**: Literal, Allegorical, Tropological (moral),
  Anagogical — the Quadriga
- **Islamic**: Zahir (exoteric), Batin (esoteric); tafsir bi'l-ma'thur (tradition-based)
  vs. tafsir bi'l-ra'y (reason-based)
- **Buddhist**: Neyartha (interpretable) vs. Nitartha (definitive); commentarial
  lineage tracking
- **Daoist**: *commentary-as-transformation* — the commentary functions as a practice
  that transforms the reader/adept, not merely as explanation; track the divide between
  the **philosophical/metaphysical** reading (xuanxue; Wang Bi) and the
  **religious/longevity-cultivation** reading (Heshang Gong) of the same text
- **Modern critical**: Historical-critical, form criticism, redaction criticism,
  canonical criticism, reader-response

When ingesting a commentary, identify which framework(s) it operates within and record
this explicitly. Cross-tradition comparisons of the same method (e.g., allegory in
Origen vs. Philo vs. Ibn Arabi) are valuable — flag these for comparison page generation.

---

## Ingest Workflow — Deployed Subagent Strategy (DEFAULT)

**Primary ingest method for all sources.** Parallelizes claim/passage extraction across
Sonnet subagents while keeping all scaffolding, taxonomy, canon decisions, reconciliation,
and validation on the main thread. The scope-and-fidelity workflow below ("Ingest Workflow
— Scope & Fidelity") remains authoritative for **what each page must contain** (page types,
frontmatter, `canon_scope`, hermeneutical tracking, coverage ledger, the lean-filing rule)
and **how to partition a large work into scopes** (the scope plan) — apply it *within* the
steps here. The two are one workflow: subagents are how a scope gets read in parallel, not a
different standard of fidelity.

Non-negotiable principle: **the main thread owns structure; subagents own bulk extraction.**
Subagents never decide taxonomy, page naming, `canon_scope` buckets, sect-vs-group splits,
or cross-links — they extract faithfully within boundaries the main thread already drew.

**Step 1 — Scaffold first, on the main thread.** Before spawning anything, read enough (TOC,
intro, conclusion, targeted sampling) to do the structural work that requires judgment:
- Identify the source type and, for any primary text, its **canonical status per sect /
  tradition** and whether that differs from the parent tradition (drives `canon_scope` and
  any sect canon-divergence section) — per Ingest-sequence step 1 below.
- Write the **source summary page** (in `scholarship/`, or the relevant text/commentary
  page) including the **scope plan** for a large multi-section work (the ordered sequence of
  bounded scopes) and the **coverage ledger** skeleton.
- Create or name the **key pages everything links to** — the central text/commentator/
  tradition/sect pages, and the figure/group/location/concept pages the ingest will
  populate — so subagents inherit names and never invent structural ones.
- Decide **naming conventions, the page taxonomy, and the hermeneutical framing** (which
  PaRDeS / Quadriga / Zahir-Batin / neyartha-nitartha / etc. frameworks are in play).

Do not spawn any agent until the linkable page names and the canon/taxonomy decisions exist.

**Step 2 — Split the scope by disjoint line-ranges.** Within the scope being read, divide the
raw text into N contiguous, non-overlapping chunks by line number.
- **Size N to the material, not a fixed number.** Base it on *body* length × density (exclude
  front matter, apparatus, indices, untranslated sections). Rule of thumb: one agent per
  ~2,000–3,500 body lines; floor 2–3; up to ~10 for very large/multi-volume references. **Do
  not default to 6** — over-splitting starves agents of context.
- **Weight chunks by density and importance, not even boundaries.** Dense/pivotal stretches
  (a key sura's tafsir, a doctrinally loaded sutta, the heart of a commentary) get their own
  agent; lighter narrative combines into a larger range. Align edges to natural
  section/chapter boundaries only where it doesn't fight the weighting.
- Ranges must be **disjoint** — every line in exactly one chunk.

**Step 3 — Spawn one Sonnet subagent per chunk (staggered batches + background).** Use the
Agent tool with **`model: sonnet`** and `run_in_background: true`, one agent per chunk. Each
prompt must contain: its **exclusive line-range** (read only that range); the **relevant
schema, naming conventions, and hermeneutical-tracking requirement** from this file; the
**established page names** it may link to (Step 1); **exclusive ownership of the titles it
creates** (a distinct topic set / title namespace so no two agents write the same file); and
the **faithfulness mandate** — extract only what is actually in its range, **with
verbatim-anchored grounding quotes and line/page loci**, no outside knowledge, no background
summary presented as the source's content, no reading beyond its range (this is principle 4
of the scope-and-fidelity workflow, enforced per agent).
- **Staggered deployment (rate-limit mitigation):** never launch all at once. Spawn in
  batches of 2 (at most 3 for lighter ranges), then `sleep 10` before the next batch (20s+
  if 429s recur). Optionally pre-cut per-range cache files
  (`/tmp/..._cache/range_N_START_END.txt`) so each agent does a cheap one-shot read of only
  its slice. Collect task_ids; monitor to completion. If a subagent fails (e.g. 429), the
  main thread recovers *that range alone* (read its slice, extract, label the block
  "Main-thread recovery (rate limit on subagent)") and lets the others continue. Do not
  restart a rate-limited agent.

**Step 4 — Review and tie together (main thread).** Dedupe overlapping claims; reconcile
naming; fix cross-links between new pages (subagents only linked Step-1 names); fill the
source page's coverage ledger for the scope just read; record any **contradictions** on both
pages and the relevant `controversies/` page (Contradiction Protocol); set/extend
`canon_scope` buckets on every affected text page; confirm each new sect/group page is
cross-linked to its counterpart. Remove agent artifacts (stray instructions, prompt echoes,
stray tags — grep first). **File lean** per the scope-and-fidelity rule: extend a central
page before creating a new one; de-link tangential mentions rather than spawning stubs.

**Step 5 — Lint and validate.** Run `python Scripts/lint_wiki.py` and resolve what it
surfaces — red links (missing pages), orphans, and commentators/figures/groups/locations/
sects mentioned without their own page. Re-run until clean.

**Step 6 — Bookkeeping and file.** Update `index.md` with new/modified pages; tick the source
on `outstanding sources.md` if it is a line item there; append the `log.md` entry stating the
declared **scope** and whether it was read in full or remains in progress (per Ingest-sequence
step 5 below). For a multi-scope work, checkpoint after **each** scope (ledger + index + log,
verified on disk) and continue autonomously to the next scope in the plan; do not pause to ask
"what next?".

**Step 7 — File the raw source out of `raw/` root.** Once a source is **fully ingested for its
declared scope** (not mid-way through a multi-scope work — wait until the work's scope plan is
exhausted), move its file out of the top level of `raw/` into the matching typed subfolder so the
root does not accumulate loose files: `raw/texts/` for primary texts, `raw/commentaries/` for
commentary works, `raw/scholarship/` for academic works, `raw/misc/` for anything that fits none.
This is a **relocation only** — never alter the file's contents (the "Never modify files in `raw/`"
rule governs *content*; filing into a subfolder is permitted and expected). After moving, **update
every reference to the old path**: the `Source:` line on the source's `scholarship/`/text page, its
coverage ledger, and the `log.md` entry. Use `git mv` so history is preserved. (For an OCR'd source,
this relocation happens together with the PDF-replacement in the OCR rule below.)

> The section below remains the source of truth for fidelity, scope partitioning, page
> contents, `canon_scope`, hermeneutical tracking, and the coverage ledger. Read it as the
> definition of *quality*; read the six steps above as the definition of *throughput*.

---

## Ingest Workflow — Scope & Fidelity

The governing principle is **fidelity within a declared scope** — not exhaustiveness. The
point of an ingest is that everything the wiki attributes to a source was actually read in it;
it is *not* that every source must be read cover to cover. These two ideas were once conflated
(a full-read mandate), which made large reference works an open-ended burden. They are now
separated: you read **what we scope**, and you read it honestly.

**1. Scope the ingest first.** Before reading, fix the *scope* — how much of the source this
ingest covers:
- **Small, bounded sources** (a primary text or pericope, a single commentary, a paper, a
  short monograph) → scope = **the whole thing**. It is small enough to simply read in full.
- **Large reference / multi-volume / survey works** (encyclopedias, multi-volume histories,
  big anthologies) → scope = a **named portion** I set or approve: a chapter, a topic, a
  volume, a span of pages. Do not silently expand beyond it.

**Scope it yourself, and progress autonomously.** Do **not** ask me to choose a scope each
time. For a large multi-section work, *you* partition it: lay out a **scope plan** — an ordered
sequence of coherent, bounded scopes that together cover the work (grouping sections
thematically/chronologically into meaty units, not one tiny scope per heading) — record it on
the source's scholarship page, and then **work through the scopes in order, one per pass,
without pausing to ask which is next.** Checkpoint after each scope (ledger + index + log,
verified) so I can read progress, redirect, or stop at any time; absent a redirection, continue
to the next scope automatically. When the current work's plan is exhausted, move to the next
unticked source on `outstanding sources.md` and scope *it* the same way. Keep every pass
**lean** (principle 3). Surface a choice to me only when partitioning is genuinely ambiguous,
when a scope proves too thin to stand alone (widen it), or when you hit something that needs my
judgment (a sourcing gap, a faithfulness problem, a contested call) — not for routine "what
next?" decisions.

**2. Read the scope in full, in order — no TOC-triage.** Within the chosen scope, actually
**read** the text sequentially; do not scan the table of contents, index, or a few searched
passages and reconstruct from those. Search tools (grep, find, keyword lookup) may
*supplement* the read — to locate a cross-reference, verify a term, or relocate a passage you
already read — but must **never substitute** for it.

**3. Read in large spans; file in lean batches.** Prioritize reading over filing. Read a
substantial span (a chapter, or several) keeping **brief, verbatim-anchored notes** as you go
(key claims with their line/page locus, so attribution stays checkable), then file the batch.
Stop to file only when you need to — at a natural boundary, when unfiled notes have grown
large enough that detail would be lost, when later material depends on a page earlier material
warranted, or when a contradiction must be recorded while both sides are fresh. **File lean:**
prefer extending a central page over creating a new one; create a page only when the subject
genuinely warrants its own; de-link a tangential mention to plain text rather than spawning a
stub. The notes must be taken *during* the read — this is not a licence to skim and
reconstruct from memory.

**4. Faithfulness — record only what the source says.** Attribute to a source only content you
actually read in it. **Never present background knowledge, a standard textbook summary, a
familiar technical term, or an inference as the source's own content.** When you add context
from outside the source, mark it explicitly as outside the source (e.g. "not in X's account").
If you are about to attribute a specific term, date, or claim to the source, confirm it is
actually there (search the text) before doing so. This is the counterpart of the Contradiction
Protocol's rule to distinguish textual claims from reconstruction.

**5. Coverage ledger (required) — and a scoped ingest is *complete for its scope*.** On the
source's `scholarship/` (or text/commentary) page, record exactly what was read — chapters,
sections, or page/line ranges. A scoped read that covers its declared scope is **done, not a
standing debt**: mark it "read in full (scope: Vol. I, Chs. I–V)" or similar, *not* "partial."
Reserve "partial / in progress" for a scope you have not yet finished reading. Any portion
inside the scope deliberately left unread (untranslatable apparatus, foreign-language
sections, indices, repetitive matter) must be stated explicitly, with the reason. Widening the
scope later (e.g. to another volume) is a **new scoped pass**, logged as such — not a debt
carried by the old one.

**OCR rule.** If a source arrives as a non-OCR (image-only) PDF, run OCR to produce a readable
`.txt` or `.md` file before ingesting. Once the OCR output is verified as usable, **replace the
original PDF in `raw/` with the OCR'd file** (same base name, new extension). The original PDF
is no longer the canonical source file after replacement — delete or overwrite it. Record the
fact of OCR conversion in the source's `scholarship/` page (e.g. "Source: `raw/foo.md` — OCR'd
from `foo.pdf` on YYYY-MM-DD").

When I provide a new source, follow this sequence (the principles above govern the whole
sequence):

1. **Identify** the source type (primary text, commentary, scholarship, or other) and,
   for any primary text, its **canonical status within the sect or tradition being
   ingested — and whether that status differs from the parent tradition** (e.g. a text
   canonical for the sect at hand but rejected by the parent, or vice versa). Answer this
   explicitly; do not leave it implicit. It drives the `canon_scope` field on the text
   page and the canon-divergence section of any sect page.
2. **Read the scope through and discuss** with me: read the in-scope text sequentially (per
   principles 2–4 above), and report key takeaways, surprising claims, and what it adds or
   challenges relative to the wiki — grounded in the actual reading, not the TOC.
3. **Write or update** the relevant pages (in lean batches per span read, per principle 3
   above — extend before creating):
   - Write a source summary page in the appropriate `wiki/` subdirectory, **including its
     coverage ledger** (the span actually read).
   - Update the commentator page if the source is attributed to a known figure.
   - Update or create text pages for any primary texts prominently discussed.
   - Update or create **figure pages** for any named biblical or religious figures
     who receive substantial biographical, typological, or interpretive treatment
     in the source. If a source introduces a significant new tradition-specific
     reading of a figure (e.g., Philo's allegorical Abraham, Origen's Moses,
     Islamic reception of a patriarch), add that tradition's section to the
     existing figure page or create the page if it does not yet exist.
   - Update or create **group pages** for any peoples, tribes, nations, ethnic
     groups, religious parties, or cultural collectives that receive sustained
     narrative, theological, or polemical treatment (e.g. Canaanites, Pharisees,
     "the nations"). If a source develops a new tradition-specific portrait or
     typology of a group, extend the existing page or create it.
   - Update or create **location pages** for any places (cities, regions, cult
     sites, etc.) whose historical inhabitants ("who lived there when") or modern
     geographic identification are discussed, or that carry significant narrative,
     theological, or pilgrimage weight (e.g. Jerusalem, Babylon, Mount Sinai,
     Shechem). Include explicit settlement history and modern mapping data.
   - Update or create **tradition and sect pages**. If the source treats a sub-tradition,
     denomination, sect, school, or movement (e.g. Gnosticism, Marcionism, Kabbalah, a
     Buddhist vehicle), create or extend its `traditions/[parent]/sects/[sect].md` page —
     especially its canon-divergence and hermeneutical-method sections — and the parent
     `traditions/[parent]/[parent].md` overview if needed. Where a `groups/` page already
     exists for the same community, keep both and cross-link.
   - **Maintain `canon_scope` on every affected text page.** Whenever a source establishes
     that a sect or tradition treats a text as canonical, deuterocanonical, authoritative
     (non-canonical), disputed, or rejected, record it in the matching `canon_scope`
     bucket. Conflicting valuations across communities are expected and must be preserved,
     not flattened (Contradiction Protocol).
   - Update or create concept pages for theological/hermeneutical terms introduced
     or developed.
   - Update or create a controversy page if the source takes a position on a
     disputed question.
   - Update `overview.md` if the new source materially shifts the scope.
4. **Update `index.md`** with the new/modified pages.
5. **Append to `log.md`** with format: `## [YYYY-MM-DD] ingest | [Source Title]` — and state
   the coverage: the declared **scope** and whether it was read in full or is still in
   progress (e.g. "scope: Vol. I Chs. I–V — read in full" or "scope: Ch. VI — partial, read
   pp. X–Y"), so the log is honest about what was read.
6. **File the raw source out of `raw/` root.** Once the source is fully ingested for its declared
   scope, `git mv` its file from the top of `raw/` into the matching typed subfolder (`raw/texts/`,
   `raw/commentaries/`, `raw/scholarship/`, or `raw/misc/`), then update every reference to the old
   path (the source page's `Source:` line and coverage ledger, and the `log.md` entry). Relocation
   only — do not alter the file's contents.

A single commentary ingest may touch 10–20 pages; a focused scope of a larger work, fewer.
Filing should be **lean** — only the pages a span genuinely changes, extending existing pages
in preference to creating new ones. Widening to a larger scope of the same work is a later,
separately-scoped pass, not an obligation incurred by the first.

---

## Contradiction Protocol

Religious commentary traditions are full of direct, irreconcilable conflicts —
between traditions, within traditions, and between historical-critical scholarship
and confessional readings. Do not flatten these.

When new material contradicts existing wiki content:
- Flag the contradiction explicitly on both affected pages.
- Create or update the relevant `wiki/controversies/` page.
- Do **not** adjudicate which reading is correct unless I explicitly ask for analysis.
- Record the tradition context of each position — a contradiction between a Calvinist
  and an Arminian reading is not the same kind of dispute as a contradiction between
  a critical scholar's dating and a traditional dating.

---

## Query Workflow

When I ask a question:

1. Read `index.md` to identify relevant pages.
2. Read those pages.
3. Synthesize an answer with citations to wiki pages (not raw sources directly).
4. If the answer required non-trivial synthesis or produced a useful comparison,
   offer to file it as a `wiki/queries/` page.
5. Append to `log.md`: `## [YYYY-MM-DD] query | [Question Summary]`

---

## Lint Workflow

When I ask for a wiki health check:

- Identify pages with no inbound links (orphans).
- Identify commentators mentioned in text pages but lacking their own page.
- Identify named biblical or religious figures mentioned repeatedly across text,
  commentator, or concept pages but lacking their own `figures/` page.
- Identify groups, peoples, tribes, nations, or cultural/religious collectives
  mentioned repeatedly across text, figure, or concept pages but lacking their own
  `groups/` page.
- Identify locations or places (cities, regions, cult sites) whose historical
  inhabitants or modern geography are discussed but that lack their own `locations/`
  page.
- Identify sub-traditions, denominations, sects, schools, or movements referenced across
  pages (in figures, groups, texts, or controversies) but lacking their own
  `traditions/[parent]/sects/` page, and any top-level tradition lacking an overview page.
- Identify text pages missing a `canon_scope` field, or whose `canon_scope` omits a
  community known (from ingested sources) to canonize, dispute, or reject the text.
- Identify concepts used repeatedly without a concept page.
- Identify controversies described inline that should be promoted to a
  `controversies/` page.
- Identify claims that newer sources have superseded — flag for review, do not
  silently overwrite.
- Identify **ledger gaps**: source pages that lack a coverage ledger entirely, or whose
  ledger marks the *declared scope* as still "in progress / partial" (as opposed to a scope
  read in full). A scope deliberately narrower than the whole work is **not** a defect — flag
  only unfinished in-scope reads, missing ledgers, or a source ticked "done" on the
  acquisition list whose ledger shows its declared scope was never actually finished.
- Suggest 3–5 sources worth seeking (specific commentaries, scholarly works,
  primary texts) based on gaps in current coverage.
- Suggest 3–5 questions worth investigating based on unresolved tensions.

---

## Naming and Linking Conventions

- File names: `kebab-case.md` (e.g., `thomas-aquinas.md`, `fourfold-sense.md`)
- Wiki-internal links use Obsidian format: `[[page-name|Display Name]]`
- For multi-tradition concepts with tradition-specific names, use the most
  widely recognized English name as the canonical page title, with tradition-specific
  terms aliased in the page body (e.g., `allegorical-reading.md` covers Remez,
  Theoria, Ta'wil as tradition-specific instances).
- **Tradition / sect / group disambiguation**: a *tradition* page is a top-level religion
  (`traditions/[tradition]/[tradition].md`); a *sect* page is a sub-tradition within it
  (`traditions/[tradition]/sects/[sect].md`) carrying canon, doctrine, and hermeneutics; a
  *group* page (`groups/`) is a people or community as a social/historical actor. A
  community that is both a people and a sub-tradition (Gnostics, Marcionites, Ebionites,
  Montanists) gets **both** a group page and a sect page, cross-linked.
- **Nested paths are for filing, not for link syntax**: sect and tradition pages are still
  referenced with bare slugs in Obsidian links (`[[gnosticism|Gnosticism]]`), not with the
  full nested path. Keep sect/tradition slugs globally unique so bare-slug links resolve.
- **`canon_scope` entries are page slugs**: each item in a `canon_scope` bucket (and in a
  sect's `canon_distinctives`) is the kebab-case slug of a tradition or sect page, so the
  canon relation is navigable (e.g. `latter-day-saints`, `sethian-gnosticism`,
  `proto-orthodox-christianity`).
- Manuscript sigla, critical apparatus notation, and original-language terms should
  appear in the page body, not in file names.
- Original-language terms: transliterate consistently (choose one system per language
  and document it in `overview.md`).

---

## Transliteration Standards (default — override as needed)

- **Hebrew**: SBL Academic style (no pointing in running text unless exegetically relevant)
- **Greek**: Standard academic transliteration; retain Greek script where meaning depends on it
- **Arabic**: Simplified transliteration without diacritics for running text; full
  diacritics in technical pages
- **Sanskrit/Pali**: IAST for Sanskrit; standard Pali transliteration

---

## Scope

Current scope of this wiki: [TO BE DEFINED — fill in as we work. Examples:
"Synoptic Gospels and their patristic commentators," "Maimonidean rationalism and
its critics," "Quranic tafsir traditions through the 10th century," etc.]

I will update this field as the scope evolves.

---

## Division of Labor

**I handle**: sourcing documents, directing the analytical focus, asking questions,
reading the wiki, and deciding what matters.

**You handle**: all writing, all cross-referencing, all maintenance, all filing,
all bookkeeping. Every word in the `wiki/` directory is yours unless I explicitly
edit something myself.
