---
name: corpus-wave-runner
description: Metabolize a large set of sources (books, docs, transcripts) into the certified OS canon through a crash-durable controller loop, banking verified-only. Use when there is a backlog of intentional sources to certify into BOOK_CANON_CERTIFICATION_LEDGER / a disposition ledger, when resuming a stalled certification wave after a crash, or when the operator says "run/resume wave 00X", "certify these books/docs", or "drive DOCTRINE_EXTRACTION_SCHEDULED to 0". Proven across waves 002-D/E/F/G (170 rows reconciled, zero data loss) and the docs/tooling program. NOT for one-off single-doc reads (just read it) or creative production.
---

# Corpus Wave Runner

Metabolize a source backlog into the canon as a controller loop, not a loose chat. The unit of work is a wave with control files, batches, banking, reconciliation, and a receipt. Crash or new terminal must RESUME from disk, never restart.

## When to use
A backlog of intentional sources needs certifying (books, tool docs, transcripts); a wave stalled after a crash; or the operator says run/resume a wave or drive scheduled-count to 0. Pairs with `docs-tooling-metabolizer` (non-book lane) and the master controller at `OS_REFINERY_AUTONOMY_001/REFINERY_MASTER_STATE.json`.

## Inputs required
- The canonical ledger (e.g. `00_COMMAND_CENTER/BOOK_CANON_CERTIFICATION_LEDGER.csv`) with `status_v2`/`wave`/`path`, and the manifest (`OS_ENGAGEMENT_MANIFEST.csv`).
- The source files on disk (verify each `path` resolves; never assume).
- A wave control folder `OS_CERT_WAVE_<id>/control/`.

## Control files (mandatory, per wave)
`RUN_STATE.json`, `PROGRESS_LEDGER.csv`, `WATCHDOG.md`, `RESUME_QUEUE.md`, `OS_RECEIPT.md`. Update RUN_STATE + PROGRESS_LEDGER after EVERY batch (heartbeat).

## Steps (executable)
1. **Map (deterministic, Bash/Python):** join each scheduled ledger row to its source `path` + ext; verify existence. Build a slug->source map (durable copy in `control/`). Reuse `OS_CERT_WAVE_002E/control/build_wave.py` (wave-agnostic) and `join_002d.py`.
2. **Extract + split:** `pdftotext` for .pdf, `ebook-convert` (calibre) for everything else (.epub/.mobi/.azw3/.djvu/.docx). Split into ~45k-word parts (`build_wave.py` uses a fixed `WORDS_PER_PART = 45000`; the original hand-written book R-scripts used ~42-80k-word parts). Write to a `/tmp/wave<id>/` work dir at the exact paths the batch scripts expect. /tmp is volatile -> the durable rebuild is `build_wave.py` (one command after any reboot).
3. **Screen (deterministic):** dedup by md5 + pairwise title Jaccard (>=0.5 = same-book); flag low-word fragments. Same-book duplicate -> DUPLICATE_OR_SUPERSEDED; fragment/excerpt -> EXCEPTION; truncated/no-spend-to-acquire -> EXCEPTION. Inspect ambiguous high/low-word outliers before disposition (this rescued the Color Purple omnibus + a mislabeled Sherman Alexie novel). Apply pre-read dispositions directly, then rebuild batches for the real remainder.
4. **Read (harness, one Workflow per batch, Sonnet, SEQUENTIAL):** reader-per-part (WHOLE-READ, NEVER SAMPLE, emit a segment ledger + observations) -> certify (5-field doctrine: operating_principles, patterns_to_steal, traps_to_avoid, applies_in_sniped, does_not_apply) -> adversarial whole-read verify. `os_cost_guard` enforces one workflow in flight; respect it, do not clear the wave lock.
5. **Bank verified-only:** gate = `segment_count>0` + 5 non-empty doctrine fields + `verdict.pass && coverage_verdict=='whole-read'`. Two path-matched flips: ledger `status_v2` -> ACTIVE_DOCTRINE_BOUND; manifest (class=source) `status` -> coverage_proven. Append the record to a wave segment ledger in `01_KNOWLEDGE_BASE/cert_ledgers/`. Dedup/exception overrides route the screened rows to their terminal disposition. Reuse `OS_CERT_WAVE_002D/control/bank_002d.py --map=<wave_map> --write`.
6. **Reconcile:** `os_checkpoint.py` must stay CLEAN; invariant `ACTIVE_DOCTRINE_BOUND == coverage_proven`; ledger + manifest totals intact.
7. **Close:** only when the wave's rows reconcile (SCHEDULED -> 0). Write `OS_RECEIPT.md` (verify with `os_receipt.py verify`). Chain the next wave.

## Watchdog
No output growth 30 min -> inspect. 45 min -> TaskStop, mark STALLED_RETRY, rerun failed-only. Rate-limit text -> drop concurrency. Stale lock -> clear only after proving no live writer (no process / no lsof handles / TaskList empty / heartbeat stale). Big multi-part books run longer; thresholds key on NO output growth, not total runtime.

## Crash / new-terminal recovery
Prove no live writer; rebuild wiped /tmp via `build_wave.py`; inspect in-flight batches (no complete bankable output -> STALLED_RETRY + rerun failed-only); NEVER re-read banked rows. Resume at the next pending batch.

## Outputs
Banked canon rows (status flipped + segment ledger), updated control files, `OS_RECEIPT.md` (verify PASS), reconciled checkpoint.

## Boundaries
No deletion/move/archive/spend/post/publish/generation/client-send. Operator ratifies terminal dispositions (DUPLICATE/EXCEPTION) at wave close. No OS-complete claim while any scheduled source work remains.

## Test (paraphrased real task)
"Resume wave 002-D from disk after a crash" -> proved no live writer, rebuilt wiped /tmp text, marked stalled batches STALLED_RETRY, reran failed-only, banked verified-only, closed 100/100 with a passing receipt. Same engine then closed 002-E/F/G + docs-tooling.
