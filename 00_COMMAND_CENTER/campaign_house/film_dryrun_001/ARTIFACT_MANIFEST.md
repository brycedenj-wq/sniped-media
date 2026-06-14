# ARTIFACT MANIFEST , film_dryrun_001
Generated 2026-06-05. Every file in this dry-run workspace, with size. Zero new generation.

| stage | file | bytes | kind |
|---|---|---|---|
| 00_intake | 00_intake/axis_facecrop.png | 15453 | image/png |
| 00_intake | 00_intake/axis_hero_v2_marked.png | 1265317 | image/png |
| 00_intake | 00_intake/axis_motion_v1.mp4 | 1954283 | video/mp4 |
| 01_plan | 01_plan/beats.json | 309 | application/json |
| 02_sequence | 02_sequence/dryrun_teaser_9x16.mp4 | 618930 | video/mp4 |
| 03_finish | 03_finish/axis_clip_capsafe_9x16.mp4 | 1097943 | video/mp4 |
| 04_gates | 04_gates/clip_obs_REUSED.json | 1358 | application/json |
| 04_gates | 04_gates/facematch_sidebyside.png | 67890 | image/png |
| 04_gates | 04_gates/MOTION_QA_REPORT.json | 985 | application/json |
| 04_gates | 04_gates/motion_qa_report.txt | 893 | text/plain |
| 04_gates | 04_gates/postproduction_report.txt | 598 | text/plain |
| 04_gates | 04_gates/scene_REUSED.json | 227 | application/json |
| 10_logs | 10_logs/EDIT_LOG.csv | 222 | text/plain |
| 10_logs | 10_logs/FACE_MATCH_LOG.csv | 341 | text/plain |
| 10_logs | 10_logs/POSTPROD_GATE_LOG.csv | 370 | text/plain |
| 10_logs | 10_logs/PRIVACY_LOG.csv | 142 | text/plain |
| ARTIFACT_MANIFEST.md | ARTIFACT_MANIFEST.md | 1236 | text/plain |
| DRY_RUN_REPORT.md | DRY_RUN_REPORT.md | 4414 | text/plain |

## Inputs (existing assets, reused , not generated this run)
- locked hero axis_v2: axis_hero_v2_marked.png
- approved motion: axis_motion_v1.mp4
- identity anchor: axis_facecrop.png

## Outputs (assembled this run, zero spend)
- 02_sequence/dryrun_teaser_9x16.mp4 (still -> teaser, ffmpeg)
- 03_finish/axis_clip_capsafe_9x16.mp4 (existing clip -> caption-safe cut, ffmpeg)

## Gate reports
- 04_gates/MOTION_QA_REPORT.json (SHIP 0.929)
- 04_gates/facematch_sidebyside.png + 10_logs/FACE_MATCH_LOG.csv (PASS)
- 04_gates/postproduction_report.txt (REJECT , partial package, correct)
- 10_logs/PRIVACY_LOG.csv (SHIP, 0 leaks)
