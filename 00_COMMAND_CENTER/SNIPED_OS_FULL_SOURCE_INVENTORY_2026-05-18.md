# SNIPED_OS FULL SOURCE INVENTORY · 2026-05-18

**Scope correction acknowledged:** the user moved all intended source files into `~/Downloads/    SNIPED_OS`. This folder is now the complete source universe for staging. The rest of `~/Downloads/` and `~/sniped-media/` are out of scope for this plan. `~/AI-Brain-Refinery/raw/` is treated as in-progress staging, NOT as complete.

**No moves, deletes, renames, extractions, or processing performed.** Read-only audit with staging recommendations only.

Path note: the folder name has 4 leading spaces. Quote it in shell: `"~/Downloads/    SNIPED_OS"`.

---

## 1 · Total counts and file type breakdown

- **Files (recursive, excluding .DS_Store):** 719
- **Files (recursive, all):** 727
- **Directories:** 156
- **Unique basenames:** 616 (103 internal duplicate basenames · most are SKILL.md and _README.md inside the 50-skill pack)
- **Total size:** 5.1 GB

### File type breakdown (recursive, excluding .DS_Store)

| Ext | Count | Notes |
|---|---:|---|
| md | 254 | doctrine, playbooks, art series, intel extractions, 50 SKILL.md files |
| pdf | 129 | books + photography references + Direction Stack book |
| epub | 128 | book canon |
| docx | 88 | Office-format playbooks, chat threads, working drafts |
| png | 50 | chapter cards, flyer iterations, screenshots |
| mobi | 20 | book canon (Kindle format) |
| mp4 | 8 | 8 YTDown YouTube photographer films (1080p mostly) |
| azw3 | 7 | book canon (Amazon format) |
| xmp | 7 | Lightroom presets (locked look v1/v2/v3, Hero, Proof, BW, Cultural Doc) |
| djvu | 5 | scanned book canon (Becker, Musashi, Ariely, Mihaly, Rensin) |
| zip | 4 | 1 preset backup + 3 website packs |
| sh | 3 | shell scripts (shoot folder setup, backup, verify) |
| html | 3 | index.html × 2 + OfDVDVbyMD.html (defer) |
| dmg | 3 | application installers (Flow, Obsidian, VSCode · NOT corpus) |
| part | 3 | incomplete browser downloads (Schwarzenegger, Coddington, Traction) |
| json | 3 | AI lead-magnet exports (Content Strategy Generator × 2, ElevenLabs agent) |
| txt | 2 | almanack_naval_ravikant analog + Virgil Abloh lecture text |
| xlsx | 1 | SNIPED CRM.xlsx |
| rar | 1 | one "rar" wrapper, actually a zip-EPUB (Davenport · Only Humans Need Apply) |

### Top-level structure

```
    SNIPED_OS/                              5.1 GB · 727 files
├── 00_BRIEF/                              34 files · 608K · spine, CURRENT_STATE, lineage doctrine, locks
├── 01_OFFERS/                              1 file · 20K
├── 02_CONTRACTS/                           3 files · 28K
├── 03_OUTREACH/                           43 files · 1.5 M · DM doctrine, sent DMs, CRM templates
├── 04_CRM/                                 1 file · 12K
├── 04_DELIVERABLES/                        9 files · 45 M · CH01_Yae card iterations (SUPERSEDED)
├── 05_PRODUCTION/                         54 files · 121 M · shoot SOPs, presets, casting doctrine
├── 06_DELIVERY/                           11 files · 56K
├── 07_CONTENT/                             7 files · 164K · caption templates, hook library, video philosophy
├── 08_BOOK/                                1 file · 444 M · The_Direction_Stack_v_final_2026-05-12.pdf
├── 09_ART_SERIES/                          (empty)
├── 10_REFERENCE/                          42 files · 28 M · tactical extractions + 26 lighting PDFs
├── 11_LEGAL/                               (empty)
├── 12_FINANCIAL/                           (empty)
├── 13_NETWORK/                             1 file · 12K
├── 14_WEB/                                 1 file · 12K
├── 99_VAULT/                              17 files · 7.8 M · raw intake archives (2026-05-07, 2026-05-12)
├── _archive/chapter_cards/                 4 files · 7.2 M · CH01_Yae_2026-05-13 canonical cards
├── _inbox/admin/                           1 file · 4K
├── _side_quests/dad_flyer/                 4 files · 968K · coach_eric_jones welcome flyer
├── _skills/                               51 files · 240K · 51 SNIPED skill .md packs (one per skill folder)
├── books/                                  2 files · 3.4 M · Predictable Revenue + Cold Email Manifesto
├── Claude_AI_Skills_50_Upload_Ready (1)/ 50 files · 236K · 50-skill prompt pack (SKILL.md × 50)
├── PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING / 15 files · 1.2 G · 8 YTDown mp4s + 7 photo PDFs
├── scripts/                                3 files · 12K · backup/verify/setup .sh
└── (root)                                364 files · loose books + working docx + ~150 epub/pdf pulls
```

---

## 2 · Likely corpus files

Corpus-eligible extensions found in SOS: pdf · epub · docx · md · mobi · azw3 · djvu · txt · csv · json · xlsx · pptx · html.

**Totals by category:**

| Category | Count |
|---|---:|
| Books (epub + pdf + mobi + azw3 + djvu) | 289 |
| Doctrine / SOP / intel docs (md + docx + txt) | 344 |
| Spreadsheets (xlsx + csv) | 1 |
| Structured data (json) | 3 |
| Web exports (html) | 3 |
| **Corpus total (excl. presets, system files, installers)** | **640** |

Non-corpus: 50 png, 8 mp4, 7 xmp, 3 sh, 3 dmg, 3 part.

---

## 3 · Archives (zip + rar) and their contents

5 archives total inside SOS. None require permanent extraction for inventory; each was inspected via `unzip -l` / `tar tf` without writing to disk.

### 3.1 · `05_PRODUCTION/_preset_backups/SNIPED_PRESETS.zip` · 6.3 KB

5 Lightroom XMP preset files (older snapshot):
- SNIPED_BW_EDITORIAL_v1.xmp · 2829 B
- SNIPED_CULTURAL_DOC_v1.xmp · 3677 B
- SNIPED_HERO_FINISH_v1.xmp · 1996 B
- SNIPED_LOCKED_LOOK_v1.xmp · 3637 B
- SNIPED_PROOF_BATCH_v1.xmp · 3502 B

**Note:** The v3 LUXURY preset (`SNIPED_LOCKED_LOOK_v3_LUXURY.xmp`) and v2 already exist as loose files inside `_preset_backups/`. This zip is a pre-v2/v3 snapshot. Defer · the loose .xmp files are the authoritative copies.

### 3.2 · `website-copy.zip` · 23 KB

```
website-copy/
├── website-copy.md (25 KB · master copy doc)
└── references/
    ├── cro-experiments.md (7.6 KB)
    ├── plain-english.md (8 KB)
    ├── transitions.md (5.4 KB)
    └── copy-frameworks.md (7.7 KB)
```

**Category:** doctrine pack · copywriting frameworks for site copy. **HIGH SIGNAL** for the website/positioning lane (overlaps the 14_WEB chapter).

### 3.3 · `website-seo.zip` · 45 KB

```
website-seo/
├── website-seo.md (27 KB · master SEO doc)
├── scripts/seo-scanner.py (44 KB · scanner code)
└── references/
    ├── platform-ranking.md (13 KB)
    ├── ai-seo-guide.md (16 KB)
    ├── content-patterns.md (18 KB)
    └── schema-examples.md (16 KB)
```

**Category:** doctrine pack + tooling. The .md is corpus, the .py is the scanner script (not corpus, but worth keeping in `14_WEB/scripts/`). **HIGH SIGNAL** for SEO positioning.

### 3.4 · `website-design.zip` · 53 KB

```
website-design/
├── website-design.md (13 KB · master design doc)
├── scripts/search.py (24 KB)
├── data/
│   ├── patterns.csv (9 KB)
│   ├── typography.csv (14 KB)
│   ├── styles.csv (22 KB)
│   ├── ux-rules.csv (19 KB)
│   └── colors.csv (20 KB)
└── references/
    ├── design-checklist.md (7 KB)
    └── ux-principles.md (5.5 KB)
```

**Category:** design system pack with structured CSV data. **HIGH SIGNAL** for design language consistency.

### 3.5 · ` Thomas H. Davenport, Julia Kirby - Only Humans Need Apply ... libgen.li.rar` · 1.3 MB

File reports as RAR (v2.0, Win32), but the payload is a standard EPUB structure (mimetype, META-INF, content.opf, 21 text/part*.html files, 4 images). `unzip -l` reads it. **Treat as one canon book in EPUB form, mis-extensioned as .rar.** No real archive overhead.

**Disposition:** rename to `.epub` on copy into raw OR leave the extension and process via `unzip` extraction during chunking. Either works.

---

## 4 · What already exists in `~/AI-Brain-Refinery/raw/`

Basename diff between SOS and raw (using `comm`, robust to special characters):

| | Basenames | Notes |
|---|---:|---|
| In SOS, present in raw | **374** | mostly the legacy mirror tree (00_BRIEF, 05_PRODUCTION, etc.) plus 19 Tier-1 books and 10 Tier-2 books |
| Unique to SOS (not in raw) | **242** | the staging gap. See §6 for the breakdown. |
| Unique to raw (not in SOS) | **1** | `mostly Powerhouse-.docx` · a misfiled docx flagged in SOURCE_RECONCILIATION_PLAN_2026-05-18.md §2.C |

The 374 already-mirrored basenames include:
- The full SNIPED chapter tree (00_BRIEF, 01_OFFERS, 02_CONTRACTS, 03_OUTREACH, 04_CRM, 05_PRODUCTION, 06_DELIVERY, 07_CONTENT, 08_BOOK, 10_REFERENCE, 13_NETWORK, 14_WEB).
- 19 Tier 1 canon books (already in `raw/02_TIER_1_CANON_BOOKS/`).
- 10 Tier 2 canon books (already in `raw/03_TIER_2_CANON_BOOKS/`).
- The 26 lighting PDFs in `10_REFERENCE/lighting_pdfs/`.
- The 8 YTDown mp4s in `PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /`.
- The 7 photography reference PDFs in the same folder.
- The 51 SNIPED skill .md files in `_skills/`.
- The 50 SKILL.md files in `Claude_AI_Skills_50_Upload_Ready (1)/` (basename-collision; each lives in a distinct subfolder).

---

## 5 · What was already processed in BATCH_001 → BATCH_004

Extracted unique sources from `MASTER_INDEX.md` + the 4 BATCH_NNN_CHUNKS.jsonl files. 62 unique source files have been chunked into the 457-chunk corpus.

### BATCH_001 · 25 sources (SNIPED OS spine)
00_BRIEF/100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md · 00_BRIEF/EXECUTION_PRIORITIZATION.md · 00_BRIEF/OPERATIONAL_BACKBONE.md · 00_BRIEF/PRODUCTION_OS.md · 00_BRIEF/REVERSE_ROADMAP.md · 00_BRIEF/SNIPED_OS_V1_SYNTHESIS_2026-05-12.md · 03_OUTREACH/cold_email_doctrine_v1.md · 05_PRODUCTION/chapter_rollout_doctrine_v1.md · 10_REFERENCE/STRATEGIC_PRINCIPLES.md · 10_REFERENCE/lighting_pdfs/PHOTOGRAPHY MASTERCLASS.docx · 99_VAULT/_intake_archive_2026-05-07/AI PHOTOGRAPHERS.docx · aesthetic_statement_v1.md · chat Sniped MAster thread.docx · Gemini Sniped MAster thread.docx · sniped_figma.docx · SNIPED_OS_OPERATING_BRIEF.md · Study_AnnieLeibovitz.md · Study_ErnstHaas.md · The_Adobe_Stack_Manual.docx · The_Attention_Stack.docx · The_Copywriting_Stack.docx · The_Offer_Stack.docx · The_Outbound_Stack.docx · The_Platform_Stack.docx · The_Production_Stack.docx · The_Revenue_Stack.docx

### BATCH_002 · 19 sources (Tier 1 canon books)
art_of_war · 33_strategies_of_war · 48_laws_of_power · alexander_the_great_freeman · cold_start_problem_chen · creativity_inc_catmull · disneywar_stewart · everything_store_bezos_stone · genghis_khan_weatherford · outsiders_thorndike · poor_charlies_almanack_munger · ride_of_a_lifetime_iger · shoe_dog_knight · song_machine_seabrook · steve_jobs_isaacson · stoute_powerhouse_talk · tanning_of_america_stoute · working_backwards_bryar_carr · zero_to_one_thiel

### BATCH_003 · 10 sources (Tier 2 canon books)
almanack_naval_ravikant · blockbusters_elberse · company_of_one_jarvis · elephant_in_the_brain_simler_hanson · perennial_seller_holiday · pricing_creativity_enns · revenge_of_analog_sax · status_anxiety_de_botton · unreasonable_hospitality_guidara · wwp_manifesto_enns

### BATCH_004 · 8 sources (SNIPED OS depth-fill)
aesthetic_statement_v1 (deep) · 100q_audit_optimizations (deep) · strategic_principles (deep) · sniped_os_v1_synthesis (deep) · chat_sniped_master_thread (deep) · gemini_sniped_master_thread (deep) · offer_stack_full · platform_stack_full

**The 457-chunk corpus is comprehensive for the SNIPED operational spine + the first 29-book canon, but does NOT yet cover photography canon, advertising/copywriting canon, AI/tech canon, VC/investing canon, hip-hop culture canon, or the 19 newer doctrine docs/playbooks sitting in the 99_VAULT intake archives.**

---

## 6 · What is new and needs staging

The 242 SOS-only basenames break down into the following categories. **"New"** means "not currently in `~/AI-Brain-Refinery/raw/`". Most of these are book pulls and recent doctrine docs the user dropped into Downloads since 2026-05-12.

### Category A · Strategy / operating canon books (NEW · HIGH SIGNAL · ~25 titles)

Candidate for `raw/02_TIER_1_CANON_BOOKS/` or `raw/03_TIER_2_CANON_BOOKS/`:

- **Influence + persuasion:** Cialdini · Influence (PDF) · Pre-Suasion (epub) · Predictably Irrational (Ariely, djvu) · Status Game (Storr) · Status and Culture (W. David Marx) · Choice Factory (Shotton) · Alchemy (Sutherland) · Contagious (Berger) · Made to Stick (Heath, PDF dup)
- **Positioning + brand strategy:** Eating the Big Fish (Morgan) · Differentiate or Die (Trout) · Crossing the Chasm (Moore) · Purple Cow (Godin) · This Is Marketing (Godin) · Tribes (Godin) · Building a StoryBrand (Donald Miller, mobi) · Obviously Awesome (Dunford) · Play Bigger (Lochhead et al)
- **Founder + operating:** Lean Startup (Ries) · Hard Thing About Hard Things (Horowitz) · Blitzscaling (Hoffman) · Founder's Dilemmas (Wasserman) · E-Myth Revisited (Gerber) · Built to Sell (Warrillow) · Amp It Up (Slootman) · Innovator's Dilemma (Christensen) · Competing Against Luck (Christensen)
- **Sales + outbound:** Hormozi $100M Offers · Hormozi $100M Leads · Never Split the Difference (Voss) · Gap Selling (Keenan) · Cold Email Manifesto · Combo Prospecting (Hughes) · Mom Test (Fitzpatrick)
- **Consulting + service business:** Personal MBA (Kaufman) · McKinsey Way (Rasiel) · Managing the Professional Service Firm (Maister) · Flawless Consulting (Block) · Million Dollar Consulting (Weiss) · Value-Based Fees (Weiss)
- **Leadership + management:** High Output Management (Grove, 2 dup PDFs) · Extreme Ownership (Willink) · Dichotomy of Leadership · Measure What Matters (Doerr) · Turn the Ship Around (Marquet) · Radical Candor (Scott) · Leadership in Turbulent Times (Goodwin) · Team of Rivals (Goodwin) · The Advantage (Lencioni) · Getting Naked (Lencioni) · Death by Meeting (Lencioni)

### Category B · Advertising + copywriting canon (NEW · HIGH SIGNAL · ~10 titles)

Candidate for `raw/02_TIER_1_CANON_BOOKS/` or a new `raw/02b_TIER_1_ADVERTISING_CANON/`:

- Confessions of an Advertising Man (Ogilvy, PDF)
- Cashvertising (Whitman)
- Breakthrough Advertising (Schwartz, PDF)
- Scientific Advertising (Hopkins, PDF)
- Hey Whipple Squeeze This (Sullivan, PDF)
- Copywriter's Handbook (Bly, mobi)
- Truth Lies and Advertising / Jon Steel journal article (PDF)

These directly feed `intel_positioning_phrases.md` and `intel_distribution_mechanics.md`. **Underrepresented in corpus.**

### Category C · Photography canon (NEW · HIGHEST SIGNAL · ~12 titles)

Candidate for `raw/02_TIER_1_CANON_BOOKS/` or `raw/10_REFERENCE/photography_books/`:

- **William Eggleston's Guide** (Szarkowski · MoMA, PDF) · NEW · the canonical Eggleston scholarly source
- **Uncommon Places** (Stephen Shore, PDF · 2 copies under different filenames)
- **The Nature Of Photographs** (Stephen Shore, PDF)
- **Annie Leibovitz at Work** (EPUB · NEW edition · the PDF is already in raw)
- **Light, Gesture, and Color** (Jay Maisel, EPUB)
- **The Photographer's Eye** (Michael Freeman, mobi)
- **The Photographer's Vision** (Michael Freeman, EPUB)
- **Robert Frank's 'The Americans': The Art of Documentary Photography** (Jonathan Day, EPUB)
- **Avedon: Something Personal** (Norma Stevens, EPUB)
- **Camera Lucida** (Roland Barthes, EPUB) · foundational photo theory
- **On Photography** (Sontag, PDF) · foundational photo theory
- **Decisive Moment** (Cartier-Bresson, PDF · scanned)
- **Looking at Photographs** (Szarkowski 1973, PDF · scanned)
- **Ernst Haas free PDF** (pdfcoffee scan)
- **Virgil Abloh: Figures of Speech** (pdfcoffee scan + Core Studio Lecture transcript .txt + Fashion Theory journal article PDF)
- **Pharrell · Places and Spaces I've Been** (PDF) · adjacent · founder portraiture reference
- **The Operator** (Tom King, PDF) · adjacent

These directly feed BATCH_005 if photography canon is the next batch · and they fill the empty `raw/09_ART_SERIES/` chapter.

### Category D · AI / tech canon (NEW · HIGH SIGNAL · ~12 titles)

Candidate for `raw/02_TIER_1_CANON_BOOKS/` or new `raw/02c_TIER_1_AI_TECH_CANON/`:

- The Network State (Balaji Srinivasan)
- Read Write Own (Chris Dixon)
- Power and Prediction (Agrawal/Gans/Goldfarb)
- Prediction Machines (same authors)
- Human + Machine (Daugherty/Wilson)
- Competing in the Age of AI (Lakhani/Iansiti)
- The Coming Wave (Suleyman)
- Co-Intelligence (Mollick)
- Life 3.0 (Tegmark, PDF)
- The Second Machine Age (Brynjolfsson, mobi)
- Only Humans Need Apply (Davenport/Kirby, the .rar/epub)
- Automate This (Steiner)

Directly feeds `intel_ai_sentiment.md` and the hybrid-operator stance defense.

### Category E · VC / investing / capital markets canon (NEW · ~12 titles)

Less directly load-bearing for SNIPED but relevant for founder-buyer psychology and decade-arc thinking:

- Sand Hill Road (Kupor, 2 versions)
- Power Law (Mallaby, epub + pdf)
- Venture Deals (Feld/Mendelson)
- The New Tycoons (Kelly · PE industry)
- King of Capital (Carey/Morris · Blackstone)
- Margin of Safety (Klarman, PDF)
- Security Analysis 6th ed (Graham/Dodd, PDF)
- Snowball (Schroeder · Buffett biography)
- Essays of Warren Buffett (Cunningham)
- Mastering the Market Cycle (Marks)
- The Most Important Thing (Marks)
- Psychology of Money (Housel)
- Intelligent Investor (Graham)
- Rich Dad Poor Dad (Kiyosaki, 2 dup epubs + pdf)
- House of Morgan / Titan / Grant / Washington / Elon Musk (Chernow + Isaacson biographies)
- Sovereign Individual (Davidson/Rees-Mogg)
- Lords of Easy Money (Leonard)

### Category F · Hip-hop / culture / lineage canon (NEW · HIGH SIGNAL FOR LINEAGE DOCTRINE · ~7 titles)

Candidate for `raw/02d_TIER_1_CULTURE_CANON/` or `raw/02_TIER_1_CANON_BOOKS/`:

- **Dilla Time** (Dan Charnas) · directly feeds the LA Black founder culture lineage
- **The Big Payback** (Charnas) · history of hip-hop business
- **Hurricanes: A Memoir** (Rick Ross)
- **The Autobiography of Gucci Mane**
- **Jay-Z Decoded**
- **Empire State of Mind** (Greenburg · Jay-Z biz biography)
- **Supreme Models** (Marcellas Reynolds · 2 dup epubs · iconic Black women fashion)
- **Tanning of America** (Stoute, already done)

### Category G · Memoirs + biographies + hospitality / media operators (NEW · ~12 titles)

- **Grace: A Memoir** (Coddington) · NEW + a stale .part incomplete download next to it
- **Total Recall** (Schwarzenegger) · NEW + a stale .part next to it
- **D.V.** (Diana Vreeland) · fashion editor memoir
- **The Chiffon Trenches** (André Leon Talley) · fashion editor memoir
- **The Beautiful Fall** (Drake · Saint Laurent / Lagerfeld history)
- **Dieter Rams: As Little Design as Possible** (Lovell)
- **Tinderbox** (Miller · HBO history)
- **Those Guys Have All the Fun** (Miller · ESPN history)
- **Live From New York** (SNL history)
- **The Airbnb Story** (Gallagher)
- **Super Pumped** (Isaac · Uber)
- **The Mailroom** (Rensin · Hollywood agent history, djvu)
- **Pour Your Heart Into It** (Schultz · early Starbucks)
- **Onward** (Schultz · Starbucks reset)
- **Hit Men** (Dannen · music industry history, big PDF)
- **Made in Japan** (Akio Morita · Sony)
- **Sam Walton: Made in America**
- **Grinding It Out** (Ray Kroc)
- **The Fish That Ate the Whale** (Cohen)
- **The Kingdom of Prep** (Bullock · J.Crew)
- **Losing My Virginity** (Richard Branson)
- **No Filter** (Sarah Frier · Instagram)
- **Marc Randolph · That Will Never Work** (Netflix)
- **The Goal** (Goldratt)
- **The Toyota Way** (Liker, PDF)
- **Reengineering the Corporation** (Hammer)
- **The Fifth Discipline** (Senge)
- **Thinking in Systems** (Meadows)

### Category H · Strategy + history canon (NEW · ~10 titles)

- Discourses on Livy (Machiavelli)
- The Prince (Machiavelli)
- On War (Clausewitz)
- The Book of Five Rings (Musashi, djvu)
- Mastery (Greene · NEW · the third Greene to pair with the two already done)
- The Laws of Human Nature (Greene · NEW)
- The 50th Law (50 Cent + Greene)
- The Campaigns of Alexander (Arrian)
- Alexander the Great and the Logistics of the Macedonian Army (Engels)
- The Landmark Herodotus / Thucydides
- LandmarkCaesarWebEssays
- Marcus Aurelius Meditations
- Napoleon: A Life

### Category I · Decision-making + cognition + judgment (NEW · ~10 titles)

- Thinking, Fast and Slow (Kahneman · epub + mobi · duplicate)
- Noise (Kahneman/Sunstein/Sibony)
- Superforecasting (Tetlock/Gardner)
- The Signal and the Noise (Silver)
- The Hero with a Thousand Faces (Campbell)
- Save the Cat (Snyder)
- The Anatomy of Story (Truby)
- Story (Robert McKee)
- Mans Search for Meaning (Frankl)
- Denial of Death (Becker, djvu)
- The True Believer (Hoffer)
- Coddling of the American Mind (Lukianoff/Haidt)
- The Righteous Mind (Haidt)
- Games People Play (Berne)
- The Crowd (Le Bon)
- Amusing Ourselves to Death (Postman, Vietnamese-language edition!)

### Category J · Fashion / luxury / style (NEW · ~10 titles · medium signal)

Adjacent to SNIPED visual direction:

- Christian Dior · Dior by Dior · autobiography
- Christian Dior · Little Dictionary of Fashion (epub + pdf dup)
- Deluxe (Dana Thomas · how luxury lost its luster)
- The Luxury Strategy (Kapferer/Bastien)
- The End of Fashion (Agins)
- Eating the Big Fish (Morgan · already in Cat A)
- Hey Whipple Squeeze This (already in Cat B)
- Confessions (already in Cat B)
- Camera Lucida (already in Cat C)

### Category K · Operator-engine / community-building (NEW · ~5 titles)

- Get Together (Stripe Press · build community with your people)
- The Business of Belonging (David Spinks)
- Long Tail (Chris Anderson)
- Free (Chris Anderson, abridged)
- The Inevitable (Kevin Kelly)
- New Rules for the New Economy (Kelly)
- The Great Online Game (Packy McCormick, PDF)
- 1000 True Fans (Kevin Kelly, PDF)

### Category L · Recent SNIPED working drafts + AI-tool docs (NEW · HIGH SIGNAL · 7 docs)

These are working drafts the user added recently. They are NOT canon books · they are operating intel + skill builds:

- `ai-ops-dashboard-prd.md` + `ai-ops-dashboard-prd (1).md` · PRD for AI ops dashboard (2 versions)
- `astro claude websites 3x faster.docx` · Astro framework speed notes
- `Built an AI SaaS in 20 min.docx` · AI SaaS tutorial extraction
- `CLAUDE CODE PLUGIN.docx` · Claude Code plugin notes
- `CLAUDE CODE SUPERPOWERS.docx` · Claude Code workflow extraction
- `REMOTION.docx` · Remotion video framework notes
- `youtube skool doc.docx` · YouTube Skool doctrine

**Disposition:** route into `raw/10_REFERENCE/` or new `raw/10_REFERENCE/_intake_2026-05-18/`.

### Category M · Lead-magnet JSON exports (NEW · medium signal)

- `AI Content Strategy Generator - Lead Magnet.json` (+ dup `(1).json`)
- `Blueprint - ElevenLabs Agent That Calls & Qualifies Leads.json`

**Disposition:** `raw/10_REFERENCE/automations/` or `raw/14_WEB/`. These are workflow templates, low-priority corpus.

### Category N · Photography reference scans (NEW · supplement Cat C)

- `257683787-Cartier-Bresson-H-1952-the-Decisive-Moment.pdf`
- `367490464-Szarkowski-1973-Looking-at-Photographs-pdf.pdf`
- `pdfcoffee.com_ernst-haas-pdf-free.pdf`
- `pdfcoffee.com_virgil-abloh-figures-of-speech-pdf-free.pdf`
- `713434459-Core-Studio-Public-Lecture-Virgil-Abloh-Insert-Complicated-Title-Here-English.txt`

### Category O · 50-skill Claude AI prompt pack (`Claude_AI_Skills_50_Upload_Ready (1)/`)

Each of the 50 sub-folders contains a `SKILL.md` and a `_README.md`. Topics include: framework-orchestrator, market-evaluation-scorecard, mom-test-customer-conversation, photography-business-system, professional-portrait-direction, etc.

**Status:** The folder already exists in raw under the same name. No staging needed · but the 50 SKILL.md files have **NEVER been chunked**. Worth a dedicated batch (see §10 BATCH_006).

---

## 7 · Duplicates and stale files

### 7.1 · Stale Office lock files (IGNORE · 2)

- `~$FIGMA.docx`
- `~$iped figma.docx`

Auto-generated Word lock files. Never useful. Safe to delete from SOS at any point.

### 7.2 · Incomplete browser downloads (REPLACE · 3)

Three `.part` files sit next to completed `.epub` siblings of the same book. The completed twin should be staged; the .part is dead.

- `Petre, Peter_Schwarzenegger, Arnold - Total recall... libgen.EMtzD5ez.li.epub.part` · keep `.epub` sibling
- `Coddington, Grace - Grace_ A Memoir... libgen.k58BBVFb.li.epub.part` · keep `.epub` sibling
- `Gabriel Weinberg, Justin Mares - Traction... libgen._3TBhCeq.li.epub.part` · keep `.epub` sibling

### 7.3 · Internal duplicate basenames within SOS (5 distinct cases)

| Basename | Count | Notes |
|---|---:|---|
| `SKILL.md` | 100 | 50 in raw skill pack + 50 in the Claude_AI_Skills_50_Upload_Ready pack. Expected · they live in distinct skill folders. Each is a different file by content. |
| `_README.md` | 2 | Distinct content, OK. |
| `The Cold Email Manifesto... Anna's Archive.pdf` | 2 | One in root, one in `books/`. Identical content. Pick one. |
| `PHOTOGRAPHY MASTERCLASS.docx` | 2 | One in `10_REFERENCE/lighting_pdfs/`, one in `99_VAULT/_intake_archive_2026-05-07/`. The lighting_pdfs copy is canonical (BATCH_001 already ingested it). The vault copy is the raw intake antecedent. Keep both for now (provenance). |
| `Aaron Ross... Predictable Revenue... libgen.li.pdf` | 2 | One in root, one in `books/`. Identical. Pick one. |

### 7.4 · Books with both `.epub` and `.pdf` (same title, different format) · KEEP BOTH

The corpus pipeline benefits from EPUB (better text extraction) but PDF holds figures. Both should be staged · no action needed.

Examples in SOS: `Christian Dior · Little Dictionary of Fashion`, `Made to Stick (Heath)`, `Toyota Way (Liker)`, `Good Strategy Bad Strategy (Rumelt)`, `The Creative Act (Rubin)`, `The Curated Closet (Rees)`, `Power Law (Mallaby)`, `Sand Hill Road (Kupor)`, `Rich Dad Poor Dad (Kiyosaki)`, several others.

### 7.5 · Superseded CH01_Yae chapter cards (9 PNGs · IGNORE)

Live in `04_DELIVERABLES/CH01_yae/`. Replaced by `raw/_archive/chapter_cards/CH01_Yae_2026-05-13/`. The B&W Card Dual-Register rule locked 2026-05-13 made these obsolete. **Documented in SOURCE_RECONCILIATION_PLAN_2026-05-18.md §1.B and §5 W1.**

### 7.6 · Dad-flyer side quest (4 PNGs · OPTIONAL · NOT SNIPED CORPUS)

Live in `_side_quests/dad_flyer/`. Personal favor work · "Coach Eric Jones welcome flyer". Not corpus material. Leave in SOS or optionally mirror to `raw/_archive/side_quests/`. Not blocking.

### 7.7 · Application installers (3 DMGs · IGNORE · NOT CORPUS)

- `Flow-v1.5.339.dmg`
- `Obsidian-1.12.7.dmg`
- `VSCode-darwin-universal.dmg`

Software installers. Never corpus. Worth moving out of SOS into a separate `_installers/` location at some point · not blocking.

### 7.8 · System / data files (LEAVE)

- 8 `.DS_Store` · macOS metadata · ignore
- 7 `.xmp` Lightroom presets · already in raw under `_preset_backups/` · no action
- `SNIPED_PRESETS.zip` · superseded snapshot · keep as backup, do not stage
- 3 `.sh` scripts · already in raw under `scripts/` · no action
- 3 `.html` (`index.html` × 2, `OfDVDVbyMD.html`) · low signal · defer

### 7.9 · Cross-reference to prior reconciliation finding

`SOURCE_RECONCILIATION_PLAN_2026-05-18.md` flagged 15 unique-to-legacy basenames as of this morning. That count was based on a snapshot before the user moved files in. The current count is 242 unique-to-SOS. **The growth (~227 files) is the new intake the user moved in.**

---

## 8 · Recommended raw subfolder staging plan

Lay out a target structure under `~/AI-Brain-Refinery/raw/` and copy from SOS in passes. **No moves recommended yet · only the destination map.** Execute in BATCH_005 prep.

### 8.1 · Existing chapter slots (no structural change)

- `raw/00_BRIEF/` → all `00_BRIEF/*.md` from SOS (already mirrored, just refresh the few newer ones · CANONICAL_TRUTHS.md, THE_LINEAGE_DOCTRINE.md, OPERATOR_QUESTIONS_2026-05-13.md, OPERATING_LOCKS_2026-05-12.md, etc., if they have grown.)
- `raw/05_PRODUCTION/` → refresh any newly edited SOPs from SOS.
- `raw/07_CONTENT/` → already mirrored.
- `raw/09_ART_SERIES/` → empty in raw. Populate with the 9 `Art_Series_*.md` + `Study_*.md` files from SOS root.
- `raw/10_REFERENCE/` → already mirrored. Add `_intake_2026-05-18/` subfolder for the 7 working docs in Category L.
- `raw/13_NETWORK/`, `raw/14_WEB/` → already mirrored. Add the website-{copy,seo,design} extracted contents under `raw/14_WEB/`.

### 8.2 · Tier 1 / Tier 2 canon book layout (extension proposal)

The existing flat `raw/02_TIER_1_CANON_BOOKS/` and `raw/03_TIER_2_CANON_BOOKS/` have served 29 books. Adding 100+ more books needs sub-categorization or it becomes unbrowsable. Proposed:

```
raw/02_TIER_1_CANON_BOOKS/
├── strategy/             (Sun Tzu, Greene ×3, Thiel, Thorndike, Munger, etc.)
├── operating/            (Bezos, Iger, Catmull, Bryar, Stewart, Isaacson, Knight, Walton, Kroc)
├── advertising/          (Ogilvy, Hopkins, Schwartz, Sullivan, Whitman, Bly, Steel)
├── photography/          (Eggleston/Szarkowski, Shore ×2, Leibovitz, Maisel, Freeman ×2, Day-Frank, Stevens-Avedon, Barthes, Sontag, Cartier-Bresson, Looking at Photographs, Haas, Abloh)
├── ai_tech/              (Balaji, Dixon, Agrawal ×2, Daugherty, Lakhani, Suleyman, Mollick, Tegmark, Brynjolfsson, Davenport, Steiner)
├── culture/              (Stoute ×2, Charnas ×2, Jay-Z, Gucci Mane, Rick Ross, Greenburg, Reynolds)
└── network_distribution/ (Chen, Seabrook, Anderson ×2, Kelly ×2)

raw/03_TIER_2_CANON_BOOKS/
├── pricing/              (Enns ×2, Weiss ×2)
├── hospitality_service/  (Guidara, Maister)
├── status_signaling/     (de Botton, Simler/Hanson, Storr, Marx)
├── leverage_scale/       (Naval, Jarvis, Hormozi ×2)
├── perennial_blockbuster/(Holiday, Elberse)
├── analog/               (Sax)
├── persuasion_psych/     (Cialdini ×2, Ariely, Berger-Contagious, Shotton, Sutherland, Heath)
├── decision_judgment/    (Kahneman ×2, Sunstein-Noise, Tetlock, Silver, Frankl, Becker)
├── consulting_service/   (Block, Lencioni ×3, Maister, Weiss ×2, Rasiel-McKinsey)
├── investing/            (Graham ×2, Buffett, Munger-dup-PDF, Klarman, Marks ×2, Mallaby ×2, Schroeder, Housel, Kiyosaki)
├── leadership_mgmt/      (Grove, Doerr, Willink ×2, Marquet, Scott, Goodwin ×2)
└── systems_thinking/     (Meadows, Senge, Goldratt, Hammer-Reengineering)
```

If sub-categorization is too heavy, defer it and create a flat `raw/02_TIER_1_CANON_BOOKS/_new_2026-05-18/` and `raw/03_TIER_2_CANON_BOOKS/_new_2026-05-18/` for the new pulls. Decide format before BATCH_005.

### 8.3 · Website packs

```
raw/14_WEB/
├── website-copy/       (extracted from zip)
├── website-seo/        (extracted from zip)
├── website-design/     (extracted from zip)
└── (existing 14_WEB content)
```

### 8.4 · Working drafts + lead-magnet JSONs + AI-tool docs

```
raw/10_REFERENCE/_intake_2026-05-18/
├── ai-ops-dashboard-prd.md
├── astro_claude_websites.docx
├── built_an_ai_saas_in_20_min.docx
├── claude_code_plugin.docx
├── claude_code_superpowers.docx
├── remotion.docx
├── youtube_skool.docx
└── automations/
    ├── ai_content_strategy_generator.json
    └── elevenlabs_agent_calls_qualifies_leads.json
```

### 8.5 · Photography canon supplement (in addition to 8.2)

```
raw/10_REFERENCE/photography_books/   (already exists implicitly via PHOTOGRPAHY GOLD)
└── (the existing 7 photo PDFs in PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /)

raw/10_REFERENCE/photography_scans/   (NEW)
├── cartier_bresson_decisive_moment.pdf
├── szarkowski_looking_at_photographs.pdf
├── ernst_haas_pdfcoffee.pdf
├── virgil_abloh_figures_of_speech_pdfcoffee.pdf
└── virgil_abloh_core_studio_lecture.txt
```

---

## 9 · High-signal flags · do not miss

1. **Photography canon is finally complete.** William Eggleston's Guide (Szarkowski), Uncommon Places + Nature of Photographs (Shore), Camera Lucida (Barthes), On Photography (Sontag), Decisive Moment (Cartier-Bresson), Looking at Photographs (Szarkowski 1973), Avedon Something Personal (Stevens) · these were the **missing canonical foundations** behind the existing Study_*.md and Art_Series_*.md files. The 7-photographer canon (Avedon, Eggleston, Leibovitz, Shore, Herzog, Frank, Meyerowitz, Iturbide, Haas) plus Cartier-Bresson, Maisel, Freeman ×2, and the Roland Barthes / Sontag theory pair give SNIPED its photo theory + lineage primary sources for the first time. **BATCH_005 photography canon is now substantially deeper than the prior plan assumed.**
2. **Dilla Time + The Big Payback (Charnas)** are direct lineage doctrine inputs · they ground the LA Black founder culture lineage (per `feedback_lineage_doctrine.md`) in primary sources. **HIGH PRIORITY for Cat F.**
3. **Advertising + copywriting canon is now staged.** 7 foundational ad books (Ogilvy, Hopkins, Schwartz, Whitman, Sullivan, Bly, Steel) directly feed `intel_positioning_phrases.md` and `intel_distribution_mechanics.md`. **Underrepresented in current corpus · worth a dedicated batch.**
4. **AI / tech canon is staged.** 12 titles let SNIPED defend the hybrid-operator stance with cited primary-source intel (Brynjolfsson, Mollick, Suleyman, Tegmark, Davenport).
5. **Hormozi ×2 ($100M Offers + $100M Leads)** · the lone offer/sales canon currently missing. Pair with the Enns pricing canon already done.
6. **Greene complete set** · Mastery + Laws of Human Nature now sit next to the already-processed 33 Strategies + 48 Laws. The 50th Law (50 Cent + Greene) is a culture-strategy bridge.
7. **Lencioni service-business set** (The Advantage, Getting Naked, Death by Meeting, Five Dysfunctions-implied, Dichotomy of Leadership) maps directly to the SNIPED service-as-product positioning.
8. **3 incomplete .part files** sit next to completed siblings. Confirm completed files are intact before discarding the .part. Total Recall, Grace, and Traction are all real adds.
9. **The .rar that is actually an EPUB** (Davenport · Only Humans Need Apply) · handle as a regular EPUB during BATCH staging. Don't waste cycles trying to install unrar.
10. **The 50-skill Claude AI prompt pack** in `Claude_AI_Skills_50_Upload_Ready (1)/` has **never been chunked**. Each SKILL.md is a structured prompt artifact. Worth its own batch (see §10 BATCH_006).
11. **The 3 website packs** (copy/seo/design) are doctrine-quality content. The CSV data files in website-design.zip are structured design-system tokens · they may be more useful to the website project than to the corpus, but the .md sources should be chunked.
12. **The Direction Stack v_final PDF** sits in `08_BOOK/` and weighs 444 MB · it has not been chunked. **The Direction Stack book launch is BJ's named decade-asset.** Its own chunked corpus presence is overdue.

---

## 10 · Recommended next 5 batches

Given the corrected source universe, the recommended sequence:

### BATCH_005 · Photography canon at depth (12 sources)

**Sources:**
- 9 `Study_*.md` and `Art_Series_*.md` files from SOS root (Avedon, Eggleston, Leibovitz, Shore, Herzog, Frank, Meyerowitz, Iturbide, Haas)
- `Art_Series.docx` wrapper
- The 6 photo theory + monograph PDFs: William Eggleston's Guide (Szarkowski), Uncommon Places (Shore), Nature of Photographs (Shore), Camera Lucida (Barthes), On Photography (Sontag), Annie Leibovitz at Work (EPUB)
- The 2 scanned reference PDFs: Decisive Moment (Cartier-Bresson), Looking at Photographs (Szarkowski 1973)
- The 2 Freeman books (Photographer's Eye, Photographer's Vision)
- Robert Frank's 'The Americans' (Jonathan Day)
- Avedon: Something Personal (Stevens)
- Light, Gesture, and Color (Maisel)
- Ernst Haas in Black and White (already in raw via PHOTOGRPAHY GOLD)
- The Americans (Robert Frank/Kerouac, already in raw via PHOTOGRPAHY GOLD)
- Fred Herzog journal article (already in raw via PHOTOGRPAHY GOLD)
- Avedon American West journal article (already in raw via PHOTOGRPAHY GOLD)
- Virgil Abloh: Figures of Speech (Fashion Theory journal article · already in SOS root)

**Why first:** ACTIVE_KNOWLEDGE_STATE.md already names this as the next batch · and the new finds in §6 Cat C and §9 flag this as the most under-served corpus zone given how central photography craft is to SNIPED. Populates the empty `raw/09_ART_SERIES/` chapter.

### BATCH_006 · The 50-skill Claude AI prompt pack + the 51 SNIPED skill .md files

**Sources:**
- 50 SKILL.md files from `Claude_AI_Skills_50_Upload_Ready (1)/`
- 51 SKILL.md files from `_skills/sniped-*/`
- The 7 working drafts in Cat L (PRDs, Claude Code docs, Astro, Remotion, YouTube Skool, AI SaaS)

**Why second:** Structured prompt artifacts and operational AI-tool intel. Self-referential to the agent system that runs SNIPED. Currently zero corpus presence.

### BATCH_007 · Advertising + copywriting + positioning canon (10 books)

**Sources:**
- Ogilvy · Confessions of an Advertising Man
- Hopkins · Scientific Advertising
- Schwartz · Breakthrough Advertising
- Whitman · Cashvertising
- Sullivan · Hey Whipple Squeeze This
- Bly · The Copywriter's Handbook
- Jon Steel · Truth Lies and Advertising
- Morgan · Eating the Big Fish
- Trout · Differentiate or Die
- Moore · Crossing the Chasm

**Why third:** This is the corpus's biggest blind spot. Positioning phrases and distribution mechanics are already strong in derived intel · adding the primary sources locks them down.

### BATCH_008 · AI/tech + hybrid-operator defense canon (10 books)

**Sources:**
- Balaji · The Network State
- Dixon · Read Write Own
- Agrawal et al · Power and Prediction
- Agrawal et al · Prediction Machines
- Daugherty/Wilson · Human + Machine
- Lakhani/Iansiti · Competing in the Age of AI
- Suleyman · The Coming Wave
- Mollick · Co-Intelligence
- Tegmark · Life 3.0
- Davenport/Kirby · Only Humans Need Apply (the .rar/epub)

**Why fourth:** Anchors the hybrid-operator AI sentiment with primary sources. Defends the Camp B routing rule.

### BATCH_009 · Lineage doctrine + hip-hop / culture canon (8 sources)

**Sources:**
- Charnas · Dilla Time
- Charnas · The Big Payback
- Reynolds · Supreme Models
- Stoute · The Tanning of America (already done · re-reference, do not re-chunk)
- Rick Ross · Hurricanes
- Gucci Mane · Autobiography
- Jay-Z · Decoded
- Greenburg · Empire State of Mind

**Why fifth:** Grounds the Lineage Doctrine (LOCKED 2026-05-12) in primary-source LA Black founder culture material. Currently the lineage doctrine is named but under-referenced in the chunked corpus.

### Deferred to BATCH_010+

- The Direction Stack v_final PDF (its own batch · 444 MB, likely 100-200 chunks alone)
- VC / investing canon (Cat E · 12 books · medium load-bearing for SNIPED)
- The 26 lighting PDFs (per `sniped-lighting-vault` skill, slow-burn vision training, micro-batch)
- Founder + leadership (Cat A operating · Lean Startup, Hard Thing About Hard Things, Blitzscaling)
- Memoirs (Cat G · Coddington, Schwarzenegger, Vreeland, Talley, Schultz, Branson, Frier, Randolph, Isaac, Kelly, Carey)
- Strategy + history canon (Cat H · Machiavelli ×2, Clausewitz, Musashi, Greene Mastery, Greene Laws, 50th Law, Caesar, Herodotus, Thucydides, Aurelius, Napoleon)
- Decision + judgment (Cat I · Kahneman ×2, Noise, Tetlock, Silver, Frankl, Becker, Hoffer, Haidt ×2, Berne, Le Bon)
- Fashion / luxury (Cat J · Dior ×2, Thomas, Kapferer, Agins)
- Consulting / service business (Cat A consulting · Kaufman, Rasiel, Maister, Block, Weiss ×2, Lencioni ×3)
- Operator-engine / community (Cat K · Get Together, Spinks, Anderson ×2, Kelly ×2, Packy McCormick)
- Investing canon (Graham ×2, Klarman, Marks ×2, Mallaby ×2, Schroeder, Housel, Kiyosaki)

---

## 11 · Constraints respected

- No moves, deletes, renames, extractions, or chunk processing performed.
- BATCH_005 NOT started.
- MASTER_INDEX, MASTER_CHUNK_MAP, and ACTIVE_KNOWLEDGE_STATE NOT updated.
- Source folder treated as read-only canonical universe per user instruction.
- `~/AI-Brain-Refinery/raw/` treated as in-progress staging (NOT complete).
- Rest of `~/Downloads/` and `~/sniped-media/` left out of scope.

End of inventory. Next step is to choose between the BATCH_005 photography canon path or to authorize a staging copy pass first.
