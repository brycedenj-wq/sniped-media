# OS INCOMING TOOLS , integration map (2026-06-05)
> Four real tools entered the OS today, all closing gaps I named in the ceiling audit. Staged + documented. Activation steps + what each needs from you. Environment ready: Node v25, npm 11, ffmpeg, python3, After Effects 2026 installed, global ~/.claude/skills present.

## 1. video-use (Claude Code skill) , the REAL edit/trailer layer  [HIGHEST FIT]
- **What:** conversation-driven video editor. Transcribe (ElevenLabs Scribe) -> cut filler/dead-space -> per-segment grade + 30ms fades -> burn subtitles -> animation overlays (via HyperFrames/Manim/PIL in PARALLEL sub-agents) -> self-evaluate every cut -> persist project.md memory.
- **Why it matters:** it is built on the OS's own doctrine (ask->confirm->execute->iterate, hard production-correctness rules vs artistic freedom, self-verify before showing). It SUPERSEDES os_adobe_cut for real editing and gives a true multi-shot trailer with subtitles + sound discipline.
- **Unlocks:** real edited videos, cinematic trailers, social cutdowns, subtitle burn, parallel overlay generation.
- **Staged:** ~/Developer/video-use (helpers: grade/render/transcribe/timeline_view/pack_transcripts).
- **Needs from you:** an ELEVENLABS_API_KEY (for transcription). One `brew install` confirmation if a dep is missing.
- **Activation:** (1) put the key in ~/Developer/video-use/.env; (2) register SKILL.md in ~/.claude/skills/ (or import via CLAUDE.md); (3) verify with one real clip. Gate: the OS's os_motion_qa + the skill's own hard rules.
- **Status:** STAGED -> TEST_NOW (one key away).

## 2. HyperFrames (npm) , the motion-graphics layer  [closes the AE-titling gap without AE]
- **What:** "write HTML, render video, built for agents." HTML/CSS -> video. Animated titles, lower-thirds, data charts, overlays.
- **Why it matters:** this is the animated-titling + motion-graphics gap I flagged as needing After Effects , solved with HTML (which the OS already writes) instead. video-use uses it for overlays.
- **Unlocks:** animated mastheads/lower-thirds, kinetic type, data-driven motion , doctrine-styled (Didot/the locked kit) because it is just HTML/CSS.
- **Staged:** ~/Developer/hyperframes (package.json present).
- **Needs from you:** greenlight to `npm install` (no API key).
- **Activation:** npm install -> render one test (a DEED animated title card) -> wire as the overlay engine for video-use. Gate: os_doctrine layout + os_motion_qa.
- **Status:** STAGED -> TEST_NOW (one npm install away).

## 3. After Effects MCP (Dakkshin/after-effects-mcp) , keyframed motion design  [AE 2026 now installed]
- **What:** MCP server giving the OS control of After Effects (comps, layers, text/shape/solid, keyframes, expressions) via ExtendScript.
- **Why it matters:** for motion design beyond HTML (real keyframed AE work, expressions). Complementary to HyperFrames (HTML overlays) , AE for deep timeline animation.
- **Unlocks:** keyframed title sequences, expression-driven motion (wiggle, responsive boxes), AE-grade compositing.
- **Needs from you:** clone the repo, npm install/build/install-bridge, add to Claude Code MCP config, open the AE panel (Window > mcp-bridge-auto.jsx, Auto-run on), and a Claude Code restart to load the MCP server. AE 2026 is installed.
- **Activation:** ordered steps in OS_INSTALL_AND_BRIDGE_BACKLOG. Gate: os_motion_qa + taste sign-off.
- **Status:** INSTALLABLE NOW (AE present) -> needs the MCP config + restart (your side).

## 4. Blender MCP (Blender Foundation) , scriptable 3D  [the 3D drop path]
- **What:** MCP server + add-on giving natural-language control of Blender's Python API (scene analysis, objects, materials, geometry nodes, renaming, optimization).
- **Why it matters:** the one 3D tool that is genuinely scriptable into the OS (Python API). For a true 3D DEED certificate / wax seal / virtual set.
- **SECURITY WARNING (from Blender docs):** the MCP executes LLM-generated code in Blender WITHOUT guards. Run only in a context without sensitive data. The OS must gate every Blender action and never auto-run destructive code.
- **Needs from you:** install Blender 5.1+, the add-on, the MCP server, + config.
- **Status:** WIRE/INSTALL (not installed). LATER, only when a 3D drop is the play, with the security gate.

## OS ROUTING (how the input now picks these)
- "edit this footage / make a real trailer" -> video-use (transcribe->cut->grade->subtitle->overlay).
- "animated title / lower-third / kinetic type" -> HyperFrames (HTML overlay) ; deep keyframe -> AE MCP.
- "3D object / virtual set" -> Blender MCP (with the security gate).
- Everything still passes os_doctrine (motion/layout/visual) + os_motion_qa + os_privacy_gate before it ships.

## RECOMMENDED ACTIVATION ORDER
1. HyperFrames (npm install, no key) , prove an animated DEED title card.
2. video-use (your ELEVENLABS key) , the real edit layer; use HyperFrames for overlays.
3. AE MCP (config + restart) , when keyframed AE work is needed beyond HTML.
4. Blender MCP , later, for a 3D drop, behind the security gate.
