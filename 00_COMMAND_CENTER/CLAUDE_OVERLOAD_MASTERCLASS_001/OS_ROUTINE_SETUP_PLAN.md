> **Retired 2026-06-28.** One or more OS_* systems referenced in this document were retired during the OS repository convergence and moved to `_HISTORY/` or `_ARCHIVE/`. Those references are historical and no longer active. See `CONVERGENCE_PLAN_2026-06-28.md`.

# OS Routine Setup Plan

**Phase:** OS Takeover Phase 7 - Scheduled Tasks and Routines
**Date:** 2026-06-21
**Status:** PLAN ONLY - no cron, no routine, no live creation
**Source doctrine:** `CLAUDE_OVERLOAD_DOCTRINE.md` - Loop / Schedule / Cloud section, Self-Improving Status File section
**Governing law:** A routine may be PROMOTED to live only after its underlying workflow passes manually TWICE.
**Author:** Sonnet 4.6 subagent (every claim grounded in Phase 4-6 audit data and disk reads)

---

## Governing Rules Before Reading Anything Else

1. A scheduled task is NOT a loop. A loop keeps session context and dies with the session. A scheduled task is stateless - it must read a status file before work and overwrite it after work.
2. LOCAL-ONLY MCP tools (Premiere Pro, After Effects, Blender, ElevenLabs, Higgsfield) CANNOT run inside a cloud routine. Those routines are either local-only (laptop must be open) or require a hosted connector that does not exist yet.
3. Cloud routines must store secrets in the host's Environment Variables panel, not in a local `.env` file.
4. Permission boundaries are hardcoded per routine. No routine may spend, post, publish, delete, or move without explicit operator approval at the moment of spend/post. Approval belongs at the boundary between routines, not mid-run.
5. Every routine has a single status file it reads at start and overwrites at end. This is how the assistant improves run-to-run without infinite context.
6. Destructive actions (delete, move, archive, client-send) are BLOCKED inside all routines.
7. No routine goes live until it has a status file path, a receipt from the first manual run, and zero permission-prompt blockers on that manual run.

---

## The Five Candidate Routines

### Routine A: Morning Cockpit

**Purpose:** Boot the operator into the week without a long context re-read. Surface: what is the live mission, what is blocked, what is the highest-leverage action today. Replaces ad hoc "what should I do" chats with a single structured output.

#### Does a proven manual workflow or skill exist? (P5 citation)

PARTIAL - NOT READY.

The `sniped-monday-cockpit` skill exists at `.claude/skills/sniped-monday-cockpit/SKILL.md`. It fires on "Plan my week / Monday morning / what should I focus on" and reads `~/Downloads/    SNIPED_OS/00_BRIEF/` files. However:

- The skill reads from `~/Downloads/    SNIPED_OS/00_BRIEF/MONDAY_COCKPIT.md` (the SNIPED source universe), but the current live mission state lives in `00_COMMAND_CENTER/NEXT_ACTION.md`, `OS_CURRENT_STATE.md`, and `ACTIVE_KNOWLEDGE_STATE.md` inside this repo. Those two context layers are not joined.
- The `sniped-monday-cockpit` skill is for the SNIPED OS launch lane (weekly 3 outcomes, LinkedIn POV cadence). The OS Takeover cockpit is different: it answers "what is the live mission, what wave is running, what is blocked, what is the scheduled-tasks readiness." These are separate scopes.
- No single manual morning cockpit has been run as a workflow with a status file and receipt. The existing `OS_MORNING_REPORT_2026-06-04.md` in the command center is the closest prior artifact, but it was written ad hoc inside a long chat, not as a structured stateless routine with a status-file read/write cycle.
- P5 skill audit found the skill lifecycle incomplete: no test record, no first-failure patch log, no second manual run receipt.

**Readiness: NEEDS-MANUAL-PROOF-FIRST**

#### Proposed schedule or loop window

Daily at 07:00 local (laptop must be open). Not a cloud routine - it reads local OS files. Not time-critical to the minute; 07:00 is aspirational; the real trigger is session start on any day the operator has not already reviewed.

Alternative trigger: operator types "cockpit" or opens a new Claude Code session. This is actually a better trigger than a cron for a local-only routine. The "schedule" is: run as the first thing in any new session if the status file is more than 18 hours old.

#### Permission boundaries

- READ: `00_COMMAND_CENTER/NEXT_ACTION.md`, `OS_CURRENT_STATE.md`, `ACTIVE_KNOWLEDGE_STATE.md`, `LANE_DISCOVERY_LEDGER.md`, `00_COMMAND_CENTER/CLAUDE_OVERLOAD_MASTERCLASS_001/OS_RECEIPT.md`, `00_COMMAND_CENTER/OS_CERT_WAVE_*/control/RUN_STATE.json`.
- WRITE: one status file only (path below). One output report to command center.
- BLOCKED: no spend, no post, no publish, no delete, no move, no archive, no book-status mutation, no master-corpus write.

#### Status file path

`00_COMMAND_CENTER/ROUTINES/morning_cockpit/STATUS.json`

```json
{
  "last_run": "ISO-8601",
  "last_result": "clean | blocked | no_change",
  "live_mission": "...",
  "wave_state": "...",
  "blockers": [],
  "highest_leverage_action": "...",
  "known_issues": [],
  "what_changed": "...",
  "next_suggested_improvement": "...",
  "what_not_to_repeat": "..."
}
```

#### Where results land

`00_COMMAND_CENTER/ROUTINES/morning_cockpit/MORNING_REPORT_<YYYY-MM-DD>.md`

The status file is overwritten every run. Reports accumulate (one per day) as a log of what state the OS was in each morning. After 14 days the operator reviews and prunes. Reports are never auto-deleted by the routine.

#### Manual proof steps remaining before promotion

1. Define the cockpit scope precisely: is it the SNIPED lane cockpit (skill), the OS Takeover cockpit (mission + wave state), or both? Operator decides. Do not run both from one routine - scope collision is a context-soup risk.
2. Draft the cockpit prompt as a single markdown file: `00_COMMAND_CENTER/ROUTINES/morning_cockpit/COCKPIT_PROMPT.md`. It must name every file it reads, its output format, its permission boundaries, and its status-file contract.
3. Run the cockpit prompt manually once in a fresh Claude Code session (clear context first). Read the status file. Confirm output matches expected format.
4. Fix any file-path errors or missing-file errors. Confirm zero permission prompts (all reads already pre-approved in `.claude/settings.json` or added before the run).
5. Run it a second time in a different fresh session. Confirm status file is overwritten cleanly. Confirm report is written.
6. After two clean manual runs, the routine is eligible for promotion to a local scheduled task.

---

### Routine B: Weekly Active-Project Pulse

**Purpose:** Every Friday or Sunday, surface the open project capsule list, flag any project with no forward movement in 7 days, and write a one-page pulse report. Catches drift before it becomes a missed commitment.

#### Does a proven manual workflow or skill exist? (P5 citation)

NO. There is no pulse-check workflow or skill in the P5 audit. The Phase 4 structure audit found that NO live project folder contains a filled `PROJECT_CAPSULE.md` (the template exists in the command center but has never been applied). This means:

- There is no capsule to pulse-check yet. The first prerequisite is that project capsules exist.
- The `sniped-execution-prioritization` skill covers "what should I do next" at session start, but it reads from the SNIPED OS source folder, not from live project capsules in this repo.
- The closest artifact is `LANE_DISCOVERY_LEDGER.md`, which tracks lane candidates but not project delivery status.

Running a weekly pulse without project capsules would generate a report from context soup (reading NEXT_ACTION + assorted folders) rather than from a clean structured source. That is the pattern the masterclass doctrine explicitly forbids.

**Readiness: NOT-READY**

#### Blocked by

1. Project capsules must exist first. Phase 4 acceptance criteria require capsules for all live projects. That gap is not closed.
2. A pulse prompt cannot be finalized until the capsule schema is final (the template at `PROJECT_CAPSULE_TEMPLATE.md` is in the command center, but it has never been applied).
3. No manual pulse run has been attempted.
4. P5 audit found no "pulse check" skill - it must be authored fresh.

#### What must happen before this routine can be planned further

1. Fill `PROJECT_CAPSULE.md` for each live project. Minimum: OS Takeover, Lane Discovery, Alma Love (stills wrap only).
2. Author a `pulse-check` prompt that reads capsules and writes a delta report.
3. Run it manually once. Confirm counts, confirm no stale-project drift detection is a false positive.
4. Run manually a second time after a real project update. Confirm the delta is detected.
5. Then design the weekly schedule and status file.

**Proposed schedule (post-readiness):** Every Sunday 20:00 local. Local routine only (reads local repo files). Not cloud-eligible until project capsules are also written to a cloud-synced path.

---

### Routine C: Book and Docs Refinery Checkpoint

**Purpose:** After a certification wave completes, a checkpoint routine reads the current ledger state, confirms manifest reconciliation, and writes a brief status note. Prevents the "is the refinery done?" question from requiring a full re-read of control files.

#### Does a proven manual workflow or skill exist? (P5 citation)

YES - STRONGLY. This is the closest routine to having two proven manual passes.

Evidence:
- Wave 002-D closed with a full controller/watchdog loop (P1 + P2 compliance): `RUN_STATE.json`, `PROGRESS_LEDGER.csv`, `WATCHDOG.md`, `OS_RECEIPT.md` all present in `00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/`.
- The refinery checkpoint was run manually across waves 002-A through 002-G and the docs/tooling program. Each wave has its own `OS_RECEIPT.md` with counts, gate results, and what-changed log.
- The `MASTER_RESUME.md` + `REFINERY_MASTER_STATE.json` pattern in `OS_REFINERY_AUTONOMY_001/` is the earliest working version of a status-file read/write contract.
- The current NEXT_ACTION.md records "BOOK CANON DONE (2026-06-20)" and "DOCS/TOOLING DONE (2026-06-21)" as clean checkpoints, confirming the manual process has run to completion twice (books + docs separately).

What is NOT proven:
- A checkpoint has never been run as a standalone stateless prompt with a dedicated status file distinct from the wave-control files. The checkpoint has always been embedded inside the wave itself.
- The checkpoint has not been separated into a recurring "check the state of the ledger from outside" routine that any Claude session can call without loading the full wave control context.

**Readiness: READY-TO-PILOT** (with the caveats below)

#### Proposed schedule or loop window

No hard schedule needed now: the refinery is at SCHEDULED=0 and DOCS/TOOLING is reconciled. The trigger is: run after any future certification wave closes (event-driven, not calendar-driven). If a new batch opens in the future (e.g., a new source universe), the checkpoint routine fires when that batch closes.

For the period when no wave is active: run once per month on the first Monday to confirm ledger state has not drifted (no accidental writes, no manifest corruption, counts stable).

**Local-only:** reads local ledger CSV and JSON files. Cloud-eligible in principle, but requires the repo to be pushed and the cloud runner to clone it, which is infrastructure not yet built.

#### Permission boundaries

- READ: `01_KNOWLEDGE_BASE/MASTER_INDEX.md`, `BOOK_CANON_CERTIFICATION_LEDGER.csv`, `DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv`, `OS_CERT_WAVE_*/control/RUN_STATE.json`, `OS_CERT_WAVE_*/OS_RECEIPT.md`, `OS_DOCS_TOOLING_001/RUN_STATE.json`.
- WRITE: one status file (path below). One checkpoint report to command center.
- BLOCKED: no book-status mutation, no manifest write, no master-corpus write, no spend, no post, no delete, no move.

#### Status file path

`00_COMMAND_CENTER/ROUTINES/refinery_checkpoint/STATUS.json`

```json
{
  "last_run": "ISO-8601",
  "last_result": "clean | drift_detected | error",
  "book_canon_scheduled": 0,
  "book_canon_bound": 240,
  "docs_tooling_terminal": 50,
  "manifest_source_count": 1246,
  "checkpoint_state": "CLEAN | DIRTY",
  "drift_flags": [],
  "known_issues": [],
  "what_changed": "...",
  "next_suggested_improvement": "...",
  "what_not_to_repeat": "..."
}
```

#### Where results land

`00_COMMAND_CENTER/ROUTINES/refinery_checkpoint/CHECKPOINT_<YYYY-MM-DD>.md`

Accumulates as a dated log. No auto-delete. After 90 days the operator prunes.

#### Manual proof steps remaining before promotion

1. Author `00_COMMAND_CENTER/ROUTINES/refinery_checkpoint/CHECKPOINT_PROMPT.md`. It must name exactly which CSV and JSON files to read, what counts to verify, what drift means, and what the output format is.
2. Run the checkpoint prompt manually in a fresh session. Confirm it reads the correct counts from the real files on disk (no hallucinated counts). Write the status file and a checkpoint report.
3. Intentionally introduce a small ledger inconsistency in a scratch file (not the real ledger) and confirm the checkpoint prompt detects and flags it.
4. Fix any issues. Run a second clean pass.
5. Two clean passes = eligible for promotion. Do not promote until both passes are receipted.

---

### Routine D: Stale-Tool Verification Reminder

**Purpose:** Every 30 days, check the `OS_TOOL_APP_INTEGRATION_LEDGER.csv` (Phase 6 deliverable) for tools whose `last_verified` date is more than 30 days old. Surface a list for operator review. Does NOT re-run the verification itself - that requires judgment and sometimes spend. This is a reminder, not a verifier.

#### Does a proven manual workflow or skill exist? (P5 citation)

NO. The Phase 6 tool ledger (`OS_TOOL_APP_INTEGRATION_LEDGER.csv`) was produced as the P6 deliverable. The ledger exists (as a CSV in the P6 work product). However:

- No "stale tool scan" prompt or skill has ever been run.
- The Phase 6 tool ledger was produced once, by hand, as an audit artifact. It has never been read back by a routine.
- P5 found no "tool verification" skill. The closest entry in the skill list is `os-quality-gates`, which covers task-output QA, not tool-state checking.
- The `OS_TOOL_UNDERUSE_LEDGER.csv` and `OS_GEMINI_CLI_INTEGRATION_AUDIT.md` are related reference files but are not structured for a stateless checkpoint read.

**Readiness: NEEDS-MANUAL-PROOF-FIRST**

#### Blocked by

1. The ledger must be at a stable path that the routine can always find. If P6 produced it as part of its work output, confirm the canonical path and move it to the ROUTINES folder or a stable command-center location.
2. A "stale scan" prompt must be authored. It needs to: read the ledger CSV, parse `last_verified` dates, compute staleness from today's date, surface tools over threshold, write the reminder to the status file and a dated reminder note.
3. No manual run has been done.

#### Proposed schedule or loop window (post-readiness)

Monthly on the first Monday. Local routine (reads local CSV). The reminder report itself does not trigger any action - it surfaces a list for operator judgment. The operator then decides whether to manually re-verify a tool in a new session.

#### Permission boundaries

- READ: `OS_TOOL_APP_INTEGRATION_LEDGER.csv` (P6 canonical path to be confirmed), system date.
- WRITE: one status file, one dated reminder report.
- BLOCKED: no tool re-verification (that requires judgment + possibly spend), no spend, no authentication actions, no MCP tool calls, no delete/move.

#### Status file path

`00_COMMAND_CENTER/ROUTINES/stale_tool_reminder/STATUS.json`

```json
{
  "last_run": "ISO-8601",
  "last_result": "clean | stale_tools_found | error",
  "tools_over_30d": [],
  "tools_over_60d": [],
  "known_issues": [],
  "what_changed": "...",
  "next_suggested_improvement": "...",
  "what_not_to_repeat": "..."
}
```

#### Where results land

`00_COMMAND_CENTER/ROUTINES/stale_tool_reminder/REMINDER_<YYYY-MM-DD>.md`

#### Manual proof steps remaining before promotion

1. Confirm the canonical stable path for `OS_TOOL_APP_INTEGRATION_LEDGER.csv`.
2. Author `STALE_TOOL_SCAN_PROMPT.md` that reads the CSV and computes staleness.
3. Run manually once in a fresh session. Confirm date arithmetic is correct. Confirm no permission-prompt blockers.
4. Run a second time after manually editing one `last_verified` cell to a date 35 days ago. Confirm the tool appears in the stale list.
5. Two clean passes = eligible for promotion.

---

### Routine E: Source-Retirement Review Reminder

**Purpose:** Every 90 days, flag any source in `BOOK_CANON_CERTIFICATION_LEDGER.csv` with status `DUPLICATE_OR_SUPERSEDED` or `EXCEPTION` that has been sitting for more than 90 days without an operator ratification note. Also flags any source in the docs/tooling ledger with `EXCEPTION` status whose reason references a spend gate (e.g., the 6 photography videos blocked by the Whisper key). Surfaces these for operator decision: ratify permanently, upgrade (install the tool), or prune.

#### Does a proven manual workflow or skill exist? (P5 citation)

PARTIAL. The source-retirement discipline is proven as a MANUAL PROCESS:
- The 2 duplicate book entries in 002-D were dispositioned with rationale and recorded in `control/close_dispositions.json`.
- The 6 EXCEPTION videos in the docs/tooling ledger were operator-ratified explicitly in the OS_RECEIPT.
- The OS_RECEIPT file format already contains a "what blocks the exception from resolving" field.

What is NOT proven:
- A recurring scan of BOTH ledgers from outside has never been run as a stateless prompt.
- No "retirement review" prompt or skill exists.
- The scan has always been embedded inside the wave that produced the exception, not as a separate recurring check.

**Readiness: NEEDS-MANUAL-PROOF-FIRST**

#### Proposed schedule or loop window (post-readiness)

Quarterly (every 90 days). Local routine (reads local CSVs). Not time-sensitive; can shift to the nearest Monday if the 90-day mark falls mid-week. Not cloud-eligible in the current infrastructure.

#### Permission boundaries

- READ: `BOOK_CANON_CERTIFICATION_LEDGER.csv`, `DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv`, system date.
- WRITE: one status file, one dated review report.
- BLOCKED: no book status mutation, no ledger write, no spend, no delete/move/archive. The routine surfaces a list; the operator acts in a separate session.

#### Status file path

`00_COMMAND_CENTER/ROUTINES/source_retirement_review/STATUS.json`

```json
{
  "last_run": "ISO-8601",
  "last_result": "clean | items_flagged | error",
  "flagged_books": [],
  "flagged_docs": [],
  "known_issues": [],
  "what_changed": "...",
  "next_suggested_improvement": "...",
  "what_not_to_repeat": "..."
}
```

#### Where results land

`00_COMMAND_CENTER/ROUTINES/source_retirement_review/REVIEW_<YYYY-MM-DD>.md`

#### Manual proof steps remaining before promotion

1. Author the scan prompt: read both ledgers, filter by status + age, surface flagged items with their `exception_reason` and `last_verified` fields.
2. Run manually in a fresh session against the real ledgers. Confirm the 6 EXCEPTION docs/tooling videos appear as flagged (they should, as they are blocked by the Whisper key and are now ~30 days since the program closed).
3. Fix any parse errors. Run a second clean pass.
4. After two clean passes, schedule at 90-day interval.

---

## Cloud vs. Local Classification

| Routine | Local or Cloud | Reason |
|---|---|---|
| A - Morning Cockpit | LOCAL ONLY | Reads local repo files; no hosted MCP, no local-MCP dependency; local scheduled task or session-start trigger |
| B - Weekly Project Pulse | LOCAL ONLY (until capsules exist) | Reads local project capsules; not cloud-eligible until repo is pushed and cloud runner can clone |
| C - Refinery Checkpoint | LOCAL PREFERRED | Reads local ledger CSV/JSON; could become cloud-eligible if repo is pushed and a hosted connector clones the repo + runs Bash; not yet built |
| D - Stale Tool Reminder | LOCAL ONLY | Reads local CSV; tool re-verification often requires local MCP connections; reminder-only, no execution |
| E - Source Retirement Review | LOCAL ONLY | Reads local CSVs; no cloud path needed for a quarterly read-and-flag routine |

Note: none of these five routines use Premiere Pro, After Effects, Blender, ElevenLabs, or Higgsfield MCP. Those tools are local-only and cannot be called from a cloud routine. If a future production routine needs those tools, it must be a local routine or use a hosted connector (not yet available on this OS).

---

## Routines Closest to Ready

### Rank 1: Routine C - Refinery Checkpoint

**Why it is closest:** The underlying workflow has run successfully multiple times under real conditions (waves 002-A through 002-G plus docs/tooling). The controller/watchdog/receipt pattern is proven. The status-file read/write contract exists in `REFINERY_MASTER_STATE.json`. The only gap is that the checkpoint has never been run as a STANDALONE STATELESS PROMPT separated from the wave context. That is a small separation step, not a build-from-scratch step.

**Exact manual proof steps remaining:**

1. Create `00_COMMAND_CENTER/ROUTINES/refinery_checkpoint/` directory.
2. Write `CHECKPOINT_PROMPT.md` - a self-contained prompt that reads the real ledger files and produces the status JSON + markdown report. The prompt must not require any context from the wave that produced the ledger. It must work from cold start.
3. Run once in a fresh Claude Code session with `/clear` first. Read the status file. Confirm counts match the real ledger (books BOUND=240, SCHEDULED=0, docs TERMINAL=50).
4. Write the result to `CHECKPOINT_2026-06-21.md`.
5. Run a second time in a different session. Confirm the status file is overwritten (not appended). Confirm the report matches.
6. After both receipts, the routine is eligible for promotion to a monthly local scheduled task.

Estimated effort: 1-2 hours across 2 sessions.

### Rank 2: Routine A - Morning Cockpit

**Why it is second closest:** The `sniped-monday-cockpit` skill exists and fires correctly. The OS_MORNING_REPORT_2026-06-04.md shows the output format works for the operator. The scope question (SNIPED lane cockpit vs. OS Takeover cockpit) is the only blocking decision.

**Exact manual proof steps remaining:**

1. Operator decides scope: is the morning cockpit for the SNIPED operating lane (weekly outcomes, cadence), the OS Takeover mission state (wave status, phase tracking), or a combined two-section report? This is a routing decision only the operator can make.
2. Once scope is decided, author `COCKPIT_PROMPT.md` with exact file reads and output format.
3. Run manually once in a fresh session. Read the output. Note any file-not-found errors or context-soup issues.
4. Fix. Run a second clean pass.
5. After two receipts, the cockpit is eligible for a local scheduled task or session-start trigger.

Estimated effort: 1-3 hours across 2 sessions (blocked on operator's scope decision first).

---

## Required Infrastructure Before Any Routine Goes Live

1. `00_COMMAND_CENTER/ROUTINES/` directory - does not yet exist on disk. Create it with one subfolder per routine when manual proof begins.
2. Each routine subfolder needs: `PROMPT.md`, `STATUS.json` (initialized), a `receipts/` folder for dated reports.
3. `.claude/settings.json` allowlist must include the read paths each routine uses. Confirm with `/fewer-permission-prompts` after the first manual run to catch any prompts that block the run.
4. The `os_cost_guard` hook (currently enforcing SEQUENTIAL workflows for the refinery) must not interfere with routine reads. Refinery checkpoint is READ-ONLY so it should be outside the guard scope. Confirm before promoting.

---

## What This Plan Does NOT Do

- This is a PLAN, not a live creation. No cron job, no routine, no Claude scheduled task has been created.
- No status files have been written to disk (the `ROUTINES/` directory does not exist yet).
- No workflow has been promoted.
- The governing law stands: promotion happens only after two clean manual passes, with a receipt for each.

---

## Acceptance Criteria (Phase 7 complete when ALL are met)

- [ ] Each routine has a `ROUTINES/<name>/` subfolder with `PROMPT.md`, `STATUS.json` (initialized), and a `receipts/` folder.
- [ ] Each promoted routine has at least 2 manual-run receipts in its `receipts/` folder.
- [ ] No routine's first prompt is run in a session that already has project context loaded (must start fresh).
- [ ] Status file is confirmed overwritten (not appended) after the second manual run.
- [ ] Destructive actions confirmed blocked (attempt a delete inside the prompt, confirm refusal).
- [ ] Local-only routines are labeled `LOCAL ONLY` in their `PROMPT.md` frontmatter.
- [ ] All spend-capable tools (Higgsfield, ElevenLabs) are confirmed absent from all five routine prompts.
- [ ] The refinery checkpoint routine's counts match the real ledger on first run (no hallucinated numbers).
- [ ] Operator has approved the cockpit scope decision before Routine A is drafted.
