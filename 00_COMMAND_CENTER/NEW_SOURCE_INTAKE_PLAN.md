# NEW_SOURCE_INTAKE_PLAN · high level convos.docx + the Bible · 2026-05-24

**Status:** REPORT / PLAN ONLY. Read-only inspection of two newly added resources. No extraction, no chunking, no master-file changes, no file moves, no OCR. Nothing is chunked here.

## 0. Current corpus state (verified)

- **Head commit:** `a91c939 save session after DEEP_FINANCE_EXPANSION consolidation`
- **Total chunks:** 1,430 · **numbered batches:** 10 · **mini-batches:** 19 · **official domains:** 62 (keys 75).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.

## 1. Location + file facts (read-only)

Both files are in the source universe `~/Downloads/    SNIPED_OS/` (4 leading spaces · NOT yet in `raw/`).

| Resource | Path | Type | Size | Extractable? |
|---|---|---|---|---|
| high level convos.docx | `~/Downloads/    SNIPED_OS/high level convos.docx` | docx (Word 2007+) | 1.9 MB | YES · pandoc · 684,626 words / 102,682 lines |
| The Bible (KJV) | `~/Downloads/    SNIPED_OS/The-Holy-Bible-King-James-Version.pdf` | pdf (v1.6) | 10.2 MB | YES · pdftotext · 742 pp / 840,834 words |

Both are **usable** (clean text, no OCR needed). Overlap check: **both net-new** (0 hits across all 29 `*_CHUNKS.jsonl` for Earn Your Leisure / Miss Pinky / high level convos / Bible / KJV / scripture).

(Note: BJ also dropped several other books into the source universe this session, e.g. Alexander the Great logistics, On War, The Network State, The Founder's Dilemmas, The Elephant in the Brain. Those are OUT OF SCOPE for this plan, which covers only the two named resources, but they are flagged for a future strategy/decision-canon intake.)

## 2. high level convos.docx

### What it is
A large **multi-transcript collection** (684,626 words) of video/podcast transcripts with embedded timestamps (`0:00`, `1:15:32`, etc.) and chapter markers. Detected named sources and threads:

- **Miss Pinky · investment/fundraising basics** (opening): equity, valuation, cap tables, ownership-dilution explained in a plain, almost teaching register.
- **Earn Your Leisure (EYL) · hospitality / nightlife / operator lessons:** a club-owner / nightlife interview (Mark Barnes, DC nightlife history, challenges for Black entrepreneurs in nightlife, an *Unreasonable Hospitality* book recommendation).
- **Earn Your Leisure · "AI Future Shock":** an AI future / work / skills episode.
- Additional community / business / capital conversation threads throughout.

### One lane or split?
**Recommendation: ONE curated `HIGH_LEVEL_CONVOS` mini-batch**, NOT a numbered batch and NOT (by default) multiple lanes. Rationale:
- It is transcripts (conversational · lower information density than books · heavy filler and timestamps), so the right move is tight principle-extraction across the threads, not exhaustive coverage. A single curated mini-batch (~15-25 chunks, to be set at plan time) fits the precedent (EDGE / ONWARD scale).
- **Per-transcript source attribution is required.** Each chunk must carry the originating source in `source_title`/`author` (e.g., "Earn Your Leisure · AI Future Shock", "Miss Pinky · investment basics"). Do not collapse distinct creators into one anonymous blob. (Consistent with the SNIPED attribution discipline.)
- **Optional split (flag, not default):** if the operator prefers, the natural sub-lanes are (a) capital/fundraising basics (Miss Pinky), (b) hospitality/nightlife operator lessons (EYL nightlife), (c) AI-future/work/skills (EYL AI). Default is one mini-batch with attribution; split only on request.

### Recommended domains (existing only)
- **capital** · equity, valuation, cap tables, fundraising basics (Miss Pinky).
- **commercial-architecture** · ownership structure, dilution, deal mechanics.
- **operator-doctrine** · the operator/hospitality lessons (how nightlife/hospitality operators actually run things).
- **culture** · Black entrepreneurship, nightlife scene, the cultural context of the EYL conversations.
- **strategy** · positioning and business-building threads.
- **ai-tooling** and/or **strategy** · the AI-future/work/skills episode.
- **content-strategy** / **media-business** (light) · EYL itself as a media/creator operation, if any chunk is about the podcast-as-business.
- **ethics** (only if warranted).

### New domain?
**No new domain required.** All threads route to existing domains. **Flag (do NOT create):** "hospitality" reads like a candidate but should route to `operator-doctrine`/`culture`, not a new domain. Hold unless the operator explicitly approves.

### Guardrails for this lane
- Decision-support / pattern-library framing, read against CURRENT_OPERATOR_REALITY_BRIEF · NOT a directive (e.g., not "BJ should open a nightclub" or "BJ should raise venture money").
- Preserve identity optionality: no final SNIPED / SNIPED Media / BASEPLATE direction.
- Short illustrative quotes only (transcripts · attribute the speaker/source); strip timestamps and filler at chunk time.
- Em-dash clean.

## 3. The Bible (King James Version)

### What it is
- **Translation/version:** King James Version (KJV · from the filename and text). Public-domain translation.
- **Completeness:** **Full Bible** · 742 pages, 840,834 words, Genesis 1:1 ("In the beginning God created...") present, Revelation present, ~100+ book headings detected (Old + New Testament). Not a partial or excerpt.
- **Extractable:** YES (clean text layer · pdftotext · no OCR).

### Recommended plan style
A **dedicated `SPIRITUAL_FOUNDATION` track** (preferred over `WISDOM_CANON`), kept entirely separate from the business/operator corpus. `WISDOM_CANON` risks implying the Bible is one "wisdom resource" among business books; `SPIRITUAL_FOUNDATION` better signals it is a foundational/sacred text on its own footing.

### Chunk now, or hold as anchor/reference?
**Recommendation: HOLD as a reverent anchor/reference for now · do NOT chunk the Bible into the SNIPED corpus at this time.** Reasons:
- The operator explicitly said to treat it as sacred/foundational, not generic business content. Folding scripture into a business knowledge base risks instrumentalizing it.
- There is **no appropriate existing domain** for scripture (`scripture`/`wisdom`/`theology`/`spirituality`/`faith`/`religion` all absent · verified). Chunking it would force either a misfit into business domains (wrong) or a brand-new domain (requires explicit operator approval and careful design).
- A reverent treatment needs design decisions (translation neutrality, citation format, theological humility) that should be made deliberately, not rushed into a mini-batch.

If the operator later chooses to proceed, it should be a **separate SPIRITUAL_FOUNDATION lane** with its own guardrails (below), its own ID namespace, and **NOT** mixed into capital/commercial/operator domains. A dedicated domain (e.g., `scripture` or `wisdom-tradition`) MAY be warranted at that point · **flagged, NOT created here.**

### Guardrails (reverence · context · theological humility)
- **Do NOT flatten scripture into hustle/business doctrine.** No "10 money lessons from Proverbs" framing. No instrumentalizing verses as operator tactics.
- **Reverence:** treat the text as sacred to many readers; neutral, respectful handling.
- **Context:** preserve book/chapter/verse citation (e.g., "Proverbs 3:5-6"); never quote out of context to make a business point.
- **Theological humility:** KJV is one translation among many; make NO doctrinal/denominational claims; do not adjudicate interpretation.
- **Separation:** keep it out of the SNIPED business retrieval paths; if ever chunked, a distinct batch_id and (proposed) distinct domain, not the commercial domains.
- **Optionality:** this does not change SNIPED direction or imply a "faith-based brand" pivot; it is foundational/personal grounding, held as such.

## 4. Overlap with current corpus

- **high level convos.docx:** 0 overlap · Earn Your Leisure / Miss Pinky transcripts are net-new. (Note: *Unreasonable Hospitality* is name-dropped inside a transcript but is not itself in the corpus · a possible future acquisition, not chunked here.)
- **The Bible:** 0 overlap · no scripture currently in the corpus.

## 5. Recommended next action (operator decision · none started)

1. **Intake-only now** (this report) · both files remain in the source universe, unstaged.
2. **Plan the HIGH_LEVEL_CONVOS lane** next (one curated mini-batch · existing domains · per-transcript attribution · decision-support framing) · highest-value of the two for the business corpus.
3. **Defer the Bible to a deliberate SPIRITUAL_FOUNDATION decision** · recommend HOLD as anchor/reference; do not chunk now; revisit as its own reverent track with explicit guardrail + (possible) new-domain approval.

**Sequencing recommendation:** (a) if the operator wants to keep building the business corpus, plan HIGH_LEVEL_CONVOS next (and, when authorized, stage the docx into an appropriate `raw/` folder first · likely `raw/07_CONTENT/` or a new transcripts subfolder · operator to confirm the folder). (b) Treat the Bible separately and unhurriedly: hold as a reverent anchor; only design a SPIRITUAL_FOUNDATION lane on explicit instruction. Do not bundle the two into one lane.

## 6. Recommended lane names + domain summary

| Resource | Lane name | One lane / split | Domains (existing) | New domain? | Chunk now? |
|---|---|---|---|---|---|
| high level convos.docx | `HIGH_LEVEL_CONVOS` | one curated mini-batch (split optional) | capital, commercial-architecture, operator-doctrine, culture, strategy, ai-tooling, content-strategy/media-business (light), ethics if warranted | No (hold "hospitality" → operator-doctrine/culture) | Yes, when authorized (plan first) |
| The Bible (KJV) | `SPIRITUAL_FOUNDATION` (preferred over WISDOM_CANON) | dedicated, separate track | none of the business domains fit · scripture/wisdom domain absent | MAYBE later (flagged · NOT created) | No · HOLD as reverent anchor/reference now |

## 7. Scope guards honored

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,430.
- Did NOT move, rename, or modify any source/raw file (read-only `file` / `wc` / `pdfinfo` / pandoc-to-/tmp / pdftotext-to-/tmp · temp deleted).
- Did NOT OCR and did NOT install anything.
- No CHUNKS.jsonl, no extracted dir created.
- Wrote only this report. Not committed (operator will review first).
