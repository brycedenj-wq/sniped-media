# SOURCE LOCATION MAP · 2026-05-18

Snapshot of where SNIPED-related material currently lives. Read-only inventory. No moves, deletes, or extractions performed.

## Critical discrepancies vs the original request

| Requested path | Actual status |
|---|---|
| `~/Downloads` | Exists. 2,460 top-level entries · 8,258 files recursive · ~14 GB+ across major subfolders. |
| `~/SNIPED_OS` | **Does NOT exist at this path.** The actual older OS dump is at `~/Downloads/    SNIPED_OS` (note: 4 leading spaces in the folder name). |
| `~/AI-Brain-Refinery/raw` | Exists. 484 files. Mirrors SNIPED_OS chapter structure plus added book/reference material. |
| `~/Sniped Media Business Files` | **Does NOT exist** at any casing or location under `~`. Closest candidates are `~/Downloads/Sniped Media/` (42 MB) and `~/sniped-media/` (a website codebase, 8,151 files). |

Search across `~` (depth 2) confirms no other directory matches `*sniped*`, `*business*files*`, or `*OS*` besides the entries listed below.

---

## A · ~/Downloads · raw intake pile

- **File count:** 8,258 recursive · 2,409 loose at root · 2,460 entries (files+dirs) at top level.
- **Disk:** ~14 GB+ across major subfolders.
- **Recent activity:** 356 files modified at the root level within the last 14 days. Active intake surface.
- **Major file types (recursive):** docx 585 · md 468 · jpg 423 · pdf 418 · png 349 · epub 174 · heic 162 · dng 152 · tif 88 · mp4 81 · jpeg 75 · zip 62 · xlsx 51 · csv 40 · xmp 30 · mobi 28 · jsx 28 · js 21.
- **Root-level loose files (NOT inside subdirs):** 2,409 files. Top exts: docx 455 · jpg 371 · pdf 333 · png 240 · heic 162 · epub 156 · dng 150 · tif 87. Includes installers (`*.dmg`), screenshots, recent epub/pdf book pulls.
- **Heaviest subdirs:**
  - `SNIPED_PRODUCTION/` · 2.9 GB · production shoot pipeline (raw frames, project files).
  - `    SNIPED_OS/` · 2.6 GB · the legacy SNIPED canonical OS (see C below).
  - `PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /` · 1.2 GB · photo reference book + video collection.
  - `EVOTO EDIT/` · 251 MB.
  - `Sniped Media/` · 42 MB · loose Sniped Media assets (likely older client-facing pile).
  - `SM/` · 41 MB · likely Sniped Media variant or duplicate.
  - `SNIPED · Chapter Card Master/` · 33 MB · chapter card production assets.
  - `BASEPLATE/` · 17 MB · doctrine baseplate doc dump.
  - `SnipedMedia_SOPs_CLEAN_DOCX/` · 560 KB · cleaned SOP docx pack.
  - `Two-Look-Moodboard-Pack` · 3 near-identical copies (8.1 MB each) · obvious duplication.
- **Likely purpose:** Live intake bucket. Receives book downloads, screenshots, shoot exports, packaged SOPs, vendor zips. Not curated.
- **Classification:** Raw intake (active, unsorted).
- **Obvious duplicates by filename only:**
  - `Two-Look-Moodboard-Pack/`, `Two-Look-Moodboard-Pack (2)/`, `Two-Look-Moodboard-Pack (2) 2/` · 3 copies of the same pack.
  - `Claude_AI_Skills_50_Upload_Ready/` and `Claude_AI_Skills_50_Upload_Ready (1)/` · paired duplicates.
  - `3 deliverables/` and `3 deliverables 2/` · paired duplicates.
  - `SnipedMedia_SOPs_CLEAN_DOCX/` and `SOPs/` · same byte size (560 K), likely overlapping content.
  - `Sniped Media/` and `SM/` · adjacent size and naming, probable duplicates.
  - Many root-level files with `(1)`, ` 2.JPG`, or `copy` suffix patterns.
- **Recommended next action:** Triage in passes. (1) Quarantine and de-dupe `Two-Look-Moodboard-Pack`, `Claude_AI_Skills_50_*`, `3 deliverables*`. (2) Route SNIPED-specific subfolders (`    SNIPED_OS`, `SNIPED_PRODUCTION`, `SNIPED · Chapter Card Master`, `Sniped Media`, `SM`, `BASEPLATE`, `SnipedMedia_SOPs_CLEAN_DOCX`) into Refinery once a target structure is locked. (3) Decide whether root-level book epubs/pdfs (~150) should land in `raw/02_TIER_1_CANON_BOOKS` and `raw/03_TIER_2_CANON_BOOKS` or stay in Downloads. **Do not bulk-move yet.**

---

## B · ~/AI-Brain-Refinery · processed corpus + command center

- **File count:** 582 recursive across `00_COMMAND_CENTER/`, `01_KNOWLEDGE_BASE/`, `batches/`, `indexes/`, `outputs/`, `raw/`, `scripts/`.
- **Command Center contents:** `ACTIVE_KNOWLEDGE_STATE.md`, `BATCH_002_INVENTORY.md`, `BATCH_002_PLAN.md`, `BATCH_003_PLAN.md`, `BATCH_004_PLAN.md`, `STEP_005_BUILD_MASTER_INDEX.md`, `DOWNLOADS_INVENTORY_2026-05-18.txt`, plus `batch_logs/`, `decisions/`, `session_saves/`.
- **Outputs to date:** `BATCH_001_CHUNKS.jsonl`, `BATCH_001_SOURCE_INDEX.md`, `BATCH_001_SUMMARY.md` (Batch 1 complete). `batches/batch_001_extracted/` populated.
- **Likely purpose:** The current operating environment. Holds the refined / batch-processed knowledge corpus, batch-extraction artifacts, and the master plan/decision log.
- **Classification:** Processed corpus + active command center.
- **Obvious duplicates:** None at this level. Already-curated naming convention.
- **Recommended next action:** Treat as canonical destination. Future batches (005+) should write here. No structural changes needed yet.

### B.1 · ~/AI-Brain-Refinery/raw · staged intake mirror

- **File count:** 484 recursive · ~1.9 GB.
- **Major file types:** md 253 · docx 80 · pdf 50 · png 37 · epub 35 · mp4 8 · xmp 7 · mobi 2 · azw3 1.
- **Mod-time range observed:** 2026-02-24 → 2026-05-16 (active recent edits).
- **Chapter structure present:** `00_BRIEF`, `01_OFFERS`, `02_CONTRACTS`, `02_TIER_1_CANON_BOOKS`, `03_OUTREACH`, `03_TIER_2_CANON_BOOKS`, `04_CRM`, `05_PRODUCTION`, `06_DELIVERY`, `07_CONTENT`, `08_BOOK`, `09_ART_SERIES` (empty), `10_REFERENCE`, `11_LEGAL` (empty), `12_FINANCIAL` (empty), `13_NETWORK`, `14_WEB`, `99_VAULT`, plus `_archive/`, `_inbox/` (empty), `_skills/`, `books/`, `Claude_AI_Skills_50_Upload_Ready (1)/`, `scripts/`, and the photography books archive `PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /` (1.2 GB).
- **Heaviest subdirs in raw:** `PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /` 1.2 GB · `08_BOOK/` 444 MB · `05_PRODUCTION/` 121 MB · `02_TIER_1_CANON_BOOKS/` 44 MB · `10_REFERENCE/` 28 MB · `03_TIER_2_CANON_BOOKS/` 26 MB.
- **Empty chapters:** `09_ART_SERIES`, `11_LEGAL`, `12_FINANCIAL`.
- **Likely purpose:** Staged copy of SNIPED OS plus book canon, sitting ready for extraction. The structural mirror of `~/Downloads/    SNIPED_OS` with added book canon volumes and recent additions.
- **Classification:** Raw staged intake (one step downstream of Downloads, one step upstream of `batches/`).
- **Obvious duplicates:** Substantial overlap with `~/Downloads/    SNIPED_OS` (108 identical basenames). 18 basenames are unique to raw (added newer canon books, e.g. `ArtOfWar.pdf`, `GETHOOKD_AD_SWIPES_2026-05-16.md`, Cold Start Problem, Everything Store, Charlie Munger, Hit Makers, Zero to One, Steve Jobs, Outsiders, 48 Laws, 33 Strategies, Shoe Dog, Disney War, Song Machine, Creativity Inc, Tanning of America, Ride of a Lifetime, Alexander the Great). 22 basenames are in Downloads/SNIPED_OS but missing from raw (Status Anxiety, Pricing Creativity, WWP Manifesto, Blockbusters, Perennial Seller, Naval Almanack, Revenge of Analog, Elephant in the Brain, Unreasonable Hospitality, Company of One, Robert Frank, Ernst Haas, 7 photographer YTDown mp4s, 2 stale `~$` Office lock files, `access_and_community_architecture.md`).
- **Recommended next action:** Treat as the canonical staging point. Before BATCH_005: (a) decide whether to pull the 22 Downloads/SNIPED_OS-only files into raw (the 7 YTDown mp4s and 12 book epubs/pdfs look like real adds; the 2 `~$` files are stale Office lock files, ignore). (b) Decide whether the 18 raw-only book additions should also be reflected back into the legacy OS folder or remain only here. (c) Do not bulk re-copy until intent is set.

---

## C · ~/Downloads/    SNIPED_OS · older canonical OS (legacy)

NOTE: The folder name begins with **four space characters** ("    SNIPED_OS"). Quote the path or escape spaces when scripting.

- **File count:** 480 recursive · 2.6 GB.
- **Major file types:** md 252 · docx 81 · png 50 · pdf 49 · epub 18 · mp4 8 · ds_store 8 · xmp 7 · sh 3 · zip 1 · xlsx 1 · mobi 1 · azw3 1.
- **Structure present:** Full chapter set · `00_BRIEF`, `01_OFFERS`, `02_CONTRACTS`, `03_OUTREACH`, `04_CRM`, `04_DELIVERABLES`, `05_PRODUCTION`, `06_DELIVERY`, `07_CONTENT`, `08_BOOK`, `09_ART_SERIES`, `10_REFERENCE`, `11_LEGAL`, `12_FINANCIAL`, `13_NETWORK`, `14_WEB`, `99_VAULT`, plus `_archive/`, `_inbox/`, `_side_quests/`, `_skills/`. Has an extra `04_DELIVERABLES/` chapter that raw does not.
- **Mod-time range observed:** 2026-02-24 → 2026-05-17 (still receiving edits).
- **Likely purpose:** The older / "production" SNIPED operating system corpus. The source the Refinery raw pile was largely derived from.
- **Classification:** Canonical OS · legacy / source of truth for older docs.
- **Obvious duplicates:** Heavy overlap with `~/AI-Brain-Refinery/raw/` (108 identical basenames). Also contains 2 stale Office lock files (`~$FIGMA.docx`, `~$iped figma.docx`) safe to ignore.
- **Recommended next action:** Hold position. Do not edit in-place. Once Refinery raw has fully absorbed the legacy OS, this folder becomes archive-eligible · but only after confirming the 22 Downloads-only basenames are accounted for (see B.1 notes) and the `04_DELIVERABLES/` chapter contents have been reviewed. Consider renaming the folder to drop the leading spaces if the path is going to be referenced from scripts.

---

## D · ~/sniped-media · website codebase + legacy doc dump (CANDIDATE for "Sniped Media Business Files")

- **File count:** 8,151 recursive.
- **Major file types:** js 1,456 · map 430 · ts 134 · md 109 · json 109 · jpg 93 · jsx 86 · woff2 73 · docx 66 · css 35 · png 29 · cts 26 · mts 25.
- **Top-level dirs:** `new website/`, `SNIPED OVERLAYS/`, `sniped-media copy/`, `sniped-media/` (self-nested).
- **Root-level loose docs:** 86 docx + md + pdf files at root (e.g. `000_MASTER_OVERRIDE_BASEPLATE.docx`, `Aesthetic_Statement_v1.docx`, `7_Powers_Strategic_Power_FRAMEWORKS.docx`, all `Art_Series_*.md` 1-9 incl. duplicate `Art_Series_6_RobertFrank (1).md`, web component `.jsx` files like `HomePage.jsx`, `AboutPage.jsx`, `ContactPage.jsx`, `Footer.jsx`, `caseStudies (1).js`, `index.html`).
- **Likely purpose:** Web project codebase (Next/React-style with `node_modules`-driven js/ts/map counts) plus a legacy flat dump of business doctrine docs at the root. Possibly the "Business Files" location the user mentioned, sitting alongside the website source.
- **Classification:** Mixed · codebase (the vast majority of file count) + legacy archive of older doctrine docs at root.
- **Obvious duplicates:** `Art_Series_6_RobertFrank (1).md` next to `Art_Series_6_RobertFrank.md`. `Baseplate_Exploration_Notes (1).docx`. `Content_Strategy (1).docx`. `Homepage_Copy_V1.docx` + `Homepage_Copy_V2.docx`. `sniped-media/` and `sniped-media copy/` likely whole-tree duplicates.
- **Recommended next action:** Confirm with user whether this is what they meant by "Sniped Media Business Files." Do not touch codebase. Earmark the 86 root-level docx/md/pdf for review · most likely already represented in `~/Downloads/    SNIPED_OS` and `~/AI-Brain-Refinery/raw`, but cross-check before declaring redundant.

---

## Cross-store filename overlap summary

| A | B | Common basenames | Unique to A | Unique to B |
|---|---|---|---|---|
| `~/Downloads/    SNIPED_OS` | `~/AI-Brain-Refinery/raw` | 108 | 22 | 18 |

The `~/sniped-media` root and `~/Downloads` root were not exhaustively cross-compared in this pass · noted only as obvious-by-eye duplicates above.

---

## Open questions for the operator

1. Is `~/sniped-media` what was meant by "Sniped Media Business Files," or does an older external-drive / cloud copy still exist?
2. The legacy OS folder at `~/Downloads/    SNIPED_OS` was edited as recently as 2026-05-17 · is it still being actively edited, or is Refinery `raw/` now the single editable surface?
3. The 22 Downloads-only basenames include ~12 canon book pulls (Status Anxiety, WWP, Blockbusters, Perennial Seller, Naval, Revenge of Analog, Elephant in the Brain, Hospitality, Company of One, Robert Frank, Ernst Haas) and 7 photographer YTDown mp4s. Want them pulled into `raw/` before BATCH_005?

No moves, deletes, or processing performed. End of map.
