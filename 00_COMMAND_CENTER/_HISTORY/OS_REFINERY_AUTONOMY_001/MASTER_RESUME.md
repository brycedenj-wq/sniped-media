# MASTER RESUME · Continuous Refinery (books -> docs/tooling)

**Standing directive (operator 2026-06-20):** Keep the refinery working continuously until the intentional-source backlog is actually metabolized. This is NOT a one-off recovery pass. A crash or a new terminal must RESUME, never restart.

**Read order at any session/terminal start:**
1. `REFINERY_MASTER_STATE.json` (this folder) · global mission + active wave + SOP.
2. Active wave control folder `RUN_STATE.json` -> `PROGRESS_LEDGER.csv` -> `WATCHDOG.md` -> `RESUME_QUEUE.md`.
3. The wave `OS_RECEIPT.md`.

## The goal (in order, do not skip)
1. **Book canon to SCHEDULED=0**: 002-D (business) -> 002-E (taste/culture) -> 002-F (operations) -> 002-G (photography). Arbiter = `BOOK_CANON_CERTIFICATION_LEDGER.csv` (297 rows) reconciled against `OS_ENGAGEMENT_MANIFEST.csv` (1246 source rows). Invariant: `ACTIVE_DOCTRINE_BOUND == coverage_proven`.
2. **Docs/tooling/transcripts**: open `DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv`, disposition every source (bound / scheduled / reference / rejected / duplicate / missing / misclassified), drain to scheduled=0 the same way.

## Per-wave SOP (the loop)
`extract (deterministic) -> read (Workflow harness, Sonnet) -> bank verified-only -> reconcile -> close -> chain next`.
- **Extract**: `pdftotext` (.pdf) / `ebook-convert` (.epub/.mobi/.azw3/.djvu) from `~/Downloads/    SNIPED_OS/`. Split into ~42-80k-word parts. Durable re-extract script + slug->source map in the wave control folder (rebuild /tmp in one command after any reboot).
- **Read**: one Workflow per batch, role-scoped agents: reader-per-part (WHOLE-READ, never sample, segment ledger) -> certify (5-field doctrine) -> adversarial whole-read verify. `os_cost_guard` hook = SEQUENTIAL (1 workflow in flight). Respect it; do not clear the wave lock.
- **Bank verified-only** (gate): `segment_count>0` + 5 non-empty doctrine fields + `verdict.pass && coverage_verdict=='whole-read'`. Two path-matched flips (ledger status_v2 -> ACTIVE_DOCTRINE_BOUND; manifest class=source status -> coverage_proven) + append record to the wave segment ledger. Same-book duplicate -> DUPLICATE_OR_SUPERSEDED; truncated/unreadable source -> EXCEPTION (operator ratifies terminal dispositions at close).
- **Reconcile**: `os_checkpoint.py` CLEAN; update `PROGRESS_LEDGER.csv` + `RUN_STATE.json` (heartbeat) every batch.

## Watchdog (mandatory)
No output growth 30 min -> inspect. 45 min -> TaskStop, mark STALLED_RETRY, rerun failed-only. Rate-limit text -> drop concurrency. Stale lock -> clear only after proving no live writer. No closure without exact counts.

## Crash/new-terminal recovery
Prove no live writer (ps/lsof/TaskList/locks + heartbeat staleness). Rebuild /tmp text if gone. Inspect in-flight batches: no complete bankable output -> STALLED_RETRY + rerun failed-only. NEVER re-read banked rows. Resume at the next pending batch.

## Boundaries (hard)
No deletion / move / archive / spend / post / publish / generation / client-facing send. No broad project-context blending. No false completion. **No OS-complete claim while any scheduled source work remains** (books OR docs/tooling). Operator ratifies DUPLICATE/EXCEPTION terminal dispositions at wave close.

## Model routing
Bash/Python: extract, count, reconcile. Sonnet: read/synthesize/verify. Opus: reserved for cross-wave synthesis, contradiction resolution, failed-Sonnet re-judge only.
