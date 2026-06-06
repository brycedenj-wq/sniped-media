# Prime Mover Big Lanes Audit

2026-06-05. Boot loaded first (commit c2494d3, 12/12 artifacts). No creative work, no spend. Judged on real operationalization (tool + route + gate + proof), not keyword mentions. Status legend: ACTIVE (proven) / AMBER (wired, no proof or partial) / RED (missing) / HANDOFF (manual/operator) / DEFERRED (intentionally held).

## 1. Full lane map (25 departments)

| # | Lane | Status | Tools | Docs/cards | Scripts/routes | Proof | Biggest gap | Need docs? | Need app? | Next activation test |
|---|------|--------|-------|-----------|----------------|-------|-------------|-----------|----------|----------------------|
| 1 | Strategy / positioning | ACTIVE | corpus, doctrine router | intel_* + 201 hits | os_doctrine_router, os_execution_graph | GRAND_MONEY_PLAY answer | none major | no | no | route a positioning Q through os_execution_graph |
| 2 | Creative direction | ACTIVE | moodboard/treatment cards | 34 direction cards + photo 52 | os_world, os_vision_gate | composite/vision gates built | premium MG direction thin | no | no | run os_world on a brief |
| 3 | World-building | ACTIVE | Blender MCP, world-builder | blender 27, wbld_* | os_world + os_blender_gate | blender_sandbox renders | fal spend untested | no | no | world-builder 1-ref scene (needs fal $) |
| 4 | Image generation | ACTIVE | Higgsfield, nano-banana, Firefly | higgsfield 75 | os_generate, os_herolock | 4K stills proven | none major | no | no | conditioned still on locked hero |
| 5 | Motion generation | ACTIVE | Higgsfield (Kling/Seedance/WAN/Veo) | hf cards | os_generate video, os_motion_qa | i2v beats proven | none major | no | no | start/end-frame beat |
| 6 | Video editing | AMBER (preferred PENDING) | Premiere MCP (269), video-use, ffmpeg | premc_ 13, vuse_ 8 | os_video_edit_router, os_premiere_compliance_gate | HYBRID selftest passed | Premiere bridge not started | no | no (built) | start MCP Bridge + new session -> read sequence |
| 7 | Motion graphics / titles | AMBER | AE MCP (pending), aerender, HyperFrames | AE 4 (thin) | os_motion_qa | HyperFrames titles proven | AE library thin; AE bridge manual | LIGHT (AE how-to) | no (built) | aerender a real .aep title |
| 8 | Sound / voice / music | **RED** | none wired (Higgsfield audio unused) | scattered (ff_sound only) | NONE | none | **no voice, no music, no SFX engine** | maybe | **YES (ElevenLabs + Suno/Udio)** | connect ElevenLabs, generate 1 VO line |
| 9 | Adobe post-production | ACTIVE | Adobe MCP + os_adobe_* local | adobe 128 | os_adobe_grade/composite/reframe, os_postproduction_gate | DEED crop/grade proven | cloud gen-expand untested | no | no | grade + composite a frame |
| 10 | 3D / materials / mockups | AMBER | Blender, world-builder (Tripo/PATINA/PolyHaven) | blasm_ 4, blender 27 | os_blender_gate, os_mark | object-space render proven | material libraries thin; no Substance | no | USEFUL (material lib) | render a product mockup object-space |
| 11 | Figma / design system / decks | ACTIVE | Figma MCP + figma-desktop | figma 25, taste_ 4 | os_adobe_layout (fallback), elite gate | Figma whoami proven | live deck build untested | no | no | build a 1-frame design-system board |
| 12 | Copywriting / sales psych | ACTIVE | corpus | copy 50 | os_ask, os_sales_script | money cards proven | none major | no | no | os_ask "write the sales page" |
| 13 | Social distribution / YT packaging | AMBER | social cards; NO scheduler | social 84 | os_ask | doctrine only | no posting tool (held) | no | DEFERRED (scheduler) | draft a YT package (unsent) |
| 14 | Analytics / feedback loops | AMBER | Semrush, Higgsfield virality_predictor, proofcell | analytics scattered | os_form_ingest/score | proofcell form built | no campaign-perf loop | no | no | run virality_predictor on a clip (later) |
| 15 | CRM / Airtable / leads | AMBER | Airtable MCP | crm cards | os_crm_schema | schema built | no live populated base | no | no | create the Airtable base from schema |
| 16 | Notion client/project room | AMBER | Notion MCP | - | - | connector live | no room template built | no | no | create a Notion project-room template |
| 17 | Drive delivery / archive | ACTIVE | Google Drive MCP | - | - | connector live | no delivery folder convention | no | no | create a private delivery folder |
| 18 | Vercel / private demo page | DEFERRED (held) | Vercel MCP (+Netlify needs auth) | - | - | connector live | hosting HELD by doctrine | no | no | (held) password-gated demo when approved |
| 19 | Legal / IP / commercial | AMBER | manual.legal handoff | Contracts/Legal cards | os_privacy_gate (identity) | privacy gate built | no IP/commercial checklist gate | no (docs exist) | no | build legal checklist gate from cards |
| 20 | Payment / invoicing | DEFERRED (held) | manual.payment RED | pricing cards | os_pricing_gate | pricing logic proven | payment-follows-proof (intentional) | no | no | (held) fastest legit link when proof lands |
| 21 | Proof-to-cash routing | ACTIVE | - | money 144, sales 110 | os_proof_to_cash_router, os_offer_builder, os_client_fit_gate | routing proven | none major | no | no | route a proof asset to cash play |
| 22 | Quality gates | ACTIVE | - | - | 15 gates incl max_readiness | gates fire correctly | none major | no | no | os_max_readiness_gate on a proof.json |
| 23 | Automation / orchestration | ACTIVE | Workflow, Agent, MCPs | - | os_execution_graph, prime_router, Workflow | 85-agent pass ran | none major | no | no | run a workflow phase |
| 24 | Security / privacy / identity | ACTIVE | exiftool, gated sandbox | - | os_privacy_gate, blender.gated | metadata strip + deny ~/.ssh proven | none major | no | no | os_privacy_gate on an asset |
| 25 | Backup / versioning | ACTIVE | git (99 commits), os_backup.sh | - | os_backup.sh, os_wave_lock | git-backed brain | no offsite remote pushed | no | no | push to a private remote (later) |

## 2. Missing high-ceiling lanes (the real departments to add)
1. **SOUND / VOICE / MUSIC (RED)** , the one true missing department. A campaign film with no scored sound, VO, or SFX is half a deliverable. Need a voice engine (ElevenLabs) + a music engine (Suno or Udio) + an os_sound route + a sound gate + cards.
2. **Motion graphics / titles (AMBER)** , AE library thin (4 cards) and the AE bridge is a manual install. Functional via HyperFrames; premium MG is shallow.
3. **Analytics feedback loop (AMBER)** , connectors exist (Semrush, virality_predictor, proofcell) but not wired into a campaign-performance loop.
4. **Legal/IP checklist (AMBER)** , docs exist, no enforcing gate.
5. **CRM/Notion room (AMBER)** , schema + connectors ready, no live base/template instantiated.

## 3. Apps/tools to add or verify
| App | Verdict | Why |
|-----|---------|-----|
| Premiere | ALREADY COVERED (MCP, bridge pending) | preferred editor, finish activation |
| After Effects | ALREADY COVERED (MCP + aerender, bridge manual) | titles/MG |
| CapCut | NOT NEEDED (doctrine-only) | app/CLI absent; Premiere covers |
| DaVinci Resolve | USEFUL LATER | free Fusion (MG) + Fairlight (audio) + color alt if Adobe stalls |
| Runway | NOT NEEDED NOW | Higgsfield covers motion (Kling/Seedance/WAN/Veo) |
| Krea | NOT NEEDED NOW | image covered (Higgsfield/nano-banana/Firefly) |
| Topaz Video | ALREADY COVERED (via Higgsfield upscale) | standalone USEFUL LATER for photo |
| **ElevenLabs** | **NEEDED NOW** | voice/VO , the sound gap |
| **Suno / Udio** | **NEEDED NOW** | music/score , the sound gap |
| Descript | USEFUL LATER | overlaps Premiere-MCP autoedit + video-use |
| Frame.io | USEFUL LATER | review/approval; Notion/Drive cover now |
| Substance / Adobe 3D | USEFUL LATER | Blender + world-builder (Tripo/PATINA) cover now |
| Blender add-ons / material libs | USEFUL | deepen 3D materials |
| Figma plugins | ALREADY COVERED | Figma MCP live |
| Notion templates / API | ALREADY COVERED (need template) | connector live |
| Airtable automations | ALREADY COVERED (need base) | connector + schema live |
| Vercel / Netlify | ALREADY COVERED (held) | Vercel live; Netlify needs auth |
| YT / social scheduling | NEED SETUP (DEFERRED) | no scheduler; posting held anyway |
| Analytics tools | ALREADY COVERED (Semrush) + need wiring | operationalize a loop |
| Payment / invoice | NEED SETUP (DEFERRED) | held by payment-follows-proof |

## 4. Docs/sources to add ONLY if truly needed
- Sound: a short ElevenLabs + Suno/Udio operator how-to (or just connect and card from use). This is the only lane where a new doc genuinely helps.
- After Effects: a light AE how-to / a template titles.aep would thicken the thin AE library.
- Everything else: the OS already has enough docs. The gap is operationalization or tool-control, not knowledge.

## 5. Already enough (do not add docs)
Strategy, creative direction, image, motion, Adobe post, copy, money/offer/sales, world-building doctrine, quality gates, automation, security, backup. 987 cards already cover these.

## 6. Overkill / do not add now
Runway, Krea, Descript, Frame.io, Substance, DaVinci, standalone Topaz, social schedulers, second image models. Adding them now is tool-hoarding, not capability. (Anti-pattern: the OS already learned this.)

## 7. What blocks a true max campaign-house run
1. **Sound department missing (RED)** , no VO/music/SFX. Hard blocker for a film-grade deliverable.
2. **Premiere/AE MCP bridges not started + new session** , editing is preferred-pending (manual + restart).
3. **AE/motion-graphics thin** , premium titles shallow.
NOT blocked by: docs (plenty), strategy, image/motion gen, post, design, money, gates, automation. The blockers are one missing department + tool-control (bridges), not knowledge or taste-docs.

## 8. Shortest path to "totally unlocked"
1. Start Premiere MCP Bridge + AE bridge install + NEW Claude session (unblocks editing). [manual]
2. Stand up the SOUND department: connect ElevenLabs (voice) + Suno/Udio (music); build os_sound route + os_sound_gate; extract cards. [one build, low spend]
3. Thicken motion-graphics: build a reusable titles.aep (or HyperFrames title kit) + a few AE cards.
4. Wire analytics feedback loop (os_analytics: Semrush + virality_predictor + proofcell).
5. Instantiate CRM (Airtable base from os_crm_schema) + Notion client-room template + Drive delivery convention.
After 1+2 the OS can produce a complete sound-on campaign film end-to-end; 3-5 are polish/ops.

## 9. Exact manual actions for the operator
- Premiere: open a project -> Window>Extensions>MCP Bridge -> temp dir /tmp/premiere-mcp-bridge -> Start Bridge.
- After Effects: `cd ~/after-effects-mcp && npm run install-bridge` (the app-modifying installer the auto-classifier blocked), then Window>Extensions in AE.
- Restart Claude Code (new session) so premiere-pro + after-effects tools load.
- Decide the sound stack: ElevenLabs account + Suno or Udio account (so I can wire the sound lane).

## 10. Exact next build after this audit
**Stand up the SOUND department** (the only RED lane): os_sound route + os_sound_gate + ElevenLabs/Suno wiring + sound cards. It is the single highest-leverage missing department for a max campaign film. (Pending your sound-stack choice + go. Premiere/AE activation is parallel and manual.)
