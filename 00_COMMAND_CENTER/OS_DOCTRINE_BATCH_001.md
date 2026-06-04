## DOCTRINE ENTRIES

### Consolidation map (read before the blocks)
The 11 docs fall into 4 families. Repeated doctrine is written once at the family level, then each doc carries only its delta.

- **Family A · Corpus-pipeline / inventory hygiene** (4 docs): `DOWNLOADS_INVENTORY_2026-05-18.txt`, `SNIPED_OS_FULL_SOURCE_INVENTORY_2026-05-18.md`, `SNIPED_OS_STAGING_PLAN_2026-05-18.md`, `BATCH_007_PLAN.md`
- **Family B · OS spine / governance synthesis** (3 docs): `SNIPED_OS_V1_SYNTHESIS_2026-05-12.md`, `MASTER_OS_SYNTHESIS.md`, `COMMAND_ROUTER.md`
- **Family C · Execution + reality audit** (2 docs): `100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md`, `EXECUTION_PRIORITIZATION.md`
- **Family D · Production runbook + portable-method proof** (2 docs): `PRODUCTION_OS.md`, `165_building_antique_insights_brand_strategy.md`

---

### FAMILY A · Corpus-pipeline / inventory hygiene

**Shared doctrine (consolidated once, applies to all 4 Family A docs):**
- **TEACHES:** The operator's failure mode is not scarcity of knowledge, it is duplication and version-sprawl (Direction Stack in 30+ variants, Master Operating Document in many). A source is canon only after version-resolution picks one instance; raw count is noise. The source universe is one bounded, read-only folder (`~/Downloads/    SNIPED_OS`, 4 leading spaces), never "Downloads." Inventory before assuming, diff before staging, never let the corpus drift into processing the whole disk.
- **APPLIES:** AI systems / corpus integrity. The brain is bounded and staged-but-unfinished; when a skill leans on derived intel, treat the underlying primary source as not-in-corpus until the batch that loads it has run.
- **REJECT:** All date-stamped counts (chunk totals, source counts, SOS-only basenames, "latest batch") are 2026-05-18/19 snapshots, not live state. Re-diff against `ACTIVE_KNOWLEDGE_STATE.md` / `MASTER_INDEX.md` before acting. Never chunk lock-files (`~$*`), `.part`/`.crdownload` partials, `(1)(2)(3)` copies, raw AI outputs (`hf_*`, `Gemini_Generated_*`, `kling_*`), DMG installers, presets, or `.DS_Store`. Superseded CH01_Yae 9-PNG card set is dead (05-13 B&W dual-register lock). `SNIPED_PRESETS.zip` is pre-v3, stale.
- **SKILL CANDIDATE (shared):** Mostly covered by existing `source-inventory` + `staging-plan` skills (these docs are outputs of that chain). One genuinely missing layer: **canon-dedup / version-resolution** (group files by semantic stem, rank variants by version token Final > v2 > Revised > dated > `(N)`, pick canonical, quarantine the rest). Fold as a checklist into `staging-plan` rather than spawn a new skill.

**Per-doc deltas:**

| Doc | Delta over Family A shared doctrine |
|---|---|
| `DOWNLOADS_INVENTORY_2026-05-18.txt` | The raw census (2,737 path entries). Its unique signal: **three operator identities physically interleaved on one disk** (SNIPED founder / field-commissioning engineer / personal-life operator). Lane-separation is a hard ingestion boundary, not a nicety. Hard scope: do not chunk anything outside lines 1-118 (`    SNIPED_OS/`) without operator instruction. |
| `SNIPED_OS_FULL_SOURCE_INVENTORY_2026-05-18.md` | The bounded census + staging recommendation (727 files, 5.1 GB, 242 unstaged in 15 buckets A-O). Unique signal: the craft/advertising/AI/culture primary sources the skills cite are largely **not yet loaded**. §8.2 deep sub-categorization is an unauthorized proposal, an operator call, not a decision. |
| `SNIPED_OS_STAGING_PLAN_2026-05-18.md` | The staging manifest (18-category book taxonomy). Unique doctrine: **staging is a read-only planning act; mutation requires explicit operator authorization in a separate session** (plan and execution never share a session). **Operating-hygiene scaffolding is tooling, not canon** (worksheets, course transcripts never outweigh CANONICAL_TRUTHS / WWP / Direction Stack). Open loops: 3 chapter-slot collisions (05/08/13) need a global rename before any batch reads from those folders; the 7th late-add file needs a second authorization. |
| `BATCH_007_PLAN.md` | Plan to chunk the 55-file doctrine layer (~128 chunks). Two unique durable rules: **ephemeral state is never chunked** (live-state docs read fresh at session start; chunking volatile state manufactures staleness), and **supersede with a trail, never a silent overwrite** (STALE-FLAG the stale chunk, de-prioritize on retrieval, keep provenance). Live flag: the `$2K × 3mo` Phase-B trigger here CONFLICTS with `sniped-retoucher-onboarding` memory (`$3K × 2mo`). Operator must reconcile once. |

---

### FAMILY B · OS spine / governance synthesis

**Shared doctrine (consolidated once, applies to all 3 Family B docs):**
- **TEACHES:** The OS is one sentence: three engines (Revenue funds Reputation, Reputation creates Audience, Audience drives Revenue), funded by $1,500 founder portraiture, compounding over a 10-year arc into the named visual documentarian of LA's emerging Black founder/operator/artist/athlete culture. The moat is the empty intersection: editorial rigor + cultural documentation + operator-coded methodology. The methodology IS the product (Direction Stack); the photo is the deliverable. The refusal list is the brand. Phase = trigger-defined state, not calendar. Lean is permanent, not a Phase-1 condition.
- **APPLIES:** SNIPED spine, brand, AI hybrid stance (AI for world-construction, anti-identity-AI on deliverables), all routing/governance.
- **REJECT (shared stale tokens):** Adobe Portrait → use **v3 LUXURY / Adobe Neutral**. "3 VIBs/week" → use **6/week**. Flat "anti-AI" → use **hybrid operator**. 2-engine labels → **3-engine model**. BASEPLATE "optional/historical" framing → CURRENT_STATE LOCKED wins. Any blanket "BANNED / REFUSED" reflex → reclassify under the 5-class taxonomy. Date-bound proof-loop status (AlmaLove Kennedie 5/30, casting dates) is past, read as superseded by STANDING_ORDER.
- **SKILL CANDIDATE (shared):** Mostly already skilled (`sniped-command-router`, `sniped-os-execution-governor`, `sniped-canonical-truths`, etc.). Two genuinely new: **corpus-contradiction sweep** (scan corpus for a known stale token, report every doc still carrying it) and **corpus-retrieval** (`sniped-corpus-retrieve`: MASTER_INDEX → domain→batch map → grep/jq → cite `[BATCH_NNN_chunk_NNN]`), worth building only if router corpus-citation rate stays at 0%.

**Per-doc deltas:**

| Doc | Delta over Family B shared doctrine |
|---|---|
| `SNIPED_OS_V1_SYNTHESIS_2026-05-12.md` | The original self-audit (1,144 lines, 300+ files). Unique durable principle: **"Run the office; the cathedral compounds"**, once architecture exists, refining it is the productive-avoidance trap; this doc is itself the artifact the Execution Governor warns against producing more of. Its "files NOT read" / "missing systems" gap lists are now **stale** (Lineage Doctrine, composite rotation, casting/cold-email/LinkedIn doctrines were subsequently built and locked). Treat as read-only reference, not a work queue. |
| `MASTER_OS_SYNTHESIS.md` (2026-05-29) | The true-state map. Unique contribution: the **5-class constraint taxonomy** (only 10 Class A hard constraints are refusable; B style / C tactical-defer / D not-in-rotation / E stale-lock all route), replaces blanket-ban framing OS-wide. Plus lane architecture (5 business × 9 enabling lanes) and **§13 corpus activation** (1,837 chunks built and never queried at decision-time). Open loop: confirm corpus wiring is actually exercised (citation rate >0%). |
| `COMMAND_ROUTER.md` (2026-05-29) | The intake classifier (15 input types). Unique load-bearing mechanic: the **INPUT-OR-TASK gate**, if the input asks for action, STANDING_ORDER goes FOREGROUND; if it is a question/idea/concern, STANDING_ORDER stays AMBIENT and the answer must NOT collapse into the active loop. Default mode is INPUT-READY, not STATE-OBEY. Plus §17 high-risk routing (security/legal/tax/payment classified FIRST, records stored OUTSIDE the OS) and §18 dry-test discipline (tests never mutate; report defect → propose patch → await separate-turn approval). **Editorial defects to patch (not doctrine):** 14-vs-15 type drift, duplicate step 6, 11-field vs "16-field" receipt mismatch with the skill. |

---

### FAMILY C · Execution + reality audit

**Shared doctrine (consolidated once, applies to both Family C docs):**
- **TEACHES:** The bottleneck is execution, not strategy. The architecture is over-built; doc-writing is productivity theater. **Motion is not progress; only tracked conversion counts** (docs, comments, posts, free shoots, networking are motion unless they become named pipeline). **Earn the right to scale**: no new tool/channel/hire/lane until the Minimum Viable Empire has produced a closed + delivered Reset + testimonial + Op-Kit-pitched + lived CRM data, including one deliberately-surfaced SLA failure. Capacity-full is the only trigger to raise price, never to discount.
- **APPLIES:** Cash (the $1,500 Reset is floor and forcing function; VIB → Discovery → Reset in 7-14 days is fastest cash), brand discipline (refuses follower/viral chasing as off-game), AI (Cultural Documentation = the AI-proof moat).
- **REJECT (shared):** The literal sprint calendars and 100-task list are consumed/PAUSED, source library, not live to-do. Financial Tier-1 tasks (Stripe/LLC/W-9) are **EIN-gated** (BASEPLATE vs Baseplate, LLC); non-payment work proceeds, payment rails wait.
- **SKILL CANDIDATE (shared):** `sniped-execution-prioritization` + `sniped-lean-audit` cover the call. One candidate: a **Pre-Scaling Gate Check** (run the gate checklist + Tier-9 suppression list against any proposed addition, return ADD or BLOCKED-WITH-REASON), fold into `sniped-lean-audit` rather than spawn new.

**Per-doc deltas:**

| Doc | Delta over Family C shared doctrine |
|---|---|
| `100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md` | The 100-question reality audit. Two unique durable reframes: **Speed-run OPTIONALITY, not survival** (AWS salary = unlimited runway; the pressure is psychological, not survival; urgency not panic), and **the buyer world is constructed, not claimed** (LA founders/operators is a deliberate 6-12 month build distinct from the current content world of models/creatives; methodology refines register, it does not generate it). Hard recalibration: **Phase B trigger lowered to $2K MRR × 3 months** (was $3K × 2). One skill candidate: `sniped-boost-gate` (48-72hr wait, saves >3% OR shares >1.5%, then $30/day × 7, 10-mi LA, never boost mediocre work). |
| `EXECUTION_PRIORITIZATION.md` | The Operating Map. Unique content: the 6-element Minimum Viable Empire spine, the Tier-9 active-suppression list (external-IP, cold-email, paid ads, TikTok/Reels, generalist work closed off for the 90-day window, intentional focus, not identity collapse), and the realistic field-engineer time budget (~10-12 hr/week sustainable, recovery non-negotiable). Carries the pre-override labels inline (2-engine, 3-VIB, 100-task), gate behind the 2026-05-06 canon header before surfacing. |

---

### FAMILY D · Production runbook + portable-method proof

These two share little doctrine; kept separate.

| Doc | Doctrine block |
|---|---|
| `PRODUCTION_OS.md` | **TEACHES:** Two-folder separation is law (`/SNIPED_OS/` strategy never mixes with `/SNIPED_PRODUCTION/` assets); naming is a search index; storage is 4-tier 3-2-1 (RAW never to cloud); the pipeline is **time-capped not perfection-driven** (Hero 12-15 min, hard stop 25; Reset 7-9 hr BJ-time, above = drift, below = corner-cutting); one shoot → 8 outputs; delegation is pre-specced with a permission matrix that hard-walls hires out of OS/RAW/CRM/Pixieset/Stripe/pricing; automation deferred until proven friction. **APPLIES:** SNIPED daily runbook, cash margin defense, brand quality, AI routing. **REJECT:** preset names `v1` → live standard is **v3 LUXURY + B&W Card dual-register**; "manual everything / Zapier-when-$3K" predates the 2026-05-28 Connected Toolchain Default; Calendly+Stripe deposit rail is **EIN-gated**. **SKILL CANDIDATE:** mostly covered (`sniped-production-os`, `sniped-capture-to-delivery`, etc.); one script worth building: **new-shoot folder + naming scaffold generator** (date + client + TYPE → locked 9-subfolder root on Hot+Warm). **MASTER-DOCTRINE DELTA:** (1) time-cap over perfection at every tier; (2) AI generates inputs, never the subject (Camp B, absolute). |
| `165_building_antique_insights_brand_strategy.md` | **TEACHES:** A full small-business launch run in chat for BJ's mother's antiques business (NOT a SNIPED client). Every SNIPED primitive proven portable on a non-photography business: positioning-by-vocabulary, authority mining, "First Look" list-building, audience-before-infrastructure sequencing, lean-hours cap, delegation trigger. Core thesis: solve **The Cash Trap** (seasonal/single-channel revenue → year-round list-owned direct-sell loop: IG Live selling + owned email list + always-on backup store, sequenced audience-first). **APPLIES:** SNIPED method portability (a candidate Baseplate "launch engine" offer), cash-resilience (anti-seasonality pattern usable for SNIPED's own off-cycles), connected-toolchain validation. **REJECT:** all 2025 dates historical; NOT subject to the $1,500 floor / Reset ladder / lineage doctrine; keep antiques tactics firewalled from SNIPED's luxury-editorial positioning. **SKILL CANDIDATE:** strong, `niche-business-launch-90day` (or `cash-trap-breaker`) as a **generalized, non-SNIPED-branded wrapper** to protect the photography lane; secondary `ig-live-selling-script`. **MASTER-DOCTRINE DELTA:** (1) anti-seasonality / Cash-Trap principle (generalizes to any lumpy-revenue operator); (2) the OS is method, not vertical (proven portable, is itself a leverage asset distinct from the photography proving ground). |

---

## DECISION JOURNAL (batch 001)

**2026-06-02 · OS Engagement whole-read batch 001 · 11 artifacts**

- `DOWNLOADS_INVENTORY_2026-05-18.txt`, No strategy delta. Canon already abstracted into memory intel docs; scope discipline already locked in AGENTS.md. Process change only: regenerate a fresh inventory and add a dedup/canonical-pick pass before the next staging pass. *Coverage: lines 1-2738 (last content 2737).*
- `SNIPED_OS_FULL_SOURCE_INVENTORY_2026-05-18.md`, Nothing new. BATCH_005 (photography canon) already locked in CLAUDE.md / ACTIVE_KNOWLEDGE_STATE.md; doc reinforces sequence. One open operator call: §8.2 deep-categorization vs §8.3 flat staging folder. Re-validate snapshot counts against live master files before any batch session. *Coverage: lines 1-714 (last content 713).*
- `SNIPED_OS_STAGING_PLAN_2026-05-18.md`, No strategy delta. Two operational opens belonging to the operator: authorize the 7th late-add file copy (BATCH_030), and globally rename the 3 chapter-slot collisions (05/08/13) before any batch reads those folders. *Coverage: lines 1-1089 (complete).*
- `BATCH_007_PLAN.md`, No strategy delta; plan-only, gated on operator authorization. One live conflict surfaced: Phase-B trigger reads `$2K × 3mo` here vs `$3K × 2mo` in `sniped-retoucher-onboarding` memory, operator must reconcile the canonical trigger once before either fires. *Coverage: lines 1-456 (complete).*
- `SNIPED_OS_V1_SYNTHESIS_2026-05-12.md`, Nothing structurally new; its recommendations were actioned into the memory lock layer (Lineage Doctrine, Execution Governor, hybrid AI, composite rotation). One live decision: treat as read-only reference, not a refinement queue; optionally run a one-time contradiction sweep to clear the stale tokens it named, then close. *Coverage: lines 1-1144 (complete).*
- `100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md`, This doc IS the source the memory layer was distilled from. One verification delta: confirm Phase-B trigger reads **$2K MRR × 3 months** everywhere downstream (this doc is the canonical override of $3K × 2). BASEPLATE $15K firewall is a standing decision, not re-litigated. Sprint calendars consumed. *Coverage: lines 1-697 (complete).*
- `MASTER_OS_SYNTHESIS.md`, Mostly already captured (5-class taxonomy, EIN gate, lane architecture live in memory + `sniped-command-router`). One net-new operational action: confirm §13 corpus wiring is exercised, if routing receipts still show "Corpus chunks retrieved: none," that is the open loop this doc creates. *Coverage: lines 1-750 (complete).*
- `COMMAND_ROUTER.md`, Architecture the memory entries point at; no strategy delta. Changes: fix editorial defects before using as a dry-test oracle (14-vs-15 type drift, duplicate step 6) via §18 report→propose→await-approval; reconcile receipt field count (11 vs "16-field" skill); reaffirm §17 stores sensitive records OUTSIDE the OS. *Coverage: lines 1-584 (complete).*
- `EXECUTION_PRIORITIZATION.md`, Mostly already metabolized (three-engine, 6-VIB override, $1,500 floor, Execution Governor, AI-proof Cultural Doc moat). Change: gate any future surfacing behind the 2026-05-06 canon header (3-engine relabel, 6-VIB, 12-task active surface, EIN-gate on financial Tier-1). *Coverage: lines 1-529 (complete).*
- `PRODUCTION_OS.md`, Strategic spine already in memory + CANONICAL_TRUTHS; doc operationalizes it. Two real deltas to action: patch the preset version reference (`v1` → **v3 LUXURY** + B&W Card dual-register), and re-baseline Sections 7.3-7.6 against the Connected Toolchain Default + EIN gate (do not treat manual-first / Stripe-rail instructions as current). *Coverage: lines 1-864 (complete).*
- `165_building_antique_insights_brand_strategy.md`, Net-new at the optionality level: first concrete proof the OS productizes into a repeatable outside-business launch service. Action: log "Antique Insights" as a portfolio proof point for a potential Baseplate launch-engine offer; consider extracting the generalized 90-day-launch skill. No change to SNIPED's photography spine, floor, or lineage doctrine; firewalled from the SNIPED brand. *Coverage: lines 1-152 (full transcript on line 4; source ends mid-sentence, not a read truncation).*

---

## MASTER-DOCTRINE ADDITIONS

The durable principles this batch contributes (deduped across all 11 docs):

1. **If it is not deduplicated, it is not canon.** A source becomes canonical only after version-resolution picks one instance; raw count is noise. *(Family A)*
2. **The disk holds three operators; the brain must keep them separate.** Lane-separation (SNIPED founder / field engineer / personal life) is a hard ingestion boundary, not a nicety. *(Family A)*
3. **Staging is a read-only planning act; mutation requires explicit operator authorization in a separate session.** Plan and execution never share a session. *(Family A)*
4. **Ephemeral state is never chunked; supersede with a trail, never a silent overwrite.** Volatile state read fresh at session start; stale resolutions get STALE-FLAGGED and de-prioritized, never deleted, so provenance survives. *(Family A)*
5. **Run the office; the cathedral compounds.** Once architecture exists, refining it is the productive-avoidance trap. Default response shape is action, not corpus refinement. *(Family B/C)*
6. **The refusals are the moat, and lean is permanent.** 65+ named refusals are the positioning asset; lean is the perpetual operating discipline, phases only swap which 3-6 loops are critical. *(Family B)*
7. **Refusal is a list of 10, not a reflex.** Only the 10 Class A hard constraints are refusable; everything else routes (B style / C tactical-defer / D not-in-rotation / E stale-lock). Activate before you add; the gap is the lever, not a failure. *(Family B)*
8. **Classify the input before consulting state; keep active work AMBIENT unless the input asks for it.** A question is not a task; answer the question asked, do not advance the loop you were already running. *(Family B)*
9. **Motion is not progress; only tracked conversion counts. Earn the right to scale.** No new surface until the MVE has produced a closed+delivered Reset + testimonial + Op-Kit-pitch + one surfaced SLA failure. Capacity-full raises price, never discounts. *(Family C)*
10. **Speed-run optionality, not survival; the buyer world is constructed, not claimed.** AWS = runway, so every decision is measured against next-decade optionality (urgency, not panic); the paying lane is a deliberate 6-12 month build distinct from the current content circle. *(Family C)*
11. **Time-cap over perfection at every tier; AI generates inputs, never the subject (Camp B, absolute).** The system ships to a clock; the Camp B line is what keeps the moat and the Berger/Sax defense intact. *(Family D)*
12. **The OS is method, not vertical; solve the Cash Trap with an audience-first, list-owned, year-round direct-sell loop.** The playbook is portable (proven on a non-photography business) and is itself a leverage asset distinct from the photography proving ground. *(Family D)*

---

## SKILLS TO EXTRACT

Ranked, deduped, with the existing-coverage note so nothing is rebuilt:

1. **Canon-dedup / version-resolution** (NEW, high value), group inventory files by semantic stem, rank variants by version token (Final > v2 > Revised > dated > `(N)`), pick canonical, emit a quarantine list. Fold as a checklist into the existing `staging-plan` skill. *(Family A)*
2. **`niche-business-launch-90day` / `cash-trap-breaker`** (NEW, strong), generalized, **non-SNIPED-branded** wrapper: brand-vocabulary lock + authority-mining interview + audience-before-website sequence + IG-Live 6-part item formula + First-Look list mechanics + idiot-proof inventory sheet + domain/email/card checklist + card-vs-loan financial frame + 90-day plan with lean-hours cap + delegation + stuck off-ramp. Build generic to protect the photography lane. *(Family D)*
3. **`sniped-boost-gate`** (NEW), go/no-go: wait 48-72hr after a HERO/Card, boost only if saves >3% of impressions OR shares >1.5%, then $30/day × 7, 10-mi LA, founder/operator targeting, never boost mediocre work. *(Family C)*
4. **Corpus-contradiction sweep** (NEW, conditional), scan the corpus for a known stale token (`Adobe Portrait`, `3 VIBs/week`, `anti-AI`, `$3K × 2`) and report every doc still carrying it. The highest-leverage maintenance workflow this batch begs for. *(Family B)*
5. **`sniped-corpus-retrieve`** (NEW, conditional), MASTER_INDEX → domain→batch map → grep/jq → cite `[BATCH_NNN_chunk_NNN]`, skip on already-strong categories. Build only if router corpus-citation rate stays at 0%. *(Family B)*
6. **New-shoot folder + naming scaffold generator** (NEW, script not skill), date + client last name + TYPE → locked 9-subfolder root on Hot+Warm with the naming pattern stamped. *(Family D)*
7. **Pre-Scaling Gate Check** (FOLD, not new), run the gate checklist + Tier-9 suppression list against any proposed tool/channel/hire/lane, return ADD or BLOCKED-WITH-REASON. Fold into `sniped-lean-audit`. *(Family C)*
8. **`ig-live-selling-script`** (NEW, secondary), 6-part formula (What it is → Unique details → Condition → Size → Story → Hook) + urgency/FOMO/connection phrase banks + practice-Live framing. Subset of #2. *(Family D)*

**Already covered, do not rebuild:** `source-inventory`, `staging-plan`, `batch-extraction`, `jsonl-validation`, `master-consolidation` (Family A pipeline); `sniped-command-router`, `sniped-os-execution-governor`, `sniped-canonical-truths`, `sniped-direction-stack` (Family B); `sniped-execution-prioritization`, `sniped-lean-audit` (Family C); `sniped-production-os`, `sniped-capture-to-delivery`, `sniped-luxury-edit`, `sniped-post-shoot-same-day`, `sniped-retoucher-onboarding`, `sniped-pixieset-gallery`, `sniped-caption-writer` (Family D).

**Optionality guard on this list:** Skills 2 and 8 are deliberately generic/non-SNIPED-branded so the OS-as-method stays a separable Baseplate leverage layer and never collapses BJ into the single photographer identity. The dedup and contradiction-sweep skills (1, 4) preserve optionality by keeping superseded positions visible and reopenable rather than silently overwritten.
