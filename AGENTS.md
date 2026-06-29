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

## Orchestration laws (added 2026-06-08, from the Claude Code workflow/agent/routine videos)

The unit of work is a HARNESS, not a chat turn. Default mode = orchestrate -> monitor -> promote. Manual single-thread is the exception (interactive creative judgment only).

1. **Harness-by-default routing.** Long / parallel / adversarial work (whole-watch many clips, whole-read many docs, multi-asset QA, broad sweeps) -> a Workflow (fan out fresh-context agents). A few delegated steps -> subagent. One recurring scoped job, unattended -> Managed Agent. Cadence, laptop-off -> Routine.
2. **The three single-agent failure modes (defend every time):** agentic laziness (declares done at partial -> count done vs required), self-preferential bias (a model cannot judge its own output -> route judging to a fresh-context / second-model Verify), goal drift (loses "do not do X" across compaction -> re-read the pinned STANDING_ORDER/NEXT_ACTION + constraints each phase).
3. **Adversarial Verify is a first-class phase.** No serious result is crowned until `adversarial-verify` (or the Gemini lane) tries to break it. Every workflow ends with it.
4. **Human approval moves to the BOUNDARY, not the middle.** No mid-run pause inside a fan-out or a routine. Approval lives between two harnesses (Routine A drafts+posts -> operator approves -> Routine B ships), at plan-approval before a workflow, or as a per-tool permission policy. Operator authorizes spend/publish.
5. **Workflow cost laws:** per-phase model routing (Sonnet/Haiku default, Opus only the hardest phase), a hard token budget + maxRounds<=6 stated in the prompt, `isolation:'worktree'` for any file-writing fan-out, a durable backlog file so reruns skip rediscovery.
6. **Routines/Managed-Agents (when enabled) discipline:** secrets go in the cloud Environment Variables panel, never `.env`; remote runs are stateless (commit master writes to GitHub within the run or they vanish); Claude may only push `claude/*` branches; local-only MCP (Premiere/AE/Blender/ElevenLabs/Higgsfield) is NOT reachable remotely -> keep that work local or use a hosted connector. Managed Agents bill the API key: a budget line + Analytics watch is required before any scheduled run.

Full plan + prioritized actions: `00_COMMAND_CENTER/OS_UPGRADE_FROM_VIDEOS_2026-06-08.md`. Standing Verify harness: `.claude/workflows/adversarial-verify.workflow.js`.

## Harness-mandatory law (added 2026-06-08)
Serious production work (film/photo/edit/composite/campaign/web/client deliverable) MUST run through a harness: a workflow with role-scoped agents (separate moment/select, grade, brand-taste, edit-build, and adversarial-verify agents), with the orchestrator owning the goal and final decision and the Stop gate blocking false completion. NO single agent selects, cuts, grades, reviews, and crowns its own work (that is self-preferential bias). Single-thread mode is allowed ONLY for casual drafting, quick messages, or low-risk notes. If a serious task is about to be done single-threaded: STOP before editing and spawn the harness.

## Production governance doctrine (added 2026-06-28, permanent)

The objective is to behave like a disciplined production organization that finishes what it starts and reports only what is objectively true. These four rules are permanent and override convenience.

1. **Mission Lock.** Once an approved sprint begins, the mission cannot be reinterpreted. Only a genuine execution blocker (something that makes completion impossible) may interrupt the approved sequencing. Do NOT substitute replanning for execution: improvements may be logged, they may not rewrite the mission. Approved mission sequencing is immutable.
2. **Repository Truth.** Never report work as complete until every governance document matches repository reality. Governance is deliverable work, not cosmetic. If the documents disagree with the repo, the project is not in a trustworthy state and is not done. Reconcile until document truth == repository truth.
3. **Completion Doctrine.** "Built", "Operator-Gated", "Live-Gated", and "Accepted" are DISTINCT production states. Never collapse them into "Done". A frozen hero candidate is not an accepted asset; a built document package is not a launched universe. State the exact state.
4. **Autonomous Runs.** Optimize for completed deliverables, not additional reasoning. Do not narrate every internal step. Execute, verify, continue. Checkpoint only at sprint boundaries (and at the real spend / publish / irreversible boundary, where the operator authorizes).

Full closeout that established this doctrine: `00_COMMAND_CENTER/THE_HOUSE/LATERRE/` (governance reconciliation + `LAUNCH_GAP_LIST.md`, 2026-06-28).
