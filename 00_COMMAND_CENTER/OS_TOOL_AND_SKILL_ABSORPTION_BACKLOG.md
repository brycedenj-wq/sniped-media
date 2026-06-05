# OS TOOL AND SKILL ABSORPTION BACKLOG
### Everything not yet fully absorbed, ranked by ceiling lift x money impact
Built: 2026-06-05 (total integration pass). An item leaves this list only when it has route + artifact + log + gate + repeat, or is marked DEFERRED by choice.

Absorption state legend:
- **ABSORBED** , in router/workflow/gate/dashboard with proof.
- **PARTIAL** , connected + a route exists, but the value half is untested (the unblock is named).
- **DEFERRED** , intentionally parked (handoff env, or held by safety mandate).

---

## Tier 1 , highest ceiling + money impact (do next)

| Item | State | The exact unblock | Why it matters |
|---|---|---|---|
| Airtable write route (`track_leads`) | PARTIAL | run `create_records_for_table` on a test base, log record id | turns CRM/forecast from read-only to a live revenue dashboard |
| Adobe asset-dependent ops (remove_bg, select_subject, retouch, generative_expand) | PARTIAL | one full `os_adobe_cloud` handshake on the DEED asset, then call the op | unlocks the cloud post-production half (mockups, masks, outpaint) |
| Real responsive HTML host for `build_private_demo` | PARTIAL/DEFERRED | web-artifacts-builder is HANDOFF (claude.ai app); or build a local static export | the private demo is the closing asset; today it ships as static PNG |
| Blender world build (`build_world_3d`) at production depth | PARTIAL | run one real environment from the 7-rotation through gate -> render -> persist | 3D world-construction is the IG creative-engine moat |
| Notion CRM write (build the 5-DB) | PARTIAL | create the 5 databases + dashboard page via `notion-create-database` | the operator dashboard that runs the office |

---

## Tier 2 , real lift, lower urgency

| Item | State | Unblock |
|---|---|---|
| AE motion/title comp | PARTIAL | author one `.aep`, run `aerender` to a frame |
| Adobe quick_cut / video_resize / media ops | PARTIAL | upload one test video asset, run the op |
| Figma design read/write | PARTIAL | open a live file, run `get_design_context` -> `use_figma` |
| HyperFrames render at depth | ABSORBED (env ok) | optional: start Docker for containerized render |
| Higgsfield image/video at depth | ABSORBED | spend-gated; proven; scale on approval |
| Adobe layout/vector/pdf render | PARTIAL | run `document_render_layout` on a sample |

---

## Tier 3 , deferred by choice (handoff or held)

| Item | State | Reason |
|---|---|---|
| Claude app skills (canvas, web-artifacts, theme-factory, brand-guidelines, skill/mcp-builder) | DEFERRED | run in claude.ai app; mcp-builder is the path to bridge plugins into CLI later |
| Plugins (twilio, zapier, zoominfo, adspirer, pdf-viewer, desktop-commander, product-tracking, brand-voice, biz-skills) | DEFERRED | HANDOFF to app; zapier/adspirer also spend/risk gated |
| Vercel / Netlify deploy | DEFERRED (HELD) | no hosting/public action by mandate; Netlify also needs OAuth |
| Gmail send / outreach | DEFERRED (HELD) | draft-only; no send without explicit go |
| Payment / legal finalization | DEFERRED (HELD) | follows proof; never auto |
| Semrush data | DEFERRED (RED) | plan excludes MCP access; unlock at semrush.com/mcp-access |

---

## Router-level refinements found this pass (cheap, high-clarity)

- `os_prime_router` has no explicit `ops/crm` or `campaign` module , "track leads" and "make campaign package" fall through to `strategy`. The `os_tool_router` catches both correctly, but adding triggers would make the two routers agree. LOW effort.
- Native Blender renders to the MCP server temp dir, not an arbitrary path , the OS must copy the artifact into the sandbox. Documented in the registry note; consider a tiny `os_blender_persist` helper. LOW effort.
- Adobe upload requires the `os_adobe_cloud` handshake (no file picker in CLI) , this is the gating dependency for ~8 Adobe capabilities. Proving it once on a real asset flips multiple Tier-1/2 items at once. HIGH leverage.

---

## The one move that unblocks the most

Run a single `os_adobe_cloud` upload handshake on the DEED asset and execute `image_select_subject` + `image_remove_background`. That one proof converts 4+ Adobe capabilities from PARTIAL to ABSORBED and is the highest leverage item on this list.
