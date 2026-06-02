# CLAUDE.md · AI-Brain-Refinery

@AGENTS.md

## Claude Code specifics

- **Skills live in `.claude/skills/`.** Available: `source-inventory`, `staging-plan`, `batch-extraction`, `jsonl-validation`, `master-consolidation`, `session-save`. Invoke via `/<skill-name>`.
- **Use `/clear` between unrelated tasks.** A staging plan session and a chunking session do not share context. Save state via `/session-save` first.
- **Use plan mode** for anything that would touch disk state (cp, mkdir, write to MASTER_*). Exit plan mode only after operator authorizes execution.
- **Default `AskUserQuestion` for ambiguous routing.** Chapter-slot collisions (e.g., `13_OPERATING_DISCIPLINE` vs `13_NETWORK`) are routing decisions. Ask, do not auto-rename.
- **Side questions go in `/btw`** so they do not enter conversation history.

## Current operating lock (date-sensitive · keep this section tight)

- Source universe: `~/Downloads/    SNIPED_OS` (2026-05-18).
- Next batch: BATCH_005 = photography canon (locked).
- Future batches queued: see `00_COMMAND_CENTER/SNIPED_OS_STAGING_PLAN_2026-05-18.md` §6.
- Future-source notes (uncanonical · do not chunk): `00_COMMAND_CENTER/future_sources/`.

## Hooks

Not configured yet. Hooks are a later pass once the skills have run once successfully.

## When to escalate to the operator

- Any disk-state change not in the authorized plan.
- Any chunk that fails `/jsonl-validation`.
- Any `source_file` value that cannot be resolved on disk.
- Any chapter-slot collision.
- Any time context exceeds 70% before reaching a clean save point.
