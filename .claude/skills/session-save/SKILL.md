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
