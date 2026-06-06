# OS Repo Integration Backlog

Survey 2026-06-05 (read-first). Status: ACTIVE / PREFERRED-PENDING / QUEUED / DISCARDED / SECURITY-HOLD.

| Repo / folder | Status | Reason | Setup needed | OS library affected | Cards | Gates/routes | Next action |
|---|---|---|---|---|---|---|---|
| ~/premiere-pro-mcp | ACTIVE-READ-PROVEN | 269-tool Premiere MCP; bridge LIVE + read-proof 2026-06-05 (PREMIERE_MCP_PROOF.md). Read tier ACTIVE; edit/export tier unproven | edit-and-export proof through os_premiere_compliance_gate for edit-tier | PREMIERE_MCP_OPERATOR | premc_* 13 | os_premiere_compliance_gate; video route #1 | run smallest edit-and-export proof when a real job needs it |
| ~/after-effects-mcp + Downloads/ae-mcp-setup | PREFERRED-PENDING | AE MCP built+registered; ScriptUI bridge manual | run setup-mac.sh / install-bridge, new session | AE_EXPRESSION_LIBRARY | aexp_* 5 | os_motion_qa; video route #3 | operator runs setup-mac.sh |
| ~/hyperframes | ACTIVE | proven HTML->mp4 title spine | none | (HYBRID spine) | - | video route #4 | use in edits |
| ~/remotion | QUEUED | programmable React video (data-driven MG); large, not yet wired | npm install in a project | (video route #4) | - | video route #4 (programmable) | scaffold a Remotion title comp when needed |
| ~/video-use | ACTIVE (cards) | conversational ffmpeg edit skill | install skill | VIDEO_USE_EDIT | vuse_* 8 | os_premiere_compliance_gate; route #5 | run a proof edit later |
| ~/matts-peeker | QUEUED | video inspect (frames+transcript) | install skill | (QA) | - | feeds os_vision_gate | card when a clip-QA need arises |
| ~/Blender-MCP-Assembly-Skill | ACTIVE (cards) | geometry correctness | none | BLENDER | blasm_* 4 | os_blender_gate | apply on Blender builds |
| ~/world-builder | AMBER | reference->scene; needs fal spend | fal key | BLENDER | wbld_* 2 | os_world | run 1 scene on approval ($) |
| ~/Downloads/cc-motion-tracking-blender | QUEUED (carded) | camera-track 3D into footage | Blender | BLENDER | ccbl_motion_tracking | os_blender_gate | use for 3D-over-plate |
| ~/Downloads/cc-blender-environments | QUEUED (carded) | atmospheric environments | Blender | BLENDER | ccbl_environments | os_world | use for sets |
| ~/taste-skill | ACTIVE (cards) | anti-slop design | none | FIGMA | taste_* 4 | elite_art_direction | apply on decks |
| ~/Documents/BJ-WIKI/impeccable | QUEUED | design vocabulary (front-end) | read | FIGMA | - | elite_art_direction | mine 2-3 cards later |
| ~/Documents/BJ-WIKI/awesome-design-md | QUEUED | DESIGN.md collection | read | FIGMA | - | - | reference; taste covers gate |
| ~/Documents/BJ-WIKI/elevenlabs-mcp | PREFERRED-PENDING | official ElevenLabs MCP (voice/TTS/clone) | uvx + API key (Agents write scope) | ELEVENLABS_OPERATOR | elv_* 7 | os_sound_gate | operator provides key -> register -> new session |
| ~/Documents/BJ-WIKI/openclaw | SECURITY-HOLD | 1.6G; "openclaw" unclear provenance | read-only audit before any run | - | - | - | audit before integrating; do not run |
| ~/n8n-skills | QUEUED (carded) | n8n workflow skills | read | N8N_AUTOMATION | n8n_* 2 | none | wire booking flow on approval |
| ~/n8n-mcp | QUEUED (carded) | manage n8n via Claude | self-host or cloud n8n | N8N_AUTOMATION | (n8n_mcp_route) | none | stand up n8n when SDR built |
| ~/self-hosted-ai-starter-kit | QUEUED | self-host n8n+models | docker | N8N_AUTOMATION | - | none | host n8n locally if needed |
| ~/cli (googleworkspace) | QUEUED (carded) | Google Workspace CLI | auth | GOOGLE_WORKSPACE_AUTOMATION | gws_* 2 | none | use for calendar booking |
| ~/autoresearch | QUEUED | research automation (audit-offer fuel) | read | AI_AUDIT_OFFER | - | none | wire research-first audit |
| ~/claude-code | QUEUED | Claude Code source/reference | read | - | - | - | reference only |
| ~/skills | QUEUED | Anthropic standard skills (doc-gen) | install per-skill | - | - | - | use for deck/PDF gen |
| ~/superpowers | ACTIVE (2 cards) | dev methodology | none | (claude) | sp_* 2 | none | rest queued |
| ~/unreal-mcp | QUEUED/RED | Unreal control; games lane not active | - | - | - | mcp.unreal RED | defer |
| ~/ClaudeBusiness | QUEUED | agentic-entrepreneurship docs | read | MONEY | - | - | mine money cards later |

## Security-hold note
- openclaw (1.6G, ambiguous name/provenance) , READ-ONLY audit before any execution. Do not npm/pip/run until audited. (Pattern discipline after the Adobe-Premiere malware.)

## Newly carded this pass (+23, store 1010): aexp_* (5 AE), elv_* (7 ElevenLabs), vagent_* (3 voice agent), n8n_* (2), gws_* (2), audit_* (1), sagent_* (1), ccbl_* (2).
