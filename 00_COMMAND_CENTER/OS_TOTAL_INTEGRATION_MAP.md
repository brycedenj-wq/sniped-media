# OS TOTAL INTEGRATION MAP
### The whole SNIPED_OS as one operating organism
Built: 2026-06-05 (post-restart total integration pass). Source of truth for "is this one thing or a pile of parts."

---

## The rule (operator mandate)

> Every doc, source, skill, script, connector, plugin, and app must either become part of the **router**, part of a **workflow**, part of a **gate**, part of a **dashboard**, or be **intentionally deferred**. Nothing floats.

This map assigns every category to one of those five homes. If something is not in a home, it is a leak and goes to the absorption backlog.

---

## The spine (the organism's nervous system)

One input flows through one chain. No step is chosen by hand.

```
INPUT
  -> os_prime_router.py        which MODULES wake (18 modules)
  -> os_doctrine_router.py     which DOCTRINES load + confidence (CERTIFIED/MIXED/PROVISIONAL)
  -> os_doctrine.py load       inject the doctrine pack INTO creation
  -> os_tool_router.py         which ROUTE (toolchain) runs
  -> os_tool_registry.py       live ACTIVE/AMBER/RED per tool  <- REFUSES non-ACTIVE
  -> [skill]                   OS_SKILL_REGISTRY.csv best-match ACTIVE skill
  -> GATES                     doctrine check + route validation + standing safety floor
  -> ARTIFACT                  the deliverable
  -> LOG + DASHBOARD           EDIT_LOG / SPEND_LEDGER / gate logs / registries
  -> LEARNING LOOP             failure rule -> doctrine/registry update
```

The capstone that fuses all of the above for any task is **`os_execution_graph.py`**. One task in, the whole chain out, with a built-in refusal when a required tool or route is not ACTIVE.

```
os_execution_graph.py graph "<any task>"
os_execution_graph.py command "<one of the 14 commands>"
```

---

## Where every category lives (router / workflow / gate / dashboard / deferred)

| Category | Home | How it is wired |
|---|---|---|
| **Custom OS scripts** (50 `os_*.py`) | ROUTER + WORKFLOW + GATE | registered in `os_tool_registry.TOOLS`, invoked by routes, several ARE gates |
| **Custom skills** (74 in `OS_SKILL_REGISTRY.csv`) | ROUTER | `os_execution_graph.match_skill` selects the ACTIVE skill per task |
| **Claude app skills** (canvas, web-artifacts, theme-factory, brand-guidelines, skill/mcp-builder) | DEFERRED (HANDOFF) | registry `askill.*` rows, AMBER, run in claude.ai app |
| **Plugins** (twilio, zapier, zoominfo, pdf, adspirer, etc.) | DEFERRED (HANDOFF) | registry `bridge.*` rows, AMBER, gated per action |
| **Adobe for Creativity MCP** | WORKFLOW + GATE | 17 capabilities in `ADOBE_CAPABILITIES`, upload via `os_adobe_cloud` handshake |
| **Adobe downloaded skills** (batch-edit, social-variations, design-from-template, quick-cut, resize, retouch) | ROUTER (as MCP substitutes) | `skill.adobe.*` rows map each to the underlying `mcp.adobe.*` capability |
| **Blender** | WORKFLOW + GATE | `blender.native` (ACTIVE) always behind `blender.gated` (os_blender_gate), sandbox only |
| **HyperFrames** | WORKFLOW | `hyperframes` ACTIVE, owns code-defined HTML motion/video |
| **Higgsfield / Seedance** | WORKFLOW + GATE | `mcp.higgsfield.*` ACTIVE, spend-gated via os_cost |
| **Figma** | ROUTER | `mcp.figma` ACTIVE, owns design-system + code<->design bridge |
| **Airtable** | DASHBOARD + WORKFLOW | `mcp.airtable` ACTIVE, owns structured ops/forecast data |
| **Notion** | DASHBOARD + DOCTRINE SURFACE | `mcp.notion` ACTIVE, owns CRM (5-DB) + human-readable doctrine |
| **Google Drive / Gmail / Calendar** | WORKFLOW (storage/inbox/schedule) | ACTIVE-read, TEMP-bridge + outbound gates |
| **Vercel / Netlify** | DEFERRED (HELD) | Vercel ACTIVE route but public-action held; Netlify needs OAuth |
| **Local utilities** (ffmpeg, exiftool, git, python, AE aerender) | WORKFLOW | `local.*` ACTIVE, proven this session |
| **Certified + provisional docs + books + intel** | DOCTRINE | `os_doctrine.DOCTRINE` (9 domains) + memory `intel_*/feedback_*` |
| **Proof loops** | WORKFLOW + GATE | `create_proof_loop` route, keep/kill/scale gate |
| **Campaign engine** | WORKFLOW | `os_campaign` -> `make_campaign_package` route |
| **Post-production engine** | WORKFLOW + GATE | `os_adobe_*` chain + `os_postproduction_gate` |
| **Launch / money / privacy / vision / motion gates** | GATE | `os_launch_check`, `os_money_path`, `os_privacy_gate`, `os_vision_gate`, `os_motion_qa` |
| **Failure ledger + self-correction** | LEARNING LOOP | `learning_self_improvement` module + gate logs feeding doctrine |

---

## The 10 organism questions (answered automatically per task)

`os_execution_graph.py` answers all ten for any input. Verified working 2026-06-05:

1. doctrine to load, 2. tool to use, 3. skill to invoke, 4. script to run, 5. connector to use, 6. gate to apply, 7. artifact to produce, 8. dashboard/log to update, 9. failure rule to check, 10. human approval line not to cross.

---

## Standing safety floor (never crossed without explicit go)

Applied on every task regardless of trigger (the `safety_identity` standing-floor doctrine):
- No real identity / employer overlap, no metadata leak, faceless-safe.
- No public action (host/post/send/deploy/spend-irreversible) without an explicit go.
- Payment + legal finalization HELD.
- Capability counts only with a proving artifact.

---

## Honest status (verified counts, 2026-06-05)

- Tools: 40 ACTIVE / 24 AMBER / 8 RED (of 72)
- Routes: 12 ACTIVE / 6 AMBER (of 18)
- Adobe capabilities: 5 ACTIVE / 12 AMBER (of 17)
- Skills: ACTIVE subset of 74 (see OS_SKILL_REGISTRY.csv)

AMBER and HELD are not failures. They are honestly-labeled edges with a named unblock. See `OS_TOOL_AND_SKILL_ABSORPTION_BACKLOG.md`.
