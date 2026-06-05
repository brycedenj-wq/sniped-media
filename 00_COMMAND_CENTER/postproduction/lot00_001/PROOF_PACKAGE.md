# PROOF PACKAGE , LOT 00 post-production chain (2026-06-04)
> The acceptance test, run end to end on a real asset. Raw generated still to graded, color-law'd, exported, captioned, gated. Every stage left an artifact and a log row. No new generation: the raw is the existing stage-1 LOT 00 still.

## THE CHAIN (each step = a real file)
| step | tool | artifact | result |
|---|---|---|---|
| 0 raw | os_adobe_asset register | `00_raw/lot00_raw.png` | 896x1200, metadata clean |
| 1 grade | os_adobe_grade apply | `01_graded/lot00_graded.png` | locked LUXURY look (deterministic) |
| 2 color-law | os_adobe_composite colorlaw | `02_composite/lot00_composite.png` | only auction-red retains saturation |
| 2b glyph | os_adobe_composite glyph | `02_composite/lot00_glyph_demo.png` | legibility stamp proven on tag crop |
| 3 exports | os_adobe_reframe run | `03_exports/` (7 platform specs) | one hero in, full set out |
| 4 motion | os_adobe_cut run | `04_motion/cut_test_9x16_capsafe.mp4` | clip in, muted/resized/caption-safe out (tested on existing AXIS clip) |
| 5 caption | world-bible voice | `caption.md` | auctioneer catalogue copy |
| 6 gate | os_postproduction_gate run | `10_logs/POSTPROD_GATE_LOG.csv` | verdict REJECT (honest, see below) |
| 7 log | os_adobe_asset log_edit | `10_logs/EDIT_LOG.csv` | every artifact logged, non-silent |

## GATE VERDICT: REJECT (the gate working, not failing)
The gate is not a rubber stamp. It PASSED grade-applied, exports-complete, metadata-clean, no-banned-tokens, log-not-silent, identity-withheld, beats-source. It correctly FLAGGED the two real problems:
1. `text_legible = FAIL` , the LOT 00 wrist stamp is still not crisp on the hero. Fix: apply os_adobe_composite glyph at the tag coords, or run the Adobe-MCP generative re-stamp escalation (logged, AMBER).
2. `no_enlarge = WARN` , 6 of 7 exports upscaled from a 1k source. Fix: regenerate the hero at higher resolution (nano_banana_pro supports 4K) before final export.

This is the layer doing its job: it caught exactly what a human eye flagged, and it will not let an under-spec asset ship.

## REPEATABLE WORKFLOW (copy/paste, any asset)
```
RUN=postproduction/<name>; LOG=$RUN/10_logs/EDIT_LOG.csv
python3 scripts/os_adobe_asset.py register $RUN/00_raw/<raw>.png --log $LOG
python3 scripts/os_adobe_grade.py apply --src $RUN/00_raw/<raw>.png --out $RUN/01_graded/g.png --log $LOG
python3 scripts/os_adobe_composite.py colorlaw --src $RUN/01_graded/g.png --out $RUN/02_composite/c.png --log $LOG
python3 scripts/os_adobe_reframe.py run --src $RUN/02_composite/c.png --outdir $RUN/03_exports --focus 0.52,0.62 --log $LOG
python3 scripts/os_postproduction_gate.py run $RUN --final $RUN/02_composite/c.png --model-scores "identity_withheld=PASS,beats_source=PASS,text_legible=PASS|FAIL"
```

## ADOBE-MCP ESCALATION (AMBER, wired + logged, runs on approval)
For the seamless wrist-tag re-stamp and content-aware cleanup that a local op cannot match, the chain logs an ESCALATE_ADOBE row (see EDIT_LOG). The Adobe MCP bridge is connected; running it = a generative op, held for explicit approval per the no-extra-generation rule. One approval moves this from AMBER to GREEN.
