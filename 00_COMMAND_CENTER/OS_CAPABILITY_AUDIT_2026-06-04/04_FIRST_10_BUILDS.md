# 04 FIRST 10 GAP-CLOSING BUILDS (in order)
> Smallest infra that closes the biggest gap. Danger before leverage. Reuse the existing os_*.py + gate pattern. Do not build randomly.

## 1. Set offsite backup: git remote add osbackup <private url>, flip launchd ProgramArguments to os_backup.sh push, trigger one real run
- **Closes:** backups AMBER->GREEN: brain has zero offsite copy today (no osbackup remote, no /tmp/os_backup.log verified). Closes the single most irreversible exposure.
- **Smallest form:** Two commands + one manual run that creates /tmp/os_backup.log and confirms push. No new code.
- **Depends on:** Operator provides a private GitHub/GitLab repo URL
- **Approval needed:** Operator must create/name the private remote (non-real-name considerations apply).

## 2. os_privacy_gate.py: exiftool-strip any share asset folder + grep deployed HTML/form for banned tokens (real name, sniped, employer, handles), refuse on hit
- **Closes:** privacy gate enforced (script verified absent): turns the manual PRIVACY_CHECKLIST.md into a gate wired before SHARE. Hardest-to-reverse leak for an employed operator.
- **Smallest form:** One os_*.py reusing the existing gate pattern: exiftool pass + token grep + exit-2 on hit. No deploy yet.
- **Depends on:** exiftool installed; banned-token list from PRIVACY_CHECKLIST.md/SHARE_CHECKLIST.md
- **Approval needed:** Operator confirms the exact banned-token list (real name, employer, handles).

## 3. Set cost USD rate: os_cost.py rate set --usd-per-credit <X>
- **Closes:** cost ledger reads UNKNOWN in dollars (.prod_cost_rate verified absent). Makes every logged credit convert to real money so runaways are visible in USD.
- **Smallest form:** Single CLI call writing .prod_cost_rate. No code change.
- **Depends on:** Nothing on disk
- **Approval needed:** Operator supplies the USD/credit rate.

## 4. Move legal NOW-stubs to live 00_COMMAND_CENTER/legal/ and write the 2 missing files (_stub_nda.md, _stub_ip_assignment.md)
- **Closes:** legal layer (live folder verified absent): ToS/Privacy/NDA/IP-assignment must exist outside the demo sandbox before any named/public surface or IP share.
- **Smallest form:** Create legal/ folder, copy the 4 existing stubs, author the 2 missing template stubs from the kit spec.
- **Depends on:** STARTUP_OPERATING_KIT.md stub templates
- **Approval needed:** Lawyer review of the 4 NOW stubs is a later human step; folder + stubs can be drafted now.

## 5. Router fixture set + checker: labeled example prompts (expected mode+gates) and a tiny test script; log each ROUTE receipt to CSV
- **Closes:** command router AMBER/untested: proves classification is test-backed not vibes, and gives an auditable routing trail before the loop drives real requests.
- **Smallest form:** A small fixtures file + a checker reusing the os_skill.py/test_*.py pattern (pass/fail count).
- **Depends on:** os-command-router SKILL.md (exists)
- **Approval needed:** None

## 6. os_adobe_asset.py: shared upload/get-id/run/pull I/O layer for all Adobe MCP wrappers
- **Closes:** Adobe foundational plumbing (no os_adobe* exists, verified): the single dependency under grade/cutout/reframe/composite. Build-once, unlock-many.
- **Smallest form:** One wrapper around asset_initialize/finalize_file_upload + asset_search + pull-back, logged. One dry-run on an existing TIFF.
- **Depends on:** Adobe MCP live; a real local TIFF (FINAL_hero.tiff exists in sandbox)
- **Approval needed:** Adobe MCP auth confirmed; first upload may incur minor cost.

## 7. os_adobe_reframe.py + SNIPED_EXPORT_SPECS.json from the 9 locked export presets; one hero -> platform-spec set
- **Closes:** highest-leverage output multiplier with zero new decisions (specs locked on disk). Cleanest first Adobe dry-run; proves the asset layer end-to-end.
- **Smallest form:** JSON of the 9 presets + a wrapper chaining image_crop_and_resize; one logged dry-run writing to 09_exports.
- **Depends on:** Build 6 (os_adobe_asset.py); preset_library.md s4 / lightroom_operating_system.md s8
- **Approval needed:** Minor Adobe MCP spend on one hero.

## 8. os_adobe_grade.py + SNIPED_LUXURY_GRADE.json encoding the v3 LUXURY 10-step slider math, with strongest-photograph reject gate
- **Closes:** Lightroom grade AMBER/untested: converts the manual locked look into a repeatable MCP batch pass so every frame is recognizably SNIPED. Core authorship multiplier.
- **Smallest form:** JSON params from SNIPED_LOCKED_LOOK_v3_LUXURY.xmp + chained image_adjust_* in locked order + before/after vision-gate, one dry-run.
- **Depends on:** Build 6 (asset layer); sniped-luxury-edit SKILL.md values
- **Approval needed:** Minor Adobe MCP spend on one sample frame; human taste confirms output beats source.

## 9. Deploy the proofcell form: paste one real endpoint (Tally private link OR Formspree URL into index.html) and host on Netlify/Vercel, gated by Build 2
- **Closes:** landing/form AMBER undeployed (action=REPLACE stub verified): starts the proof clock and feeds the GREEN ingestion/scoring engine its first real input. Unlocks the entire demand side.
- **Smallest form:** Endpoint paste + host wiring; assets already done. Run os_privacy_gate (Build 2) against the live HTML first.
- **Depends on:** Build 1 (offsite backup), Build 2 (privacy gate), Build 4 (legal stubs live)
- **Approval needed:** Operator pastes the endpoint and authorizes a non-real-name host/team; this is the going-public trigger (human-only).

## 10. os_proof_dashboard.py (~30 lines): read RESPONSES.csv + SCORE.md, write populated PROOF_LOOP_DASHBOARD.md rows
- **Closes:** dashboard AMBER/empty (header-only tables verified): turns scattered signal into one glanceable keep/kill/scale panel once the form starts filling.
- **Smallest form:** ~30-line reader/writer reusing the os_*.py pattern; regenerates the dashboard from the two source files.
- **Depends on:** Build 9 (form live so RESPONSES.csv fills + SCORE.md generates)
- **Approval needed:** None
