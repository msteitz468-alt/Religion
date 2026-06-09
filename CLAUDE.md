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

## Ingest Workflow

When I provide a new source, follow this sequence:

1. **Identify** the source type (primary text, commentary, scholarship, or other) and,
   for any primary text, its **canonical status within the sect or tradition being
   ingested — and whether that status differs from the parent tradition** (e.g. a text
   canonical for the sect at hand but rejected by the parent, or vice versa). Answer this
   explicitly; do not leave it implicit. It drives the `canon_scope` field on the text
   page and the canon-divergence section of any sect page.
2. **Discuss** with me: key takeaways, surprising claims, what this source adds or
   challenges relative to the wiki's existing contents.
3. **Write or update** the relevant pages:
   - Write a source summary page in the appropriate `wiki/` subdirectory.
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
5. **Append to `log.md`** with format: `## [YYYY-MM-DD] ingest | [Source Title]`

A single commentary ingest may touch 10–20 pages. That is expected.

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
