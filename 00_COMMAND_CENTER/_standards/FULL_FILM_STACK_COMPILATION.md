# FULL FILM STACK COMPILATION (2026-06-08)

Compiled, not collected. Every film-relevant resource ACTUALLY available in this OS, converted into production behavior and mapped to a stage of `REAL_FILM_PRODUCTION_OS`. Anti-hallucination note: I only inventory resources that exist on disk or as connected tools. Resources referenced but not provided as files (e.g. Joey's other ~8 skills) are listed in Gaps, not invented.

Stage key (REAL_FILM_PRODUCTION_OS): 1 brief · 2 story intention · 3 emotional arc · 4 action/verb script · 5 scene beats+mode · 6 coverage map · 7 moving-shot plan (spend gate) · 8 tool per shot · 9 edit blueprint · 10 sound map · 11 watch · 12 hostile review · 13 rebuild list · 14 final gate.

---

## A. THE GENERATION GRAMMAR (new Joey/Higgsfield resources)

| Resource | Purpose (1 line) | Production laws extracted | OS stage | Failure prevented | The Door impact |
|---|---|---|---|---|---|
| **cinema-worldbuilder** (skill) | Seedance motion-prompt director with locked cinematography grammar | Pick a cinema MODE per scene (M1-M5) that locks body/lens/movement/grade; prompt ACTION across the duration (Dynamic) + locked elements (Static); diegetic audio only, never music; energy over position; motivated camera per mode; per-shot timing inline; no names/brands/meta | 5,7,8,10 | Random camera language; "moving photo" prompts; music baked into generation | Every Door motion shot gets a mode + a written action; the wake/together beats get real performance prompts, not push-ins |
| **banana-pro-director** (skill) | Higgsfield image-asset director: character base → 6-panel sheet → scene plate | Build the locked canonical reference sheet FIRST (front/3-4/profile/full-body); face/bone/body/skin/hair locked, outfit/hair/makeup swap; strict order base→sheet→plate; hyperreal stack | 2,6,8 | Identity drift; re-describing a character every prompt | The Door characters become locked sheets before any motion; Eleanor/daughter/caregiver carry across shots from one ref each |
| **HIGGSFIELD OG guide + transcript** (reference, `REFERENCE_LIBRARY/higgsfield_og/`) | The written master system + the stack roles | "The lock is the look"; stack = Soul Cinema/Cast (faces+outfit), Nano Banana Pro (sheets/plates), Seedance (video, 1080p), Tiger Video (finish), Suno (music); 10 skills total | 6,8,10 | Treating tools as random generators | Names Suno as the owned-music answer to the Door music gap |
| **Scene_Sequence_Prompts** (reference) | Two coverage mega-prompts | 3x3 Cinematic Contact Sheet = 9 angles of one locked subject in one generation; 9-Scene Sequence = logical multi-beat from one input | 6 | Spending video credits before coverage is planned | Plan Door coverage cheaply before any clip |
| **watch** (skill) | Claude actually watches the cut (frames + transcript) | /watch the assembled cut at Stage 11; judge what MOVES vs what is static; focus-mode on a beat with --start/--end | 11 | Trusting a cut you never watched; mistaking stills for motion | Confirmed the frozen-Eleanor defect by watching 22s vs 24s |

## B. THE CONSISTENCY + QA GATES (existing OS, were bypassed on The Door)

| Resource | Purpose (1 line) | Production laws extracted | OS stage | Failure prevented | The Door impact |
|---|---|---|---|---|---|
| **os-face-lock** (skill) | Lock one hero face as the reference anchor + pre-video readiness gate | Approve a hero still → anchor; condition generation on THAT face; run the motion-ready gate BEFORE spending motion credits | 6,7,8 | Identity drift across shots; spending on a face that will not hold | Each Door character must pass face-lock before any clip; Eleanor/daughter conditioned on their anchor |
| **os-world-bible** (skill) | Lock the world (environments, light logic, color, camera language, forbidden elements, continuity) and check scenes against it | Define the world rules once; gate every scene for continuity before a run | 5,6 | A prompt-collage that looks like different films | The Door home + coast + light logic become one gated world; no shot drifts out of it |
| **kling-production-sop** (skill) | Route + gate an AI motion clip for character/world consistency; preflight credits; QA before ship | Choose the video model deliberately; preflight credits; run motion QA on the clip before it counts; generation needs explicit approval | 7,8,11,13 | Random motion slop; ungated clips in the cut | Every Door clip runs the motion-QA gate; the wake/together regens get gated, not assumed good |
| **os-vision-reject-gate** (skill) | Per-frame reject: slop / hands / skin / clothing-physics / text / identity / brand / likeness / beat-source | Any hard-fail on the checklist = REJECT before ship; review every generated frame | 11,13,14 | Shipping AI-uncanny frames (melted hands, plastic skin) | Run on every Door shot; the pills/asleep/any artifact frames get caught |
| **os-quality-gates** (skill) | The 11 OS gates (anti-hallucination, completion-verification, anti-old-anchoring, no early crowning) | Run the mode's gates before declaring done; a fail blocks "done" | 14 | False "done"/"client-ready"; crowning a cut early | The Door cannot be called ready until gates pass |
| **composite-master-qa** (skill) | Physics QA for a subject composited into a generated world | Two-shadow grounding, relight, edge, sensor-match, 6-axis; no "believable" without proof crops | 11,14 | Floating cutouts, fake grounding | Only if a Door shot composites a real subject into a plate (not currently; held for future) |
| **platform-mastering** (skill) | Per-surface export masters; color vs B&W on evidence | Re-compose per platform, never resize one flat master; numeric skin-drift check; clean-no-text default | 14 | One flat export degrading on feed/story | The Door 9:16 + YouTube get proper per-surface masters, not a blurred-fill afterthought |

## C. THE EDIT / SOUND / CRAFT STANDARDS (existing OS)

| Resource | Purpose (1 line) | Production laws extracted | OS stage | Failure prevented | The Door impact |
|---|---|---|---|---|---|
| **COMMERCIAL_CRAFT_BENCHMARK_V2** (doc) | Format-aware edit judgment + 12-axis scorecard | Classify FORMAT first; apply its ASL band; slow fails only when unmotivated/repetitive/no-payoff; hero = longest hold, contrast >=2.2x; score 12 axes, ELITE >=30/36 | 9,14 | Judging every cut by one pace; monotone editing | The Door scored on the 12 axes; pacing contrast enforced |
| **OS_FINISHING_DEPARTMENT_STANDARD** (doc) | Turn footage into a client-ready deliverable | Choose MODE A (dialogue) vs MODE B (visual) FIRST; never edit source in place; selects→rough cut→finishing→review; "PASS is not excellent, CLIENT-READY needs the checklist"; finishing tool routing (Premiere/AE/Adobe/ffmpeg/ElevenLabs); compose_music is paid-gated | 9,10,14 | Shipping "a render came out"; wrong selects engine | The Door is MODE B (visual); finishing routed to best tools; not called ready on completion |
| **OS_AUTOEDIT_DOCTRINE** (doc) | Build the auto-editor stack, do not buy | Pipeline: selects → bad-take cleanup → best-moment → beat grid → rough-cut → VFX/transition → grade → excellence gate; beat-snap to BPM; director label is truth until disproven by timestamped evidence | 9 | Buying tools we own; unmotivated assembly | The Door edit assembles on a motivated spine, beat-aware |
| **OS_COMMERCIAL_CRAFT_LIBRARY** (doc) | Craft cards (expensive vs amateur tells) | Motivated cuts, pacing contrast, consistent grade, one title system, restraint; kill monotone/unmotivated/auto-WB-drift | 9,14 | Amateur tells | Door QA against the expensive/amateur list |
| **OS_STORY_PSYCHOLOGY layer + STORY_GATE** (skill/doc) | Story/hook/psychology operating cards + 9-question gate | But/therefore; open-loop hook in 3s; name the feeling; withhold/reveal; closed loop | 1,2,3,4 | And-then narration; no hook; unearned emotion | The Door passes STORY_GATE (already 9/9) |
| **Second-model Gemini lane** (`os_gemini_review.py`) | Hostile critic, read-only | Accept evidence-backed notes, reject tone-deaf; never crowns final | 12 | Self-judged "good"; confirmation bias | Ran on The Door (6/10), reconciled |

## D. THE TOOLS (connected MCPs)

| Tool | Purpose | Laws | Stage | Door impact |
|---|---|---|---|---|
| **Higgsfield MCP** | Seedance / Kling 3.0 / Nano Banana Pro / Soul generation | Stills before motion; get_cost preflight; i2v keyframe for locked identity; Kling when Seedance filter blocks; uniform res | 6,7,8 | All Door generation |
| **ElevenLabs MCP** | TTS (works), SFX (works), Music (PAID-GATED, 402) | VO + diegetic SFX owned; music NOT available here → use Suno | 10 | Door VO + SFX done; music blocked |
| **Premiere / After Effects / Adobe MCP** | Finishing: timeline, grade/LUT, rack-focus, plate blur, cutouts | Route finishing to best tool, prove any skip; AE for motion title; Adobe for cutouts | 9,10,14 | Door finishing path |

## E. REDUNDANT / LOW-VALUE FOR FILM (labeled, not adopted)
- **AI Playbook pack** (`today`, `article`, `decide`, `ai-digest`, `qa-transcript-processor`): non-film or duplicate existing SNIPED skills (sniped-operator-plan, sniped-article, sniped-decide). **REDUNDANT for film.** Only `watch` was film-relevant (adopted).
- **sniped-higgsfield-pipeline / sniped-seedream-prompt / sniped-ai-image-tool-pick**: useful for image content velocity and tool-pick, but **secondary** to banana-pro-director + cinema-worldbuilder for cinema; keep as routers, not the grammar.

---

## RECONCILED HIERARCHY (contradictions resolved)
1. **Authority order (top wins):** REAL_FILM_PRODUCTION_OS → OS_AI_CINEMA_PRODUCTION_DOCTRINE (the loop) → {OS_HIGGSFIELD_PRODUCTION_DOCTRINE (generate) + OS_FINISHING_DEPARTMENT_STANDARD (finish)} → skills {cinema-worldbuilder, banana-pro-director, kling-production-sop, os-face-lock, os-world-bible, os-vision-reject-gate} → benchmarks/libraries {Commercial Craft V2, story layer, autoedit} → tools (MCPs).
2. **Diegetic-audio-only vs owned-music:** no contradiction. Diegetic audio is for the GENERATION prompt (cinema-worldbuilder); music is added in FINISHING. Never put music in a generation prompt.
3. **Music route:** Suno (owned) is preferred; ElevenLabs compose_music only if the tier is upgraded; a synth/SFX bed is scratch-only and never final. (Reconciles AI cinema doctrine + finishing standard.)
4. **"PASS is not excellent" / 9/10 floor:** consistent across finishing standard, AI cinema doctrine, quality gates. One rule.
5. **Selects engine:** MODE A transcript vs MODE B frames. The Door is MODE B (visual). AutoEdit doctrine's selects pipeline is for real footage; for AI films the "selects" are the approved shot plan, then beat-snap assembly. Noted, not a conflict.

---

## GAPS (knowledge/resources still missing)
1. **The other ~8 Joey skills** referenced in the guide are NOT on disk (only cinema-worldbuilder + banana-pro-director were provided). Likely missing: a bilingual/multi-shot seedance-director, Soul/character-training skill, a music/Suno skill, an editing/sequence skill, a transitions skill. **Cannot compile what is not provided.** Need the files or the source link.
2. **Suno (or any owned-music) tool is not connected.** Music cannot be produced in-session. Blocker for any final emotional film. Need: Suno access, or ElevenLabs music upgrade, or licensed-track route.
3. **No AI-film-native assembly engine.** The autoedit/finishing engines assume real-footage selects; an AI-film assembles from a shot plan. Minor build gap (a shot-plan→EDL→ffmpeg wrapper).
4. **No live-action capture** (all-AI by design); not a gap unless a brief requires real footage.
5. **Kling cost preflight + balance endpoints were erroring** at last attempt; confirm credit cost model for Kling before a batch.

---

## STATUS
Stack compiled and reconciled. `REAL_FILM_PRODUCTION_OS` updated to reference this registry as the master authority. The Door paper rebuild (next section / `THE_DOOR_FILM_AUDIT_AND_REBUILD.md`) now passes the fuller grammar. **No rendering until the rebuild plan clears the grammar and the music + missing-skills gaps are resolved or explicitly accepted.**
