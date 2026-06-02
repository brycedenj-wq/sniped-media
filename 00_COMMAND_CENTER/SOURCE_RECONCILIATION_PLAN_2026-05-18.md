# SOURCE RECONCILIATION PLAN · 2026-05-18

Reconciles `~/Downloads/    SNIPED_OS` (legacy canonical OS) against `~/AI-Brain-Refinery/raw/` (staged processing intake). No moves, deletes, renames, or processing performed. Read-only analysis with action recommendations for the next session.

---

## 0 · Correction to the prior inventory

The `SOURCE_LOCATION_MAP_2026-05-18.md` and `RAW_INTAKE_INVENTORY_2026-05-18.txt` files generated earlier today reported:

- 22 basenames unique to `~/Downloads/    SNIPED_OS`
- 18 basenames unique to `~/AI-Brain-Refinery/raw`

Those numbers were **wrong**. The basename extraction step used `xargs -I{} basename {}` which dropped some filenames containing special characters (apostrophes, ampersands, brackets, leading spaces), producing a false-positive uniqueness signal.

Re-running with a robust `sed 's|.*/||'` basename extraction gives the accurate picture:

| Location | Basenames | Common with the other | Unique |
|---|---:|---:|---:|
| `~/Downloads/    SNIPED_OS` | 369 | 354 | **15** |
| `~/AI-Brain-Refinery/raw` | 375 | 354 | **21** |

The 10 canon books listed as "unique to SNIPED_OS" in the prior inventory (Status Anxiety, Pricing Creativity, WWP, Blockbusters, Perennial Seller, Naval Almanack, Revenge of Analog, Elephant in the Brain, Hospitality, Company of One) are in fact ALREADY in `~/AI-Brain-Refinery/raw/03_TIER_2_CANON_BOOKS/` and were ingested in BATCH_003. Likewise the 7 YTDown YouTube photographer mp4s exist in BOTH locations under `PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /`. No action is needed on any of those.

The remainder of this plan uses the corrected lists.

---

## 1 · The 15 files unique to legacy `~/Downloads/    SNIPED_OS`

Grouped by category:

### A · Stale Office lock files (2) · IGNORE

| File | Path | Disposition |
|---|---|---|
| `~$FIGMA.docx` | root | Stale Word lock file. Ignore. Safe to delete from legacy folder at any time (do not copy to raw). |
| `~$iped figma.docx` | root | Stale Word lock file. Ignore. Safe to delete. |

### B · CH01_yae chapter card iterations (9) · SUPERSEDED, DO NOT COPY

| File | Legacy path |
|---|---|
| `CARD · 4_5 · LIGHT · STANDARD.png` | `04_DELIVERABLES/CH01_yae/` |
| `CARD · 4_5 · LIGHT · STANDARD-1.png` | `04_DELIVERABLES/CH01_yae/` |
| `CARD · 4_5 · LIGHT · STANDARD@4x.png` | `04_DELIVERABLES/CH01_yae/` |
| `FLYER · 4_5 MASTER.png` | `04_DELIVERABLES/CH01_yae/` |
| `yae_card_4x5_LIGHT.png` | `04_DELIVERABLES/CH01_yae/cards/` |
| `yae_card_4x5_LIGHT_v3_archival.png` | `04_DELIVERABLES/CH01_yae/cards/` |
| `yae_card_4x5_LIGHT_v3_final.png` | `04_DELIVERABLES/CH01_yae/cards/` |
| `yae_card_4x5_LIGHT_v3_FINAL_3qtr.png` | `04_DELIVERABLES/CH01_yae/cards/` |
| `yae_card_9x16_STORY.png` | `04_DELIVERABLES/CH01_yae/cards/` |

**Why superseded:** The locked Yae chapter cards now live at `~/AI-Brain-Refinery/raw/_archive/chapter_cards/CH01_Yae_2026-05-13/` using the canonical dated naming convention `SNIPED_CH01_Yae_2026-05-13_card_4x5_FINAL.png`. The B&W Card Dual-Register rule was locked 2026-05-13, after these v3 iterations were made. The newer set is the authoritative artifact.

**Cross-store sighting:** The 3 generic `CARD · 4_5 · LIGHT · STANDARD*.png` files also exist in `~/Downloads/SNIPED · Chapter Card Master/` (3 PNGs total, matching the legacy `04_DELIVERABLES` set). That folder is the working scratch area; both copies are pre-rename obsolete.

### C · Dad coach flyer side-quest (4) · OPTIONAL COPY

| File | Legacy path | Disposition |
|---|---|---|
| `coach_eric_jones_welcome_v1.png` | `_side_quests/dad_flyer/` | Side-quest, not SNIPED corpus. |
| `coach_eric_jones_welcome_v2.png` | `_side_quests/dad_flyer/` | Side-quest. |
| `coach_eric_jones_welcome_v3_with_headshot.png` | `_side_quests/dad_flyer/` | Side-quest. |
| `coach_eric_jones_welcome_FINAL.png` | `_side_quests/dad_flyer/` | Side-quest, FINAL version. |

These are a personal favor / side project (a welcome flyer for "Coach Eric Jones"). They live in the legacy folder's `_side_quests/` chamber which `~/AI-Brain-Refinery/raw/` does not mirror. **Default recommendation: leave in legacy folder.** They are not SNIPED corpus material, do not feed any batch, and do not need to be in the active processing tree. If you want them preserved alongside the active corpus for traceability, copy `_side_quests/dad_flyer/` whole to `raw/_archive/side_quests/dad_flyer/` later; not required for BATCH_005.

---

## 2 · The 21 files unique to `~/AI-Brain-Refinery/raw`

Grouped by category:

### A · Tier 1 canon book additions (19) · ALREADY CORRECTLY FILED · NO ACTION

All 19 of these live under `raw/02_TIER_1_CANON_BOOKS/` and were already ingested in BATCH_002. The earlier inventory missed them because their filenames have a leading space or bracketed prefix that the previous basename extractor dropped.

| # | Title | File |
|--:|---|---|
| 1 | Cold Start Problem | ` Andrew Chen - The Cold Start Problem_ ... - libgen.li.epub` |
| 2 | The Everything Store | ` Brad Stone - The Everything Store_ ... - libgen.li.epub` |
| 3 | Poor Charlie's Almanack | ` Charles T. Munger - Poor Charlie's Almanack_ ... - libgen.li.epub` |
| 4 | Working Backwards | ` Colin Bryar_ Bill Carr - Working Backwards ... - libgen.li.epub` |
| 5 | Hit Makers | ` Derek Thompson - Hit Makers_ ... - libgen.li.epub` |
| 6 | Creativity, Inc. | ` Ed Catmull, Amy Wallace - Creativity, Inc._ ... - libgen.li.epub` |
| 7 | Genghis Khan and the Making of the Modern World | ` Jack Weatherford - Genghis Khan ... - libgen.li.epub` |
| 8 | DisneyWar | ` James B. Stewart - DisneyWar _ ... - libgen.li.epub` |
| 9 | The Song Machine | ` John Seabrook - The Song Machine_ ... - libgen.li.epub` |
| 10 | Zero to One | ` Peter Thiel, Blake Masters - Zero to One_ ... - libgen.li.epub` |
| 11 | Shoe Dog | ` Phil knight - Shoe dog (0) - libgen.li.mobi` |
| 12 | The Ride of a Lifetime | ` Robert Iger_ Joel Lovell - The Ride of a Lifetime_ ... - libgen.li.epub` |
| 13 | The Tanning of America | ` Stoute, Steve - The Tanning of America_ ... - libgen.li.epub` |
| 14 | Steve Jobs | ` Walter Isaacson - Steve Jobs Walter Isaacson (2011) - libgen.li.epub` |
| 15 | The Outsiders | ` William N. Thorndike - The Outsiders_ ... - libgen.li.epub` |
| 16 | Alexander the Great | `[Alexander the Great 1 ] Freeman, Philip - Alexander the Great (2016) - libgen.li.epub` |
| 17 | The 48 Laws of Power | `[Baker & Taylor Books (Firm)._ Axis 360] Robert Greene_ ... 48 Laws of Power ... - libgen.li.epub` |
| 18 | The 33 Strategies of War | `[Joost Elffers Books ] Greene, Robert - The 33 Strategies of War ... - libgen.li.epub` |
| 19 | The Art of War | `ArtOfWar.pdf` |

**Status:** all 19 are properly placed in `raw/02_TIER_1_CANON_BOOKS/` and are referenced in `BATCH_002_CHUNKS.jsonl`. No action.

### B · Recent intake (1) · KEEP, OPTIONAL RELOCATION

| File | Current path | Notes |
|---|---|---|
| `GETHOOKD_AD_SWIPES_2026-05-16.md` | `raw/GETHOOKD_AD_SWIPES_2026-05-16.md` (root) | Newer than the legacy OS snapshot. Lives at raw root instead of under a chapter. Likely belongs under `raw/07_CONTENT/` or `raw/03_OUTREACH/` once you decide. Not blocking. |

### C · Anomaly · misfiled docx (1) · FLAG

| File | Current path | Issue |
|---|---|---|
| `mostly Powerhouse-.docx` | `raw/02_TIER_1_CANON_BOOKS/mostly Powerhouse-.docx` | A loose .docx sitting inside a folder that otherwise contains only canon book .epub / .pdf / .mobi files. Name suggests a working draft, not a canon book. Either move it out (likely to `raw/_archive/` or `raw/99_VAULT/`) or, if it is genuinely a book excerpt, rename it to make that clear. Do not touch until you confirm what it is. |

---

## 3 · Files to copy INTO `~/AI-Brain-Refinery/raw/` from legacy

Recommended copies before BATCH_005:

**None required.** The reconciliation reveals no canonical material in legacy that is missing from raw. Every canon book, every YTDown video, every photography reference is already present in raw.

**Optional (low priority, defer):** the 4 `coach_eric_jones_welcome_*.png` side-quest files (1.C above). Only if you want side-quests mirrored into the active processing tree for archival traceability. Suggested destination: `raw/_archive/side_quests/dad_flyer/`. Not needed for any batch.

---

## 4 · Files to ignore as stale, lock files, videos, or superseded

| Category | Count | Files | Reason |
|---|---:|---|---|
| Stale Office lock files | 2 | `~$FIGMA.docx`, `~$iped figma.docx` | Auto-generated Word/Office lock files. Never useful. Safe to delete at any time. |
| Superseded CH01_Yae card iterations | 9 | Legacy `04_DELIVERABLES/CH01_yae/` set (see 1.B) | Replaced by `raw/_archive/chapter_cards/CH01_Yae_2026-05-13/` set under the canonical dated naming convention. Locked 2026-05-13 with the B&W Card Dual-Register rule. |
| Working-scratch chapter cards in Downloads | 3 | `~/Downloads/SNIPED · Chapter Card Master/CARD · 4_5 · LIGHT · STANDARD*.png` | Pre-rename copies of the same superseded set. Also obsolete. |
| YTDown YouTube photographer mp4s | 7 | The Avedon / Helmut Newton / Lindbergh / Sarah Moon ×3 / Tim Walker set | Already in raw at `PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /`. Not unique. The prior inventory was wrong to flag these. |
| Canon books already in raw/03_TIER_2 | 10 | Status Anxiety, Pricing Creativity, WWP, Blockbusters, Perennial Seller, Naval Almanack, Revenge of Analog, Elephant in the Brain, Hospitality, Company of One | Already ingested in BATCH_003. The prior inventory miscounted because of the basename extractor bug. |

**Net legacy folder cleanup recommendation (NOT to execute now):** once BATCH_005 has run and confirmed nothing else is needed from the legacy folder, the entire `~/Downloads/    SNIPED_OS/` tree becomes archive-eligible. Do not delete preemptively. A single tarball snapshot before deletion is the right move when the time comes.

---

## 5 · Duplicate-risk warnings

### W1 · Chapter card material exists in three locations
1. `~/Downloads/    SNIPED_OS/04_DELIVERABLES/CH01_yae/` · 9 files · superseded
2. `~/Downloads/SNIPED · Chapter Card Master/` · 3 files · pre-rename copies of 3 of the above
3. `~/AI-Brain-Refinery/raw/_archive/chapter_cards/CH01_Yae_2026-05-13/` · canonical, dated, with B&W variant

**Risk:** confusion or accidental re-import of the v3 set if naming gets reused.
**Action:** treat raw `_archive/chapter_cards/CH01_Yae_2026-05-13/` as the only source of truth. Do not reference the other two for live work.

### W2 · Legacy folder retains an `04_DELIVERABLES/` chapter that raw does NOT mirror
`raw/` skips a `04_DELIVERABLES` folder. The `04_` slot in raw is `04_CRM`. The legacy folder uses `04_DELIVERABLES`. This is a structural delta to be aware of when reconciling chapter numbering, but does not block anything · the deliverables material was all superseded chapter card iterations (see 1.B), so no migration of chapter folder is needed. The naming-collision risk is purely conceptual.

### W3 · Two folders in `~/Downloads/` claim to be "Sniped Media" sources
- `~/Downloads/Sniped Media/` · 42 MB
- `~/Downloads/SM/` · 41 MB

Near-identical size and naming suggest duplicates. Neither has been folded into `raw/` or examined in this pass. Treat as a future triage item, not blocking for BATCH_005.

### W4 · Three identical Two-Look Moodboard Packs at `~/Downloads/` root
`Two-Look-Moodboard-Pack/`, `Two-Look-Moodboard-Pack (2)/`, `Two-Look-Moodboard-Pack (2) 2/` are 8.1 MB each. Same content, three copies. Cleanup-eligible after one is selected as canonical. Not blocking.

### W5 · `~/AI-Brain-Refinery/raw/02_TIER_1_CANON_BOOKS/` contains 1 non-book file
`mostly Powerhouse-.docx` (see 2.C). A stray docx inside a folder of canon book epubs/pdfs/mobis. Worth flagging before any tier-1-folder-wide operation runs.

### W6 · `~/AI-Brain-Refinery/raw/` root contains a loose recent file
`GETHOOKD_AD_SWIPES_2026-05-16.md` lives at raw root rather than under a chapter. Belongs under `07_CONTENT/` or `03_OUTREACH/`. Defer the move decision but do not let it drift further.

### W7 · Empty chapter folders in raw
`raw/09_ART_SERIES/`, `raw/11_LEGAL/`, `raw/12_FINANCIAL/` are empty (no files). The legacy folder has non-empty versions of all three. If any of those chapters need to feed a future batch, they need to be populated from legacy (or marked intentionally empty).

---

## 6 · Recommended corrected source hierarchy going forward

Lock these three roles cleanly:

### Tier 1 · `~/AI-Brain-Refinery/raw/` · the staged processing intake (PRIMARY · editable)
- The single editable surface for active corpus work.
- All new doctrine docs, swipe files, intel pulls, and book additions land here first.
- All BATCH_NNN processing reads from this tree.
- Maintain the chapter structure (`00_BRIEF/` through `99_VAULT/` plus `02_TIER_1_CANON_BOOKS/`, `03_TIER_2_CANON_BOOKS/`, `_archive/`, `_inbox/`, `_skills/`).
- Loose files at the root (`GETHOOKD_AD_SWIPES_2026-05-16.md`, `mostly Powerhouse-.docx`) are technical debt; let them accumulate at most as a small queue, drain to chapters before each new batch.

### Tier 2 · `~/Downloads/    SNIPED_OS/` · the legacy canonical OS (READ-ONLY snapshot)
- Treat as a frozen reference snapshot from before the Refinery move.
- Do not edit. Do not add to it.
- After BATCH_005 confirms no further lifts are needed, snapshot as a tarball and remove from active disk.
- The folder name's 4 leading spaces are an annoyance; rename only when you delete (no benefit to renaming a frozen folder).

### Tier 3 · `~/Downloads/` (everything else) · the raw intake surface (UNCURATED)
- Where browser downloads, Slack/email exports, screenshots, vendor zips, and book pulls land.
- Triage in passes, never bulk-move into raw.
- Specific known piles still to triage: `SNIPED_PRODUCTION/` (2.9 GB shoot pipeline), `SNIPED · Chapter Card Master/` (working scratch), `Sniped Media/` + `SM/` (likely duplicates), `BASEPLATE/` (doctrine doc dump), `SnipedMedia_SOPs_CLEAN_DOCX/` (SOP pack), root-level book pulls (~150 epub/pdf since the last sweep).

### Tier 4 · `~/sniped-media/` · website codebase (NOT a corpus source)
- Treat as a frontend code project. Hands off the codebase.
- The 86 loose `*.docx`/`*.md`/`*.pdf` at the project root are legacy doctrine doc dumps. Most are likely already represented in raw or legacy SNIPED_OS. Only mine selectively if a specific doc is named.

### Tier 5 · Out-of-scope drives or cloud
- If "Sniped Media Business Files" exists outside `~`, it has not been seen by this session. Confirm before relying on it.

---

## 7 · Recommended BATCH_005 choice after reconciliation

`ACTIVE_KNOWLEDGE_STATE.md` already names the next batch:

> **Next batch (recommended, not executed): BATCH_005 · Photography canon at depth**

Reconciliation confirms this is the right call. Reasoning:

1. **Operational corpus complete.** BATCH_001 (SNIPED OS) + BATCH_004 (depth-fill) covered the operating spine. Strategy + memoir canon covered by BATCH_002. Pricing / hospitality / status / leverage canon covered by BATCH_003. The next density gap is **photography craft + photographer studies**, which currently exists in chunks only via the BATCH_001 sampled photographer studies (Leibovitz + Haas in BATCH_001, 7 more art-series .md files deferred to BATCH_002 Pri 3 and never executed).

2. **Source pile is already staged.** Photography material in raw:
   - `raw/PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /` · 1.2 GB · the photo reference vault (Eggleston Guide, Robert Frank Americans, Stephen Shore Uncommon Places, Ernst Haas, Avedon journal, Fred Herzog journal, Robert Frank Art Book + 7 YTDown photographer films).
   - `raw/10_REFERENCE/lighting_pdfs/` · 28 MB · 26-PDF lighting + posing + vision vault.
   - `raw/09_ART_SERIES/` · empty · needs the 9 Art_Series_*.md files copied in from legacy or `~/sniped-media/` root before extraction (they are deferred BATCH_002 Pri 3 items).

3. **No reconciliation blockers.** Section 3 above confirms zero required copies from legacy → raw before BATCH_005 can run. Optional side-quest copy can be deferred indefinitely.

4. **Scope shape** (sketch only, to be locked in `BATCH_005_PLAN.md` next session):
   - **Pri 1:** the 9 `Art_Series_*.md` files (Avedon, Eggleston, Leibovitz already done, Shore, Herzog, Frank, Meyerowitz, Iturbide, Haas already done, plus the Art_Series.docx wrapper).
   - **Pri 2:** the 7 photography reference PDFs in `PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /` (Eggleston Guide, Americans, Uncommon Places, Ernst Haas in Black and White, Avedon journal, Fred Herzog journal, Art Book on Robert Frank).
   - **Pri 3:** thematic mining of the 8 YTDown mp4 photographer films via existing transcripts or single-pass viewing notes (NOT raw mp4 ingestion · the chunks live in the operator's interpretation, not the audio).
   - **Pri 4 (deferred):** the 26 lighting PDFs in `lighting_pdfs/` · slow-burn vision training per `sniped-lighting-vault` skill stance, NOT a binge target. Probably its own micro-batch later.
   - **Skip from this batch:** Direction Stack PDF (BATCH_002 Pri 5 separate canonical confirmation), Two-Look-Moodboard-Pack (not canon).

5. **Pre-BATCH_005 housekeeping (5-minute task, not blocking):**
   - Decide whether `GETHOOKD_AD_SWIPES_2026-05-16.md` moves out of `raw/` root before extraction.
   - Decide whether `mostly Powerhouse-.docx` exits `raw/02_TIER_1_CANON_BOOKS/` (it is not a canon book).
   - Populate `raw/09_ART_SERIES/` with the 9 Art_Series_*.md files (they currently live in legacy SNIPED_OS root and in `~/sniped-media/` root). This IS a legacy→raw copy step, but it was already on the deferred-Pri-3 list from BATCH_002 · not new scope from this reconciliation.

---

## Summary

- The prior inventory's "22 / 18" numbers were inflated by a basename-extractor bug. Correct counts: 15 unique to legacy, 21 unique to raw.
- Of the 15 legacy-only files, 11 are stale / superseded, 4 are an optional side-quest copy. Zero required copies into raw.
- Of the 21 raw-only files, 19 are already correctly filed canon books from BATCH_002, 1 is a recent intake at raw root, 1 is a misfiled docx to flag.
- The legacy folder is now read-only by policy. Raw is the only editable corpus surface.
- BATCH_005 = photography canon at depth. Source pile already staged. No reconciliation blockers.

No moves, deletes, renames, or processing performed. End of plan.
