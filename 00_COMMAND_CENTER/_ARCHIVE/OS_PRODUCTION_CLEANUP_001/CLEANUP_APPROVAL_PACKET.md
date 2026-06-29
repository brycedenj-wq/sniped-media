# PRODUCTION-ASSET CLEANUP APPROVAL PACKET 001

**Date:** 2026-06-19. **Status:** C1-step-1 EXECUTED 2026-06-19 (operator-approved, 1.32 GB reclaimed, see `CLEANUP_EXECUTION_LOG.md`). All other buckets remain REVIEW ONLY, nothing else moved, deleted, renamed, or archived. Measured live with `du` / `find`.

## TL;DR
The AI-Brain-Refinery repo is **30 GB** (after the 1.35 GB Wave-scratch delete). By media type: **.png 8.7 GB, .mp4 7.5 GB, .tif 3.3 GB**. The real reclaim is production renders, intermediate cuts, demoted/retired project folders, the source mirror, and review zips. Books (591.9 MB) are noise by comparison.

**Ballpark reclaim if you approve the safe buckets:** roughly **8 to 12 GB** without touching client masters or git history.

## Recommended action per folder (exact paths)

### DO_NOT_DELETE (client masters / active client work)
| Size | Path | Why |
|---:|---|---|
| 3.9 GB | `/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/02_EDITED_STUDIO_PHOTO/` | 25 EVOTO .tif edited-photo MASTERS (150-212 MB each), client deliverable originals. Misnamed Finder dump, but it holds the real masters. Confirm an external backup exists, then it could become COLD_ARCHIVE_OK; until then DO_NOT_DELETE. |
| 2.8 GB | `/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/05_BUILD/` | Active Alma build assets (Alma is an open client obligation). KEEP while Alma is live. |
| 1.1 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_EDITOR_HANDOFF_001/` | Alma shoot footage / editor handoff (source-of-record for the 62-clip shoot). |
| 0.4 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/kingdom_of_the_sun/` | Warm active opportunity (dad's tournament). KEEP_ACTIVE. |

### COLD_ARCHIVE_OK (done / proof / superseded, keep one copy off-Mac, then remove)
| Size | Path | Why |
|---:|---|---|
| 5.7 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/` | Mostly intermediate AI cuts + regen: 4.0 GB .mp4 (many duplicate versions), 1.7 GB .png, HER_VISION_AI 3.1 GB, 07_REGEN 1.3 GB. KEEP the single final delivery cut + the Premiere project; archive the rest. Biggest single archive target. |
| 2.7 GB | `/Users/sniper/AI-Brain-Refinery/raw/` | Staged intake MIRROR of the SNIPED_OS sources (per AGENTS.md). Duplicate of files that already live in the corpus. Verify it is a true mirror, then archive or delete. |
| 0.66 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/` | Sandbox/test pipeline output (incl. a 152 MB test hero tiff). Not a deliverable. |
| 0.57 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OVERNIGHT_PRIME_MOVER_PRODUCTION_SPRINT_001/` | Prime Mover is superseded (per NEXT_ACTION). Proof artifact. |
| 0.51 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/postproduction/` | Intermediate post output (verify nothing active before archiving). |
| 0.27 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/THE_MEANTIME_001_PER_DIEM/` | Closed as FAIL evidence (per memory). Archive as proof. |
| 0.22 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/MAX_PRODUCTION_PROOF_001/` | Proof artifact. |
| 0.21 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_OVERNIGHT_MAX_OPERATING_SPRINT_001/` | Sprint artifact. |
| 0.10 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_PRIVATE_DEMO_PACKAGE_001/` | Demo package. |

### DELETE_ELIGIBLE (waste / demoted / retired / duplicate, on approval)
| Size | Path | Why |
|---:|---|---|
| 1.9 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/` | DEMOTED project (friend's pitch, back burner, zero spend per NEXT_ACTION). Highest-value delete. Archive first if you want the proof. |
| 0.34 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/AXIS_ELITE_DEMO_PACKAGE_001/` | AXIS is RETIRED as a target (per OS_CURRENT_STATE). |
| 0.19 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/AXIS_ELITE_001/` | AXIS retired. |
| 0.21 GB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_OVERNIGHT_MAX_OPERATING_SPRINT_001_REVIEW_PACKAGE.zip` (207 MB) + `OVERNIGHT_PRIME_MOVER_PRODUCTION_SPRINT_001/CHATGPT_REVIEW_BUNDLE.zip` (140 MB) + `OS_PRIVATE_DEMO_PACKAGE_001.zip` (100 MB) | Review/handoff .zip bundles, duplicates of folder contents already on disk. |
| ~1.0 GB | ALMA_MARGIELA duplicate intermediate cuts: `HER_VISION_AI/06_FULL_CUT/ALMA_DEADPAN_SUMMER_v2.mp4` (179 MB), `..._v2_1.mp4` (141 MB), `..._v3_luxbackbone.mp4` (135 MB), `motion/v2final/seg/silent_cut.mp4` (179 MB), `seg2/silent_cut.mp4` (141 MB), `v3seg/silent.mp4` (134 MB) | Superseded render iterations; keep only `07_DELIVERY/ALMA_DEADPAN_SUMMER_v3_share.mp4` (the final). These overlap the ALMA_MARGIELA COLD bucket above; counted once. |
| 152 KB | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT/Adobe Premiere Pro Auto-Save/` | Premiere auto-saves, pure scratch. |

### DO_NOT_TOUCH (operator hold)
| Size | Path | Why |
|---:|---|---|
| 6.8 GB | `/Users/sniper/AI-Brain-Refinery/.git/` (one pack file) | Committed binary assets bloating history. You HELD decision D (no history rewrite). Left untouched. Biggest single item, but off-limits this round. |

## Category totals (approx)
- DO_NOT_DELETE (masters / active): ~8.2 GB , keep.
- COLD_ARCHIVE_OK: ~11.1 GB , archive then remove on approval.
- DELETE_ELIGIBLE: ~3.9 GB , delete on approval (archive proof first if wanted).
- DO_NOT_TOUCH (git, held): 6.8 GB.

## Risk notes
- I did NOT verify external backups. Before removing ANY client master (the EVOTO tifs) or final delivery cut, confirm a backup exists. Treat DO_NOT_DELETE as keep-until-backup-confirmed.
- `raw/` is labeled a staged mirror, but verify it is byte-identical to the SNIPED_OS sources before deleting (md5 sample) so nothing unique is lost.
- COLD_ARCHIVE_OK folders may contain a single keeper (final cut, project file). For each, I will identify the one-or-two keepers and archive only the rest, on approval.
- Demoted/retired (SYNERGY, AXIS) are safe to delete per current operating state, but archiving the proof is cheap insurance.
- Same copy-verify-remove discipline as the book retirement: copy to destination, md5-verify, then remove. Never move-then-hope.
- Status divergence to resolve: `kingdom_of_the_sun` (0.4 GB) is listed under "archive" in NEXT_ACTION but framed as a warm active opportunity in memory. Kept in DO_NOT_DELETE here as the safe call; if it is truly archived, move it to COLD_ARCHIVE_OK. Your call.

## DECISION PAGE (approve later, per line; nothing runs until you mark these)
| # | Action | Reclaim | Recommended |
|---|---|---:|---|
| C1 | DELETE_ELIGIBLE bucket: SYNERGY + AXIS x2 + 3 review zips + ALMA_MARGIELA duplicate cuts + auto-save | ~3.9 GB | YES, lowest risk, archive proof first if wanted |
| C2 | COLD_ARCHIVE_OK bucket: ALMA_MARGIELA intermediates, raw mirror, sandbox, superseded sprints, closed proofs | ~11.1 GB | YES, copy-verify-remove to a destination you name |
| C3 | Confirm backup of the EVOTO .tif masters, then move them to COLD_ARCHIVE (frees 3.9 GB) | 3.9 GB | ONLY after you confirm a backup exists |
| C4 | Keep DO_NOT_DELETE in place (ALMA active build, editor handoff, kingdom_of_the_sun) | 0 | YES, no action |
| C5 | git history (.git 6.8 GB) | 6.8 GB | HELD by you (D). No action this round. |

Nothing happens until you mark these. On approval I execute exactly the marked lines, copy-verify-remove only, identify per-folder keepers first, and log every move.
