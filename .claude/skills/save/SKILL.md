---
name: save
description: Persist a specific insight, decision, preference, or fact from the current conversation into the correct durable location · the auto-memory system (cross-session facts, preferences, feedback, project state), a Command Center anchor doc (a standalone strategic artifact), or a short log note. Use whenever the operator says "/save", "save this", "remember this", "persist this", or asks to keep something from the conversation. Routes correctly, checks for duplicates, follows each destination's format, and never chunks or mutates master files.
disable-model-invocation: false
---

# Save

Capture valuable context from the current conversation into the right durable home. This workspace has three persistence layers and a hard rule about what is off-limits. Route to the correct layer · do not dump a markdown file somewhere generic.

## The three destinations (pick by what the content IS)

1. **Auto-memory** · `/Users/sniper/.claude/projects/-Users-sniper/memory/`
   For anything that should survive across conversations: a fact about the operator (`user`), guidance on how to work (`feedback`), ongoing project state (`project`), or a pointer to an external system (`reference`). This is the default for durable, cross-session signal.

2. **Command Center anchor doc** · `00_COMMAND_CENTER/`
   For a strategic decision, synthesis, or artifact substantial enough to warrant its own standalone markdown document (the way `TRUE_BILLION_DOLLAR_THESIS.md` or `BASEPLATE_CANONICAL_STATEMENT.md` do). Anchor-class: not chunked, not in the master files.

3. **Session state** · defer to `/session-save`
   If the operator means "save where we are" broadly (files touched, decisions, open questions, next action), do not duplicate that here · invoke `/session-save` instead.

If it is a one-off observation with no durable principle, a short `project`-type memory entry or a `/session-save` note is enough. Do not write into `raw/` (the intake mirror is immutable, including its `00_BRIEF/ACTIVE_THREADS.md`). Do not manufacture a page to justify the invocation.

## Workflow

### 1. Classify the save-worthy content
Scan the conversation and identify the discrete piece(s) worth keeping. Map each to one destination above. One conversation can produce more than one save. Do not force everything into one place, and do not split one coherent item across several.

### 2. Check what already exists before creating
Duplicates rot the system. Before creating anything:
- Memory: read `MEMORY.md` (the index) and `ls` the memory dir. If a memory on the same topic exists, UPDATE it rather than create a new one.
- Command Center: `ls 00_COMMAND_CENTER/` and check the coverage manifest. If a doc already covers it, update or extend.

### 3. Write or update, following the destination's exact format

**Memory** (two-step, per the memory system rules):
- Step 1 · write the memory to its own file (e.g. `feedback_<slug>.md`) with the required frontmatter: `name`, `description`, `metadata.type` (user | feedback | project | reference). For feedback/project, structure the body as the rule/fact, then a **Why:** line and a **How to apply:** line. Link related memories with `[[slug]]`.
- Step 2 · add a one-line pointer in `MEMORY.md`: `- [Title](file.md) · one-line hook`. Keep it under ~150 chars. Never write memory content directly into `MEMORY.md`.
- Convert relative dates ("Thursday", "next week") to absolute dates before saving.

**Command Center anchor doc:**
- Header block: date, status, and an "Anchor-class: markdown-only, not chunked, not in the master files" line.
- A guardrails block at the end mirroring the workspace locks (no permanent identity lock where relevant, no fake proof, north-star intact, Bible held, total_chunks unchanged).

### 4. Update the relevant index
If a new memory was created, add its pointer to `MEMORY.md`. If a new Command Center doc was created, note it where the coverage manifest expects.

### 5. Report back
Short summary: what was created or updated (with paths), what the index/pointer now says, and anything you considered saving but decided against, with one-line reasoning.

## Decision guide: memory vs. Command Center vs. log
- **Memory** · cross-session, about the operator or how to work or project state or an external pointer. Most `/save` invocations land here.
- **Command Center doc** · a strategic artifact with a named topic that future work will route through, substantial enough to stand alone.
- **Log note** · a one-off decision or observation with no durable principle.

When unsure between memory and a CC doc, prefer updating an existing memory · memories compound and are always loaded; CC docs are heavier.

## What this skill must NEVER do (hard guardrails)
- Never write into `01_KNOWLEDGE_BASE/` · no chunks, no `CHUNKS.jsonl`, no edits to `MASTER_INDEX.md` or `MASTER_CHUNK_MAP.json`, no new domains, no `extracted/` dirs. The corpus is processed brain · this skill does not touch it.
- Never touch `raw/`.
- Never touch the held Bible (`SPIRITUAL_FOUNDATION`).
- Never invent facts, dates, or quotes the conversation did not produce. If the operator said "around 40%", write "around 40%".
- No em-dashes anywhere.
- Do not commit. The operator gates all commits · report what was written and stop.


## Inputs
- The specific insight, decision, preference, or fact from the current conversation to persist (required)
- Operator signal: '/save', 'save this', 'remember this', or 'persist this' (required trigger)
- Destination hint if stated (memory vs Command Center anchor doc); skill classifies if not provided

## Outputs
- For memory saves: new or updated memory file under /Users/sniper/.claude/projects/-Users-sniper/memory/ with required frontmatter (name, description, metadata.type) plus a one-line pointer added or updated in MEMORY.md
- For Command Center anchor docs: new or updated markdown under 00_COMMAND_CENTER/ with header block (date, status, Anchor-class line) and guardrails block
- Short report: paths created or updated, what MEMORY.md now says, and anything considered but not saved with one-line reasoning
- One-line receipt: e.g. 'Saved to memory/alma_color_world_grade.md + pointer updated in MEMORY.md; no CC doc (not standalone-artifact class)'

## Gates
- Duplicate check: read MEMORY.md + ls memory dir before creating; if topic exists UPDATE, never create a duplicate
- Destination gate: route to auto-memory, CC anchor doc, or defer to /session-save only; never dump to a generic markdown file
- Hard corpus lock: never write into 01_KNOWLEDGE_BASE/, raw/, MASTER_INDEX.md, MASTER_CHUNK_MAP.json, extracted/ dirs, or the held Bible (SPIRITUAL_FOUNDATION)
- No invented content: if operator said 'around 40%' write 'around 40%'; never fabricate quotes, dates, or figures
- No commit: report what was written and stop; operator gates all commits

## Test
- case: Operator says 'save this: Alma hero skin drift was +2.8/+2.8/+2.9 uniform, color leads, B&W is sidecar only.' Expected: classify as project-type memory, check MEMORY.md for existing Alma color-world entry, update memory/alma_color_world_grade.md with measured values and rule, update MEMORY.md pointer, print file path and one-line report. No CC doc. No commit.
- expected failure: Operator says 'save this' but the conversation contains no discrete fact or decision (e.g. only a Q&A with no new principle). Skill responds: 'Nothing save-worthy identified. Quote the specific fact or decision and re-invoke /save.'


## INVOKE WHEN
- the save task arises: Persist a specific insight, decision, preference, or fact from the current conversation into the correct durable locatio
