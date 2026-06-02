# CURRENT_IDENTITY_AND_BRAND_OPTIONALITY mini-batch · PLAN

**Date planned:** 2026-05-23
**Status:** PLAN ONLY · not extracted, not chunked, master files untouched, not committed.
**Supersedes:** the earlier `BRAND_STRATEGY_PLAN.md` (reframed per operator correction · the old plan over-relied on stale BASEPLATE-era brand decisions as if they were current SNIPED truth).
**Batch kind:** mini-batch (descriptive slug · numbered slots stay reserved for canon batches).

---

## 0. Verified starting state

- **Head commit:** `c91980e save session after CULTURE_AND_STATUS consolidation`
- **Working tree:** only this plan + the prior `BRAND_STRATEGY_PLAN.md` are untracked. No tracked changes.
- **Total chunks:** 1,278 · 10 numbered batches + 11 mini-batches · 60 official domains.
- **No lane started:** no `*_CHUNKS.jsonl`, no extracted dir, no COMPLETE marker for this lane.

---

## 1. Operator correction captured (the anchor for this plan)

**Identity is not fixed yet. Do not finalize brand architecture.**

Current truth:
- **SNIPED** = the operator's identity / handle / current container. It functions almost like his name.
- **SNIPED Media** = his existing photography company (one current vehicle · one real edge).
- **BASEPLATE** = an optional/historical exploration (domains bought, logos explored) · NOT the decided future brand.
- The final direction will be re-determined soon from current reality. **No final brand decisions yet.**
- Do not treat old BASEPLATE docs as active truth. Do not treat SNIPED as photography-only forever.

Strategic correction:
- The operator may have over-invested in pictures, edits, and beating people creatively through photography alone.
- Photography is still a real edge, but it must not dominate the OS or force every answer into a photography business.
- This lane's job is to **help discover the highest-leverage next direction**, not lock the operator into old photography or BASEPLATE assumptions.

---

## 2. Reframed goal

Extract **reusable, decision-neutral principles** about identity, brand, positioning, and leverage that **support the operator's upcoming direction decision while preserving optionality.**

This lane does NOT:
- finalize naming, rebrand, niche, offer ladder, website positioning, or company architecture;
- canonize SNIPED Media / photography as the permanent or only lane;
- treat any BASEPLATE positioning, voice, architecture, or proof points as current truth.

It DOES:
- capture transferable *method* (how to audit a brand, how to construct a positioning statement, how to evaluate a name, how to preserve optionality) so the operator has decision-support when he writes the fresh current brief;
- record the current identity model as plain context (not as final architecture);
- keep the aperture wide (multiple possible directions, photography being one edge among options).

---

## 3. Current identity model (stated as CONTEXT · not chunked as final architecture)

| Layer | Current reality | Status |
|---|---|---|
| Operator identity / handle | **SNIPED** (≈ his name · the live container) | Live · stable for now |
| Existing company | **SNIPED Media** (photography) | Active · one current vehicle / edge |
| Rebrand exploration | **BASEPLATE** (domains + logos explored) | Optional · historical · NOT decided |
| Future direction | Highest-leverage next move | To be determined soon from current reality |

These facts anchor retrieval (so the corpus knows what is live vs exploratory). They are not to be expanded into a brand-architecture canon.

---

## 4. Source candidates and how to mine them (PRINCIPLE-ONLY)

### INCLUDE · principle extraction only

1. **The BASEPLATE 10-doc set** (`raw/00_BRIEF/BRAND_STRATEGY_2026-05-13/`, 00-09 · ~14,000 words).
   - **Extract ONLY the transferable METHOD**, stripped of the BASEPLATE/SNIPED-specific content:
     - the 10-criteria naming-evaluation **framework** (how to score any name)
     - the brand-**audit method** (how to honestly assess register/fit)
     - the positioning-statement **construction method** (the "what is this / who is it for" discipline · not the literal sentence)
     - brand-architecture **as a reusable pattern** (parent / imprint / series · not SNIPED's specific imprints)
     - brand-**voice discipline as a technique** (anchor words, surface-by-surface consistency · not the specific anchors)
     - **migration sequencing** as a reusable playbook (how to move a brand without losing equity)
     - the **optionality lesson itself** (pre-audience phase = cheapest time to keep choices open)
   - **HARD-EXCLUDE** (do not chunk · these are stale aspirational/BASEPLATE-specific): the literal positioning sentence, the 4-imprint architecture (EDITIONS/STUDIO/PRESS/LAB), the proof points, the audience table, the taglines, the bio/DM/deck/colophon templates, the Forbes/cadence/collaborator/scale claims, and the BASEPLATE rename recommendation.
   - **Tag every resulting chunk:** `principle-only · historical-source · optionality-preserving · NOT current SNIPED truth`.

2. **`Brand_Builders_Playbook.docx`** (raw/ top level · 2,451 words · net-new).
   - Source-agnostic brand psychology: "a brand is the gut feeling someone has about you when you're not in the room · you sell belonging, status, identity." Decision-neutral · safe to extract as principle. Bridges to CULTURE_AND_STATUS.

### DEFER (do not pull into this lane now)

- **Third-party brand canon** (Positioning · The Brand Gap · Designing Brand Identity · Brand Naming · Identity Designed · Hello My Name Is Awesome) → a future numbered `BATCH_011` brand-canon batch. Pure transferable principle, but a large ingest that is not needed to preserve optionality right now, and ingesting a full brand-theory shelf would itself nudge the OS toward "branding" as the answer.
- **`branding x clothes gold.docx`** (clothing supply-chain · off-goal) and **`Build a Brand Like Apple.docx`** (74K-word manifesto transcript) → later content/voice pass if ever.

### EXCLUDE (already canonical · BATCH_009)

- Building a StoryBrand · Made to Stick.

---

## 5. Hard guardrails (carry into the chunk step)

1. **No finalization.** Nothing in this lane decides naming, rebrand, niche, offer ladder, website positioning, or company architecture.
2. **No photography lock-in.** Do not frame principles as photography-only. Photography (SNIPED Media) is one current edge, not the mandatory container.
3. **BASEPLATE is not truth.** Any BASEPLATE-derived chunk is principle-only and tagged historical/optional.
4. **No stale overwrite.** Nothing may assert an aspirational/mature-operation state (publishing house, imprints, bi-weekly chapters, collaborators, Forbes path, $1,500 ladder) as current reality. Current reality = solo operator, drawing-board/ideation stage, Canon R6 Mark II.
5. **Preserve optionality.** Where a doc states a decision, re-cast it as a reversible option + the reasoning, so it supports a future choice rather than pre-making it.
6. **Per-chunk tagging:** `principle-only`, `optionality-preserving`, source-status (`historical` for BASEPLATE-derived, `current-context` for the identity model, `source-agnostic` for the playbook).
7. **Halt-and-ask** if any candidate chunk can only be written as a literal current SNIPED/BASEPLATE positioning claim · do not write it.

---

## 6. Pre-flight peek (already performed)

- All 10 first-party docs are substantive (754-2,362 words · no stubs). `Brand_Builders_Playbook` is clean prose.
- Net-new grep across all `*_CHUNKS.jsonl`: 0 hits for every candidate except Building a StoryBrand + Made to Stick (BATCH_009). The BASEPLATE set and the playbook are net-new.
- The BASEPLATE set is confirmed stale/aspirational (proposes a rename not adopted · describes a mature operation that does not match current reality).
- `raw/` untouched · recovery/acquisition items untouched.

---

## 7. Estimated chunk yield

Principle-only scope is deliberately small (we drop all literal positioning/architecture/proof/taglines):

| Source | Principle chunks |
|---|--:|
| naming-criteria framework | 1-2 |
| brand-audit method | 1 |
| positioning-construction method | 1 |
| brand-architecture-as-pattern | 1 |
| brand-voice-discipline technique | 1 |
| migration-sequencing playbook | 1 |
| optionality / pre-audience-phase lesson | 1 |
| Brand_Builders_Playbook (brand-as-perception, belonging/status) | 2-3 |
| synthesis (identity vs brand vs company · how to choose direction · leverage lens) | 1-2 |

**Target: ~9-13 chunks. Acceptable range: 6-16.** (Lower than the superseded plan's 20-26 because all stale SNIPED/BASEPLATE-specific positioning content is excluded.) ID pattern `CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_001..NNN`.

---

## 8. Domain set (NO new domain · all verified to exist)

| Domain | Current | Use here |
|---|--:|---|
| `brand` | 27 | brand-as-perception, brand vs identity distinction |
| `positioning` | 14 | positioning-construction method (reversible) |
| `strategy` | 150 | direction-choice logic, optionality, leverage lens |
| `brand-psychology` | 22 | belonging/status/identity (ties to CULTURE_AND_STATUS) |
| `systems-thinking` | 31 | optionality preservation, keeping choices open |
| `small-company-strategy` | 9 | solo-operator / right-size / Company-of-One framing |
| `commercial-architecture` | 37 | brand-architecture-as-pattern (not SNIPED's specific) |
| `content-strategy` | 49 | voice-discipline technique (LIGHT) |
| `offer-design` | 15 | LIGHT · only if a principle is genuinely offer-neutral |

**No new domain.** If a concept fits none, halt and surface rather than mint one.

---

## 9. How this lane connects to the corpus (reframed for optionality)

- **CULTURE_AND_STATUS:** identity/status/belonging is the psychology under any brand or direction · directly supports "what confers status / leverage" thinking.
- **intel_leverage_logic (Naval):** the lane's purpose is to find the highest-leverage next direction · this is the lens the principles serve.
- **intel_company_of_one (Jarvis):** right-size / stay-optional / resilience-over-scale · directly supports the solo-operator, don't-prematurely-architect stance.
- **WWP positioning (intel_wwp_proclamations):** positioning as a reversible discipline, not a one-time lock.
- **BATCH_009 commercial voice + brand theory:** the general theory · this lane is the decision-neutral, current-reality-aware application layer.
- **BATCH_005 photography canon:** photography is ONE edge in the option set, explicitly not the mandatory frame for every answer.
- **The fresh current SNIPED brief (not yet written):** when the operator writes it, that becomes the clean first-party source for any future positioning lane · this lane only supplies the method to write it well.

---

## 10. Deliverables (produced only when authorized · NOT now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/current_identity_and_brand_optionality_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_COMPLETE.md` |
| Extract script | `scripts/extract_current_identity_and_brand_optionality.py` |
| Chunk writer | `scripts/write_current_identity_and_brand_optionality_chunks.py` |

Schema: canonical 12-field JSONL. `batch_id` = `CURRENT_IDENTITY_AND_BRAND_OPTIONALITY`. Extraction: `.md` copy/normalize · docx via `pandoc -f docx -t plain` · no OCR · no new dependencies.

(If the lane name is too long for comfort, the operator may shorten the slug · the principle-only + optionality framing is what matters, not the exact name.)

---

## Constraints honored by this plan

- Did NOT extract, chunk, update master files, or commit.
- Did NOT modify any `raw/` source file · recovery/acquisition items untouched.
- No em-dashes.
- No new domain proposed.
- No final brand decision made · optionality preserved.

## Recommendation + open questions (resolve before any ship)

**Recommendation:** ship a **small principle-only set (~9-13 chunks)** that gives the corpus transferable brand/identity/leverage *method* without locking anything in · OR continue to **hold** until the operator writes the fresh current SNIPED brief. Either is consistent with the correction; the principle-only ship is low-risk and aids the upcoming decision.

Open questions:
1. **Ship principle-only now, or hold** until the fresh current brief exists?
2. **Old plan disposition:** delete `BRAND_STRATEGY_PLAN.md` (recommended · it's untracked and now superseded), or keep it as a parked reference?
3. **Confirm the guardrail set** in §5 is complete (anything else that must not be finalized?).
