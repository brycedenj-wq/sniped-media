# OS ACTIVATION SPINE (LOCKED 2026-06-08)

**The bridge that makes the whole OS body fire as one unit on every task.** Built to end the loop of weak output caused by a stacked OS whose skills/docs/books sat unused because nothing assembled them for the task at hand.

## The problem it solves
The OS had the knowledge (the Higgsfield film stack, face-lock, world-bible, vision-reject, finishing standard) but no mechanism forced it to activate together for a given job. The every-turn hook only printed a generic gate reminder and told the model to "classify via os-command-router" as a manual step that got skipped under momentum. Result: more stacked than anyone, but not a machine.

## How it works (the chain)
RESOURCE -> RULE -> SHOT/TASK DECISION -> TOOL EXECUTION -> QA, enforced by 4 mechanical parts:

1. **The index — `OS_ACTIVATION_INDEX.json`** (the body, tagged). One file mapping each domain (film, image_design, photo, writing, strategy, research, build_automation) to its triggers, authority doc, required skills, docs, gates, tools, production loop, hard laws, and known gaps. This is the body declared as data.

2. **The router — `scripts/os_activate.py`** (task -> activation set). Classifies any task string by trigger match and prints the exact set to activate. Run manually any time: `os_activate.py "make a brand film"`. Reused by the hook in `--hook` mode (reads the prompt as JSON on stdin).

3. **The every-turn hook — `scripts/os_gate_injector.py`** (UserPromptSubmit). Now reads the actual prompt, classifies it, and injects the specific activation manifest into context BEFORE the model answers. Falls back to the static gate map if no domain matches. This is what makes the body fire automatically, scoped to the task, every turn. Exit 0 always (cannot break the harness).

4. **The maintainer — `scripts/os_index_audit.py`** (keeps it complete). Scans every skill + standards doc on disk and reports what is NOT yet wired into the index, so the body stays "ready for anything" as books/docs/skills are added instead of drifting back into unused piles. Run it after adding resources.

## Honest limits (what it does and does not do)
- It DOES: name the exact skills/docs/gates for the task every turn, so "I did not know to pull it" can no longer happen. It removes the failure that produced the weak Synergy/Alma work.
- It does NOT: physically force the model to read every named doc or run every gate. Compliance is still required. The Stop hook (`os_stop_check.py`) backstops by warning on state contradictions; production completion enforcement is the next hardening step.
- Coverage is partial by design: as of build, 33 of 76 skills are wired (the production-relevant ones). Off-domain OS-maintenance skills (jsonl-validation, session-save, etc.) are intentionally not in production domains. Run the audit to extend coverage deliberately.

## Maintenance loop (do this when you add resources)
1. Drop the new skill/doc/book in.
2. `python3 00_COMMAND_CENTER/scripts/os_index_audit.py` -> see what is unregistered.
3. Add it to the right domain in `OS_ACTIVATION_INDEX.json` (or consciously skip it).
4. `os_activate.py "<a task that should use it>"` to confirm it now fires.

## Authority
Composes under `REAL_FILM_PRODUCTION_OS.md` (master film authority). The activation spine is the delivery mechanism for ALL domains. Memory `[[os-activation-spine]]` carries it.
