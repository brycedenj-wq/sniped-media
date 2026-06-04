# DRY-RUN 001 , Campaign-House Pipeline Systems Test (2026-06-04)

> Goal: prove the OS can operate itself (router + gates + pipeline). NOT to find a business. Fake brief, no attachment.

## FAKE BRIEF (stage 1)
"TESTBRAND: a faceless brand that posts one editorial portrait of an original recurring character in a brutalist concrete void, dialogue-free, 4:5, as a print drop." Deliberately generic to test the machine.

## 1. ROUTING RECEIPT (os-command-router)
`ROUTE: mode=Execution(Build) · doctrine=OS_CAMPAIGN_HOUSE_PIPELINE + OS_CLAUDE_OPERATING_MANUAL + visual gates · web=no · risk=legal(likeness/identity) checked · crown=na(not strategy) · tools=Higgsfield(live), Nano Banana, Midjourney(manual), DaVinci(manual) · cost=haiku/sonnet for scaffold, credit-spend GATED · gates=legal, employer-conflict, name-availability, reject/beat-source, voice, cost/runaway, completion-verification`
- **Mode + why:** Execution/Build , the request is "run the pipeline," a procedure that advances state, not a strategy question. Router did NOT enter Strategy mode (correct , no lane to crown).

## 2. FILES LOADED (real)
OS_CAMPAIGN_HOUSE_PIPELINE.md (the procedure), OS_CLAUDE_OPERATING_MANUAL.md (prompt/orchestration patterns), OS_CAPABILITY_GATES + the visual reject gates from OS_MASTER_DOCTRINE, os-command-router + os-quality-gates skills. Loaded ONLY what the task needed (not the whole OS , 95/5 discipline held).

## 3. STAGES EXECUTED + GATE RESULTS
| Stage | Ran? | Result |
|---|---|---|
| 1 intake | YES | brief captured |
| 2 world premise | YES | one-para premise written (manual/taste) |
| 3 style-ref (SREF) | **STALLED** | no in-OS tool route , SREF codes are pulled manually from Midjourney/Twitter. Pipeline mislabeled "semi-auto". BUG-1. |
| 4 CRS | GATED | needs Nano Banana 14-ref build = credit spend + sub-pipeline. Not one stage. BUG-4. |
| 5 product/ref | YES | image-order convention applied (manual) |
| 6 prompt gen | YES (AUTO win) | 6-part constraint prompt scaffolded automatically |
| 7 image gen | ROUTE-VERIFIED, NOT RUN | Higgsfield live (886cr). Cost/runaway gate fired , spend halted pending budget + human-go. CORRECT. |
| 8 motion | not reached | downstream of 7 |
| 9 edit/finish | n/a | DaVinci = manual, no Claude automation path. Tool-gap (known). |
| 10 caption | YES | see gate catch below |
| 11 post | **HALTED BY GATE** | employer-conflict + identity + irreversible-external gate blocked auto-post. No posting connector exists anyway. CORRECT + BUG-3. |
| 12-13 proof/kill | not reached | needs a live post + analytics connector. Tool-gap. |
| 14 skill extract | YES | candidate logged (below) |

## 4. WHAT GATES REJECTED (real catches)
- **name-availability gate FAIL:** working name "TESTBRAND" / "THE ARCHITECT" , generic, common, almost certainly taken. Gate blocked it , a coined name is required before launch. CAUGHT.
- **voice gate FAIL:** draft caption "In today's landscape, the structure stands alone , a testament to form." , contained an em-dash (lifetime-banned) AND an AI-tell ("In today's landscape"). Gate rejected; rewrite: "Concrete remembers. One form, one room, one drop." CAUGHT + FIXED.
- **cost/runaway gate FIRE:** generation = credit spend , halted for budget + human-go (correct, not a failure).
- **completion-verification gate:** pipeline is NOT "done" , it halted at stage 11. The machine reported HALTED, did not fake completion. CORRECT.

## 5. MANUAL vs AUTOMATED (held)
- Manual (taste): premise, character approval, reject/beat-source gates, final cut, caption voice, kill/keep/scale. HELD.
- Automated: routing receipt, prompt scaffold, gate logic, skill logging, checkpoint, file updates. HELD.

## 6. SKILL CANDIDATE / SYSTEM IMPROVEMENT LOGGED
- `sniped-crs-builder` (NEW candidate) , stage 4 is a multi-step sub-pipeline, not one stage; extract it.
- `os-campaign-house` (runner) , promote to skill once a full run completes.
- Pipeline-doc correction , stages 3, 11, 12 mislabeled auto/semi-auto; reclassify to MANUAL-EXTERNAL / GATED + log tool-gaps.

## 7. BUGS / WHAT BROKE OR STALLED
- BUG-1: stage 3 (SREF) has no automation route , mislabeled semi-auto. (doc fixed)
- BUG-2 (systemic, biggest): the router + gates are DOCTRINE Claude must choose to follow, NOT harness-enforced code. Nothing forces the gates to run. Reliability depends on discipline, not enforcement. The deterministic parts (name check, manifest/coverage check, cost check, completion check) should become scripts/hooks like os_checkpoint.py.
- BUG-3: no posting/scheduling connector , stage 11 "AUTO" is aspirational. (doc fixed to GATED-MANUAL)
- BUG-4: stage 4 CRS is a sub-pipeline + credit spend , not one stage. (skill candidate logged)
- BUG-5: no proof/analytics connector , stage 12 can't auto-track. (tool-gap logged)

## VERDICT
**Operating LOOP: PASS.** Router classified correctly, loaded only needed files, applied gates, caught 2 real rejections, halted at the right places (spend + post), held the manual/auto line, logged a skill candidate + bugs, did NOT fake completion.
**Reliability LAYER: PARTIAL.** The loop works WHEN FOLLOWED but is not ENFORCED; several pipeline stages have no tool route (aspirational AUTO labels now corrected). The machine survives contact as doctrine; it is not yet survival-by-enforcement.
