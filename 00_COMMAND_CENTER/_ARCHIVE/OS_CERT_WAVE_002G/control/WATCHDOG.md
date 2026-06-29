# WATCHDOG - Wave 002-G (photography, 2 books, 1 batch)

Master rules: `OS_REFINERY_AUTONOMY_001/MASTER_RESUME.md`.
- No output growth 30 min: inspect. 45 min: TaskStop -> STALLED_RETRY -> rerun failed-only.
- Rate-limit text: drop concurrency (already 1 via os_cost_guard). Stale lock: clear only after proving no live writer.

## Bank rule
`python3 00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/bank_002d.py <out.json> R1 --map=00_COMMAND_CENTER/OS_CERT_WAVE_002G/control/wave002g_map.json --write`
Gate: segment_count>0 + 5-field doctrine + adversarial whole-read. No pre-read dispositions (screen clean).
