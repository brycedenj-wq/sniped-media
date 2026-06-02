# CULTURE_AND_STATUS mini-batch plan · status / culture / symbolic-value theory · 2026-05-22

Plan only. No staging, extraction, chunking, master-file updates, OCR, or commits. This plan defines the CULTURE_AND_STATUS mini-batch so a later authorized extraction session can run the locked SOP (extract → chunk → validate → ship → consolidate → session-save) without re-deriving scope.

**Source universe:** `~/AI-Brain-Refinery/raw/` (already staged). No new staging required.
**Theme:** status, culture, symbolic value, hierarchy, taste, identity signaling, group belonging, fashion/status mechanics, cultural capital, social performance, and how status systems shape brand, image, and SNIPED positioning. It is the status-theory lane that explains the lived status games in the BATCH_010 hip-hop memoirs and the signaling mechanics under the BATCH_009 brand-psychology.
**Naming:** `CULTURE_AND_STATUS` (non-BATCH_NNN mini-batch slug · preserves numbered-batch slots). batch_id `CULTURE_AND_STATUS`. ID pattern `CULTURE_AND_STATUS_NNN`.

---

## 0 · Verified starting state (this session)

- Latest commit: `6c82075 save session after BATCH_010 consolidation`
- Total chunks: 1,262 · 10 numbered batches + 10 mini-batches · 60 official domains
- Working tree: clean
- CULTURE_AND_STATUS: NOT started (no `CULTURE_AND_STATUS_CHUNKS.jsonl`, no `culture_and_status_extracted/`, no `CULTURE_AND_STATUS_COMPLETE.md`)
- These two books were HELD from BATCH_009 (Status sociology) and BATCH_010 (deferred to this lane).

---

## 1 · Candidate source location

Both held Status-pair books are in `raw/03_TIER_2_CANON_BOOKS/persuasion_psych/`:

| File | Title | Author |
|---|---|---|
| ` Will Storr - The Status Game_ On Social Position and How We Use It (2021, William Collins) - libgen.li.epub` | The Status Game (2021) | Will Storr |
| ` W. David Marx - Status and Culture_ How Our Desire for Social Rank Creates Taste, Identity, Art, Fashion, and Constant Change (2022, Viking) - libgen.li.epub` | Status and Culture (2022) | W. David Marx |

(Both filenames have a leading space · the extractor will match by keyword to avoid the trap.)

---

## 2 · Inventory by filename, format, extraction method (read-only composition peek)

| # | Title | Type | Size | Images | Approx words | Method |
|--:|---|---|---:|---:|---:|---|
| 1 | The Status Game (Storr) | epub | 483 KB | 4 | 129,713 | stdlib zipfile + HTML-strip |
| 2 | Status and Culture (Marx) | epub | 4,034 KB | 9 | 153,729 | stdlib zipfile + HTML-strip |

Both are clean prose epubs with minimal images. No OCR. No new dependencies.

---

## 3 · Pre-flight source-quality / stub check (read-only · nothing written)

- **No stubs.** Both have substantial extractable text (129,713 and 153,729 words).
- **No format issues** · standard epubs, the proven stdlib zipfile path.
- **No already-chunked overlap (verified definitively).** Neither book is a source_title or source_file in ANY `*_CHUNKS.jsonl` (checked "The Status Game_ On Social Position", "Status and Culture_ How Our Desire", "Will Storr", "W. David Marx" → 0 refs each). The earlier "status game" string hits were the *phrase* inside BATCH_003's de Botton **Status Anxiety** chunks (which discuss the status game), NOT chunks from Storr's or Marx's books. Both are genuinely net-new.

---

## 4 · Recommended inclusion vs defer / exclude

### 4.1 · INCLUDE (CORE · 2 books)
The Status Game (Storr) + Status and Culture (Marx). Both clean, net-new, on-theme.

### 4.2 · No deferrals / exclusions
No format-blocked, stub, or duplicate items in this lane. The mini-batch is exactly these two books plus synthesis.

---

## 5 · Estimated chunk yield + target range

Two dense theory books, chunked at the durable-concept depth (the status mechanics, not exhaustive coverage), plus synthesis.

| Source | Estimate |
|---|---:|
| The Status Game (Storr) | ~6-8 |
| Status and Culture (Marx) | ~6-8 |
| Cross-source synthesis | ~2-3 |

**Target: ~14-16 chunks. Planning range: 12-20.** A focused mini-batch (consistent with the documented ~8-14 estimate, sized up slightly because both books are ~140k-word canonical status theory deserving ~6-8 each). Can be trimmed to ~12 if the operator wants it tighter.

---

## 6 · Domain set (existing-where-possible · NO new domain expected)

All from the operator-approved list, all pre-existing:

| Domain | Where it comes from | Status |
|---|---|---|
| `status` (11) | the core · status games, social rank, the hidden status drive · directly extends de Botton (Status Anxiety) + Simler/Hanson (Elephant in the Brain) already in this domain | exists |
| `culture` (37) | status as the engine of culture, trends, subcultures, taste-as-belonging (Marx) | exists |
| `systems-thinking` (28) | status as a system · the mechanics of how rank propagates into taste and cultural change | exists |
| `brand-psychology` (20) | signaling, distinction, conspicuous/inconspicuous consumption, identity signaling | exists |
| `aesthetics` (65) | taste formation, the status logic of style, why aesthetics shift | exists |
| `strategy` (148) | the positioning application · how to operate within (not chase) status systems | exists |
| `lineage` (19) | only where inherited status / cultural capital warrants it (light · likely 0-1) | exists |

### NEW-domain flag
**Recommendation: introduce NO new domain.** `status` is the natural home and already exists (with de Botton + Simler/Hanson). The mini-batch deepens it rather than needing a new bucket. If extraction reveals a genuine gap, halt and report.

---

## 7 · How this mini-batch connects to the corpus

- **BATCH_010 lineage + Black culture canon:** BATCH_010 shows the lived status games (the come-up, persona-construction, the boss image); CULTURE_AND_STATUS supplies the THEORY of why those status games work. The hip-hop memoirs are the case studies; Storr/Marx are the mechanics.
- **BATCH_009 commercial voice:** the signaling and distinction theory under B009's brand-psychology (Cialdini social proof, Sutherland's costly-signalling, Shotton's distinctiveness) · the deeper status logic beneath the persuasion levers.
- **LITERARY_CANON_BLACK:** the status / dignity / recognition themes (Morrison, Hurston) get their sociological frame here · why recognition and rank are load-bearing.
- **BATCH_005 photography canon:** status signaling via image, taste-as-distinction, and the aesthetics of rank · directly informs the SNIPED image-as-status-signal thesis (the portrait confers status).
- **SNIPED Lineage Doctrine + `intel_status_psychology` memory:** this mini-batch is the canonical-text extension of the existing status-psychology intel (de Botton's status anxiety + Simler/Hanson's hidden-motive signaling), giving SNIPED two more primary status texts to reason about pricing, premium-buyer psychology, and the founder-buyer experience.

---

## 8 · Deliverables (defined here · produced only in the authorized extraction session)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/CULTURE_AND_STATUS_CHUNKS.jsonl` |
| Extracted text dir | `01_KNOWLEDGE_BASE/batches/culture_and_status_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/CULTURE_AND_STATUS_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/CULTURE_AND_STATUS_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/CULTURE_AND_STATUS_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/CULTURE_AND_STATUS_COMPLETE.md` |
| Extractor script | `scripts/extract_culture_and_status.py` |
| Chunk-writer script | `scripts/write_culture_and_status_chunks.py` |

Schema: the canonical 12-field schema (`chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags`). ID pattern `CULTURE_AND_STATUS_NNN`. batch_id `CULTURE_AND_STATUS`.

---

## 9 · Validation gates (at the authorized extraction session)
The 6 jsonl-validation checks (parse · 12 fields · chunk_id uniqueness · single batch_id `CULTURE_AND_STATUS` · source_file resolution · count) plus: pre-flight stub peek on both sources, copyright-safe SHORT quotes only (in-copyright trade books · a sentence or two), SNIPED-authored output em-dash clean, no new dependencies, no OCR, no new domain without authorization.

---

## 10 · What this plan does NOT do
- No staging, extraction, chunking, or master-file updates.
- No OCR · no new dependencies.
- No touching recovery/acquisition items (Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi, Confessions text edition, Sugarman/Caples/Halbert, Predictably Irrational).
- No commits. CULTURE_AND_STATUS not started.

Authorization required before any extraction. Stop here.

---

## 11 · Open operator decisions surfaced
1. **Chunk depth** · target ~14-16 (6-8 per book · recommended) or trim to ~12 for a tighter mini-batch?
2. **`lineage` usage** · include a light inherited-status / cultural-capital chunk (1) or keep the lane to status/culture/systems-thinking/brand-psychology/aesthetics/strategy only? Default: light, only if a chunk genuinely warrants it.

---

## 12 · Revision log
- **rev 1 (2026-05-22):** First CULTURE_AND_STATUS plan. 2 held Status-pair books located in `persuasion_psych/` (Storr · The Status Game · 129,713 words; Marx · Status and Culture · 153,729 words). Read-only peek: both clean prose epubs, no stubs, minimal images. Verified definitively net-new (0 source-refs in any chunk file · the prior "status game" hits were the phrase inside BATCH_003's Status Anxiety chunks). INCLUDE both; target ~14-16 chunks (range 12-20). Existing domains only (status, culture, systems-thinking, brand-psychology, aesthetics, strategy, light lineage) · no new domain. Extends the existing `status` domain (de Botton + Simler/Hanson). No extraction, chunking, master updates, or commits performed.
