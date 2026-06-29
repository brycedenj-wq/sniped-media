# RESUME QUEUE - Wave 002-E (34 real books, 12 batches)

Built from the 39 wave=002-E DOCTRINE_EXTRACTION_SCHEDULED rows, minus 5 pre-read dispositions (3 DUPLICATE + 2 EXCEPTION) = 34 real books to whole-read + certify.

## Queue (12 Sonnet batches, SEQUENTIAL)
R1 (5b/7p) , R2 (5/10) , R3 (5/10) , R4 (4/10) , R5 (3/9) , R6 (3/9) , R7 (2/7) , R8 (2/8) , R9 (2/10) , R10 (1/6) , R11 (1/6) , R12 (1/7).

## Per-batch loop
1. Launch one R-batch: `Workflow({scriptPath: ".../OS_CERT_WAVE_002E/control/scripts/wave002e-R<N>.js"})`.
2. On completion: bank verified-only with `--map=.../OS_CERT_WAVE_002E/control/wave002e_map.json`.
3. Update PROGRESS_LEDGER.csv + RUN_STATE.json (heartbeat) every batch.
4. os_checkpoint CLEAN; BOUND==coverage_proven.
5. Launch the next. os_cost_guard enforces 1-in-flight.

## Crash recovery
If /tmp/wave002e parts are wiped: `python3 control/build_wave.py 002-E <control_abspath>` rebuilds them (re-extracts) and re-emits scripts. Then resume at the next PENDING batch. Never re-read banked rows.

## Close gate (002-E)
Close when 002-E rows reconcile (SCHEDULED->0): 34 BOUND (target) + 3 DUPLICATE + 2 EXCEPTION = 39. Write OS_RECEIPT, reconcile checkpoint, then chain 002-F.

## Notes
- the_color_purple = Alice Walker omnibus (3 novels); large read, legit.
- part_1_libgen_li = Sherman Alexie "The Absolutely True Diary of a Part-Time Indian" (mislabeled catalog metadata); real complete novel.
