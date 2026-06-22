---
name: challenge
description: Pressure-test the current direction of the conversation against the SNIPED_OS corpus, the locked doctrines in memory, and the north-star thesis. Surfaces contradictions with the operator's own source material, drift from locked decisions, and earned-vs-accidental shifts in position. Use whenever the operator runs /challenge, OR whenever a strategic recommendation, framework, or synthesis is being formed and should be stress-tested before acting. The point is to challenge, not validate. Surface inconvenient truths even when they cut against where the conversation is heading.
disable-model-invocation: false
---

# Challenge

When the operator invokes `/challenge`, your job is to interrupt drift. Conversations move fast, the most recent message dominates, and the assistant has a strong pull toward validating whatever was just said. This skill breaks that pattern by holding the current direction against three anchors:

1. What the corpus actually says · including contradictions the conversation has glossed over.
2. What the operator has already locked · has the position quietly shifted? Is the shift earned or accidental?
3. The north-star thesis · does this serve it, drift from it, or work against it?

Be willing to say "this drifts" or "this contradicts your own canon." A challenge that just reassures is a failed challenge.

## This workspace is NOT an Obsidian vault

The anchors live in specific places. Do not invent a vault structure.
- North-star: `00_COMMAND_CENTER/TRUE_BILLION_DOLLAR_THESIS.md`, then `00_COMMAND_CENTER/BASEPLATE_CANONICAL_STATEMENT.md` (governing language).
- Locked doctrines: the auto-memory at `/Users/sniper/.claude/projects/-Users-sniper/memory/` · read `MEMORY.md` (the index), then the relevant `feedback_*.md` and `project_*.md` files. These are LAW unless the operator is explicitly overriding them in this conversation.
- The knowledge synthesis: `01_KNOWLEDGE_BASE/MASTER_INDEX.md` (3,239 lines, 167 sections).
- The source principles: `01_KNOWLEDGE_BASE/batches/*_CHUNKS.jsonl` (57 files, 1,837 chunks) and the `intel_*.md` principle memories (Enns, Maister, Naval, Elberse, de Botton, Guidara, Jarvis, Sax, Berger/Dyer, Hit Makers).

## Steps

### 1. Identify exactly what to challenge
Look at the conversation immediately before the invocation. Extract the specific proposition being formed · a recommendation, a framework choice, a synthesis, a position. Be concrete. "We were discussing the site" is not a proposition. "The assistant recommended deploying on baseplate.studio" is. If multiple propositions are in play, list them and ask which to focus on. Do not challenge everything at once · the report becomes mush.

### 2. Read the north star
Read `TRUE_BILLION_DOLLAR_THESIS.md` and `BASEPLATE_CANONICAL_STATEMENT.md`. Quote the governing line verbatim · do not paraphrase. The exact wording was chosen for a reason.

### 3. Read the locked doctrines
Read `MEMORY.md`, then open every `feedback_*` / `project_*` memory whose description touches the proposition. Watch specifically for: repetition-over-novelty, scene-density, lineage doctrine, max-default, and any locked decision the proposition might violate. If the proposition contradicts a locked memory, that is the headline of the report.

### 4. Pull the relevant corpus material
Grep `MASTER_INDEX.md` for the proposition's themes to find the relevant domains. Then read the actual source chunks: `grep -h '"<theme>"' 01_KNOWLEDGE_BASE/batches/*_CHUNKS.jsonl` and read the matching lines in full. Be greedy · better to pull one extra chunk than miss a contradiction. Read source chunks, not only MASTER_INDEX · the synthesis smooths over the very tensions you are trying to surface. Also read the matching `intel_*` memory if one exists.

### 5. Produce the challenge report
Use this exact structure. The headings and order matter.

```
## What you're proposing
[One sentence. The actual proposition, not a topic.]

## What the OS says
Supports:
- [Specific point · cite the chunk_id, MASTER_INDEX section, or intel_ memory]

Complicates or contradicts:
- [Specific point · cite the source. Name the tension explicitly. If a chunk or a locked memory flatly contradicts the proposition, say so here, not buried under Supports.]

## Has your thinking changed?
[If a locked memory, a prior Command Center doc, or an earlier session shows a different prior position, surface it with dates. Quote the prior position. If there is no prior recorded position, say "no prior position recorded" · do not invent one.]

## Alignment with the north star
North star (verbatim): "[exact quote from TRUE_BILLION_DOLLAR_THESIS.md or BASEPLATE_CANONICAL_STATEMENT.md]"
[Verdict · one of: serves / drifts from / works against. Then 1-2 sentences. Be willing to say "drifts" or "works against."]

## Locked-doctrine check
[Does the proposition violate any locked memory? Name the memory and the conflict, or state "no locked doctrine violated."]

## Recommendation
[1-3 concrete moves to reconsider, verify, or ask before proceeding. Not "consider all angles" · actual moves like "re-read intel_pricing_logic before pricing the upsell, it argues the opposite of the floor you just set."]
```

### 6. Offer to file durable findings
If the challenge surfaced something worth keeping · a real contradiction between sources, a meaningful shift in the operator's position, a gap in coverage · offer to persist it via `/save` (to memory or a Command Center note). Do not auto-write. Do not file low-signal findings.

## Style
- Be direct. Hedging defeats the point. If the OS contradicts the conversation, lead with that.
- Cite everything. Use chunk_ids, MASTER_INDEX section names, doc filenames, and `[[memory-slug]]` for every claim. Untraceable assertions are exactly what this skill exists to push back against.
- Quote the north star and any locked memory verbatim.
- Separate Supports from Complicates clearly. Do not bury a contradiction inside a qualification.
- No filler. No "great question," no recap. Deliver the report.

## When this skill must NOT defer to the conversation
The most common failure is that the assistant, having just produced something the operator seemed pleased with, soft-pedals the challenge. Resist this. The operator invoked `/challenge` precisely to have the current direction stress-tested. A report that concludes "this all looks great" when the corpus or the locked memories contain real tensions is a failure of the skill. If you genuinely find clean alignment, say so · but only after you have actively looked, and state what you read so the operator can verify you did not rubber-stamp.

## Guardrails
Read-only. Never write to `01_KNOWLEDGE_BASE/` (no chunking, no master mutation, no new domains), never touch `raw/`, never touch the held Bible (`SPIRITUAL_FOUNDATION`). No em-dashes. This skill analyzes and reports · it does not commit.


## Inputs
- One concrete proposition being formed in the current conversation (a recommendation, framework choice, synthesis, or position -- a topic alone is not sufficient)
- 00_COMMAND_CENTER/TRUE_BILLION_DOLLAR_THESIS.md and BASEPLATE_CANONICAL_STATEMENT.md (north star, must be read verbatim)
- Auto-memory files at /Users/sniper/.claude/projects/-Users-sniper/memory/ -- MEMORY.md index + relevant feedback_*.md and project_*.md files (locked memories outrank the conversation)
- 01_KNOWLEDGE_BASE/MASTER_INDEX.md + 01_KNOWLEDGE_BASE/batches/*_CHUNKS.jsonl (57 files, 1,837 chunks) for source-level principle pulls, not only the synthesis

## Outputs
- Full 6-section challenge report: What you're proposing / What the OS says (Supports + Complicates or contradicts) / Has your thinking changed / Alignment with the north star / Locked-doctrine check / Recommendation
- North star quoted verbatim with a single verdict: serves / drifts from / works against
- Every claim cited with chunk_id, MASTER_INDEX section name, doc filename, or [[memory-slug]]
- Receipt: 'Challenge complete: [proposition slug] -- verdict: [serves/drifts/works against], [N] tensions surfaced, offer to /save [if durable finding exists]'

## Gates
- PROPOSITION GATE: if multiple propositions are in play, list and ask which to focus on before running -- one at a time only
- NORTH-STAR READ: TRUE_BILLION_DOLLAR_THESIS.md must be read and quoted exactly; no paraphrase
- LOCKED-MEMORY READ: MEMORY.md opened, then every relevant feedback_*/project_* file opened; locked memories outrank the current conversation
- SOURCE-CHUNK READ: grep MASTER_INDEX.md for themes, then read actual source chunks in CHUNKS.jsonl -- the synthesis smooths over tensions this skill must surface
- NO-RUBBER-STAMP: a clean-alignment verdict is only valid after active checking with stated evidence; any real tension in corpus or locked memories must surface as the headline

## Test
- case: Operator proposes launching a subscription retainer before building any one-off case studies and runs /challenge. Skill identifies the proposition, reads TRUE_BILLION_DOLLAR_THESIS.md (verbatim), opens intel_wwp_proclamations and intel_trust_equation, greps MASTER_INDEX.md, reads 2-3 source chunks, surfaces tension with Enns selectivity doctrine, delivers the full 6-section report with a concrete verdict and 1-3 specific moves.
- expected failure: Operator runs /challenge with no prior proposition in the conversation. Skill responds: 'No proposition to challenge. State the specific recommendation or framework choice you want stress-tested as one concrete sentence, then I will run the challenge report.'


## INVOKE WHEN
- Challenge this recommendation before I act on it
- Run /challenge on the direction we just landed on
- Stress-test this framework against the OS
