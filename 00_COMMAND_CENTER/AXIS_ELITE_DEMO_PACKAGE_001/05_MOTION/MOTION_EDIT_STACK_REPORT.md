# MOTION-EDIT STACK REPORT (mandatory)
## Route assessment (checked, not assumed)
- Premiere Pro 2026: INSTALLED (/Applications/Adobe Premiere Pro 2026). BUT no safe headless/CLI authoring path , Premiere is GUI-only for edit assembly; launching it to script an edit risks a hung GUI session. NOT used this pass (route present, not callable headlessly).
- After Effects 2026 (aerender 26.2.1x2): INSTALLED. aerender RENDERS an .aep; it cannot AUTHOR a comp from CLI. Authoring needs an .aep template + GUI ExtendScript. NOT used this pass (would need a templated .aep).
- HyperFrames 0.6.74: ACTIVE + CALLABLE + scriptable (headless Chrome + ffmpeg). USED , this is the strongest callable premium route for kinetic type / titles / motion graphics. Rendered the intro + end-card title system (GSAP kinetic type, 1080x1920).
- Adobe cloud video (mcp.adobe quick_cut/video_resize): available but AI-reel/async + needs upload; not the right control for an authored title edit. Considered, not used.
- ffmpeg: ASSEMBLY/EXPORT support layer only (concat, scale, caption-safe, fades). Not the creative editor.
- Motion content (beats): Higgsfield Seedance 1080p i2v , premium generation (beat A push-in/approved + beat B gesture: closes ledger, looks up).

## Verdict: NOT ffmpeg-only. Premium motion route = HyperFrames (titles, kinetic type) + Seedance (beats). Premiere/AE present but not headless-authorable this pass (logged, not faked). ffmpeg = assembly only.

## Edit plan
Shot order: INTRO TITLE (HyperFrames, AXIS kinetic) -> BEAT A (wide push-in) -> BEAT B (gesture: closes ledger, looks up) -> END CARD (HyperFrames, MERIDIAN HOUSE / what we'd build).
Title system: display-serif masthead + grotesk kicker + oxblood rule + italic sub; GSAP fades/rises.
Transition logic: hard cuts between beats (editorial); cross-fade titles in/out (0.4s).
Pacing: title 3.6s (let it breathe) -> beats 5s each (hold the hero) -> end card 3.7s. ~17s.
Caption-safe: lower third kept clear; safe margins on 9x16.
Export specs: 1080x1920 (9:16) primary, muted (AI audio off; sound is the honest gap); plus a 16:9 crop for landscape review.
