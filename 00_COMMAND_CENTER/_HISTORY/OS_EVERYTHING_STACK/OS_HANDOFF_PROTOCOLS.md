# OS HANDOFF PROTOCOLS , tools installed elsewhere, exact handoff to use them
> "Installed somewhere else" is not a dead end. It is a handoff. Here is the exact path for each.

## Figma (Mac app + MCP, but app must be open)
Trigger: a job needs a real UI/design-system/dev-handoff. Steps: (1) open Figma.app and the target design file; (2) select the frame/page; (3) here, call figma get_metadata (no node) -> lists pages -> get_design_context/get_screenshot on a node. Proven failure mode today: app closed -> "Unable to connect." Artifact: a node screenshot or design-context code.

## Photoshop 2026 / Lightroom Classic (Mac desktop)
Trigger: hero-level manual retouch or a final master grade beyond the cloud MCP. Steps: (1) open the asset in PS/LR; (2) do the manual artistry (skin, dust, final curve); (3) export to the run folder; (4) here, register it through os_adobe_asset + run os_postproduction_gate. The OS automates everything up to the hero; the final hand-polish is a deliberate human handoff before a real sale.

## /web-artifacts-builder, /canvas-design, /theme-factory, biz skills (claude.ai app)
Trigger: a rich interactive HTML artifact or a domain workflow. Steps: run the skill IN the claude.ai app, export the HTML/asset, drop it into the run folder here, gate + privacy-scan it. (Local HTML + Chrome headless covers simpler landings without the handoff.)

## Desktop Commander (claude.ai app)
Trigger: you want to DRIVE a Mac desktop app (PS/Premiere) programmatically. Steps: use it in the app to script the desktop tool; bring the artifact back here. Note: this CLI already has Bash for local file/CLI ops, so Desktop Commander is only for GUI-app automation.

## Gmail / Twilio / ZoomInfo / Zapier / Adspirer (app / outbound)
Trigger: reaching a person or automating across apps. Steps: HELD by policy. When approved: draft in-app, you review, you send. Nothing outbound fires from here without your explicit go.

## Rule
Every handoff returns an artifact that re-enters the OS through a gate. A handoff is not done until its output is logged and gated here.
