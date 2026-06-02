---
name: master-consolidation
description: Update MASTER_INDEX.md, MASTER_CHUNK_MAP.json, ACTIVE_KNOWLEDGE_STATE.md after a batch validates clean. Argument is the batch number. Refuses to run if validation has not passed.
disable-model-invocation: false
---

Update the canonical master files for BATCH_$ARGUMENTS. This is the ONLY skill that writes to those files.

Preconditions (verify before any write):
1. `01_KNOWLEDGE_BASE/batches/BATCH_$ARGUMENTS_CHUNKS.jsonl` exists.
2. The `jsonl-validation` skill has been run on this batch in the current session and passed. If not, refuse and direct the operator to run it first.
3. No master file has been modified since the last `master-consolidation` run.

Steps:
1. Snapshot the current state. Copy `MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` to `.prev` siblings (e.g., `MASTER_CHUNK_MAP.json.prev`) for rollback and reconciliation.
2. Compute:
   - `PREV_TOTAL` = chunk count from `MASTER_CHUNK_MAP.json.prev` (or 0 if first run).
   - `ADDED` = line count of `BATCH_$ARGUMENTS_CHUNKS.jsonl`.
   - `NEW_TOTAL` = `PREV_TOTAL + ADDED`.
3. Update `MASTER_CHUNK_MAP.json` · add the new batch entry, update `total_chunks`, update per-domain counts.
4. Update `MASTER_INDEX.md` · append a narrative section for BATCH_$ARGUMENTS · domain coverage, source count, key concepts, cross-references to canon.
5. Update `ACTIVE_KNOWLEDGE_STATE.md`:
   - Bump "Total chunks in corpus" to `NEW_TOTAL`.
   - Bump "Batches complete" count.
   - Move BATCH_$ARGUMENTS from "recommended next" to "complete and canonical."
   - Update "Next batch (recommended, not executed)" to the next item in the queue.
6. Reconcile · confirm `NEW_TOTAL` in MASTER_CHUNK_MAP.json equals `PREV_TOTAL + ADDED`. If not, halt and roll back from `.prev` snapshots.
7. Print a one-line summary: `BATCH_<NNN> consolidated · +<ADDED> chunks · total <NEW_TOTAL>`.

Never run mid-batch. Never run on a JSONL that has not passed `jsonl-validation`. Never bulk-update multiple batches in one invocation.
