# WATCHDOG - Wave 002-F (operations, 29 books)

Master rules: `OS_REFINERY_AUTONOMY_001/MASTER_RESUME.md`.
- No output growth 30 min: inspect. 45 min: TaskStop -> STALLED_RETRY -> rerun failed-only.
- Empty output after 15 min: failed batch.
- Rate-limit text: drop concurrency (already 1 via os_cost_guard).
- Stale lock: clear only after proving no live writer.
- Big books (the_operator 5 parts/213k, davidson 4, suleyman 3) run longer; thresholds key on NO output growth.

## Bank rule
`python3 00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/bank_002d.py <out.json> R<N> --map=00_COMMAND_CENTER/OS_CERT_WAVE_002F/control/wave002f_map.json --write`
Gate: segment_count>0 + 5-field doctrine + adversarial whole-read. Never re-read banked rows. No pre-read dispositions (screen was clean).
