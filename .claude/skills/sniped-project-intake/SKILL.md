---
name: sniped-project-intake
description: Intake a messy client/project brief and build a clean PROJECT CAPSULE before any production. Separates truth from noise, flags conflicts and missing inputs, routes to the right domain/skill/workflow, and keeps project-specific facts in the capsule (never in the permanent OS). Use when a task starts from a messy brief, raw notes, a new client/project, or "rescue/turn this messy X into Y". The capsule-first gate for any real client work.
---

# SNIPED Project Intake

Capsule-first. Before producing anything for a project, build the project capsule so the OS works from clean project truth and the permanent OS stays uncontaminated.

## When to use
A messy brief, raw client notes, a new client/project, or "rescue this messy brief / turn this messy idea into <deliverable>". Run this BEFORE the production skill/workflow. Pairs with `OS_RUNTIME_CONTRACT.md` and `PROJECT_CAPSULE_TEMPLATE.md`.

## Inputs required
Whatever the user has (notes, links, files, voice-dump). Nothing else is needed to START; gaps become HUMAN-INPUT REQUIRED entries in the capsule.

## Steps (executable)
1. **Dump-to-capsule:** copy `PROJECT_CAPSULE_TEMPLATE.md` to the project folder and fill every field from the input.
2. **Separate truth from noise:** sort notes into `approved_truth` (confirmed/locked) vs `client_notes` (raw) vs `conflicting_notes` (contradictions). Never silently pick a side of a conflict; flag it.
3. **Inventory assets honestly:** list `usable_assets` / `unusable_assets` by path. Mark a file "inspected" ONLY if you actually opened it; otherwise mark uninspected.
4. **Name the gaps:** anything missing that the work needs -> `human_input_required`; any current tool limit/credit/API -> `external_check_required`.
5. **Classify + route:** identify the deliverable domain (film / web / app / brand / copy / offer / strategy / short-form) and name the skill or workflow that will execute (creative-levelup, ai-edl, sniped-web-builder, sniped-app-builder, sniped-shortform-retention, sniped-pricing-decision, sniped-strategy-execution).
6. **Set status:** `approval_status` = draft, `send_no_send` = NO-SEND (default until proof + operator approval).
7. **Hand off:** pass the capsule to the chosen production path; the production path reads project truth FROM the capsule, not from the permanent OS.

## Output format
A filled `PROJECT_CAPSULE.md` in the project folder + a one-line routing decision (domain + skill/workflow + what is blocked on human input).

## Quality gate (pass/fail)
- Every capsule field addressed (blank = explicitly marked HUMAN-INPUT REQUIRED, not guessed).
- Truth vs noise separated; conflicts flagged, not resolved silently.
- No invented product/identity/taste facts.
- No asset claimed inspected without actually opening it.
- `send_no_send` = NO-SEND until proof passes.

## Proof / receipt
The capsule IS the intake proof. On a serious task the conductor RECEIPT (OS_RECEIPT) still applies to the production output. Log: capsule built, truth/noise split, gaps flagged, route chosen.

## Ask the human when
Objective, deliverable spec, deadline, real product/identity/asset, or taste target is missing or contradictory. These gate the dependent production steps.

## Contamination boundary (the point of this skill)
Project facts (product color, client identity, taste notes, brand marks) live in the capsule and are used by the OS for THIS project only. They are NEVER written into `os_doctrine.py`, memory, `OS_ACTIVATION_INDEX.json`, the standards, or any skill. A fact graduates to the permanent OS only if it is GENERAL (true for any client) and passes the doctrine proof bar.

## Depends on
OS_RUNTIME_CONTRACT.md, PROJECT_CAPSULE_TEMPLATE.md, os-quality-gates, os_proof_manifest / os_receipt (proof gate). Routes to the lane skills/workflows listed in step 5.


## Gates
- Every capsule field addressed (blank = explicitly HUMAN-INPUT REQUIRED, not guessed)
- Truth vs noise separated; conflicts flagged, not silently resolved
- No invented product/identity/taste facts
- No asset claimed inspected without actually opening it
- send_no_send = NO-SEND until proof passes; project facts stay in the capsule and are never written into OS_ACTIVATION_INDEX.json, memory, standards, or any skill

## Test
- case: Operator drops a voice-dump note: 'Kennedie wants a brand video for Alma Love Club, something like her IG reel but more editorial, she mentioned coral and cream colors, deadline is unclear, she sent 3 files.' Intake copies PROJECT_CAPSULE_TEMPLATE.md to the project folder, sorts the note into approved_truth (brand name: Alma Love Club, reference: IG reel, color notes: coral and cream) vs client_notes (raw style description) vs conflicting_notes (none yet). Asset inventory lists the 3 files as uninspected until actually opened. Gaps flagged as HUMAN-INPUT REQUIRED: confirmed deadline, deliverable spec (length, format, platform), taste target beyond IG reel. Routing decision: domain = film/brand video, skill = creative-levelup + ai-edl, blocked on deadline + deliverable spec. send_no_send = NO-SEND.
- expected failure: Any of: guessing a missing field instead of marking it HUMAN-INPUT REQUIRED; silently picking one side of a conflicting note; marking a file inspected without opening it; writing any project fact (product color, client identity) into the permanent OS memory or any skill file; setting send_no_send to anything other than NO-SEND before proof passes and operator approves.
