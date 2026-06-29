# CLEANUP DECISION BRIEF , one-page read before approving C1/C2

**Date:** 2026-06-19. **Status:** REVIEW ONLY. Nothing moved, copied, deleted, archived; git untouched. Distilled from `CLEANUP_APPROVAL_PACKET.md` (fresh-context verified 9.5/10). Repo is 30 GB.

## 1. Delete with near-zero risk today (~3.9 GB)
Demoted, retired, duplicate, or scratch , nothing current depends on these.
- `00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/` , 1.9 GB , DEMOTED project (zero spend, back burner).
- `00_COMMAND_CENTER/AXIS_ELITE_DEMO_PACKAGE_001/` (0.34 GB) + `AXIS_ELITE_001/` (0.19 GB) , AXIS is RETIRED.
- 3 review zips: `OS_OVERNIGHT_MAX_OPERATING_SPRINT_001_REVIEW_PACKAGE.zip` (207 MB) + `OVERNIGHT_PRIME_MOVER.../CHATGPT_REVIEW_BUNDLE.zip` (140 MB) + `OS_PRIVATE_DEMO_PACKAGE_001.zip` (100 MB) , duplicate bundles of folders already on disk.
- ALMA_MARGIELA superseded render iterations (~1 GB): `HER_VISION_AI/06_FULL_CUT/ALMA_DEADPAN_SUMMER_v2.mp4`, `..._v2_1.mp4`, `..._v3_luxbackbone.mp4`, `motion/v2final/seg/silent_cut.mp4`, `seg2/silent_cut.mp4`, `v3seg/silent.mp4` , keep only the final `07_DELIVERY/ALMA_DEADPAN_SUMMER_v3_share.mp4`.
- `ALMA_MARGIELA_SAVE_001/06_FULL_CUT/Adobe Premiere Pro Auto-Save/` (152 KB) , Premiere scratch.
- Caveat: archive the proof first if you want a record of SYNERGY/AXIS; otherwise straight delete is fine.

## 2. Cold-archive, do not delete (~11 GB)
Done or superseded work with possible future reference value. Copy off-Mac, verify, then remove.
- `00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/` , 5.7 GB (archive the intermediates + regen + stills; keep the one final cut + the Premiere project).
- `raw/` , 2.7 GB , staged source MIRROR (verify byte-identical to SNIPED_OS first).
- `00_COMMAND_CENTER/photo_pipeline_sandbox/` , 0.66 GB.
- `00_COMMAND_CENTER/OVERNIGHT_PRIME_MOVER_PRODUCTION_SPRINT_001/` , 0.57 GB (Prime Mover superseded).
- `00_COMMAND_CENTER/postproduction/` , 0.51 GB.
- `00_COMMAND_CENTER/THE_MEANTIME_001_PER_DIEM/` , 0.27 GB (closed FAIL evidence).
- `MAX_PRODUCTION_PROOF_001/` 0.22 GB + `OS_OVERNIGHT_MAX_OPERATING_SPRINT_001/` 0.21 GB + `OS_PRIVATE_DEMO_PACKAGE_001/` 0.10 GB , proof/demo artifacts.

## 3. Must stay (active / client-facing / source-of-record / master) (~8 GB)
- `ALMA_LOVE_PRODUCTION_001/New Folder With Items/02_EDITED_STUDIO_PHOTO/` , 3.9 GB , 25 EVOTO .tif client MASTERS. DO_NOT_DELETE until an external backup is confirmed; then it may move to cold archive.
- `ALMA_LOVE_PRODUCTION_001/05_BUILD/` , 2.8 GB , active Alma build (open client obligation).
- `00_COMMAND_CENTER/ALMA_EDITOR_HANDOFF_001/` , 1.1 GB , Alma shoot footage / source-of-record.
- `00_COMMAND_CENTER/kingdom_of_the_sun/` , 0.4 GB , warm active opportunity (NEXT_ACTION says "archive"; treated active as the safe call , confirm).
- `.git/` , 6.8 GB , you HELD it (no history rewrite). Stays this round.

## 4. Top 10 space hogs (exact paths + action)
| # | GB | Path | Action |
|---|---:|---|---|
| 1 | 6.8 | `/Users/sniper/AI-Brain-Refinery/.git/` | DO_NOT_TOUCH (held) |
| 2 | 5.7 | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/` | COLD_ARCHIVE_OK (keep final cut) |
| 3 | 3.9 | `/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/02_EDITED_STUDIO_PHOTO/` | DO_NOT_DELETE (masters, backup-gated) |
| 4 | 2.8 | `/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/05_BUILD/` | KEEP_ACTIVE |
| 5 | 2.7 | `/Users/sniper/AI-Brain-Refinery/raw/` | COLD_ARCHIVE_OK (verify mirror) |
| 6 | 1.9 | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/` | DELETE_ELIGIBLE (demoted) |
| 7 | 1.1 | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_EDITOR_HANDOFF_001/` | DO_NOT_DELETE (source-of-record) |
| 8 | 0.66 | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/` | COLD_ARCHIVE_OK |
| 9 | 0.57 | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OVERNIGHT_PRIME_MOVER_PRODUCTION_SPRINT_001/` | COLD_ARCHIVE_OK |
| 10 | 0.51 | `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/postproduction/` | COLD_ARCHIVE_OK |

## 5. Safest first move (recovers real space, cannot break current work)
**Delete the provably redundant set: the 3 review zips + the Premiere auto-save + the ALMA_MARGIELA superseded render iterations (keeping the final delivery cut). ~1.4 GB, zero risk.** These are duplicate bundles and superseded copies; no active workflow, project file, or client deliverable points at them. It needs no backup step (the content is duplicated or superseded) and is fully reversible in effect (the originals/finals remain).
- Second-safest tier (after that): SYNERGY (1.9 GB demoted) + AXIS x2 (0.53 GB retired), archive-proof-first optional. Brings the easy total to ~3.9 GB.
- Do NOT start with the EVOTO masters, raw mirror, or anything in section 3.

## Recommendation
Approve **C1 (delete-eligible, ~3.9 GB)** in two steps: first the ~1.4 GB redundant set (no backup needed), then SYNERGY + AXIS (~2.4 GB, archive-proof-first if wanted). Defer **C2 (cold-archive ~11 GB)** until you pick a destination drive. Keep section 3 untouched. Leave git alone. Nothing runs until you say go.
