# RESUME QUEUE - Wave 002-F (29 operations books, 8 batches)

Built by build_wave.py from the 29 wave=002-F DOCTRINE_EXTRACTION_SCHEDULED rows. Pre-read screen CLEAN (no dups, no fragments) -> all 29 are real books to whole-read + certify.

## Queue (8 Sonnet batches, SEQUENTIAL)
R1 (5b/6p) , R2 (5/10) , R3 (5/10) , R4 (4/9) , R5 (3/9) , R6 (3/9) , R7 (2/7) , R8 (2/9).

## Per-batch loop
1. `Workflow({scriptPath: ".../OS_CERT_WAVE_002F/control/scripts/wave002f-R<N>.js"})`.
2. Bank verified-only with `--map=.../OS_CERT_WAVE_002F/control/wave002f_map.json`.
3. Update PROGRESS_LEDGER + RUN_STATE (heartbeat) every batch. os_checkpoint CLEAN; BOUND==coverage_proven.
4. Launch next (os_cost_guard = 1 in flight).

## Crash recovery
If /tmp/wave002f parts wiped: `python3 .../OS_CERT_WAVE_002E/control/build_wave.py 002-F <control_abspath>` rebuilds. Resume at next PENDING. Never re-read banked rows.

## Close gate (002-F)
Close when SCHEDULED->0 (target 29 BOUND, adjust if any reader surfaces a dup/fragment at bank time). Write OS_RECEIPT, reconcile, then chain 002-G (2).
