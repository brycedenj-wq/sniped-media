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
