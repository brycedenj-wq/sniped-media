# OS After Effects Automation Audit

Audited 2026-06-05. Question: can the OS render titles / motion-graphics automatically?

## Install
- After Effects 2026 INSTALLED: `/Applications/Adobe After Effects 2026`.
- aerender CALLABLE (headless): `/Applications/Adobe After Effects 2026/aerender` (registry: PROVEN aerender 26.2.x).

## Automation routes checked
| Route | Result |
| --- | --- |
| aerender headless render of a comp | YES. `aerender -project x.aep -comp "name" -output out.mov`. |
| Build comp programmatically then render | YES via `aerender -r build.jsx` (ExtendScript builds comp + text + render). Headless. |
| Template .aep on disk | NONE yet. This is the one missing input. |
| Card library depth | THIN (3 AE cards, Remotion-leaning). Real corpus gap; AE motion-design doctrine is sparse. |

## Verdict
AFTER_EFFECTS_AUTOMATED = **AVAILABLE / FULL_AUTO capable**, gated on one build item: a template `.aep` or a `build.jsx`. Until that exists, titles route through HyperFrames (HTML -> mp4), which is already proven.

## Update 2026-06-05 (ae-mcp-setup + AE cards)
- `~/Downloads/    SNIPED_OS/ae-mcp-setup` provides setup-mac.sh: clones the AE MCP, npm install+build, installs the bridge ScriptUI panel, configures Claude Code. Operator runs it (app-modifying installer; classify before running). after-effects-mcp already built + registered (Connected).
- AE library thickened from 4 -> with AE_EXPRESSION_LIBRARY cards (aexp_*): mcp_setup, expressions, responsive text boxes (sourceRectAtTime), wiggle/loop patterns, aerender render route.
- Automatable directly: expressions, comp/layer build, render (aerender). Handoff/manual: the ScriptUI bridge install + new session.

## Role in AXIS
Secondary title / motion-graphics engine. Use AE via aerender when a title needs heavier motion-design than HyperFrames gives. Build a reusable `titles.aep` (or `titles_build.jsx`) once, then it is fully automated. Do NOT claim AE-grade motion-design without a real comp rendered.
