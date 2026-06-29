# RETIREMENT APPROVAL PACKET , Source Cold-Archive (Waves 001 + 001-B)

**Date:** 2026-06-19. **Status:** REVIEW ONLY. Nothing has been copied, moved, renamed, deleted, or archived. This packet exists so you can approve later. Source of truth: the per-wave `SOURCE_RETIREMENT_RECEIPTS.csv` files and `RETIREMENT_PLAN_001.md`.

## TL;DR , the honest size reality (answer to: is 591.9 MB meaningful?)

**No. 591.9 MB of books is not the real cleanup target. It is about 2 percent of the footprint.** Measured with `du` on 2026-06-19:

| Location | Size | Note |
|---|---:|---|
| AI-Brain-Refinery repo (total) | 31 GB | the actual disk hog |
| , .git (one pack file) | 6.8 GB | binary assets committed into git history |
| , 00_COMMAND_CENTER | 14 GB | production folders (see below) |
| , ALMA_LOVE_PRODUCTION_001 | 7.4 GB | incl. EVOTO .tif masters 150-212 MB each |
| , raw/ (staged mirror) | 2.7 GB | duplicate intake mirror |
| SNIPED_OS corpus (total) | 4.6 GB | source universe |
| THIS packet's 42 COLD_ARCHIVE_OK books | 591.9 MB | the small stuff |

By media type across the repo: **.png 8.7 GB, .mp4 7.5 GB, .tif 3.3 GB, .jpg 0.8 GB, .mov 0.4 GB** (about 20 GB of media). The fat is generated/rendered production assets and git history, not books.

**Biggest real targets (orders of magnitude bigger than the books):**
1. **My own Wave 001/001-B temp artifacts , ~1.35 GB , SAFE to delete now** (derived scratch, the active forms are already extracted): `OS_GAP_CLOSURE_WAVE_001B/_render` 1.0 GB, `/_ocr_pdf` 167 MB, `/_ocr_src` 124 MB, `OS_GAP_CLOSURE_WAVE_001/_render` 62 MB. Not sources, not originals.
2. **.git pack 6.8 GB** , binary assets were committed; reclaimable only by history rewrite (BFG / git filter-repo). Advanced and irreversible; separate decision.
3. **Production folders in 00_COMMAND_CENTER:** ALMA_MARGIELA_SAVE_001 5.7 GB, SYNERGY_HOMECARE_TEST_001 1.9 GB (a DEMOTED project), ALMA_EDITOR_HANDOFF_001 1.1 GB, OVERNIGHT_PRIME_MOVER 572 MB, postproduction 509 MB, AXIS_ELITE_DEMO 343 MB (AXIS is RETIRED).
4. **ALMA_LOVE_PRODUCTION_001 'New Folder With Items' 4.1 GB** incl. EVOTO .tif masters; **video renders 7.5 GB** (many intermediate v2/v3/silent_cut cuts).

These are PRODUCTION assets (renders, masters, project files), not corpus sources, so they are out of scope for the source-retirement gate. They need a separate production-asset cleanup pass with their own keep/archive decisions. I did not measure backups; confirm an external/cloud backup exists before removing any production master.

## The 42 COLD_ARCHIVE_OK sources , exact paths, grouped by folder (total 591.9 MB)

### `/Users/sniper/Downloads/    SNIPED_OS/` , 12 files, 489.4 MB
- 104.4 MB , `[Maus Series _1] Art Spiegelman - Maus I A Survivor's Tale My Father Bleeds History _1 (1986, Penguin Books) - libgen.li.epub`
- 77.4 MB , `[Maus Series _2] Art Spiegelman - Maus II A Survivor's Tale And Here My Troubles Began _2 (1992, Penguin Books) - libgen.li.epub`
- 69.9 MB , ` Lovell, Sophie - Dieter Rams_ As Little Design as Possible (2011, Phaidon Press) - libgen.li.epub`
- 53.4 MB , `Story{Robert McKee}{115577124} libgen.li.pdf`
- 52.2 MB , `John Caples, David Ogilvy - Tested Advertising Methods (4th Ed.) - libgen.li.pdf`
- 48.3 MB , `pdfcoffee.com_virgil-abloh-figures-of-speech-pdf-free.pdf`
- 41.8 MB , `Annie Leibovitz - Annie Leibovitz at Work (2008, Random House) - libgen.li.epub`
- 14.6 MB , `Shore Stephen. - Uncommon Places_ The Complete Works - libgen.li.pdf`
- 9.3 MB , `257683787-Cartier-Bresson-H-1952-the-Decisive-Moment.pdf`
- 8.8 MB , `367490464-Szarkowski-1973-Looking-at-Photographs-pdf.pdf`
- 8.5 MB , `John Szarkowski - William Eggleston's Guide (2002, The Museum of Modern Art, New York) - libgen.li.pdf`
- 0.8 MB , `pdfcoffee.com_ernst-haas-pdf-free.pdf`

### `/Users/sniper/Downloads/    SNIPED_OS/PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /` , 3 files, 75.2 MB
- 30.2 MB , ` Stephen Shore, Lynne Tillman, Stephan Schmidt-Wulffen - Stephen Shore_ Uncommon Places_ The Complete Works (2015, Aperture) - libgen.li.pdf`
- 27.0 MB , ` Robert Frank, Jack Kerouac - The Americans (2008, Steidl) - libgen.li.pdf`
- 18.0 MB , `Ernst Haas in Black and White{Jim Hughes_ Alexander Haas_ Ernst Haas}(1992, Bulfinch Press){115446337} libgen.li.pdf`

### `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/lighting_pdfs/` , 25 files, 26.1 MB
- 1.4 MB , `Lecture+20+related.+Standard-Group-Shot.pdf`
- 1.3 MB , `Lecture+7+related.+A+5-Light-Studio-Setup.pdf`
- 1.2 MB , `Lecture+9+related.+4-Light-Beauty-On-White.pdf`
- 1.2 MB , `Lecture+21+related.+Standard-Couples.pdf`
- 1.1 MB , `Lecture+10+related.+Broad-Lighting.pdf`
- 1.1 MB , `Lecture+7+related.+Butterfly-Lighting.pdf`
- 1.1 MB , `Lecture+7+related.+Main-Key-Light.pdf`
- 1.1 MB , `Lecture+5+related.+Open-Loop-Example.pdf`
- 1.1 MB , `Lecture+7+related.+White-Background.pdf`
- 1.1 MB , `Lecture+18+related.+The-Male-Light-Pose.pdf`
- 1.1 MB , `Lecture+6+related.+Closed-Loop-Example.pdf`
- 1.1 MB , `Lecture+7+related.+2-Light-Clamshell.pdf`
- 1.1 MB , `Lecture+2+related.+Home-Based-Studio.pdf`
- 1.0 MB , `Lecture+5+related.+One-Light-45-Degree-Beauty-Dish.pdf`
- 1.0 MB , `Lecture+9+related.+Short-Lighting.pdf`
- 1.0 MB , `Lecture+17+related.+Stretch-Things-Forward-Female.pdf`
- 1.0 MB , `Lecture+11+related.+Rembrandt-Lighting.pdf`
- 1.0 MB , `Lecture+8+related.+3-Light-Commercial.pdf`
- 1.0 MB , `Lecture+19+related.+The-Female-Shadow-Pose.pdf`
- 1.0 MB , `Lecture+8+related.+Split-Lighting.pdf`
- 0.9 MB , `Lecture+16+related.+45-Degree-Angle-Slims-Body.pdf`
- 0.9 MB , `Lecture+7+related.+Fill-Light.pdf`
- 0.9 MB , `Lecture+7+related.+Rim-Hair-Light.pdf`
- 0.9 MB , `Lecture+10+related.+Hollywood-3-Light.pdf`
- 0.6 MB , `Lecture+6+related.+Creative-Window-Light.pdf`

### `/Users/sniper/Downloads/    SNIPED_OS/99_VAULT/_corpus_inventory/review_completion_work/docx_txt/` , 1 files, 1.2 MB
- 1.2 MB , `cold_out_reach_instantly_gold_everything_use_this_.txt`

### `/Users/sniper/Downloads/    SNIPED_OS/99_VAULT/_corpus_inventory/review_completion_work/b2_txt/` , 1 files, 0.0 MB
- 0.0 MB , `cold_out_reach_instantly_gold_everything_use_this_alway.txt`

## DO_NOT_DELETE (1)
- `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/post_pipeline/SHOOTS/_TEST_alma-love_proof/CAMPAIGN_DIRECTION/ALMA_DROP_ENGINE_DECK.pdf` (1.2 MB) , project original-of-record (ALMA deck). Keep in place.

## DELETE_ELIGIBLE (1)
- `/Users/sniper/Downloads/    SNIPED_OS/Coddington, Grace - Grace_ A Memoir (2012, Random House Publishing Group) - libgen.li.epub` (0 MB, 0-byte corrupt) , holds nothing. Delete only on your word; or re-download a valid copy.

## Total size by source folder (COLD_ARCHIVE_OK only)
| folder | files | MB |
|---|---:|---:|
| `...SNIPED_OS` | 12 | 489.4 |
| `...SNIPED_OS/PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING ` | 3 | 75.2 |
| `...SNIPED_OS/10_REFERENCE/lighting_pdfs` | 25 | 26.1 |
| `...SNIPED_OS/99_VAULT/_corpus_inventory/review_completion_work/docx_txt` | 1 | 1.2 |
| `...SNIPED_OS/99_VAULT/_corpus_inventory/review_completion_work/b2_txt` | 1 | 0.0 |

## Recommended cold-archive destination options
- **A. External drive (best):** `/Volumes/<YourDrive>/SNIPED_COLD_ARCHIVE/2026-06-19_gapclosure/` , gets the bytes fully off the Mac. You name the volume.
- **B. Cloud archive:** Backblaze B2 / iCloud Archive / Google Drive folder , off-device, but a paid/connected service (no spend without your go).
- **C. On-Mac holding folder (weakest):** `~/SNIPED_COLD_ARCHIVE/` , reclaims nothing until later off-loaded; only useful as a staging step.
- For 591.9 MB, honestly any of these is fine; the books are small. The destination decision matters far more for the 20 GB of production media.

## Copy-verify-remove procedure (only after approval, I will not run it unprompted)
1. COPY each source to the chosen destination (preserve the relative path).
2. VERIFY: recompute md5 of the copy and diff against the md5 in `SOURCE_RETIREMENT_RECEIPTS.csv`. Abort that file if mismatch.
3. Only after a verified copy exists, REMOVE the Mac original.
4. Log each move (source, dest, md5, timestamp) to a RETIREMENT_EXECUTION_LOG.csv.
5. Re-run `os_checkpoint.py` to confirm manifest still consistent (statuses already read_verified; paths now point to archive).
Never move-then-hope. Never delete before a verified copy exists.

## Risk notes
- All 42 are libgen/scrape copies (replaceable); the OS already holds their signal in `_reference/` active forms with retrieval tests. Losing the files loses nothing the OS needs.
- If any source is later needed in full (e.g. exact-quote fidelity, or McKee in English not Portuguese), re-download; do not rely on the cold archive being the only copy unless you trust the destination.
- Confirm the cold-archive destination is itself backed up before removing Mac originals.
- The 2 exceptions below are NOT closed content; do not treat their absence as coverage.

## The 2 open exceptions , exact recovery ask
**1. Missing screen-recording (needs_transcription).**
- Path on record: `/Users/sniper/Downloads/    SNIPED_OS/ai-celebrity-content-blueprint_default-title_4d1c7250b2884530/ScreenRecording_03-30-2026 20-20-17_1.MP4`
- It is gone from disk (folder holds only 2 .txt files). **Recovery ask: locate the original .MP4** (check macOS Trash, Time Machine, any external drive, or the original 'ai-celebrity-content-blueprint' download). Drop it back at that path (or tell me the new path). Then I transcribe locally (no spend) and whole-read it to close.
**2. Corrupt Coddington 'Grace' epub (needs_ocr).**
- Path: `/Users/sniper/Downloads/    SNIPED_OS/Coddington, Grace - Grace_ A Memoir (2012, Random House Publishing Group) - libgen.li.epub`
- It is 0 bytes (empty/failed download). **Recovery ask: re-download a valid 'Grace: A Memoir' (Grace Coddington, 2012) epub or pdf** to that path. Then I OCR/read it to close. Until then it stays as `exception_corrupt_source`.

## DECISION PAGE , approve later (yes / no each)
| # | Decision | Recommended | Your call |
|---|---|---|---|
| A | Cold-archive the 42 COLD_ARCHIVE_OK books (591.9 MB) via copy-verify-remove, to a destination I name | YES, low value but harmless | ____ |
| B | Delete my Wave temp render/OCR artifacts now (~1.35 GB, derived scratch, not sources) | YES, easiest real reclaim, zero risk | ____ |
| C | Open a separate PRODUCTION-ASSET cleanup wave for the ~20 GB media + demoted-project folders (SYNERGY 1.9 GB, AXIS 343 MB) | YES, this is where the space actually is | ____ |
| D | Investigate the 6.8 GB .git pack (history rewrite to drop committed binaries) | LATER, advanced + irreversible, needs care | ____ |
| E | Delete the 0-byte Coddington corrupt file | YES once you accept re-download is the only recovery | ____ |
| F | Recover the 2 exception files (you locate/re-download, I close them) | YES if the content matters; otherwise leave as exceptions | ____ |

Nothing happens until you mark these. I will not copy, move, delete, or archive anything before an explicit go.
