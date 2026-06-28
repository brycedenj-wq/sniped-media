# OS_TOOL_ROUTING_STANDARD (permanent)

Installed 2026-06-27 by operator directive. Applies to every tool decision in every project, forever.

## The law

**Capability unavailable through MCP does not mean capability unavailable.** A connector limit is a small-minded tool limit, not a production standard. The manual professional route beats automated slop every time. Claude's job is to route, specify, prepare, and keep building. BJ's manual pass in a pro app is part of the premium workflow, not a failure.

Do not say "Adobe cannot be used" when only the connector is limited. Do not settle for the callable tool when a manual Firefly / Photoshop / Illustrator / Lightroom / InDesign / Blender pass is the better route. Do not proceed with slop because it is callable. Do not grade slop as if it is excellent.

## Every tool decision must state five things

1. **Best professional route.** What an excellent operator would use if quality were the only standard.
2. **Callable route.** What Claude can execute directly through MCP/tools right now.
3. **Manual/operator route.** What BJ must do by hand in the app if the MCP is limited or worse.
4. **Exact operator recipe** (when manual is better, give all of it):
   - app / tool
   - source file to open (absolute path)
   - exact prompt or setting
   - reference image(s) (absolute paths)
   - model or mode
   - crop / aspect
   - seed / variation logic if relevant
   - export format
   - destination folder path
   - naming convention
   - acceptance criteria (what a pass looks like)
   - what to reject
   - how to bring the result back into the build
5. **Continue-without-waiting work.** While the manual step is pending, keep building everything that does not depend on that asset.

## The approval boundary

Do not spend credits or drive the operator's accounts/apps without approval. But do not stop the system because a step needs manual excellence. Bring the operator an exact approval line ONLY when credits or account actions are about to happen. Everything else continues.

## The standing routing table (defaults, override per artifact)

| Artifact | Best professional route | Callable now | Manual-best route |
|---|---|---|---|
| Photoreal hero still | Firefly (reference-image) or Higgsfield, then Photoshop finish | Higgsfield generate_image (spend) | Firefly web reference-gen + Photoshop grade |
| Upscale / super-res | Higgsfield upscale, or Photoshop/Topaz | Higgsfield upscale_image (spend) | Topaz / PS Super Zoom |
| Color grade | Lightroom / Camera Raw masked | Adobe connector image_adjust_* (coarse) | Lightroom/ACR masked grade |
| Interior generative fill / text | Firefly generative fill (web/app) | connector: image_generative_expand (edge only) | Firefly web fill, Photoshop generative fill |
| Vector mark / wordmark / seal | Illustrator true vector | connector image_vectorize (rough) | Illustrator pen + type |
| Label / packaging print layout | InDesign | Figma (screen layout) | InDesign print-true |
| 3D product form | Blender | blender MCP (if running) | Blender by hand |
| Screen design / mockup | Figma | Figma MCP + plugin | Figma by hand |
| Web / landing build | hand-coded or Next on Vercel | local-code (Bash/Write) | operator deploy |

## Why

The artifact does not define the OS; the quality bar does. A premium universe is built by routing each asset to the route that makes it excellent, doing the callable parts now, writing the operator the exact recipe for the manual parts, and never letting a callable-but-worse path lower the bar. See `OS_TOOL_APP_INTEGRATION_LEDGER.csv` for live tool readiness and the capability audit at `THE_HOUSE/BUILD/_capability_audit/`.
