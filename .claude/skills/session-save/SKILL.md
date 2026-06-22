---
name: session-save
description: Snapshot current session state to 00_COMMAND_CENTER/session_saves/ before /clear, before context approaches the 70% limit, or before closing the terminal.
disable-model-invocation: false
---

Write a session-state snapshot. Markdown only. No disk-state changes elsewhere.

1. Target path: `00_COMMAND_CENTER/session_saves/<YYYY-MM-DD>_<HHMM>_<short-slug>.md`. Generate the timestamp from `date +%Y-%m-%d_%H%M`. Slug is a 2-4 word kebab-case description of the session's work.

2. Capture these sections:
   - **Session intent** · what was the operator's brief for this session?
   - **Files touched** · list every file created or modified this session, grouped by directory.
   - **Decisions made** · numbered list. Especially routing decisions, scope locks, and any chapter-slot collision resolutions.
   - **Open questions** · anything the operator paused on without a final answer.
   - **In-flight tasks** · TaskList state · which tasks are completed, in_progress, pending.
   - **Next recommended action** · one paragraph. Be specific. Include the exact command or skill invocation that the next session should start with.
   - **Drift flags** · anything that violated or risked violating the AGENTS.md drift-prevention rules.

3. After writing, print the file path and a one-line summary. Do not `/clear` automatically · the operator triggers `/clear` after reviewing the save.

This skill is read-only against the corpus. It only writes the single snapshot file under `session_saves/`. Never modify master files, raw/, or 01_KNOWLEDGE_BASE/ contents during a save.


## INVOKE WHEN
- Before /clear or closing the terminal mid-session
- Context approaches the 70% limit
- "save where we are" / "snapshot this session" / "save session before we switch tasks"

## Inputs
- Current session work: operator's brief, all files touched, decisions made (derived from conversation context, required)
- TaskList state if tasks were created or updated this session
- Any open questions, unresolved routing decisions, or drift flags to surface

## Outputs
- Single snapshot markdown file at 00_COMMAND_CENTER/session_saves/<YYYY-MM-DD>_<HHMM>_<short-slug>.md with 7 sections: Session intent, Files touched (grouped by directory), Decisions made (numbered), Open questions, In-flight tasks, Next recommended action, Drift flags
- Printed file path and one-line summary of the session
- One-line receipt: e.g. '00_COMMAND_CENTER/session_saves/2026-06-20_1430_batch005-photo-staging.md written; next action: /staging-plan after operator authorizes the copy pass'

## Gates
- Read-only against the corpus: skill writes ONLY the single snapshot file under session_saves/; never touches master files, raw/, or 01_KNOWLEDGE_BASE/
- Timestamp gate: generate from `date +%Y-%m-%d_%H%M` at invocation time; never hardcode or estimate
- Slug gate: 2-4 word kebab-case slug must describe the session's actual work, not a generic label
- Drift flags required: surface any actions that violated or risked AGENTS.md drift-prevention rules; do not omit
- No auto-clear: print path and summary then stop; operator triggers /clear after reviewing

## Test
- case: At 68% context, operator has been staging BATCH_005: reviewed source inventory, made a routing decision (AI_IMAGE_TOOLS doc to slot 10_REFERENCE), left one chapter-slot collision unresolved. Expected: 00_COMMAND_CENTER/session_saves/2026-06-20_1412_batch005-staging-plan.md with all 7 sections, drift flag for unresolved collision, next action citing exact /staging-plan invocation. No files outside session_saves/ touched.
- expected failure: Invoked immediately after /clear on a blank session with no work done. Skill produces the snapshot but notes in Open questions: 'Session was blank; snapshot may be empty. Verify this is the intended save point before /clear.'
