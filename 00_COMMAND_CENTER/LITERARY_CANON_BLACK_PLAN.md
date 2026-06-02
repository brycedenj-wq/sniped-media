# LITERARY_CANON_BLACK mini-batch plan · 2026-05-20

Plan only. No extraction, no chunking, no master-file updates, no BATCH_008 start, no commit. Stops after this plan is written.

This mini-batch extracts literary + cultural-canon signal from the Black literary canon staged in the 2026-05-19 intake, to strengthen the locked Lineage Doctrine, cultural memory, voice, dignity, survival, identity formation, Black interiority, and SNIPED's refusal to become shallow content. It is the first of the 3 queued literary-canon mini-batches and the first LITERARY (vs operator/AI) lane in the corpus.

---

## 0 · Headline

- **4 files in the lane · 3 usable full-text sources · 1 unusable stub.** To Kill a Mockingbird is NOT present (see section 3).
- **CRITICAL FINDING · Beloved PDF is a STUB, not the novel.** It is a 698-word, 4-page publisher-blurb + SEO-spam page ("Top 10 Best Seller Books" ad list with Verity, It Ends with Us, etc.), not Morrison's prose. DEFER Beloved (re-acquire real text); do NOT chunk it. Flagged below.
- **Usable sources (3 files · 5 novels):** The Bluest Eye (Morrison · mobi), Their Eyes Were Watching God (Hurston · epub-in-zip), and The Color Purple Collection (Walker · epub · contains 3 novels: The Color Purple + The Temple of My Familiar + Possessing the Secret of Joy).
- **Extraction:** stdlib `zipfile` + HTML-strip for the 2 epub-family files (proven in the peek · handles the `.zip` extension cleanly · no new deps); `ebook-convert` for the `.mobi`. No new dependencies. No OCR.
- **Estimated yield:** 22-32 chunks · target ~28 (Beloved deferral is offset by the Walker collection's 3 novels + cross-cutting synthesis).
- **Domains:** culture (existing), `lineage` (**NEW domain · approved by operator brief**), operator-doctrine (existing · only where directly tied to SNIPED identity), aesthetics (existing · only where tied to voice/image/form), strategy (existing · only if needed).
- **Copyright discipline:** these are in-copyright novels. Extracted full text is for INTERNAL chunk-authoring reference only; chunks capture THEMES + cultural-canon signal + SHORT illustrative quotes (a sentence or two · fair-use scale). Never reproduce long passages in `direct_quotes`.

---

## 1 · Source files confirmed on disk

`raw/02_TIER_1_CANON_BOOKS/literary_canon_black/` · 4 files.

| # | File | Author / Title | Type | Size | Status |
|--:|---|---|---|---:|---|
| 1 | `Toni Morrison - The Bluest Eye (2007, Knopf Doubleday) - libgen.li.mobi` | Toni Morrison · *The Bluest Eye* (1970) | Mobipocket v6 (magic-confirmed "The Bluest Eye") | 532 KB | USABLE · full novel |
| 2 | `Zora Neale Hurston - Their Eyes Were Watching God (2009, HarperCollins) - libgen.li.zip` | Zora Neale Hurston · *Their Eyes Were Watching God* (1937) | EPUB inside a `.zip` (mimetype + OPF present · file magic = EPUB) | 768 KB | USABLE · full novel (71k+ words sampled) |
| 3 | `[The Color Purple 1 ...] The Color Purple Collection ... {Walker, Alice}(2012, Open Road) - libgen.li.epub` | Alice Walker · *The Color Purple Collection* (The Color Purple 1982 + The Temple of My Familiar 1989 + Possessing the Secret of Joy 1992) | EPUB · 293 html docs | 5.16 MB | USABLE · 3 full novels |
| 4 | `[Beloved Trilogy 1 ...] Beloved{Toni Morrison}(1987){...} libgen.li.pdf` | Toni Morrison · *Beloved* (1987) | PDF · 4 pages | 234 KB | **STUB · NOT the novel · DEFER** |

### The Beloved problem (read-only peek confirmed)

The Beloved PDF contains only: the back-cover blurb ("Sethe, its protagonist, was born a slave...") followed by a "Top 10 Best Seller Books" advertising list (Verity, It Ends with Us, I'm Glad My Mom Died, Fairy Tale, Ugly Love, etc.) with "Read More..." spam links. 698 words total · zero novel prose. This is a download-site SEO stub, not the text of Beloved.

**Disposition:** DEFER. Do NOT chunk Beloved from this file (there is no prose to chunk, and a summary-only chunk authored from a marketing blurb would be exactly the shallow content the brief says SNIPED refuses). Flag for real-text re-acquisition (a proper epub/pdf of Beloved). If the operator wants Beloved represented in the interim, that is a separate decision · default recommendation is clean deferral.

---

## 2 · Per-file extraction method

A read-only peek (stdlib `zipfile` to stdout for the epub-family files · `pdftotext` for the PDF · file-magic for the mobi) was run during planning. No files written.

| Source | Method | Rationale |
|---|---|---|
| The Bluest Eye (`.mobi`) | `ebook-convert <mobi> <txt>` | Calibre is the right tool for mobi; on PATH. |
| Their Eyes (`.zip` = epub) | stdlib `zipfile` + HTML-strip → txt | The `.zip` extension would snag `ebook-convert` (expects `.epub`); stdlib reads the zip container directly and cleanly (proven in peek · 71k+ words). No rename of raw/ needed, no new deps. |
| Color Purple Collection (`.epub`) | stdlib `zipfile` + HTML-strip → txt | Consistent with Their Eyes · 293 html docs · proven in peek (40k+ words sampled). Avoids any calibre quirks on the 3-novel collection. |
| Beloved (`.pdf`) | NONE · DEFER | Stub · not the novel. |

Output: one normalized `.txt` per usable source FILE in `01_KNOWLEDGE_BASE/batches/literary_canon_black_extracted/` (`bluest_eye_morrison.txt`, `their_eyes_hurston.txt`, `color_purple_collection_walker.txt`). The collection's 3 novels share one extracted file; the chunk concept-map records which novel each chunk draws from. Sanity floor: each extracted file >= 5,000 words (these are full novels); halt + surface if any comes back tiny (would indicate a stub like Beloved).

**No OCR** · all 3 usable sources are real digital text. No new dependencies (`ebook-convert` on PATH · `zipfile` is stdlib).

---

## 3 · To Kill a Mockingbird decision

**TKAM is NOT in this lane and is EXCLUDED from LITERARY_CANON_BLACK.** Per `STAGING_PLAN_2026-05-19_INTAKE.md` §2.7, Lee TKAM was an OPTIONAL 5th title with an open operator decision (route to `literary_canon_black/` or `literary_canon_general/`). It was not staged into `literary_canon_black/`, so it is not part of this mini-batch.

**Recommendation:** keep TKAM OUT of LITERARY_CANON_BLACK. This lane is a coherent canon of Black women's literary voice (Morrison · Hurston · Walker); TKAM is white-authored Southern lit and would dilute the lane's thesis (Black interiority / lineage / voice from inside). If the operator wants TKAM chunked, route it to a future `LITERARY_CANON_GENERAL` mini-batch or handle it as a deliberate separate add · not here.

---

## 4 · Estimated chunk yield · 22-32 chunks · target ~28

Literature chunks differently from operator/AI material: chunk by THEME + load-bearing motif (not per-chapter), each chunk = a durable cultural-canon concept with short illustrative quotes. Provisional map:

### Per-novel thematic chunks

| Novel (author) | Est. chunks | Candidate themes |
|---|---:|---|
| The Bluest Eye (Morrison) | 6-8 | the beauty-standard wound / internalized racism / Pecola and the unloved gaze / community as witness and complicity / seasons-as-structure / whose-story-gets-told |
| Their Eyes Were Watching God (Hurston) | 6-8 | Janie's self-possession / voice and vernacular as dignity / the porch and communal storytelling / the horizon as desire / Black female interiority / love and autonomy / folklore and oral tradition |
| The Color Purple (Walker) | 6-8 | epistolary voice / letters to God / Celie's survival and becoming / sisterhood (Celie + Nettie + Shug) / liberation and self-authorship / spirituality reimagined |
| The Temple of My Familiar (Walker) | 2-3 | ancestral memory / inherited story / myth and the familiar (light coverage · companion novel) |
| Possessing the Secret of Joy (Walker) | 2-3 | the body, ritual, and harm / cultural trauma and witness (light coverage · companion novel) |

### Cross-cutting synthesis chunks (~4-5)

| Chunk | Domain |
|---|---|
| The Black literary canon as Lineage-Doctrine backing · work from INSIDE the lineage | lineage |
| Voice + vernacular as craft and dignity (Hurston/Walker) · the anti-shallow-content thesis | culture / aesthetics |
| Black interiority + double-consciousness · who is seen, who narrates | culture |
| Cultural memory, survival, and inherited story across the three authors | lineage |
| Artistic seriousness as refusal · the canon SNIPED measures itself against | operator-doctrine |

That is ~24-30 mapped. Range 22-32, target ~28. **Note:** the staging plan's 25-35 estimate assumed Beloved was usable; with Beloved deferred, the depth comes from the Walker 3-novel collection + the synthesis chunks. If the operator later supplies real Beloved text, +5-7 chunks (a follow-up addendum).

---

## 5 · Approved domains / tags

| Domain | Status | Use |
|---|---|---|
| culture | EXISTS (5) | primary on the voice/interiority/witness/memory chunks · roughly triples this thin domain |
| `lineage` | **NEW · approved by operator brief** | primary on the Lineage-Doctrine-backing + inherited-story + survival chunks · the 59th domain |
| operator-doctrine | EXISTS (39) | only where DIRECTLY tied to SNIPED identity (e.g. artistic-seriousness-as-refusal · the canon as the bar SNIPED measures against) · sparing |
| aesthetics | EXISTS (43) | only where tied to voice/image/form (e.g. vernacular-as-craft, the gaze) · sparing |
| strategy | EXISTS (97) | only if a chunk frames the canon as a positioning asset · likely 0 |

**NEW-domain flag:** `lineage` does not yet exist in the corpus (the Lineage Doctrine lives as feedback-memory + a brief doc, not as a chunk domain). The operator's brief explicitly lists `lineage` as an approved domain, so this plan treats it as authorized · it will be the corpus's 59th unique domain. Surfacing it here per the AGENTS.md "surface NEW domains" rule.

**Recommended tag bank:** `literary-canon`, `black-literary-canon`, `lineage-doctrine`, `cultural-memory`, `voice`, `vernacular`, `dignity`, `survival`, `identity-formation`, `double-consciousness`, `black-interiority`, `witness`, `the-gaze`, `whose-story-gets-told`, `folklore`, `oral-tradition`, `inherited-story`, `sisterhood`, `epistolary-voice`, `artistic-seriousness`, `anti-shallow-content`, `morrison`, `hurston`, `walker`, `bluest-eye`, `their-eyes-were-watching-god`, `color-purple`.

**Aging note:** none · these are timeless primary literary texts (1937-1992). No `ai-tooling-aging-risk`. Capture publication years in chunks.

---

## 6 · How this mini-batch connects to the rest of the corpus

### BATCH_004 aesthetic doctrine
- The canon's interiority, restraint, and seriousness back the SNIPED quiet-luxury-editorial restraint and the locked "refusal to become shallow content." Morrison/Hurston/Walker are the literary embodiment of depth-over-volume. Cross-tag `aesthetics` where voice/form is the load-bearing element.

### BATCH_005 photography canon
- Black interiority + witness + dignity ↔ the SNIPED portraiture-as-dignity and the question of the gaze (who is seen, who is rendered fully human). Hurston's "the horizon" and the act of witnessing ↔ photographic seeing; The Bluest Eye's beauty-standard wound ↔ the SNIPED counter-position on whose beauty gets photographed.

### BATCH_007 operator doctrine + the Lineage Doctrine
- Directly strengthens the locked Lineage Doctrine (`feedback_lineage_doctrine` · work from INSIDE the lineage, single-visit cultural tourism refused). Cultural memory + survival + identity-formation are the primary-source literary grounding for that doctrine. The `lineage` domain is the chunk-level home for this.

### INTELLECTUAL_ARTIST_FRAME
- MJ Moonwalk (IAF) gave the operator-doctrine cluster a Black artistic-seriousness exemplar in performance; this mini-batch gives the LITERARY canon of Black artistic seriousness. Both embody depth-over-shallowness and craft-as-dignity · sibling cultural-canon logic across performance and literature.

### Future BATCH_010 culture / lineage / Black culture
- This is the LITERARY foundation of the lineage; BATCH_010 (hip-hop / music-industry memoirs · Charnas / Ross / Gucci Mane / Jay-Z) is the music/culture layer. Complementary halves of the same lineage backing. The `culture` + `lineage` domains established here are the buckets BATCH_010 will extend. May fold together or stand as the literary half · operator decision at BATCH_010 time.

---

## 7 · Deliverables (produced in the EXTRACTION + CHUNK session · NOT now)

| Deliverable | Path | Notes |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/LITERARY_CANON_BLACK_CHUNKS.jsonl` | 22-32 chunks · batch_id `LITERARY_CANON_BLACK` · 12-field canonical schema |
| Extracted source dir | `01_KNOWLEDGE_BASE/batches/literary_canon_black_extracted/` | 3 normalized `.txt` (Beloved NOT extracted · deferred) |
| Summary | `01_KNOWLEDGE_BASE/summaries/LITERARY_CANON_BLACK_SUMMARY.md` | coverage · the Beloved deferral · NEW `lineage` domain · cross-references |
| Source index | `01_KNOWLEDGE_BASE/indexes/LITERARY_CANON_BLACK_SOURCE_INDEX.md` | per-chunk concept + domain + source-novel map + Beloved-deferred note |
| Extraction log | `00_COMMAND_CENTER/batch_logs/LITERARY_CANON_BLACK_EXTRACTION_LOG.md` | sources in / extracted out / Beloved-stub flag / failures |
| Completion marker | `00_COMMAND_CENTER/batch_logs/LITERARY_CANON_BLACK_COMPLETE.md` | status · validation summary · deviations · Beloved-deferred |
| Extraction script | `scripts/extract_literary_canon_black.py` | NEEDED · stdlib zipfile+HTML-strip (2 epubs) + ebook-convert (mobi) · skip Beloved stub. No new deps. |
| Chunk writer | `scripts/write_literary_canon_black_chunks.py` | NEEDED · hand-authored thematic chunks + em-dash sweep via `chr(0x2014)` · short illustrative quotes only. Mirror `scripts/write_prompt_templates_deep_chunks.py`. |

### Schema decisions (recommended · finalized at chunk-write time)
- `batch_id`: `LITERARY_CANON_BLACK`
- `chunk_id` pattern: `LITERARY_CANON_BLACK_001` ... `_0NN`
- `source_title`: `<Novel Title> · <Author>` (e.g. `The Bluest Eye · Toni Morrison`); synthesis chunks use `Black Literary Canon · cross-author pattern`
- `author`: the novelist (`Toni Morrison`, `Zora Neale Hurston`, `Alice Walker`); synthesis chunks `SNIPED (cross-author synthesis)`
- `source_file`: `bluest_eye_morrison.txt`, `their_eyes_hurston.txt`, `color_purple_collection_walker.txt`. The Walker collection's 3 novels all cite `color_purple_collection_walker.txt` (concept-map notes the specific novel). Synthesis chunks cite the most representative file.

---

## 8 · Explicit exclusions

| Material | Disposition |
|---|---|
| Beloved (Morrison · `.pdf`) | DEFER · stub (publisher blurb + SEO spam · 698 words · no novel prose) · NOT chunked · flag for real-text re-acquisition |
| To Kill a Mockingbird (Lee) | NOT in this lane · excluded from LITERARY_CANON_BLACK (white-authored Southern lit · would dilute the Black-canon thesis) · route to a future GENERAL pass if wanted |
| Bulk/long passages of in-copyright novels | NOT reproduced · `direct_quotes` limited to short illustrative lines (a sentence or two · fair-use scale) |
| Front/back-matter, copyright pages, ad pages | Stripped at extraction · not chunked |
| Dystopian / general literary intake sources | OUT OF SCOPE · not touched (separate lanes) |

---

## 9 · What this planning session does NOT do

- No extraction. The planning peek used stdlib `zipfile` + `pdftotext` to stdout only · no extracted files written.
- No chunking. No JSONL writes.
- No master-file updates.
- No script files written.
- No BATCH_008 start.
- No dystopian/general literary intake touched.
- No source files moved/renamed/deleted (Beloved stub left in place · flagged, not deleted).
- No new dependencies.
- No commit.

---

## 10 · Recommended next operation

Authorize the extraction + chunk session per the locked 7-step SOP (steps 5-6):
1. Run `scripts/extract_literary_canon_black.py` · stdlib zipfile+HTML-strip on the 2 epub-family files + ebook-convert on the mobi into `literary_canon_black_extracted/` (skip Beloved · front/back-matter stripped).
2. Hand-author 22-32 thematic chunks (target ~28) per the section 4 map · short illustrative quotes only · introduce the `lineage` domain.
3. Run `jsonl-validation` (6 checks) + em-dash sweep + a NEW-domain note for `lineage`.
4. Write summary + source index + logs + completion marker (record the Beloved deferral prominently).
5. Stop after validation + reporting · await `master-consolidation` authorization (which will register the NEW `lineage` domain).

After this mini-batch consolidates (target 918 -> ~940-950), the next queued literary mini-batches per `STAGING_PLAN_2026-05-19_INTAKE.md` §5 are LITERARY_CANON_DYSTOPIAN and LITERARY_CANON_GENERAL, then BATCH_008 AI/tech canon. Separately, flag the Beloved re-acquisition.

---

## 11 · Open operator decisions surfaced

| # | Decision | Default recommendation |
|--:|---|---|
| 1 | Beloved stub · defer or chunk-from-blurb? | DEFER · re-acquire real text · do not chunk a marketing blurb |
| 2 | `lineage` as a NEW domain? | APPROVE (operator brief already lists it) · the 59th domain |
| 3 | TKAM in this lane? | NO · keep out · route to GENERAL if wanted |
| 4 | Depth on the 2 Walker companion novels (Temple of My Familiar, Possessing the Secret of Joy)? | Light coverage (2-3 chunks each) · The Color Purple is the marquee · companions add ancestral-memory + cultural-trauma signal |

---

## 12 · Revision log

- **rev 1 (2026-05-20 · this version):** First plan for LITERARY_CANON_BLACK. 4 files confirmed in the lane. Read-only peek revealed Beloved PDF is a 698-word stub (publisher blurb + SEO spam · NOT the novel) · DEFER. The other 3 are real full texts (Bluest Eye mobi · Their Eyes epub-in-zip · Color Purple Collection epub = 3 Walker novels). TKAM not present · excluded from this lane. Extraction: stdlib zipfile+HTML-strip (2 epubs) + ebook-convert (mobi) · no OCR · no new deps. 22-32 chunk estimate · target ~28 (Beloved deferral offset by the Walker 3-novel collection). `lineage` flagged as a NEW domain (approved by operator brief · 59th domain). Cross-references mapped to B4 aesthetic doctrine, B5 photography canon, B7 + the Lineage Doctrine, INTELLECTUAL_ARTIST_FRAME, and future BATCH_010. In-copyright brief-quote discipline specified.
