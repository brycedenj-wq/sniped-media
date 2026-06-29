> **Retired 2026-06-28.** One or more OS_* systems referenced in this document were retired during the OS repository convergence and moved to `_HISTORY/` or `_ARCHIVE/`. Those references are historical and no longer active. See `CONVERGENCE_PLAN_2026-06-28.md`.

# CONTEXT BOOT CARD (read this first, one screen)

The single card a fresh session/terminal reads to reconstruct context. Phase 4 audit fixed: no longer 3-4 files to reconstruct state. Updated at each clean boundary.

**As of 2026-06-21.**

## Current state (one paragraph)
Corpus metabolization is RECONCILED: book canon 297 rows, DOCTRINE_EXTRACTION_SCHEDULED=0 (240 BOUND + dups/exceptions/etc.); docs/tooling ledger 50/50 terminal. Checkpoint CLEAN, coverage_proven==BOUND==240. OS_TAKEOVER Phases 4-7 audit DONE + verified; execution underway: skill program 85/85 ACTIVE (INSTALLED_INCOMPLETE=0), structure basics populated. The OS is NOT complete (takeover routine-piloting + tool live-verification remain).

## What is the live mission
Continuous refinery + OS takeover. Source of truth: `OS_REFINERY_AUTONOMY_001/REFINERY_MASTER_STATE.json` (mission + phase) and `OS_TAKEOVER_PHASES_001/` (takeover audit + execution).

## Read order (only if you need more than this card)
1. This card.
2. `NEXT_ACTION.md` (live next action + standing mission).
3. `OS_REFINERY_AUTONOMY_001/REFINERY_MASTER_STATE.json` (phase, backlog, SOP).
4. The active program's `RUN_STATE.json` (per wave/program control folder).
5. Latest `session_saves/SESSION_SAVE_*.md`.

## Active blockers (operator-gated)
- Routine piloting: candidate routines need 2 manual proofs each before any cron (see `OS_TAKEOVER_PHASES_001/OS_ROUTINE_PILOT_PACKAGE.md`).
- Tool live-verification: several MCP tools are UNTESTED/UNVERIFIED-LIVE; need read-only safe-first-tests (see `OS_TOOL_READINESS_LAYER.md`). Premiere MCP last ping TIMED OUT 2026-06-13.
- 6 photography videos = EXCEPTION (transcription needs a Whisper key / spend); reopen only if a key is added.

## Standing boundaries (hard)
No spend, deletion, move, archive, post, publish, generation, client-facing send, or live cron creation without explicit operator approval. No OS-complete claim while any of the above blockers are open. Project facts live in project capsules, never in permanent OS. No em-dashes.

## Decision log + failure log
Decisions: `decisions/DECISIONS_INDEX.md`. Failures + lessons: `OS_FAILURE_LEDGER.csv` (16 rows).
