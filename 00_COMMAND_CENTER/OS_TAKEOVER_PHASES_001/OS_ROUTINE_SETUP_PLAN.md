> **Retired 2026-06-28.** One or more OS_* systems referenced in this document were retired during the OS repository convergence and moved to `_HISTORY/` or `_ARCHIVE/`. Those references are historical and no longer active. See `CONVERGENCE_PLAN_2026-06-28.md`.

# OS_ROUTINE_SETUP_PLAN.md - Full Content

Here is the complete markdown, also written to disk at the path above.

---

## Governing Rules

Five permanent laws that sit above every candidate:

1. Scheduled tasks are stateless. Read status file before work, overwrite it after. Loops die with the session; scheduled tasks must survive restarts.
2. Local-only MCP tools (Premiere Pro, After Effects, Blender, ElevenLabs, Higgsfield) cannot run inside any cloud routine. Cloud routines would need a hosted connector, which does not exist yet.
3. Cloud routine secrets go in the host's Environment Variables panel, never `.env`.
4. Spend, post, publish, delete, and move are hard-blocked inside every routine. Approval lives at the boundary between routines, not mid-run.
5. Promotion requires two clean manual passes with a receipt from each. That law does not bend for any candidate.

---

## The Five Candidates, Evaluated

### Routine A: Morning Cockpit

**Proven manual workflow or skill:** PARTIAL. `sniped-monday-cockpit` skill exists at `.claude/skills/sniped-monday-cockpit/SKILL.md`. It fires on "Plan my week / Monday morning / what should I focus on" and reads from `~/Downloads/    SNIPED_OS/00_BRIEF/`. However, the current live mission state lives in `00_COMMAND_CENTER/NEXT_ACTION.md`, `OS_CURRENT_STATE.md`, and `ACTIVE_KNOWLEDGE_STATE.md` inside this repo. The two context layers are not joined. No standalone stateless morning-cockpit prompt with a status-file contract has ever been run. The one existing `OS_MORNING_REPORT_2026-06-04.md` was written ad hoc inside a long chat, not as a structured routine.

**Readiness:** NEEDS-MANUAL-PROOF-FIRST

**Schedule:** Local only. Trigger is session start when status file is more than 18 hours old (calendar cron is secondary). Not cloud-eligible (reads local repo files, not hosted).

**Permission boundaries:**
- READ: `NEXT_ACTION.md`, `OS_CURRENT_STATE.md`, `ACTIVE_KNOWLEDGE_STATE.md`, `LANE_DISCOVERY_LEDGER.md`, `OS_TAKEOVER_UPGRADE_PLAN.md` receipts, `OS_CERT_WAVE_*/control/RUN_STATE.json`.
- WRITE: status file + one dated report.
- BLOCKED: spend, post, publish, delete, move, archive, book-status mutation, master-corpus write.

**Status file path:** `00_COMMAND_CENTER/ROUTINES/morning_cockpit/STATUS.json`

**Where results land:** `00_COMMAND_CENTER/ROUTINES/morning_cockpit/MORNING_REPORT_<YYYY-MM-DD>.md`

**Manual proof steps remaining:**
1. Operator decides scope: SNIPED lane cockpit (weekly 3 outcomes + cadence), OS Takeover cockpit (wave status + phase tracking), or a two-section combined report. This routing decision blocks drafting.
2. Author `COCKPIT_PROMPT.md` naming exact file reads, output format, and status-file contract.
3. Run in a fresh session (`/clear` first). Confirm zero permission prompts, correct file reads, correct output.
4. Fix any errors. Run a second time in a different fresh session. Confirm status file is overwritten (not appended). Confirm report lands at the correct path.
5. Two clean receipts = eligible for promotion.

---

### Routine B: Weekly Active-Project Pulse

**Proven manual workflow or skill:** NO. Phase 4 audit confirmed that no live project folder contains a filled `PROJECT_CAPSULE.md`. The template exists but has never been applied. There is nothing to pulse-check yet. Running a pulse without capsules would produce a context-soup read of NEXT_ACTION plus assorted folders, which is the pattern the masterclass doctrine explicitly forbids.

**Readiness:** NOT-READY

**Blocked by:**
1. `PROJECT_CAPSULE.md` must exist for each live project first. Phase 4 gap is not closed.
2. No pulse-check prompt or skill exists. It must be authored from scratch after capsules exist.
3. Zero manual runs.

**Proposed schedule (post-readiness):** Sunday 20:00 local. Local only. Not cloud-eligible until project capsules are in a cloud-synced path.

**Status file path:** `00_COMMAND_CENTER/ROUTINES/weekly_pulse/STATUS.json`

**Where results land:** `00_COMMAND_CENTER/ROUTINES/weekly_pulse/PULSE_<YYYY-MM-DD>.md`

**Manual proof steps remaining:**
1. Fill `PROJECT_CAPSULE.md` for each live project (minimum: OS Takeover, Lane Discovery, Alma Love stills wrap). This is Phase 4 work, not Phase 7 work.
2. Author a `pulse-check` prompt that reads capsules and produces a delta report.
3. Run manually once. Fix errors. Run a second time after a real project update. Confirm delta is detected.
4. Two clean passes = eligible for promotion.

---

### Routine C: Book and Docs Refinery Checkpoint

**Proven manual workflow or skill:** YES. This is the strongest candidate. The controller/watchdog/receipt pattern ran successfully across waves 002-A through 002-G and the docs/tooling program. `RUN_STATE.json`, `PROGRESS_LEDGER.csv`, `WATCHDOG.md`, and `OS_RECEIPT.md` are present in `OS_CERT_WAVE_002D/control/`. The refinery checkpoint has run under real conditions, survived a laptop crash with zero data loss, and produced 2 separate closure receipts (books: SCHEDULED=0 as of 2026-06-20; docs/tooling: 50/50 terminal as of 2026-06-21). The `MASTER_RESUME.md` + `REFINERY_MASTER_STATE.json` pattern is the earliest working status-file read/write contract in this OS. What has NEVER been done: run the checkpoint as a standalone stateless prompt from outside the wave context. That gap is a separation step, not a rebuild.

**Readiness:** READY-TO-PILOT

**Schedule:** Event-driven (fires when a new wave closes). When no wave is active: first Monday of each month to confirm ledger drift = 0. Local preferred. Cloud-eligible in principle but requires repo push + clone, not yet built.

**Permission boundaries:**
- READ: `BOOK_CANON_CERTIFICATION_LEDGER.csv`, `DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv`, `OS_CERT_WAVE_*/control/RUN_STATE.json`, `OS_CERT_WAVE_*/OS_RECEIPT.md`, `OS_DOCS_TOOLING_001/RUN_STATE.json`, `01_KNOWLEDGE_BASE/MASTER_INDEX.md`.
- WRITE: status file + one dated checkpoint report.
- BLOCKED: book-status mutation, manifest write, master-corpus write, spend, post, delete, move.

**Status file path:** `00_COMMAND_CENTER/ROUTINES/refinery_checkpoint/STATUS.json`

Fields: `last_run`, `last_result`, `book_canon_scheduled`, `book_canon_bound`, `docs_tooling_terminal`, `manifest_source_count`, `checkpoint_state` (CLEAN or DIRTY), `drift_flags`, `known_issues`, `what_changed`, `next_suggested_improvement`, `what_not_to_repeat`.

**Where results land:** `00_COMMAND_CENTER/ROUTINES/refinery_checkpoint/CHECKPOINT_<YYYY-MM-DD>.md`

**Manual proof steps remaining:**
1. Create `00_COMMAND_CENTER/ROUTINES/refinery_checkpoint/` directory.
2. Write `CHECKPOINT_PROMPT.md`: a self-contained prompt that reads the real ledger files and produces the status JSON + markdown report. Must work from a cold start without any wave context loaded.
3. Run once in a fresh session (`/clear` first). Confirm counts match real ledger: BOUND=240, SCHEDULED=0, docs TERMINAL=50, manifest source=1,246. Confirm status file written at the correct path.
4. Run a second time in a different session. Confirm status file is OVERWRITTEN (not appended). Confirm report lands. Confirm counts are still consistent.
5. Two clean receipts = eligible for promotion to monthly local scheduled task.

---

### Routine D: Stale-Tool Verification Reminder

**Proven manual workflow or skill:** NO. The Phase 6 tool ledger (`OS_TOOL_APP_INTEGRATION_LEDGER.csv`) was produced once as an audit artifact. No scan prompt or skill exists that reads it back. P5 found no "tool verification" skill in the 83-skill inventory. No manual run has been done.

**Readiness:** NEEDS-MANUAL-PROOF-FIRST

**Blocked by:**
1. Confirm the canonical stable path for the P6 CSV (it must be at a predictable path, not buried in a work subfolder).
2. Author the scan prompt: read the CSV, compute staleness from today's date, surface tools where `last_verified` is more than 30 days old.
3. Zero manual runs.

**Note:** This routine does NOT re-verify tools itself. It produces a reminder list for operator judgment. Any actual re-verification happens in a separate session with operator approval.

**Proposed schedule (post-readiness):** First Monday of each month. Local only (reads local CSV). The reminder report triggers no action; the operator decides in a separate session whether to re-verify.

**Status file path:** `00_COMMAND_CENTER/ROUTINES/stale_tool_reminder/STATUS.json`

Fields: `last_run`, `last_result`, `tools_over_30d`, `tools_over_60d`, `known_issues`, `what_changed`, `next_suggested_improvement`, `what_not_to_repeat`.

**Where results land:** `00_COMMAND_CENTER/ROUTINES/stale_tool_reminder/REMINDER_<YYYY-MM-DD>.md`

**Manual proof steps remaining:**
1. Confirm and document the canonical path for `OS_TOOL_APP_INTEGRATION_LEDGER.csv`.
2. Author `STALE_TOOL_SCAN_PROMPT.md` with date arithmetic and CSV parsing.
3. Run once. Confirm date math. Confirm zero permission prompts.
4. Manually edit one `last_verified` cell to a date 35 days ago in a scratch copy. Confirm the tool appears in the stale list.
5. Restore the real CSV. Run a clean second pass on the real file.
6. Two clean receipts = eligible for promotion.

---

### Routine E: Source-Retirement Review Reminder

**Proven manual workflow or skill:** PARTIAL. The retirement disposition process is proven manually: the 2 duplicate books in 002-D were dispositioned in `control/close_dispositions.json`, and the 6 EXCEPTION videos in the docs/tooling program were operator-ratified in that program's OS_RECEIPT. However, no recurring scan of BOTH ledgers from outside has ever been run as a standalone stateless prompt. The scan has always been embedded inside the wave that produced the exceptions.

**Readiness:** NEEDS-MANUAL-PROOF-FIRST

**Proposed schedule (post-readiness):** Quarterly (every 90 days), first Monday of the quarter. Local only. Not time-sensitive; can shift to the nearest Monday.

**Permission boundaries:**
- READ: `BOOK_CANON_CERTIFICATION_LEDGER.csv`, `DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv`, system date.
- WRITE: status file + one dated review report.
- BLOCKED: no book-status mutation, no ledger write, no spend, no delete/move/archive. Surfaces a list; operator acts in a separate session.

**Status file path:** `00_COMMAND_CENTER/ROUTINES/source_retirement_review/STATUS.json`

Fields: `last_run`, `last_result`, `flagged_books`, `flagged_docs`, `known_issues`, `what_changed`, `next_suggested_improvement`, `what_not_to_repeat`.

**Where results land:** `00_COMMAND_CENTER/ROUTINES/source_retirement_review/REVIEW_<YYYY-MM-DD>.md`

**Manual proof steps remaining:**
1. Author the scan prompt: read both CSVs, filter by `DUPLICATE_OR_SUPERSEDED` or `EXCEPTION` status older than 90 days without an operator-ratification note, surface with their `exception_reason`.
2. Run manually. Confirm the 6 EXCEPTION docs/tooling videos appear (blocked by Whisper key, ~30 days since program closed - not yet 90 days, so they may not flag yet; note this and confirm the logic is correct for the age threshold).
3. Adjust threshold if needed. Run a second clean pass.
4. Two clean receipts = eligible for promotion.

---

## Cloud vs. Local Classification Summary

| Routine | Classification | Reason |
|---|---|---|
| A - Morning Cockpit | LOCAL ONLY | Reads local repo files; session-start trigger preferred over calendar cron |
| B - Weekly Project Pulse | LOCAL ONLY | Reads local project capsules; not cloud-eligible until repo push + cloud runner built |
| C - Refinery Checkpoint | LOCAL PREFERRED | Reads local CSV/JSON; cloud-eligible in principle but requires repo push + clone, not yet built |
| D - Stale Tool Reminder | LOCAL ONLY | Reads local CSV; tool re-verification requires local MCP connections |
| E - Source Retirement Review | LOCAL ONLY | Reads local CSVs; quarterly read-and-flag needs no cloud path |

None of these five routines use Premiere Pro, After Effects, Blender, ElevenLabs, or Higgsfield MCP. If a future production routine needs those tools, it must be a local routine or use a hosted connector not yet available.

---

## Required Infrastructure Before Any Routine Goes Live

1. `00_COMMAND_CENTER/ROUTINES/` directory does not yet exist on disk. Create it before drafting any prompt.
2. Each routine subfolder needs: `PROMPT.md`, `STATUS.json` (initialized with zeroed fields), and a `receipts/` folder for dated reports.
3. `.claude/settings.json` allowlist must include the read paths each routine uses. Run `/fewer-permission-prompts` after the first manual run to catch any blockers.
4. The `os_cost_guard` hook (enforcing SEQUENTIAL workflows for the refinery) must not interfere with routine reads. Refinery checkpoint is READ-ONLY so it should be outside the guard scope. Confirm before promoting.

---

## The Two Routines Closest to Ready + Exact Next Steps

**Rank 1: Routine C (Refinery Checkpoint).** Underlying process has run 7+ times under real conditions with receipts. Gap is only the separation into a standalone stateless prompt. Estimated effort: 1-2 hours across 2 sessions.

Exact next steps:
1. Create `00_COMMAND_CENTER/ROUTINES/refinery_checkpoint/` on disk.
2. Write `CHECKPOINT_PROMPT.md` (cold-start, no wave context loaded).
3. Run in a fresh session. Verify BOUND=240, SCHEDULED=0, docs=50, manifest=1,246. Write receipt.
4. Run second pass in a different session. Confirm overwrite. Write second receipt.
5. Promote.

**Rank 2: Routine A (Morning Cockpit).** Existing skill and a prior morning report show the format works. Single blocking decision is operator scope choice (SNIPED lane vs. OS Takeover vs. combined). Estimated effort: 1-3 hours across 2 sessions, after scope decision.

Exact next steps:
1. Operator decides: cockpit scope = SNIPED lane, OS Takeover, or combined two-section report.
2. Author `COCKPIT_PROMPT.md` with that scope.
3. Run in fresh session. Fix errors. Run second pass.
4. Two receipts = promote.

---

## Phase 7 Acceptance Criteria (all must be met before phase is complete)

- Each routine has a `ROUTINES/<name>/` subfolder with `PROMPT.md`, initialized `STATUS.json`, and a `receipts/` folder.
- Each promoted routine has at least 2 dated receipts in its `receipts/` folder.
- No routine's first prompt runs in a session that already has project context loaded.
- Status file is confirmed overwritten (not appended) after the second manual run.
- Destructive actions confirmed blocked inside every routine prompt.
- Local-only routines are labeled `LOCAL ONLY` in their `PROMPT.md` frontmatter.
- All spend-capable tools (Higgsfield, ElevenLabs) are absent from all five routine prompts.
- Refinery checkpoint counts match the real ledger on first run (no hallucinated numbers).
- Operator has approved the cockpit scope decision before Routine A is drafted.

---
## ADVERSARIAL-VERIFY NOTES (verdict PASS, grounded=true)
- The `00_COMMAND_CENTER/ROUTINES/` directory and the per-routine `STATUS.json` paths are PROPOSED, not yet created (this is a plan, correct per Phase 7). They are created only when a routine is promoted after passing its workflow manually twice.
- Full paths for resume: OS_TAKEOVER_UPGRADE_PLAN.md is at `00_COMMAND_CENTER/CLAUDE_OVERLOAD_MASTERCLASS_001/`; the docs ledger is `00_COMMAND_CENTER/OS_DOCS_TOOLING_001/DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv`.
