# Needed Sources — Religious Commentary Wiki

Sequenced ingestion plan for expanding the wiki beyond its current Jewish/Christian foundation.
Add in order: Islam → Buddhism → Hinduism → Daoism. Each tier assumes the previous tier's
schema upgrades are in place.

---

## Instructions for Claude Code

### On First Run

Read this file in full. Then execute the following steps in order:

1. **Create the directory structure** if it does not exist:
   ```
   raw/texts/islam/
   raw/texts/buddhism/
   raw/texts/hinduism/
   raw/texts/daoism/
   raw/texts/zoroastrianism/
   raw/texts/confucianism/
   raw/texts/second-temple-judaism/
   raw/commentaries/islam/
   raw/commentaries/buddhism/
   raw/commentaries/hinduism/
   raw/commentaries/daoism/
   raw/scholarship/
   ```

2. **Attempt to download every source marked `[PUBLIC DOMAIN]` or `[FREE ONLINE]`**
   using the URLs provided. Save each file to the path specified. Log every attempt
   — success or failure — to `raw/download-log.md` with format:
   ```
   ## [YYYY-MM-DD] [SUCCESS|FAILED] | [Source Title] | [URL]
   ```

3. **After all download attempts**, update the `## Outstanding Sources` section at
   the bottom of this file. For every source that could not be downloaded, add or
   confirm its entry under the appropriate tradition. Do not remove entries that
   were successfully downloaded — move them to a `## Downloaded Sources` section
   instead so there is a permanent record.

4. **Do not begin wiki ingestion** until I confirm the downloads and give the go-ahead.
   The download pass and the ingestion pass are separate operations.

### On Subsequent Runs

- Check `raw/download-log.md` to see what has already been attempted.
- Do not re-download files that already exist in `raw/`.
- If new sources have been added to this file since the last run, download only the new ones.
- Re-attempt any prior `[FAILED]` downloads — sources sometimes come back online.
- Update `## Outstanding Sources` and `## Downloaded Sources` sections accordingly.

### Download Rules

- Save files as `.txt` or `.md` where the source is plain text or HTML-converted.
- Save files as `.pdf` where the source is a PDF.
- Preserve the original language where available; save English translations as separate
  files in the same directory with `-en` appended to the filename.
- If a URL redirects to a different format than expected, download whatever is available
  and note the format in `download-log.md`.
- Do not download anything behind a paywall, login wall, or access restriction.
  Mark those as `[NEEDS SOURCING]` in the Outstanding Sources section.
- Project Gutenberg, Wikisource, Sacred Texts (sacred-texts.com), SuttaCentral,
  GRETIL, and Internet Archive are reliable open sources — prefer these over
  aggregator sites.

---

## Sequencing Rationale

- **Islam first**: integrates cleanly with existing Abrahamic schema; immediately generates
  cross-tradition controversy pages (Quranic vs. biblical figures — Ibrahim/Abraham, Isa/Jesus,
  Musa/Moses)
- **Buddhism second**: forces schema surgery (non-theistic tradition, multiple non-ancestral
  canons, Neyartha/Nitartha hermeneutical framework) that prepares the wiki for Hinduism
- **Hinduism third**: most complex single entry; requires the sect page type fully built
  before ingestion begins
- **Daoism fourth**: hermeneutically most foreign; benefits from comparative depth built
  in earlier legs

---

## Tier 1 — Add Immediately

### Islam

**Schema note**: Tafsir tradition maps directly onto existing commentator page type.
Add Sunni/Shia/Sufi as sect pages before ingesting. The qira'at (variant Quranic
readings) should be a controversy page.

#### Primary Texts

| Source | Status | URL | Save Path |
|---|---|---|---|
| Quran — Arabic (Uthmanic text) | `[FREE ONLINE]` | https://tanzil.net/download/ | `raw/texts/islam/quran-arabic.txt` |
| Quran — Yusuf Ali English translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/isl/quran/index.htm | `raw/texts/islam/quran-yusuf-ali-en.txt` |
| Quran — Pickthall English translation | `[PUBLIC DOMAIN]` | https://www.gutenberg.org/ebooks/7440 | `raw/texts/islam/quran-pickthall-en.txt` |
| Sahih al-Bukhari (English) | `[FREE ONLINE]` | https://www.sacred-texts.com/isl/bukhari/index.htm | `raw/texts/islam/sahih-bukhari-en.txt` |
| Sahih Muslim (English) | `[FREE ONLINE]` | https://www.sacred-texts.com/isl/ms/index.htm | `raw/texts/islam/sahih-muslim-en.txt` |
| Al-Muwatta — Malik ibn Anas (English) | `[FREE ONLINE]` | https://www.sacred-texts.com/isl/muw/index.htm | `raw/texts/islam/al-muwatta-en.txt` |

#### Classical Commentaries (Tafsir)

| Source | Status | Notes |
|---|---|---|
| *Tafsir al-Tabari* — Ibn Jarir al-Tabari (d. 923) | `[NEEDS SOURCING]` | No complete English translation freely available; Arabic text partially on archive.org |
| *Tafsir al-Kashshaf* — al-Zamakhshari (d. 1144) | `[NEEDS SOURCING]` | No complete English translation in print or online |
| *Tafsir Ibn Kathir* (abridged English) | `[FREE ONLINE]` | Partial English available at https://www.qtafsir.com — download key chapters | `raw/commentaries/islam/ibn-kathir-abridged-en/` |
| *Tafsir al-Mizan* — Tabatabai (Shia) | `[FREE ONLINE]` | English translation at https://www.al-islam.org/al-mizan-exegesis-quran-allamah-sayyid-muhammad-husayn-tabatabai | `raw/commentaries/islam/al-mizan-en/` |
| *Fusus al-Hikam* — Ibn Arabi (d. 1240) | `[NEEDS SOURCING]` | English translations exist (R.W.J. Austin) but are copyrighted |

#### Modern Scholarship

| Source | Status | Notes |
|---|---|---|
| *The Qur'an: A Biography* — Bruce Lawrence | `[NEEDS SOURCING]` | Copyrighted; purchase or library |
| *Introduction to the Qur'an* — Bell & Watt | `[NEEDS SOURCING]` | Copyrighted; purchase or library |
| *The History of the Qur'anic Text* — Al-Azami | `[NEEDS SOURCING]` | Copyrighted; purchase or library |
| *Qur'an and Woman* — Amina Wadud | `[NEEDS SOURCING]` | Copyrighted; purchase or library |

---

### Buddhism

**Schema note**: Requires schema surgery before ingestion. No God, no single canon,
multiple entirely separate canons with no common ancestor text. The Neyartha/Nitartha
distinction (interpretable vs. definitive teachings) has no parallel in the current
schema and must be added as a hermeneutical framework. Add Theravada, Mahayana, and
Vajrayana as sect pages first.

#### Primary Texts

| Source | Status | URL | Save Path |
|---|---|---|---|
| Dhammapada — Buddharakkhita translation | `[FREE ONLINE]` | https://www.accesstoinsight.org/tipitaka/kn/dhp/dhp.intro.budd.html | `raw/texts/buddhism/dhammapada-en.txt` |
| Majjhima Nikaya — Bhikkhu Bodhi translation (selections) | `[FREE ONLINE]` | https://suttacentral.net/mn | `raw/texts/buddhism/majjhima-nikaya-en/` |
| Digha Nikaya (selections) | `[FREE ONLINE]` | https://suttacentral.net/dn | `raw/texts/buddhism/digha-nikaya-en/` |
| Heart Sutra — Conze translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/bud/tib/hrt.htm | `raw/texts/buddhism/heart-sutra-en.txt` |
| Diamond Sutra — A.F. Price translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/bud/tib/diam.htm | `raw/texts/buddhism/diamond-sutra-en.txt` |
| Lotus Sutra — Kern translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/bud/lotus/index.htm | `raw/texts/buddhism/lotus-sutra-kern-en.txt` |
| Bardo Thodol — Evans-Wentz translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/bud/tib/tibdead.htm | `raw/texts/buddhism/bardo-thodol-en.txt` |
| Platform Sutra — Wong Mou-Lam translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/bud/zen/platform.htm | `raw/texts/buddhism/platform-sutra-en.txt` |
| Pali Canon — full text (Pali) | `[FREE ONLINE]` | https://suttacentral.net | `raw/texts/buddhism/pali-canon/` — download key suttas |

#### Classical Commentaries

| Source | Status | URL | Save Path |
|---|---|---|---|
| *Visuddhimagga* — Bhikkhu Nanamoli translation | `[FREE ONLINE]` | https://www.accesstoinsight.org/lib/authors/nanamoli/PathofPurification2011.pdf | `raw/commentaries/buddhism/visuddhimagga-en.pdf` |
| *Mulamadhyamakakarika* — Garfield translation | `[NEEDS SOURCING]` | Copyrighted; purchase or library | — |
| *Bodhicaryavatara* — Wallace & Wallace translation | `[NEEDS SOURCING]` | Copyrighted; purchase or library | — |
| *Bodhicaryavatara* — older Barnett translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/bud/btg/index.htm | `raw/commentaries/buddhism/bodhicaryavatara-barnett-en.txt` |

#### Modern Scholarship

| Source | Status | Notes |
|---|---|---|
| *What the Buddha Taught* — Walpola Rahula | `[NEEDS SOURCING]` | Copyrighted; purchase or library |
| *The Heart of the Buddha's Teaching* — Thich Nhat Hanh | `[NEEDS SOURCING]` | Copyrighted; purchase or library |
| *Buddhist Thought* — Paul Williams | `[NEEDS SOURCING]` | Copyrighted; purchase or library |
| *In the Buddha's Words* — Bhikkhu Bodhi | `[NEEDS SOURCING]` | Copyrighted; purchase or library |

---

## Tier 2 — After Tier 1 Schema Upgrades Are Complete

### Hinduism

**Schema note**: The sect page type must be fully built before ingestion begins.
The Shankaracharya / Ramanujacharya / Madhvacharya commentary triad is a built-in
controversy triad — create the controversy page structure before ingesting any of the three.

#### Primary Texts

| Source | Status | URL | Save Path |
|---|---|---|---|
| Upanishads — Müller translation (12 principal) | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/hin/sbe01/index.htm | `raw/texts/hinduism/upanishads-muller-en/` |
| Bhagavad Gita — Gambhirananda translation | `[NEEDS SOURCING]` | Copyrighted | — |
| Bhagavad Gita — Edwin Arnold translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/hin/gita/index.htm | `raw/texts/hinduism/bhagavad-gita-arnold-en.txt` |
| Brahma Sutras — Thibaut translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/hin/sbe34/index.htm | `raw/texts/hinduism/brahma-sutras-thibaut-en.txt` |
| Yoga Sutras of Patanjali — Johnston translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/hin/yogasutr.htm | `raw/texts/hinduism/yoga-sutras-johnston-en.txt` |

#### Classical Commentaries

| Source | Status | URL | Save Path |
|---|---|---|---|
| Shankaracharya commentary on Brahma Sutras — Thibaut trans. | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/hin/sbe34/index.htm | `raw/commentaries/hinduism/shankara-brahma-sutras-en.txt` |
| Ramanujacharya commentary on Brahma Sutras — Thibaut trans. | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/hin/sbe48/index.htm | `raw/commentaries/hinduism/ramanuja-brahma-sutras-en.txt` |
| Madhvacharya commentary on Brahma Sutras | `[NEEDS SOURCING]` | No complete English translation freely available | — |
| Abhinavagupta commentary on Bhagavad Gita | `[NEEDS SOURCING]` | No complete English translation freely available | — |

#### Modern Scholarship

| Source | Status | Notes |
|---|---|---|
| *A History of Indian Philosophy* — Dasgupta (5 vols.) | `[NEEDS SOURCING]` | Copyrighted; purchase or library |
| *Being Different* — Rajiv Malhotra | `[NEEDS SOURCING]` | Copyrighted; purchase or library |
| *The Hindus: An Alternative History* — Wendy Doniger | `[NEEDS SOURCING]` | Copyrighted; purchase or library |

---

### Daoism

**Schema note**: Add commentary-as-transformation as a hermeneutical approach in
CLAUDE.md before ingesting. Build Wang Bi vs. Heshang Gong controversy structure first.

#### Primary Texts

| Source | Status | URL | Save Path |
|---|---|---|---|
| Daodejing — James Legge translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/tao/taote.htm | `raw/texts/daoism/daodejing-legge-en.txt` |
| Daodejing — D.C. Lau translation | `[NEEDS SOURCING]` | Copyrighted; purchase or library | — |
| Zhuangzi — James Legge translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/tao/sbe39/index.htm | `raw/texts/daoism/zhuangzi-legge-en.txt` |
| Liezi — Lionel Giles translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/tao/lieh/index.htm | `raw/texts/daoism/liezi-giles-en.txt` |

#### Classical Commentaries

| Source | Status | Notes |
|---|---|---|
| Wang Bi commentary on Daodejing | `[NEEDS SOURCING]` | English trans. (Ariane Rump/Chan) copyrighted |
| Heshang Gong commentary on Daodejing | `[NEEDS SOURCING]` | No complete modern English translation freely available |
| Guo Xiang commentary on Zhuangzi | `[NEEDS SOURCING]` | No complete English translation freely available |

#### Modern Scholarship

| Source | Status | Notes |
|---|---|---|
| *The Way of Zhuangzi* — Thomas Merton | `[NEEDS SOURCING]` | Copyrighted; purchase or library |
| *Taoism: The Enduring Tradition* — Russell Kirkland | `[NEEDS SOURCING]` | Copyrighted; purchase or library |

---

## Tier 3 — Later Legs, After Schema Is Mature

### Zoroastrianism

| Source | Status | URL | Save Path |
|---|---|---|---|
| Avesta — Darmesteter translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/zor/index.htm | `raw/texts/zoroastrianism/avesta-darmesteter-en/` |
| Gathas of Zarathustra — various translations | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/zor/gat/index.htm | `raw/texts/zoroastrianism/gathas-en.txt` |
| *Zoroastrianism: An Introduction* — Jenny Rose | `[NEEDS SOURCING]` | Copyrighted; purchase or library | — |

---

### Confucianism

| Source | Status | URL | Save Path |
|---|---|---|---|
| Analects — James Legge translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/cfu/conf1.htm | `raw/texts/confucianism/analects-legge-en.txt` |
| Mencius — James Legge translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/cfu/menc/index.htm | `raw/texts/confucianism/mencius-legge-en.txt` |
| Great Learning & Doctrine of the Mean — Legge | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/cfu/conf1.htm | `raw/texts/confucianism/great-learning-doctrine-mean-en.txt` |
| Zhu Xi — *Collected Commentaries on the Four Books* | `[NEEDS SOURCING]` | No complete English translation freely available | — |

---

### Manichaeism

| Source | Status | Notes |
|---|---|---|
| Manichaean Psalm-Book (fragments) | `[NEEDS SOURCING]` | Scholarly editions only; no free English translation |
| Kephalaia (fragments) | `[NEEDS SOURCING]` | Scholarly editions only |
| *Manichaeism* — Iain Gardner & Samuel Lieu | `[NEEDS SOURCING]` | Copyrighted; purchase or library |

---

### Second Temple Judaism

| Source | Status | URL | Save Path |
|---|---|---|---|
| 1 Enoch — R.H. Charles translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/bib/boe/index.htm | `raw/texts/second-temple-judaism/1-enoch-charles-en.txt` |
| Book of Jubilees — R.H. Charles translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/bib/jub/index.htm | `raw/texts/second-temple-judaism/jubilees-charles-en.txt` |
| Dead Sea Scrolls — Vermes translation selections | `[NEEDS SOURCING]` | Copyrighted; purchase or library | — |
| 4 Ezra / 2 Baruch — R.H. Charles translation | `[PUBLIC DOMAIN]` | https://www.sacred-texts.com/bib/apo/index.htm | `raw/texts/second-temple-judaism/pseudepigrapha-charles-en/` |
| *The Dead Sea Scrolls Today* — James VanderKam | `[NEEDS SOURCING]` | Copyrighted; purchase or library | — |

---

## Schema Flags by Tier

Items that require CLAUDE.md updates before ingestion:

| Tradition | Required Schema Work |
|---|---|
| Islam | Add Sunni/Shia/Sufi sect pages; qira'at controversy page |
| Buddhism | Non-theistic canon model; Neyartha/Nitartha hermeneutical framework; multiple non-ancestral canons |
| Hinduism | Full sect page type required; Advaita/Vishishtadvaita/Dvaita controversy triad structure |
| Daoism | Commentary-as-transformation hermeneutical approach; Wang Bi vs. Heshang Gong controversy structure |
| Zoroastrianism | Influence-tracing page type |
| Manichaeism | Extinct tradition flag; influence-tracing mode |
| Second Temple Judaism | Pseudepigrapha canon status handling |

---

## Outstanding Sources

*This section is maintained by Claude Code. Updated after each download run.
All sources below require manual acquisition. Status flags:*

- `[COPYRIGHT]` — *English translation exists; purchase or source from library*
- `[NO TRANSLATION]` — *No complete English translation exists in print; secondary scholarship is the only option unless a new translation is published*
- `[PARTIAL ONLY]` — *English translation exists but is incomplete, fragmentary, or academically superseded; use with caution*

*Once acquired, place the file in the appropriate `raw/` subdirectory and remove
the entry from this list. Claude Code will not remove entries automatically —
manual confirmation required.*

---

### Islam

| Source | Flag | Recommended Edition / Notes |
|---|---|---|
| *Tafsir al-Tabari* — Ibn Jarir al-Tabari | `[NO TRANSLATION]` | No complete English translation exists. Best workaround: *Al-Tabari: The History* (SUNY Press, 40 vols.) covers his historical writing but not the tafsir. For the exegesis itself, use secondary scholarship: *The Commentary on the Quran* by John Cooper translates Vol. 1 only (Oxford UP, 1987) — source this as a partial. |
| *Tafsir al-Kashshaf* — al-Zamakhshari | `[NO TRANSLATION]` | No complete English translation exists. Partially covered in academic articles. Note in wiki as a significant gap; use secondary descriptions in commentator page. |
| *Fusus al-Hikam* — Ibn Arabi | `[COPYRIGHT]` | R.W.J. Austin translation, *The Bezels of Wisdom* (Paulist Press, 1980). Best available English edition. Out of print but findable secondhand or via library. |
| *The Qur'an: A Biography* — Bruce Lawrence | `[COPYRIGHT]` | Atlantic Books, 2006. Widely available. |
| *Introduction to the Qur'an* — Bell & Watt | `[COPYRIGHT]` | Edinburgh UP, revised ed. 1977. Standard academic introduction; available via university libraries. |
| *The History of the Qur'anic Text* — Al-Azami | `[COPYRIGHT]` | UK Islamic Academy, 2003. May require ordering directly; not always in general libraries. |
| *Qur'an and Woman* — Amina Wadud | `[COPYRIGHT]` | Oxford UP, 1999. Widely available. |

---

### Buddhism

| Source | Flag | Recommended Edition / Notes |
|---|---|---|
| *Mulamadhyamakakarika* — Nagarjuna | `[COPYRIGHT]` | Jay Garfield translation, *The Fundamental Wisdom of the Middle Way* (Oxford UP, 1995). Includes Tibetan commentary by Chandrakirti. The standard scholarly edition. |
| *Bodhicaryavatara* — Shantideva | `[COPYRIGHT]` | Wallace & Wallace translation, *A Guide to the Bodhisattva Way of Life* (Snow Lion, 1997). Preferred over the older Barnett public domain version already downloaded, which is archaic and unreliable. |
| *What the Buddha Taught* — Walpola Rahula | `[COPYRIGHT]` | Grove Press, revised ed. 1974. Thin book, widely available, essential Theravada entry point. |
| *The Heart of the Buddha's Teaching* — Thich Nhat Hanh | `[COPYRIGHT]` | Broadway Books, 1999. Widely available. |
| *Buddhist Thought* — Paul Williams | `[COPYRIGHT]` | Routledge, 2nd ed. 2000. Best single-volume academic survey of Mahayana doctrine. |
| *In the Buddha's Words* — Bhikkhu Bodhi | `[COPYRIGHT]` | Wisdom Publications, 2005. Anthology of Pali Canon selections with scholarly apparatus. Pairs with the SuttaCentral downloads already in `raw/`. |

---

### Hinduism

| Source | Flag | Recommended Edition / Notes |
|---|---|---|
| *Bhagavad Gita* — Gambhirananda translation | `[COPYRIGHT]` | Advaita Ashrama, 1997. Includes Shankaracharya's commentary. Preferred over the Arnold public domain version already downloaded for commentary purposes. |
| Madhvacharya — *Commentary on the Brahma Sutras* | `[NO TRANSLATION]` | No complete scholarly English translation exists. Best available substitute: B.N.K. Sharma, *Brahmasutras and Their Principal Commentaries* (Munshiram Manoharlal, 3 vols.) — covers Madhva's positions in scholarly description rather than direct translation. Source this as secondary scholarship, not primary text. Flag in wiki accordingly. |
| Abhinavagupta — *Gitarthasangraha* (commentary on Bhagavad Gita) | `[NO TRANSLATION]` | No complete modern English translation exists. Boris Marjanovic produced a translation (*Abhinavagupta's Commentary on the Bhagavad Gita*, Indica Books, 2004) but it is rare and academically limited. Source if findable; otherwise use secondary scholarship on Kashmir Shaivism. |
| *A History of Indian Philosophy* — Dasgupta | `[COPYRIGHT]` | Cambridge UP, 5 vols., 1922–1955. Partially in public domain (vols. 1–2 pre-1928); check Project Gutenberg and Internet Archive for downloadable volumes before purchasing. |
| *Being Different* — Rajiv Malhotra | `[COPYRIGHT]` | HarperCollins India, 2011. May require ordering; not always in Western libraries. |
| *The Hindus: An Alternative History* — Wendy Doniger | `[COPYRIGHT]` | Penguin Press, 2009. Widely available. Note: withdrawn from Indian market by publisher in 2014 under legal pressure — relevant context for the controversy page pairing it with Malhotra. |

---

### Daoism

| Source | Flag | Recommended Edition / Notes |
|---|---|---|
| *Daodejing* — D.C. Lau translation | `[COPYRIGHT]` | Penguin Classics, revised ed. 1963. The most reliable scholarly English edition. Prefer this over the Legge public domain version already downloaded for interpretive work — Legge's Victorian English distorts the register of the text. |
| Wang Bi — *Commentary on the Daodejing* | `[COPYRIGHT]` | **Preferred edition**: Richard John Lynn, *The Classic of the Way and Virtue* (Columbia UP, 1999) — integrates Wang Bi's commentary with the text, better apparatus than the Rump/Chan edition. Widely available. The Ariane Rump/Chan edition (*Commentary on the Lao Tzu by Wang Pi*, University of Hawaii Press, 1979) is the alternative but out of print and expensive. |
| Heshang Gong — *Commentary on the Daodejing* | `[NO TRANSLATION]` | No complete modern English translation exists. Eduard Erkes produced a partial German translation (1950); no English equivalent. The gap is real. Best workaround: Alan Chan's secondary scholarship on Heshang Gong in *Two Visions of the Way* (SUNY Press, 1991) — source this as secondary scholarship. |
| Guo Xiang — *Commentary on the Zhuangzi* | `[NO TRANSLATION]` | No standalone English translation exists. Portions appear in Burton Watson's *The Complete Works of Chuang Tzu* (Columbia UP, 1968) as interpolated notes, but not as a distinct commentary text. Flag in wiki as a genuine scholarly gap. |
| *The Way of Zhuangzi* — Thomas Merton | `[COPYRIGHT]` | New Directions, 1965. Widely available. Note: this is a contemplative adaptation, not a scholarly translation — note this distinction in the source's wiki page. |
| *Taoism: The Enduring Tradition* — Russell Kirkland | `[COPYRIGHT]` | Routledge, 2004. Best modern academic survey. Widely available. |

---

### Zoroastrianism

| Source | Flag | Recommended Edition / Notes |
|---|---|---|
| *Zoroastrianism: An Introduction* — Jenny Rose | `[COPYRIGHT]` | I.B. Tauris, 2011. Best accessible modern introduction. Widely available. |
| *The Gathas of Zarathushtra* — Helmut Humbach | `[COPYRIGHT]` | Carl Winter, 2 vols., 1991. The definitive scholarly edition; expensive and specialist. Source via university library if possible. The Darmesteter public domain translation already downloadable covers the broader Avesta but is dated (1880s) — usable as a base text with caveats noted in the wiki. |

---

### Confucianism

| Source | Flag | Recommended Edition / Notes |
|---|---|---|
| Zhu Xi — *Collected Commentaries on the Four Books* | `[NO TRANSLATION]` | No complete English translation exists. Daniel Gardner's *The Four Books: The Basic Teachings of the Later Confucian Tradition* (Hackett, 2007) translates selections with Zhu Xi's commentary — source this as a partial. Gardner's *Zhu Xi's Reading of the Analects* (Columbia UP, 2003) covers the Analects commentary in more depth. Both are `[COPYRIGHT]`. |

---

### Manichaeism

| Source | Flag | Recommended Edition / Notes |
|---|---|---|
| Manichaean Psalm-Book | `[PARTIAL ONLY]` | C.R.C. Allberry, *A Manichaean Psalm-Book Part II* (Stuttgart, 1938) — the standard edition but Coptic/scholarly; no accessible modern English translation. Source via university library as a reference only. |
| Kephalaia | `[PARTIAL ONLY]` | No complete English translation. Iain Gardner, *The Kephalaia of the Teacher* (Brill, 1995) covers a portion. Expensive specialist volume; source via university library. |
| *Manichaeism* — Iain Gardner & Samuel Lieu | `[COPYRIGHT]` | Routledge, 2004. The most accessible English-language introduction with translated source excerpts. Widely available. This is the practical substitute for the untranslated primary texts. |

---

### Second Temple Judaism

| Source | Flag | Recommended Edition / Notes |
|---|---|---|
| Dead Sea Scrolls — complete translation | `[COPYRIGHT]` | **Preferred edition**: Florentino García Martínez, *The Dead Sea Scrolls Translated* (Brill/Eerdmans, 2nd ed. 1996) — more complete than Vermes. Geza Vermes, *The Complete Dead Sea Scrolls in English* (Penguin, revised ed. 2004) is the more accessible alternative. Either works; source whichever is available. |
| *The Dead Sea Scrolls Today* — James VanderKam | `[COPYRIGHT]` | Eerdmans, 2nd ed. 2010. Accessible scholarly introduction. Widely available. |
| *Jewish Literature Between the Bible and the Mishnah* — George Nickelsburg | `[COPYRIGHT]` | Fortress Press, 2nd ed. 2005. Best survey of the pseudepigrapha and Second Temple corpus. Widely available. |

---

## Downloaded Sources

*This section is maintained by Claude Code. Moved here from Outstanding Sources
after successful download. Includes save path and date.*

*(empty — no downloads run yet)*
