# OS_ROUTER_INDEX , domain → what to pull (the router reads THIS, not everything)

> The router consults this map to pull ONLY the relevant doctrine doc / skill / chunk-index for a task. Keep it small. Tag each entry `active` / `superseded` / `hypothesis`. The router ignores `superseded` by default.

## How to use
Request → classify domain → pull the listed doctrine doc(s) + skill(s). For evidence, pull chunk ids via `01_KNOWLEDGE_BASE/MASTER_INDEX.md` → `batches/*_CHUNKS.jsonl`. Never bulk-load.

## Domains
| domain | doctrine (pull one) | skills (invoke) | chunk index | status |
|---|---|---|---|---|
| corpus certification | OS_CERTIFICATION_STANDARD, OS_CERTIFICATION_REPORT | os_certify, os_segment_ledger, os-token-safe-reader | , | active |
| AI image / composite | OS_DOCTRINE_BATCH_007/008/011/012, OS_CAPABILITY_TOOL_ROUTING | sniped-crs-builder, os-face-lock, kling-production-sop | batch_006/007 | active |
| AI video / motion | OS_CAMPAIGN_HOUSE_PIPELINE | kling-production-sop, os_motion_qa, os_motion_ready | , | active |
| character + world | OS_PHASE1_ATOM, OS_PHASE3_FACELOCK | sniped-crs-builder, os-world-bible, os-face-lock | , | active |
| production harness | OS_CAMPAIGN_HOUSE_PIPELINE | os_production, os_batch, os_generate | , | active |
| brand / positioning | OS_DOCTRINE_REREAD_C_*, intel_positioning_phrases (memory) | brand-validation-machine | persuasion/positioning | hypothesis |
| outreach / sales | OS_DOCTRINE (VIB), feedback_use_outbound_stack (memory) | sniped-vib-outreach (drafted) | cold_email | hypothesis |
| content / distribution | OS_STARTHERE_* (Content-Marketing OS) | hit-mechanics (drafted) | , | active |
| Claude / automation | OS_CLAUDE_OPERATING_MANUAL, OS_BOOTLOADER_ARCHITECTURE | os-command-router, os-quality-gates | claude_operator | active |
| skill lifecycle | feedback_skill_activation_contract (memory) | os_skill | , | active |
| books / strategy classics | OS_DOCTRINE_REREAD_* / BOOKWAVE_* | , | batches/*_extracted | provisional (no segment ledger) |

## Notes
- `provisional` / `hypothesis` doctrine: usable as input, NEVER as settled fact. Attach the tag when citing.
- Update this index when a new certified doctrine doc or ACTIVE skill is added. Keep it under ~30 rows; it is a router map, not a catalog.
