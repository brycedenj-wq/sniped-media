# OS ACTIVATION EVALUATION + GAP ROADMAP (2026-06-04)

> The OS sitting its own exam. Every score is backed by what is actually on disk and what actually ran, not by what the doctrine claims. Goal: move each category from "knows about it" to "can execute it repeatedly." No strategy.

## Evidence base (verified this run, not asserted)
- **Production harness is real + tested:** `test_production_harness.py` → **14 pass / 0 fail** (live run 2026-06-04). 15 `os_*` scripts in `00_COMMAND_CENTER/scripts/`. 4 hooks wired in `.claude/settings.json`.
- **Real projects through the harness:** `_live_001` (closed, 1 credit, 1 export), `_batch_001` (ready, 3 credits, 3 exports), `_TEMPLATE`.
- **`os_generate.py` video capability: ZERO** (grep for video/motion/generate_video = 0 hits). Image only.
- **No CRS script, no posting script, no analytics script** anywhere in `scripts/`.
- **Installed-active skills: 18** (in `.claude/skills/`). The **57 `sniped-*` skills live in `raw/_skills/` = reference, NOT installed**, so they do not fire on command. Executable skill surface = 18, not 75.
- **Manifest:** `OS_ENGAGEMENT_MANIFEST.csv` present (3,877 lines), 96.6% verified.

The 10 scoring axes: (1) traceability (2) command routing (3) skill activation (4) quality gates (5) tool/workflow routing (6) proof-loop logic (7) web/current-market disclosure (8) no old-lane anchoring (9) no identity collapse (10) output usefulness. ✅ pass · ⚠️ partial · ❌ fail.

Verdict tiers: **PASS** = executes repeatably today. **CONDITIONAL** = correct reasoning/routing/gates but the execution muscle is doctrine-only. **FAIL** = cannot execute repeatably AND a core axis breaks.

---

## 1. BENCHMARK RESULTS

### B1 , generate a 2026-native faceless money model from zero
Attempt produced: owned-character pseudonymous visual-IP micro-studio; rails = $27-97 digital pack now / print drop gated at 300 signups / licensing one-sheet later; faceless (handle only, no real name in WHOIS/payment); proof loop = 1 pack sale on $0 seed in 7d, 72h organic-signal kill gate; optionality preserved, not crowned.
Scores: 1✅ 2✅ 3✅ 4✅ 5⚠️ 6✅ 7✅ 8✅ 9✅ 10✅ → **PASS** (reasoning benchmark; gates + possibility-engine fire correctly).

### B2 , build a one-person campaign pipeline
Attempt produced: the 14-stage campaign house + the real harness (`os_production`/`os_batch`/`os_generate`/`os_vision_gate`) with enforced gates and 14/14 tests. Stages 1-2, 5-7, 9-10, 13-14 wired; stages 3 (sref manual-external), 8 (motion , unwired), 11 (post , no connector), 12 (analytics , no connector) are manual-gated.
Scores: 1✅ 2✅ 3✅ 4✅ 5⚠️ 6⚠️ 7✅ 8✅ 9✅ 10✅ → **PASS, with 4 execution gaps** (motion, sref, post, analytics).

### B3 , design a character-consistency workflow
Attempt produced: correct DESIGN , CRS 14-ref mandate, Nano Banana identity-preserve, image-order convention (1=base, 2=identity, 3+=refs), vision reject gate. But no `sniped-crs-builder` skill installed, no `os_crs.py`, no tested multi-frame run.
Scores: 1✅ 2✅ 3❌ 4✅ 5⚠️ 6⚠️ 7✅ 8✅ 9✅ 10⚠️ → **FAIL on execute-repeatedly** (design is correct; the muscle does not exist).

### B4 , route an AI video idea through tools
Attempt produced: correct ROUTE , Seedance/Kling/Cinema selection, 3-tier polish, dialogue-free, virality_predictor. But `os_generate` has no video path, no `kling-production-sop` skill, no motion-physics QA gate, no tested video run.
Scores: 1✅ 2✅ 3❌ 4⚠️ 5⚠️ 6⚠️ 7✅ 8✅ 9✅ 10⚠️ → **FAIL on execute-repeatedly** (can name the route; the harness cannot run it).

### B5 , turn a book principle into an executable skill
Attempt: take a verified principle (Hormozi Value Equation) → scaffold a SKILL.md (trigger/inputs/outputs/rule/example) → install. The process works (via Write), but there is no `os_skill_scaffold.py` and no skill-lint gate, so it is executable-by-Claude, not enforced/repeatable.
Scores: 1✅ 2✅ 3⚠️ 4⚠️ 5✅ 6✅ 7✅ 8✅ 9✅ 10✅ → **CONDITIONAL** (works by discipline, not by enforced script).

### B6 , create a no-conflict off-grid monetization path
Attempt produced: employer-conflict gate + off-grid rules (no employer data/relationships/name, pseudonymous, personal devices) + payment-follows-proof + faceless rail + proof loop. Gates fire.
Scores: 1✅ 2✅ 3✅ 4✅ 5⚠️ 6✅ 7✅ 8✅ 9✅ 10✅ → **PASS**.

### B7 , compare 5 money models without old-lane anchoring
Attempt produced: 5 models scored on fastest-cash/proof-loop/assets/risk/upside/faceless/optionality from the inventory; no crowning, no old lane.
Scores: 1✅ 2✅ 3✅ 4✅ 5⚠️ 6✅ 7✅ 8✅ 9✅ 10✅ → **PASS**.

### B8 , build a production SOP with gates
Attempt produced: the harness itself , prompt→generation→vision→caption→export→audit→close, each gate enforced in code, 14/14 tests, registry as single source of truth.
Scores: 1✅ 2✅ 3✅ 4✅ 5✅ 6✅ 7✅ 8✅ 9✅ 10✅ → **PASS** (strongest benchmark).

### B9 , identify where proof is required before scaling
Attempt produced: proof-before-crowning gate + kill/keep/scale signals + traceability (tested vs theoretical), explicitly naming what is still doctrine-only.
Scores: 1✅ 2✅ 3✅ 4✅ 5⚠️ 6✅ 7✅ 8✅ 9✅ 10✅ → **PASS**.

---

## 2. PASS / FAIL TABLE

| # | Benchmark | Type | Verdict | Weak axes |
|---|---|---|---|---|
| B1 | faceless money model from zero | reasoning | **PASS** | 5 |
| B2 | one-person campaign pipeline | execution | **PASS (4 gaps)** | 5,6 |
| B3 | character-consistency workflow | execution | **FAIL** | 3,5,6,10 |
| B4 | route AI video through tools | execution | **FAIL** | 3,4,5,6,10 |
| B5 | book principle → skill | execution | **CONDITIONAL** | 3,4 |
| B6 | off-grid no-conflict path | reasoning | **PASS** | 5 |
| B7 | compare 5 models, no anchoring | reasoning | **PASS** | 5 |
| B8 | production SOP with gates | execution | **PASS** | , |
| B9 | proof required before scaling | reasoning | **PASS** | 5 |

**Score: 6 PASS · 1 CONDITIONAL · 2 FAIL.** Reasoning benchmarks: 5/5 pass. Execution benchmarks: 2 pass (B2, B8), 1 conditional (B5), 2 fail (B3, B4). The failures cluster exactly in the creative-scale execution muscles, plus one systemic finding below.

**Systemic finding (cross-cutting, no excuse):** the OS counted 57 `sniped-*` skills as capability; they are drafted in `raw/_skills/` and **not installed**, so only 18 skills actually fire. Axis-3 (skill activation) is structurally weaker than the audit implied across most categories. This is build item #7.

---

## 3. WHAT FAILED AND WHY

- **B3 character consistency , FAIL.** Cause: no `os_crs.py` and no installed `sniped-crs-builder`. The OS can describe a correct 14-ref CRS workflow but cannot generate a reference sheet or verify identity across frames on command. Reliance on Claude remembering the doctrine = survival-by-discipline (the exact DRYRUN-001 BUG-2 anti-pattern).
- **B4 AI video , FAIL.** Cause: `os_generate.py` is image-only; the Higgsfield `generate_video` MCP tool exists but is not wired into the harness; no motion-physics QA gate; no `kling-production-sop`. Routing knowledge is real; execution path is absent.
- **B5 skill-from-principle , CONDITIONAL.** Cause: the "built 3x = skill" lifecycle is doctrine, not a script. No `os_skill_scaffold.py`, no skill-lint gate, no auto-register. Works when Claude chooses to; not enforced.
- **B2 gaps (still a pass).** Motion, sref pull, posting, and analytics are manual-gated stubs, not wired tools. The pipeline routes correctly and the image half is tested; the video/distribution/proof half is not executable yet.
- **Systemic , skills not installed.** 57 high-value skills sit uninstalled. Capability that is drafted but not registered is doctrine, not a muscle.

---

## 4. SKILLS TO BUILD (install-active, not draft)

| Skill | Unlocks | Source doctrine |
|---|---|---|
| `sniped-crs-builder` | B3, stage 4 | CRS mandate (NEWFILES), Nano Banana identity-preserve |
| `kling-production-sop` | B4, stage 8 | video routing, 3-tier polish, dialogue-free motion |
| `os-world-bible` | worldbuilding, stage 2 | 7-env rotation, lineage texture, Island-of-Nod framing |
| `os-skill-smith` (skill that scaffolds skills) | B5 | capability-growth mandate, "built 3x = skill" |
| Install batch of high-value `sniped-*` from `raw/_skills/` | axis-3 across the board | already drafted; needs registration + lint |

## 5. SCRIPTS TO BUILD

| Script | Does | Unlocks |
|---|---|---|
| `os_generate.py` video path | `generate_video` + `job_status` poll + ingest + cost gate | B4, stage 8 |
| `os_motion_qa.py` (extend `os_vision_gate`) | motion reject gate: grounding, edge integrity, physics, AI-tell | B4, stage 9 |
| `os_crs.py` | 14-ref sheet gen + cross-frame identity-consistency score | B3, stage 4 |
| `os_post.py` | posting handoff: identity-scrub on metadata + scheduled-draft, human-go gate | stage 11 |
| `os_proof.py` | ingest saves/shares/DMs/print-intent → proof dashboard; compute kill/keep/scale | stages 12-13 |
| `os_skill_scaffold.py` + skill-lint gate | deterministic SKILL.md scaffold + frontmatter/trigger/test validation + register | B5, systemic |
| `os_store.py` | digital-product packager: product manifest + Gumroad/Stripe link, payment-follows-proof | money |
| `os_license.py` | owned-character catalog → licensing one-sheet | money |
| `os_webcheck.py` | timestamped WebSearch wrapper → freshness-dated note for model lists / ToS / pricing | kills stale-knowledge risk |

## 6. TOOL KNOWLEDGE NEEDING CURRENT WEB VERIFICATION
- Higgsfield current model list + params + credit costs (Seedance/Kling/Cinema versions, Nano Banana Pro). Models shift; the corpus is a snapshot.
- Midjourney current version + SREF syntax.
- Platform ToS + AI-content disclosure rules (IG / TikTok / YouTube, 2026).
- Gumroad / Stripe / Shopify current fees + checkout API.
- Blender MCP current state + Unreal procedural tooling (deferred, see §8).
- Likeness / IP law for owned-character commercial use (the CF-020 AI-disclosure addendum is still an open hard block).
- Voice agents (Vapi / Retell / ElevenLabs) , only if pursued later.

## 7. DOCTRINE-ONLY vs EXECUTABLE (the honest line)

**EXECUTABLE today (script/skill + tested):** production harness (prompt→export→close), image generation (`os_generate`), vision reject gate (image), cost guard, checkpoint reconciler, token-safe reader, name gate, backup, the 14-test suite, the 18 installed skills.

**DOCTRINE-ONLY (known, not wired/installed):** AI video + motion, character consistency (CRS), worldbuilding systems, posting connector, analytics/proof ingest, digital store/checkout, licensing packaging, YouTube/media-channel ops, the 57 drafted `sniped-*` skills, Blender/Unreal 3D, voice agents, all current-market specifics.

---

## 8. FIRST 10 BUILDS , activated → operational
Ordered to make the **2026 one-person campaign house / AI-native production machine** executable first, because it touches the most categories (image, video, motion, character, style, world, copy, product, proof, distribution, money) in one system. Blender/Unreal and voice are deliberately deferred.

1. **`os_generate` video path** , `generate_video` + poll + ingest + cost gate. Unlocks B4 + stage 8. (highest leverage: turns the machine from stills-only to motion)
2. **`os_motion_qa.py`** , motion reject gate (grounding/edges/physics/AI-tell). Pairs with #1 so no motion ships ungated.
3. **`os_crs.py` + `sniped-crs-builder`** , 14-ref sheet + cross-frame identity-consistency score. Unlocks B3 + stage 4. (character is the spine of a repeatable channel)
4. **`os-world-bible` skill** , 7-env rotation + lineage texture → locked world para + sref slots. Stage 2.
5. **`os_post.py`** , posting handoff with identity-scrub metadata check + human-go gate. Stage 11.
6. **`os_proof.py`** , proof-loop ingest + kill/keep/scale compute. Stages 12-13. (closes the loop from output to signal)
7. **`os_skill_scaffold.py` + skill-lint gate + install the high-value `sniped-*` batch** , fixes B5 and the 18-vs-75 systemic gap in one build.
8. **`os_store.py`** , digital-product packager + checkout link (payment-follows-proof). First money rail.
9. **`os_license.py`** , owned-character → licensing one-sheet. Second money rail (highest-upside, lowest-effort once #3 exists).
10. **`os_webcheck.py`** , timestamped research harness for model lists / ToS / pricing. Kills the stale-knowledge risk permanently.

Each build ships with: a test added to `test_production_harness.py`, a gate, and a one-line registry/dashboard hook. Definition of done = a new passing test, not a description.

## 9. FIRST LIVE TEST (proves the upgraded system)
**One pseudonymous brief → one character → one world → BOTH a still and a motion clip of the same character in the same world → gated → captioned → posting-handoff → proof row.**

Run order: brief (1 line) → world-bible para (#4) → lock 3 srefs → build CRS + 1 hero still (#3) → generate the still (`os_generate` image, vision gate) → generate a 3-5s motion clip of the same character (#1, `os_motion_qa` #2) → finish + caption (voice gate) → posting handoff with identity-scrub (#5) → log the proof row (#6).

**Success criteria (all must hold):**
- the same character is recognizably consistent across the still AND the motion clip,
- both beat the source visually (beat-source gate),
- the reject + motion-QA gates caught at least one failure,
- zero real name in any metadata/WHOIS/handle,
- a skill candidate was logged,
- a proof row exists with a kill/keep/scale signal computed.

That single run proves image + video + character + world + copy + distribution-handoff + proof in one pass , the campaign house operating, not described. Only after it passes do we ask what to point it at.
