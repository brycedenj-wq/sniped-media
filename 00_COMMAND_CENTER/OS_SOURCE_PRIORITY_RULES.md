# OS SOURCE PRIORITY RULES

How the OS uses the whole Mac without crawling everything or trusting stale docs. Enforced via `os_source_router.py` + `EXTERNAL_SOURCE_REGISTRY.csv`.

## The priority ladder (highest = wins on conflict)
1. **AI-Brain-Refinery** (`/Users/sniper/AI-Brain-Refinery`) - the execution root and CURRENT-STATE truth. Newest committed truth here wins, always.
2. **Active project folders** (e.g. `ALMA_LOVE_PRODUCTION_001`) - truth for THAT project's selects/exports.
3. **BJ-WIKI** (`~/Documents/BJ-WIKI`) - long-term memory / second brain. Synthesis + identity, not execution.
4. **SNIPED_OS legacy** (`~/Downloads/    SNIPED_OS`, 4 leading spaces) - high-priority LEGACY/source library. Deep doctrine, history, books, prompts, frameworks. **Never current truth.**
5. **Intake** (`~/Downloads`, `~/Desktop`) - staging only. Never canon without a freshness check.

## Conflict rule (the one that matters)
If an old SNIPED_OS (or any legacy) file conflicts with a newer AI-Brain-Refinery current-state doc, **flag the conflict and use the newer PROVEN truth.** Legacy informs, never overrides.

## Use-class rules
- **Books / frameworks** -> compressed into decision principles (story/psych cards + libraries via `os_story_gate.py`). Do NOT read raw books every time; consult SNIPED_OS/BJ-WIKI only to EXTEND a card.
- **Media folders** (`~/Pictures`, Lightroom catalog, `Documents/Photography`) -> used by project-specific photo/video builders, NOT by strategy answers (unless the question is the workflow itself).
- **Naming** -> the naming engine/library FIRST, not old brainstorm docs.
- **Client files** (`~/ClaudeBusiness`) -> only when a client decision needs records; contains identity/client info, handle privately.

## Hard ignores (never scanned/ingested)
`~/Library`, `**/.git`, `**/node_modules`, `**/.cache`, `**/*.lrdata`, secret stores. Downloads/Desktop are intake, not corpus.

## Safety
Read-only. The OS never copies huge files, moves, deletes, `git add -A`, or ingests caches just to map sources. The map is a router, not a crawler.

## No overclaiming
The OS may not claim "the whole Mac is wired" unless `EXTERNAL_SOURCE_REGISTRY.csv` lists the source and `os_source_map_scan.py` confirms it exists. Unverified = unknown.
