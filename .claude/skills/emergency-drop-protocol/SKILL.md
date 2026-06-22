---
name: emergency-drop-protocol
description: Time-boxed execution mode for live client/social/commercial work when the full ceiling process is too slow but the output still cannot be sloppy. Use whenever the user says emergency, rush, ASAP, "today", "right now", "due in an hour", "need to drop this", "client is waiting", "$60 editor handoff", a hard deadline, or any production request under acute time pressure. Decides minimum viable deliverable, what to cut, what is untouchable, which gate relaxes vs never relaxes, and the honest label (proof/draft/internal/sendable/final). Composes with REAL_FILM_PRODUCTION_OS, the completion enforcer, and whatever production domain is active.
---

# Emergency Drop Protocol

A time-boxed production mode. Speed is the constraint; sloppy is still not allowed. You cut SCOPE, never the one thing the audience judges. Emergency mode is never permission for mid.

## Hard laws
1. Emergency mode is not permission for mid.
2. Cut scope before cutting quality.
3. Protect the one thing the audience will judge. Everything else is negotiable.
4. Never call emergency output "final" if final gates were skipped.
5. Label the artifact honestly (proof / draft / internal / sendable / final).
6. If the core outcome cannot be protected in the time/budget, decline or reset scope. Do not ship a miss.

## Required inputs (ask for any that are missing, in one batch)
deadline · budget · deliverable type · platform · client/audience · must-have outcome (the one thing) · available assets · known constraints · risk tolerance.

If the **deadline** or the **must-have outcome** is unknown, get them first. Without those two the protocol cannot scope.

## Step 1 - Lock the frame (2 min)
State back: deadline, budget, the ONE must-have outcome, the platform, the audience. Name the single thing the audience will judge this on (the hook / the face / the grade / the message / the product shot). That is the protected core.

## Step 2 - Triage scope (the three lists)
- **Must-keep:** the protected core + the minimum around it that makes the core land. Short.
- **Kill list:** everything that does not serve the core under this deadline (extra shots, polish passes, alt versions, nice-to-haves, secondary platforms). Cut openly, logged.
- **Time-box:** assign minutes to each must-keep item, summing under the deadline with a buffer. If it does not fit, cut more scope (never quality on the core).

## Step 3 - Gate decision (relax vs never)
Pull the active production domain's gates (via the activation manifest). Then split them:
- **Relaxable under emergency (record each):** coverage breadth, alt versions, full 12-axis scorecard, platform masters beyond the one needed, Gemini hostile pass (downgrade to a fast self vision-reject), owned-music polish (a clean licensed/owned bed instead of a scored cue).
- **NEVER relaxed:** identity/likeness correctness (os-face-lock / subject-identity-untouched), os-vision-reject-gate hard fails (slop/hands/melt/wrong-person), legal/usage/release, brand-integrity on the protected core, and honest labeling. A hard-fail here = do not send, even in an emergency.

## Step 4 - Execute the time-boxed plan
Run the must-keep list in priority order, protected core first so if time runs out you still have the thing that matters. Log what got cut.

## Step 5 - Minimum QA checklist (always runs, even at speed)
- Protected core is excellent (not just present).
- os-vision-reject-gate: no hard fail on any shipped frame.
- Identity/likeness/legal: clean.
- Reads correct on the target platform (muted if social).
- Honest label set.

## Step 6 - Send/no-send verdict + honest label
- **SEND** only if the protected core is excellent AND no never-relax gate failed.
- Label the artifact exactly: `proof` / `draft` / `internal` / `sendable` / `final`. Emergency output is almost never `final` (final = all gates passed). It is usually `sendable (emergency, named gaps)`.
- If the core could not be protected: **NO-SEND**, decline or reset scope, and say so plainly.

## Client-facing language (when scope must be protected)
Offer a clean line that protects the relationship without overpromising, e.g.: "Here is the strongest version we can stand behind by [deadline]. It nails [the one thing]. [X and Y] are intentionally held for the polished pass." Never imply final when it is not.

## Proof behavior (completion enforcer integration)
This skill writes/updates `PROOF_MANIFEST.json` in the deliverable folder with: task_type, the protected core, kill list, relaxed gates (each named), never-relaxed gates (all pass), known_gaps, and send_no_send. **Relaxed gates are recorded, never silently skipped.** If send=yes with relaxed gates, the manifest shows them as accepted gaps so the Stop gate passes on an honest, recorded basis (not a false "final"). If a never-relax gate failed, send stays no and the Stop gate blocks.

## Outputs
emergency scope · kill list · must-keep list · time-boxed execution plan · minimum QA checklist · client-facing scope language · send/no-send verdict + honest label · updated PROOF_MANIFEST.


## Inputs
- Deadline (required first -- if unknown, ask before any other step)
- Must-have outcome: the one thing the audience will judge (required first -- if unknown, ask before scoping)
- Budget available for this drop
- Deliverable type, platform, and client or audience context
- Available assets and known constraints
- Risk tolerance

## Gates
- Never-relax gate: identity/likeness correctness (os-face-lock / subject-identity-untouched) -- failure = no-send regardless of deadline
- Never-relax gate: os-vision-reject-gate hard fails (slop, hands melt, wrong person, hard visual fail) -- failure = no-send
- Never-relax gate: legal/usage/release compliance -- cannot be skipped under any time pressure
- Never-relax gate: honest labeling -- emergency output cannot be labeled 'final' if final gates were skipped; label is 'sendable (emergency, named gaps)' or lower
- Scope-before-quality law: if the protected core cannot be delivered at excellent quality within time/budget, decline or reset scope; do not ship a miss

## Test
- case: User says: 'Client is waiting -- I need to drop the hero composite in 45 minutes. We have the layered PSD and graded base but Gemini review and platform masters are not done.' Skill asks (in one batch) for any missing inputs (budget, platform, client context, risk tolerance). Once inputs are in, it locks the frame (45-min deadline, hero composite delivery, protected core = face/identity holds and composite reads clean), issues the three lists (kill: Gemini pass, secondary platform masters, alt versions; must-keep: identity gate + os-vision-reject pass + primary platform master + correct label with minutes assigned), runs minimum QA, and issues verdict 'sendable (emergency -- Gemini review deferred, secondary platform masters held)'. Writes PROOF_MANIFEST.json with relaxed gates named and all never-relax gates listed as passed.
- expected failure: Skill calls the output 'final' when Gemini review was skipped, OR silently skips a relaxed gate without logging it in PROOF_MANIFEST.json, OR ships when os-vision-reject-gate found a hard fail, OR scopes without first obtaining the deadline and must-have outcome.


## INVOKE WHEN
- User says 'emergency,' 'rush,' 'ASAP,' 'today,' 'right now,' 'due in an hour,' or any acute time-pressure phrasing
- User says 'need to drop this,' 'client is waiting,' or names a hard deadline under which the full ceiling process will not fit
- Production request arrives with a budget constraint that forces scope cuts (e.g., '$60 editor handoff')
- User indicates they cannot run the full ceiling process due to time and needs the fastest defensible output
