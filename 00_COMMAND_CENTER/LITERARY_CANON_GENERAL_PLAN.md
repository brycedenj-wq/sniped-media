# LITERARY_CANON_GENERAL mini-batch plan · 2026-05-21

Plan only. No extraction, no chunking, no master-file updates, no BATCH_008 start, no commit. Stops after this plan is written.

This mini-batch extracts durable general literary canon signal from the remaining staged literary classics. It is the third and final literary lane (after LITERARY_CANON_BLACK and LITERARY_CANON_DYSTOPIAN) and closes the 2026-05-19 literary intake. No NEW domain is introduced.

---

## 0 · Headline

- **8 files in the lane · 6 candidate text sources · 2 unextractable (DEFER).**
- **Pre-flight stub check (Beloved lesson applied):** 5 of the 6 candidates confirmed REAL full texts; 1 (Gibran `.lit`) is conditional on an extraction-time conversion test.
- **2 DEFERRED for format reasons (no OCR, no new deps):** Maus I (`.cbr` · a RAR of comic-book images · no text layer) and Jonathan Livingston Seagull (`.djvu` · `djvutxt` not installed · calibre cannot read djvu input).
- **No NEW domain.** This lane reuses culture, lineage, aesthetics, operator-doctrine (+ ethics where warranted). systems-thinking only if truly needed (unlikely).
- **Estimated yield:** 26-38 chunks · target ~32 (the staging plan's 30-50 assumed Maus + JLS + the Russian-author mobi were usable; with those deferred/absent the realistic range is lower).
- **Copyright discipline:** mostly in-copyright (Joyce/Ulysses now PD in many jurisdictions; Vonnegut, Nabokov, Hosseini, Gibran in-copyright; Allen PD). `direct_quotes` SHORT illustrative lines only (a sentence or two · fair-use scale). Extracted full text is INTERNAL chunk-authoring reference only.

---

## 1 · Source files confirmed on disk

`raw/02_TIER_1_CANON_BOOKS/literary_canon_general/` · 8 files.

| # | File | Author / Title | Type | Size | Pre-flight |
|--:|---|---|---|---:|---|
| 1 | `James Joyce - Ulysses (2000, Penguin Group) - libgen.li.epub` | James Joyce · *Ulysses* (1922) | EPUB · 15 html docs | 2.74 MB | REAL · 291,518 words · 1391 Stephen/Bloom/Stately markers |
| 2 | `Kurt Vonnegut - Slaughterhouse-Five - libgen.li.pdf` | Kurt Vonnegut · *Slaughterhouse-Five* (1969) | PDF · 105 pages | 1.0 MB | REAL · 49,544 words · "Billy Pilgrim" / "So it goes" / "Tralfamadore" |
| 3 | `Nabokov, Vladimir - Lolita (Vladimir Nabokov) - libgen.li.pdf` | Vladimir Nabokov · *Lolita* (1955) | PDF · v1.2 | 1.08 MB | REAL · 111,150 words · "Humbert Humbert" / opening line present |
| 4 | `Khaled Hosseini - The Kite Runner (2004, Riverhead Trade) - libgen.li.mobi` | Khaled Hosseini · *The Kite Runner* (2003) | Mobipocket (magic-confirmed title) | 707 KB | REAL (high confidence) · Hassan / Kabul markers · verify word count at extraction (30k floor) |
| 5 | `JAMES_ALLEN-AS_A_MAN_THINKETH.pdf` | James Allen · *As a Man Thinketh* (1903) | PDF · 6 pages | 89 KB | REAL · 7,584 words · the FULL short essay (6 pages = dense layout, not abridged) · opens "Mind is the Master power that moulds and makes" |
| 6 | `Kahlil Gibran - The Prophet (1973) - libgen.li.lit` | Kahlil Gibran · *The Prophet* (1923) | Microsoft Reader `.lit` | 100 KB | CONDITIONAL · `.lit` not peekable without conversion · test `ebook-convert` (calibre supports LIT input) at extraction · defer if it fails or yields a stub |
| 7 | `Maus I.cbr` | Art Spiegelman · *Maus I* (1986) | RAR archive of images (`.cbr`) | 52.9 MB | DEFER · comic-book images · NO text layer · no OCR (per rules) |
| 8 | `Richard Bach - Jonathan Livingston Seagull. (1973, Avon Books) - libgen.li.djvu` | Richard Bach · *Jonathan Livingston Seagull* (1970) | DjVu (scanned) | 2.57 MB | DEFER · `djvutxt` not installed · calibre cannot read djvu input · no new deps · no OCR |

**Absent (per staging plan):** Maus II (zero-byte/broken download · not staged) and the Russian-author mobi (`[Part 1 ] Шерман, Алекси` · uncertain provenance · held). Neither is in the lane.

---

## 2 · Source-quality / stub check

Done because the Beloved PDF in LITERARY_CANON_BLACK turned out to be a stub. Results:
- **Real full texts (5):** Ulysses, Slaughterhouse-Five, Lolita, As a Man Thinketh, The Kite Runner (mobi · markers confirm, word count to verify at extraction).
- **Conditional (1):** The Prophet `.lit` · not peekable without conversion · ebook-convert test at extraction time decides include-or-defer.
- **No stubs found** among the peekable sources (As a Man Thinketh's small page count is dense layout of the full 7.5k-word essay, NOT a stub).

---

## 3 · Difficult / unsupported formats

| File | Issue | Disposition |
|---|---|---|
| Maus I `.cbr` | RAR archive of page images · no text layer · 52.9 MB | DEFER · text extraction not possible without OCR (banned per rules). See section 5 for the optional summary-chunk decision. |
| Jonathan Livingston Seagull `.djvu` | `djvutxt` not on PATH · `ebook-convert`/calibre does not read djvu input · likely scanned | DEFER · unsupported with current tooling · no new deps · no OCR |
| The Prophet `.lit` | Microsoft Reader format · calibre (`ebook-convert`) supports LIT input but it is untested here | CONDITIONAL · test `ebook-convert <lit> <txt>` at extraction · if it produces clean text >= 3,000 words, INCLUDE; else DEFER |
| The Kite Runner `.mobi` | compressed mobi (peek only surfaced fragments) | INCLUDE · `ebook-convert` decompresses properly · verify >= 30,000 words at extraction |

---

## 4 · Lolita handling note

Lolita is a literary masterwork narrated by a predatory unreliable narrator. Chunks will treat it strictly at the CRAFT / MORAL level: the unreliable narrator, the seduction of beautiful style, the reader's manufactured complicity, and aesthetics-vs-morality. No graphic or sympathetic treatment of the subject matter · the durable signal is exactly Nabokov's point that gorgeous prose can launder a monstrous narrator, which is itself a warning about style divorced from ethics (a useful counterpoint to the SNIPED craft lane).

---

## 5 · Curated subset · include vs defer

### INCLUDE (chunk these)
1. Ulysses (Joyce) · epub · stdlib zipfile+HTML-strip
2. Slaughterhouse-Five (Vonnegut) · pdf · pdftotext -layout
3. Lolita (Nabokov) · pdf · pdftotext -layout (craft/moral framing per section 4)
4. The Kite Runner (Hosseini) · mobi · ebook-convert (30k floor)
5. As a Man Thinketh (Allen) · pdf · pdftotext -layout
6. The Prophet (Gibran) · `.lit` · ebook-convert · **CONDITIONAL** (include only if the conversion yields clean full text)

### DEFER (do not chunk in this batch)
- **Maus I** (`.cbr`) · no text layer · no OCR. **Operator decision surfaced:** (a · default) DEFER entirely and flag for a future OCR/summary pass; or (b) author 1 metadata/thematic chunk from general knowledge (inherited/second-generation trauma · the mouse-vs-cat allegory · comics as serious witness) explicitly tagged metadata-only with NO source quotes. Default recommendation: DEFER (keeps the batch text-grounded; Maus deserves real treatment, not a thin gloss).
- **Jonathan Livingston Seagull** (`.djvu`) · unsupported format · DEFER · flag for re-acquisition in a text format (epub/pdf) or a future djvu/OCR pass.

---

## 6 · Estimated chunk yield · 26-38 chunks · target ~32

Thematic chunks (by motif, not chapter), short illustrative quotes. Provisional map:

| Work (author) | Est. chunks | Candidate themes |
|---|---:|---|
| Ulysses (Joyce) | 5-7 | the ordinary day made epic · stream of consciousness · language as the hero · Bloom's everyday humanity & empathy · Dublin as a fully-rendered world · Molly's closing "yes" · the novel as total attention |
| Slaughterhouse-Five (Vonnegut) | 4-6 | anti-war witness · "So it goes" & the fatalism of grief · Dresden & the unspeakable · Tralfamadorian time / non-linearity · absurdity as survival · trauma (PTSD) rendered structurally |
| Lolita (Nabokov) | 4-6 | the unreliable narrator · the seduction of style · the reader's manufactured complicity · beauty vs morality · language as both art and concealment (craft/moral framing) |
| The Kite Runner (Hosseini) | 4-5 | guilt & the long arc of atonement · "For you, a thousand times over" · betrayal & loyalty · exile & displacement (Afghanistan to America) · fathers & sons & inheritance |
| As a Man Thinketh (Allen) | 3-4 | thought shapes character & circumstance · the mind as a gardener · self-mastery · the literary root of mindset-as-software (careful · no shallow business gloss) |
| The Prophet (Gibran · conditional) | 3-4 | work as love made visible · on giving · on children (they are not yours) · poetic-parable form |
| Cross-author synthesis | 2-3 | literature as attention training · moral seriousness & craft across the canon · operator lessons from literature WITHOUT forcing shallow takeaways |

If Gibran defers, drop ~3-4 (range floor ~26). With all six, ~32-36.

---

## 7 · Approved domains / tags (NO NEW domain)

| Domain | Status | Use |
|---|---|---|
| culture | EXISTS (21) | the rendered world, empathy, displacement, moral seriousness |
| lineage | EXISTS (8) | inherited story / memory / identity (Kite Runner fathers-and-sons & exile; Gibran on children) |
| aesthetics | EXISTS (48) | form / voice / craft (Ulysses stream-of-consciousness; Nabokov's style; Vonnegut's structure) · the central domain for this lane |
| operator-doctrine | EXISTS (45) | only where directly tied to discipline / attention / seriousness (As a Man Thinketh self-mastery; literature-as-attention-training; craft-vs-shallow) |
| ethics | EXISTS (4) | only where warranted (Lolita's moral complicity; Slaughterhouse anti-war witness) |
| systems-thinking | EXISTS (8) | only if truly needed · likely 0 |

**No NEW domain introduced** (unlike the prior two literary lanes which added `lineage` and `systems-thinking`). All six candidate domains pre-exist.

**Recommended tag bank:** `literary-canon`, `general-literary-canon`, `attention`, `ambition`, `exile`, `memory`, `alienation`, `moral-seriousness`, `craft`, `voice`, `stream-of-consciousness`, `myth`, `fable`, `parable`, `identity-formation`, `family`, `inheritance`, `trauma`, `survival`, `absurdity`, `anti-war`, `tenderness`, `human-scale-meaning`, `artistic-discipline`, `unreliable-narrator`, `style-vs-ethics`, `joyce`, `vonnegut`, `nabokov`, `hosseini`, `allen`, `gibran`.

**Aging note:** none · timeless primary texts (1903-2003). No `ai-tooling-aging-risk`. Capture publication years.

---

## 8 · How this mini-batch connects to the rest of the corpus

### LITERARY_CANON_BLACK
- Completes the literary cultural lane that LCB opened. Shared `culture` + `lineage` domains (Kite Runner's fathers-and-sons & exile pair with the Black canon's inherited-story chunks). Both lanes embody artistic seriousness as the refusal of shallow content.

### LITERARY_CANON_DYSTOPIAN
- Counterpoint: Lolita's "beautiful style laundering a monstrous narrator" (style-vs-ethics) pairs with the dystopian warning that persuasion can bypass morality (Huxley's arts of selling). Vonnegut's anti-war witness sits beside the dystopian systems-warnings as the human-scale view of catastrophe.

### BATCH_004 aesthetic doctrine
- The strongest tie: Ulysses, Lolita, and Vonnegut are masterclasses in form / voice / craft. They back the SNIPED restraint + seriousness lane and the conviction that HOW a thing is made is the argument. Cross-tag `aesthetics`.

### BATCH_005 photography canon
- Joyce's total attention to an ordinary Dublin day ↔ the photographic discipline of seeing the everyday fully (the dignifying gaze). Literature-as-attention-training is the same muscle as the photographer's eye.

### INTELLECTUAL_ARTIST_FRAME
- The general canon extends the artistic-seriousness frame (MJ descriptive · POC prescriptive · the Black canon · now the broad canon). As a Man Thinketh is the literary root of the mindset-as-software / self-mastery thread (POC chunk 009).

### Future BATCH_008 AI / tech canon
- The humanistic counterweight read alongside the AI-builder canon: literature trains the attention, empathy, and moral seriousness that the build-canon does not. Cross-reference, do not merge.

---

## 9 · Deliverables (produced in the EXTRACTION + CHUNK session · NOT now)

| Deliverable | Path | Notes |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/LITERARY_CANON_GENERAL_CHUNKS.jsonl` | 26-38 chunks · batch_id `LITERARY_CANON_GENERAL` · 12-field schema |
| Extracted source dir | `01_KNOWLEDGE_BASE/batches/literary_canon_general_extracted/` | normalized `.txt` per INCLUDED source (5-6 files · Maus + JLS not extracted) |
| Summary | `01_KNOWLEDGE_BASE/summaries/LITERARY_CANON_GENERAL_SUMMARY.md` | coverage · Maus/JLS deferral · Gibran conditional outcome · cross-references |
| Source index | `01_KNOWLEDGE_BASE/indexes/LITERARY_CANON_GENERAL_SOURCE_INDEX.md` | per-chunk concept + domain + source map + deferral note |
| Extraction log | `00_COMMAND_CENTER/batch_logs/LITERARY_CANON_GENERAL_EXTRACTION_LOG.md` | sources in / extracted out / deferred / stub-check / Gibran .lit result / failures |
| Completion marker | `00_COMMAND_CENTER/batch_logs/LITERARY_CANON_GENERAL_COMPLETE.md` | status · validation summary · deviations |
| Extraction script | `scripts/extract_literary_canon_general.py` | NEEDED · stdlib zipfile (epub) + pdftotext (pdfs) + ebook-convert (mobi + .lit) · skip Maus .cbr + JLS .djvu. No new deps. |
| Chunk writer | `scripts/write_literary_canon_general_chunks.py` | NEEDED · hand-authored thematic chunks + em-dash sweep via `chr(0x2014)` · short illustrative quotes only. Mirror `scripts/write_literary_canon_dystopian_chunks.py`. |

### Schema decisions (recommended · finalized at chunk-write time)
- `batch_id`: `LITERARY_CANON_GENERAL`
- `chunk_id` pattern: `LITERARY_CANON_GENERAL_001` ... `_0NN`
- `source_title`: `<Title> · <Author>`; synthesis chunks `General Literary Canon · cross-author synthesis`
- `author`: the author; synthesis `SNIPED (cross-author synthesis)`
- `source_file`: normalized lowercase-snake-case `.txt` per included source (`ulysses_joyce.txt`, `slaughterhouse_five_vonnegut.txt`, `lolita_nabokov.txt`, `the_kite_runner_hosseini.txt`, `as_a_man_thinketh_allen.txt`, `the_prophet_gibran.txt` if included)

---

## 10 · Explicit exclusions

| Material | Disposition |
|---|---|
| Maus I (`.cbr`) | DEFER · images · no OCR · flag for future OCR/summary pass (operator decision in section 5) |
| Jonathan Livingston Seagull (`.djvu`) | DEFER · unsupported format · no djvutxt · no new deps · flag for re-acquisition in a text format |
| Maus II + Russian-author mobi | NOT in lane (absent · broken/held per staging plan) |
| Long passages of in-copyright text | NOT reproduced · short illustrative quotes only |
| Lolita subject matter | Treated at craft/moral level only (section 4) · no graphic content |
| Front/back-matter, copyright pages | Stripped at extraction |
| Black + dystopian literary lanes | Already chunked (separate mini-batches) · not touched |

---

## 11 · What this planning session does NOT do

- No extraction (planning peek used stdlib zipfile / pdftotext / strings to stdout only · no files written).
- No chunking. No JSONL writes. No master-file updates. No script files written.
- No BATCH_008 start. No source files moved/renamed/deleted. No new dependencies. No OCR. No commit.

---

## 12 · Recommended next operation

Authorize the extraction + chunk session per the locked 7-step SOP (steps 5-6):
1. Run `scripts/extract_literary_canon_general.py` · stdlib zipfile (Ulysses) + pdftotext (Slaughterhouse-Five, Lolita, As a Man Thinketh) + ebook-convert (Kite Runner mobi + Gibran .lit) into `literary_canon_general_extracted/`. Skip Maus .cbr + JLS .djvu. Verify Kite Runner >= 30k words and Gibran .lit yields clean text (else defer Gibran). Front/back-matter stripped.
2. Hand-author 26-38 thematic chunks (target ~32) per the section 6 map · short illustrative quotes only · no NEW domain.
3. Run `jsonl-validation` (6 checks) + em-dash sweep.
4. Write summary + source index + logs + completion marker (record the Maus/JLS deferral + Gibran outcome).
5. Stop after validation + reporting · await `master-consolidation` authorization.

After this mini-batch consolidates (target 963 -> ~989-1001), the 2026-05-19 literary lane is COMPLETE (BLACK + DYSTOPIAN + GENERAL). The next major work is **BATCH_008 AI/tech canon** (still reserved). Two follow-ups stay flagged: Beloved re-acquisition (LCB) and Maus I / Jonathan Livingston Seagull re-acquisition or OCR (this lane).

---

## 13 · Open operator decisions surfaced

| # | Decision | Default recommendation |
|--:|---|---|
| 1 | Maus I `.cbr` · defer entirely or author 1 metadata-only chunk? | DEFER entirely · flag for future OCR/summary · do not gloss |
| 2 | Jonathan Livingston Seagull `.djvu` · defer or attempt conversion? | DEFER · unsupported with current tooling · re-acquire in a text format |
| 3 | Gibran The Prophet `.lit` · include if ebook-convert succeeds? | INCLUDE if conversion yields clean full text · else defer |
| 4 | Lolita inclusion + framing? | INCLUDE · craft/moral level only (section 4) · no graphic content |

---

## 14 · Revision log

- **rev 1 (2026-05-21 · this version):** First plan for LITERARY_CANON_GENERAL. 8 files in the lane. Pre-flight confirmed 5 real full texts (Ulysses 291k, Lolita 111k, Slaughterhouse-Five 49k, As a Man Thinketh 7.5k full essay, Kite Runner markers) + 1 conditional (Gibran .lit). 2 DEFERRED for format: Maus I (.cbr images · no OCR) and Jonathan Livingston Seagull (.djvu · no djvutxt · calibre can't read it). Maus II + Russian mobi absent. Extraction: stdlib zipfile + pdftotext + ebook-convert · no OCR · no new deps. 26-38 chunk estimate · target ~32 (lower than the staging plan's 30-50 because Maus/JLS deferred). NO NEW domain · reuses culture/lineage/aesthetics/operator-doctrine (+ ethics). Lolita handled at craft/moral level only. Cross-references mapped to LCB, LCD, B4, B5, INTELLECTUAL_ARTIST_FRAME, future BATCH_008. In-copyright brief-quote discipline specified.
