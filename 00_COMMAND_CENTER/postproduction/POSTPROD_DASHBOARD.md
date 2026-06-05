# POST-PRODUCTION LAYER , DASHBOARD (2026-06-04)
> Capability counts only with a proving artifact: a script that runs, logs, gates, exports, repeats. Proven on LOT 00. Tests: `scripts/test_postproduction.py` (12 passed, 0 failed).

## SCRIPT STATUS
| script | does | status | proof |
|---|---|---|---|
| os_adobe_asset.py | shared I/O protocol: register, sha1, dims, EXIF, strip, edit-log, Adobe escalation | ACTIVE | ran on LOT 00 raw + test suite |
| os_adobe_grade.py | locked LUXURY look as deterministic grade pass | ACTIVE | `01_graded/lot00_graded.png` + tests |
| os_adobe_composite.py | colorlaw / glyph / cleanup / crop | ACTIVE | `02_composite/` + tests |
| os_adobe_reframe.py | one hero in, 7 platform exports out, enlarge-flagged | ACTIVE | `03_exports/` (7 files) + tests |
| os_adobe_cut.py | motion finish: trim/mute/resize/caption-safe | ACTIVE | `04_motion/cut_test_9x16_capsafe.mp4` + tests |
| os_postproduction_gate.py | ship gate: 6 deterministic + 3 model-judged checks, SHIP/FIX/REJECT | ACTIVE | `10_logs/POSTPROD_GATE_LOG.csv` + tests |

## CAPABILITY DELTA (vs OS_CAPABILITY_AUDIT_2026-06-04)
- **Adobe post-production layer (umbrella):** AMBER -> ACTIVE for the deterministic engine (grade/composite/reframe/cut + gate, all logged). The Adobe-MCP GENERATIVE escalation stays AMBER (wired + logged, one approval from GREEN).
- **Lightroom/Camera Raw grade layer:** AMBER -> ACTIVE (os_adobe_grade encodes the real v3 LUXURY XMP).
- **Photoshop/composite layer:** AMBER -> ACTIVE for colorlaw/glyph/cleanup/crop; generative composite = AMBER escalation.
- **Premiere/After Effects edit layer:** RED -> AMBER (os_adobe_cut covers trim/mute/resize/caption-safe; multi-clip sequence/titles not yet built).
- **Illustrator/InDesign layout layer:** RED -> still RED (no layout capability; document_render via Adobe MCP is the queued path).
- **export/versioning layer:** GREEN, reinforced (export specs + enlarge-guard now scripted).

## KNOWN LIMITS (honest)
- Source hero is 1k, so 6 of 7 exports are upscale-flagged. Production needs a 4K regenerate.
- Deterministic glyph overlay proves legibility-fix capability; the seamless in-place hero re-stamp is the Adobe-MCP escalation (AMBER).
- Layout (InDesign/Illustrator) is still RED.

## NEXT SMALLEST GAP
Either: (a) run the Adobe-MCP generative re-stamp on the LOT 00 wrist tag to move the generative composite + the gate's text_legible from AMBER/FAIL to GREEN (needs spend approval), or (b) regenerate the hero at 4K so the export set passes no_enlarge (needs ~2cr generation approval).
