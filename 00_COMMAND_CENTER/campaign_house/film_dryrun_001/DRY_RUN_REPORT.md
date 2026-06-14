# BUILD_FILM_PIPELINE , ZERO-SPEND DRY RUN REPORT
### Preflight, not destination. Tighten the shoes before running full speed.
Run: 2026-06-05. Workspace: `00_COMMAND_CENTER/campaign_house/film_dryrun_001/`. No new generation. Existing assets only. No public action.

---

## Verdict: PASS (preflight clean) with one expected REJECT that proves a gate works

The film pipeline route selects correctly, activates the right doctrine, plans a sequence, assembles motion from existing assets through the real finishing scripts, and passes the privacy, identity, motion-QA, and world-continuity gates. The post-production gate correctly REJECTS the partial package (no full grade + 7-size export), which is the honest, desired behavior, not a failure of the route.

---

## The 15 required proof points

| # | Proof point | Result | Evidence |
|---|---|---|---|
| 1 | route selection | PASS | "build a film pipeline" -> `build_film_pipeline` (no fallback) |
| 2 | doctrine activation | PASS | world_character, narrative_canon, visual_grade, motion, safety_identity |
| 3 | source confidence | PASS | visual_grade CERTIFIED, world_character MIXED, safety_identity CERTIFIED |
| 4 | shot/sequence planning | PASS | `01_plan/beats.json` (3 beats: title -> hero move -> title) |
| 5 | asset selection | PASS | locked hero `axis_v2` + approved `axis_motion_v1.mp4` (existing) |
| 6 | motion/teaser assembly (existing assets) | PASS | `02_sequence/dryrun_teaser_9x16.mp4` (7.6s, 1080x1920, ffmpeg, zero spend) |
| 7 | AE / HyperFrames / ffmpeg finishing route | PARTIAL (honest) | ffmpeg REAL (`03_finish/axis_clip_capsafe_9x16.mp4`); AE + HyperFrames = route-declared, NOT exercised (no .aep / no HTML comp authored) , labeled SIMULATED |
| 8 | continuity gate | PASS | `os_world continuity world_meridian_01` -> [pass] |
| 9 | motion QA gate | SHIP | score 0.929, 0 identity-quarantined frames (run against REUSED observation from original axis run , labeled) |
| 10 | post-production gate | REJECT (correct) | grade_applied FAIL + exports incomplete , gate properly refuses a partial package; 3 model-judged checks PENDING |
| 11 | privacy gate | SHIP | 0 leaks across 7 files (`10_logs/PRIVACY_LOG.csv`) |
| 12 | edit log | PASS | `10_logs/EDIT_LOG.csv` (teaser op logged w/ sha + dims) |
| 13 | artifact manifest | PASS | `ARTIFACT_MANIFEST.md` |
| 14 | dashboard update | PASS | `DASHBOARD.md` |
| 15 | final dry-run report | PASS | this file |

---

## What was REAL vs SIMULATED (no fake-complete)

REAL (executed this run):
- Route + doctrine + confidence resolution (os_execution_graph / os_doctrine_router)
- Sequence assembly from an existing still (os_adobe_teaser, ffmpeg)
- Caption-safe cut of an existing clip (os_adobe_cut, ffmpeg)
- Privacy audit, facematch, motion-QA, world-continuity, post-production gates (all ran, real exit codes)
- Edit log, gate logs, this manifest/dashboard/report

SIMULATED / REUSED (labeled, because dry run = no new generation, no fresh vision):
- Motion-QA observations REUSED from the original axis run (`clip_obs_REUSED.json`), not fresh per-frame vision on the new teaser
- World-continuity scene REUSED (`scene_REUSED.json`)
- AE title render + HyperFrames titles = route declared, not exercised (no project authored)
- The 3 model-judged post-prod checks (text_legible, identity_withheld, beats_source) left PENDING

---

## Smallest safe gaps found + fixed this run

1. `os_motion_qa` and `os_world` take a SLUG, not a path (CRS/world). Fixed the call.
2. `os_facematch --out` must be an image extension (.png), not .json (it writes a side-by-side). Fixed the call.
3. `os_motion_qa --clip` expects a frame-observation JSON, not the raw mp4. Supplied the reused observation file.

No script code was changed; these were invocation corrections. The post-prod REJECT is left as-is because it is correct behavior.

---

## What the REAL paid run would add (the delta)

- Fresh generation: hero stills + motion clips (Higgsfield/Seedance) conditioned on the locked hero.
- Fresh per-frame vision feeding motion-QA (not reused observations).
- Full grade (os_adobe_grade) + the 7-size export chain -> post-production gate flips REJECT to SHIP.
- AE title comp + HyperFrames lower-thirds actually rendered.
- Human taste sign-off (SHIP is eligible for taste approval, never auto-post).

See `FILM_PROOF_LAUNCH_PLAN.md` (in 00_COMMAND_CENTER) for the exact paid-run preflight.
