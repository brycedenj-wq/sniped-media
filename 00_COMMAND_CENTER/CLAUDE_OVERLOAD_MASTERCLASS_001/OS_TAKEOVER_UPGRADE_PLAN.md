> **Retired 2026-06-28.** One or more OS_* systems referenced in this document were retired during the OS repository convergence and moved to `_HISTORY/` or `_ARCHIVE/`. Those references are historical and no longer active. See `CONVERGENCE_PLAN_2026-06-28.md`.

# OS Takeover Upgrade Plan

Date: 2026-06-20
Status: active plan
Source doctrine: `CLAUDE_OVERLOAD_DOCTRINE.md`
Anchor-class: markdown-only, not chunked, not in master files

## Purpose

Turn the masterclass from "good ideas in a doc" into the operating behavior of the OS.

The goal is not more files. The goal is fewer weak chats, fewer false completions, cleaner routing, stronger loops, and a system that keeps improving without blending unrelated projects together.

## Phase 0: Binding, Done In This Pass

Create the masterclass doctrine packet and wire it into the live router:

- `CLAUDE_OVERLOAD_DOCTRINE.md`
- `OS_TAKEOVER_UPGRADE_PLAN.md`
- `CLAUDE_SEND_PACKET.md`
- `OS_RECEIPT.md`
- `OS_ROUTER_INDEX.md` pointer
- `NEXT_ACTION.md` pointer
- `OS_CURRENT_STATE.md` pointer
- `AUTONOMOUS_REFINERY_LOOP_SPEC.md` pointer

Acceptance:

- Router search finds the doctrine.
- Boot state names the doctrine.
- Receipt proves the source was extracted and segmented.

## Phase 1: Stabilize The Active Book Loop

Before any 002-D resume:

- create `00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/RUN_STATE.json`
- create `PROGRESS_LEDGER.csv`
- create `WATCHDOG.md`
- create `RESUME_QUEUE.md`
- clear stale locks only after proving no live writer
- run Sonnet batches with watchdog backoff
- bank verified-only

Acceptance:

- no batch can hang silently for hours
- redo pool is explicit
- every completion claim has a receipt

## Phase 2: Finish Book Canon

Finish:

- 002-D business
- 002-E taste and culture
- 002-F operations and AI automation
- 002-G photography

Rules:

- Sonnet for bulk read/synthesis/verify
- Opus only for final cross-canon synthesis and contradictions
- no book status flip without segment ledger and adversarial verify
- no OS-complete claim while scheduled count is above 0

Acceptance:

- `DOCTRINE_EXTRACTION_SCHEDULED = 0`
- ledger reconciles to 297 rows
- dashboard/checkpoint clean
- final book-canon receipt says what changed and what remains

## Phase 3: Docs, Tooling, Transcripts

After book canon, open a separate non-book metabolization program.

Scope:

- tool docs
- Claude docs
- MCP docs
- Higgsfield/Seedance/video docs
- design-system transcripts
- automation transcripts
- app setup notes
- local connected-app notes

Deliverables:

- `DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv`
- one status per source: bound, scheduled, reference-active, rejected, duplicate, missing, misclassified
- active doctrine files only where the source changes behavior
- router pointers only after proof

Acceptance:

- no half-read "doc soup"
- every intentionally added doc has a disposition
- tool claims match tested reality

## Phase 4: Executive Assistant Structure Audit

Audit whether the repo has clean equivalents of:

- context
- projects
- decisions
- references
- skills
- tools
- logs
- archives

Deliverable:

- `OS_EXECUTIVE_ASSISTANT_STRUCTURE_AUDIT.md`

Acceptance:

- one active objective pointer
- project capsules for live projects
- retired lanes walled off
- decision log exists and is current
- root state stays lean

## Phase 5: Skill Upgrade Program

For each repeated workflow:

1. prove the manual process
2. convert to skill only if repeated
3. tighten frontmatter trigger
4. keep `SKILL.md` concise
5. move rubrics to references
6. test on paraphrased real tasks
7. log first failures and patch

High-priority skills to audit:

- project intake capsule
- book certification wave runner
- docs/tooling metabolization
- external visual proof packet
- morning cockpit
- pulse check
- tool/app integration audit
- client delivery wrap

Acceptance:

- no skill counted as live without a test
- stale or over-triggering skills are tightened

## Phase 6: Tool And MCP Integration Audit

For every connected app/tool:

- available
- authenticated
- local-only or cloud-ready
- read/write/spend risk
- best task
- skill pointer
- missing skill
- test status
- last verified date

Deliverable:

- `OS_TOOL_APP_INTEGRATION_LEDGER.csv`

Acceptance:

- no "installed equals useful" claims
- no spend-capable tool runs without approval
- stale docs/tool names carry warning labels

## Phase 7: Scheduled Tasks And Routines

Only after a workflow passes manually twice:

- create a status file
- define exact schedule or loop window
- define permission boundaries
- run manually once
- confirm no permission prompts
- add notification/hook
- record where results land

Candidate routines:

- morning cockpit
- weekly active-project pulse
- book/docs refinery checkpoint
- stale-tool verification reminder
- source-retirement review reminder

Acceptance:

- each routine has a status file
- each routine has a receipt or report
- destructive actions are blocked
- laptop-dependent tasks are labeled local
- cloud tasks have proper env var guidance

## What Not To Do

- do not bulk-load every source into every chat
- do not create random skills before the manual process works
- do not route retired project context into new projects
- do not call a tool connected until it passes a real test
- do not call visual work final without external proof
- do not call the OS complete while books, docs, tools, or project capsules remain unresolved

## Current Next Move

If the operator says go:

1. Resume 002-D only after creating the control folder.
2. Finish all book waves.
3. Then open docs/tooling/transcripts metabolization.
4. Then run the executive assistant structure audit.
5. Then build scheduled routines from proven workflows.

This is the takeover path.
