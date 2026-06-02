# BATCH_009 plan · advertising / copywriting / persuasion / positioning canon · 2026-05-22

Plan only. No staging, extraction, chunking, master-file updates, OCR, or commits. This plan defines BATCH_009 so a later authorized extraction session can run the locked SOP (extract → chunk → validate → ship → consolidate → session-save) without re-deriving scope.

**Source universe:** `~/AI-Brain-Refinery/raw/` (already staged). No new staging required.
**Theme:** advertising, copywriting, persuasion, positioning, offer construction, market education, trust, memorability, direct response, brand meaning, customer psychology, and SNIPED's commercial voice. The lane that gives SNIPED's external-facing copy (Carrd, IG, LinkedIn, ad creative, outreach, post-delivery emails) a theory backbone.

---

## 0 · Verified starting state (this session)

- Latest commit: `fdbf372 save session after CLAUDE_OPERATOR_DOCS consolidation`
- Total chunks: 1,141 · 8 numbered batches + 10 mini-batches · 60 official domains
- Working tree: clean
- BATCH_009: NOT started (no `BATCH_009_CHUNKS.jsonl`, no `batch_009_extracted/`, no `BATCH_009_COMPLETE.md`)
- **Decisive overlap finding:** BATCH_002 (Tier 1) chunked the strategy/founder titles (Shoe Dog, Zero to One, 48 Laws, Art of War, Creativity Inc, etc.); BATCH_003 (Tier 2) chunked the strategy/economics titles (Blockbusters, Company of One, Perennial Seller, Pricing Creativity, WWP Manifesto, etc.). **Neither touched the `advertising/`, `sales_positioning/`, or `persuasion_psych/` subfolders** · those are net-new BATCH_009 territory. Confirmed by reading the actual BATCH_002 + BATCH_003 chunk source_titles (0 of these candidate books appear).

---

## 1 · Candidate source locations

| Folder | Candidates | Role |
|---|---|---|
| `raw/02_TIER_1_CANON_BOOKS/advertising/` | 7 files (advertising + copywriting) | CORE |
| `raw/02_TIER_1_CANON_BOOKS/sales_positioning/` | 16 files (positioning, offers, memorability) | CORE + expansion + defer |
| `raw/03_TIER_2_CANON_BOOKS/persuasion_psych/` | 8 files (persuasion + customer psychology) | CORE + defer |
| `raw/10_REFERENCE/_intake_2026-05-18/document.pdf` | Seth Godin "This Is Marketing" (dup) | EXCLUDE (dedupe) |

**Operator-named priorities not staged in raw/ (ABSENT · flag for re-acquisition):** Sugarman (*Adweek Copywriting Handbook*), Caples (*Tested Advertising Methods*), Halbert (*Boron Letters*). Not present anywhere in raw/.

---

## 2 · Inventory by folder, filename, type, extraction method

### 2.1 · advertising/ (7)

| Author · Title | Type | Size | Method | Verdict |
|---|---|---:|---|---|
| Claude C. Hopkins · Scientific Advertising (2010) | pdf | 185 KB | pdftotext -layout | CORE |
| Drew Eric Whitman · Cashvertising (2009) | epub | 597 KB | stdlib zipfile / ebook-convert | CORE |
| Luke Sullivan · Hey, Whipple, Squeeze This (2008) | pdf | 4,999 KB | pdftotext -layout (100,496 words · text OK) | CORE |
| Eugene M. Schwartz · Breakthrough Advertising (2004) | pdf | 1,190 KB | pdftotext -layout | CORE |
| David Ogilvy · Confessions of an Advertising Man (2004) | pdf | 21,971 KB | **pdftotext returns 0 words · SCANNED image-only PDF** | DEFER (OCR-blocked) |
| Robert W. Bly · The Copywriter's Handbook (2006) | mobi | 768 KB | ebook-convert | CORE |
| Jon Steel · Truth, Lies and Advertising (Journal of Advertising, 1998) | pdf | 412 KB | pdftotext (1,455 words · a journal **book-review** by Neal M. Burns, not the book) | EXCLUDE (review stub) |

### 2.2 · sales_positioning/ (16)

| Author · Title | Type | Size | Verdict |
|---|---|---:|---|
| Seth Godin · This Is Marketing (2018) | pdf | 3,771 KB | CORE (the canonical copy · document.pdf is its byte-identical dup) |
| Seth Godin · Purple Cow (2003) | pdf | 1,871 KB | CORE |
| Jack Trout · Differentiate or Die (2008) | pdf | 1,148 KB | CORE |
| April Dunford · Obviously Awesome (2019) | epub | 2,058 KB | CORE |
| Alex Hormozi · $100M Offers (2021) | epub | 2,095 KB | CORE |
| Alex Hormozi · $100M Leads (2023) | epub | 16,784 KB | CORE |
| Chip & Dan Heath · Made to Stick (2007) | pdf | 921 KB | CORE |
| Donald Miller · Building a StoryBrand (2017) | mobi | 2,365 KB | CORE |
| Chris Voss · Never Split the Difference (2016) | epub | 455 KB | EXPANSION (negotiation / sales voice) |
| Adam Morgan · Eating the Big Fish (2009) | pdf | 2,902 KB | EXPANSION (challenger-brand positioning) |
| Al Ramadan et al · Play Bigger (2016) | epub | 421 KB | EXPANSION (category design) |
| Seth Godin · Tribes (2008) | epub | 149 KB | EXPANSION (market/community) |
| Christensen et al · Competing Against Luck (2016) | epub | 273 KB | EXPANSION (JTBD · customer choice) |
| Geoffrey Moore · Crossing the Chasm (2014) | mobi | 632 KB | DEFER (tech-adoption GTM · less copy/persuasion) |
| Rob Fitzpatrick · The Mom Test (2016) | azw3 | 262 KB | DEFER (customer-discovery · OMT-adjacent) |
| Clayton Christensen · The Innovator's Dilemma (2013) | pdf | 3,050 KB | DEFER (disruption strategy · not advertising/copy) |

### 2.3 · persuasion_psych/ (8 · Tier 2)

| Author · Title | Type | Size | Verdict |
|---|---|---:|---|
| Robert Cialdini · Influence | pdf | 3,490 KB | CORE (the persuasion canon) |
| Robert Cialdini · Pre-Suasion (2016) | epub | 2,346 KB | CORE |
| Jonah Berger · Contagious (2013) | mobi | 733 KB | CORE (why things catch on) |
| Richard Shotton · The Choice Factory (2018) | epub | 307 KB | CORE (25 behavioural biases in buying) |
| Rory Sutherland · Alchemy (2019) | epub | 2,494 KB | CORE (psycho-logic in brands) |
| Dan Ariely · Predictably Irrational (2010) | djvu | 3,502 KB | DEFER (`.djvu` · no djvutxt · format-blocked, like JLS) |
| Will Storr · The Status Game (2021) | epub | 483 KB | DEFER (status sociology → future status/culture lane) |
| W. David Marx · Status and Culture (2022) | epub | 4,034 KB | DEFER (status/taste sociology → future status/culture lane) |

**Tooling:** pdftotext, ebook-convert (epub/mobi/azw3), stdlib zipfile. No OCR. No new dependencies. (`.djvu` and the scanned Ogilvy PDF are the only unextractable items · both deferred.)

---

## 3 · Pre-flight source-quality / stub check (read-only peek · nothing written)

- **Confessions of an Advertising Man** · 21.9 MB but `pdftotext` yields **0 words** → scanned image-only PDF, no text layer. DEFER (no OCR per rules). The only staged Ogilvy title; "Ogilvy on Advertising" is absent. Flag for re-acquisition of a text edition.
- **Truth, Lies and Advertising (Jon Steel)** · 1,455 words · the header confirms it is a *Journal of Advertising* book review by Neal M. Burns (1998), NOT the Jon Steel book. EXCLUDE (review stub).
- **Hey, Whipple, Squeeze This** · 100,496 words · real text despite the 5 MB image-heavy size. INCLUDE.
- **Predictably Irrational** · `.djvu` · unextractable with current tooling. DEFER (format).
- All other CORE candidates are standard pdf/epub/mobi/azw3 with normal text density · no stubs detected.
- **No already-chunked overlap:** confirmed against BATCH_002/003 source_titles (§0). All candidates are net-new.

---

## 4 · document.pdf / This Is Marketing decision

**CONFIRMED: `document.pdf` IS Seth Godin's "This Is Marketing" (2018).** `document.pdf` (md5 `4a766745b4d72a388db8a8fca14ba7ed`) is **byte-identical** to the named `sales_positioning/Seth Godin - This Is Marketing ... .pdf` (same md5). It belongs in BATCH_009. **Decision:** chunk the canonical named copy in `sales_positioning/`; treat `document.pdf` as the duplicate and EXCLUDE it (0 chunks). This closes the CLAUDE_OPERATOR_DOCS reroute cleanly.

---

## 5 · Recommended inclusion vs defer / exclude

### 5.1 · INCLUDE (CORE · 18 books)
- **Advertising / copywriting (5):** Scientific Advertising (Hopkins), Cashvertising (Whitman), Hey Whipple Squeeze This (Sullivan), Breakthrough Advertising (Schwartz), The Copywriter's Handbook (Bly).
- **Persuasion / customer psychology (5):** Influence (Cialdini), Pre-Suasion (Cialdini), Contagious (Berger), The Choice Factory (Shotton), Alchemy (Sutherland).
- **Positioning / offers / memorability / market education (8):** This Is Marketing (Godin), Purple Cow (Godin), Differentiate or Die (Trout), Obviously Awesome (Dunford), $100M Offers (Hormozi), $100M Leads (Hormozi), Made to Stick (Heath), Building a StoryBrand (Miller).

### 5.2 · EXPANSION (operator-decision · include if a larger batch is wanted · ~+15-20 chunks)
Never Split the Difference (Voss), Eating the Big Fish (Morgan), Play Bigger (category design), Tribes (Godin), Competing Against Luck (Christensen JTBD).

### 5.3 · DEFER
- Confessions of an Advertising Man (Ogilvy · scanned, OCR-blocked · re-acquire text edition).
- Predictably Irrational (Ariely · `.djvu` · format-blocked).
- The Innovator's Dilemma + Crossing the Chasm (disruption / tech-GTM strategy · route to a strategy lane).
- The Mom Test (customer discovery · OMT-adjacent).
- The Status Game + Status and Culture (status/taste sociology · suggest a future status/culture mini-batch, or BATCH_010 lineage/culture).

### 5.4 · EXCLUDE
- document.pdf (byte-identical dup of named This Is Marketing).
- Truth, Lies and Advertising (a 1,455-word journal book-review, not the book).

### 5.5 · ABSENT (re-acquisition flags)
Sugarman (*Adweek Copywriting Handbook*), Caples (*Tested Advertising Methods*), Halbert (*Boron Letters*) · operator-named but not in raw/ · acquire to round out the direct-response canon.

---

## 6 · Estimated chunk yield + target range

CORE 18 books, chunked at canon-survey depth (the durable principles per book, not deep coverage), ~3-4 chunks each, plus cross-source synthesis.

| Cluster | Books | Per-book | Subtotal |
|---|---:|---|---:|
| Advertising / copywriting | 5 | ~4 | ~20 |
| Persuasion / customer psychology | 5 | ~4 | ~20 |
| Positioning / offers / memorability | 8 | ~3-4 | ~26-32 |
| Cross-source synthesis | n/a | the SNIPED commercial-voice synthesis | ~3-4 |

**Target: ~70-78 chunks. Planning range: 60-85.** Matches the documented BATCH_009 estimate (60-80). If the operator adds the 5 EXPANSION books, target rises to ~85-100 (range 80-110).

---

## 7 · Domain set (existing-where-possible) + NEW-domain flag

**Existing domains that cover this batch (recommended default · NO new domain):**

| Domain | Where it comes from | Status |
|---|---|---|
| `copywriting` (6) | the copy craft (Hopkins, Bly, Schwartz, Cashvertising, Hey Whipple) · grows substantially | exists |
| `meta-advertising` | advertising principles / philosophy (Ogilvy-style maxims, Schwartz market-awareness) | exists |
| `positioning` (4) | Differentiate or Die, Obviously Awesome, Purple Cow, category design · grows | exists |
| `brand-psychology` | persuasion + customer psychology (Cialdini, Shotton, Sutherland, Berger) | exists |
| `sales-flow` | offers + negotiation + the selling system (Hormozi, Voss) | exists |
| `offer-design` | $100M Offers, offer construction | exists |
| `content-strategy` | memorability / stickiness / contagion (Made to Stick, Contagious) | exists |
| `brand` | brand meaning / StoryBrand / Tribes | exists |
| `commercial-architecture` | the commercial model behind the offers | exists |
| `strategy` | market education, differentiation strategy | exists |
| `client-application` | applying the copy/persuasion craft to client work | exists |
| `aesthetics` | brand voice / craft of the line | exists |
| `operator-process` | the repeatable selling/copy system | exists |

### NEW-domain flag (operator decision · NOT recommended by default)
The operator's proposed set named `advertising` and `persuasion`, which do **NOT** currently exist (they would be the 61st/62nd domains). **Recommendation: do NOT introduce them** · `copywriting` + `meta-advertising` + `brand` cover advertising, and `brand-psychology` + `sales-flow` + `positioning` cover persuasion, consistent with the standing "flag NEW only if absolutely necessary" rule. **Operator-approval option:** if you want these two foundational lanes to have dedicated retrieval buckets (Cialdini is THE persuasion canon; `copywriting` is currently thin at 6), `advertising` and `persuasion` are the cleanest new-domain candidates since `systems-thinking`. Either way, the extractor will NOT introduce a new domain without explicit authorization · if extraction reveals a genuine gap, halt and report.

---

## 8 · How BATCH_009 connects to the corpus

- **B2B_POSITIONING_CLAUDE_OPERATOR:** B2B captured the buyer-side market reception of AI services; BATCH_009 supplies the persuasion + positioning + offer theory that shapes how SNIPED writes that B2B copy. Differentiate or Die + Obviously Awesome are the positioning backbone behind the B2B one-liner.
- **OPPORTUNITY_MANAGEMENT_TEMPLATES:** $100M Offers + $100M Leads give the offer-construction and lead-gen theory behind the opportunity hopper and business-case; the Mom Test (deferred) is the discovery complement.
- **CLAUDE_OPERATOR_DOCS:** the Claude-operator docs are HOW SNIPED produces copy at leverage; BATCH_009 is WHAT good copy is · the craft standard the AI-assisted production is held to.
- **BATCH_008 AI/tech canon:** B008's augmentation thesis says AI amplifies a human craft; BATCH_009 is that craft for the commercial-voice lane · the human judgment layer the AI copy production serves.
- **SNIPED offers / outreach / content doctrine (BATCH_007 + intel memories):** BATCH_009 is the primary-source theory under the locked outreach + content + offer doctrine (the WWP Manifesto, Pricing Creativity, and Hit Makers intel already in the corpus get their advertising-canon foundation here). Made to Stick + Contagious back the content/distribution doctrine; Cialdini backs the trust/outreach doctrine.

---

## 9 · Deliverables (defined here · produced only in the authorized extraction session)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/BATCH_009_CHUNKS.jsonl` |
| Extracted text dir | `01_KNOWLEDGE_BASE/batches/batch_009_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/BATCH_009_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/BATCH_009_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/BATCH_009_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/BATCH_009_COMPLETE.md` |
| Extractor script | `scripts/extract_batch_009.py` |
| Chunk-writer script | `scripts/write_batch_009_chunks.py` |

Schema: the canonical 12-field schema (`chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags`). ID pattern `BATCH_009_NNN`. batch_id `BATCH_009`.

---

## 10 · Validation gates (at the authorized extraction session)
The 6 jsonl-validation checks (parse · 12 fields · chunk_id uniqueness · single batch_id `BATCH_009` · source_file resolution · count) plus: pre-flight stub peek on every source, dedupe document.pdf, copyright-safe SHORT quotes only (all in-copyright trade books), SNIPED-authored output em-dash clean, no new dependencies, no OCR, no new domain without authorization.

---

## 11 · What this plan does NOT do
- No staging, extraction, chunking, or master-file updates.
- No OCR (so the scanned Ogilvy stays deferred) · no new dependencies.
- No touching recovery items (Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi).
- No commits. BATCH_009 not started.

Authorization required before any extraction. Stop here.

---

## 12 · Open operator decisions surfaced
1. **EXPANSION set** (Never Split the Difference, Eating the Big Fish, Play Bigger, Tribes, Competing Against Luck) · include in BATCH_009 (→ ~85-100 chunks) or hold? Default: hold to the 18-book CORE for a focused 60-80.
2. **NEW domains `advertising` + `persuasion`** · introduce (operator-approved) or reuse existing (`copywriting` / `meta-advertising` / `brand-psychology` / `sales-flow`)? Default: reuse, no new domain.
3. **Deferred status/culture pair** (Status Game, Status and Culture) · spin a future status/culture mini-batch or fold into BATCH_010 lineage/culture? Operator decision.
4. **Re-acquire** Ogilvy text edition (Confessions is a scan) + Sugarman / Caples / Halbert (absent) to complete the direct-response canon?

---

## 13 · Revision log
- **rev 1 (2026-05-22):** First BATCH_009 plan. 31 candidate books located across `advertising/` (7), `sales_positioning/` (16), `persuasion_psych/` (8) + document.pdf. Confirmed BATCH_002/003 never chunked these subfolders (net-new). document.pdf confirmed = This Is Marketing (md5-identical dup · excluded). Pre-flight peek caught Confessions = scanned/0-text (deferred) and Truth-Lies-and-Advertising = journal review stub (excluded). CORE 18 books (target ~70-78 · range 60-85); EXPANSION 5 (operator decision); DEFER 6 (incl. djvu + scan); ABSENT re-acquisition flags (Sugarman/Caples/Halbert). Recommended existing-domain reuse with `advertising`/`persuasion` flagged as optional operator-approved new domains. No extraction, chunking, master updates, or commits performed.
