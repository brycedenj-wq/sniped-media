# RECOVERY_REACQUISITION pass · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation. This pass inspects and classifies the held recovery candidates and gives BJ a redownload list. Nothing is currently chunkable.

## 0. Current corpus state (verified)

- **Head commit:** `2242909 save session after ONWARD_TURNAROUND consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,403 · **numbered batches:** 10 · **mini-batches:** 18 · **official domains:** 62 (keys 75).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted.
- **Identity optionality guardrails:** ACTIVE.

## 1. Tooling reality (governs format guidance)

- **Supported extractors on PATH:** `pdftotext` (pdf), `ebook-convert` / calibre (epub, mobi, azw3), `pandoc` (docx). stdlib `zipfile` handles epub internals.
- **NOT on PATH (and banned to install):** `djvutxt`, `ddjvu`, `djvused` (djvu), `unrar` (cbr/cbz). No OCR engine (`ocrmypdf`/`tesseract`).
- **Consequence:** `.djvu`, `.cbr`, `.cbz`, and image-only/scanned PDFs are **unsupported** in this pipeline. They must be re-acquired in a supported text format. No OCR, no new dependencies (locked rule).

## 2. Recovery candidate table (all 15)

| # | Candidate (author) | Status | Path in raw/ (if present) | Problem type | Priority | Preferred format | Suggested future lane |
|---|---|---|---|---|---|---|---|
| 1 | Confessions of an Advertising Man (Ogilvy) | found · unusable | `raw/02_TIER_1_CANON_BOOKS/advertising/David Ogilvy_ Alan Parker - Confessions of an Advertising Man (2004, Southbank Publishing) - libgen.li.pdf` | scanned / image-only PDF (107 pp · pdftotext 0 words) | HIGH | epub | advertising recovery (BATCH_009 family) |
| 2 | Hit Men (Dannen) | found · unusable | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/ Fredric Dannen - Hit men... - libgen.li.pdf` | scanned / image-only PDF (216 pp · 0 words) | HIGH | epub | media-business recovery (MEDIA_BUSINESS) |
| 3 | The Mailroom (Rensin) | found · unusable | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/David Rensin - The Mailroom... - libgen.li.djvu` | unsupported format (djvu · no djvutxt) | HIGH | epub | media-business recovery (MEDIA_BUSINESS) |
| 4 | Predictably Irrational (Ariely) | found · unusable | `raw/03_TIER_2_CANON_BOOKS/persuasion_psych/Dan Ariely - Predictably Irrational... - libgen.li.djvu` | unsupported format (djvu) | HIGH | epub | persuasion / decision recovery (BATCH_009 family) |
| 5 | The Adweek Copywriting Handbook (Sugarman) | missing | (absent from raw/) | needs manual re-acquisition | HIGH | epub | advertising recovery (BATCH_009 family) |
| 6 | Tested Advertising Methods (Caples) | missing | (absent from raw/) | needs manual re-acquisition | HIGH | epub | advertising recovery (BATCH_009 family) |
| 7 | The Boron Letters (Halbert) | missing | (absent from raw/) | needs manual re-acquisition | MEDIUM | epub | advertising recovery (BATCH_009 family) |
| 8 | Grace: A Memoir (Coddington) | found · unusable | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Coddington, Grace - Grace_ A Memoir... - libgen.li.epub` | 0-byte stub / empty file | MEDIUM | epub | founder-media / fashion-luxury (BIOGRAPHY_FOUNDER_MEDIA-adjacent) |
| 9 | Total Recall (Schwarzenegger/Petre) | found · unusable | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Petre, Peter_Schwarzenegger... - libgen.li.epub` | 0-byte stub / empty file | LOW | epub | founder/biography (optional) |
| 10 | Margin of Safety (Klarman) | found · unusable | `raw/03_TIER_2_CANON_BOOKS/investing_finance/Seth A. Klarman - Margin of Safety... - libgen.li.pdf` | scanned / image-only PDF (68 pp · 0 words) | MEDIUM | clean text PDF or epub | deep-finance expansion (capital lane) |
| 11 | Beloved (Morrison) | found · unusable | `raw/02_TIER_1_CANON_BOOKS/literary_canon_black/[Beloved Trilogy 1...] Beloved{Toni Morrison}(1987)... libgen.li.pdf` | stub / excerpt (4 pp · 696 words · not the full novel) | LOW | epub | literary recovery (LITERARY_CANON_BLACK-adjacent) |
| 12 | Maus I (Spiegelman) | found · unusable | `raw/02_TIER_1_CANON_BOOKS/literary_canon_general/Maus I.cbr` | unsupported format (cbr · image comic · 52 MB) | SKIP | n/a (image-only) | skip |
| 13 | Maus II (Spiegelman) | missing | (absent from raw/) | absent (graphic novel · image-only) | SKIP | n/a (image-only) | skip |
| 14 | Jonathan Livingston Seagull (Bach) | found · unusable | `raw/02_TIER_1_CANON_BOOKS/literary_canon_general/Richard Bach - Jonathan Livingston Seagull... - libgen.li.djvu` | unsupported format (djvu) | LOW | epub | literary recovery (optional · lane complete) |
| 15 | Russian-author mobi (Sherman / `Шерман, Алекси`) | missing | (absent / unidentified) | absent · title and relevance unconfirmed | SKIP | mobi or epub | hold until BJ identifies it |

### Read-only file checks performed (no OCR · no mutation)

- **PDFs probed with `pdftotext` to /tmp (temp deleted):** Beloved (4 pp · 696 words · text layer present but it is only a 4-page excerpt, NOT the ~324-page novel · STUB), Confessions (107 pp · 0 words · scanned), Margin of Safety (68 pp · 0 words · scanned), Hit Men (216 pp · 0 words · scanned).
- **EPUBs:** Grace and Total Recall are both **0 bytes** (empty · corrupt download).
- **DjVu:** The Mailroom, Predictably Irrational, Jonathan Livingston Seagull · valid djvu but no djvu tooling on PATH (unsupported · ebook-convert does not accept djvu input).
- **CBR:** Maus I is a 52 MB RAR of image scans (comic) · no text · no `unrar` on PATH and OCR is banned.
- All originals untouched (read-only checks only).

## 3. Status tally

- **Candidates inspected:** 15
- **Found in raw/:** 11 · **Missing (absent):** 4 (Sugarman, Caples, Halbert, Maus II, Russian-author mobi · note: 5 absent total · Maus II is both a graphic novel and absent)
- **By problem type:**
  - Scanned / image-only PDF (would need OCR): 3 (Confessions, Margin of Safety, Hit Men)
  - Unsupported format djvu/cbr: 4 (The Mailroom, Predictably Irrational, Jonathan Livingston Seagull · djvu; Maus I · cbr)
  - 0-byte stub / empty: 2 (Grace, Total Recall)
  - Stub / partial excerpt: 1 (Beloved · 4-page PDF)
  - Missing / absent: 5 (Sugarman, Caples, Halbert, Maus II, Russian-author mobi)
- **Currently chunkable:** 0. Every candidate is broken, scanned, unsupported, empty, or missing. No direct recovery mini-batch can run today.

## 4. Top 6 redownload list for BJ (value x tractability)

Get these in **epub** (or mobi/azw3) where possible:

1. **Confessions of an Advertising Man** (Ogilvy) · advertising canon · directly extends the BATCH_009 advertising/copywriting lane.
2. **Hit Men** (Dannen) · music-industry power/money · extends MEDIA_BUSINESS + the BATCH_010 music lineage.
3. **The Mailroom** (Rensin) · Hollywood talent-system oral history · extends MEDIA_BUSINESS.
4. **Predictably Irrational** (Ariely) · behavioral economics · extends BATCH_009 persuasion + status psychology.
5. **The Adweek Copywriting Handbook** (Sugarman) · direct-response copywriting canon · BATCH_009.
6. **Tested Advertising Methods** (Caples) · direct-response copywriting canon · BATCH_009.

Just below the cut (get if convenient): **The Boron Letters** (Halbert · completes the direct-response trio) and **Grace: A Memoir** (Coddington · fashion/taste-making · re-download the 0-byte epub).

## 5. "Do not stress if unavailable" list

- **Maus I + Maus II** · image-only graphic novels · not text-corpus material · skip (would need OCR of comic panels, which is both banned and low-value).
- **Jonathan Livingston Seagull** · short fable · the literary lane is already complete · marginal value-add.
- **Russian-author mobi** (`Шерман, Алекси`) · unidentified · skip until BJ confirms what the title is and why it belongs.
- **Margin of Safety** (Klarman) · famously out-of-print and expensive · clean text editions barely circulate (scanned copies are the norm) · do not burn effort chasing it · the `capital` lane already stands without it.
- **Total Recall** (Schwarzenegger) · celebrity memoir · marginal corpus value · only re-download if trivially easy.

## 6. Lane routing for recovered sources (when usable)

- **Advertising recovery** (BATCH_009 family): Confessions + Sugarman + Caples + Halbert. A coherent direct-response / advertising-canon recovery mini-batch once 2+ are usable. NO new domain (copywriting / meta-advertising / brand-psychology already exist).
- **Media-business recovery** (MEDIA_BUSINESS): Hit Men + The Mailroom. A music/Hollywood recovery expansion. NO new domain (`media-business` exists).
- **Persuasion / decision recovery** (BATCH_009 family): Predictably Irrational. Folds into persuasion-psych or a future decision/judgment lane. NO new domain.
- **Deep-finance expansion** (capital lane): Margin of Safety, if a clean copy ever surfaces. NO new domain (`capital` exists).
- **Literary recovery** (LITERARY_CANON_BLACK-adjacent): Beloved, if re-acquired clean. NO new domain (`lineage` exists).
- **Founder / fashion**: Grace → BIOGRAPHY_FOUNDER_MEDIA / fashion-luxury; Total Recall → optional founder lane. NO new domain.
- **Held until later / skipped**: Maus I/II, Jonathan Livingston Seagull, Russian-author mobi.

No source becomes a **direct recovery mini-batch now** (nothing is usable). All routing is conditional on BJ re-acquiring a supported, text-bearing file.

## 7. Rules for when BJ redownloads new files

1. **Drop into the matching `raw/` subfolder** (advertising/, memoirs_biographies/, persuasion_psych/, investing_finance/, literary_canon_black/ or _general/). Do not invent new folders.
2. **Format preference:** epub > mobi > azw3 > clean-text PDF. **AVOID** djvu, cbr, cbz, and image-only/scanned PDF (unsupported · no djvutxt/unrar/OCR on PATH · new deps are banned).
3. **Verify each new file before planning** (read-only): non-zero size; file type matches extension; for PDF, `pdftotext` yields a real word count (text layer present, not a scan); for epub/mobi, ebook-convert opens it.
4. **Then plan per the locked 7-step SOP.** Two or more thematically-coherent usable sources → a recovery mini-batch. A single strong source can be a single-source mini-batch (the ONWARD_TURNAROUND precedent).
5. **Route into existing lanes; NO new domain** unless the operator explicitly approves one.
6. **Never** OCR, install dependencies, or mutate the raw/ originals. Recovery does not change those locked rules.
7. **CURRENT_OPERATOR_REALITY_BRIEF stays the anchor** and identity-optionality guardrails stay active for any recovered source that touches founder/brand/operator material.

## 8. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files.
- Did NOT modify any `raw/` file (read-only `file`, `wc -c`, `pdfinfo`, and `pdftotext`-to-/tmp probes only · temp deleted).
- Did NOT OCR and did NOT install anything.
- No next lane started · corpus remains 1,403 chunks · 10 numbered batches + 18 mini-batches · 62 domains.
- Wrote only this plan file. Not committed (operator will review first).
