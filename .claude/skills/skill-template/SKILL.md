---
name: skill-template
description: Reference template proving the skill activation contract. Use when creating any new OS skill so it is born ACTIVE.
---

# skill-template

One-line statement of what this skill produces.

## INVOKE WHEN
- the trigger condition that should route here
- "natural language phrase the operator might say"

## Inputs
- input_1 , what it is and where it comes from
- input_2 , optional

## Outputs
- output_1 , the artifact this skill produces
- a one-line receipt of what was done

## Procedure
1. step one
2. step two
3. run the gate(s), then emit the output

## Gates
- the quality/safety gate(s) this skill must pass before emitting output

## Test
- case: given <input_1 = sample>, the skill should produce <output_1 shape> and pass <gate>.
- expected failure: given a missing input_1, the skill refuses and asks for it.
