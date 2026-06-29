# WATCHDOG - Wave 002-E (taste/culture, 34 real books)

Same rules as the master loop (`OS_REFINERY_AUTONOMY_001/MASTER_RESUME.md`).

- Heartbeat = output growth of the in-flight batch / progress in /workflows. Check each turn + on each notification.
- No output growth 30 min: inspect (Read the task output, check /workflows).
- No output growth 45 min: TaskStop, mark STALLED_RETRY in PROGRESS_LEDGER, rerun failed-only.
- Empty output file after 15 min: treat as failed batch.
- Server rate-limit text: drop concurrency (already 1 via os_cost_guard).
- Stale lock: clear ONLY after proving no live writer (TaskStop the suspect run first).
- SEQUENTIAL: os_cost_guard hook enforces 1 workflow in flight. Do not clear the wave lock.
- Big books (Color Purple omnibus 6 parts, Ulysses 7, Steve Jobs 6, Big Payback 6) legitimately run longer; the 30/45-min thresholds key on NO output growth, not total runtime.

## Bank rule
Bank verified-only: segment_count>0 + 5-field doctrine + adversarial whole-read pass.
`python3 00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/bank_002d.py <out.json> R<N> --map=00_COMMAND_CENTER/OS_CERT_WAVE_002E/control/wave002e_map.json --write`
Never re-read banked rows. 5 pre-read dispositions already applied (control/close_dispositions.json).
