# OS BOOTLOADER / COMMAND-ROUTER ARCHITECTURE (2026-06-04)

> How the OS resumes from disk and operates as one body , without dumping every doc into context, without turning chunks into a mega-skill, and without restarting work each session. A thin front door that loads almost nothing, then pulls only what the task needs.

## RECOMMENDATION (the one idea)
Build a **thin bootloader** that, on a cold start, loads only ~5 tiny "boot files" (current-state, mission, next-action, router index, cert-ledger summary) , **never doctrine, never chunks, never skills in bulk.** The bootloader orients the session, then a **router** (the existing `os-command-router`) pulls the *specific* doctrine doc / skill / chunk the current task needs, by consulting small INDEXES. Disk is the source of truth; chat memory is disposable. The cert ledger decides whether anything actually needs (re)doing.

The layers stay separate and do different jobs (this is the whole point):
| layer | what it is | when loaded |
|---|---|---|
| **chunks** | evidence / quotes / examples in the KB | on demand, by id, never in bulk, never auto-skills |
| **doctrine** | distilled, reusable operating knowledge | one domain doc at a time, when the task touches that domain |
| **skills** | executable, repeatable procedures | invoked by name when the procedure is run |
| **indexes** | lookup tables (topic → doctrine/skill/chunk) | read by the router to decide what to pull (small) |
| **current-state** | what is true NOW (mission, done, blocked) | every cold start |
| **handoff** | what the last session left (next action, log tail) | every cold start |
| **cert ledger** | what is actually certified / incomplete | gates the "do we redo this?" decision |
| **bootloader** | decides what to load | the front door |

---

## FILE STRUCTURE
```
00_COMMAND_CENTER/
  OS_BOOT.md                  # THE FRONT DOOR. read-order + startup sequence. ~1 page.
  OS_CURRENT_STATE.md         # what is true now: ACTIVE mission, done, blocked, cert summary
  NEXT_ACTION.md              # the single next step (handoff)
  SESSION_LOG.md              # append-only: what each session did
  OS_ROUTER_INDEX.md          # domain -> doctrine docs + skills + chunk-index pointers
  OS_CERTIFICATION_LEDGER.csv # what is certified / incomplete (the redo gate)
  OS_ENGAGEMENT_MANIFEST.csv  # every source + status (dedup arbiter)
  scripts/os_boot.py          # prints the boot brief (runs at SessionStart)
  OS_DOCTRINE_*.md            # distilled doctrine (pulled one domain at a time)
01_KNOWLEDGE_BASE/
  MASTER_INDEX.md             # narrative index of the chunked corpus
  batches/*_CHUNKS.jsonl      # chunks (evidence) , retrieved by id, never bulk-loaded
99_ARCHIVE/                   # superseded projects (NOT loaded at boot)
.claude/
  skills/<name>/SKILL.md      # executable procedures (invoked by name)
  settings.json               # SessionStart hook -> os_boot.py
CLAUDE.md                     # @import -> points the cold session at OS_BOOT.md
MEMORY.md                     # auto-loaded by the harness (durable facts)
```

## STARTUP PROTOCOL (the exact sequence)
A fresh Claude Code chat, cold:
1. Harness auto-loads `CLAUDE.md` (+ `MEMORY.md`). `CLAUDE.md` says: "First action , read `OS_BOOT.md`."
2. `SessionStart` hook runs `os_boot.py`, which prints the **boot brief**: ACTIVE mission, cert summary (certified % + what's incomplete), NEXT_ACTION, last 3 SESSION_LOG lines, and any open checkpoint.
3. Claude reads `OS_BOOT.md` (the read-order) and `OS_CURRENT_STATE.md`. **It does NOT load doctrine or chunks.** It now knows: the mission, what's done, what's next.
4. For the task at hand, Claude invokes `os-command-router`, which reads `OS_ROUTER_INDEX.md` and pulls ONLY the relevant doctrine doc(s) / skill(s) / chunk id(s).
5. Execute the task. Run quality gates.
6. **Session end:** update `OS_CURRENT_STATE.md` + `NEXT_ACTION.md`, append to `SESSION_LOG.md`, run `os_checkpoint.py`. The next session resumes from these, not from chat.

## SKILL ARCHITECTURE
- **One front-door router** (`os-command-router`, already ACTIVE): classify request → mode → which doctrine/skill/chunk to pull. It is the only thing that decides loading.
- **Domain skills** (executable procedures): `sniped-*`, `os-*`. Invoked by name, never bulk-loaded. The router maps request → skill via the index.
- A skill is a *procedure*, not knowledge. If it's knowledge, it's doctrine, not a skill.

## RETRIEVAL ARCHITECTURE (two-stage, never bulk)
1. **Router reads the INDEX** (`OS_ROUTER_INDEX.md` , small): maps the request's domain to the exact doctrine doc, skill, and chunk-index.
2. **Pull the specific item**: one doctrine doc, or specific chunk ids via `MASTER_INDEX` → `batches/*_CHUNKS.jsonl`. Never load a whole batch, never load all doctrine.
- Chunks are retrieved by **id/topic**, used as evidence, then dropped from context. The KB is a database queried on demand, not a context payload.

## CHUNK-TO-SKILL DECISION RULE (the user's core distinction, made operational)
For any piece of knowledge, route it ONCE:
- **It stays a CHUNK** (KB/reference) if it's evidence, a quote, an example, a data point , retrieved occasionally. **Default.**
- **It becomes DOCTRINE** if the *principle* is reused across tasks → distill into an `OS_DOCTRINE_*` entry (with its source cert status attached).
- **It becomes a SKILL** only if it's an *executable, repeatable PROCEDURE* you've run **3+ times** (the "built 3x = skill" rule) and it passes the skill activation contract (trigger/inputs/outputs/tests).
- **It becomes an INDEX entry** if it needs to be *findable* by the router.
Decision: `executable procedure + repeated → skill` · `reusable knowledge → doctrine` · `evidence → chunk` · `findability → index`. When unsure, it stays a chunk. **Most chunks never become skills.**

## CURRENT-STATE / HANDOFF SYSTEM
- `OS_CURRENT_STATE.md` , the single source of "what is true now": the ONE active mission, cert summary, what's done, what's blocked. Overwritten at session end.
- `NEXT_ACTION.md` , the single next step, verbatim, so the next session doesn't re-derive it.
- `SESSION_LOG.md` , append-only history (date, what was done, commit). The audit trail.
- Resume = read these three. Never reconstruct state from chat memory.

## ANTI-DUPLICATION PROTOCOL
1. Before any work, the router checks `OS_CERTIFICATION_LEDGER.csv` + `OS_CURRENT_STATE.md` + `SESSION_LOG.md`: **if it's certified/done, do not redo it.**
2. **The cert ledger is the redo gate** , "do not restart unless the cert ledger says incomplete." (Your rule, enforced.)
3. The manifest md5 dedup prevents re-processing the same file; `OS_*_DUPLICATES.csv` logs exact dups (preserved, not reread).
4. A WORK_REGISTRY line in `OS_CURRENT_STATE.md` lists what's already built (scripts, skills, gates) so they're reused, not rebuilt.

## ANTI-OLD-PROJECT-CONTAMINATION PROTOCOL
1. **Exactly ONE active mission** named in `OS_CURRENT_STATE.md`. The boot loads only the active mission's handoff.
2. Superseded projects move to `99_ARCHIVE/` and are **never loaded at boot**. The router refuses to pull archived doctrine unless explicitly asked by name.
3. Doctrine entries carry a `status: active | superseded | hypothesis` tag; the router ignores `superseded` by default.
4. The possibility-engine guardrail holds: no old "crowned lane" leaks in , current-state names the active mission only, and old strategy docs are evidence, not law.

## WHAT TO BUILD NEXT (implementation plan, in order)
1. Create the 4 boot files: `OS_BOOT.md`, `OS_CURRENT_STATE.md`, `OS_ROUTER_INDEX.md`, `NEXT_ACTION.md` (templates created with this doc).
2. Build `scripts/os_boot.py` , prints the boot brief (mission + cert summary + next action + log tail + open checkpoints). Wire it into the `SessionStart` hook (alongside the existing `os_session_start.sh`).
3. Point `CLAUDE.md` at `OS_BOOT.md` ("first action: read OS_BOOT.md").
4. Populate `OS_ROUTER_INDEX.md` from the existing doctrine docs + skills (a one-time index build).
5. Extend `os-command-router` to consult `OS_ROUTER_INDEX.md` before pulling anything.
6. Create `99_ARCHIVE/` and move superseded project docs there; tag remaining doctrine `active/superseded/hypothesis`.
7. Add a session-end skill (`os-session-end`) that updates current-state + next-action + session-log + runs `os_checkpoint.py`.

## EXACT STARTUP COMMAND / PROMPT
- **Automatic:** the `SessionStart` hook runs `os_boot.py` , the boot brief prints with no user action.
- **Manual one-liner (the activation prompt):**
  > `Boot the OS: read 00_COMMAND_CENTER/OS_BOOT.md and resume the ACTIVE mission from OS_CURRENT_STATE.md + NEXT_ACTION.md. Do not load doctrine or chunks until the router needs them. Do not redo anything the certification ledger marks certified.`
- Or a slash command `/os-boot` that does the same.

## THE GOAL, RESTATED
Every new session starts cold, reads the boot files (small), learns the mission + what's done + what's next, pulls only the relevant doctrine/skills/chunks via the router+indexes, and continues , no circling, no duplication, no reliance on chat memory, no old project bleeding in. The OS is one body that wakes up from disk.
