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


## Inputs
- Batch argument passed as $ARGUMENTS (e.g., OPERATOR_DOCS_CLEANUP)
- Passing jsonl-validation run for this batch in the current session (required precondition)
- 01_KNOWLEDGE_BASE/batches/BATCH_$ARGUMENTS_CHUNKS.jsonl must exist on disk
- Current MASTER_CHUNK_MAP.json, MASTER_INDEX.md, and ACTIVE_KNOWLEDGE_STATE.md (all read before any write)

## Outputs
- MASTER_CHUNK_MAP.json updated: new batch entry added, total_chunks bumped to NEW_TOTAL, per-domain counts updated
- MASTER_INDEX.md updated: narrative section appended for the batch (domain coverage, source count, key concepts, cross-references to canon)
- ACTIVE_KNOWLEDGE_STATE.md updated: total chunks bumped to NEW_TOTAL, batches-complete count bumped, batch moved to canonical, next-batch pointer updated
- .prev snapshot siblings created for all three master files before any write for rollback (e.g., MASTER_CHUNK_MAP.json.prev)
- One-line summary printed: BATCH_NAME consolidated + ADDED chunks + total NEW_TOTAL

## Gates
- Precondition gate: BATCH_$ARGUMENTS_CHUNKS.jsonl must exist on disk -- refuses if absent
- Precondition gate: jsonl-validation must have passed in the current session -- refuses and redirects if not
- Precondition gate: no master file may have been modified since the last master-consolidation run -- refuses if drift detected
- Reconciliation gate: after writing, NEW_TOTAL in MASTER_CHUNK_MAP.json must equal PREV_TOTAL + ADDED -- halts and rolls back from .prev snapshots if mismatch
- Single-batch gate: never bulk-updates multiple batches in one invocation; never runs mid-batch

## Test
- case: A new mini-batch OPERATOR_DOCS_CLEANUP has just been chunked and jsonl-validation passed in the current session, producing OPERATOR_DOCS_CLEANUP_CHUNKS.jsonl with 22 lines. Current MASTER_CHUNK_MAP.json shows total_chunks = 1879 (the real corpus total after Promotion Batch 1 consolidated DECISION_SYSTEMS_SUPP + TOOLCHAIN_DISTRIBUTION_SUPP + LEADERSHIP_SUPP on 2026-05-31). Skill creates .prev snapshots of all three master files, reads PREV_TOTAL = 1879, reads ADDED = 22 from the JSONL line count, computes NEW_TOTAL = 1901, writes the batch entry and updated total to MASTER_CHUNK_MAP.json, appends narrative to MASTER_INDEX.md, updates ACTIVE_KNOWLEDGE_STATE.md (total = 1901, OPERATOR_DOCS_CLEANUP marked canonical), confirms 1879 + 22 = 1901, and prints: 'BATCH_OPERATOR_DOCS_CLEANUP consolidated + 22 chunks + total 1901'.
- expected failure: Skill runs without a passing jsonl-validation in the current session, OR updates multiple batches in one invocation, OR writes to master files without creating .prev snapshots first, OR prints the final summary without verifying NEW_TOTAL = PREV_TOTAL + ADDED, OR accepts a batch argument for a JSONL that does not exist on disk.


## INVOKE WHEN
- Operator says 'consolidate BATCH_X' or 'run master-consolidation on [batch name]'
- jsonl-validation has just passed for a batch in the current session and the operator authorizes the consolidation step (Step 7 of the 7-step SOP)
- Operator says 'update the master files' or 'promote [batch name] to canonical'
- Operator explicitly authorizes the master write after a clean validation result
