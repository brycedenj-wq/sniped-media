# WATCHDOG - Wave 002-D resume (mandatory)

Heartbeat = growth of a batch's output file / progress in /workflows. Check at each turn and on each notification.

## Stall detection
- No output growth 30 min: warn, inspect the batch (Read its task output, check /workflows).
- No output growth 45 min: stop that batch if safe (TaskStop), mark STALLED_RETRY in PROGRESS_LEDGER, resume failed-only.
- Empty output file after 15 min: treat as failed batch, not "running".
- Lock file older than active batch heartbeat: clear ONLY after proving no live writer (TaskStop the suspect run first).

## Rate-limit handling
- Any server-side rate-limit text in a result: drop to 1 in-flight Sonnet batch for at least 2 clean batches.
- Second rate-limit in this wave: 1 in-flight for the rest of the wave.
- Cooldown between launches: one launch per completion notification (staggered).

## Backoff ladder
- Post-hang resume: 1 in flight.
- After 2 clean batches: allow 2 in flight.
- Never 3 unless 2 prior receipts show zero rate-limits (not the case this wave).
- Any 30-min silence: no new launches until the active batch is resolved.

## Bank rule
- Bank verified-only: segment_count>0 + 5-field doctrine + adversarial whole-read pass.
- Never re-read banked 53 unless a verifier/ledger fails them.
- Edition mismatch (Dalio 2011 vs 2017) = doctrine metadata, recorded, not silently normalized.
