# 00 OS CAPABILITY DASHBOARD , 2026-06-04
> Disk-grounded audit of the one-person 2026 campaign/media/IP machine. A layer is GREEN only if a real artifact proves it (script/skill/template/gate/test/dashboard/logged-run). "Notes about it" does not count.

## SCORE: 16 GREEN · 9 AMBER · 4 RED  (of 29 layers, at audit time)

## REFERENCE PROOF OF "ACTIVE" (banked 2026-06-04)
> This exact chain is now the STANDARD EXAMPLE of what ACTIVE means. A layer is only ACTIVE if it can do this: route, execute, produce an artifact, gate it, log it, export it, repeat it.
>
> **Raw Higgsfield still , 4K source , grade , color-law , export package , post-production gate , SHIP.**
>
> Proven on LOT 00 (THE SITTER): job 706e806e, 3584x4800, full chain, gate verdict SHIP, 7/7 exports no-enlarge OK, 12/12 layer tests pass. Artifacts: `postproduction/lot00_4k_001/` (PROOF_PACKAGE.md, EDIT_LOG.csv, POSTPROD_GATE_LOG.csv). The same gate returned REJECT on the 1k version, so the standard is evidence-backed, not asserted.

## POST-PRODUCTION DELTA (since audit)
- Lightroom/Camera Raw grade: AMBER -> **ACTIVE** (`os_adobe_grade.py`, encodes the real v3 LUXURY XMP).
- Photoshop/composite (colorlaw/glyph/cleanup/crop): AMBER -> **ACTIVE** (`os_adobe_composite.py`).
- Adobe post-production umbrella: AMBER -> **ACTIVE** for the deterministic engine; the Adobe-MCP GENERATIVE escalation stays AMBER (wired + logged, one approval from GREEN).
- export/versioning: GREEN, reinforced (`os_adobe_reframe.py` + enlarge-guard + `os_postproduction_gate.py`).
- Premiere/After Effects edit: RED -> **AMBER** (`os_adobe_cut.py` does single-clip trim/mute/resize/caption-safe; multi-clip sequence + titling not yet built).
- Illustrator/InDesign layout: still **RED** (queued).
- Score after delta: ~18 GREEN · ~8 AMBER · 3 RED. See `postproduction/POSTPROD_DASHBOARD.md`.

## RED (missing or blocked , the surprise-gap killers)
- **Illustrator/InDesign layout layer** , No repeatable way to lay out the Op Kit one-pager, Pitch deck, Direction Stack book pages, or branded drop cards. Layout deliverables fall back to fully manual GUI work with no template, no data-merge, no version discipline.
- **Premiere/After Effects edit layer** , No way to turn multiple generated/shot clips into a finished edited piece (multi-shot reel, titled cutdown, platform edit). Motion output stops at single generated clips that pass QA; there is no assembly, no cut, no sequence, no titling step.
- **distribution/content calendar layer** , No posting cadence is enforced or visible. Content gets generated but its release is improvised, untracked, and dependent on operator memory. The proof-loop layer downstream has no upstream feed of what was posted when, so kill/keep/scale signals can never be attributed to a scheduled plan. Distribution (the actual moat per Hit Makers / Blockbuster intel) stays a one-off manual act.
- **monetization/payment layer** , There is no path from interest to cleared money. A Green discovery call or a print/method buyer cannot be invoiced or charged through any OS artifact; the entire machine can generate proof and demand but cannot capture revenue, so it cannot close the loop it exists to close.

## AMBER (exists but unproven or not wired)
- **Adobe post-production layer (umbrella: Lightroom/Camera Raw grade, Premiere/AE edit, speech/media enhance, render/merge)** , flags: known_not_operationalized, needs_adobe_bridge, needs_automation. Write os_edit.py that wraps two Adobe MCP calls into one gated, logged workflow: (1) apply the v3 LUXURY look to a still via image_apply_preset/image_adjust_* a
- **Command router** , flags: built_untested, needs_human_taste. Add a tiny fixture set of labeled example prompts with expected mode+gates and a checker script, so the router classification is test-proven (not just model-jud
- **Lightroom/Camera Raw grade layer** , flags: built_untested, needs_adobe_bridge, needs_human_taste. Wrap the .xmp slider values + 5-mask stack into an os_grade.py that drives the LIVE Adobe MCP image_adjust_* tools on a sample frame, log a before/after with a 
- **Photoshop/composite layer (locked subject into generated/shot world)** , flags: built_untested, needs_human_taste, needs_proof_loop_bridge. Run ONE composite end-to-end and write the proof to disk: integrate the locked axis hero into a Brutalist-Monument plate, produce the required 5 proof crops + t
- **backups** , flags: built_untested, needs_automation, known_not_operationalized. Two commands: (1) git remote add osbackup <private GitHub/GitLab url>; (2) flip the launchd ProgramArguments to call os_backup.sh with 'push' (it currently runs
- **dashboard/control-room layer** , flags: known_not_operationalized, needs_automation, needs_proof_loop_bridge. A ~30-line script (os_proof_dashboard.py) that reads RESPONSES.csv + SCORE.md and writes the populated PROOF_LOOP_DASHBOARD.md row(s) (asset, posted?, metric, 2
- **landing/form layer** , flags: built_untested, blocked_account_manual, needs_human_taste. Operator pastes ONE real endpoint: either rebuild in Tally per TALLY_SPEC.md (2 min, gives private link) OR replace action="REPLACE_WITH_YOUR_FORM_ENDPOINT" in 
- **privacy/identity/employer-risk layer** , flags: built_untested, known_not_operationalized, needs_human_taste, blocked_legal_privacy_employer. Write os_privacy_gate.py that (1) runs exiftool over any asset folder and flags/strips identifying metadata, (2) greps the built site/form HTML for the banned t
- **startup/legal document layer** , flags: built_untested, known_not_operationalized, needs_human_taste, blocked_legal_privacy_employer. Move the 4 NOW-set items out of the OS_MAX_DEMO_001 demo sandbox into a live /00_COMMAND_CENTER/legal/ folder, and actually write the two missing template stub 

## GREEN (active + tested , the spine that works)
- AI generation layer  `GENERATION_LOG.csv (3 var_*.png + 1 FAILED row proving the failure path fires)`
- OS source/certification layer  `OS_CERTIFICATION_LEDGER.csv`
- Quality gates  `settings.json)`
- analytics/proof-loop layer  `PROOF_LOOP_DASHBOARD.md (filled structure, all 'not-activated until posted').`
- archive/learning loop  `OS_DRYRUN_001.md.`
- character consistency layer  `0 fail)`
- cost/session control: runaway + concurrency guard  `os_cost_guard.py`
- cost/session control: session-state save + cold boot  `SKILL.md`
- cost: per-run cost ledger  `OS_PRODUCTION_COST.csv`
- export/versioning layer  `monolith01_4x5.export)`
- hooks: stop-check / completion-verification  `os_stop_check.py`
- motion/video layer  `GENERATION_LOG.csv (Vmotion1 seedance_2_0 18cr downloaded)`
- reliability/hooks  `settings.json`
- response ingestion/scoring layer  `os_form_score.py (RESPONSES.csv exists as empty header-only template; SCORE.md generated on dry-run then template restored)`
- skill lifecycle layer  `os_skill.py`
- world bible layer  `0 fail, incl. forbidden-element and off-rotation-environment quarantine cases)`

## EXECUTIVE READ
The cognition and production core is real and tested: source certification, quality gates, reliability hooks, cost guard, skill lifecycle, generation, character-consistency, world-bible, motion-QA, export, ingestion-scoring, and the archive loop are GREEN with logged real runs (a real 18-credit video shipped, face-match PASS at 0.97 and QUARANTINE at 0.1 both logged). What is missing is not the brain, it is the edges where the machine touches the outside world and the outside world touches money. The four most dangerous gaps are verified absent on disk, not merely weak: there is no offsite backup (no osbackup remote, no backup log, so a laptop loss wipes everything), no enforced privacy gate (os_privacy_gate.py does not exist, only a checklist), no payment path (no payments/ folder, no link, SCORE.md never generated), and the form is still an unpasted stub (action=REPLACE_WITH_YOUR_FORM_ENDPOINT). The entire Adobe post-production umbrella is a claim, not a capability: all four EDIT_LOG.csv files are header-only, no os_adobe* or os_edit/os_grade script exists, and no subject-into-plate composite or scorecard is on disk, so grade/cut/composite remain manual desktop work with no audit trail. The correct sequence is to close danger before leverage: backup, privacy gate, cost-rate, and legal stubs first (cheap, mostly two-command or one-script moves), then the shared Adobe asset layer that unlocks reframe and grade, then deploy the form behind the privacy gate to start the proof clock. Do not let the polished core fool you into shipping a public proof loop while the brain has no copy and the operator's identity has no enforced gate.