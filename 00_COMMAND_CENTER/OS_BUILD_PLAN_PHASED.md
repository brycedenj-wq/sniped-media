# OS BUILD PLAN , PHASED BY DEPENDENCY (2026-06-04)

> Reordered from the flat first-10 list into dependency order. The rule that drives the order: nothing downstream is allowed to execute on top of a fake or unstable layer. Skills before character, character before world, world before video, video before distribution. Remove fake capability first.

## Dependency logic (why this order)
1. **Skills are the substrate.** Every later build is delivered partly as a skill. If "skill = active" is a lie (drafted-but-not-installed counted as capability), every later phase inherits the lie. So the activation contract + registry come first.
2. **Character + world are the atom.** A repeatable channel needs one original character, one world, one visual language that survive multiple outputs. Build this before any motion.
3. **Video without CRS + world = random motion slop.** Motion only earns its place once it can render *the same character in the same world*. So video depends on Phase 1.
4. **Posting/proof cannot activate until the production atom is stable.** You cannot run a real proof loop on an unstable output. Distribution + proof come last, and stay gated behind explicit human go.

## Honest count correction
The drafted skill pool is **51** (`raw/_skills/sniped-*`), not 57. The prior "57+50" figure was drafted + a separate 50-pack reference; this plan tracks the 51 installable `sniped-*` skills and grades them against the activation contract. No number is trusted until the registry prints it.

---

## THE ACTIVATION CONTRACT (applies to every skill, every phase)
A skill counts as **ACTIVE** only if ALL six hold. Anything less is named honestly, never as active.
1. **installed** , exists at `.claude/skills/<name>/SKILL.md`
2. **discoverable** , valid frontmatter with `name` + non-empty `description`
3. **trigger** , an `## INVOKE WHEN` / `## Trigger` section, or a "Use when..." trigger in the description
4. **inputs/outputs** , explicit `## Inputs` and `## Outputs`
5. **tests** , a `## Test` section with >=1 concrete case (or a sibling test file)
6. **invokable** , frontmatter `name` == dir name, valid kebab-case

Status tiers: **ACTIVE** (all 6) · **INSTALLED_INCOMPLETE** (installed, missing >=1) · **DRAFTED** (valid but not installed) · **MALFORMED** (fails structural parse). The registry is the single source of truth for which is which.

---

## PHASE 0 , Skill activation substrate (EXECUTE NOW)
**Goal:** make "active" mean something, then grade the whole pool honestly. No fake activation.

**Files to create**
- `scripts/os_skill.py` , CLI: `lint`, `new`, `install`, `registry`, `audit`.
- `scripts/test_skill_substrate.py` , regression suite for the substrate.
- `.claude/skills/skill-template/SKILL.md` , a born-compliant reference skill that lints ACTIVE (proof the contract is achievable).
- `OS_SKILL_REGISTRY.csv` , the source of truth (name, installed, status, missing, source, description).
- `OS_SKILL_DASHBOARD.md` , human-readable counts by tier.

**Definition of done**
- `os_skill.py lint --all-installed` and `--all-drafted` run and grade every skill.
- The 51 drafted skills are installed (those passing structural lint) or reported as MALFORMED, never silently dropped.
- No skill is marked ACTIVE unless all 6 criteria pass (enforced + tested).
- `test_skill_substrate.py` passes 100%.
- `OS_SKILL_REGISTRY.csv` + `OS_SKILL_DASHBOARD.md` written with true tier counts.

**Tests (test_skill_substrate.py)**
- scaffolded `new` skill lints ACTIVE.
- a skill missing `## Test` grades INSTALLED_INCOMPLETE, not ACTIVE.
- malformed frontmatter grades MALFORMED and is refused on install.
- install never overwrites an existing skill without `--force`.
- registry CSV has the correct header and one row per skill.
- invariant: ACTIVE implies all 6 criteria true.

---

## PHASE 1 , Character + world atom
**Goal:** one original (non-real, non-celebrity) character + one world + one visual language that survive multiple outputs.

**Files to create**
- `scripts/os_crs.py` , build a 14-ref character sheet (front/side/3-4/back/expressions) + compute a cross-frame identity-consistency score; quarantine drift.
- `.claude/skills/sniped-crs-builder/SKILL.md` , the CRS workflow skill (born-compliant).
- `.claude/skills/os-world-bible/SKILL.md` , 7-env rotation + lineage texture → a locked world bible paragraph + sref slots.
- dashboard hook: CRS + world status rows.

**Definition of done**
- `os_crs.py` produces a 14-ref manifest for one character and a consistency score across >=3 frames, with a drift-reject gate.
- both skills lint ACTIVE.
- a real CRS run exists for one original character (no real/celebrity likeness), recorded.

**Tests (extend test_production_harness.py + new test_crs.py)**
- CRS refuses to proceed without a validated base identity.
- consistency score below threshold quarantines the frame (no silent pass).
- world-bible output contains a locked environment from the 7-env rotation + >=3 sref slots.
- identity-leak guard: CRS rejects any input flagged as real-person/celebrity reference.

---

## PHASE 2 , Video / motion (depends on Phase 1)
**Goal:** render the SAME character in the SAME world in motion, gated so no slop ships.

**Files to create**
- `os_generate.py` video path , `generate_video` + `job_status` poll + ingest + cost gate.
- `scripts/os_motion_qa.py` , motion reject gate: grounding, edge integrity, physics, AI-tell, identity-hold-across-frames.
- `.claude/skills/kling-production-sop/SKILL.md` , video routing + 3-tier polish + dialogue-free SOP.

**Definition of done**
- a motion clip generates for the Phase 1 character + world, passes motion-QA, and beats source.
- video path blocks on no-prompt / over-budget exactly like the image path.
- skill lints ACTIVE.

**Tests (test_motion.py)**
- video generation blocks without a prompt record and over budget.
- motion-QA quarantines a clip that fails grounding/identity-hold (no silent pass).
- bad/short download → FAILED, no placeholder asset (mirrors the image-path guarantee).

---

## PHASE 3 , Posting / proof (depends on a stable atom)
**Goal:** be ready to run a real proof loop on command, never before approval, never faked.

**Files to create**
- `scripts/os_post.py` , posting handoff: identity-scrub on metadata + scheduled-draft, hard human-go gate (no auto-post).
- `scripts/os_proof.py` , ingest saves/shares/DMs/print-intent → proof dashboard; compute kill/keep/scale.

**Definition of done**
- `os_post.py` refuses to post without explicit `--go` and fails if any real name appears in metadata/handle/WHOIS descriptor.
- `os_proof.py` writes a proof row only from real logged signal (no synthetic numbers) and computes the signal verdict.
- both wired to the dashboard.

**Tests (test_distribution.py)**
- post blocks without `--go`.
- post blocks if metadata contains a real-name pattern.
- proof refuses a row with no underlying signal record (no fake proof).
- kill/keep/scale computed correctly from sample signals.

---

## FIRST LIVE TEST (after Phases 0-2)
One pseudonymous brief → one character (Phase 1) → one world (Phase 1) → one still + one motion clip of that same character in that world (Phase 2) → gated → captioned → posting handoff staged but NOT posted (Phase 3, awaiting go) → proof row scaffolded. Proves the atom holds across stills and motion before anything is distributed.

## Binding rules (all phases)
No strategy map · no lane ranking · no real likeness · no celebrity likeness · no employer data/tools/relationships/identity leakage · no "done" without a passing test · every build adds a regression test · every failed test becomes a build item · every new capability updates the dashboard. Drafted is called drafted; doctrine is called doctrine; executable is proven with a test.
