# SNIPED_OS STAGING PLAN · 2026-05-18

Plan to stage the 242 unique-to-SNIPED_OS files from `~/Downloads/    SNIPED_OS/` into `~/AI-Brain-Refinery/raw/` for future batch processing.

**Source universe:** `~/Downloads/    SNIPED_OS/` ONLY. (Out of scope: rest of `~/Downloads/`, `~/sniped-media/`, external drives.)
**Destination:** `~/AI-Brain-Refinery/raw/` (existing chapter tree, extended in §1).
**Constraints respected:** No files moved, deleted, renamed, extracted, chunked. No master files updated. Commands below are **recommendations only · do NOT execute as part of this plan**.

Based on: `SNIPED_OS_FULL_SOURCE_INVENTORY_2026-05-18.md` (this morning) · 243 unique basenames resolved to source paths in `/tmp/sos_stage/sos_only_paths2.txt`.

Distribution of the 243 SOS-only files by parent directory:
- 230 at SOS root (loose books + working docs)
- 5 in `04_DELIVERABLES/CH01_yae/cards/` · superseded
- 4 in `04_DELIVERABLES/CH01_yae/` · superseded
- 4 in `_side_quests/dad_flyer/` · side quest

**Late addition (2026-05-18, after first plan draft):** 3 new AI Edge PDFs were added to SOS root and are NOT in the 243 count above. They are handled in §2.25 below. Updated copy count: ~213 files. Future batch slot named `EDGE_AND_OPERATING_DISCIPLINE` added to §6 deferred list.

**Second late addition (2026-05-18, evening):** 2 new docx files were added to SOS root:
- `COURSE WORK 1 thru 2.docx` (63 KB, 18:08) · AI automation agency course transcript covering Phase 1 (AI Opportunity) and Phase 2 (Strategic Positioning) · handled in §2.26.
- `AI CHANGED EVERYTHING.docx` (67 KB, 18:03) · AI history / DeepMind / AlphaGo / human-machine creativity canon · handled in §2.27.

These are SEPARATE FILES (different size, different timestamp, different title). Not a combined transcript. Updated copy count: ~215 files. Future batch slots named `AI_AUTOMATION_AGENCY_COURSE` and `AI_TECH_AND_HUMAN_MACHINE_CREATIVITY` added to §6 deferred list.

**Third late addition (2026-05-18, evening verification pass):** `Finding Your Edge.pdf` (554 KB, 17:21, SOS root) confirmed by the operator as course/operating-discipline material. Classified as `EDGE_AND_OPERATING_DISCIPLINE / AI_AUTOMATION_AGENCY_COURSE`. Staged in §2.26 alongside `COURSE WORK 1 thru 2.docx` into `raw/05_AI_EDGE_COURSE/`. Updated copy count: ~216 files.

**Fourth late addition (2026-05-18, 19:38 · post-staging-commit):** `MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx` (15.6 KB, SOS root) · transcript material for an 8-lesson Claude Code operating-layer course. NOT in the 2026-05-18 staging commit (`01b05e9`). Handled in §2.28 below. Updated copy count target if authorized: 217 files. Future batch slot added to §6 as BATCH_030 · `CLAUDE_CODE_OPERATING_LAYER`.

**Filename note:** The file lands on disk as `MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx` with a doubled `.docx.docx` extension (Word save artifact). The operator should decide whether to keep the doubled extension on the staged copy or rename to a single `.docx` at copy-time. Default recommendation: keep verbatim during staging (no rename in transit) and rename at extraction time if it breaks tooling.

**Late-addition verification (2026-05-18, evening · all 7 named files confirmed):**

| File | SOS root | Active cp block | Staged in commit `01b05e9`? |
|---|---|---|---|
| `COURSE WORK 1 thru 2.docx` | ✓ | §2.26 → `raw/05_AI_EDGE_COURSE/` | yes |
| `AI CHANGED EVERYTHING.docx` | ✓ | §2.27 → `raw/08_AI_TECH/ai_history_case_studies/` | yes |
| `Finding Your Edge.pdf` | ✓ | §2.26 → `raw/05_AI_EDGE_COURSE/` | yes |
| `ICP Definition Worksheet.pdf` | ✓ | §2.25 → `raw/13_OPERATING_DISCIPLINE/` | yes |
| `Setting Goals.pdf` | ✓ | §2.25 → `raw/13_OPERATING_DISCIPLINE/` | yes |
| `Weekly Reflections.pdf` | ✓ | §2.25 → `raw/13_OPERATING_DISCIPLINE/` | yes |
| `MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx` | ✓ | §2.28 → `raw/05_AI_EDGE_COURSE/claude_code/` | **NO · added post-commit, pending authorization** |

Six of seven late-addition files are present and committed. The seventh (`MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx`) is pending a second staging-copy authorization.

---

## 0 · Reading guide

This plan has four parts:

1. **§1 Target structure** · the proposed `mkdir` block. New subfolders under `raw/02_TIER_1_CANON_BOOKS/` and `raw/03_TIER_2_CANON_BOOKS/` to absorb 130+ new books without flattening.
2. **§2 Copy plan** · one `cp` block per destination subfolder, with exact source filenames quoted.
3. **§3 Ignore / defer list** · explicit files NOT being staged (stale lock files, .part fragments, superseded cards, side-quest PNGs, installers, internal duplicates).
4. **§4-§6** · internal duplicate decisions, post-staging verification, recommended next 5 batches.

**All commands use:**
```bash
SRC="$HOME/Downloads/    SNIPED_OS"
DST="$HOME/AI-Brain-Refinery/raw"
```

Quote `SRC` exactly because the folder has 4 leading spaces.

**Total copy count after this plan: ~217 files (210 from the 243 unique pile + 3 first-late-added AI Edge PDFs + 2 second-late-added docx files + 1 third-late-added course PDF + 1 fourth-late-added Claude Code course docx). Ignore / defer count: ~33 files plus 1 new lock file. No unrouted candidates remain.**

**Commit status:** 216 of the 217 files have been staged and committed in `01b05e9 stage SNIPED_OS source expansion into raw`. The 1 fourth-late-addition (`MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx`) is NOT in that commit · it requires a second staging-copy authorization to land.

---

## 1 · Target raw subfolder structure

Recommended `mkdir` block. Existing chapter dirs (00_BRIEF, 01_OFFERS, etc.) are untouched.

```bash
SRC="$HOME/Downloads/    SNIPED_OS"
DST="$HOME/AI-Brain-Refinery/raw"

# Tier 1 sub-categorization (new)
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/photography"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/advertising"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/ai_tech"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/culture"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/strategy_history"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/sales_positioning"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/operating_founder"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/network_distribution"

# Tier 2 sub-categorization (new)
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/persuasion_psych"
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/decision_judgment"
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/consulting_service"
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/leadership_mgmt"
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/investing_finance"
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/memoirs_biographies"
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/fashion_luxury"
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/systems_thinking"
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/operator_engine_community"
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/expertise_creativity"

# Reference + intake (new)
mkdir -p "$DST/10_REFERENCE/_intake_2026-05-18"
mkdir -p "$DST/10_REFERENCE/_intake_2026-05-18/automations"
mkdir -p "$DST/10_REFERENCE/photography_scans"

# Web (extracted from the 3 SOS website zips)
mkdir -p "$DST/14_WEB/website-copy"
mkdir -p "$DST/14_WEB/website-seo"
mkdir -p "$DST/14_WEB/website-design"

# AI Edge / operating-discipline course materials (late addition · see §2.25)
mkdir -p "$DST/13_OPERATING_DISCIPLINE"
# Optional: if ICP Definition Worksheet is preferred as course material instead of operating discipline,
# replace the line above with:
#   mkdir -p "$DST/05_AI_EDGE_COURSE"
# and route ICP Definition Worksheet.pdf there. See §2.25 for the trade-off.

# AI Edge course transcripts (second late addition · see §2.26)
mkdir -p "$DST/05_AI_EDGE_COURSE"

# AI history / human-machine creativity canon (second late addition · see §2.27)
mkdir -p "$DST/08_AI_TECH/ai_history_case_studies"
# Note: 08_BOOK already occupies the 08_ slot. See §1 numbering-collision note below.
# Alternative routings if strict chapter-number uniqueness matters:
#   mkdir -p "$DST/16_AI_TECH/ai_history_case_studies"
# Then mirror the destination updates in §2.27 accordingly.

# Art series (raw/09_ART_SERIES is currently empty in raw)
# (No mkdir needed · 09_ART_SERIES exists. Just populate it.)
```

**Note on duplicates of existing flat-tier book filenames:** The 19 books already in `raw/02_TIER_1_CANON_BOOKS/` (BATCH_002 sources) stay where they are. They do NOT need to be re-sorted into the new subfolders for this batch · BATCH_002 chunks reference their current paths. New books from this staging pass go into the subfolders; old books stay at the flat root. (Optional cleanup pass later · do not bundle with this staging.)

**Note on the new `13_OPERATING_DISCIPLINE/` chapter slot:** The `13_` prefix already belongs to `raw/13_NETWORK/`. Creating `raw/13_OPERATING_DISCIPLINE/` alongside it gives two sibling chapters both prefixed `13_`. The filesystem allows this and the chapter is staged per operator instruction · but if strict chapter-number uniqueness matters, rename to `raw/15_OPERATING_DISCIPLINE/` (next free slot · 11_LEGAL, 12_FINANCIAL, 13_NETWORK, 14_WEB are all occupied, 15+ are free) before any batch reads from the folder. Same caveat applies to the new `05_AI_EDGE_COURSE/` (`05_` is occupied by `05_PRODUCTION`) and the new `08_AI_TECH/` (`08_` is occupied by `08_BOOK`).

**Numbering-collision summary for late-additions:**

| Proposed path | Conflicts with | Clean alternative |
|---|---|---|
| `raw/05_AI_EDGE_COURSE/` | `raw/05_PRODUCTION/` | `raw/15_AI_EDGE_COURSE/` |
| `raw/08_AI_TECH/` | `raw/08_BOOK/` | `raw/16_AI_TECH/` |
| `raw/13_OPERATING_DISCIPLINE/` | `raw/13_NETWORK/` | `raw/15_OPERATING_DISCIPLINE/` |

The operator's literal naming is preserved in the cp blocks below. If you choose to rename to clean slots before any batch reads from these folders, do a single global rename pass · cheaper than letting batches encode the collided paths.

---

## 2 · Copy plan by destination

### 2.1 · `raw/02_TIER_1_CANON_BOOKS/photography/` · 14 files · HIGH PRIORITY (BATCH_005 feeds here)

```bash
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/photography"
cp -p \
  "$SRC/John Szarkowski - William Eggleston's Guide (2002, The Museum of Modern Art, New York) - libgen.li.pdf" \
  "$SRC/Shore Stephen. - Uncommon Places_ The Complete Works - libgen.li.pdf" \
  "$SRC/Stephen Shore - The Nature Of Photographs (2007, Phaidon Press) - libgen.li.pdf" \
  "$SRC/Annie Leibovitz - Annie Leibovitz at Work (2008, Random House) - libgen.li.epub" \
  "$SRC/Roland Barthes - Camera Lucida_ Reflections on Photography (1982, Hill and Wang) - libgen.li.epub" \
  "$SRC/Sontag, Susan - On Photography (2012) - libgen.li.pdf" \
  "$SRC/Michael Freeman - The Photographer's Eye_ Composition and Design for Better Digital Photos (2007, Focal Press) - libgen.li.mobi" \
  "$SRC/Michael Freeman - The Photographer's Vision_ Understanding and Appreciating Great Photography (2011, Elsevier Science_ Focal Press) - libgen.li.epub" \
  "$SRC/Jonathan Day - Robert Frank's 'The Americans' _ The Art of Documentary Photography (2011, Intellect Books) - libgen.li.epub" \
  "$SRC/Norma Stevens, Steven M. L. Aronson - Avedon_ Something Personal (2017, Spiegel & Grau) - libgen.li.epub" \
  "$SRC/[Voices That Matter] Jay Maisel - Light, Gesture, and Color (2014, New Riders) - libgen.li.epub" \
  "$SRC/_OceanofPDF.com_Pharrell_Places_and_Spaces_Ive_Been_-_Pharrell_Williams.pdf" \
  "$SRC/_OceanofPDF.com_The_Operator_-_Tom_King.pdf" \
  "$SRC/Marcellas Reynolds - Supreme Models_ Iconic Black Women Who Revolutionized Fashion (2019, Abrams) - libgen.li.epub" \
  "$DST/02_TIER_1_CANON_BOOKS/photography/"
```

### 2.2 · `raw/10_REFERENCE/photography_scans/` · 5 files · low-fidelity scanned PDFs

```bash
mkdir -p "$DST/10_REFERENCE/photography_scans"
cp -p \
  "$SRC/257683787-Cartier-Bresson-H-1952-the-Decisive-Moment.pdf" \
  "$SRC/367490464-Szarkowski-1973-Looking-at-Photographs-pdf.pdf" \
  "$SRC/pdfcoffee.com_ernst-haas-pdf-free.pdf" \
  "$SRC/pdfcoffee.com_virgil-abloh-figures-of-speech-pdf-free.pdf" \
  "$SRC/713434459-Core-Studio-Public-Lecture-Virgil-Abloh-Insert-Complicated-Title-Here-English.txt" \
  "$DST/10_REFERENCE/photography_scans/"
```

### 2.3 · `raw/09_ART_SERIES/` · already empty · populate from existing SOS roots

The Art_Series_*.md and Study_*.md files exist in SOS root and are already in BATCH_001 in normalized form (`Study_AnnieLeibovitz.md`, `Study_ErnstHaas.md`). The 9-file set still belongs in `raw/09_ART_SERIES/` for the photography canon batch to read from.

```bash
cp -p \
  "$SRC/Art_Series_1_RichardAvedon.md" \
  "$SRC/Art_Series_2_WilliamEggleston.md" \
  "$SRC/Art_Series_3_AnnieLeibovitz.md" \
  "$SRC/Art_Series_4_StephenShore.md" \
  "$SRC/Art_Series_5_FredHerzog.md" \
  "$SRC/Art_Series_6_RobertFrank.md" \
  "$SRC/Art_Series_7_JoelMeyerowitz.md" \
  "$SRC/Art_Series_8_GracielaIturbide.md" \
  "$SRC/Art_Series_9_ErnstHaas.md" \
  "$SRC/Art_Series.docx" \
  "$SRC/Study_AnnieLeibovitz.md" \
  "$SRC/Study_ErnstHaas.md" \
  "$SRC/Study_FredHerzog.md" \
  "$SRC/Study_GracielaIturbide.md" \
  "$SRC/Study_JoelMeyerowitz.md" \
  "$SRC/Study_RichardAvedon.md" \
  "$SRC/Study_RobertFrank.md" \
  "$SRC/Study_StephenShore.md" \
  "$SRC/Study_WilliamEggleston.md" \
  "$DST/09_ART_SERIES/"
```

**Note:** these files are NOT in the 242-unique-to-SOS list (they share basenames with raw via the SOS legacy mirror). They appear in `comm` as in-common · but `raw/09_ART_SERIES/` is empty, so they need to be physically populated there before BATCH_005 reads from it. Verify they are missing from `raw/09_ART_SERIES/` before running. Also ignore `Art_Series_6_RobertFrank (1).md` (the `(1)` suffix dup).

### 2.4 · `raw/02_TIER_1_CANON_BOOKS/advertising/` · 7 files

```bash
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/advertising"
cp -p \
  "$SRC/David Ogilvy_ Alan Parker - Confessions of an Advertising Man (2004, Southbank Publishing) - libgen.li.pdf" \
  "$SRC/ Claude C. Hopkins - Scientific Advertising (2010, www.snowballpublishing.com) - libgen.li.pdf" \
  "$SRC/Eugene M. Schwartz - Breakthrough Advertising (2004) - libgen.li.pdf" \
  "$SRC/ Whitman, Drew Eric - Cashvertising_ How to Use More Than 100 Secrets of Ad-Agency Psychology to Make Big Money Selling Anything to Anyone (2009, Career Press) - libgen.li.epub" \
  "$SRC/[Adweek Series] Luke Sullivan - Hey, Whipple, Squeeze This_ A Guide to Creating Great Advertising (2008, Wiley) - libgen.li.pdf" \
  "$SRC/Robert W. Bly - The copywriter's handbook_ a step-by-step guide to writing copy that sells (2006, Henry Holt) - libgen.li.mobi" \
  "$SRC/[Journal of Advertising 1998-dec vol. 27 iss. 4] Jon Steel, Truth, Lies and Advertising , Wiley, 1998{Burns, Neal M.}(1998 December)[10.1080_00913367.1998.10673571]{61156666} libgen.li.pdf" \
  "$DST/02_TIER_1_CANON_BOOKS/advertising/"
```

### 2.5 · `raw/02_TIER_1_CANON_BOOKS/ai_tech/` · 12 files

```bash
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/ai_tech"
cp -p \
  "$SRC/Balaji Srinivasan - The Network State - libgen.li.pdf" \
  "$SRC/Chris Dixon - Read Write Own_ Building the Next Era of the Internet (2024, Random House) - libgen.li.epub" \
  "$SRC/Ajay Agrawal, Joshua Gans, Avi Goldfarb - Power and Prediction_ The Disruptive Economics of Artificial Intelligence (2022, Harvard Business Review Press) - libgen.li.epub" \
  "$SRC/Ajay Agrawal, Joshua Gans, Avi Goldfarb - Prediction Machines_ The Simple Economics of Artificial Intelligence (2018, Harvard Business Review Press) - libgen.li.epub" \
  "$SRC/Daugherty, Paul R._Wilson, H. James - Human + machine_ reimagining work in the age of AI (2018, Harvard Business Review Press) - libgen.li.epub" \
  "$SRC/Karim R. Lakhani_Marco Iansiti - Competing in the Age of AI_ Strategy and Leadership When Algorithms and Networks Run the World (2020, Harvard Business Review Press) - libgen.li.epub" \
  "$SRC/Mustafa Suleyman_Michael Bhaskar__ Michael Bhaskar - The Coming Wave _ Technology, Power, and the Twenty-first Century's Greatest Dilemma (2023, Penguin Random House LLC) - libgen.li.epub" \
  "$SRC/Ethan Mollick - Co-Intelligence_ Living and Working With AI (2024, Penguin Publishing Group) - libgen.li.epub" \
  "$SRC/max-tegmark-life-30-being-human-in-the-age-of-artificial-intelligence-alfred-a-knopf-2017-aTvn.pdf" \
  "$SRC/Erik Brynjolfsson, Andrew McAfee, Jeff Cummings - The Second Machine Age_ Work, Progress, and Prosperity in a Time of Brilliant Technologies (2014, Brilliance Audio on MP3-CD) - libgen.li.mobi" \
  "$SRC/ Thomas H. Davenport, Julia Kirby - Only Humans Need Apply_ Winners and Losers in the Age of Smart Machines (2016, HarperBusiness) - libgen.li.rar" \
  "$SRC/ Christopher Steiner - Automate This_ How Algorithms Came to Rule Our World (2012, Penguin Group, USA_Portfolio Hardcover) - libgen.li.epub" \
  "$DST/02_TIER_1_CANON_BOOKS/ai_tech/"
```

**Note on the .rar:** The Davenport file is structurally an EPUB despite the .rar extension. The corpus extraction pipeline should treat it as zip-EPUB. Optionally rename on copy:
```bash
mv "$DST/02_TIER_1_CANON_BOOKS/ai_tech/ Thomas H. Davenport, Julia Kirby - Only Humans Need Apply_ Winners and Losers in the Age of Smart Machines (2016, HarperBusiness) - libgen.li.rar" \
   "$DST/02_TIER_1_CANON_BOOKS/ai_tech/ Thomas H. Davenport, Julia Kirby - Only Humans Need Apply_ Winners and Losers in the Age of Smart Machines (2016, HarperBusiness) - libgen.li.epub"
```

### 2.6 · `raw/02_TIER_1_CANON_BOOKS/culture/` · 7 files · feeds Lineage Doctrine

```bash
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/culture"
cp -p \
  "$SRC/Dan Charnas - Dilla Time_ The Life and Afterlife of J Dilla, the Hip-Hop Producer Who Reinvented Rhythm (2022, Farrar, Straus and Giroux) - libgen.li.epub" \
  "$SRC/Dan Charnas - The Big Payback_ The History of the Business of Hip-Hop (2010, NAL) - libgen.li.epub" \
  "$SRC/Rick Ross_ Neil Martinez-Belkin - Hurricanes_ A Memoir (2019, Hanover Square Press) - libgen.li.epub" \
  "$SRC/Gucci Mane, Neil Martinez-Belkin - The Autobiography of Gucci Mane (2017, Simon & Schuster) - libgen.li.epub" \
  "$SRC/Jay-Z Decoded{Jay-Z}(2010, Random House Publishing Group){108293762} libgen.li.epub" \
  "$SRC/Zack O'Malley Greenburg - Empire State of Mind_ How Jay-Z Went from Street Corner to Corner Office (2011, Portfolio _ Penguin) - libgen.li.epub" \
  "$SRC/Marcellas Reynolds - Supreme Models_ Iconic Black Women Who Revolutionized Fashion (2019, Abrams) - libgen.li.epub" \
  "$DST/02_TIER_1_CANON_BOOKS/culture/"
```

**Note:** Supreme Models also appears as `Supreme Models_ Iconic Black Women Who Revolutionized Fashion.epub` at SOS root (no author prefix). Pick the libgen-prefixed version (canonical filename). Same file. See §4.

### 2.7 · `raw/02_TIER_1_CANON_BOOKS/strategy_history/` · 14 files

```bash
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/strategy_history"
cp -p \
  "$SRC/Greene, Robert - Mastery (2013_2012, Penguin Group_ Penguin Books_Viking Adult) - libgen.li.epub" \
  "$SRC/[Laws of Human Nature] Robert Greene - The Laws of Human Nature (2019, VIKING) - libgen.li.pdf" \
  "$SRC/50 Cent, Robert Greene - The 50th Law (2009, Harper) - libgen.li.mobi" \
  "$SRC/[Oxford World's Classics] Carl von Clausewitz, Beatrice Heuser - On War (2007, Oxford University Press, USA) - libgen.li.pdf" \
  "$SRC/Niccolo Machiavelli - The prince (2008, Hackett Pub. Co) - libgen.li.pdf" \
  "$SRC/[Dover books on history, political and social science] Niccolo Machiavelli, Ninian Hill Thomson - Discourses on Livy (2007, Dover Publications) - libgen.li.pdf" \
  "$SRC/[Shambhala Dragon Editions] Miyamoto Musashi - The Book of Five Rings (1993, Shambhala) - libgen.li.djvu" \
  "$SRC/[Classics] Arrian - The Campaigns of Alexander (2003, Penguin Books Ltd) - libgen.li.azw3" \
  "$SRC/Donald W. Engels - Alexander the Great and the Logistics of the Macedonian Army (2020, University of California Press) [10.1525_9780520352162] - libgen.li.pdf" \
  "$SRC/Herodotus, Robert B. Strassler[ed] - The Landmark Herodotus_ Histories (2007, 2009, Anchor Books) - libgen.li.epub" \
  "$SRC/Thucydides, Robert B. Strassler, Richard Crawley, Victor Davis H - The Landmark Thucydides_ A Comprehensive Guide to the Peloponnesian War (1998, Free Press) - libgen.li.epub" \
  "$SRC/LandmarkCaesarWebEssays_5Jan2018.pdf" \
  "$SRC/Marcus Aurelius - Meditations - libgen.li.epub" \
  "$SRC/Emperor of the French Napoleon I_ Frankreich Kaiser Napoléon I._ - Napoleon _ a life (2014, Penguin Group_Viking) - libgen.li.epub" \
  "$DST/02_TIER_1_CANON_BOOKS/strategy_history/"
```

### 2.8 · `raw/02_TIER_1_CANON_BOOKS/sales_positioning/` · 17 files

```bash
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/sales_positioning"
cp -p \
  "$SRC/Alex Hormozi - \$100M Offers_ How To Make Offers So Good People Feel Stupid Saying No (2021) - libgen.li.epub" \
  "$SRC/Alex Hormozi - \$100M Leads_ How to Get Strangers To Want To Buy Your Stuff (2023) - libgen.li.epub" \
  "$SRC/Raz, Tahl_Voss, Chris - Never Split the Difference_ Negotiating As If Your Life Depended On It (2016, HarperBusiness) - libgen.li.epub" \
  "$SRC/Fitzpatrick, Rob - The Mom Test_ How to talk to customers & learn if your business is a good idea when everyone is lying to you (2016) - libgen.li.azw3" \
  "$SRC/Dunford, April - Obviously Awesome (2019) - libgen.li.epub" \
  "$SRC/ Adam Morgan - Eating the Big Fish_ How Challenger Brands Can Compete Against Brand Leaders (2009) - libgen.li.pdf" \
  "$SRC/ Jack Trout, Steve Rivkin - Differentiate or Die_ Survival in Our Era of Killer Competition (2008) - libgen.li.pdf" \
  "$SRC/ Geoffrey A. Moore - Crossing the Chasm, 3rd Edition_ Marketing and Selling Disruptive Products to Mainstream Customers (2014, HarperBusiness) - libgen.li.mobi" \
  "$SRC/ Christensen, Clayton M. & Dillon, Karen & Hall, Taddy & Duncan, - Competing Against Luck_ The Story of Innovation and Customer Choice (2016) - libgen.li.epub" \
  "$SRC/The Innovator&_039_s Dilemma_ When New Technologies Cause Great Firms to Fail (Management of Innovatio...{Clayton M. Christensen}(2013, Harvard Business Review Press){113262812} libgen.li.pdf" \
  "$SRC/Al Ramadan, Dave Peterson, Christopher Lochhead, Kevin Maney - Play Bigger_ How Pirates, Dreamers, and Innovators Create and Dominate Markets (2016, HarperBusiness) - libgen.li.epub" \
  "$SRC/Seth Godin - Purple Cow_ Transform Your Business by Being Remarkable (2003, Portfolio Hardcover) - libgen.li.pdf" \
  "$SRC/Seth Godin - This Is Marketing_ You Can't Be Seen Until You Learn to See (2018, Penguin Publishing Group_ Portfolio_Penguin_Portfolio) - libgen.li.pdf" \
  "$SRC/Seth Godin - Tribes_ We Need You to Lead Us (2008, Penguin) - libgen.li.epub" \
  "$SRC/Donald Miller - Building a StoryBrand_ Clarify Your Message So Customers Will Listen (2017, HarperCollins Leadership) - libgen.li.mobi" \
  "$SRC/ Chip Heath, Dan Heath - Made to Stick_ Why Some Ideas Survive and Others Die (2007, Random House) - libgen.li.pdf" \
  "$SRC/[Made to Stick ] Heath, Chip _ Heath, Dan - Made to Stick - libgen.li.mobi" \
  "$DST/02_TIER_1_CANON_BOOKS/sales_positioning/"
```

**Note:** Made to Stick appears in BATCH_002 already as the Hit Makers-adjacent reference but not as its own source. Both formats (PDF + mobi) staged for the dedicated chunking pass.

### 2.9 · `raw/02_TIER_1_CANON_BOOKS/operating_founder/` · 11 files

```bash
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/operating_founder"
cp -p \
  "$SRC/Eric Ries - The Lean Startup How Todays Entrepreneurs Use Continuous Innovation To Create Radically Successful Businesses (2017_2011, Crown Business) - libgen.li.pdf" \
  "$SRC/Ben Horowitz - The Hard Thing About Hard Things_ Building a Business When There Are No Easy Answers (2014, HarperBusiness) - libgen.li.epub" \
  "$SRC/[Blitzscaling] Reid Hoffman, Chris Yeh, Bill Gates - Blitzscaling_ The Lightning-Fast Path to Building Massively Valuable Companies (2018, Currency) - libgen.li.epub" \
  "$SRC/[Kauffman Foundation Series on Innovation and Entrepreneurship] Noam Wasserman - The Founder's Dilemmas_ Anticipating and Avoiding the Pitfalls That Can Sink a Startup (2012, Princeton University Press) - libgen.li.epub" \
  "$SRC/Michael E. Gerber - The E-Myth Revisited_ Why Most Small Businesses Don't Work and What to Do About It (1995, HarperCollins) - libgen.li.mobi" \
  "$SRC/John Warrillow - Built to Sell_ Turn Your Business Into One You Can Sell (2010) - libgen.li.pdf" \
  "$SRC/Amp It Up{Frank Slootman}(2022, Wiley){112881352} libgen.li.pdf" \
  "$SRC/Gabriel Weinberg, Justin Mares - Traction_ a startup guide to getting customers (2014, S-curves Publishing) - libgen.li.epub" \
  "$SRC/Eliyahu, Goldratt - The goal_ a process of ongoing improvement (2004, North River Press) - libgen.li.pdf" \
  "$SRC/Jeffrey Liker - The Toyota Way, Second Edition_ 14 Management Principles from the World's Greatest Manufacturer (2020, McGraw-Hill Education) - libgen.li.pdf" \
  "$SRC/Michael Hammer_ James Champy - Reengineering the corporation _ a manifesto for business revolution (2001, HarperBusiness) - libgen.li.pdf" \
  "$DST/02_TIER_1_CANON_BOOKS/operating_founder/"
```

### 2.10 · `raw/02_TIER_1_CANON_BOOKS/network_distribution/` · 5 files

```bash
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/network_distribution"
cp -p \
  "$SRC/Chris Anderson - Long Tail, The, Revised and Updated Edition_ Why the Future of Business is Selling Less of More (2008, Hyperion) - libgen.li.epub" \
  "$SRC/Chris Anderson - Free_ The Future of a Radical Price (Abridged) (2009, Random House Business Books) - libgen.li.pdf" \
  "$SRC/Kevin Kelly - The Inevitable_ Understanding the 12 Technological Forces That Will Shape Our Future (2016, Viking) - libgen.li.epub" \
  "$SRC/Kevin Kelly - New Rules for the New Economy_ 10 Radical Strategies for a Connected World (1999) - libgen.li.pdf" \
  "$SRC/XcMwr2sETldxuEwaZeEw_The+Great+Online+Game+-+Not+Boring+by+Packy+McCormick.pdf" \
  "$DST/02_TIER_1_CANON_BOOKS/network_distribution/"
```

### 2.11 · `raw/03_TIER_2_CANON_BOOKS/persuasion_psych/` · 8 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/persuasion_psych"
cp -p \
  "$SRC/ ROBERT B. CIALDINI - Influence (Harper collins) - libgen.li.pdf" \
  "$SRC/ Robert Cialdini - Pre-Suasion_ A Revolutionary Way to Influence and Persuade (2016, Simon & Schuster) - libgen.li.epub" \
  "$SRC/Dan Ariely - Predictably Irrational_ The Hidden Forces That Shape Our Decisions (2010, Harper Perennial) - libgen.li.djvu" \
  "$SRC/ Will Storr - The Status Game_ On Social Position and How We Use It (2021, William Collins) - libgen.li.epub" \
  "$SRC/ W. David Marx - Status and Culture_ How Our Desire for Social Rank Creates Taste, Identity, Art, Fashion, and Constant Change (2022, Viking) - libgen.li.epub" \
  "$SRC/ Richard Shotton - The Choice Factory_ 25 Behavioural Biases That Influence What We Buy (2018, Harriman House) - libgen.li.epub" \
  "$SRC/ Rory Sutherland - Alchemy_ The Dark Art and Curious Science of Creating Magic in Brands, Business, and Life (2019, William Morrow) - libgen.li.epub" \
  "$SRC/ Jonah Berger - Contagious_ Why Things Catch On (2013, Simon & Schuster) - libgen.li.mobi" \
  "$DST/03_TIER_2_CANON_BOOKS/persuasion_psych/"
```

### 2.12 · `raw/03_TIER_2_CANON_BOOKS/decision_judgment/` · 12 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/decision_judgment"
cp -p \
  "$SRC/Daniel Kahneman - Thinking, Fast and Slow (2011, Farrar, Straus and Giroux) - libgen.li.mobi" \
  "$SRC/Sunstein, Cass R._ Sibony, Olivier_ Kahneman, Daniel - Noise_ A Flaw in Human Judgment (2021, Little, Brown and Company) - libgen.li.pdf" \
  "$SRC/ Gardner, Dan_Tetlock, Philip Eyrikson - Superforecasting_ The Art and Science of Prediction (2015, Crown_Archetype_ Crown Publishers) - libgen.li.epub" \
  "$SRC/ Nate Silver - The Signal and the Noise_ Why So Many Predictions Fail-but Some Don't (2012, Penguin Press HC, The) - libgen.li.epub" \
  "$SRC/ Joseph Campbell - The Hero with a Thousand Faces (2020, Joseph Campbell Foundation) - libgen.li.epub" \
  "$SRC/ Blake Snyder - Save The Cat! The Last Book on Screenwriting You'll Ever Need (2005, Michael Wiese Productions) - libgen.li.pdf" \
  "$SRC/ John Truby - The Anatomy of Story_ 22 Steps to Becoming a Master Storyteller (2008, Faber & Faber) - libgen.li.pdf" \
  "$SRC/Story{Robert McKee}{115577124} libgen.li.pdf" \
  "$SRC/Viktor E. Frankl - Man's search for meaning (2000, Beacon Press) - libgen.li.pdf" \
  "$SRC/[Free Press Paperback] Ernest Becker - The Denial of Death (1997, Free Press) - libgen.li.djvu" \
  "$SRC/Eric Hoffer - The true believer_ Thoughts on the nature of mass movements (1980, Time-Life Books) - libgen.li.epub" \
  "$SRC/Eric Berne - Games People Play_ The Basic Handbook of Transactional Analysis. (1996, Ballantine Books) - libgen.li.epub" \
  "$DST/03_TIER_2_CANON_BOOKS/decision_judgment/"
```

Also stage these political-psychology adjacent titles in the same folder (4 files):

```bash
cp -p \
  "$SRC/Gustave Le Bon - The crowd_ a study of the popular mind (2001, Dover Publications) - libgen.li.pdf" \
  "$SRC/Greg Lukianoff, Jonathan Haidt - The Coddling of the American Mind_ How Good Intentions and Bad Ideas Are Setting up a Generation for Failure (2018, Penguin Press) - libgen.li.pdf" \
  "$SRC/Jonathan Haidt - The Righteous Mind_ Why Good People Are Divided by Politics and Religion (2012, Pantheon) - libgen.li.azw3" \
  "$SRC/Giải trí đến chết (Amusing Ourselves to Death_ Public Discourse in the Age of Show Business){Neil Postman_ Andrew Postman (giới thiệu)_ Nhung Nguyễn (dịch)}(2022, Nhà xuất bản Thanh Niên - 1980 Books){10812373….epub" \
  "$DST/03_TIER_2_CANON_BOOKS/decision_judgment/"
```

**Note:** The Postman is a Vietnamese-language translation. The extraction pipeline should detect and skip-or-language-tag accordingly. Stage as-is; flag during BATCH planning.

### 2.13 · `raw/03_TIER_2_CANON_BOOKS/consulting_service/` · 8 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/consulting_service"
cp -p \
  "$SRC/ Kaufman, Josh - The Personal MBA_ Master the Art of Business (2010, Portfolio Hardcover) - libgen.li.epub" \
  "$SRC/Ethan M. Rasiel - The McKinsey Way_ Using the Techniques of the World's Top Strategic Consultants to Help You and Your Business (1999, McGraw-Hill) [10.1036_0071368833] - libgen.li.pdf" \
  "$SRC/Maister, David H. - Managing the professional service firm (1997, Free Press Paperbacks) - libgen.li.pdf" \
  "$SRC/Peter Block - Flawless consulting_ a guide to getting your expertise used (2000, Jossey-Bass_Pfeiffer) - libgen.li.epub" \
  "$SRC/Alan Weiss, Alan Weiss - Million Dollar Consulting_ The Professional's Guide to Growing a Practice (2002, McGraw-Hill) - libgen.li.pdf" \
  "$SRC/Alan Weiss - Value-Based Fees_ How to Charge - and Get - What You're Worth (Ultimate Consultant (Pfeiffer)) (2008, Pfeiffer) - libgen.li.pdf" \
  "$SRC/Patrick Lencioni - The advantage _ why organizational health trumps everything else in business (2012, Jossey-Bass) - libgen.li.pdf" \
  "$SRC/Patrick Lencioni - Getting Naked_ A Business Fable About Shedding The Three Fears That Sabotage Client Loyalty (J-B Lencioni Series) (2010) - libgen.li.pdf" \
  "$DST/03_TIER_2_CANON_BOOKS/consulting_service/"
```

### 2.14 · `raw/03_TIER_2_CANON_BOOKS/leadership_mgmt/` · 8 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/leadership_mgmt"
cp -p \
  "$SRC/[Andrew_S._Grove]_High_Output_Management(z-lib.org).pdf" \
  "$SRC/Jocko Willink, Leif Babin - Extreme Ownership_ How U.S. Navy SEALs Lead and Win (2015, St. Martin's Press) - libgen.li.mobi" \
  "$SRC/Jocko Willink_ Leif Babin - The Dichotomy of Leadership_ Balancing the Challenges of Extreme Ownership to Lead and Win (2018, St. Martin's Press) - libgen.li.epub" \
  "$SRC/John Doerr - Measure What Matters_ How Google, Bono, and the Gates Foundation Rock the World with OKRs (2018, Portfolio) - libgen.li.epub" \
  "$SRC/L. David Marquet - Turn the Ship Around! - A True Story of Turning Followers into Leaders (2013, Portfolio) - libgen.li.epub" \
  "$SRC/Kim Scott - Radical Candor_ Be a Kick-Ass Boss Without Losing Your Humanity (2017, St. Martin's Press) - libgen.li.epub" \
  "$SRC/Goodwin, Doris Kearns - Leadership_ In Turbulent Times (2018, Simon & Schuster) - libgen.li.epub" \
  "$SRC/Goodwin, Doris Kearns - Team of rivals_ the political genius of Abraham Lincoln (2013, Editora Record) - libgen.li.azw3" \
  "$DST/03_TIER_2_CANON_BOOKS/leadership_mgmt/"
```

**Note:** SOS has 2 copies of High Output Management (`(z-lib.org).pdf` and `(z-lib.org)-2.pdf`). Pick the non-suffixed copy. See §4.

Also stage the culture-of-teams adjacents:

```bash
cp -p \
  "$SRC/ Daniel Coyle - The Culture Code_ The Secrets of Highly Successful Groups (2018, Bantam) - libgen.li.epub" \
  "$SRC/[J-B Lencioni Series] Patrick Lencioni - Death by Meeting_ A Leadership Fable...About Solving the Most Painful Problem in Business (2004, Jossey-Bass) - libgen.li.txt" \
  "$DST/03_TIER_2_CANON_BOOKS/leadership_mgmt/"
```

### 2.15 · `raw/03_TIER_2_CANON_BOOKS/investing_finance/` · 14 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/investing_finance"
cp -p \
  "$SRC/ Benjamin Graham - The Intelligent Investor_ The Definitive Book on Value Investing. A Book of Practical Counsel (2003, Collins Business) - libgen.li.pdf" \
  "$SRC/[Security Analysis Prior Editions] Benjamin Graham, David Dodd, Warren Buffett - Security Analysis_ Sixth Edition, Foreword by Warren Buffett (2008, McGraw-Hill) [10.1036_0071592539] - libgen.li.pdf" \
  "$SRC/Seth A. Klarman - Margin of Safety_ Risk-Averse Value Investing Strategies for the Thoughtful Investor (1991, HarperCollins) - libgen.li.pdf" \
  "$SRC/Howard Marks - The most important thing_ uncommon sense for the thoughtful investor (2011, Columbia University Press) - libgen.li.pdf" \
  "$SRC/Howard Marks - Mastering the Market Cycle_ Getting the Odds on Your Side (2018, Houghton Mifflin Harcourt) - libgen.li.epub" \
  "$SRC/Schroeder, Alice - The Snowball_ Warren Buffett and the Business of Life (2008, Bantam) - libgen.li.pdf" \
  "$SRC/Warren E. Buffett, Lawrence A. Cunningham, Lawrence A. Cunningha - The Essays of Warren Buffett_ Lessons for Corporate America, Third Edition (2013, Carolina Academic Press) - libgen.li.epub" \
  "$SRC/ Charles T. Munger, Peter D. Kaufman, Ed Wexler, Warren E. Buffet - Poor Charlie's Almanack_ The Wit and Wisdom of Charles T. Munger (2005, Walsworth Publishing Company) - libgen.li.pdf" \
  "$SRC/Morgan Housel - The Psychology of Money Timeless Lessons on Wealth Greed and Happiness - libgen.li.pdf" \
  "$SRC/Sebastian Mallaby - The Power Law _ Venture Capital and the Making of the New Future (2022, Penguin Publishing Group) - libgen.li.epub" \
  "$SRC/Jason Kelly - The New Tycoons_ Inside the Trillion Dollar Private Equity Industry That Owns Everything (2012, Bloomberg Press) - libgen.li.azw3" \
  "$SRC/David Carey, John E. Morris - King of Capital_ The Remarkable Rise, Fall, and Rise Again of Steve Schwarzman and Blackstone (2010, Crown Business) - libgen.li.epub" \
  "$SRC/Christopher Leonard - The Lords of Easy Money_ How the Federal Reserve Broke the American Economy (2022) - libgen.li.epub" \
  "$SRC/James Dale Davidson_ William Rees-Mogg - The sovereign individual _ how to survive and thrive during the collapse of the welfare state (1997, Simon & Schuster) - libgen.li.pdf" \
  "$DST/03_TIER_2_CANON_BOOKS/investing_finance/"
```

**Note:** Mallaby exists as both .epub and .pdf in SOS. Stage the epub (better text extraction); pdf is redundant duplicate. See §4.
**Note:** Munger's Almanack already exists in raw as the .epub via BATCH_002. The .pdf is a richer (184 MB) version with images. Stage as supplement, NOT as replacement.

### 2.16 · `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` · 17 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/memoirs_biographies"
cp -p \
  "$SRC/Walter Isaacson - Elon Musk (2023, Simon & Schuster) - libgen.li.epub" \
  "$SRC/Ron Chernow - Grant (2017, Penguin Publishing Group) - libgen.li.epub" \
  "$SRC/Ron Chernow - Titan_ The Life of John D. Rockefeller, Sr. (2004, Vintage) - libgen.li.mobi" \
  "$SRC/Ron Chernow - Washington_ A Life - libgen.li.pdf" \
  "$SRC/ Sam Walton - Sam Walton_ Made In America (1993, Bantam) - libgen.li.pdf" \
  "$SRC/ Ray Kroc - Grinding It Out_ The Making of McDonald's (2016, St. Martin's Paperbacks) - libgen.li.epub" \
  "$SRC/ Howard Schultz, Joanne Gordon - Onward_ How Starbucks Fought for Its Life without Losing Its Soul (2011, Rodale Books) - libgen.li.mobi" \
  "$SRC/Howard Schultz, Dori Jones Yang - Pour Your Heart Into It_ How Starbucks Built a Company One Cup at a Time (1997, Hyperion) - libgen.li.mobi" \
  "$SRC/Akio Morita, Edwin M. Reingold, Mitsuko Shimomura - Made in Japan_ Akio Morita and Sony (1986, E. P. Dutton) - libgen.li.pdf" \
  "$SRC/Richard Branson - Losing My Virginity_ How I Survived, Had Fun, and Made a Fortune Doing Business My Way (2011, Crown Business) - libgen.li.epub" \
  "$SRC/Marc Randolph - That Will Never Work (2019, Little, Brown and Company) - libgen.li.epub" \
  "$SRC/ Sarah Frier - No Filter_ The Inside Story of Instagram (2020, Simon & Schuster) - libgen.li.epub" \
  "$SRC/Mike Isaac - Super Pumped_ The Battle for Uber (2019, W. W. Norton Company) - libgen.li.epub" \
  "$SRC/Leigh Gallagher - The Airbnb Story_ How Three Ordinary Guys Disrupted an Industry, Made Billions . . . and Created Plenty of Controversy (2017, Houghton Mifflin Harcourt) - libgen.li.epub" \
  "$SRC/Petre, Peter_Schwarzenegger, Arnold - Total recall_ my unbelievably true life story (2012, Simon & Schuster) - libgen.li.epub" \
  "$SRC/Coddington, Grace - Grace_ A Memoir (2012, Random House Publishing Group) - libgen.li.epub" \
  "$SRC/ Vreeland, Diana - D.V. (2011, HarperCollins) - libgen.li.epub" \
  "$DST/03_TIER_2_CANON_BOOKS/memoirs_biographies/"
```

Also stage these media/entertainment operator biographies:

```bash
cp -p \
  "$SRC/James Andrew Miller - Tinderbox_ HBO's Ruthless Pursuit of New Frontiers (Henry Holt and Co.) - libgen.li.mobi" \
  "$SRC/James Andrew Miller, Tom Shales - Those Guys Have All the Fun_ Inside the World of ESPN (2011, Little, Brown and Company) - libgen.li.epub" \
  "$SRC/Tom Shales, James Andrew Miller - Live From New York_ An Uncensored History of Saturday Night Live, as Told By Its Stars, Writers and Guests (2003, Back Bay Books) - libgen.li.epub" \
  "$SRC/David Rensin - The Mailroom -- Hollywood History from the Bottom Up (2003, Ballantine Books _ The Random House Publishing Group) - libgen.li.djvu" \
  "$SRC/ Fredric Dannen - Hit men_ power brokers and fast money inside the music business (1991, Vintage Books) - libgen.li.pdf" \
  "$SRC/ Rich Cohen - The Fish That Ate the Whale_ The Life and Times of America's Banana King (2012, Farrar, Straus and Giroux) - libgen.li.mobi" \
  "$DST/03_TIER_2_CANON_BOOKS/memoirs_biographies/"
```

### 2.17 · `raw/03_TIER_2_CANON_BOOKS/fashion_luxury/` · 8 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/fashion_luxury"
cp -p \
  "$SRC/ Christian Dior - Dior by Dior- The Autobiography of Christian Dior - libgen.li.pdf" \
  "$SRC/ Christian Dior - The little dictionary of fashion (2007, V & A Publications) - libgen.li.epub" \
  "$SRC/ Dana Thomas - Deluxe_ How Luxury Lost Its Luster (2008, Penguin Books) - libgen.li.epub" \
  "$SRC/ Jean-Noel Kapferer, Vincent Bastien - The Luxury Strategy_ Break the Rules of Marketing to Build Luxury Brands (2009, Kogan Page) - libgen.li.pdf" \
  "$SRC/ Agins, Teri - The end of fashion_ how marketing changed the clothing business forever (1999_2000, HarperCollins_Quill) - libgen.li.epub" \
  "$SRC/ Alicia Drake - The Beautiful Fall_ Fashion, Genius, and Glorious Excess in 1970s Paris (2009, Little, Brown and Company) - libgen.li.mobi" \
  "$SRC/ André Leon Talley - The Chiffon Trenches_ A Memoir (2020, Random House Publishing Group) - libgen.li.epub" \
  "$SRC/[Fashion Theory The Journal of Dress Body &amp_ Culture 2019-sep 11 vol. 24 iss. 3] Virgil Abloh_ \"Figures of Speech\"{Peters, Lauren Downing}(2019 September 11)[10.1080_1362704x.2019.1655998]{83133693} libgen.li.pdf" \
  "$DST/03_TIER_2_CANON_BOOKS/fashion_luxury/"
```

### 2.18 · `raw/03_TIER_2_CANON_BOOKS/systems_thinking/` · 5 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/systems_thinking"
cp -p \
  "$SRC/ Peter M. Senge - The Fifth Discipline_ The Art & Practice of The Learning Organization (1994, Doubleday Business) - libgen.li.pdf" \
  "$SRC/ Meadows, Donella H. Wright, Diana - Thinking in Systems_ A Primer - libgen.li.pdf" \
  "$SRC/ Atul Gawande - The Checklist Manifesto_ How to Get Things Right (2009, Metropolitan Books) - libgen.li.epub" \
  "$SRC/ Marshall McLuhan - Understanding media (1995, MIT Press) - libgen.li.pdf" \
  "$SRC/ Marshall McLuhan, Lewis H. Lapham - Understanding Media_ The Extensions of Man (1994, The MIT Press) - libgen.li.pdf" \
  "$DST/03_TIER_2_CANON_BOOKS/systems_thinking/"
```

**Note:** Two McLuhan PDFs are different editions of the same work · stage both; pick one for the chunking pass.

### 2.19 · `raw/03_TIER_2_CANON_BOOKS/expertise_creativity/` · 6 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/expertise_creativity"
cp -p \
  "$SRC/Anders Ericsson, Robert Pool - Peak_ Secrets from the New Science of Expertise (2016, Eamon Dolan_Houghton Mifflin Harcourt) - libgen.li.epub" \
  "$SRC/Geoff Colvin - Talent Is Overrated_ What Really Separates World-Class Performers from Everybody Else (2008, Portfolio Hardcover) - libgen.li.pdf" \
  "$SRC/Mihaly Csikszentmihalyi - Creativity_ Flow and the Psychology of Discovery and Invention (1996, Harpercollins) - libgen.li.djvu" \
  "$SRC/ Lovell, Sophie - Dieter Rams_ As Little Design as Possible (2011, Phaidon Press) - libgen.li.epub" \
  "$SRC/ Rick Rubin - The Creative Act_ A Way of Being (2023, Penguin Publishing Group) - libgen.li.epub" \
  "$SRC/ John Berger - Ways of Seeing (2008, Penguin Books Ltd) - libgen.li.epub" \
  "$DST/03_TIER_2_CANON_BOOKS/expertise_creativity/"
```

### 2.20 · `raw/03_TIER_2_CANON_BOOKS/operator_engine_community/` · 4 files

```bash
mkdir -p "$DST/03_TIER_2_CANON_BOOKS/operator_engine_community"
cp -p \
  "$SRC/Bailey Richardson_ Kai Elmer Sotto_ Kevin Huynh - Get Together_ How to build a community with your people (2019, Stripe Press) - libgen.li.mobi" \
  "$SRC/David Spinks - The Business of Belonging_ How to Build Communities That Grow the Bottom Line (2021, Wiley) - libgen.li.epub" \
  "$SRC/1000-true-fans-kevin-kellydocx_compress.pdf" \
  "$SRC/ Vaynerchuk, Gary - Jab, jab, jab, right hook how to tell your story in a noisy, social world (2013, Harper Business, an imprint of HarperCollins Publishers) - libgen.li.epub" \
  "$DST/03_TIER_2_CANON_BOOKS/operator_engine_community/"
```

### 2.21 · `raw/10_REFERENCE/_intake_2026-05-18/` · 7 working drafts (Cat L)

```bash
mkdir -p "$DST/10_REFERENCE/_intake_2026-05-18"
cp -p \
  "$SRC/ai-ops-dashboard-prd.md" \
  "$SRC/astro claude websites 3x faster.docx" \
  "$SRC/Built an AI SaaS in 20 min.docx" \
  "$SRC/CLAUDE CODE PLUGIN.docx" \
  "$SRC/CLAUDE CODE SUPERPOWERS.docx" \
  "$SRC/REMOTION.docx" \
  "$SRC/youtube skool doc.docx" \
  "$DST/10_REFERENCE/_intake_2026-05-18/"
```

**Note:** `ai-ops-dashboard-prd (1).md` is a near-duplicate of `ai-ops-dashboard-prd.md`. Pick the unsuffixed copy unless content diff says otherwise.

### 2.22 · `raw/10_REFERENCE/_intake_2026-05-18/automations/` · 3 JSONs (Cat M)

```bash
mkdir -p "$DST/10_REFERENCE/_intake_2026-05-18/automations"
cp -p \
  "$SRC/AI Content Strategy Generator - Lead Magnet.json" \
  "$SRC/Blueprint - ElevenLabs Agent That Calls & Qualifies Leads.json" \
  "$DST/10_REFERENCE/_intake_2026-05-18/automations/"
```

**Note:** `AI Content Strategy Generator - Lead Magnet (1).json` is a duplicate of the unsuffixed copy. Skip the (1) copy.

### 2.23 · `raw/14_WEB/website-{copy,seo,design}/` · 3 archive extractions (1 mkdir, then 3 unzips)

The 3 website zips inside SOS need extraction into `raw/14_WEB/`. Inventoried contents in `SNIPED_OS_FULL_SOURCE_INVENTORY_2026-05-18.md` §3.2 / §3.3 / §3.4.

```bash
mkdir -p "$DST/14_WEB"
cd "$DST/14_WEB"
unzip "$SRC/website-copy.zip"
unzip "$SRC/website-seo.zip"
unzip "$SRC/website-design.zip"
cd -
```

The zips themselves are NOT copied · only their contents are extracted into `raw/14_WEB/`. The originals stay in SOS as the archived source.

### 2.24 · Additional miscellaneous (root-level reference files)

```bash
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/operating_founder"  # already created above
cp -p \
  "$SRC/document.pdf" \
  "$SRC/index.html" \
  "$DST/10_REFERENCE/_intake_2026-05-18/"
```

**Note:** `document.pdf` and `index.html` are unnamed/generic; their value can only be assessed by reading. Stage cautiously; review before chunking. `OfDVDVbyMD.html` and `index (1).html` are defer (see §3.4).

### 2.25 · `raw/13_OPERATING_DISCIPLINE/` · 3 AI Edge PDFs (LATE ADDITION 2026-05-18)

Three AI Edge course PDFs were added to SOS root after the initial 243-file inventory was taken. They sit at:

- `~/Downloads/    SNIPED_OS/ICP Definition Worksheet.pdf` · 670 KB · added 2026-05-18 17:48
- `~/Downloads/    SNIPED_OS/Setting Goals.pdf` · 444 KB · added 2026-05-18 17:49
- `~/Downloads/    SNIPED_OS/Weekly Reflections.pdf` · 405 KB · added 2026-05-18 17:49

All three are course/operating-discipline source material. Per operator instruction, they belong in `raw/13_OPERATING_DISCIPLINE/`. ICP Definition Worksheet could alternatively live in `raw/05_AI_EDGE_COURSE/` if the operator prefers to separate course content from recurring operating-hygiene material · but for this plan all three are staged together in `raw/13_OPERATING_DISCIPLINE/` to keep the future `EDGE_AND_OPERATING_DISCIPLINE` batch source bundle unified.

```bash
mkdir -p "$DST/13_OPERATING_DISCIPLINE"
cp -p \
  "$SRC/ICP Definition Worksheet.pdf" \
  "$SRC/Setting Goals.pdf" \
  "$SRC/Weekly Reflections.pdf" \
  "$DST/13_OPERATING_DISCIPLINE/"
```

**Optional alternative routing for ICP Definition Worksheet** (if separating course material from operating discipline matters):

```bash
# Instead of staging all three together, route ICP Definition into a dedicated course folder:
mkdir -p "$DST/05_AI_EDGE_COURSE"
cp -p "$SRC/ICP Definition Worksheet.pdf" "$DST/05_AI_EDGE_COURSE/"
# Then stage only Goals + Reflections into 13_OPERATING_DISCIPLINE:
cp -p \
  "$SRC/Setting Goals.pdf" \
  "$SRC/Weekly Reflections.pdf" \
  "$DST/13_OPERATING_DISCIPLINE/"
```

**Classification:** Future batch candidate · `EDGE_AND_OPERATING_DISCIPLINE` (see §6).
**Not in BATCH_005 photography canon.**

**Why these matter for SNIPED:**
- *ICP Definition Worksheet* feeds the `sniped-wwp-positioning` skill and the locked ICP work for the Reset $1,500 floor. ICP refinement is a recurring discipline (quarterly review during Constraint Audit), not one-time setup.
- *Setting Goals* + *Weekly Reflections* feed the drift-detection nested loops (daily HLQ / weekly review / monthly metric / quarterly audit / annual 10-year test) named in BATCH_004 canon item 10. Direct alignment with the existing operating spine, not new doctrine.
- All three are operating-discipline scaffolding, not strategic canon. They are tooling for the operator to run the spine that already exists. Stage them, give them their own batch (`EDGE_AND_OPERATING_DISCIPLINE`), but do NOT inflate their canonical weight relative to the locked CANONICAL_TRUTHS / WWP / Direction Stack.

### 2.26 · `raw/05_AI_EDGE_COURSE/` · COURSE WORK 1 thru 2.docx + Finding Your Edge.pdf (SECOND + THIRD LATE ADDITIONS 2026-05-18)

Two files: the AI automation agency course transcript (Phase 1 + Phase 2) and the Phase-1 Edge handout that accompanies it.

- `~/Downloads/    SNIPED_OS/COURSE WORK 1 thru 2.docx` · 63 KB · added 2026-05-18 18:08
- `~/Downloads/    SNIPED_OS/Finding Your Edge.pdf` · 554 KB · added 2026-05-18 17:21

```bash
mkdir -p "$DST/05_AI_EDGE_COURSE"
cp -p \
  "$SRC/COURSE WORK 1 thru 2.docx" \
  "$SRC/Finding Your Edge.pdf" \
  "$DST/05_AI_EDGE_COURSE/"
```

**Routing alternatives (per operator's note):**

```bash
# Alt 1: keep alongside the §2.25 operating-discipline worksheets
cp -p "$SRC/COURSE WORK 1 thru 2.docx" "$DST/13_OPERATING_DISCIPLINE/"

# Alt 2: clean slot (no numbering collision)
mkdir -p "$DST/15_OPERATING_DISCIPLINE"
cp -p "$SRC/COURSE WORK 1 thru 2.docx" "$DST/15_OPERATING_DISCIPLINE/"

# Alt 3: under AI tech as course transcripts subfolder
mkdir -p "$DST/08_AI_TECH/course_transcripts"
cp -p "$SRC/COURSE WORK 1 thru 2.docx" "$DST/08_AI_TECH/course_transcripts/"
```

**Default recommendation:** stage in `raw/05_AI_EDGE_COURSE/` to separate course transcript canon from recurring operator-hygiene worksheets (which stay in `raw/13_OPERATING_DISCIPLINE/`). This split maps cleanly to the two future batches: `AI_AUTOMATION_AGENCY_COURSE` reads from `05_AI_EDGE_COURSE/`, and `EDGE_AND_OPERATING_DISCIPLINE` reads from both folders.

**Classification:**
- AI automation agency course canon
- Phase 1: AI Opportunity
- Phase 2: Strategic Positioning
- Edge / ICP / offer / one-liner pitch / goals / execution foundation

**Future batch candidates (both apply):**
- `AI_AUTOMATION_AGENCY_COURSE` (primary)
- `EDGE_AND_OPERATING_DISCIPLINE` (secondary · the source also informs the worksheets in §2.25)

**Not in BATCH_005 photography canon.**

**Finding Your Edge.pdf classification (confirmed by operator 2026-05-18 evening):**
- Feeds future batch `EDGE_AND_OPERATING_DISCIPLINE` (Phase 1 Edge handout maps to ICP refinement + the recurring weekly/quarterly review loops in §2.25)
- Feeds future batch `AI_AUTOMATION_AGENCY_COURSE` (Phase 1 AI Opportunity handout maps to the transcript's Phase 1 section)
- Stays paired with `COURSE WORK 1 thru 2.docx` in the same folder so chunking can cross-reference handout to transcript section in one pass

### 2.27 · `raw/08_AI_TECH/ai_history_case_studies/` · AI CHANGED EVERYTHING.docx (SECOND LATE ADDITION 2026-05-18)

One file: AI history and case-study canon covering DeepMind, AlphaGo, and the human-machine creativity arc.

- `~/Downloads/    SNIPED_OS/AI CHANGED EVERYTHING.docx` · 67 KB · added 2026-05-18 18:03

```bash
mkdir -p "$DST/08_AI_TECH/ai_history_case_studies"
cp -p \
  "$SRC/AI CHANGED EVERYTHING.docx" \
  "$DST/08_AI_TECH/ai_history_case_studies/"
```

**Numbering-collision alternative:**

```bash
# Clean slot (no collision with 08_BOOK)
mkdir -p "$DST/16_AI_TECH/ai_history_case_studies"
cp -p "$SRC/AI CHANGED EVERYTHING.docx" "$DST/16_AI_TECH/ai_history_case_studies/"
```

**Classification:** AI history / DeepMind / AlphaGo / human-machine creativity canon. SEPARATE from `raw/02_TIER_1_CANON_BOOKS/ai_tech/` (which holds the 12 AI/tech books from §2.5 · Balaji, Dixon, Agrawal ×2, Daugherty, Lakhani, Suleyman, Mollick, Tegmark, Brynjolfsson, Davenport, Steiner). The `08_AI_TECH/` chapter slot is for AI history and case studies (narrative, primary-source events), while `02_TIER_1_CANON_BOOKS/ai_tech/` is for canonical AI books. Two distinct lanes.

**Doctrine tags (per operator's note):**
- AlphaGo / DeepMind
- Move 37
- Lee Sedol move 78
- human-machine creativity
- AI as mirror
- AI expanding human taste and strategy
- machine-discovered non-human moves
- human resilience against machine pressure
- good human + machine doctrine

**Why this matters for SNIPED:**
- Directly reinforces the hybrid-operator stance per `intel_ai_sentiment.md` (LOCKED) · AlphaGo's Move 37 is the canonical proof that AI expands human taste rather than replacing it.
- Lee Sedol's move 78 is the canonical proof of human resilience under machine pressure · feeds `intel_trust_mechanics.md` and the defensive Cat B / hybrid stance.
- "AI as mirror" + "good human + machine" doctrine pair directly to the locked `feedback_edit_register_bifurcation.md` rule (identity holds, world/styling can be AI-augmented) and to BATCH_004 canon item 6 (Camp B AI routing rule).
- Counter-balances the Fastlane / Content Rewards intel note (`future_sources/FASTLANE_CONTENT_REWARDS_INTELLIGENCE_2026-05-18.md`) · gives SNIPED a primary-source AI history corpus to draw from when defending against the mass-distribution / synthetic-influencer lane.

**Future batch candidate:** `AI_TECH_AND_HUMAN_MACHINE_CREATIVITY` (primary).

Secondary read path: chunks from this file should be cross-referenced in BATCH_008 (`raw/02_TIER_1_CANON_BOOKS/ai_tech/`) processing when the corresponding canon books (Mollick · Co-Intelligence, Suleyman · Coming Wave, Tegmark · Life 3.0, Davenport · Only Humans Need Apply) are chunked · same intellectual territory, different surface.

**Not in BATCH_005 photography canon.**

**Verification reminder:** Treat `COURSE WORK 1 thru 2.docx` (§2.26) and `AI CHANGED EVERYTHING.docx` (§2.27) as SEPARATE FILES. They are not the same file under different names · confirmed by size (63 KB vs 67 KB), timestamp (18:08 vs 18:03), and title. Do not deduplicate the two during staging or chunking.

### 2.28 · `raw/05_AI_EDGE_COURSE/claude_code/` · MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx (FOURTH LATE ADDITION 2026-05-18 · POST-COMMIT)

One file: transcript material from an 8-lesson Claude Code operating-layer course.

- `~/Downloads/    SNIPED_OS/MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx` · 15.6 KB · added 2026-05-18 19:38

**Lessons covered:**
1. What is Claude Code & Why You Should Care
2. CLI Demystified · Terminal Basics for Non-Devs
3. Installing Claude Code Step-by-Step
4. Your First Session & Understanding Permissions
5. CLAUDE.md · Teaching Claude About Your Projects
6. Essential Commands, Costs & Context Management
7. Plan Mode, PRDs & MRDs · Think Before You Code
8. GitHub Basics · Version Control & PR Reviews

```bash
mkdir -p "$DST/05_AI_EDGE_COURSE/claude_code"
cp -p \
  "$SRC/MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx" \
  "$DST/05_AI_EDGE_COURSE/claude_code/"
```

**Routing alternatives (per operator's note):**

```bash
# Alt 1: keep course material separate from the §2.25 worksheets, but in a clean chapter slot
mkdir -p "$DST/15_OPERATING_DISCIPLINE/claude_code"
cp -p "$SRC/MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx" "$DST/15_OPERATING_DISCIPLINE/claude_code/"

# Alt 2: rename at copy-time to drop the doubled .docx.docx extension
cp -p "$SRC/MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx" \
      "$DST/05_AI_EDGE_COURSE/claude_code/MASTER CLAUDE CODE COURSE 1 thru 8.docx"
```

**Default recommendation:** stage in `raw/05_AI_EDGE_COURSE/claude_code/` (subfolder under the existing AI Edge course chapter). Keep the doubled `.docx.docx` extension verbatim during staging · rename only at extraction time if it breaks tooling. Maintains symmetry with `COURSE WORK 1 thru 2.docx` (§2.26) and `Finding Your Edge.pdf` (§2.26) which also live under `05_AI_EDGE_COURSE/`.

**Classification:**
- Claude Code operating-layer course canon
- Agentic workflow
- CLI basics
- Permissions
- CLAUDE.md / AGENTS.md
- Context management
- `/clear` and `/compact` discipline
- PRD / MRD planning
- Git / GitHub / version control
- PR review workflow
- Local app build workflow

**Future batch candidates (in priority order):**
1. `CLAUDE_CODE_OPERATING_LAYER` (primary) · own batch · direct primary-source feed to the locked operating-layer files in `~/AI-Brain-Refinery/AGENTS.md` and `CLAUDE.md` + the 6 skills under `.claude/skills/`.
2. `AI_AUTOMATION_AGENCY_COURSE` (secondary · pair with `COURSE WORK 1 thru 2.docx` from §2.26 if chunking the course canon as one pass).
3. `EDGE_AND_OPERATING_DISCIPLINE` (tertiary · operator-tooling reference layer).

**Not in BATCH_005 photography canon.**

**Cross-reference:** when chunked, the lessons map directly to the existing operating-layer spec:
- Lessons 1-4 → ground the AGENTS.md "what to read at session start" + drift-prevention rules.
- Lesson 5 (CLAUDE.md) → ground the `.claude/skills/` invocation pattern and the import-not-duplicate principle (`@AGENTS.md`).
- Lesson 6 (commands, costs, context) → ground the `/clear` rule and the `/session-save` skill purpose.
- Lesson 7 (plan / PRD / MRD) → ground the locked 7-step SOP (inventory → plan → authorize → stage → extract → chunk + validate → consolidate + save).
- Lesson 8 (Git / GitHub / PRs) → ground the 6-commit history pattern (init operating layer → 4 imports → staging checkpoint).

The transcript is the primary source for the canonical operating layer that already lives in the repo. Chunking it makes the rationale behind the spec searchable.

---

## 3 · Ignore / defer list (NOT copied)

### 3.1 · Stale Office lock files (3) · permanent ignore

| File | Reason |
|---|---|
| `~$FIGMA.docx` | Word lock file. Auto-generated. Safe to delete from SOS at any point. |
| `~$iped figma.docx` | Same. Safe to delete. |
| `~$STER CLAUDE CODE COURSE 1 thru 8.docx.docx` | Word lock file sitting next to `MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx` (§2.28). Indicates Word currently has or recently had the master file open. Safe to delete once Word is closed. Never stage. |

### 3.2 · Incomplete browser downloads (3) · ignore (completed siblings being staged)

| File | Reason |
|---|---|
| `Coddington, Grace - Grace_ A Memoir (2012, Random House Publishing Group) - libgen.k58BBVFb.li.epub.part` | Completed sibling `Coddington, Grace - Grace_ A Memoir ... - libgen.li.epub` is being staged. |
| `Petre, Peter_Schwarzenegger, Arnold - Total recall_ my unbelievably true life story (2012, Simon & Schuster) - libgen.EMtzD5ez.li.epub.part` | Completed sibling `... - libgen.li.epub` is being staged. |
| `Gabriel Weinberg, Justin Mares - Traction_ a startup guide to getting customers (2014, S-curves Publishing) - libgen._3TBhCeq.li.epub.part` | Completed sibling `... - libgen.li.epub` is being staged. |

### 3.3 · Superseded chapter cards (9 PNGs) · ignore

Live in `04_DELIVERABLES/CH01_yae/` and `04_DELIVERABLES/CH01_yae/cards/`. Replaced by `raw/_archive/chapter_cards/CH01_Yae_2026-05-13/` per the B&W Card Dual-Register rule locked 2026-05-13.

| File | Path |
|---|---|
| `CARD · 4_5 · LIGHT · STANDARD-1.png` | `04_DELIVERABLES/CH01_yae/` |
| `CARD · 4_5 · LIGHT · STANDARD.png` | `04_DELIVERABLES/CH01_yae/` |
| `CARD · 4_5 · LIGHT · STANDARD@4x.png` | `04_DELIVERABLES/CH01_yae/` |
| `FLYER · 4_5 MASTER.png` | `04_DELIVERABLES/CH01_yae/` |
| `yae_card_4x5_LIGHT.png` | `04_DELIVERABLES/CH01_yae/cards/` |
| `yae_card_4x5_LIGHT_v3_archival.png` | `04_DELIVERABLES/CH01_yae/cards/` |
| `yae_card_4x5_LIGHT_v3_final.png` | `04_DELIVERABLES/CH01_yae/cards/` |
| `yae_card_4x5_LIGHT_v3_FINAL_3qtr.png` | `04_DELIVERABLES/CH01_yae/cards/` |
| `yae_card_9x16_STORY.png` | `04_DELIVERABLES/CH01_yae/cards/` |

### 3.4 · Side quest PNGs (4) · ignore (not SNIPED corpus)

| File |
|---|
| `_side_quests/dad_flyer/coach_eric_jones_welcome_v1.png` |
| `_side_quests/dad_flyer/coach_eric_jones_welcome_v2.png` |
| `_side_quests/dad_flyer/coach_eric_jones_welcome_v3_with_headshot.png` |
| `_side_quests/dad_flyer/coach_eric_jones_welcome_FINAL.png` |

Personal-favor flyer work. Not corpus material. Optional mirror to `raw/_archive/side_quests/` if archival traceability matters; not blocking.

### 3.5 · Application installers (3 DMGs) · ignore (not corpus)

| File |
|---|
| `Flow-v1.5.339.dmg` |
| `Obsidian-1.12.7.dmg` |
| `VSCode-darwin-universal.dmg` |

Software installers. Move out of SOS into a `~/Apps_Installers/` folder at convenience.

### 3.6 · Defer until reviewed (3 HTMLs · low signal)

| File | Note |
|---|---|
| `OfDVDVbyMD.html` | Unnamed export. Review before staging. |
| `index (1).html` | Dup of `index.html`. Pick one. |
| `Da'Nielle Green's Resume.pdf` | Third-party resume. Not SNIPED corpus. |

### 3.7 · The 4 zip archives (Lightroom presets + 3 website packs) · partial

| Archive | Disposition |
|---|---|
| `05_PRODUCTION/_preset_backups/SNIPED_PRESETS.zip` | Pre-v2/v3 preset snapshot. Loose .xmp files (v1, v2, v3 LUXURY, Hero, Proof, BW, Cultural Doc) already in raw. **Do not stage the zip.** |
| `website-copy.zip` | Extract into `raw/14_WEB/website-copy/`. See §2.23. |
| `website-seo.zip` | Extract into `raw/14_WEB/website-seo/`. See §2.23. |
| `website-design.zip` | Extract into `raw/14_WEB/website-design/`. See §2.23. |

### 3.8 · Books NOT staged (deferred personal-finance / out-of-scope · 7 files)

| File | Reason |
|---|---|
| `[Rich Dad] Robert T. Kiyosaki ... - libgen.li (1).epub` + `.epub` + `.pdf` | Personal-finance canon. Low signal for SNIPED (premium service business). Defer. |
| `[For Dummies] Eric Tyson, Margaret A. Munro - Taxes For Dummies_ 2024 Edition` | Reference, not canon. Defer to financial-prep batch if ever. |
| `[J.K. Lasser's Your Income Tax 2016] J.K. Lasser Institute - ... 2015 Tax Return` | Same. Outdated tax doc. Defer. |
| `[Rich Dad Advisors] Tom Wheelwright - Tax-Free Wealth_ ...` | Same. Defer. |
| ` Anderson, Rodney - Credit 911_ ...` | Same. Defer. |
| ` Bolt, Chandler - Published_ ...` | Self-publishing how-to. Lower priority than Direction Stack book canon. Defer. |
| ` Carnegie, Dale - Dale Carnegie's lifetime plan for success_ ...` | Already adjacent to canon. Defer. |
| ` Lara Casey - Make It Happen_ ...` | Self-help. Defer. |
| ` Jon Acuff - Quitter_ ...` | Career advice. Defer. |
| ` Goldratt, Eliyahu` already in operating section · OK |
| ` Sowell, Thomas - Basic Economics` | Reference, low load-bearing. Defer. |
| `-Alison Freer ... compressed.pdf`, `-Alison Lumbatis ... compressed.pdf`, `-Christian Dior ... compressed.pdf`, `-Jeffrey Liker ... compressed.pdf`, `-Rees, Anuschka ... compressed.pdf`, `-Sowell, Thomas ... compressed.pdf` | These are URL-encoded duplicate compressions of full-quality copies already being staged. Skip the `-compressed.pdf` set entirely. |

### 3.9 · Fashion / costume design books · deferred 6 files

| File | Reason |
|---|---|
| ` Alan Flusser - Dressing the Man_ ...` | 694 bytes only · corrupted / empty file. Skip. |
| ` Alison Freer - How to Get Dressed_ ... .epub` and `.pdf` | Costume design. Low corpus signal. Defer to fashion-canon-v2 batch. |
| ` Alison Lumbatis - The Ultimate Book of Outfit Formulas_ ... .epub` and `.pdf` | Defer. |
| ` Rees, Anuschka - The curated closet_ ... .epub` and `.pdf` | Defer. |

These were already adjacent to the fashion category but are how-to / consumer rather than canon. Stage in a future `raw/03_TIER_2_CANON_BOOKS/fashion_styling/` batch if styling becomes load-bearing for the Direction Stack.

### 3.10 · Random PDFs at SOS root · defer

`document.pdf` is unnamed · review before deciding. The user has many PDFs at SOS root I am not classifying (statements, receipts, manuals like `2010-Dodge-Charger-UG.pdf`, `0ce20966-0176-4146-8916-7cbc34a31ca3_production_merged.pdf`, etc.) · but those are NOT in the 242-unique list because they have no basename-match question. Confirm: any file at SOS root NOT explicitly named in §2 should be considered defer-by-default. If a file is corpus-relevant, name it in a follow-on staging revision.

---

## 4 · Internal duplicate decisions

Decisions for files that appear 2+ times within SOS with identical or near-identical content:

| Title | Versions | Decision |
|---|---|---|
| Marc Randolph · That Will Never Work | ` Marc Randolph - ... .epub` (root, leading space) + `Marc Randolph - ... .epub` (root, no leading space) | Pick the no-leading-space version. Identical content. Drop the duplicate from staging. |
| Empire State of Mind (Greenburg) | Two variants of the same epub at root (with/without leading space) | Pick the no-leading-space version. Drop the duplicate. |
| Supreme Models (Reynolds) | `Marcellas Reynolds - Supreme Models_ ... - libgen.li.epub` + `Supreme Models_ Iconic Black Women Who Revolutionized Fashion.epub` | Pick the libgen-prefixed version (canonical filename). Drop the un-prefixed copy. |
| Rich Cohen · The Fish That Ate the Whale | Single file · OK |
| Predictable Revenue (Ross/Tyler) | One at root, one in `books/` | Pick the root copy. Both already in raw via the legacy mirror. NOT in the 242-new list. |
| The Cold Email Manifesto (Berman/Indries) | One at root, one in `books/` | Same · pick one. NOT in new list. |
| PHOTOGRAPHY MASTERCLASS.docx | One in `10_REFERENCE/lighting_pdfs/` (BATCH_001 already chunked), one in `99_VAULT/_intake_archive_2026-05-07/` | Both already in raw. Keep both for provenance. NOT in new list. |
| ai-ops-dashboard-prd.md + `(1).md` | Two versions at root | Pick the unsuffixed. Drop the (1). |
| AI Content Strategy Generator - Lead Magnet.json + `(1).json` | Same | Pick unsuffixed. Drop (1). |
| ai after ramon.docx + `copy.docx` | Working draft pair · already in raw via legacy mirror, not in new list | No action. |
| takeover after ramon.docx + `copy.docx` | Same · already in raw | No action. |
| [Andrew_S._Grove]_High_Output_Management(z-lib.org).pdf + `-2.pdf` | Two PDFs same size · likely identical | Pick unsuffixed. Drop -2. |
| The Cold Email Manifesto in books/ (duplicate) | Already covered above | No action. |
| Power Law (Mallaby) .epub + .pdf | Same book, two formats | Stage only the .epub. .pdf is a redundant format duplicate. |
| Robert Frank The Americans (BATCH_005 sources) | Different · the Day book (analysis) and the Frank/Kerouac book (primary). Both stage. | Stage both. |
| Munger Almanack | .epub (in raw via BATCH_002) + .pdf (in SOS root, 184 MB image-rich) | Stage the .pdf into `investing_finance/` as a supplement. Do NOT replace the .epub. |
| Made to Stick (Heath) | PDF in SOS + mobi version `[Made to Stick ] Heath, Chip _ Heath, Dan ... .mobi` | Both stage. Different format identity. |
| McLuhan Understanding Media | Two PDFs (1994 + 1995 editions) | Stage both. Mark editions during chunking. |
| Rick Rubin Creative Act | `(2023, Penguin)` + `(2023, Canongate)` · two regional epubs | Pick one · the Penguin/US edition is canonical. |
| Stephen Shore Uncommon Places | ` Stephen Shore, Lynne Tillman ... .pdf` (in `PHOTOGRPAHY GOLD`) + `Shore Stephen. - Uncommon Places_ The Complete Works - libgen.li.pdf` (at SOS root) | The `PHOTOGRPAHY GOLD` copy is already in raw via legacy mirror. The root copy is the same book differently filenamed. Stage the root copy into `02_TIER_1_CANON_BOOKS/photography/` as the canonical reference. |

---

## 5 · Post-staging verification (before BATCH_005 chunks anything)

After (and only after) the staging copies above are executed in a separate session, verify:

```bash
# 1. Confirm photography canon staged
ls -la "$DST/02_TIER_1_CANON_BOOKS/photography/"  # expect ~14 files

# 2. Confirm Art Series chapter populated
ls -la "$DST/09_ART_SERIES/"  # expect ~19 files (9 Art_Series + 9 Study + 1 docx)

# 3. Confirm advertising canon staged
ls -la "$DST/02_TIER_1_CANON_BOOKS/advertising/"  # expect 7 files

# 4. Confirm photography scans staged
ls -la "$DST/10_REFERENCE/photography_scans/"  # expect 5 files

# 5. Confirm website packs extracted
ls -la "$DST/14_WEB/website-copy/" "$DST/14_WEB/website-seo/" "$DST/14_WEB/website-design/"

# 6. Confirm the 7 working drafts staged
ls -la "$DST/10_REFERENCE/_intake_2026-05-18/"  # expect 9 files (7 drafts + 2 misc)

# 7. Spot-check that no .part / ~$ / dmg / superseded card / dad_flyer file landed in raw
find "$DST" -name "*.part" -o -name "~\$*" -o -name "*.dmg" -o -path "*CH01_yae*" -o -path "*coach_eric_jones*"
# Should return nothing.

# 8. Confirm Davenport rar (or its renamed .epub) is staged in ai_tech
ls "$DST/02_TIER_1_CANON_BOOKS/ai_tech/" | grep -i Davenport

# 9. Confirm the 3 AI Edge PDFs staged (late addition · see §2.25)
ls -la "$DST/13_OPERATING_DISCIPLINE/"  # expect 3 PDFs unless ICP routed to 05_AI_EDGE_COURSE

# 10. Confirm the AI Edge course transcript + Edge handout staged (second + third late additions · see §2.26)
ls -la "$DST/05_AI_EDGE_COURSE/"  # expect 2 files: COURSE WORK 1 thru 2.docx + Finding Your Edge.pdf

# 11. Confirm the AI history file staged (second late addition · see §2.27)
ls -la "$DST/08_AI_TECH/ai_history_case_studies/"  # expect 1 docx (AI CHANGED EVERYTHING.docx)

# 12. Confirm COURSE WORK 1 thru 2.docx and AI CHANGED EVERYTHING.docx ended up in DIFFERENT folders (not deduplicated)
find "$DST" -name "COURSE WORK 1 thru 2.docx" -o -name "AI CHANGED EVERYTHING.docx"
# Should return exactly 2 paths in different directories.
```

If any verification fails, do NOT proceed with BATCH_005 · diagnose first.

---

## 6 · Recommended next 5 batches

BATCH_005 stays as photography canon (per ACTIVE_KNOWLEDGE_STATE.md + the inventory's recommendation). The staging analysis confirms: photography canon is the deepest currently underserved corpus zone and the source pile is densest at root (Cat C in the inventory · 14 books + 9 Art Series + 5 scans + 7 already-in-raw photography PDFs in PHOTOGRPAHY GOLD). No reason to reorder.

### BATCH_005 · Photography canon at depth · ~14-18 sources

**Source folders to read:**
- `raw/09_ART_SERIES/` (post-staging · 9 Art_Series + 9 Study .md + Art_Series.docx)
- `raw/02_TIER_1_CANON_BOOKS/photography/` (post-staging · 14 new books)
- `raw/10_REFERENCE/photography_scans/` (post-staging · 5 reference scans)
- `raw/PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /` (already in raw · 7 photo PDFs)

**Why first:** Deepest gap, source pile dense, BATCH_001 only sampled 2 photographer studies (Leibovitz, Haas), the canonical theory (Barthes, Sontag) has never been chunked, and `raw/09_ART_SERIES/` is empty.

### BATCH_006 · The 51 SNIPED skills + 50 Claude AI prompt pack + 7 working drafts · ~108 sources

**Source folders to read:**
- `raw/_skills/sniped-*/SKILL.md` (51 skill packs, never chunked)
- `raw/Claude_AI_Skills_50_Upload_Ready (1)/*/SKILL.md` (50 prompt artifacts, never chunked)
- `raw/10_REFERENCE/_intake_2026-05-18/` (post-staging · 7 working drafts + 2 misc + 2 JSONs)

**Why second:** Self-referential corpus · the skills are the agent's own operational primitives. Currently zero corpus presence. The working drafts (CLAUDE CODE SUPERPOWERS, REMOTION, Astro speed) inform how the agent system itself runs.

### BATCH_007 · Advertising + copywriting + positioning canon · 7 sources

**Source folder to read:** `raw/02_TIER_1_CANON_BOOKS/advertising/` (post-staging · 7 books · Ogilvy, Hopkins, Schwartz, Whitman, Sullivan, Bly, Steel)

**Why third:** Biggest blind spot in current corpus. Directly feeds `intel_positioning_phrases.md` and `intel_distribution_mechanics.md` with primary sources. Filling this batch closes the positioning-language gap that's been raised in multiple session reviews.

### BATCH_008 · AI / tech / hybrid-operator defense canon · 12 sources

**Source folder to read:** `raw/02_TIER_1_CANON_BOOKS/ai_tech/` (post-staging · 12 books · Balaji, Dixon, Agrawal ×2, Daugherty, Lakhani, Suleyman, Mollick, Tegmark, Brynjolfsson, Davenport, Steiner)

**Why fourth:** Anchors the hybrid-operator AI sentiment with primary sources. Defends the Camp B routing rule in client conversations. Also addresses the Fastlane / Content Rewards intel note (saved to `future_sources/`) by giving SNIPED a primary-source corpus to draw from when defending against the mass-distribution lane.

### BATCH_009 · Lineage Doctrine + hip-hop / culture canon · 7 sources

**Source folder to read:** `raw/02_TIER_1_CANON_BOOKS/culture/` (post-staging · 7 books · Charnas ×2, Rick Ross, Gucci Mane, Jay-Z, Greenburg, Reynolds)

**Why fifth:** Grounds the Lineage Doctrine (LOCKED 2026-05-12) in primary-source LA Black founder culture material. Currently the lineage doctrine is named but under-referenced in the chunked corpus. Pairing this with the already-done Stoute (Tanning of America) gives the doctrine 8 primary-source chunks to draw from.

### Deferred to BATCH_010+

In rough priority order:
- BATCH_010 · The Direction Stack v_final PDF · own batch · 444 MB · likely 100-200 chunks alone. Cornerstone for the book launch.
- BATCH_011 · Investing / finance canon (`raw/03_TIER_2_CANON_BOOKS/investing_finance/` · 14 books). Medium-load-bearing for founder-buyer psychology.
- BATCH_012 · Strategy + history canon (`raw/02_TIER_1_CANON_BOOKS/strategy_history/` · 14 books · Machiavelli ×2, Clausewitz, Musashi, Greene ×3, Arrian, Engels, Landmarks ×3, Aurelius, Napoleon).
- BATCH_013 · Decision + judgment + cognition (`raw/03_TIER_2_CANON_BOOKS/decision_judgment/` · 16 books).
- BATCH_014 · Memoirs + operator biographies (`raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` · 17 books).
- BATCH_015 · The 26 lighting PDFs in `raw/10_REFERENCE/lighting_pdfs/`. Slow-burn per `sniped-lighting-vault` skill. Micro-batch.
- BATCH_016 · Operating / founder canon (`raw/02_TIER_1_CANON_BOOKS/operating_founder/` · 11 books).
- BATCH_017 · Leadership / management (`raw/03_TIER_2_CANON_BOOKS/leadership_mgmt/` · 10 books).
- BATCH_018 · Consulting / service business (`raw/03_TIER_2_CANON_BOOKS/consulting_service/` · 8 books).
- BATCH_019 · Sales / positioning (`raw/02_TIER_1_CANON_BOOKS/sales_positioning/` · 17 books). Could be elevated earlier if the corpus needs sales primary sources sooner.
- BATCH_020 · Persuasion / psych (`raw/03_TIER_2_CANON_BOOKS/persuasion_psych/` · 8 books · Cialdini ×2, Ariely, Storr, Marx, Shotton, Sutherland, Berger).
- BATCH_021 · Network / distribution (`raw/02_TIER_1_CANON_BOOKS/network_distribution/` · 5).
- BATCH_022 · Fashion / luxury (`raw/03_TIER_2_CANON_BOOKS/fashion_luxury/` · 8).
- BATCH_023 · Systems thinking (`raw/03_TIER_2_CANON_BOOKS/systems_thinking/` · 5).
- BATCH_024 · Expertise / creativity (`raw/03_TIER_2_CANON_BOOKS/expertise_creativity/` · 6).
- BATCH_025 · Operator engine / community (`raw/03_TIER_2_CANON_BOOKS/operator_engine_community/` · 4).
- BATCH_026 · `BATCH_CONTENT_DISTRIBUTION_INTELLIGENCE` from `future_sources/FASTLANE_CONTENT_REWARDS_INTELLIGENCE_2026-05-18.md`. Defensive intel; only run if/when the strategy spine ever opens to a mass-distribution lane.
- BATCH_027 · `EDGE_AND_OPERATING_DISCIPLINE` · 3 AI Edge course PDFs (`raw/13_OPERATING_DISCIPLINE/` · ICP Definition Worksheet, Setting Goals, Weekly Reflections). Operating-discipline scaffolding for the drift-detection nested loops + recurring ICP refinement. Low corpus weight relative to canonical truths; useful as operator tooling reference. Could be elevated earlier if a quarterly Constraint Audit or weekly-review redesign needs the source material first. The `COURSE WORK 1 thru 2.docx` transcript is also a secondary read path for this batch (see BATCH_028).
- BATCH_028 · `AI_AUTOMATION_AGENCY_COURSE` · `raw/05_AI_EDGE_COURSE/` · 2 files (`COURSE WORK 1 thru 2.docx` + `Finding Your Edge.pdf`). Phase 1 AI Opportunity + Phase 2 Strategic Positioning transcript paired with the Phase 1 Edge handout. Covers Edge / ICP / offer / one-liner pitch / goals / execution foundation. Could be combined with BATCH_027 into a single `COURSE_AND_DISCIPLINE` batch if the chunking pass would benefit from cross-referencing transcript + handout to worksheets in the same pass. Cross-reference target: BATCH_027 worksheets (`ICP Definition Worksheet`, `Setting Goals`, `Weekly Reflections`) are the operator outputs whose source instruction lives in this batch's transcript.
- BATCH_029 · `AI_TECH_AND_HUMAN_MACHINE_CREATIVITY` · `raw/08_AI_TECH/ai_history_case_studies/AI CHANGED EVERYTHING.docx`. AlphaGo / DeepMind / Move 37 / Lee Sedol move 78 / human-machine creativity canon. Reinforces hybrid-operator stance (Camp B routing) and counter-balances the Fastlane / Content Rewards intel note. Could be combined with BATCH_008 (AI/tech canon books) if both pile up before either runs · same intellectual territory.
- BATCH_030 · `CLAUDE_CODE_OPERATING_LAYER` · `raw/05_AI_EDGE_COURSE/claude_code/MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx` (pending staging-copy authorization · see §2.28). 8-lesson transcript covering Claude Code from CLI basics through GitHub PR workflow. Direct primary-source feed to the operating-layer spec already live in `AGENTS.md`, `CLAUDE.md`, and the 6 `.claude/skills/` packs. Chunking this batch makes the rationale behind the spec searchable. Could be combined with BATCH_028 (`AI_AUTOMATION_AGENCY_COURSE`) into a single `COURSE_CANON` batch since both transcripts live under `05_AI_EDGE_COURSE/`. Self-referential value · the corpus would carry primary-source justification for the operating files that govern how the corpus is built.

---

## 7 · Constraints respected (final check)

- No files moved, copied, deleted, renamed, extracted, or chunked. All `mkdir` / `cp` / `unzip` commands above are **recommendations only · do NOT execute as part of writing this plan**.
- `MASTER_INDEX.md` not touched.
- `MASTER_CHUNK_MAP.json` not touched.
- `ACTIVE_KNOWLEDGE_STATE.md` not touched.
- BATCH_005 not started.
- Source folder treated as read-only universe.
- `~/AI-Brain-Refinery/raw/` treated as the staging destination but not yet modified.
- Rest of `~/Downloads/` and `~/sniped-media/` left out of scope.

End of staging plan. Next step is to authorize the staging copy pass, then proceed to BATCH_005 photography canon chunking.
