---
name: boardroom
description: Convene a decision board drawn from the operator's own canon (the thinkers already chunked in the SNIPED_OS corpus) to pressure a specific decision from multiple expert lenses, then synthesize a recommendation. Each advisor argues from their actual doctrine in the corpus with citations, not from a generic invented persona. Use whenever the operator runs /boardroom, or faces a real decision (pricing, positioning, a build, a launch, a hire, a client-experience choice) that benefits from being argued from several angles before committing.
disable-model-invocation: false
---

# Boardroom

Convene a board of the operator's own canon to argue a decision from multiple lenses, surface where the advisors disagree (that is the signal), test it against the north star, and deliver one recommendation. The board members are not generic personas · each one argues from their actual principle as captured in this corpus.

## The board (drawn from the corpus, cite when you seat them)

Each advisor maps to a real `intel_*` memory and to chunks in `01_KNOWLEDGE_BASE/`. Seat only the ones relevant to the decision.

- **Blair Enns** · positioning, selectivity, pricing, sales-flow · `intel_wwp_proclamations`, `intel_pricing_logic`.
- **David Maister** · trust, self-orientation, B2B service · `intel_trust_equation`, `intel_trust_mechanics`.
- **Naval Ravikant** · leverage (labor / capital / code+media), stay-small · `intel_leverage_logic`.
- **Paul Jarvis** · company-of-one, right-size-not-scale, resilience · `intel_company_of_one`.
- **Anita Elberse** · blockbuster bets, superstar economics, distribution dominance · `intel_blockbuster_strategy`.
- **Derek Thompson** · hit mechanics, exposure/MAYA, broadcast vs clusters · `intel_hit_mechanics`, `intel_distribution_mechanics`.
- **de Botton / Simler / Hanson** · status psychology, hidden-motive signaling · `intel_status_psychology`.
- **Trading Up / New Luxury** · why buyers trade up, technical-functional-emotional ladder · `intel_new_luxury`.
- **Will Guidara** · hospitality beyond service, the unreasonable touch · `intel_hospitality_layer`.
- **David Sax** · analog premium, revenge-of-analog, anti-AI moat · `intel_analog_premium`.
- **Berger / Dyer** · photography theory, taken-vs-made, the suit and the photograph · `intel_photo_theory`.
- **Ryan Holiday** · perennial work, patience, content-vs-promotion · `intel_perennial_logic`.

## Steps

### 1. State the decision precisely
One sentence, concrete. "Should we price the AI-Ops upsell as a fixed retainer or value-based?" not "thinking about pricing."

### 2. Seat the relevant board
Select advisors by decision type. Examples:
- Pricing · Enns + Maister + New Luxury + Status.
- Positioning / what-lane · Enns + Maister + Sax.
- Build / tooling / hire · Naval + Jarvis.
- Launch / distribution / audience · Thompson + Elberse + Holiday.
- Client experience / delivery · Guidara + Maister.
- Creative / photography / AI-defense · Berger-Dyer + Sax.
Seat 3 to 5. Too many advisors and the report turns to mush.

### 3. Give each advisor a real position
For each seated advisor, read their `intel_*` memory (and pull a source chunk if you need the exact principle). Then write:
- **Position** · what they would advise on THIS decision, argued from their doctrine.
- **Cite** · the principle, with the memory slug or chunk_id.
- **Strongest objection** · the sharpest thing they would warn against. Every advisor must include an objection · no rubber-stamping.

### 4. Surface the disagreements
Name explicitly where advisors conflict. The conflict is the decision's real tension (e.g. Elberse says bet big on a named client, Jarvis says that bet threatens the company-of-one resilience). Do not smooth it over.

### 5. Run it against the north star and locked doctrines
Quote the governing line from `00_COMMAND_CENTER/TRUE_BILLION_DOLLAR_THESIS.md` (or `BASEPLATE_CANONICAL_STATEMENT.md`) verbatim, and check the relevant locked memories. If the leading option violates a lock, say so. This keeps `/boardroom` from validating a drift just because the advisors liked it. When the decision is strategic, consider chaining `/challenge` first.

### 6. Synthesize
Deliver:
- **Recommendation** · the call, in one or two sentences.
- **Why it wins the room** · which advisors carry it and why.
- **Remaining dissent** · the objection that does not go away.
- **The test** · the one cheap experiment or fact that would resolve the dissent (tie it to the proof loop where relevant).

### 7. Offer to persist
If the decision is durable, offer to `/save` it (memory or a Command Center note). Do not auto-write.

## Style
- Advisors argue from the corpus, with citations. If you cannot ground an advisor's position in their actual doctrine, do not seat them.
- Every advisor gives an objection. A board that unanimously agrees was seated wrong · widen it.
- Quote the north star verbatim. No filler, no preamble.

## Guardrails
Read-only. Never write to `01_KNOWLEDGE_BASE/` (no chunking, no master mutation, no new domains), never touch `raw/`, never touch the held Bible. Honor the locked memories · they outrank the board. No em-dashes. This skill argues and recommends · it does not commit.
