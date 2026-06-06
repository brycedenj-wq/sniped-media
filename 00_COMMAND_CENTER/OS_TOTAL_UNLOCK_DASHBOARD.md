# OS TOTAL TOOL / REPO / SKILL UNLOCK DASHBOARD

> Pass date: 2026-06-06. Mission: operationalize everything already added before picking the next play.
> AXIS is retired as a target (weak stress-test artifact). No spend, no generation, no creative artifacts this pass.
> ACTIVE bar = route + artifact/log + gate + repeat. Nothing is called ACTIVE without all four.

## Classification legend
1. ACTIVE , proven (route + artifact/log + gate + repeat)
2. PREFERRED-PENDING , one exact manual step away
3. QUEUED , useful, deferred with reason
4. DISCARDED , with reason
5. SECURITY-HOLD , with reason
6. DOCTRINE-ONLY , useful knowledge, not automatable here

---

## A. MASTER CLASSIFICATION TABLE (every repo/source)

| # | Target | Path | Lane | Class | Proof / exact next step |
|---|--------|------|------|-------|--------------------------|
| 1 | premiere-pro-mcp | ~/premiere-pro-mcp | video-edit | **ACTIVE (read+project-write)** | read proof (PREMIERE_MCP_PROOF.md) + write proof (bin create/verify/delete 2026-06-06). Sequence/export sub-tier pending preset+render proof |
| 2 | after-effects-mcp | ~/after-effects-mcp | motion-gfx | **ACTIVE (read)** | live-proven 2026-06-06: operator installed+opened panel; getProjectInfo->get-results returned live state (Untitled Project, 8bpc). Authoring tier (comp/layers/keyframes) available, unproven |
| 3 | remotion | ~/remotion | motion-gfx | **PREFERRED-PENDING** | source monorepo only (node_modules empty). `npx create-video@latest` in a sandbox + `npx remotion render` to prove. Cards extracted |
| 4 | hyperframes | ~/hyperframes | motion-gfx | **PREFERRED-PENDING** (render) | source monorepo; ffmpeg spine already ACTIVE. `npx hyperframes init` + lint to prove HTML->mp4 render. Cards extracted |
| 5 | video-use | ~/video-use | video-edit | **PREFERRED-PENDING** | skill present, deps not installed, needs ELEVENLABS_API_KEY (paid Scribe). `uv sync` + `.env` key. Cards extracted |
| 6 | matts-peeker | ~/matts-peeker | video-analysis | **ACTIVE (no-key frame mode)** | `peeker.py --help` runs (stdlib). Frame-extract works keyless; vision needs OPENROUTER_API_KEY. /peek skill |
| 7 | Adobe video MCP | claude.ai Adobe for creativity | video-cloud | **AVAILABLE-CONDITIONAL** | connected; video tools require asset upload to Adobe cloud first. Express-only, cannot edit Premiere |
| 8 | ffmpeg | system | video-spine | **ACTIVE** | spine + fallback; HYBRID selftest passed prior (3-clip, no credits) |
| 9 | n8n-mcp | ~/n8n-mcp | workflow-automation | **PREFERRED-PENDING** | dist/ built. `claude mcp add n8n-mcp -- node ~/n8n-mcp/dist/mcp/index.js` (stdio, no n8n instance needed for node knowledge) + new session |
| 10 | n8n-skills | ~/n8n-skills | workflow-automation | **PREFERRED-PENDING** | 7 skill packs in dist/. Register skill paths. Cards extracted |
| 11 | self-hosted-ai-starter-kit | ~/self-hosted-ai-starter-kit | workflow-automation | **QUEUED** | requires Docker (n8n+Ollama+Qdrant+Postgres). `docker compose config` dry-run only until a Docker decision |
| 12 | ElevenLabs MCP | (not cloned) uvx elevenlabs-mcp | voice | **PREFERRED-PENDING** | not registered. Create API key WITH "11 Agents" write scope -> `claude mcp add ElevenLabs -e ELEVENLABS_API_KEY=<key> -- uvx elevenlabs-mcp` + new session |
| 13 | elevenlabs-mcp (BJ-WIKI) | ~/Documents/BJ-WIKI/elevenlabs-mcp | voice | **QUEUED** | nested copy inside the vault; same activation as #12; do not double-register |
| 14 | Voice agent blueprint | OS knowledge base (.json) | voice/agent | **DOCTRINE + QUEUED** | ElevenLabs+Twilio outbound-call n8n workflow. Networked/dangerous (real calls, public webhook). Build behind n8n; carded |
| 15 | Google Workspace CLI (gws) | ~/cli | workspace-automation | **QUEUED** | not installed; redundant for now with connected Google Calendar/Gmail/Drive MCP. Use MCP for booking; revisit gws for batch |
| 16 | Figma MCP (x2) | plugin:figma + figma-desktop | design | **ACTIVE (read)** | both connected. Read/inspect/generate available. figma-use skill mandatory before writes |
| 17 | awesome-design-md | ~/awesome-design-md | design-system | **ACTIVE (doctrine)** | 72+ DESIGN.md specs; copy into project root as DESIGN.md. Zero execution surface |
| 18 | impeccable | ~/Documents/BJ-WIKI/impeccable | design-quality | **PREFERRED-PENDING** | built (bun.lock). 23-cmd skill + deterministic `npx impeccable detect` (no key). Register skill. Cards extracted |
| 19 | taste-skill | ~/taste-skill | taste-eval | **PREFERRED-PENDING** | SKILL.md present (3-dial system). `npx skills add` or copy SKILL.md. Cards extracted |
| 20 | world-builder | ~/world-builder | world-build/3d | **QUEUED** | needs blender-mcp binary install + FAL_KEY (~$6-10/world) + Blender open. analyze-reference sub-skill is keyless/free |
| 21 | Blender-MCP-Assembly-Skill | ~/Blender-MCP-Assembly-Skill | 3d-blender | **ACTIVE (doctrine)** | SKILL.md; Blender MCP already live, so loadable now on any geometry build. Cards extracted |
| 22 | cc-blender-environments | ~/Downloads/cc-blender-environments | 3d-blender | **DOCTRINE-ONLY** | community addon bootstrap; official blender_mcp already ACTIVE supersedes it. Env archetype cards |
| 23 | cc-motion-tracking-blender | ~/Downloads/cc-motion-tracking-blender | 3d-tracking | **DOCTRINE-ONLY** | community addon + sample assets; camera-solve technique cards. Official blender_mcp supersedes the bridge |
| 24 | blender_mcp | ~/blender_mcp | 3d-blender | **ACTIVE** | MCP connected + live read proof (get_objects_summary returned 9-object scene 2026-06-06). Official Blender Lab build |
| 25 | unreal-mcp | ~/unreal-mcp | 3d-unreal | **QUEUED (security-aware)** | experimental; requires C++ plugin compile (VS/Xcode) + UE 5.5. App-modifying. No proof until a real UE need |
| 26 | anthropics/skills | ~/skills | skills-source | **PREFERRED-PENDING** | `/plugin marketplace add anthropics/skills` then install. Trusted, Apache-2.0 |
| 27 | claude-code (source) | ~/claude-code | skills-source | **DOCTRINE-ONLY** | the running binary's source; reference for plugin/hook SDK. Not installed from source |
| 28 | superpowers | ~/superpowers | os-methodology | **PREFERRED-PENDING** | `/plugin marketplace add superpowers` + load using-superpowers bootstrap. High value for OS self-build |
| 29 | autoresearch | ~/autoresearch | research-automation | **DISCARDED (no GPU)** | requires NVIDIA GPU (H100-class); this Mac has none. Re-open only on GPU access |
| 30 | openclaw | ~/Documents/BJ-WIKI/openclaw | personal-assistant | **SECURITY-HOLD** | full messaging daemon, 20+ channel credentials on disk, cloud-deploy configs, auto-exec on inbound. No run without a credential+channel plan |
| 31 | ClaudeBusiness | ~/ClaudeBusiness | second-brain | **DOCTRINE-ONLY** | 6 markdown business-pattern docs. Ingest to BJ-WIKI. Infinity-Barrier + memory-arch cards |
| 32 | BJ-WIKI | ~/Documents/BJ-WIKI | second-brain | **ACTIVE** | live Obsidian Compound Vault (15 skills, 22k files, 1.5GB). Sync route below |
| 33 | shannon | ~/shannon | security-tool | **SECURITY-HOLD** | autonomous pentester, executes REAL exploits, Docker. Only authorized-target use. Not installed |
| 34 | astro | ~/astro | framework-source | **DISCARDED** | upstream withastro/astro framework source; not an OS tool. (May be a dep of impeccable/sniped-media) |
| 35 | money-demos | ~/money-demos | asset-folder | **N/A (assets)** | client/brand creative assets + 2 operator playbooks. Not a tool; index only |
| 36 | shannon/openclaw/autoresearch nested in BJ-WIKI | various | mixed | see #29/#30/#33 | inflate vault size; openclaw has own .git nested |

---

## B. WHAT BECAME ACTIVE THIS PASS (proof attached)
- **premiere-pro-mcp** , read-tier (prior) + **project-write tier proven today**: `create_bin` -> `get_project_info` (numItems=1) -> `delete_bin` (deleted). Reversible, project left clean, no spend.
- **blender_mcp** , live read proof today: `get_objects_summary` returned the full 9-object scene hierarchy. App live, addon polling.
- **matts-peeker** , runs on stdlib (`--help` verified); keyless frame-extraction mode is usable now.
- (Already ACTIVE and re-confirmed: ffmpeg spine, Figma read, Adobe MCP, Higgsfield, Airtable, Gmail/GCal/GDrive, Notion, Semrush, Vercel.)

## C. PREFERRED-PENDING (one exact step each) , see table col 6
remotion, hyperframes(render), video-use, n8n-mcp, n8n-skills, ElevenLabs MCP, impeccable, taste-skill, anthropics/skills, superpowers.
(after-effects-mcp graduated to ACTIVE-read this pass after operator installed+opened the panel.)

## D. QUEUED (with reason)
self-hosted-ai-starter-kit (Docker decision), gws (redundant w/ Google MCP now), world-builder (FAL cost + binary), unreal-mcp (C++ build), elevenlabs-mcp BJ-WIKI copy (dup), voice blueprint (needs full n8n+Twilio+webhook).

## E. DISCARDED (with reason)
autoresearch (no NVIDIA GPU on this Mac), astro (framework source, not an OS tool).

## F. SECURITY-HOLD (with reason)
openclaw (20+ live-channel credential daemon, auto-exec, cloud deploy), shannon (executes real exploits, authorized targets only). cc-* community Blender addons = inspect-before-run but superseded by official blender_mcp.

---

## G. NEW LIBRARIES / CARDS / ROUTES / GATES (this pass)
- Audits: OS_AFTER_EFFECTS_AUTOMATION_AUDIT.md, OS_REMOTION_AUTOMATION_AUDIT.md, OS_ELEVENLABS_MCP_AUDIT.md, OS_N8N_AUTOMATION_AUDIT.md; OS_PREMIERE_AUTOMATION_AUDIT.md updated (write-tier proof).
- Scripts: os_voice_agent_router.py (voice/SDR/booking route), os_audio_stack_gate.py (sound-lane readiness gate).
- Cards: appended to os_technique_cards.py (voice/n8n/design/taste/blender/world families) , curated from the 4-agent survey.
- Route matrix: DIRECT_PREMIERE_AUTOMATED -> ACTIVE-WRITE-PROVEN (project-item tier).
- Stale ledger: premiere (write tier), after_effects (panel-not-installed), blender (read-proven), + new voice-lane rows.

## H. VIDEO EDITING AUTOMATION STATUS
Route order (proof-based): **Premiere direct (ACTIVE read+project-write)** -> Adobe video MCP (cloud, conditional) -> After Effects (PREFERRED-PENDING, panel install) -> Remotion / HyperFrames (PREFERRED-PENDING render) -> video-use (PREFERRED-PENDING, key) -> **ffmpeg/HYBRID (ACTIVE spine + fallback)** -> CapCut (doctrine) -> handoff (only if all blocked).
Strongest fully-proven end-to-end TODAY = **HYBRID (HyperFrames-titles + ffmpeg assembly/export)**; Premiere is the preferred editable finish, now proven for read + project-write, with sequence/export still to prove.

## I. VOICE / AUDIO / AGENT AUTOMATION STATUS
Lane = **SEEDED, not yet live.** Knowledge fully carded (ElevenLabs build flow, VAPI/Retell SDR, n8n booking, Cal.com/GCal). Blockers: (1) ElevenLabs MCP needs API key with "11 Agents" write scope, (2) n8n-mcp needs registration, (3) the full SDR loop needs n8n + a public webhook + Twilio (networked/dangerous, behind explicit go). Router: os_voice_agent_router.py. Gate: os_audio_stack_gate.py. Music engine (Suno/Udio) still undecided.
GAP found: ElevenLabs **V3 emotional-tag syntax + subtle/moderate/aggressive modes + the exact "11 Agents" scope toggle** are NOT in the corpus , they live in ElevenLabs' own docs. Pull them when the key is created (carded as a known gap, not faked).

## J. DESIGN / WORLD / 3D STATUS
- Design: Figma read ACTIVE; awesome-design-md ACTIVE (doctrine); impeccable + taste-skill PREFERRED-PENDING (register). Strong taste layer available immediately.
- 3D Blender: **blender_mcp ACTIVE** (live proof) + Blender-MCP-Assembly-Skill loadable now. cc-* repos = doctrine.
- World-build: world-builder QUEUED (FAL cost); analyze-reference sub-skill is free.
- Unreal: QUEUED (C++ build).

## K. BJ-WIKI / SECOND-BRAIN STATUS
**ACTIVE** as the long-term second brain (Obsidian Compound Vault, 15 skills, hybrid retrieval). Rule: **BJ-WIKI = memory/knowledge (sources, synthesis, research); AI-Brain-Refinery = execution OS (routes, gates, scripts, proofs).** Sync route: OS_TO_BJ_WIKI_SYNC_PLAN.md + os_bj_wiki_sync.py. Do not nest execution daemons (openclaw) as OS capability; keep them isolated.

## L. EXACT MANUAL ACTIONS NEEDED FROM OPERATOR
1. ~~AE panel install~~ , **DONE 2026-06-06, AE now ACTIVE (read).**
2. **ElevenLabs**: create API key WITH "11 Agents" write scope -> `claude mcp add ElevenLabs -e ELEVENLABS_API_KEY=<key> -- uvx elevenlabs-mcp` -> new session. Pick Suno or Udio for music.
3. **n8n-mcp**: `claude mcp add n8n-mcp -- node ~/n8n-mcp/dist/mcp/index.js` -> new session (unlocks workflow build w/o an n8n instance).
4. **Skills/superpowers**: `/plugin marketplace add anthropics/skills` and `/plugin marketplace add superpowers`, then install.
5. **Docker decision** (only if you want the self-hosted AI kit): say go, then `docker compose config` dry-run first.
6. (Optional) register impeccable + taste-skill skills for the design lane.

## M. WHAT TO STOP THINKING ABOUT
- **AXIS** as a target , retired. It was a weak stress test, not the play.
- **autoresearch** , no GPU; not happening on this machine.
- **openclaw / shannon** , parked behind security; not part of the near-term unlock.
- **gws** , redundant while Google MCP is connected; stop treating it as the booking path.
- **unreal-mcp** , not until a real UE job exists.

## N. WHAT THE NEXT-LEVEL OS CAN DO NOW (post-unlock)
- Drive **Blender live** (proven) + **Premiere project-write** (proven) + **Figma read** + **Higgsfield/Adobe gen** + **ffmpeg/HYBRID render** = a real one-person production spine that READS and WRITES across the stack, not just generates.
- Analyze any video (matts-peeker) and feed timestamped understanding into edits.
- A **taste/design-quality layer** (impeccable + taste-skill + awesome-design-md) that judges and upgrades any UI/brand artifact.
- A **voice/SDR/booking department** that is one key away from live (router + gate + cards built).
- A **second brain** (BJ-WIKI) that compounds every source, distinct from the execution OS.

## O. SHORTEST PATH TO FULLY UNLOCKED
1. Operator runs the 4 quick activations (AE panel, ElevenLabs key, n8n-mcp add, plugin marketplaces) , ~20 min, no spend.
2. I prove each with the smallest sandbox call (AE getProjectInfo, ElevenLabs list-voices, n8n node search, one skill invoke).
3. Decide music engine (Suno/Udio) + whether Docker kit is wanted.
4. Then the only remaining "true max" gaps are: Premiere sequence/export proof (needs a preset), and one live voice-call test (behind go). Everything else is ACTIVE or doctrine.

## P. COMMIT
(filled at commit time below)
