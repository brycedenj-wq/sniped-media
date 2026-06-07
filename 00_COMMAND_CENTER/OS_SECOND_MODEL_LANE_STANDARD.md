# OS SECOND-MODEL LANE — STANDARD

A permanent lane: a second model (Gemini CLI today) reviews and attacks Claude's work so the OS does not ship what one model rationalizes. Locked 2026-06-07.

## Why
One model settles. A hostile second model with different priors catches dead air, missed moments, privacy misses, and "good enough" rationalizations. The second model raises the floor; it never sets the truth.

## Roles — ALLOWED
- Brutal critique of finished/rough cuts.
- Review of frame contact sheets + timestamped frame sheets.
- Review of EDLs / selects maps / commercial structure.
- "What are we missing?" audits.
- Second opinion on whether Claude is settling.
- Comparison against the brief + reference doctrine + director corrections.
- Read-only code / repo / folder review.

## Roles — FORBIDDEN
- Editing files directly.
- Becoming the source of truth.
- Overwriting Claude decisions without evidence.
- Receiving private/client folders without the privacy gate first.
- Making client-delivery decisions.
- Crowning anything final.

## The lane (every second-model pass)
```
1 BUNDLE   build a de-identified review bundle (contact sheet + timestamped frames
           + EDL + selects + brief + known issues + rejects + DO-NOT-SUGGEST list)
2 RUN      gemini -p "<strict-JSON critique prompt>" --output-format json   (read-only)
3 SAVE     SECOND_MODEL_REVIEWS/<job>_REVIEW_<NNN>.json + .md (verify 0 edits)
4 RECONCILE  os_second_model_gate.py: each note -> evidence check -> accept/reject/partial
5 PLAN     write the repair plan: "model said X / footage says Y / action Z"
6 GATE     accept ONLY evidence-backed notes; reject brief-contradicting ones
```

## The reconciliation rule (core)
A second-model note becomes an action ONLY if footage / brief / director-correction backs it.
- **ACCEPT** — evidence confirms the note.
- **PARTIAL** — problem is real but the proposed fix is wrong; keep the problem, replace the fix.
- **REJECT** — contradicts verified footage or a deliberate, documented creative decision.
- Director-label-is-truth-until-disproven holds. A lower second-model score is a prompt to re-verify, not an automatic truth.

## Mandatory review prompt asks (commercial cut)
brutal score /10 · timestamped keep list · timestamped cut/fix list · missed best moments · hook reads? · gag clear? · inserts same world? · wrong-person/BTS/plate? · commercial-grade vs social rough · exact next-version plan · what is the team rationalizing · per-tool routing (Premiere/AE/Higgsfield/Adobe/ffmpeg use|avoid + why).

## Engines
- `scripts/os_gemini_review.py` (bundle + read-only run)
- `scripts/os_second_model_gate.py` (reconcile + accept/reject rules)
- Reviews: `00_COMMAND_CENTER/SECOND_MODEL_REVIEWS/`

## Interaction with the finishing dept
The second-model lane sits BETWEEN the finish gate and any "good enough" call. A cut is never called client-ready on a finish-gate pass alone; it must also survive a second-model pass with its evidence-backed notes addressed. No em-dashes in any artifact.
