# Autonomous Refinery Loop Spec

Date: 2026-06-20
Purpose: turn the OS metabolization work into a durable controller loop instead of a fragile long chat.

## Source Inputs Read

- Claude Overload 7-day masterclass doc: WAT framework, MCP setup, skill lifecycle, Trigger.dev deployment, front-end screenshot loop, scheduled tasks versus loops, executive assistant structure.
- Claude Code on VPS transcript: always-on machine, tmux, remote control, phone/browser as window.
- Persistent private server transcript: sandboxed workspace, preinstalled tooling, preview URL, no laptop dependency.
- Scheduled tasks transcript: registry, logs, results, wrappers, test-run-before-trust, scoped permissions, output directory, timeout.
- Claude desktop update transcript: dispatch, computer use as fallback, precise tool first, schedule command, loop command, effort levels, DOM targeting, project memory.
- Executive assistant transcript: lean root instruction file, context/project/decision folders, skill and agent files with YAML frontmatter, model routing, saved reports, Git/version control, daily use makes the assistant stronger.
- Existing OS upgrade doc: `00_COMMAND_CENTER/OS_UPGRADE_FROM_VIDEOS_2026-06-08.md`.
- Current 002-D shadow controller: `00_COMMAND_CENTER/OS_CERT_WAVE_002D_CODEX_SHADOW/CODEX_SHADOW_002D.md`.

## Core Doctrine

The unit is not a chat turn. The unit is a controller loop.

A strong loop has four layers:

1. Controller: decides what should run next, reads the live state, owns the goal, and refuses false completion.
2. Worker: runs one bounded batch, writes artifacts, exits.
3. Watchdog: checks for stalls, rate limits, empty output, stale locks, and count drift.
4. Receipt: records what changed, what did not, what is safe to resume, and what remains.

Any loop missing one of those layers is only a long chat with optimism taped to it.

## What The Current 002-D Failure Proved

The overnight loop did real work, but the control surface was incomplete.

What worked:
- 53 books certified and persisted.
- Partial segment ledger has 53 records.
- Checkpoint is CLEAN.
- The partial receipt honestly says 002-D is not closed.

What failed:
- Batch d14 hung for roughly 6 hours on server-side rate limiting.
- The loop did not have a hard silence timeout that killed and retried the stuck batch.
- The loop did not automatically demote concurrency after a long hang soon enough.
- The operator had to notice the stall.

Root cause: worker batching existed, but watchdog authority was too weak.

## Required Loop Contract

Every future long refinery loop must have these files:

- `RUN_STATE.json`: current wave, target count, completed count, in-flight batch, last heartbeat, deadline, model routing.
- `PROGRESS_LEDGER.csv`: one row per batch, status, start time, end time, in-flight duration, result count, failure reason, retry count.
- `WATCHDOG.md`: stall rules, kill rules, backoff ladder, resume rules.
- `OS_RECEIPT.md`: partial or final, never omitted for serious work.
- `MORNING_REPORT.md`: operator-facing summary if the loop crosses a sleep window.

Recommended location pattern:

`00_COMMAND_CENTER/OS_CERT_WAVE_<WAVE>/control/`

## Watchdog Rules

Stall detection:
- No output growth for 30 minutes: warn and check process.
- No output growth for 45 minutes: stop that batch if safe, mark `STALLED_RETRY`.
- Any server-side rate-limit text: stop launching new batches, cool down, resume at 1 in flight.
- Empty output file after 15 minutes: treat as failed batch, not "running."
- Lock file older than active batch heartbeat: clear only after proving no live process is writing.

Backoff ladder:
- Normal: 2 Sonnet batches in flight.
- Stable for 3 clean batches: allow 3 in flight only if prior receipts show zero rate limits.
- First rate-limit: drop to 1 in flight for 2 clean batches.
- Second rate-limit in same wave: 1 in flight for rest of wave.
- Any 30-minute silence: no new launches until watchdog resolves the active batch.

Resume rules:
- Resume failed-only and un-run-only.
- Never re-read already banked records unless verifier failed their ledger.
- Any edition mismatch is doctrine metadata, not silent normalization.
- Any rejected source must name the reason and the proof path.

## Model Routing

- Bash/Python: counting, extraction, reconciliation, path checks, md5, checkpoint.
- Sonnet: whole-read, segment-ledger, 5-field doctrine, normal adversarial verify.
- Haiku: cheap classification, file inventory, shallow routing, low-risk summaries.
- Opus: cross-wave synthesis, contradiction resolution, hard judgment, failed Sonnet re-judge.

Do not use Opus for bulk reading unless Sonnet fails a specific book.

## Project Context Firewall

The root instruction file should not be a warehouse. It should be a router.

Root file should contain:
- current objective pointer
- global rules
- where to find project capsules
- where to find decisions
- where to find skills
- where to find tool routing
- what not to touch

Project context loads only when named, active, routed, or explicitly requested. This prevents KEN FILM, Alma, KOTS, client stills, and book canon from blending into one soup.

## Tool And App Integration Loop

After the book canon reaches `DOCTRINE_EXTRACTION_SCHEDULED = 0`, run a separate app/tool/doc program:

1. Inventory connected tools and apps.
2. For each tool, record: available, authenticated, local-only or cloud-ready, read/write/spend risk, best task, current skill pointer, missing skill, test status.
3. Build or update skills only where a real repeated workflow exists.
4. Test each skill on a paraphrased real task.
5. Register the tool in `OS_CAPABILITY_TOOL_ROUTING.md` only after the test passes.
6. Add a scheduled or manual routine only after the workflow passes twice manually.

This prevents fake "connected" tools from being counted as real operating power.

## Book Canon Finish Order

Current state at this spec:
- 002-D partial: 53 / 100 business books certified.
- 47 remain in 002-D.
- Whole book canon: 117 scheduled remain.

Finish order:
1. Resume 002-D from d14 with watchdog rules.
2. Run redo pool.
3. Close 002-D only when all 100 target rows reconcile.
4. Run 002-E, taste and culture.
5. Run 002-F, operations and AI automation.
6. Run 002-G, photography.
7. Only then run cross-canon synthesis with Opus.
8. Then open docs/tooling/transcripts metabolization as a separate ledger.

## Morning Report Contract

If a loop runs while the operator sleeps, the morning report must answer:

1. What was the starting count?
2. What is the current count?
3. What changed on disk?
4. What failed or stalled?
5. What was rejected and why?
6. What remains?
7. Is the checkpoint clean?
8. Was any destructive action taken?
9. What exact command or message resumes the loop?
10. What should not be claimed yet?

## Boundary Rules

- No deletion, move, archive, spend, post, publish, generation, or client-facing send unless explicitly approved.
- No visual artifact can be final without External Visual Proof Gate.
- No OS-complete claim while any book ledger row remains `DOCTRINE_EXTRACTION_SCHEDULED`.
- No long loop is accepted without a watchdog.
- No broad context loading unless the project is named or routed.

## Immediate Upgrade

Before resuming 002-D, Claude should add a control folder for the active wave with:

- `RUN_STATE.json`
- `PROGRESS_LEDGER.csv`
- `WATCHDOG.md`
- `RESUME_QUEUE.md`

Then resume from d14 at 1 to 2 Sonnet batches in flight, with the watchdog enforcing stall and backoff rules.

Codex shadow will continue checking receipts and count reconciliation from the side.

## Claude Overload Binding

The governing doctrine for Claude/automation work now lives at:

`00_COMMAND_CENTER/CLAUDE_OVERLOAD_MASTERCLASS_001/CLAUDE_OVERLOAD_DOCTRINE.md`

The takeover plan now lives at:

`00_COMMAND_CENTER/CLAUDE_OVERLOAD_MASTERCLASS_001/OS_TAKEOVER_UPGRADE_PLAN.md`

Any future refinery loop, scheduled task, skill build, MCP/tool integration, or executive-assistant routine must obey those docs first, then this loop spec.

Practical effect:

- plan the workflow before the tool run
- keep the root state lean
- use project capsules instead of context soup
- create a status file for recurring tasks
- create a watchdog for long loops
- test manually before scheduling
- record a receipt before claiming completion
