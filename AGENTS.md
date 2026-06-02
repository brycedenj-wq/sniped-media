# AGENTS.md · AI-Brain-Refinery

A SNIPED Media corpus refinement workspace. Reads source documents, chunks them into a structured knowledge base, and feeds the SNIPED operating system.

## Source universe and folder semantics

- **Source universe (2026-05-18):** `~/Downloads/    SNIPED_OS/` only. Folder name has 4 leading spaces. Quote it in shell.
- **`raw/`:** staged intake mirror. Do not edit by hand outside an authorized staging pass.
- **`01_KNOWLEDGE_BASE/`:** processed brain. Holds `batches/BATCH_<NNN>_CHUNKS.jsonl`, `MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`. Written by the `master-consolidation` skill only.
- **`00_COMMAND_CENTER/`:** plans, inventories, future-source notes, session saves. Markdown only.
- **`outputs/`, `batches/`, `indexes/`, `scripts/`:** legacy locations from earlier passes. `scripts/` is active tooling; the rest are read-only.

## JSONL chunk schema (BATCH_003 onwards · canonical)

Per-line fields: `chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags`.

BATCH_002 uses `batch` instead of `batch_id`. Both schemas are canonical for their respective batches. Do not migrate retroactively.

## Workflow · the locked 7-step SOP

1. Inventory the source universe.
2. Plan the staging.
3. Operator authorizes the copy pass.
4. Stage into `raw/`.
5. Extract into `01_KNOWLEDGE_BASE/batches/batch_<NNN>_extracted/`.
6. Chunk + validate.
7. Consolidate + session-save.

Never skip steps. Never run a later step before an earlier step has produced its output.

## Verification rituals

Every batch run passes these checks before chunks become canonical:
- Every line of `BATCH_<NNN>_CHUNKS.jsonl` parses via `jq -c .`
- Required schema fields present per line
- `chunk_id` unique within the batch
- `batch_id` consistent across all lines
- Every `source_file` value resolves on disk
- Master count after consolidation = previous count + new chunks

If any check fails, halt and surface to the operator. Do not write to master files.

## Drift-prevention rules

1. Never process `~/Downloads/` globally unless explicitly instructed.
2. Source universe = `~/Downloads/    SNIPED_OS` only (until brief says otherwise).
3. `raw/` is staged intake. Do not edit as a working tree.
4. `01_KNOWLEDGE_BASE/` is processed brain. Do not modify by hand.
5. Never update master files mid-batch.
6. Never move, delete, rename, or extract during planning sessions.
7. No em-dashes anywhere, ever.
8. Always count before assuming.
9. Surface chapter-slot collisions; do not auto-rename.

## What to read at session start

- `00_COMMAND_CENTER/ACTIVE_KNOWLEDGE_STATE.md` · what is canon now, what is next.
- The latest `00_COMMAND_CENTER/*_STAGING_PLAN_*.md` if a staging pass is pending.
- `01_KNOWLEDGE_BASE/MASTER_INDEX.md` · narrative consolidation of the chunked corpus.

## Out of scope (without explicit operator instruction)

- The rest of `~/Downloads/` outside `    SNIPED_OS`.
- `~/sniped-media/` (web project codebase).
- Any disk-state change during a planning session.
- BATCH_005 redefinition (locked as photography canon).
