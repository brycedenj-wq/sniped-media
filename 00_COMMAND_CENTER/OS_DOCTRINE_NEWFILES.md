# NEW FILES DOCTRINE

## 1. WORLD BUILDING CHARACTERS DOC: FULL SYNTHESIS

### What the file actually is

The file `world building characters etc.docx` is NOT a worldbuilding or character design document. All 27 segments confirm it is a heterogeneous dump of:

- Scraped Threads/social media posts (entrepreneurship, business advice)
- YouTube tutorial transcripts (Unreal Engine 5, Unity, Blender, game mechanics)
- YouTube creator automation workflows (VidIQ, Remotion, 11Labs, Higgsfield, faceless channel builds)
- Claude Code / vibe coding livestream transcripts

No characters, settings, lore, narrative worlds, visual mythology, or brand worldbuilding appear anywhere in the file. The filename is misleading or a labeling error.

### What IS extractable for SNIPED (buried inside the noise)

Despite the mislabeling, segments 2, 3, 5, 11, 12, 13, 14, 15, 16, and 19 contain high-value technical and strategic material:

**Unreal Engine MCP Integration (segs 2, 3, 9):**
- Claude + Unreal MCP enables real-time procedural world generation via natural language: spawn structures (castles, mazes, fortresses), control lighting, take scene screenshots, iterate via self-healing blueprints
- Camera-capture class lets Claude observe Unreal scenes, read state, and iterate on 3D environments
- Persona/agent system (planned): `.md` files define character behavior; Claude adopts in-world persona for narrative/caption work
- Aura agent: image generation for character concepts → 3D model generation → auto-import into Unreal → rigging + animation retargeting + ability creation (gameplay loops)
- Direct application to Composite Environment Rotation v1: Brutalist Monument, Industrial Minimal, Sculptural Gallery environments could be procedurally generated in Unreal, rendered, then used as composite backgrounds

**Blender + Claude MCP Pipeline (segs 11, 12, 13, 14, 15):**
- Anthropic is now an official Blender Foundation patron; Claude has an official Blender MCP connector (drag-drop install, no community workaround needed)
- Setup: Blender 5.1 + Claude MCP connector + Full AI MCP (fal.ai aggregator for 100+ generative models) + Patina AI (PBR material generation)
- Demonstrated workflows: one-shot scene creation with PBR materials, geometry node plant distribution, auto-bake of normal and AO maps, batch object organization and renaming, HDRI lighting switcher panel generation
- Cost: approximately $8 per full environment generation (API calls across generation passes)
- Limitations confirmed: complex modeling from scratch fails, animation from Claude needs 2-plus iterations, geometry node precision struggles, extended sessions hit context walls (2-hour donut example crashed at 60% tokens)
- "Drunk intern" framing: Claude 3D is useful for procedural workflows and organization, not autonomous photorealistic output. Operator eye + approval gate required every 15-30 min
- Adobe connector (Photoshop, Illustrator, Premiere) underperforms manual execution (4-min AI wait vs 13-sec manual fix); validates SNIPED's operator-led composite assembly, not full-auto agentic

**Environment/Worldbuilding Methodology from Game Dev (seg 5):**
- Island of Nod doctrine: Wide/Medium/Close reference gathering (topography → biome mood → texture detail), limit palette to 3-5 object types per biome, density over novelty, story clarifies artistic constraints
- SNIPED mapping: Composite Environment Rotation v1's 7-environment constraint mirrors the "5-7 biomes, 3-5 types per biome" discipline exactly. Reference org method (wide/medium/close) is directly applicable to gathering reference for each locked environment (Brutalist Monument, Industrial Minimal, etc.)

**Content/Distribution Automation (segs 16, 18, 19, 23):**
- Higgsfield + Claude Code pipeline: transcript → timestamps → generate one image per timestamp → drag-drop video assembly. Applicable to composite-frame video for SNIPED social
- VidIQ MCP for YouTube analytics: outlier discovery, title scoring, competitor transcript parsing, scheduled reporting
- Remotion + Claude Code: data-driven motion graphics (population ranking charts etc.), 30-second MP4 from template prompt
- Sandy Lee / Charlie multi-channel playbooks: personal-blueprint-as-content-foundation, "train AI as employee via markdown files," 50-channel ops with affiliate/AdSense/brand-deal revenue layering

### Updates/Contradictions to Existing SNIPED Doctrine

No contradictions found. Three updates worth noting:

1. **Composite pipeline expansion is now active infrastructure, not future planning.** The official Blender MCP connector exists, Anthropic is a Blender Foundation patron, and the full pipeline (Claude → Blender → composite render) is demonstrably operational. This upgrades the Track B composite engine from "theoretical" to "installable today."

2. **Agentic full-auto compositing is confirmed to underperform.** Multiple segments independently validate that operator-led (Claude assists, human decides) beats agentic-full-auto for visual output. This reinforces the existing "operator-led, AI-assisting" doctrine and locks it harder.

3. **$8/environment cost gate is now known.** For planning the Composite Environment Rotation (7 environments per chapter), budget approximately $56 per full chapter of AI-generated environment assets. This is a trackable operational cost, not an unknown.

---

## 2. BLENDER MCP SERVER (mcp-1): TOOL SYNTHESIS

### What it is

A GPL-3.0 Blender add-on that turns Blender into an MCP server. An external client (Claude Code) sends Python code via TCP socket; Blender executes it in its main thread and returns results as JSON. Production-grade, not a sketch.

### Architecture (from reading all 7 source files)

| File | Role |
|------|------|
| `__init__.py` | Add-on registration, UI panel, autostart/stop controls, CLI `blender_mcp` entry point |
| `mcp_to_blender_server.py` | Core TCP socket server (port 9876), non-blocking, null-byte JSON protocol, deferred job support, stdout/stderr capture |
| `execute_interactive.py` | Timer harness for Blender interactive mode (polls server on `bpy.app.timers`) |
| `execute_blocking.py` | Blocking loop for Blender background/headless mode (no timer needed) |
| `deferred_tool.py` | Async job poller for long-running tasks (renders, bakes); up to 1-hour timeout |
| `capture_output.py` | Dual-stream stdout/stderr tee capture; feeds LLM debugging context |
| `weak_sandbox.py` | Security sandbox: blocks `sys.exit()`, `wm.quit_blender`, `wm.read_factory_settings`, `wm.read_factory_userpref`, `wm.read_userpref` |
| `cli.py` | CLI entry point: `blender --background file.blend --command blender_mcp` |

### Protocol

Request: `{"type": "execute", "code": "<python_code>", "strict_json": true/false}` + null byte
Response: `{"status": "ok"/"error", "result": <dict>, "stdout": "...", "stderr": "..."}` + null byte

### Commands / What it enables

Any valid Blender Python (bpy) command can be executed remotely. Demonstrated use cases across the file corpus:

- Scene creation and object spawning (meshes, lights, cameras, modifiers)
- Material and shader assignment (PBR, Patina-generated textures, emission materials)
- HDRI lighting switcher panel generation (custom add-on created on-demand)
- Geometry node setup (procedural plant distribution, ball-rolling animations)
- Object organization and batch renaming (100s of objects in seconds)
- Normal and AO map baking (automated, runs while operator is away)
- LOD decimation and texture extraction
- Render queue execution (background mode blocks; interactive mode defers)
- 3D model import (Tripo P1 generated models auto-imported)
- Scene state readout (for LLM decision-making and iteration)

### Concrete SNIPED Uses

**Composite Environment Rotation v1 automation:**
- Template each of the 7 locked environments (Brutalist Monument, Industrial Minimal, Monochromatic Void, Sculptural Gallery, Cinematic Urban, Organic Surreal, Futurist Editorial) as Blender scene presets
- Send Claude a direction stack prompt → Claude generates Blender Python → server executes scene swap, lighting rig, camera preset, render pass → outputs PNG/EXR for Photoshop composite assembly
- Eliminates manual Blender UI friction for environment variant generation

**Material and texture library automation:**
- Patina AI PBR generation via MCP: prompt "brick wall aged industrial" → Patina generates PBR set → Claude assigns via Blender MCP → render-ready
- Build SNIPED's environmental texture library procedurally rather than sourcing/hand-crafting

**Background-mode batch rendering:**
- `blender --background env.blend --command blender_mcp` runs headless
- Deferred job poller in `deferred_tool.py` keeps connection open for multi-second renders
- Queue chapter's worth of environment renders overnight without UI

**Track B creative engine:**
- Real subject photography (Track A) + AI-generated/Blender-assembled environment (Track B via MCP) + Photoshop composite polish = Gress playbook operationalized without leaving Claude Code
- `weak_sandbox.py` ensures LLM-generated Blender code can't terminate or reset the process

**Setup path (from seg 15 and `__init__.py`):**
1. Blender 5.1+ installed
2. Drag-drop MCP add-on (`__init__.py` et al.) into Blender preferences
3. Edit `~/.claude/claude_desktop_config.json` to add blender MCP server entry
4. Claude Desktop first, then open Blender, then start MCP from panel, then new Claude chat
5. Confirm with a smoke test scene creation prompt

---

## 3. SKILLS INVENTORY

### excalidraw-diagram-generator.skill

**Purpose:** Transforms structured ideas into real, editable Excalidraw diagram files (.excalidraw). Supports 6 diagram archetypes: flowcharts, architecture diagrams, mind maps, sequence diagrams, ERDs, slide decks. Two modes: Mode A uses Excalidraw+ MCP to write directly to workspace; Mode B emits valid JSON for paste/save.

**When to use for SNIPED:**
- Visualizing Direction Stack 5-step proof order or 17-step revenue path
- Rendering casting doctrine, LinkedIn outreach SOPs, shoot-day runbooks as flowcharts/sequence diagrams
- Architecture diagram for BASEPLATE/KOTS institutional structure (school committee, revenue-share tiers, parent trust layer)
- Scene-density cluster maps (mind map: SNIPED lineage center → LA cultural circles radiating out)
- LinkedIn authority slide decks (trust mechanics, VIB method, case study frames)
- Any time "I need to see how this connects" comes up

---

### expand-and-contract.skill

**Purpose:** Interactive scope-boundary decision tool. Takes a seed idea, expands to maximalist candidate list (8-25 items), then sorts each into Core / Nice-to-have / Maybe-later / Out via checkbox multi-select (no typed input). Delivers scope statement + concentric-circle visual.

**When to use for SNIPED:**
- New project intake where scope is ambiguous (client brief, new vertical, new content series)
- Positioning refinement: "what is SNIPED's visual lane, and what is it explicitly NOT"
- Connected toolchain decisions: "what's in this Blender MCP integration scope"
- Casting/shoot scope: what is and is not included in a photoshoot deliverable
- Direction Stack chapter boundaries: which proof elements are Core vs parked
- Any decision where explicit refusals ("Out" bucket) need to be locked before work starts

---

### infographic-builder.skill

**Purpose:** Builds polished, single-file self-contained HTML infographics from text or data. Supports 8 content types (process, stats, comparison, timeline, hierarchy, cycle, listicle, anatomy) and 5 aesthetic presets (Minimal-mono, Editorial, Bold-pop, Dark-tech, Soft-organic). Fixed dimensions per destination (Instagram square/story, X/LinkedIn, Notion, print, deck). No external dependencies.

**When to use for SNIPED:**
- SNIPED Card system visual production (B&W Card register: Minimal-mono or Editorial preset)
- Lead magnets and authority one-pagers for VIB client pipeline
- Instagram carousel graphics (Bold-pop for feed traction, Minimal-mono for document register)
- LinkedIn thought-leadership posts (methodology breakdowns, trust mechanics, case study frames)
- Shoot-day execution SOPs rendered as visual runbooks
- Scene-density LA founder network maps

---

### promptimizer.skill

**Purpose:** Writes and optimizes LLM prompts across 4 types: task prompts, system prompts, image generation prompts (Midjourney/Flux/DALL-E/Stable Diffusion), and meta-prompts (prompt generators). Delivers copy-paste-ready prompt in a code block after minimal clarification. Diagnoses core gap in draft prompts (vague goal, missing format, buried info) and rewrites rather than patches.

**When to use for SNIPED:**
- Higgsfield composite world-building prompts (subject/lighting/mood per the 7 locked environments)
- System prompts for any SNIPED_OS agent (brand voice, edge case handling, output format constraints)
- Direction Stack copywriting generation prompts
- LinkedIn outreach template refinement
- Before any major generative task where prompt quality determines output quality
- Optimizing existing Higgsfield/AI prompts that are producing off-brand results

---

### skills-sh-finder.skill

**Purpose:** Proactively searches skills.sh (90,000+ community reusable agent skills) for pre-built solutions before building custom. Fires silently at start of non-trivial tasks; returns 3-5 matches with install commands and links. Uses `site:skills.sh <query>` web search or REST API.

**When to use for SNIPED:**
- Before building any custom automation, SaaS integration, or content workflow
- When a new tool comes up (Airtable, Notion, Monday, Pixieset, Stripe, email connectors) and a pre-built skill might exist
- When starting a repeatable workflow that others likely already solved
- Operationalizes the Connected Toolchain Default doctrine: tool-first routing before building custom

---

### steelman.skill

**Purpose:** Pressure-tests a position by generating the strongest possible counter-arguments from an informed critic. 4-phase workflow: lock down the position → dialectic table (angle, case for, case against, winner) → aggregate verdict (Position Holds / Needs Revision / Fails) → revision or neighboring stronger position.

**When to use for SNIPED:**
- Direction Stack validation before a direction gets embedded in doctrine
- Positioning and pricing decisions before market deployment
- Major bets: Cultural Doc chapter commitments, book launch timing, Brand System pricing tiers
- Hiring and partnership decisions (incentive alignment, execution capacity)
- VIB method and outreach doctrine refinement (test assumptions about founder psychology)
- Any decision with real stakes where invisible failure modes need surfacing

---

### swarm-consensus.skill

**Purpose:** Queries multiple AI models in parallel via OpenRouter, aggregates responses, synthesizes into consensus with minority views flagged. Two tiers: Frontier (3-5 expensive models: Claude Opus 4.7, GPT-5, Gemini 2.5 Pro, Grok 4, DeepSeek R1, ~$0.02-0.10/call) and Cheap (5-8 fast models: Claude Haiku 4.5, GPT-5 mini, Gemini Flash, etc., 10-50x cheaper). Requires `httpx` + `OPENROUTER_API_KEY`.

**When to use for SNIPED:**
- Strategic validation: pressure-test Direction Stack refinements and VIB method iterations against diverse model perspectives before locking
- Positioning language gut-check: swarm copy before LinkedIn or DM deployment
- Factual verification: validate market claims (AI sentiment in photography, new luxury dynamics) before citing in external comms
- Creative brainstorming: cheap tier at temperature 0.9-1.0 for content ideation, caption options, scene density strategies
- Code/technical review: any automation script or API integration before shipping
- Case study / authority narrative: surface weak claims and missing authority signals in draft content

---

## NEW POSSIBILITIES OPENED

Reporting only. No lane crowned.

**1. Procedural composite environment generation is now toolchain-complete.**
The Blender MCP server (mcp-1) + official Claude connector + Patina AI PBR + fal.ai aggregator form a complete pipeline: Claude Code → Blender Python via MCP → environment scene with materials and lighting → render → Photoshop composite. The infrastructure exists today. The 7 locked composite environments could be executed programmatically rather than manually. Cost gate is known ($8/environment). Operator approval at each stage is still required (confirmed limitation of agentic Blender output quality).

**2. Unreal Engine MCP opens cinematic-quality environment rendering.**
Unreal + Claude MCP enables real-time scene observation, procedural world generation, Lumen dynamic lighting, and Megascans assets. The pipeline is more complex to set up than Blender but produces higher visual fidelity. For SNIPED's editorial lane (Meisel/Roversi/Mert & Marcus), the lighting quality ceiling in Unreal may outperform Blender renders for certain composite environments (Cinematic Urban, Brutalist Monument, Futurist Editorial).

**3. The swarm-consensus skill opens multi-model validation for strategic decisions.**
Before any positioning language, VIB method refinement, or Direction Stack commitment gets embedded in doctrine, a frontier-tier swarm (4 models, cross-lab) could pressure-test it in under 40 seconds at low cost. This operationalizes the steelman + adversarial verification practices from the OS Engagement Protocol.

**4. The skills inventory adds 6 operational tools immediately.**
excalidraw-diagram-generator, expand-and-contract, infographic-builder, promptimizer, skills-sh-finder, and steelman are all activatable now. Highest immediate leverage: promptimizer for Higgsfield composite prompts, infographic-builder for Card system visual production, steelman for Direction Stack lane validation.

**5. Timestamp-driven Higgsfield image generation opens automated composite frame sequences.**
The workflow from seg 16 (transcript → timestamps → one image per timestamp → video assembly) is directly adaptable: Direction Stack narration → timestamp list → Higgsfield generates one composite frame per beat → drag-drop video assembly. This is a path to short-form composite video without manual frame-by-frame production.

**6. Skills.sh surface (90,000+ skills) is now a mandatory pre-build check.**
Before any custom SNIPED automation is built, skills-sh-finder should run first. This operationalizes the Connected Toolchain Default doctrine at the skill-discovery layer, not just the MCP/API layer.