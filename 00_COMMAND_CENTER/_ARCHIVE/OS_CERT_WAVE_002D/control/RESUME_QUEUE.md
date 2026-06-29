# RESUME QUEUE - Wave 002-D (47 scheduled)

Rebuilt fresh from the 47 `wave=002-D` `DOCTRINE_EXTRACTION_SCHEDULED` rows (NOT the old d14-d24 scripts), so no banked-53 book can be re-read. All 47 have extracted text on disk. The redo-pool books (early-burst failures from d1/d2/d3, and the 2 strict-reverted incl Dalio 2011 ed) are inside this 47.

## Queue (13 Sonnet batches, staggered)
R1 (6) , R2 (6) , R3 (5) , R4 (4) , R5 (4) , R6 (4) , R7 (4) , R8 (4) , R9 (3) , R10 (2) , R11 (2) , R12 (2) , R13 (1). Total 47 books.

## Cadence (watchdog-governed)
- Start at 1 in flight (post-rate-limit backoff). Escalate to 2 after 2 clean batches.
- One launch per completion notification. Cooldown between launches.
- Clear the wave lock only after proving no live writer (TaskStop any suspect run first).

## Per-batch loop
1. Launch one R-batch (Sonnet).
2. On completion: bank verified-only (segment_count>0 + 5-field doctrine + adversarial whole-read).
3. Update PROGRESS_LEDGER.csv (status, result_count, failures) and RUN_STATE.json (bound/scheduled, heartbeat).
4. Flip verified books -> coverage_proven (manifest) + ACTIVE_DOCTRINE_BOUND (ledger). Keep 297 reconciled.
5. Launch the next R-batch. If a batch rate-limits or stalls: apply WATCHDOG (TaskStop, STALLED_RETRY, resume failed-only, drop concurrency).

## Close gate (002-D)
Close only when all 100 wave=002-D rows reconcile (SCHEDULED -> 0). Then OS_RECEIPT (verdict internal, full), checkpoint reconcile, answer the Codex 15-item acceptance gate.

## Dalio note
Dalio "Principles" file is the 2011 self-published edition (no 2017 Part-1 biography). The reader reads the actual file; the doctrine record must state it is the 2011 edition, not normalize to 2017.
