# CLAUDE CODE OPERATING LAYER · plan · 2026-05-18

Plan to add a project-level agent operating layer for `~/AI-Brain-Refinery/`. Captures the SOPs that have emerged across the BATCH_001-004 work + the staging plan + the inventory pass + the future-source notes, into files that future agent sessions (Claude Code, Codex, Cursor, Gemini CLI, etc.) load automatically.

**Constraints respected up front:** No CLAUDE.md created or updated yet. No AGENTS.md created. No `.claude/skills/` directory created. No chunking. No master file updates. No BATCH_005 start. This document is a plan only. Authorization is required before any of these files land on disk.

Inputs read:
- Project root structure: `~/AI-Brain-Refinery/` (no project-level CLAUDE.md, AGENTS.md, or `.claude/`)
- Global file: `~/.claude/CLAUDE.md` (em-dash ban, memory system rules · auto-loaded every session)
- `00_COMMAND_CENTER/ACTIVE_KNOWLEDGE_STATE.md`
- `00_COMMAND_CENTER/SNIPED_OS_STAGING_PLAN_2026-05-18.md`
- `00_COMMAND_CENTER/SNIPED_OS_FULL_SOURCE_INVENTORY_2026-05-18.md`
- `00_COMMAND_CENTER/future_sources/FASTLANE_CONTENT_REWARDS_INTELLIGENCE_2026-05-18.md`
- `scripts/` (10 Python + shell files for extraction, dedupe, inventory, chunk writes)
- `01_KNOWLEDGE_BASE/batches/BATCH_004_CHUNKS.jsonl` (schema confirmed)
- Reference material: Claude Code best practices + AGENTS.md guidance pasted by operator.

---

## 0 · Current state and gap

| Layer | Status | Loaded by |
|---|---|---|
| `~/.claude/CLAUDE.md` (global) | EXISTS · em-dash ban, memory rules, never-edit-git-config defaults | Every Claude Code session anywhere on this machine |
| `~/AI-Brain-Refinery/CLAUDE.md` (project) | MISSING | (would load when CWD is the project) |
| `~/AI-Brain-Refinery/AGENTS.md` (project, portable) | MISSING | (would load in Codex, Cursor, Gemini CLI, Aider, JetBrains Junie, etc.) |
| `~/AI-Brain-Refinery/.claude/skills/` | MISSING | (would let agents invoke named workflows via `/skill-name`) |
| `~/AI-Brain-Refinery/.claude/settings.json` (hooks, permissions) | MISSING | (would auto-permit safe commands, deterministic post-edit hooks) |
| Auto-loaded memory at `~/.claude/projects/-Users-sniper/memory/MEMORY.md` | EXISTS · 40+ SNIPED feedback/intel/project memories | Every Claude Code session (per the global CLAUDE.md memory system) |

**Gap:** The SOPs encoded in the 4 batch runs + the inventory + staging + future-source flow currently live only in the auto-memory and the operator's head. Every new chat or alternative-agent session has to re-discover:
- Which folder is the source universe right now (it has changed twice in 24 hours)
- What `raw/` means vs `01_KNOWLEDGE_BASE/batches/` vs `outputs/`
- What the JSONL schema is and which `batch` field name is canonical
- What the verification ritual is before chunks become canonical
- Which batch is currently next and why (BATCH_005 photography canon)
- What NOT to touch (master files, Downloads globally, etc.)

A project-level operating layer closes the gap.

---

## 1 · CLAUDE.md vs AGENTS.md · recommendation

**Recommendation: BOTH, with a single source of truth.**

Strategy:
- **`AGENTS.md`** is the canonical, portable, agent-agnostic spec. Short, declarative, no Claude-specific syntax. Compatible with Codex, Cursor, Gemini CLI, Aider, JetBrains Junie, OpenAI Codex CLI, and the rest of the AGENTS.md ecosystem (60K+ projects).
- **`CLAUDE.md`** is a thin Claude-Code-specific file that:
  1. Imports AGENTS.md with `@AGENTS.md` (Claude Code supports `@path` imports).
  2. Adds Claude-specific bits that AGENTS.md doesn't need: skill locations, hook references, slash-command intent, `/clear` rules.

This pattern keeps one source of truth (AGENTS.md) and avoids drift between the two files.

Reasoning:
1. **Portability matters.** The operator has used Claude Code as the primary agent so far, but the AGENTS.md docs show this becoming a portable contract. Future agent sessions (a Codex run, a Cursor session, a Gemini CLI batch) should all share the same project spec.
2. **AGENTS.md is the simplest format.** Standard markdown. No special syntax. Any agent can parse it.
3. **CLAUDE.md still earns its keep** for Claude-specific affordances (skills, hooks, `/btw` etc.) that AGENTS.md is not the right surface for.
4. **Single source of truth + thin import** is the pattern Claude Code best practices explicitly endorses (`@path/to/import` syntax).

Anti-pattern to avoid: duplicating the same rules in both files. If both exist and disagree, the operator and the agent both lose trust in the spec.

---

## 2 · Skills to add

Add the following 6 skills under `~/AI-Brain-Refinery/.claude/skills/`. Each gets its own folder with a single `SKILL.md`. Skills load only when invoked or when relevant, so they do NOT bloat the every-session context window.

| Skill | Path | Invoke | What it does |
|---|---|---|---|
| `source-inventory` | `.claude/skills/source-inventory/SKILL.md` | `/source-inventory` or implicit when operator asks "inventory this folder" | Runs the source-universe inventory pass · counts files, extension breakdown, archive contents, basename diff vs raw, basename diff vs already-chunked sources. Writes `00_COMMAND_CENTER/*_FULL_SOURCE_INVENTORY_<date>.md`. |
| `staging-plan` | `.claude/skills/staging-plan/SKILL.md` | `/staging-plan` | Reads the latest inventory file + raw state + BATCH_NNN_CHUNKS.jsonl history, produces `00_COMMAND_CENTER/*_STAGING_PLAN_<date>.md` with mkdir + cp commands as recommendations only. |
| `batch-extraction` | `.claude/skills/batch-extraction/SKILL.md` | `/batch-extraction <NNN>` | Extracts source files for BATCH_<NNN> from `raw/` into `01_KNOWLEDGE_BASE/batches/batch_<NNN>_extracted/`. Normalizes filenames to lowercase-snake-case. Mirrors the scripts/extract_batch_00X.py pattern. |
| `jsonl-validation` | `.claude/skills/jsonl-validation/SKILL.md` | `/jsonl-validation <NNN>` | Validates `BATCH_<NNN>_CHUNKS.jsonl` · JSON parse per line, required-field check against the locked schema, chunk count, source-file resolution (each `source_file` must exist on disk in the expected place), token-budget sanity check. |
| `master-consolidation` | `.claude/skills/master-consolidation/SKILL.md` | `/master-consolidation <NNN>` | Updates `MASTER_INDEX.md` + `MASTER_CHUNK_MAP.json` + `ACTIVE_KNOWLEDGE_STATE.md` after a batch is validated. Strict reconciliation rules · old count + new chunks = new count. Refuses to write if validation fails. |
| `session-save` | `.claude/skills/session-save/SKILL.md` | `/session-save` | Writes a snapshot to `00_COMMAND_CENTER/session_saves/<date>_<time>.md` capturing current state, in-flight tasks, next-batch intent, open decisions. Invoke before any `/clear`, before context approaches the 70% limit, or before closing the terminal. |

Each `SKILL.md` should be ~20-50 lines max. The Claude Code docs are clear: skills are loaded only when relevant, but should still stay tight.

Optional second wave (do NOT include in v1 of the operating layer):
- `chunk-writer` · the actual GPT-style chunking pass. Currently lives in scripts/write_batch_00X_chunks.py. Skill would parameterize it.
- `intake-import` · runs the cp pass from a staging plan (after operator authorization).
- `quarterly-audit` · runs the 100Q audit ritual against the corpus.
- `future-source-promote` · promotes a `future_sources/` note to a batch source.

Defer those until v1 has proven the pattern.

---

## 3 · Where each rule lives · the assignment table

| Rule / piece of context | AGENTS.md | CLAUDE.md | Skill | Memory | Comment |
|---|:-:|:-:|:-:|:-:|---|
| Em-dash ban (lifetime user rule) | | | | ✓ | Already in `~/.claude/CLAUDE.md` (global). Do NOT duplicate. |
| Source universe is `~/Downloads/    SNIPED_OS` (current) | ✓ | | | | Stable enough for AGENTS.md. Will change · update both when it does. |
| Folder semantics (raw = staged, 01_KNOWLEDGE_BASE = processed, outputs/batches = legacy) | ✓ | | | | Stable. |
| Path quoting rule (`"    SNIPED_OS"` has 4 leading spaces) | ✓ | | | | Stable. One-line caveat. |
| JSONL chunk schema (`chunk_id`, `batch_id`, `source_title`, etc.) | ✓ | | | | Stable. Encode the field list. |
| 4-phase workflow (inventory → plan → extract → chunk → verify → consolidate) | ✓ | | | | Stable. The locked SOP. |
| Verification commands (jq parse, count, field check, file-exists, count-reconcile) | | | ✓ (`jsonl-validation`) | | Skill content · too verbose for CLAUDE.md. |
| Skill paths + invocation (`/source-inventory`, `/staging-plan`, etc.) | | ✓ | | | Claude-specific. |
| `/clear` between unrelated tasks rule | | ✓ | | | Claude-specific. |
| Hook config (post-edit lint, deny-write to master files) | | ✓ | | | Claude-specific. Lives in `.claude/settings.json`, referenced from CLAUDE.md. |
| BATCH_005 = photography canon (current lock) | | ✓ | | | Date-sensitive. Lives in CLAUDE.md so it's easy to update without touching the portable AGENTS.md. |
| Drift-prevention list (never global Downloads, never master-update mid-batch) | ✓ | | | | Stable. |
| Operator profile (BJ, SNIPED Media, em-dash ban, max-default rule) | | | | ✓ | Already in MEMORY.md. Do NOT duplicate. |
| 12 Canonical Truths | | | | ✓ | Already in MEMORY.md + `00_BRIEF/CANONICAL_TRUTHS.md`. Reference, do not duplicate. |
| The 9 doctrine tags for AlphaGo / Move 37 etc. | | | | | Lives in `02_TIER_2_CANON_BOOKS/...` or `08_AI_TECH/...` source notes when chunked. Not operating layer. |
| Long-running TODO / next-batch reasoning | | | | | Lives in `ACTIVE_KNOWLEDGE_STATE.md`, NOT in CLAUDE.md (changes too often). CLAUDE.md should point at it. |

**The principle:** if it changes weekly, do NOT put it in CLAUDE.md or AGENTS.md. Point at the live doc instead. If it changes once a year, put it in AGENTS.md. If it's Claude-specific tooling, put it in CLAUDE.md.

---

## 4 · How to keep instructions short (context-efficiency)

The Claude Code best practices doc is explicit: **bloated CLAUDE.md files cause Claude to ignore rules**.

Disciplines to enforce:

1. **The 50-line target.** Both AGENTS.md and CLAUDE.md should each fit in roughly 50 lines (after pruning). If they grow past that, audit before adding more.
2. **The "would removing this cause mistakes?" filter.** For every line, ask: would the agent make a mistake without this line? If not, delete it.
3. **Point at the live docs, do not duplicate them.** ACTIVE_KNOWLEDGE_STATE.md, the staging plan, the canonical truths · these are pointed at, not copied in.
4. **No tutorials, no API documentation, no project history.** The agent can read the BATCH_NNN files directly if it needs the schema; the AGENTS.md just says "JSONL with these fields."
5. **No self-evident practices.** "Write clean code" · delete. "Don't break things" · delete.
6. **Imports, not duplication.** CLAUDE.md uses `@AGENTS.md` and `@00_COMMAND_CENTER/ACTIVE_KNOWLEDGE_STATE.md` rather than restating their contents.
7. **Test by observing behavior.** If the agent asks a question that the file answers, the phrasing is ambiguous. If the agent breaks a rule that is in the file, the file is too long. Prune.
8. **Re-audit quarterly.** Both files get a prune pass during the quarterly Constraint Audit.

---

## 5 · Default workflow (the locked SOP)

The 7-step workflow that emerges from BATCH_001-004 + the staging + inventory work. This belongs in AGENTS.md verbatim.

```
1. INVENTORY · know the source universe before doing anything else.
   → run /source-inventory · produces 00_COMMAND_CENTER/*_FULL_SOURCE_INVENTORY_<date>.md
   → never assume a folder is complete; always count first.

2. PLAN · decide where each file lands before moving anything.
   → run /staging-plan · produces 00_COMMAND_CENTER/*_STAGING_PLAN_<date>.md
   → mkdir + cp commands are recommendations only. No execution in this step.

3. AUTHORIZE · operator reviews the staging plan and authorizes the copy pass.
   → no copies happen without explicit operator authorization.

4. STAGE · execute the authorized cp pass into raw/.
   → verify with the checks in plan §5 before proceeding.

5. EXTRACT · run /batch-extraction <NNN> to normalize sources into
   01_KNOWLEDGE_BASE/batches/batch_<NNN>_extracted/.
   → never chunk without extraction first.

6. CHUNK + VALIDATE · produce BATCH_<NNN>_CHUNKS.jsonl, then
   immediately run /jsonl-validation <NNN> against it.
   → no chunks are canonical until validation passes.

7. CONSOLIDATE + SAVE · /master-consolidation <NNN> updates the master
   files. Then /session-save snapshots the state.
   → never update master files mid-batch.
   → never end a session without /session-save.
```

This is the locked SOP. Deviating from it has caused every drift incident so far (the early Downloads-wide scan, the basename-extractor bug, the moment-of-truth where the user moved 280+ files mid-flight).

---

## 6 · Required verification commands per batch

Every batch run must pass these checks before its chunks become canonical. The `jsonl-validation` skill encapsulates them; the agent should run them automatically after producing a `BATCH_<NNN>_CHUNKS.jsonl`.

```bash
B=004  # batch number, parameterize
J=~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/BATCH_${B}_CHUNKS.jsonl

# 1. JSONL validity · every line must parse as JSON
jq -c . "$J" > /dev/null && echo "JSONL parse OK" || echo "JSONL PARSE FAIL"

# 2. Chunk count · matches the count claimed in ACTIVE_KNOWLEDGE_STATE.md / commit message
wc -l "$J"

# 3. Required fields present on every line
jq -c 'select(.chunk_id == null or .batch_id == null or .source_title == null or .source_file == null or .domain == null or .concept == null or .summary == null or .tags == null) | .chunk_id // "MISSING_chunk_id"' "$J"
# Should output nothing. Any line printed is a schema violation.

# 4. Source file resolution · every distinct source_file must exist on disk
jq -r '.source_file' "$J" | sort -u | while read -r f; do
  if [ ! -f ~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/batch_${B}_extracted/"$f" ] && \
     [ ! -f ~/AI-Brain-Refinery/raw/"$f" ]; then
    echo "MISSING SOURCE: $f"
  fi
done

# 5. chunk_id uniqueness
jq -r '.chunk_id' "$J" | sort | uniq -d  # should be empty

# 6. batch_id consistency · all chunks should share the same batch_id
jq -r '.batch_id' "$J" | sort -u | wc -l  # should be 1

# 7. After /master-consolidation runs, reconcile master counts:
PREV=$(jq '.total_chunks' ~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/MASTER_CHUNK_MAP.json.prev 2>/dev/null || echo 0)
NEW=$(jq '.total_chunks' ~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/MASTER_CHUNK_MAP.json)
ADDED=$(wc -l < "$J")
[ $((PREV + ADDED)) -eq "$NEW" ] && echo "RECONCILE OK" || echo "RECONCILE FAIL"
```

If any check fails, `/master-consolidation` MUST refuse to update master files. Halt and surface the failure to the operator.

---

## 7 · Drift-prevention rules

These belong verbatim in AGENTS.md. Every drift incident in the BATCH_001-004 work maps to violating one of these.

| # | Rule | Why |
|---|---|---|
| 1 | **Never process `~/Downloads/` globally unless explicitly instructed.** | The Downloads tree has 8K+ files of mixed corpus, installers, screenshots, financial PDFs. Global scans waste 30+ min and explode context. Source universe is named explicitly each session. |
| 2 | **Source universe (as of 2026-05-18) is `~/Downloads/    SNIPED_OS` only.** | Folder name has 4 leading spaces. Quote it. Other Downloads subfolders are out of scope unless an updated brief says otherwise. |
| 3 | **`raw/` is staged intake. Do not edit it as a working tree.** | Files in raw/ feed chunking. Edits there propagate into the corpus undetected. New work lands in `00_COMMAND_CENTER/` or `_inbox/` first. |
| 4 | **`01_KNOWLEDGE_BASE/` is the processed brain. Do not modify by hand.** | Hand edits break the chunk_id-to-source provenance trail. Only `/master-consolidation` writes here. |
| 5 | **BATCH_005 remains photography canon until explicitly changed.** | Locked per ACTIVE_KNOWLEDGE_STATE.md. Any agent that proposes a different BATCH_005 source set is drifting · pause and re-read the spec. |
| 6 | **Never update master files mid-batch.** | MASTER_INDEX.md, MASTER_CHUNK_MAP.json, ACTIVE_KNOWLEDGE_STATE.md update ONLY after `/jsonl-validation` passes. |
| 7 | **Never move, delete, rename, or extract during planning sessions.** | Plan-only sessions write Markdown only. Authorization is required before any disk-state change. |
| 8 | **No em-dashes anywhere, ever.** | Lifetime rule. Already in global CLAUDE.md. Repeated here so portable-agent sessions inherit it. |
| 9 | **Never assume a folder is complete · always count first.** | The 242-vs-21 basename-extractor bug happened because the prior pass assumed; the next pass counted. Counting beats assuming. |
| 10 | **Numbered chapter slots may collide · flag, do not silently rename.** | `05_AI_EDGE_COURSE` vs `05_PRODUCTION`, `08_AI_TECH` vs `08_BOOK`, `13_OPERATING_DISCIPLINE` vs `13_NETWORK`. Surface the collision to the operator; do not auto-rename. |

---

## 8 · Recommended exact contents · AGENTS.md (preview only · DO NOT WRITE YET)

```markdown
# AGENTS.md · AI-Brain-Refinery

A SNIPED Media corpus refinement workspace. Reads source documents, chunks them into a structured knowledge base, and feeds the SNIPED operating system.

## Source universe and folder semantics

- **Source universe (2026-05-18):** `~/Downloads/    SNIPED_OS/` only. Folder name has 4 leading spaces. Quote it in shell.
- **`raw/`:** staged intake mirror. Never edit by hand outside an authorized staging pass.
- **`01_KNOWLEDGE_BASE/`:** processed brain. Holds `batches/BATCH_<NNN>_CHUNKS.jsonl`, `MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`. Written by `/master-consolidation` only.
- **`00_COMMAND_CENTER/`:** plans, inventories, future-source notes, session saves. Markdown only.
- **`outputs/`, `batches/`, `indexes/`, `scripts/`:** legacy locations from earlier passes. `scripts/` is active tooling; the rest are referenced read-only.

## JSONL chunk schema (BATCH_003 onwards · canonical)

Per-line fields: `chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags`.

BATCH_002 uses `batch` instead of `batch_id` · do NOT migrate retroactively; both schemas are canonical for their respective batches.

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
- `jq -c .` every line of `BATCH_<NNN>_CHUNKS.jsonl` parses
- Required fields present per line
- `chunk_id` unique within the batch
- All `source_file` values resolve on disk
- Master count = previous count + new chunks

If any check fails, halt and surface to the operator. Do NOT write to master files.

## Drift-prevention rules

1. Never process `~/Downloads/` globally unless explicitly instructed.
2. Source universe = `~/Downloads/    SNIPED_OS` only (until brief says otherwise).
3. `raw/` is staged intake · do not edit as a working tree.
4. `01_KNOWLEDGE_BASE/` is processed brain · do not modify by hand.
5. Never update master files mid-batch.
6. Never move/delete/rename/extract during planning sessions.
7. No em-dashes anywhere, ever.
8. Always count before assuming.
9. Surface chapter-slot collisions; do not auto-rename.

## What to read at session start

- `00_COMMAND_CENTER/ACTIVE_KNOWLEDGE_STATE.md` · what is canon now, what is next.
- `00_COMMAND_CENTER/SNIPED_OS_STAGING_PLAN_2026-05-18.md` · current staging gap (until consumed).
- `01_KNOWLEDGE_BASE/MASTER_INDEX.md` · narrative consolidation of the chunked corpus.

## Out of scope (without explicit operator instruction)

- The rest of `~/Downloads/` outside `    SNIPED_OS`.
- `~/sniped-media/` (web project codebase).
- Any disk-state change during a planning session.
- BATCH_005 redefinition (locked as photography canon).
```

Target line count: ~55. The actual file should aim under 50 after final pruning.

---

## 9 · Recommended exact contents · CLAUDE.md (preview only · DO NOT WRITE YET)

```markdown
# CLAUDE.md · AI-Brain-Refinery

@AGENTS.md

## Claude Code specifics

- **Skills live in `.claude/skills/`.** Available: `source-inventory`, `staging-plan`, `batch-extraction`, `jsonl-validation`, `master-consolidation`, `session-save`. Invoke via `/<skill-name>`.
- **Use `/clear` between unrelated tasks.** A staging plan session and a chunking session do not share context. Saving the session first via `/session-save` is required before `/clear`.
- **Use plan mode** for anything that would touch disk state (cp, mkdir, write to MASTER_*). Exit plan mode only after operator authorizes execution.
- **Default `AskUserQuestion` for ambiguous routing.** Chapter-slot collisions (e.g., `13_OPERATING_DISCIPLINE` vs `13_NETWORK`) are routing decisions · ask, do not auto-rename.
- **Side questions go in `/btw`.** Quick context lookups that should NOT enter the conversation history use `/btw`.

## Current operating lock (date-sensitive · keep this section tight)

- Source universe: `~/Downloads/    SNIPED_OS` (2026-05-18).
- Next batch: BATCH_005 = photography canon (locked).
- Future batches queued: see `00_COMMAND_CENTER/SNIPED_OS_STAGING_PLAN_2026-05-18.md` §6.
- Future-source notes (uncanonical · do NOT chunk): `00_COMMAND_CENTER/future_sources/`.

## Hooks (configured via `.claude/settings.json`)

- Post-edit hook on `01_KNOWLEDGE_BASE/batches/*.jsonl`: run `jq -c . "$file" > /dev/null` to catch syntax errors immediately.
- Pre-write deny rule on `01_KNOWLEDGE_BASE/MASTER_INDEX.md` and `MASTER_CHUNK_MAP.json`: only `/master-consolidation` may write here. Direct edits blocked.
- Pre-bash deny rule on `rm -rf ~/Downloads/    SNIPED_OS`: this folder is the source universe; never delete.

## When to escalate to the operator

- Any disk-state change not in the authorized plan.
- Any chunk that fails `/jsonl-validation`.
- Any source-file that cannot be resolved on disk.
- Any chapter-slot collision.
- Any time context exceeds 70% before reaching a clean save point.
```

Target line count: ~30 after import.

---

## 10 · Recommended `.claude/settings.json` skeleton (preview · do NOT write yet)

```json
{
  "permissions": {
    "allow": [
      "Bash(jq:*)",
      "Bash(wc:*)",
      "Bash(find ~/AI-Brain-Refinery/*:*)",
      "Bash(ls:*)",
      "Read",
      "Write",
      "Edit"
    ],
    "deny": [
      "Bash(rm -rf ~/Downloads/    SNIPED_OS*)",
      "Bash(rm -rf ~/AI-Brain-Refinery/01_KNOWLEDGE_BASE*)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "for f in ~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/*.jsonl; do jq -c . \"$f\" > /dev/null 2>&1 || echo \"JSONL syntax error in $f\"; done"
          }
        ]
      }
    ]
  }
}
```

This is illustrative · the actual hook scripts should be Bash files in `.claude/hooks/` so they are testable and version-controlled. The settings.json is intentionally minimal · auto-mode (the classifier) handles most permission decisions; explicit allow/deny is reserved for the load-bearing safety rules.

---

## 11 · Recommended skill file skeletons (preview · do NOT write yet)

Each skill is its own folder with one `SKILL.md`. Here is the template for one (`jsonl-validation`); the other five follow the same shape with task-specific bodies.

```markdown
---
name: jsonl-validation
description: Validate a BATCH_<NNN>_CHUNKS.jsonl file against the locked schema. Run BEFORE master-consolidation.
disable-model-invocation: false
---
Validate `01_KNOWLEDGE_BASE/batches/BATCH_$ARGUMENTS_CHUNKS.jsonl`.

1. JSONL parse · every line must parse via `jq -c .`. Halt on first failure.
2. Required fields · every line must have `chunk_id`, `batch_id`, `source_title`, `source_file`, `domain`, `concept`, `summary`, `tags`. (Author, usable_principle, sniped_relevance, direct_quotes are recommended but not required.)
3. chunk_id uniqueness within the batch.
4. batch_id consistency · exactly one distinct batch_id across all lines.
5. source_file resolution · every distinct source_file value must exist either at `01_KNOWLEDGE_BASE/batches/batch_$ARGUMENTS_extracted/<file>` or at `raw/<file>`.
6. Report total chunk count + unique source count.
7. If any check fails, refuse to proceed and surface the failures to the operator.

Do NOT run `/master-consolidation` if any check fails.
```

Total skill file count for v1: 6 files, ~20-50 lines each. Negligible context cost; loaded only when invoked.

---

## 12 · Migration sequence (when authorized · NOT executing yet)

Order matters. If the operator authorizes the operating layer, run in this sequence:

1. **Write AGENTS.md first.** Establish the portable single source of truth.
2. **Write CLAUDE.md second** with `@AGENTS.md` import.
3. **Create `.claude/skills/` directory + the 6 SKILL.md files.**
4. **Write `.claude/settings.json` last** · permissions and hooks come after the skills exist (so hook scripts can reference skill outputs).
5. **Test the layer in a fresh session.** Open a new Claude Code session in `~/AI-Brain-Refinery/`, verify AGENTS.md + CLAUDE.md auto-load (check via a quick "what is the source universe?" probe), verify a skill invocation works (`/source-inventory` against a small folder).
6. **Document the bootstrap** in `ACTIVE_KNOWLEDGE_STATE.md` so the next session knows the operating layer is live.

Estimated time to land: 30-45 min of focused authoring + testing once authorized.

---

## 13 · What this plan does NOT do

- Does NOT create CLAUDE.md.
- Does NOT create AGENTS.md.
- Does NOT create `.claude/` or any subdirectory.
- Does NOT write any SKILL.md files.
- Does NOT modify `.claude/settings.json` (none exists yet).
- Does NOT update `MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, or `ACTIVE_KNOWLEDGE_STATE.md`.
- Does NOT start BATCH_005.
- Does NOT chunk anything.
- Does NOT move, copy, delete, rename, or extract any file.

End of plan. Awaiting operator authorization to proceed with the migration sequence in §12.
