# OS Tool Repo Integration Matrix

Pass: TOOL REPO INTEGRATION + PREMIERE MCP ACTIVATION, 2026-06-05 (commit pending). Boot loaded first (commit 53a3ff6, 12/12 artifacts). No creative run, no spend. Convert-if-safe-relevant-proven, not inventory.

| Repo | What it is | Class | Relevance | Status | Action taken |
| --- | --- | --- | --- | --- | --- |
| premiere-pro-mcp | 269-tool Premiere MCP (the real one) | MCP | REQUIRED | **PREFERRED-PENDING** | npm install + build; registered with Claude Code (connected); CEP bridge installed. Manual + new session remain. |
| after-effects-mcp | AE MCP (comps/layers/anim/render) | MCP | USEFUL | **PREFERRED-PENDING** | npm install + build; registered (connected). ScriptUI bridge install MANUAL (classifier-blocked, correct) + new session. |
| hyperframes | HTML->mp4 title/card render | INSTALLABLE | USEFUL | **ACTIVE** | already proven (HYBRID edit spine); source repo present; no change needed. |
| video-use | conversational ffmpeg+PIL editor (Claude skill) | SKILL-LIBRARY | USEFUL | INTEGRATED (cards) | 8 edit-correctness cards (vuse_*) extracted; registered skill.video_use (AMBER, no proof edit yet). |
| matts-peeker | video inspect: frames + transcript -> package | SKILL-LIBRARY | OPTIONAL | QUEUED | video-understanding/inspection; useful for QA of generated clips; card later. |
| superpowers | dev methodology + composable skills | SKILL-LIBRARY | USEFUL | INTEGRATED (2 cards) | sp_verify_before_done, sp_parallel_agents carded; rest QUEUED (OS-dev, not campaign). |
| Blender-MCP-Assembly-Skill | Blender geometry correctness | SKILL-LIBRARY | USEFUL | INTEGRATED (cards) | 4 cards (blasm_*); skill.blender_assembly ACTIVE (feeds os_blender_gate). |
| taste-skill | anti-slop frontend/design taste | SKILL-LIBRARY | USEFUL | INTEGRATED (cards) | 4 cards (taste_*); skill.taste ACTIVE (feeds FIGMA + elite gate). |
| awesome-design-md | curated DESIGN.md collection | DOC-ONLY | OPTIONAL | QUEUED | design reference; taste-skill already covers the gate; mine later. |
| shannon | autonomous AI web pentester | MCP/app | IRRELEVANT (now) | DISCARD-FOR-LANE | security pentesting, not campaign-house; keep only if securing own site later. |
| skills (Anthropic) | standard doc-gen skills (docx/pdf/pptx/xlsx) | SKILL-LIBRARY | USEFUL | QUEUED | available for deck/one-sheet/PDF generation; reference. |
| ClaudeBusiness | agentic-entrepreneurship frameworks | DOC-ONLY | OPTIONAL | QUEUED | adjacent to existing money layer; mine for money cards later. |
| unreal-mcp | Unreal Engine MCP control | MCP | OPTIONAL | PENDING | games/3D lane not active; registered mcp.unreal RED; queued. |
| world-builder | reference image -> full Blender scene (MCP) | INSTALLABLE/skill | USEFUL | INTEGRATED (cards) | 2 cards (wbld_*); skill.world_builder AMBER (needs fal ~$4-6/world spend). |
| astro | website build framework | INSTALLABLE | OPTIONAL | QUEUED | landing pages; Vercel/hosting held; use when web surface is approved. |
| Adobe-Premiere-Pro-Version-2026 | pirated/"no limits" lure w/ payload zip | SUSPICIOUS | **DISCARD** | **DELETED** | malware pattern (README: "turn off antivirus"; single .exe/zip payload from throwaway account). rm -rf'd on operator go. |

## ACTIVE (route + artifact + log + gate + repeat proven)
- skill.blender_assembly, skill.taste (doctrine cards live + feed existing ACTIVE gates/routes), tool.hyperframes (proven render).

## PREFERRED-PENDING
- mcp.premiere (built + registered + CEP installed; needs Premiere open + bridge Start + new session).
- mcp.after_effects (built + registered; needs ScriptUI bridge install [manual] + new session).

## QUEUED (with reason)
- matts-peeker (video inspect, card later), awesome-design-md (design ref, taste covers gate), skills (doc-gen, reference), ClaudeBusiness (money ref), astro (web, hosting held), unreal-mcp (games lane not active), superpowers-remainder (OS-dev skills).

## DISCARDED
- Adobe-Premiere-Pro-Version-2026 (malware, deleted). shannon (irrelevant to campaign lane; not deleted, just not integrated).

## New cards (+20): vuse_* (8), blasm_* (4), taste_* (4), wbld_* (2), sp_* (2). Store now ~987.
