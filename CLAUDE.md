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
  traditions/               # Denominational and textual traditions (e.g., Talmudic, Patristic, Sufi)
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
canon_status: [canonical / deuterocanonical / apocryphal / non-canonical]
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

This wiki must track *how* a text is read, not just *what* it says. Every text page
and commentator page must record the interpretive framework(s) in use. Group pages
and location pages should likewise note tradition-specific interpretive moves,
typological uses, and polemical deployments of the collective or place in question.

Standard frameworks to identify and tag:

- **Jewish**: Peshat (plain), Derash (midrashic), Remez (allegorical), Sod (mystical) —
  collectively PaRDeS
- **Christian patristic/medieval**: Literal, Allegorical, Tropological (moral),
  Anagogical — the Quadriga
- **Islamic**: Zahir (exoteric), Batin (esoteric); tafsir bi'l-ma'thur (tradition-based)
  vs. tafsir bi'l-ra'y (reason-based)
- **Buddhist**: Neyartha (interpretable) vs. Nitartha (definitive); commentarial
  lineage tracking
- **Modern critical**: Historical-critical, form criticism, redaction criticism,
  canonical criticism, reader-response

When ingesting a commentary, identify which framework(s) it operates within and record
this explicitly. Cross-tradition comparisons of the same method (e.g., allegory in
Origen vs. Philo vs. Ibn Arabi) are valuable — flag these for comparison page generation.

---

## Ingest Workflow

When I provide a new source, follow this sequence:

1. **Identify** the source type: primary text, commentary, scholarship, or other.
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
