# OS <-> BJ-WIKI Sync Plan

LOCKED 2026-06-05. Two brains, one operator. Keep them distinct; sync at defined seams. Do NOT duplicate blindly.

## The two systems
- **AI-Brain-Refinery (this repo)** = the EXECUTION OS. Live operating layer: technique cards, gates, routes, registries, scripts, dashboards, the campaign-house production system. Optimized for DOING. Git-versioned.
- **~/Documents/BJ-WIKI** = the long-term SECOND BRAIN (Obsidian/LLM wiki, Mode D+C+E). Compounding knowledge: `.raw/` sources, `wiki/` synthesis (concepts, domains, entities, comparisons, questions), `_meta/hot-cache.md`, `wiki/log.md`, 10 domain pages. Optimized for KNOWING / remembering / cross-domain synthesis.

## What lives where (the rule)
| Lives in AI-Brain-Refinery | Lives in BJ-WIKI |
|---|---|
| Technique cards, gates, routes, scripts | Concepts, doctrines, entity/relationship notes |
| Tool registry, dashboards, ledgers | Raw sources (.raw/), distilled references |
| Campaign-house production artifacts | Cross-domain synthesis, comparisons, open questions |
| OS_CURRENT_STATE, NEXT_ACTION (execution state) | hot-cache.md (knowledge context), log.md (decision journal) |
| "How the OS DOES X" | "What BJ KNOWS / has decided / why" |

Rule of thumb: if it is CALLABLE (a card/gate/route/script), it lives in the Refinery. If it is KNOWLEDGE the operator reasons from across time, it lives in BJ-WIKI.

## Sync seams (only these, not everything)
1. **OS decision -> BJ-WIKI log.** When the OS makes or locks a real decision (a standing order, a lane call, a money decision, a doctrine lock), file a one-line entry into `BJ-WIKI/wiki/log.md` with date + link to the Refinery artifact/commit. Decisions are knowledge; they belong in the second brain's journal.
2. **BJ-WIKI hot-cache -> OS_CURRENT_STATE.** When `BJ-WIKI/_meta/hot-cache.md` records a new external truth that changes execution (a new tool, a new constraint, a changed goal), reflect it in OS_CURRENT_STATE.md (newest committed truth wins). The hot-cache is upstream context; OS_CURRENT_STATE is the execution snapshot.
3. **Refinery memory atoms <-> BJ-WIKI concepts.** A locked Refinery doctrine (e.g. current-state-first, video-edit-automation) gets a stub concept page in BJ-WIKI/wiki/concepts linking back to the Refinery doc. Do not copy the whole doc; link it.
4. **Raw sources -> BJ-WIKI .raw, distilled -> cards.** New transcripts/docs land in BJ-WIKI/.raw (the archive of record for knowledge), and the EXECUTABLE distillation becomes Refinery technique cards. (Mirrors STARTHERE_SOURCE_ARCHIVE -> TECHNIQUE_CARDS.)

## When each sync fires
- After any commit that locks a decision/doctrine -> append to BJ-WIKI/wiki/log.md (manual or os_bj_wiki_sync.py log).
- At session boot -> os_current_state_boot reads OS_CURRENT_STATE; if BJ-WIKI/_meta/hot-cache.md is newer and conflicts, surface it (future: add hot-cache to the boot artifact list).
- When a new doctrine is locked -> create/refresh a BJ-WIKI concept stub.

## Do NOT
- Do not mirror the entire Refinery into BJ-WIKI or vice-versa (two copies = drift).
- Do not let BJ-WIKI become a second execution layer (no cards/gates there).
- Do not auto-write into BJ-WIKI without the operator's structure (it has its own templates/_meta); os_bj_wiki_sync.py only APPENDS to log.md and reads hot-cache, nothing destructive.

## Tooling
- `os_bj_wiki_sync.py status` , show BJ-WIKI paths + hot-cache age vs OS_CURRENT_STATE.
- `os_bj_wiki_sync.py log "<decision>" <commit>` , append a decision line to BJ-WIKI/wiki/log.md (append-only, safe).
- (Deferred) hot-cache -> boot integration once the format stabilizes.
