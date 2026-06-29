# RESUME QUEUE - Wave 002-G (photography, 2 books, 1 batch)

Built by build_wave.py from the 2 wave=002-G DOCTRINE_EXTRACTION_SCHEDULED rows. Screen CLEAN.

## Queue
R1 (2 books / 3 parts): Jonathan Day - Robert Frank's 'The Americans' (66k, 2 parts); Stephen Shore - The Nature of Photographs (7.3k, 1 part).

## Loop
1. Launch only AFTER 002-F closes: `Workflow({scriptPath: ".../OS_CERT_WAVE_002G/control/scripts/wave002g-R1.js"})`.
2. Bank verified-only with `--map=.../OS_CERT_WAVE_002G/control/wave002g_map.json`.
3. Update PROGRESS_LEDGER + RUN_STATE; os_checkpoint CLEAN; BOUND==coverage_proven.

## Close gate (002-G)
Close when SCHEDULED->0 (target 2 BOUND). Write OS_RECEIPT, reconcile. THEN book DOCTRINE_EXTRACTION_SCHEDULED across the 297 ledger = 0 -> open the docs/tooling/transcripts ledger (see REFINERY_MASTER_STATE.docs_tooling_plan).

## Crash recovery
If /tmp/wave002g parts wiped: `python3 .../OS_CERT_WAVE_002E/control/build_wave.py 002-G <control_abspath>`. Never re-read banked rows.
