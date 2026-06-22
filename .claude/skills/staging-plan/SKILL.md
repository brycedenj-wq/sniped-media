---
name: staging-plan
description: Turn the latest source inventory into a staging plan for raw/. Produces mkdir + cp commands as recommendations only. No execution.
disable-model-invocation: false
---

Read the latest `00_COMMAND_CENTER/*_FULL_SOURCE_INVENTORY_*.md`, the current state of `~/AI-Brain-Refinery/raw/`, and the processed sources in `01_KNOWLEDGE_BASE/batches/BATCH_*.jsonl`. Produce a staging plan.

1. Define `SRC` and `DST` shell variables at the top of every command block. Quote `SRC` exactly when the path contains leading spaces.
2. Group new files by destination subfolder under `raw/`. Use the existing chapter structure (`00_BRIEF/` through `99_VAULT/` plus `02_TIER_1_CANON_BOOKS/<sub>/` and `03_TIER_2_CANON_BOOKS/<sub>/`).
3. Emit `mkdir -p` + `cp -p` commands per destination, with exact source filenames quoted. NEVER use bare globs that could pull untracked files.
4. Flag chapter-slot numbering collisions (e.g., `05_AI_EDGE_COURSE` vs `05_PRODUCTION`). Surface as a table with clean alternatives. Do not auto-rename.
5. List files to IGNORE / DEFER with reasons: stale lock files, `.part` fragments, superseded artifacts, side-quest items, installers, internal duplicates.
6. Resolve internal duplicates explicitly (which copy to keep, which to skip).
7. Add a post-staging verification block with `ls -la` checks per destination and a `find` sweep that should return zero results for ignored patterns.
8. Recommend the next 5 batches based on the staging gap.
9. Write the plan to `00_COMMAND_CENTER/<SOURCE-NAME>_STAGING_PLAN_<YYYY-MM-DD>.md`.

All commands are recommendations. The skill does NOT execute them. Operator authorizes execution in a separate session.


## INVOKE WHEN
- Turn the inventory into a staging plan for raw/
- Plan the copy pass from SNIPED_OS into raw/ for the next batch
- Generate staging commands from the latest source inventory

## Inputs
- Latest 00_COMMAND_CENTER/*_FULL_SOURCE_INVENTORY_*.md (must exist before this skill runs)
- Current ~/AI-Brain-Refinery/raw/ directory tree
- 01_KNOWLEDGE_BASE/batches/BATCH_*.jsonl for already-processed source_file values

## Outputs
- 00_COMMAND_CENTER/<SOURCE-NAME>_STAGING_PLAN_<YYYY-MM-DD>.md containing: SRC/DST shell variable block (SRC quoted for leading-space paths), grouped mkdir -p + cp -p commands per raw/ destination subfolder, chapter-slot collision table with clean alternatives, IGNORE/DEFER list with per-file reasons, internal-duplicate resolution table, post-staging verification block (ls -la per dest + find sweep for ignored patterns), and a recommended next-5-batches list

## Gates
- All cp commands use exact quoted filenames -- no bare globs
- Chapter-slot collisions (e.g., 05_AI_EDGE_COURSE vs 05_PRODUCTION) are surfaced as a table; skill does NOT auto-rename
- Internal duplicates are explicitly resolved (which copy to keep, which to skip) before any command is emitted
- All commands are recommendations only -- skill does NOT execute them
- Post-staging verification block (ls -la + find sweep) is present for operator to run after authorized execution

## Test
- case: After a completed source inventory, operator says 'build the staging plan for BATCH_006 photography sources.' Expected output: a dated .md plan at 00_COMMAND_CENTER/SNIPED_OS_STAGING_PLAN_2026-06-21.md with SRC/DST variable block, mkdir -p + cp -p commands grouping photography files under raw/02_TIER_1_CANON_BOOKS/ or appropriate chapter, any slot-collision table if needed, IGNORE list for .part/.dmg/lock files, duplicate resolution notes, ls -la + find verification block, and a recommended next-5-batches list starting with BATCH_006.
- expected failure: No source inventory .md exists in 00_COMMAND_CENTER/ yet: skill must halt and ask the operator to run /source-inventory first, because the plan has no inventory to read from.
