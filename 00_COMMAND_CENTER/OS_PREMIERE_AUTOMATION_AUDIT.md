# OS Premiere Automation Audit

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
