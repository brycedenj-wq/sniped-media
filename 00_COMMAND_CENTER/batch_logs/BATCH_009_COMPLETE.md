# BATCH_009 complete · advertising / copywriting / persuasion / positioning canon · 2026-05-22

## Status

**Extraction:** complete (18 of 18 CORE sources · 0 failures · 1,251,712 words · pdftotext + stdlib zipfile + ebook-convert · no OCR · no new dependencies).
**Chunking:** complete (76 chunks · target ~70-78 · inside the 60-85 planned range).
**Validation:** 6/6 PASS per `.claude/skills/jsonl-validation/SKILL.md` + 11 additional checks PASS.
**Master files:** NOT updated (per operator instruction · awaits `master-consolidation`). NO NEW domain to register.

## Artifacts produced

| File | Path | Status |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/BATCH_009_CHUNKS.jsonl` | written · 76 chunks · validated |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/batch_009_extracted/` | 18 normalized .txt |
| Extraction script | `scripts/extract_batch_009.py` | written · pdftotext + zipfile + ebook-convert |
| Chunk writer | `scripts/write_batch_009_chunks.py` | written |
| Extraction log | `00_COMMAND_CENTER/batch_logs/BATCH_009_EXTRACTION_LOG.md` | written |
| Summary | `01_KNOWLEDGE_BASE/summaries/BATCH_009_SUMMARY.md` | written |
| Source index | `01_KNOWLEDGE_BASE/indexes/BATCH_009_SOURCE_INDEX.md` | written |
| Completion marker | `00_COMMAND_CENTER/batch_logs/BATCH_009_COMPLETE.md` | this file |

## Headline numbers

- CORE sources extracted: 18 of 18 (5 advertising/copy + 5 persuasion + 8 positioning/offers)
- Chunks: 76 (target ~70-78 · range 60-85 · landed 76)
- Distinct source_file references: 18
- Domains touched: 12 (copywriting 14 · brand-psychology 14 · positioning 10 · content-strategy 8 · strategy 6 · brand 5 · meta-advertising 5 · commercial-architecture 3 · offer-design 3 · sales-flow 3 · operator-process 3 · aesthetics 2 · NO NEW domain)
- Unique batch_id: `BATCH_009`
- Extraction: pdftotext + zipfile + ebook-convert · 0 new dependencies · no OCR

## Validation summary

| Check | Result |
|---|---|
| JSONL parse | PASS |
| Required fields present per line | PASS · 0 missing (all 12 fields) |
| chunk_id uniqueness | PASS · 0 duplicates across 76 chunks |
| batch_id consistency | PASS · single value `BATCH_009` |
| source_file resolution | PASS · 18 distinct files, all resolve under `batch_009_extracted/` |
| Counts | 76 chunks · 18 unique sources |

Em-dash sweep: PASS · 0 em-dashes in SNIPED-authored output.

## Additional checks (per operator requirement)

- **Exactly the 18 CORE sources chunked.** CONFIRMED.
- **EXPANSION set contributed 0 chunks** (Never Split the Difference, Eating the Big Fish, Play Bigger, Tribes, Competing Against Luck). CONFIRMED.
- **Status pair contributed 0 chunks** (The Status Game, Status and Culture). CONFIRMED.
- **Blocked/deferred contributed 0 chunks** (Confessions of an Advertising Man, Predictably Irrational). CONFIRMED.
- **Excluded contributed 0 chunks** (document.pdf, Truth-Lies-and-Advertising review stub). CONFIRMED.
- **No NEW domains.** CONFIRMED · all 12 domains pre-exist; `advertising` + `persuasion` were NOT introduced.
- **Master files unchanged at 1,141.** CONFIRMED · no BATCH_009 entry in MASTER_CHUNK_MAP.json.
- **raw/ source files not modified.** CONFIRMED.
- **No OCR / no new dependencies.** CONFIRMED · pdftotext + zipfile + ebook-convert only (so the scanned Ogilvy stayed deferred).
- **Copyright-safe quote discipline.** CONFIRMED · longest direct_quote = 14 words · 12 of 76 chunks carry a quote.

## Per-source chunk distribution

| Source | Chunks |
|---|---:|
| Influence (Cialdini) | 6 (5 + 1 synthesis) |
| Scientific Advertising (Hopkins) | 5 (4 + 1 synthesis) |
| Differentiate or Die (Trout) | 5 (4 + 1 synthesis) |
| Contagious (Berger) | 5 (4 + 1 synthesis) |
| Cashvertising, Hey Whipple, Breakthrough Advertising, Copywriter's Handbook | 4 each |
| Pre-Suasion, Choice Factory, Alchemy | 4 each |
| This Is Marketing, Obviously Awesome, $100M Offers, $100M Leads, Made to Stick, Building a StoryBrand | 4 each |
| Purple Cow (Godin) | 3 |

## Domain distribution (NO NEW domain)

| Domain | Chunks |
|---|---:|
| copywriting | 14 |
| brand-psychology | 14 |
| positioning | 10 |
| content-strategy | 8 |
| strategy | 6 |
| brand | 5 |
| meta-advertising | 5 |
| commercial-architecture | 3 |
| offer-design | 3 |
| sales-flow | 3 |
| operator-process | 3 |
| aesthetics | 2 |

## Failed / deferred sources

None failed. Per the plan: Confessions of an Advertising Man (scanned/OCR-blocked) + Predictably Irrational (.djvu) deferred; the EXPANSION set + Status pair deferred; document.pdf + Truth-Lies excluded; Sugarman/Caples/Halbert absent (re-acquisition flags). All 0 chunks.

## Deviations from BATCH_009_PLAN.md

1. **Final count 76** (target ~70-78 · range 60-85). On target.
2. **CORE-only** (18 books); EXPANSION + Status pair deferred as instructed.
3. **No new domain** (advertising/persuasion routed to existing copywriting / meta-advertising / brand-psychology / sales-flow).
4. **No structural deviations.** No master files updated. No new dependencies. No OCR.

## What is canonical now (post-validation)

The 76 chunks in `BATCH_009_CHUNKS.jsonl` are validated and ready for master-consolidation. Until `master-consolidation` runs:
- `MASTER_INDEX.md` still shows 8 batches + 10 mini-batches (1,141 chunks).
- `MASTER_CHUNK_MAP.json` still shows 1,141 total chunks · no BATCH_009 entry.
- `ACTIVE_KNOWLEDGE_STATE.md` next-action still names BATCH_009 (now executed, pending consolidation).

After authorized master-consolidation, the corpus will reflect 9 numbered batches + 10 mini-batches (1,217 chunks · 60 unique domains · NO new domain).

## Follow-ups flagged

- **Re-acquisition:** Confessions of an Advertising Man (Ogilvy text edition · the staged copy is a scan); Sugarman / Caples / Halbert (absent · the direct-response trio).
- **Deferred for a future lane:** Predictably Irrational (djvu); the EXPANSION set (Never Split the Difference, Eating the Big Fish, Play Bigger, Tribes, Competing Against Luck); the Status pair (The Status Game, Status and Culture → future culture/status mini-batch or BATCH_010).
- **Literary recovery items** (Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi) remain flagged.

## Next recommended action

**Option A · commit BATCH_009 artifacts, then authorize `master-consolidation BATCH_009`** (no new domain · new total 1,217).
**Option B · pause for review** of the 76 chunks (especially the persuasion-ethics framing and the synthesis chunks), then authorize commit + consolidation.

Stopping here per the operator's execution spec: "Stop after validation and reporting."
