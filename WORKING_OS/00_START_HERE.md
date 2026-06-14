# 00_START_HERE · WORKING_OS boot document

This is the first file a fresh Claude session opens. It is a thin pointer layer, not the brain itself. It tells you where the brain, state, skills, and knowledge index live, the order to read them, how to route a task, and where the current state and projects sit. Read this, then 01_CURRENT_STATE.md, then route.

Lifetime rule carried into every output: no em-dashes, ever.

## The architecture in one breath

- Canonical runtime brain: `/Users/sniper/AI-Brain-Refinery`. The ONE persistent root. Only git repo, all active hooks, only unified knowledge index. Nothing the runtime depends on may live outside this root.
- Frozen read-only source archive: `/Users/sniper/Downloads/    SNIPED_OS/` (four leading spaces in the folder name, always quote it in shell). The original full OS and source universe. Cold storage. The runtime must not depend on it at session start.
- This WORKING_OS layer: `/Users/sniper/AI-Brain-Refinery/WORKING_OS/`. Thin pointers and read-order over the brain. It owns no state; it points at the owners.

## Where each thing lives (canonical)

- State surface: `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/` holds NEXT_ACTION.md (Jun 10, freshest), CURRENT_STATE.md (Jun 5), ACTIVE_KNOWLEDGE_STATE.md, OS_ACTIVATION_INDEX.json. STANDING_ORDER.md is currently only in SNIPED_OS and is pending creation here (see Open calls).
- Knowledge index: `/Users/sniper/AI-Brain-Refinery/01_KNOWLEDGE_BASE/MASTER_CHUNK_MAP.json` and `MASTER_INDEX.md` (about 1,879 chunks, 62 domains). The only unified index of the chunked brain.
- Skill harness: `/Users/sniper/AI-Brain-Refinery/.claude/skills` (78 skills) plus the router map `00_COMMAND_CENTER/OS_ACTIVATION_INDEX.json` (76 registered). 7 sniped-* skills still resolve from `SNIPED_OS/_skills` via an allowlist until migration completes (see Open calls).
- Hooks and scripts: `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/` (os_session_start.sh and the hook stack).

## Read order for a fresh session

1. This file (00_START_HERE.md) for the map and the open calls.
2. 01_CURRENT_STATE.md for the locked thesis, the proof loop, the forwarding mission, and the standing order.
3. Route the task: 02_COMMAND_ROUTER.md to classify and dispatch, 03_DECISION_ENGINE.md when the task is a real decision.
4. Pull the engine for the domain: 07_CREATIVE_ENGINE.md (AI film/image), 08_PRODUCTION_ENGINE.md (photo/post), 06_OFFERS_AND_MONEY.md (offers/pricing).
5. Query knowledge through 09_KNOWLEDGE_INDEX.md. Find skills through 10_SKILLS_INDEX.md. Find context and handoffs through 11_MEMORY_AND_HANDOFFS.md.

## How to route a task (short form)

1. Classify the input (02_COMMAND_ROUTER.md, the 15 input types).
2. Check it against STANDING_ORDER and NEXT_ACTION. If it contradicts them, surface that and get an operator override before proceeding.
3. Decide seriousness (03_DECISION_ENGINE.md): a hard production domain (film, photo_composite, editing_retouch, brand_campaign, web_build), OR two or more domains touched, OR a serious keyword present. Serious work runs through a harness (role-scoped agents plus adversarial-verify) and produces an OS_RECEIPT.md. One agent may not select, cut, grade, review, and crown its own work. Single-thread is only for casual drafting or low-risk notes.
4. Activate the scoped skill set via OS_ACTIVATION_INDEX.json. Never dump the whole corpus.
5. Retrieve knowledge from MASTER_CHUNK_MAP.json; if a topic is not yet chunked, consult CANONICAL_SOURCE_MAP.md for the file location.
6. NEVER SAMPLE. Whole-read every doc, whole-watch every clip. Sampling is a hard failure.

## Where projects live

- Index of every project: 04_PROJECTS_INDEX.md.
- Live, movable projects only: 05_ACTIVE_PROJECTS.md.
- Project folders sit under `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/` (for example ALMA_MARGIELA_SAVE_001, kingdom_of_the_sun, OS_PRIME_MOVER_ACTIVATION_001). ALMA_LOVE_PRODUCTION_001 (about 6.5G, paused) sits at the repo root and is treated as parked external asset storage.

## Current top-level state

Operating reset as of 2026-06-10 (NEXT_ACTION.md): treat the OS as fresh. All prior projects and lanes (Synergy/FMO, Alma/swimwear, the Prime Mover campaign-house default, corpus batches, AXIS, Kingdom of the Sun) are capability proof and archive, not active missions. The only forward mission is lane discovery: find the one lane/product to embody and push, logged in `00_COMMAND_CENTER/LANE_DISCOVERY_LEDGER.md`. No lane is crowned without real served or paid reps. The operator's live word beats every old doc.

Locked thesis underneath (CURRENT_STATE.md, Jun 5, BASEPLATE framing): BASEPLATE as the trusted operator layer, wedge is the Capability Dossier, public domain baseplateworks.com, Baseplate LLC. Zero paid pilots yet; the proof loop (PROOF_LOOPS_30_60_90.md) is the scoreboard. Note: the Jun 10 reset supersedes the campaign-house default in the older standing order; both are surfaced in 01_CURRENT_STATE.md and the operator confirms which leads.

Money and creative engines: 06_OFFERS_AND_MONEY.md, 07_CREATIVE_ENGINE.md, 08_PRODUCTION_ENGINE.md. Backup and the git protocol: 12_BACKUP_AND_REPO_PROTOCOL.md.

## The 12 sibling files

- 01_CURRENT_STATE.md: the reconciled operating state (thesis, proof loop, mission, standing order, guardrails).
- 02_COMMAND_ROUTER.md: the 15 input types and the routing algorithm.
- 03_DECISION_ENGINE.md: canonical truths, decision frameworks, harness dispatch.
- 04_PROJECTS_INDEX.md: one-line index of every project, by status.
- 05_ACTIVE_PROJECTS.md: live projects only, with the next action.
- 06_OFFERS_AND_MONEY.md: pointer to the money/offer/pricing engines, and what is blocked.
- 07_CREATIVE_ENGINE.md: the AI film/image stack (doctrines plus four skills).
- 08_PRODUCTION_ENGINE.md: the photo/post stack (Lightroom OS, v3 LUXURY grade, four skills).
- 09_KNOWLEDGE_INDEX.md: the retrieval index and query guide (two-index reality).
- 10_SKILLS_INDEX.md: the skill ecosystem map and the 7-skill migration.
- 11_MEMORY_AND_HANDOFFS.md: the dual-root memory map and handoff patterns.
- 12_BACKUP_AND_REPO_PROTOCOL.md: git, backup scope, and the broken-hook fix.

## Open architectural calls (flagged, NOT yet resolved)

Do not assume these are done. Each needs operator approval (detail in the named file).

1. Broken session-start hook (12_BACKUP_AND_REPO_PROTOCOL.md): os_session_start.sh searched a nonexistent `00_BRIEF` directory and fell back to STALE SNIPED_OS state (May 29). Fixed in Phase 1 (2026-06-14): the search now points at 00_COMMAND_CENTER, so the boot reads the fresh Jun 10 NEXT_ACTION. STANDING_ORDER still falls back to SNIPED_OS until a Refinery copy is created in Phase 2.
2. Canonical state winner (01_CURRENT_STATE.md): the Refinery Jun 5/Jun 10 state vs the SNIPED_OS May 31 state encode different brand containers. Designating a winner forces the SNIPED-vs-BASEPLATE identity decision.
3. 7-skill migration (10_SKILLS_INDEX.md): sniped-article, sniped-command-router, sniped-decide, sniped-operator-plan, sniped-os-execution-governor, sniped-project-ingestion, sniped-skill-intake resolve only from SNIPED_OS/_skills. Migrate them into .claude/skills so no skill loads from Downloads.
4. Memory split-brain (11_MEMORY_AND_HANDOFFS.md): TWO populated memory stores with different content exist on disk. Reconcile (merge, keep both, or deprecate one) by operator decision, after reading both.

When in doubt, prefer the freshest Refinery state and the operator's live instruction over any older doc, and surface the open call rather than guessing.
