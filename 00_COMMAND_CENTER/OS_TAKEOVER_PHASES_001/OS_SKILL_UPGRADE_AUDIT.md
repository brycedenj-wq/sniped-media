> **Retired 2026-06-28.** One or more OS_* systems referenced in this document were retired during the OS repository convergence and moved to `_HISTORY/` or `_ARCHIVE/`. Those references are historical and no longer active. See `CONVERGENCE_PLAN_2026-06-28.md`.

# OS Skill Upgrade Audit

**Phase:** OS_TAKEOVER Phase 5 - Skill Upgrade Program
**Date:** 2026-06-21
**Auditor:** Claude Sonnet 4.6 (subagent)
**Scope:** 83 skills in `.claude/skills/`, 15 workflows in `.claude/workflows/`
**Authority:** `OS_TAKEOVER_UPGRADE_PLAN.md` Phase 5 acceptance criteria

---

## Full Skill and Workflow Inventory

### Skills (83 total, `.claude/skills/`)

```
banana-pro-director        batch-extraction           boardroom
brand-validation-machine   challenge                  cinema-worldbuilder
composite-master-qa        emergency-drop-protocol    jsonl-validation
kling-production-sop       master-consolidation       model-casting-protocol
operator-review            os-command-router          os-engagement
os-face-lock               os-quality-gates           os-token-safe-reader
os-vision-reject-gate      os-world-bible             platform-mastering
save                       session-save               skill-template
sniped-ai-image-tool-pick  sniped-ai-photographer-market  sniped-ai-sentiment
sniped-analog-premium      sniped-app-builder         sniped-art-series
sniped-assistant-task-routing  sniped-blockbuster-strategy  sniped-canonical-truths
sniped-caption-writer      sniped-capture-to-delivery sniped-company-of-one
sniped-crs-builder         sniped-direction-stack     sniped-discovery-to-close
sniped-evoto-skin-pass     sniped-execution-prioritization  sniped-hero-composite-ceiling
sniped-hero-composite-lite sniped-higgsfield-pipeline sniped-hit-mechanics
sniped-hospitality-layer   sniped-lean-audit          sniped-leverage-logic
sniped-lighting-vault      sniped-luxury-edit         sniped-monday-cockpit
sniped-new-luxury          sniped-notion-crm-update   sniped-partnership-protocol
sniped-perennial-seller    sniped-photo-theory        sniped-pixieset-gallery
sniped-positioning-phrases sniped-post-delivery       sniped-post-shoot-same-day
sniped-pre-shoot-prep      sniped-pricing-decision    sniped-production-os
sniped-project-intake      sniped-retoucher-onboarding  sniped-reverse-roadmap
sniped-seedream-prompt     sniped-shoot-day-reset     sniped-shoot-day-strategic-free
sniped-shortform-retention sniped-status-psychology   sniped-strategic-implications
sniped-strategy-execution  sniped-trust-equation      sniped-trust-mechanics
sniped-udemy-ai-accelerants  sniped-udemy-lightroom-rails  sniped-vib-outreach
sniped-web-builder         sniped-wwp-positioning     source-inventory
staging-plan               watch
```

### Workflows (15 total, `.claude/workflows/`)

```
adversarial-verify.workflow.js      ai-edl.workflow.js
alma-4k-qa.workflow.js              alma-ai-edl.workflow.js
alma-her-film-edl.workflow.js       alma-v5.workflow.js
creative-levelup.workflow.js        higgs-levelup.workflow.js
synergy-3shot-verify-v3.workflow.js synergy-3shot-verify.workflow.js
synergy-bestof-verify.workflow.js   synergy-film-verify.workflow.js
synergy-hero-v4-reverify.workflow.js  synergy-keyframe-select.workflow.js
synergy-shot2-reverify.workflow.js
```

---

## High-Priority Skill Assessments

### 1. Project Intake Capsule

**Skill path:** `.claude/skills/sniped-project-intake/SKILL.md`
**Note on naming:** The plan names this as both `sniped-project-intake` and `sniped-project-ingestion`. Only `sniped-project-intake` exists. No `sniped-project-ingestion` was ever created. The old name was the interim alias before the skill was built.

**Exists:** Yes.
**Tested:** UNTESTED. No `PROJECT_CAPSULE.md` artifact was found in any project folder. The template exists (`00_COMMAND_CENTER/PROJECT_CAPSULE_TEMPLATE.md`) but has never been filled via this skill on a real project. The Alma Love and Synergy projects pre-date this skill and did not use a capsule intake.

**Trigger assessment:** Trigger is well-scoped: messy brief / raw notes / new client. The description says "use BEFORE the production skill/workflow." Risk of under-triggering is HIGH because the workflow pressure in real sessions is to go straight to a production skill (creative-levelup, ai-edl, sniped-web-builder). The router (`os-command-router`) does not name `sniped-project-intake` in its frontmatter, so there is no forced gate.

**Content assessment:** The SKILL.md is well-structured: 7 numbered steps, explicit contamination boundary, quality gate with 5 pass/fail criteria, and a clear output format. Length is appropriate.

**Recommendation:** TIGHTEN FRONTMATTER. Add `sniped-project-intake` as a named dependency in `os-command-router` for the Execution and Build modes when a client/project context is detected. Add a hook that fires it automatically when a new project folder is created. The capsule boundary (project facts never written to permanent OS) is correct doctrine and must stay. Once the next real client project starts, run this skill first and treat the resulting `PROJECT_CAPSULE.md` as the first test receipt.

---

### 2. Book Certification Wave Runner

**Skill path:** None. No packaged skill exists.
**What exists instead:** `build_wave.py` at `00_COMMAND_CENTER/OS_CERT_WAVE_002E/control/build_wave.py` (and mirrored for waves 002F, 002G). This is a standalone Python script: wave-agnostic, deterministic, no model, no spend. It reads the ledger CSV, extracts book text, emits Workflow `.js` files. A separate controller discipline uses `RUN_STATE.json`, `PROGRESS_LEDGER.csv`, `WATCHDOG.md`, and `RESUME_QUEUE.md` per wave folder.

**Tested:** YES (cited evidence). Waves 002-A through 002-E have OS_RECEIPT.md files confirming runs. Wave 002-A certified 9 books with per-book adversarial verify. Wave 002-E completed its run per the `OS_CERT_WAVE_002A/OS_RECEIPT.md` and the OS book certification memory entry. `build_wave.py` itself is a proven extraction-and-emit script.

**Should it become a skill?** YES, with a specific framing. The case for a `corpus-wave-runner` skill:
- The `build_wave.py` pattern is already repeated across 002-E, 002-F, 002-G with nearly identical structure.
- A skill would standardize the call contract: `$ARGUMENTS` = wave ID, the script path, the ledger, the control dir.
- The skill does NOT replace `build_wave.py`. It wraps the human-facing SOP: preflight (is the ledger current, is the wave ID valid, is a wave already in flight per `os_cost_guard`), runs `build_wave.py`, monitors `RUN_STATE.json`, and surfaces the resume queue.
- Name: `corpus-wave-runner`. Description: "Run a book-certification wave end to end: preflight the ledger, build the wave (build_wave.py), monitor progress via RUN_STATE.json, resume from RESUME_QUEUE.md on failure."
- The rubric (segment count, adversarial verify, dual-ledger flip) should move to a reference doc at `00_COMMAND_CENTER/_standards/CORPUS_WAVE_RUNNER_RUBRIC.md` to keep the SKILL.md concise.

**Recommendation:** CREATE `corpus-wave-runner` skill. The script already works; the gap is the operator-facing SOP wrapper and the sequential-workflow guard (`os_cost_guard` prevents two waves in flight). Move rubric to a reference doc. First test: run it on 002-G with the skill as the invocation path.

---

### 3. Docs/Tooling Metabolization

**Skill path:** None. No packaged skill exists.
**What exists:** `00_COMMAND_CENTER/OS_DOCS_TOOLING_001/` with `DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv`, `RUN_STATE.json`, `OS_RECEIPT.md`, and a `control/scripts/` directory. The controller discipline mirrors the book-wave pattern.

**Tested:** YES (cited evidence). `OS_DOCS_TOOLING_001/OS_RECEIPT.md` confirms the program ran and reached a reconciled 50/50 terminal state. 44 docs dispositioned; adversarial verify caught a real coverage-gate flaw and was corrected. Rating: 9/10.

**Should it become a skill?** Partially. The OS_DOCS_TOOLING program was a one-time closure of the non-book backlog. Once the 6 EXCEPTION videos are transcribed (Whisper key needed), this program's backlog is exhausted. A standalone skill for re-running it adds little value unless a new batch of docs/transcripts arrives.

**Better path:** The reusable pattern here is the ledger-first disposition model (scope new items, dedup, classify, whole-read verified-only, adversarial verify, reconcile counts, reconcile manifest, hold what cannot be processed). This pattern composes with `corpus-wave-runner` for books. For docs/tooling it is a lighter ad-hoc workflow, not a recurring production loop.

**Recommendation:** DO NOT skill-ify docs/tooling as a separate skill. Instead, extend the `corpus-wave-runner` skill with a `--mode docs_tooling` argument (or a distinct description trigger) so the same ledger-first SOP applies to future docs/tooling batches. Document the EXCEPTION recovery path (Whisper install -> transcribe 6 videos -> re-run disposition). Log this as a note in `ACTIVE_KNOWLEDGE_STATE.md`.

---

### 4. External Visual Proof Packet

**Skill path:** No dedicated skill. The standard lives at `00_COMMAND_CENTER/_standards/OS_EXTERNAL_VISUAL_PROOF_GATE.md`.
**Adjacent skill:** `os-vision-reject-gate` handles Claude's first-pass triage (not the external gate).

**Tested:** UNTESTED as a triggered, skill-packaged behavior. The doctrine has been cited in memory entries (Alma, Synergy proof), and the router index mentions the gate for film/photo/composite/brand_campaign contexts. However, no skill file wraps it. Claude applies it ad hoc from doctrine when memory context fires, which is not reliable across session boundaries.

**Trigger assessment:** The doctrine is clear: gate required before any visual work is called "final/client-safe/approved." Under-triggering risk is HIGH because Claude's visual judgment is unreliable and the gate is doctrine-in-a-standards-file, not a skill the router names.

**Content assessment:** `OS_EXTERNAL_VISUAL_PROOF_GATE.md` already has the full rubric (who is the judge, what counts as passing, the review packet format, status discipline). The packet format is specific: contact sheet + shot IDs + reject criteria + judge questions.

**Recommendation:** CREATE `external-visual-proof-gate` skill. It is short: read the standard, build the review packet (contact sheet + frame strip + shot map + reject criteria), route to the external judge (operator / ChatGPT / Gemini), record the verdict, update status. The rubric stays in the standard doc. The skill invokes the standard and enforces the packet-build step, which is the part currently skipped. Trigger phrase: "is this client-ready" / "run visual QA" / "proof the composite / film / photo." Wire into `os-command-router` as a named exit gate for any Execution or Build that produces visual artifacts.

---

### 5. Morning Cockpit (sniped-monday-cockpit) and sniped-operator-plan

**Skill path:** `.claude/skills/sniped-monday-cockpit/SKILL.md`. `sniped-operator-plan` does NOT exist as a skill.

**Tested (monday-cockpit):** UNTESTED. Memory contains one reference: a planned routine ("monday-cockpit 8am") that was listed in `os-orchestration-upgrade.md` as "NOT yet (need BJ go: cost/connectors)." No session save or receipt records a real Monday cockpit invocation.

**Trigger assessment:** The frontmatter trigger is tight and correct: "Monday morning," "plan my week," "what should I focus on." Risk is LOW over-trigger (the time anchor is specific). Risk of under-trigger is MEDIUM because the cockpit reads from `CURRENT_STATE.md` and `ACTIVE_THREADS.md` in the SNIPED_OS source folder, which must be kept current. If those files are stale, the skill produces a stale cockpit.

**sniped-operator-plan:** The plan references this as a separate morning cockpit variant. On inspection it does not exist as a skill. The `B2B_POSITIONING_CLAUDE_OPERATOR_PLAN.md` in `00_COMMAND_CENTER/` is a batch extraction plan, not a skill. The OS_TAKEOVER plan's "morning cockpit" and "pulse check" were listed together and likely refer to the same cockpit concept at two different cadences (Monday = weekly launch; mid-week pulse = state check).

**Content assessment:** The skill is well-scoped. MANDATORY READING references 5 source files. The REFUSE section correctly bars new strategy in the cockpit. The output format (3 outcomes, cadence checklist, blockers, active threads) is actionable.

**Recommendation (monday-cockpit):** LEAVE as-is, but run it once on a real Monday to generate the first receipt. Once the scheduled Routine lane is open (Phase 6 of OS_TAKEOVER), convert to a Routine that fires at 8am on Mondays and writes the cockpit to a dated file in `00_COMMAND_CENTER/cockpits/`. The source files (`CURRENT_STATE.md`, `ACTIVE_THREADS.md`) must be kept live for this to work.

**Recommendation (operator-plan / sniped-operator-plan):** Do not create a duplicate of `sniped-monday-cockpit`. Instead, make the Monday cockpit cover the weekly launch, and define a separate `sniped-pulse-check` skill (see below) for the mid-week state check. The name "operator-plan" is redundant given `sniped-strategy-execution` already covers planning.

---

### 6. Pulse Check

**Skill path:** None. No skill exists.
**What the plan says:** `build_wave.py` segment_08.txt and `CLAUDE_OVERLOAD_DOCTRINE.md` describe a "pulse check" that reviews all active projects and flags stalls. The doctrine groups it with "morning cockpit / pulse-check routines."

**Tested:** UNTESTED. No artifact or receipt.

**Gap:** There is currently no lightweight skill for a mid-session or mid-week state check that: (a) reads `NEXT_ACTION.md`, (b) reads `00_COMMAND_CENTER/OS_CURRENT_STATE.md` and `ACTIVE_THREADS.md`, (c) checks `RUN_STATE.json` in active wave folders for stall, (d) returns a one-paragraph "this is where we are and the one thing to do now." This is distinct from the Monday cockpit (weekly launch) and from `sniped-execution-prioritization` (competing tasks at a moment).

**Recommendation:** CREATE `sniped-pulse-check` skill. Trigger: "where are we," "quick status," "what's in flight," "any stalls," "catch me up." Inputs: no user input required. Reads: `NEXT_ACTION.md`, `ACTIVE_KNOWLEDGE_STATE.md`, the active wave `RUN_STATE.json` files, `ACTIVE_THREADS.md`. Output: a three-section status block (corpus state, production lanes, one next action) in under 200 words. No new strategy. Pairs with `sniped-monday-cockpit` (weekly) and `sniped-execution-prioritization` (competing-task decision). Keep the SKILL.md under 30 lines.

---

### 7. Tool/App Integration Audit

**Skill path:** None. No skill exists.
**What the plan says:** Phase 6 of OS_TAKEOVER defines this as a full ledger (`OS_TOOL_APP_INTEGRATION_LEDGER.csv`) covering all connected apps: available, authenticated, local-only vs cloud-ready, read/write/spend risk, best task, skill pointer, missing skill, test status, last verified date.

**Tested:** UNTESTED. The ledger does not yet exist.

**Recommendation:** This is Phase 6 work, not Phase 5. Do not create a skill now. When Phase 6 opens, create `os-tool-audit` skill (one-time + periodic). Output is the CSV ledger, not a strategy answer. The key design rule from the plan: "no installed-equals-useful claims, no spend-capable tool runs without approval, stale doc names carry warning labels." The skill should explicitly cover MCP server authentication state (Premiere/AE/Blender/ElevenLabs/Higgsfield local-only flags), credit-spend risk, and routing to the right skill or workflow. Defer to Phase 6.

---

### 8. Client Delivery Wrap (sniped-post-delivery)

**Skill path:** `.claude/skills/sniped-post-delivery/SKILL.md`

**Tested:** UNTESTED. No receipt. The memory entry `alma-love-production-standards.md` references delivery standards but no session save records `sniped-post-delivery` being invoked. No Pixieset gallery delivery session was found in `session_saves/`.

**Trigger assessment:** The frontmatter description is appropriately tight: "gallery is ready to send," "client received delivery, what's next," "Op Kit upsell timing," "how do I get a testimonial/referral." The SOP output (Day 0 through Day +60 cadence) is specific and actionable.

**Content assessment:** The MANDATORY READING references 4 source files including the locked SOP and 9 email templates. The REFUSE section is correct. The skill is well-formed but narrow to the SNIPED photography context. Length is appropriate.

**Recommendation:** LEAVE as-is. Run it on the next real gallery delivery to generate the first receipt. The biggest risk is the source files it reads (`SOP_post_delivery.md`, `email_templates/`, `pixieset_config.md`) going stale if the delivery process evolves. Add a "source freshness" check: the first step of the skill should verify the dates of those source files match the current year before proceeding.

---

## High-Priority Workflow Assessments

### adversarial-verify.workflow.js

**Exists:** Yes. `.claude/workflows/adversarial-verify.workflow.js`
**Tested:** YES (cited evidence). Memory entry `os-orchestration-upgrade.md` confirms it was built and used. Memory entry `alma-reel-footage-ceiling.md` cites it ran as part of the `alma-v5` harness (5 adversarial-verify agents + verdict). The synergy 3-shot proof ran it via `synergy-3shot-verify.workflow.js` (itself calls fresh-context skeptics on the same axes). The book cert waves used adversarial verify per OS_RECEIPT.md entries.
**Over/under-trigger:** The workflow is args-driven (target + claim + optional axes), so it does not auto-trigger on its own. It is always called by another workflow or the operator. Under-trigger risk is the real risk: production sessions skip it when time-pressured.
**Recommendation:** LEAVE. This is the backbone of the verify lane. Wire it more tightly into `os-command-router` exit gates: every Execution mode that produces a visual or film artifact should name adversarial-verify as the required exit gate, not optional.

---

### ai-edl.workflow.js

**Exists:** Yes.
**Tested:** UNTESTED. No session save or memory entry records a run. The workflow is generic and reusable (not project-specific). It has a clear 10-phase structure (Inventory → Selects → Beat map → EDL build → Durations → Transitions → Sound → Continuity → Gaps → QA + proof).
**Over/under-trigger:** The `whenToUse` is correct: "after assets exist and before any NLE timeline is cut." It is not being used because the Alma editing work used the project-specific `alma-v5` and `alma-her-film-edl` workflows instead.
**Recommendation:** LEAVE, but surface it in the router as the default edit-planning workflow when project-specific workflows are absent. The generic `ai-edl` should be the fallback for any new film/short/campaign edit that does not yet have a project workflow. Add it to `os-command-router` under the Execution/Design mode for "edit planning" tasks.

---

### alma-v5.workflow.js

**Exists:** Yes.
**Tested:** YES (cited evidence). Memory entry `alma-reel-footage-ceiling.md` confirms: "the alma-v5 7-role harness (`.claude/workflows/alma-v5.workflow.js`, run wf_cebfe65a-73f, 24 agents) ran V5 end to end." Result: 13.83s cut, verdict no-send, material ceiling identified.
**Over/under-trigger:** Project-specific (Alma Love reel). Cannot over-trigger for non-Alma work.
**Current status:** The Alma realistic 3-model video lane is RETIRED per the memory entry `alma-realistic-3model-pivot.md`. The reel work is parked.
**Recommendation:** LEAVE but tag as PARKED (not retired, because the harness architecture is reusable as a template). Add a comment in the workflow: `// STATUS: PARKED. Alma video lane retired 2026-06-19 (KEN FILM refunded). Harness pattern is canonical for future 7-role recuts.`

---

### alma-4k-qa.workflow.js

**Exists:** Yes.
**Tested:** UNTESTED. No memory entry or session save references a run. The workflow is a role-scoped whole-watch QA harness for the Alma 4K master.
**Status:** The Alma video lane is RETIRED. This workflow has no active target.
**Recommendation:** PARK. Same note as alma-v5: leave on disk as a QA harness template. No action needed beyond a status comment.

---

### alma-ai-edl.workflow.js and alma-her-film-edl.workflow.js

**Exists:** Yes (both).
**Tested:** `alma-her-film-edl` is UNTESTED. `alma-ai-edl` is UNTESTED. No run receipts found.
**Status:** Both are Alma-video-lane specific. Lane RETIRED.
**Recommendation:** PARK. Leave on disk as template artifacts. No investment in these.

---

### creative-levelup.workflow.js

**Exists:** Yes.
**Tested:** UNTESTED. No memory entry or session save records a run. The workflow has a clear, generic shape (takes weak creative material, upgrades it through the OS doctrine packs, emits a structured upgrade packet with adversarial scorer). No project-specific hardcoding.
**Over/under-trigger:** This should fire before any AI film / brand campaign / launch story generation spend. Under-trigger risk is HIGH: sessions tend to go directly to generation prompts without a concept-upgrade gate.
**Recommendation:** TIGHTEN FRONTMATTER + ROUTE. Add to `os-command-router` as the required pre-production gate for "film," "campaign," and "brand story" Execution mode tasks. The workflow's comment block already says "runs BEFORE the creative/AI-film pipeline, never after" but this is not enforced by the router. First test: run it on the next new creative brief.

---

### higgs-levelup.workflow.js

**Exists:** Yes.
**Tested:** YES (indirect cited evidence). Memory entry `higgsfield-photoreal-cinema-playbook.md` is tagged "PROVEN" and describes the realism upgrade extracted from Higgsfield tutorial transcripts. That memory entry is the output artifact of this workflow's Synthesize phase. The photoreal cinema playbook was built from a whole-read run of Higgsfield transcripts. Evidence is indirect (the memory names the playbook as proven but does not cite a workflow run ID). Classifying as TESTED (evidence-backed).
**Current status:** The workflow requires input args (`dir`, `groups`) pointing to transcript files. Those transcripts were processed. The playbook is now doctrine. This is a one-time metabolization workflow.
**Recommendation:** LEAVE. Its output (the photoreal cinema playbook) is in canon. No need to re-run unless new Higgsfield tutorial transcripts arrive. If they do, re-run with the new dir/groups.

---

### synergy-3shot-verify.workflow.js, synergy-shot2-reverify.workflow.js

**Exists:** Yes (both).
**Tested:** YES (cited evidence). Memory entry `ai-performance-shot-method.md` explicitly cites both: "Workflows: `.claude/workflows/synergy-3shot-verify.workflow.js` + `synergy-shot2-reverify.workflow.js`." The proof is described in detail: 3-shot competence proof ran, adversarial verify 3/3 cinema pass, identity-locked, slop-free.
**Status:** Project-specific (Synergy HomeCare). The proof is closed. The architectural pattern (per-shot hostile verify, endpoint-diff gate, 4 axes) is the canonical reusable shape.
**Recommendation:** LEAVE as canonical reference implementations of the per-shot adversarial verify pattern. Any new short film should clone this shape, not invent a new one.

---

### synergy-3shot-verify-v3.workflow.js, synergy-hero-v4-reverify.workflow.js, synergy-bestof-verify.workflow.js, synergy-keyframe-select.workflow.js, synergy-film-verify.workflow.js

**Exists:** Yes (all five).
**Tested:** UNTESTED (no run receipts found in memory or session saves for these specific variants).
**Status:** All are project-specific Synergy variants for progressively later-iteration work (excellence pass v3, hero v4 reverify, best-of selection, full film verify). The Synergy proof closed at the 3-shot level; none of these later workflows have run.
**Recommendation:** PARK. They are project-specific and their target (Synergy HomeCare film) has not advanced past the 3-shot proof stage. Tag as PARKED with a note: "Synergy film not in active production as of 2026-06-21. These run when the film advances to full-film production." Do not delete; the architectural patterns are valuable templates.

---

## corpus-wave-runner Skill Recommendation

**Verdict: CREATE.**

The `build_wave.py` pattern has been used for 3+ waves (002-E, 002-F, 002-G) with identical structure. The gap is the operator-facing wrapper. A `corpus-wave-runner` skill fills exactly this gap without replacing the Python script.

**Proposed SKILL.md (draft):**

```
name: corpus-wave-runner
description: Run a book-certification or corpus-metabolization wave end to end using the build_wave.py controller. Wraps the ledger preflight, wave build, progress monitoring, and resume path. Use when running a DOCTRINE_EXTRACTION_SCHEDULED wave (002-E/F/G or future), resuming from RESUME_QUEUE.md, or checking a wave's RUN_STATE.json for stalls. Argument: wave ID (e.g., 002-E).

Steps:
1. Preflight: confirm BOOK_CANON_CERTIFICATION_LEDGER.csv has rows where wave==$ARGUMENTS and status_v2==DOCTRINE_EXTRACTION_SCHEDULED. If zero rows, halt.
2. Check os_cost_guard lock: if a wave is already in flight, halt and surface the active wave.
3. Run: python3 <control_dir>/build_wave.py $ARGUMENTS <control_dir>.
4. Monitor RUN_STATE.json for progress and stall.
5. If stalled: read RESUME_QUEUE.md and surface the resume instruction.
6. After wave completes: run jsonl-validation on the output batch, then hand off to master-consolidation.

Rubric reference: 00_COMMAND_CENTER/_standards/CORPUS_WAVE_RUNNER_RUBRIC.md (segment ledger gate, adversarial verify, dual-ledger flip, never-sample, no false completion).
```

**Rubric move:** Create `00_COMMAND_CENTER/_standards/CORPUS_WAVE_RUNNER_RUBRIC.md` containing the full per-book certification standard (5 doctrine fields, segment-count > 0, adversarial verify pass, dual-ledger flip from DOCTRINE_EXTRACTION_SCHEDULED to ACTIVE_DOCTRINE_BOUND). This keeps the skill under 30 lines.

---

## Skills Not Assessed in the High-Priority List (Spot Notes)

These were inspected during the audit and are noted briefly:

| Skill | Status | Note |
|---|---|---|
| `source-inventory` | TESTED (session saves May 2026) | Core corpus pipeline, runs clean |
| `staging-plan` | TESTED (session saves May 2026) | Recommend-only, no execution, correct |
| `batch-extraction` | TESTED (session saves May 2026) | 10+ batch scripts prove the pattern |
| `jsonl-validation` | TESTED (session saves May 2026) | Ran on every batch, gates master-consolidation |
| `master-consolidation` | TESTED (session saves May 2026) | Receipt per batch in session saves, 5/5 reconciliation gate pattern |
| `session-save` | TESTED (session saves May 2026) | 20+ save files confirm it ran |
| `adversarial-verify` (skill) | N/A | This is a workflow, not a skill |
| `os-command-router` | UNTESTED (as a formal invoke) | Applied ad-hoc from context; no receipt confirming it was invoked as a skill |
| `os-quality-gates` | UNTESTED (as a formal invoke) | Applied doctrinally; no formal invoke receipt |
| `os-vision-reject-gate` | UNTESTED | Scripts referenced (`os_vision_gate.py`) do not exist in `scripts/` yet |
| `os-face-lock` | UNTESTED | Test script `test_facelock.py` referenced in SKILL.md does not exist on disk |
| `banana-pro-director` | UNTESTED (skill invoke) | The method is in use (Alma stills produced), but via MCP direct, not skill invoke |
| `cinema-worldbuilder` | UNTESTED (skill invoke) | Same pattern as banana-pro-director |
| `composite-master-qa` | UNTESTED (skill invoke) | Doctrine is applied in memory; no receipt of skill-path invoke |
| `platform-mastering` | UNTESTED (skill invoke) | Same |
| `sniped-strategy-execution` | UNTESTED | No receipt; ad-hoc strategy is the pattern |
| `sniped-shortform-retention` | UNTESTED | Recently created, no receipt |
| `sniped-app-builder` | UNTESTED | No app build in sessions |
| `sniped-web-builder` | UNTESTED | No web build receipt |
| `sniped-crs-builder` | UNTESTED | `os_crs.py` referenced but not confirmed in scripts/ |
| `watch` | TESTED (cited evidence) | Used on Higgsfield transcripts, whole-watch pattern proven |

---

## Summary Recommendations Table

| Priority Work Item | Action | Rationale |
|---|---|---|
| `sniped-project-intake` | Tighten frontmatter + add router gate | UNTESTED, under-triggers; run on next real client project |
| `corpus-wave-runner` | CREATE new skill | Pattern proven (3+ waves); no skill wrapper exists |
| Docs/tooling metabolization | Extend `corpus-wave-runner` (--mode docs_tooling) | One-time program done; reusable pattern, not a standalone skill |
| `external-visual-proof-gate` | CREATE new skill | Doctrine exists, no skill enforces packet-build + routing |
| `sniped-monday-cockpit` | Leave + schedule as Routine (Phase 6) | UNTESTED, tighten source-freshness check |
| `sniped-pulse-check` | CREATE new skill (short) | Gap identified; no mid-session state check skill exists |
| `sniped-operator-plan` | Do not create | Redundant; covered by monday-cockpit + pulse-check |
| Tool/App Integration Audit | Defer to Phase 6 | Phase 6 work; create `os-tool-audit` then |
| `sniped-post-delivery` | Leave + run on next gallery | UNTESTED; add source-freshness check to first step |
| `adversarial-verify` workflow | Leave + route from os-command-router | Core verify lane, proven, under-invoked |
| `ai-edl` workflow | Leave + add to router as default | UNTESTED; generic, reusable, should be default edit harness |
| `creative-levelup` workflow | Tighten router gate (pre-production required) | UNTESTED; under-invoked because not gated before generation |
| `alma-v5`, `alma-4k-qa`, `alma-ai-edl`, `alma-her-film-edl` workflows | Park (lane retired) | Add status comment; preserve as harness templates |
| `synergy-*` v3/v4/bestof/keyframe/film workflows | Park | UNTESTED; Synergy film not in active production |
| `synergy-3shot-verify`, `synergy-shot2-reverify` | Leave as canonical reference | TESTED; proven per-shot adversarial verify pattern |
| `higgs-levelup` | Leave | TESTED (output is photoreal cinema playbook in canon) |
| `os-face-lock` | Fix (test script missing) | `test_facelock.py` referenced but not on disk; scripts `os_herolock.py` etc. also not confirmed |
| `os-vision-reject-gate` | Fix (script missing) | `os_vision_gate.py` referenced but not in scripts/ |

---

## Phase 5 Acceptance Criteria Status

| Criterion | Status |
|---|---|
| No skill counted as live without a test | PASS: Hard "UNTESTED" labels on every unproven skill |
| Stale or over-triggering skills tightened | PARTIAL: Frontmatter tightening deferred to creation pass |
| New skills: corpus-wave-runner, external-visual-proof-gate, sniped-pulse-check | PENDING (recommended; not yet created) |
| Corpus-wave-runner rubric moved to reference doc | PENDING |
| Skills with missing referenced scripts flagged | PASS: os-face-lock, os-vision-reject-gate flagged |

---
## ADVERSARIAL-VERIFY NOTES (verdict PASS, grounded=true)
- CORRECTION: build_wave.py exists ONLY at `OS_CERT_WAVE_002E/control/build_wave.py`; it was REUSED by 002-F/002-G (invoked with their control dirs as args), NOT copied/mirrored into 002F/002G control folders. The 'mirrored' phrasing is inaccurate; the single 002E script is the shared engine.
