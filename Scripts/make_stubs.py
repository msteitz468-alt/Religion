import os

stubs = {
    'wiki/concepts/melchizedek.md': ("Melchizedek", "concept"),
    'wiki/concepts/sound-doctrine.md': ("Sound Doctrine", "concept"),
    'wiki/concepts/abraham.md': ("Abraham", "concept"),
    'wiki/concepts/godliness.md': ("Godliness", "concept"),
    'wiki/concepts/typology.md': ("Typology", "concept"),
    'wiki/concepts/creation-ex-nihilo.md': ("Creation Ex Nihilo", "concept"),
    'wiki/concepts/sacrifice.md': ("Sacrifice", "concept"),
    'wiki/commentators/f-f-bruce.md': ("F.F. Bruce", "commentator"),
    'wiki/commentators/william-lane.md': ("William Lane", "commentator"),
    'wiki/commentators/peter-obrien.md': ("Peter O'Brien", "commentator"),
    'wiki/commentators/harold-attridge.md': ("Harold Attridge", "commentator"),
    'wiki/commentators/john-calvin.md': ("John Calvin", "commentator"),
    'wiki/commentators/rabbi-abraham-ben-david.md': ("Rabbi Abraham ben David (Raavad)", "commentator"),
    'wiki/commentators/rabbenu-gershom.md': ("Rabbenu Gershom", "commentator"),
    'wiki/commentators/sherira-gaon.md': ("Sherira Gaon", "commentator"),
    'wiki/texts/tosafot.md': ("Tosafot", "text"),
    'wiki/texts/talmud-yerushalmi.md': ("Jerusalem Talmud (Talmud Yerushalmi)", "text"),
    'wiki/texts/haggai.md': ("Haggai", "text"),
    'wiki/concepts/evangelical-commentary.md': ("Evangelical Commentary", "concept"),
    'wiki/controversies/isaiah-job-servant-direction.md': ("Direction of Influence: Isaiah's Servant and Job", "controversy"),
    'wiki/controversies/flood-universality.md': ("Universality of the Flood", "controversy"),
    'wiki/controversies/jephthah-vow.md': ("Jephthah's Vow", "controversy"),
    'wiki/controversies/paris-trial-1240.md': ("Paris Trial of 1240", "controversy"),
    'wiki/controversies/women-and-worship.md': ("Women and Worship (1 Cor 11/14)", "controversy"),
}

templates = {
    'concept': """---
title: {title}
domain: theology
traditions_using: [Judaism, Christianity]
sources_ingested: 0
last_updated: 2026-06-06
tags: [concept, stub]
---

# {title}

This is a stub page for the concept of {title}. It has been mentioned in other articles but not yet fully detailed.
""",
    'commentator': """---
title: {title}
full_name: {title}
dates: unknown
tradition: unknown
affiliation: unknown
primary_texts_commented: []
sources_ingested: 0
last_updated: 2026-06-06
tags: [commentator, stub]
---

# {title}

This is a stub page for the commentator {title}.
""",
    'text': """---
title: {title}
tradition: unknown
canon_status: unknown
language_original: unknown
date_range: unknown
sources_ingested: 0
last_updated: 2026-06-06
tags: [text, stub]
---

# {title}

This is a stub page for the text {title}.
""",
    'controversy': """---
title: {title}
text_locus: multiple
positions: []
traditions_involved: []
resolution_status: open
last_updated: 2026-06-06
tags: [controversy, stub]
---

# {title}

This is a stub page for the controversy regarding {title}.
"""
}

for path, (title, category) in stubs.items():
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(templates[category].format(title=title))

print("Stubs created.")

# Link talmudic-period in talmud-bavli.md
with open("wiki/texts/talmud-bavli.md", "r") as f:
    tb = f.read()
if "talmudic-period" not in tb:
    tb = tb.replace("Rabbinic Judaism", "Rabbinic Judaism (see [[talmudic-period]])", 1)
    with open("wiki/texts/talmud-bavli.md", "w") as f:
        f.write(tb)
