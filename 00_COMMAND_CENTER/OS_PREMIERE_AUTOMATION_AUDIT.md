# OS Premiere Automation Audit

> **PROOF UPDATE 2026-06-06: ACTIVE at READ + PROJECT-WRITE tier.** Read proof 2026-06-05 (PREMIERE_MCP_PROOF.md: ping/version/project/state). Write proof 2026-06-06: `create_bin('OS_PROOF_BIN')` -> `get_project_info` (numItems 0->1) -> `delete_bin` (deleted). Reversible, project left clean, no save-over, no asset, no spend. Bridge is now the real-copy CEP panel (not the symlink). SEQUENCE/EXPORT sub-tier still UNPROVEN: `create_sequence` errors "Not Enough Parameters" on Premiere 26.2.2 (needs a preset) -> prove via `create_sequence_from_preset` + a tiny export before claiming timeline/render. Route status in OS_VIDEO_EDIT_ROUTE_MATRIX.csv = ACTIVE-WRITE-PROVEN.

> CORRECTION 2026-06-05 (operator transcripts): Premiere IS directly automatable via the **Premiere Pro MCP** (GitHub, 269 tools) + the **MCP Bridge** CEP extension (Window > Extensions > MCP Bridge). With a project open + the bridge running + a refreshed Claude session, Claude drives Premiere directly: remove silences, transcript bad-take cutting, rough cut from scenes, ripple/roll/slip/slide, move clips to tracks, A-roll/B-roll organization, captions, effects/preset search, bulk rename + color, export/render, and save reusable edit skills. This SUPERSEDES the "headless-blocked -> handoff" verdict below. Headless (no-GUI) render remains the only blocked part; FCPXML/EDL is a secondary bridge. The 269-tool Premiere MCP is the PREFERRED max-edit route (status NEEDS_INSTALL until cloned). Adobe's official "Adobe for Creativity" connectors are NOT this: they drive Adobe Express only (~50 tools, cannot edit video).

> BRIDGE-NOT-VISIBLE FIX 2026-06-05 (operator opened Premiere 2026; Window>Extensions showed only "Film Impact Dashboard", no MCP Bridge). Diagnosis: CEP runtime WORKS in this Premiere 2026 (Film Impact is a CEP panel, PlugPlug.framework present), PlayerDebugMode=1 for CSXS 9-14, manifest targets PPRO [14.0,99.9] (Premiere 2026 qualifies), RequiredRuntime CSXS 9.0. Root causes: (1) install-cep used a SYMLINK ("development mode") and macOS CEP frequently refuses to load symlinked unsigned extensions; (2) Premiere was running during install. FIX APPLIED: replaced the symlink with a REAL COPY at ~/Library/Application Support/Adobe/CEP/extensions/MCPBridgeCEP (panel id com.mcp.premiere.bridge.panel, Menu "MCP Bridge"). REMAINING MANUAL: fully QUIT Premiere (Cmd+Q) and relaunch, then Window>Extensions>MCP Bridge -> set temp dir /tmp/premiere-mcp-bridge -> Start Bridge -> NEW Claude session -> read project info. Status stays PENDING-PROOF (not ACTIVE) until that proof exists; then write PREMIERE_MCP_PROOF.md and the router flips ACTIVE. If after a full relaunch it still does not appear, Premiere 2026 may require a UXP build of the bridge (CEP deprecated) , but Film Impact loading as CEP suggests CEP still works here.

Audited 2026-06-05 (read-only, no GUI launch). Question: can the OS control Premiere automatically?

## Install
- Premiere Pro 2026 INSTALLED: `/Applications/Adobe Premiere Pro 2026/Adobe Premiere Pro 2026.app`. (Corrects the earlier stale "not installed" assumption.)

## Automation routes checked
| Route | Result |
| --- | --- |
| Headless CLI render | NO. Premiere has no supported command-line/headless render (unlike aerender). |
| ExtendScript (.jsx) | Possible only with the GUI app running and scripting driven via the app; not reliable unattended. |
| UXP / CEP panel | CEP extensions dir exists (`/Library/Application Support/Adobe/CEP/extensions`, ccx.start only). No custom automation panel installed. Building one is a project, still requires the app open. |
| Create/import a project programmatically | NOT natively. But Premiere OPENS interchange formats. |
| FCPXML / EDL / Final Cut XML | YES. The OS generates FCPXML 1.9 and CMX3600 EDL (os_video_edit_router.py fcpxml/edl), both Premiere-openable. PROVEN in the selftest. |
| Adobe video MCP (cloud) | quick_cut / video_resize callable after asset upload (separate route #2). |

## Verdict
DIRECT_PREMIERE_AUTOMATED = **BLOCKED** (no headless control). 
PARTIAL AUTOMATED BRIDGE = **FCPXML/EDL generation** (PROVEN). The OS produces the finished video through the automated HYBRID route (HyperFrames + ffmpeg) and ALSO emits an FCPXML/EDL so the operator can open it in Premiere for an optional finishing pass. Premiere is an enhancement, never a dependency, never a default handoff.

## If direct Premiere control is wanted later
Build a UXP/CEP automation panel or an ExtendScript batch driven by `osascript` against the running app. This is a real build with low ROI versus the proven HYBRID route. Not required for AXIS.
