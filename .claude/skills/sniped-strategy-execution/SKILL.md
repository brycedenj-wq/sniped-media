---
name: sniped-strategy-execution
description: Turn a strategy question into a decision-useful brief, not a generic essay. Use for launch plans, "what should I do next", client-delivery go/hold calls, offer/business decisions, brand direction, and prioritization between competing items. Trigger phrases "what should I do", "should I do X or Y", "launch plan", "is this on-strategy", "which lane", "deliver or hold", "what's the offer", "prioritize this".
---

# SNIPED Strategy Execution

Frame any strategy input as a decision, rank divergent options, and ship the smallest reversible next move with a test attached. Recommend an action plus a proof checkpoint, never crown a lane or identity.

## When it fires
- Launch plan, "what do I do next", client-delivery go/hold, offer/business decision, brand direction, or prioritization between competing items.
- A strategy answer is about to be returned as an essay instead of a decision.
- The user says "is this on-strategy", "which lane", "deliver or hold", "what's the offer".

## Inputs required
- The decision (or enough context to frame one).
- The objective: what winning looks like.
- Constraints: time, cash, identity, the 10-12 hr/week lean override.
- Risk tolerance and money/priority facts (cash position, deadline, what is already promised).
- If objective, risk tolerance, or money facts are missing: ask the human first (see Ask the human when).

## Steps (numbered, executable)
1. **Frame the decision** in one concrete sentence. "Should the Op Kit ship as a fixed price or value-based?" not "thinking about pricing." If the input is a list of tasks, run `sniped-execution-prioritization` first to find the one decision that governs.
2. **State the objective** (what winning looks like) in one line. If unstated or fuzzy, stop and ask the human. Do not invent it.
3. **List the constraints**: time, cash, identity, the 10-12 hr/week lean override. Check the move against `sniped-canonical-truths` (which of the 12 truths apply and what they constrain) and `sniped-leverage-logic` (is this code+media leverage or labor drag).
4. **Generate 3 divergent options.** They must differ in kind, not in degree. If money/positioning/distribution is at stake, load the matching `os_doctrine.py` pack (`pricing_offer`, `distribution_hook`, `trust_sales`) so options are doctrine-correct at birth.
5. **Tradeoffs per option**: upside, cost, what it forecloses. For a real founder-level fork, seat the relevant advisors via `boardroom` and record where they disagree (the disagreement is the signal).
6. **Name the bottleneck**: the one constraint that actually governs the outcome (usually cash, time, or proof). Everything downstream serves relieving it.
7. **Mark each option reversible or irreversible.** Irreversible + unproven = do not recommend; run `challenge` against it before it ships.
8. **Pick the next action**: the smallest shippable move that relieves the bottleneck. An action plus a test, never a crowned lane. For a stuck founder-level fork, hand off to `sniped-decide` for the contrarian pass and memo.
9. **Set kill criteria**: the observable signal that says stop or pivot, with a date.
10. **Set the proof checkpoint**: what evidence promotes this from test to commitment. Run `os-quality-gates` (gates 3, 4, 7, plus no-crown) before declaring the brief done.

## Output format (the exact deliverable shape)
- **Decision** (one sentence).
- **Objective** (one line).
- **Constraints + bottleneck** (the one constraint that governs).
- **Ranked options table**: 3 rows, columns = Option | Upside | Cost / what it forecloses | Reversible? | Rank.
- **Recommended action** (smallest shippable move + the test attached).
- **Why now** (1-2 lines).
- **What NOT to do** (the tempting wrong move, named).
- **Kill criteria** (signal + date).
- **Proof checkpoint** (evidence that promotes test to commitment).
- **Receipt block** (see Proof / receipt).

## Quality gate (pass/fail)
Run `os-quality-gates` before "done":
- Gate 4 proof-before-crowning: no lane/identity crowned without current proof. "The answer is X" with no proof = FAIL.
- Gate 3 optionality-protection: lanes/identity stay open absent explicit proof + operator decision. Collapsing optionality = FAIL.
- No-crown rule: the deliverable is an action + a test, not an identity. Crowning a lane = FAIL.
- Gate 7 output-usefulness: operator can act now. Vague = FAIL.
- Gate 1 anti-hallucination: every strategic/factual claim cites a source or is labeled inference.
Any FAIL blocks done. Fix and re-run.

## Proof / receipt (what to log)
Log before the brief is done:
- Files / skills used (by exact name) and which `os_doctrine.py` pack(s) fired.
- The framed decision and the 3 options considered.
- Assumptions made (especially any objective or money fact you had to infer).
- Recommended next action + kill criteria + proof checkpoint.
- `os-quality-gates` pass/fail (gates 3, 4, 7, no-crown).
- Human-approval-needed: the exact priority, risk-tolerance, or money facts still missing.
Format follows `os_receipt.py` discipline (what CHANGED because the OS activated, gates passed/failed, verdict). No `os_proof_manifest.py` artifact is required: this is a strategy deliverable, not a production task.

## Ask the human when
- The objective is unstated or fuzzy (what does winning look like here).
- Risk tolerance is unknown (can BJ afford to be wrong on this one).
- Money/priority facts are missing (cash position, deadline, what is already promised).
- The decision would crown an identity or lane rather than test one.
Use `AskUserQuestion`. Do not invent the objective or the money facts.

## Depends on
`sniped-canonical-truths`, `sniped-leverage-logic`, `sniped-execution-prioritization`, `boardroom`, `challenge`, `sniped-decide`, `os-quality-gates`, and the `os_doctrine.py` packs `pricing_offer` / `distribution_hook` / `trust_sales` (rules in `00_COMMAND_CENTER/scripts/os_doctrine.py`). Receipt discipline from `os_receipt.py`.

## External-resource gap
None tool-version-sensitive here. This skill is reasoning-only and depends on on-disk OS docs, which are the current source of truth.

