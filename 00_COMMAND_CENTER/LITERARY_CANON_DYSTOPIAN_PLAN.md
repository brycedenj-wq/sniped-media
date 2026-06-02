# LITERARY_CANON_DYSTOPIAN mini-batch plan · 2026-05-20

Plan only. No extraction, no chunking, no master-file updates, no BATCH_008 start, no commit. Stops after this plan is written.

This mini-batch extracts durable dystopian / systems-warning signal from the dystopian canon staged in the 2026-05-19 intake. It is the second literary lane (after LITERARY_CANON_BLACK) and the cautionary counterweight to the corpus's AI / automation / operator-build layers: the warnings an operator building AI and automation systems should hold while building them.

---

## 0 · Headline

- **3 files in the lane · all 3 confirmed REAL full texts (no stubs).** The 2 study guides are NOT present (skipped per staging-plan default · see section 4).
- **Pre-flight stub check PASSED on all 3** (done because the Beloved PDF in the prior lane turned out to be a stub). Animal Farm 30,156 words + 393 character markers; Brave New World Revisited 93 pages / 34,610 words with a genuine 1958 copyright page; The Handmaid's Tale carries Gilead / Offred / Commander / "Republic of Gilead" markers.
- **NOTE · file #3 is *Brave New World Revisited* (Huxley's 1958 NONFICTION essays), not the novel Brave New World.** This is actually the single most on-theme source for the operator-warning brief (propaganda, conditioning, comfort-as-control, the future of freedom).
- **Extraction:** stdlib `zipfile` + HTML-strip (Animal Farm epub) · `ebook-convert` (Handmaid's Tale mobi) · `pdftotext -layout` (BNW Revisited pdf). No OCR. No new dependencies.
- **Estimated yield:** 12-19 chunks · target ~16.
- **Domains:** culture (existing), `systems-thinking` (**NEW · operator-approved by brief · the 60th domain · adjacent to the existing `systems` domain · see section 6**), operator-doctrine (existing), ethics (existing · as needed), strategy (existing · only if needed).
- **Copyright discipline:** in-copyright texts (Orwell 1945, Atwood 1985, Huxley 1958) · `direct_quotes` are SHORT illustrative lines only (a sentence or two · fair-use scale). Extracted full text is INTERNAL chunk-authoring reference only.

---

## 1 · Source files confirmed on disk

`raw/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/` · 3 files.

| # | File | Author / Title | Type | Size | Stub check |
|--:|---|---|---|---:|---|
| 1 | `[Animal Farm _1] Orwell, George - Animal Farm (1945, Secker & Warburg) - libgen.li.epub` | George Orwell · *Animal Farm* (1945) | EPUB · 13 html docs | 135 KB | REAL · 30,156 words · 393 Napoleon/Boxer/Snowball markers |
| 2 | `[The Handmaid's Tale 1 ] Atwood, Margaret - The Handmaid's Tale (2006_2017, Everyman's Library_Anchor Books) - libgen.li.mobi` | Margaret Atwood · *The Handmaid's Tale* (1985) | Mobipocket | 425 KB | REAL (high confidence) · Gilead / Offred / Commander / Republic of Gilead markers present · confirm word count at extraction (ebook-convert) · sanity floor 30k words |
| 3 | `Aldous Huxley - Brave New World Revisited (2001) - libgen.li.pdf` | Aldous Huxley · *Brave New World Revisited* (1958 nonfiction essays · RosettaBooks 2000 e-edition) | PDF · 93 pages | 407 KB | REAL · 34,610 words · genuine copyright page (Copyright 1958 Aldous Huxley) |

Staged in commit `215ffce`. None extracted or chunked.

### Stub pre-flight (per the Beloved lesson)

A read-only peek (stdlib zipfile for the epub · pdftotext for the pdf · `strings` for the mobi) was run on all 3. None is a publisher-blurb / SEO-spam stub. Animal Farm and BNW Revisited yield clean full prose; The Handmaid's Tale mobi is PALMDOC-compressed (so `strings` only surfaced fragments) but the distinctive Gilead/Offred markers confirm it is the real novel · its word count will be verified at extraction with a 30k-word sanity floor before any chunking.

---

## 2 · Per-file extraction method

| Source | Method | Rationale |
|---|---|---|
| Animal Farm (`.epub`) | stdlib `zipfile` + HTML-strip (spine-ordered) | Proven on the LITERARY_CANON_BLACK epubs · no new deps · clean prose. |
| The Handmaid's Tale (`.mobi`) | `ebook-convert <mobi> <tmp.txt>` → read → remove tmp | Calibre decompresses the PALMDOC mobi properly (strings cannot). On PATH. |
| Brave New World Revisited (`.pdf`) | `pdftotext -layout` | Strong text layer confirmed (93pp · 34,610 words) · no OCR needed. |

Output: one normalized `.txt` per source in `01_KNOWLEDGE_BASE/batches/literary_canon_dystopian_extracted/` (`animal_farm_orwell.txt`, `handmaids_tale_atwood.txt`, `brave_new_world_revisited_huxley.txt`). Strip front/back-matter, copyright pages, and the RosettaBooks eForeword as noise. **No OCR. No new dependencies.** Sanity floor: each extracted file >= 25,000 words (Animal Farm is a short novella · ~30k); halt + surface if any comes back tiny.

---

## 3 · Estimated chunk yield · 12-19 chunks · target ~16

Thematic chunks (chunk by motif/warning, not per chapter), each with short illustrative quotes.

### Animal Farm (Orwell · 4-6 chunks)

| Theme | Domain |
|---|---|
| The revolution betrayed · the pigs become the men | systems-thinking |
| Propaganda + the rewriting of the commandments ("all animals are equal, but some are more equal than others") | systems-thinking |
| Squealer · the spin apparatus that makes the population doubt its own memory | culture |
| Boxer · the exploited loyalty of the believing worker · "I will work harder" | culture |
| Fear + the dogs · violence as the enforcement behind the propaganda | systems-thinking |

### The Handmaid's Tale (Atwood · 4-6 chunks)

| Theme | Domain |
|---|---|
| Theocratic control of bodies · the system that reduces people to function | systems-thinking |
| Language control · renaming (Offred / Ofglen) + banned reading + slogans | culture |
| Surveillance + informants · the Eyes · everyone polices everyone | systems-thinking |
| Gradual normalization · "nothing changes instantaneously" · how a free society slides | operator-doctrine |
| The Aunts · co-opted enforcers · the system runs on the complicity of the controlled | ethics |
| Private resistance + memory · "nolite te bastardes carborundorum" · dignity under pressure | culture |

### Brave New World Revisited (Huxley · 5-7 chunks · the operator-warning core)

| Theme | Domain |
|---|---|
| Over-organization · the system that subordinates the person to efficiency | systems-thinking |
| Propaganda in a democratic society · manufacturing consent vs informing | systems-thinking |
| The arts of selling · persuasion that bypasses reason | culture |
| Chemical / distraction persuasion (the soma principle) · comfort + pleasure as control | operator-doctrine |
| Brainwashing + conditioning · engineering belief | ethics |
| Education for freedom · the antidote · teaching people to resist manipulation | operator-doctrine |
| "A person may be perfectly happy and yet enslaved" · comfort is not freedom | operator-doctrine |

### Cross-text synthesis (~1-2 chunks)

| Chunk | Domain |
|---|---|
| The dystopian warnings as the operator's guardrail · what NOT to build when building AI / automation systems | operator-doctrine |
| Two faces of control · Orwell's boot/fear vs Huxley's soma/comfort (Postman's distinction) · which one AI tends toward | systems-thinking |

That is ~15-17 mapped. Range 12-19, target ~16.

---

## 4 · Study-guide decision

**The 2 study guides remain SKIPPED · they are NOT in the lane.** Per `STAGING_PLAN_2026-05-19_INTAKE.md` §2.8, the default was "stage the 3 strict primary texts + skip the 2 secondary study guides" (1984 SparkNotes · Fahrenheit 451 Bloom's Critical Interpretations). The lane contains exactly the 3 primary texts and neither study guide · confirming the default was applied at staging.

**Recommendation:** keep them skipped. They are secondary texts about works NOT in this intake (the SparkNotes is for 1984, the Bloom's is for Fahrenheit 451 · neither primary novel was staged), so they would be weak, orphaned chunks. Do NOT re-stage unless the operator specifically wants them · and even then, route them to a study-guide handling, not the primary-canon lane.

---

## 5 · Approved domains / tags

| Domain | Status | Use |
|---|---|---|
| culture | EXISTS (18) | propaganda, language control, the arts of selling, complicity, dignity under pressure |
| `systems-thinking` | **NEW · operator-approved by brief · 60th domain** | over-organization, surveillance, institutional design, the control mechanism itself · see note below |
| operator-doctrine | EXISTS (41) | only where directly tied to SNIPED operating identity (the guardrail · comfort-is-not-freedom · education-for-freedom) |
| ethics | EXISTS (2) | conditioning / brainwashing / complicity-of-enforcers · the moral dimension · grows this thin domain |
| strategy | EXISTS (97) | only if a chunk frames a warning as a positioning stance · likely 0 |

**NEW-domain flag (`systems-thinking`):** the operator's brief lists `systems-thinking` as an approved domain. It does NOT yet exist · but an adjacent `systems` domain (6 chunks) already does. Two clean options:
- **(A · recommended) introduce `systems-thinking` as the NEW 60th domain** · it is the operator's named choice and is more precise for the dystopian systems-warning angle (institutional design, control mechanisms) than the broader, older `systems` bucket.
- (B) reuse the existing `systems` domain to avoid a near-duplicate.
Surfacing per the AGENTS.md "surface NEW domains" rule · default to (A) since the brief names it, but flag for operator confirmation at chunk-write time (the consolidation registers whichever is chosen).

**Recommended tag bank:** `dystopian-canon`, `systems-warning`, `propaganda`, `surveillance`, `language-control`, `social-conditioning`, `state-power`, `corporate-power`, `fear-as-governance`, `comfort-as-control`, `attention-discipline`, `truth-decay`, `dignity-under-pressure`, `institutional-design`, `over-organization`, `manufacturing-consent`, `the-arts-of-selling`, `soma-principle`, `education-for-freedom`, `complicity`, `normalization`, `orwell-vs-huxley`, `operator-guardrail`, `animal-farm`, `handmaids-tale`, `brave-new-world-revisited`.

**Aging note:** none · timeless primary texts (1945 / 1958 / 1985). No `ai-tooling-aging-risk`. Capture publication years in chunks.

---

## 6 · How this mini-batch connects to the rest of the corpus

### BATCH_006 operator skill layer
- The cautionary counterweight to the AI/automation skill layer. B6 teaches how to BUILD agentic systems; this mini-batch is the warning about what those systems can become (surveillance, conditioning, attention capture). Operator power + ethical restraint as a pair.

### BATCH_007 operator doctrine
- The dystopian texts sharpen the SNIPED operating ethic: fear-as-governance and comfort-as-control are the anti-patterns to the SNIPED hospitality + dignity stance (B3 Guidara · B7 doctrine). "Education for freedom" (Huxley) pairs with the operator's refusal to manipulate. Institutional-design warnings inform how SNIPED designs its own systems and client deliverables.

### N8N_AUTOMATION_SYSTEMS
- The most direct tie: these are the WARNINGS for the exact systems N8N builds. Surveillance + data tables (Airtable-as-memory · N8N 014), AI voice agents + attention capture (N8N 001-002), and automated persuasion are precisely Huxley's and Orwell's subjects. The N8N structured-output guardrail + human-approval-gate (N8N 012/013) is the practical answer to the dystopian warning · the operator builds with the brakes on.

### PROMPT_TEMPLATES_DEEP
- Language control (the rewritten commandments in Animal Farm · the renaming and banned reading in Handmaid's Tale) is the dark mirror of prompt-craft as language shaping (PTD). The ethical dimension: controlling language controls thought · the operator who shapes prompts and copy holds that power and must hold it responsibly.

### Future BATCH_008 AI / tech canon (NOT started)
- The dystopian canon is the ETHICAL / cautionary counterweight to read the AI-builder canon against. Huxley's propaganda + conditioning + chemical-persuasion warnings apply almost directly to AI recommendation, persuasion, and engagement-optimization systems. BATCH_008 (how to build) should be read with this lane (what to fear) in view · cross-reference at BATCH_008 consolidation.

---

## 7 · Deliverables (produced in the EXTRACTION + CHUNK session · NOT now)

| Deliverable | Path | Notes |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/LITERARY_CANON_DYSTOPIAN_CHUNKS.jsonl` | 12-19 chunks · batch_id `LITERARY_CANON_DYSTOPIAN` · 12-field canonical schema |
| Extracted source dir | `01_KNOWLEDGE_BASE/batches/literary_canon_dystopian_extracted/` | 3 normalized `.txt` |
| Summary | `01_KNOWLEDGE_BASE/summaries/LITERARY_CANON_DYSTOPIAN_SUMMARY.md` | coverage · the BNW-Revisited-not-novel note · NEW domain decision · cross-references |
| Source index | `01_KNOWLEDGE_BASE/indexes/LITERARY_CANON_DYSTOPIAN_SOURCE_INDEX.md` | per-chunk concept + domain + source map |
| Extraction log | `00_COMMAND_CENTER/batch_logs/LITERARY_CANON_DYSTOPIAN_EXTRACTION_LOG.md` | sources in / extracted out / stub-check results / failures |
| Completion marker | `00_COMMAND_CENTER/batch_logs/LITERARY_CANON_DYSTOPIAN_COMPLETE.md` | status · validation summary · deviations |
| Extraction script | `scripts/extract_literary_canon_dystopian.py` | NEEDED · stdlib zipfile (epub) + ebook-convert (mobi) + pdftotext (pdf). No new deps. |
| Chunk writer | `scripts/write_literary_canon_dystopian_chunks.py` | NEEDED · hand-authored thematic chunks + em-dash sweep via `chr(0x2014)` · short illustrative quotes only. Mirror `scripts/write_literary_canon_black_chunks.py`. |

### Schema decisions (recommended · finalized at chunk-write time)
- `batch_id`: `LITERARY_CANON_DYSTOPIAN`
- `chunk_id` pattern: `LITERARY_CANON_DYSTOPIAN_001` ... `_0NN`
- `source_title`: `<Title> · <Author>` (e.g. `Animal Farm · George Orwell`); synthesis chunks `Dystopian Canon · cross-text synthesis`
- `author`: `George Orwell`, `Margaret Atwood`, `Aldous Huxley`; synthesis `SNIPED (cross-text synthesis)`
- `source_file`: `animal_farm_orwell.txt`, `handmaids_tale_atwood.txt`, `brave_new_world_revisited_huxley.txt`

---

## 8 · Explicit exclusions

| Material | Disposition |
|---|---|
| 1984 SparkNotes guide · Fahrenheit 451 Bloom's Critical Interpretations | NOT in lane · skipped per staging-plan default · orphaned secondary texts (their primaries were not staged) · keep skipped |
| Front/back-matter, copyright pages, RosettaBooks eForeword | Stripped at extraction · not chunked |
| Long passages of in-copyright text | NOT reproduced · short illustrative quotes only (a sentence or two) |
| The novel Brave New World (1932) | NOT staged · only Brave New World REVISITED (1958 essays) is present · chunked as the nonfiction it is |
| General literary intake sources | OUT OF SCOPE · not touched (separate lane) |

---

## 9 · What this planning session does NOT do

- No extraction (the planning peek used stdlib zipfile / pdftotext / strings to stdout only · no extracted files written).
- No chunking. No JSONL writes. No master-file updates. No script files written.
- No BATCH_008 start. No general literary intake touched. No source files moved/renamed/deleted. No new dependencies. No commit.

---

## 10 · Recommended next operation

Authorize the extraction + chunk session per the locked 7-step SOP (steps 5-6):
1. Run `scripts/extract_literary_canon_dystopian.py` · stdlib zipfile (epub) + ebook-convert (mobi) + pdftotext (pdf) into `literary_canon_dystopian_extracted/` (front/back-matter stripped · Handmaid's Tale word-count verified against the 30k floor before chunking).
2. Hand-author 12-19 thematic chunks (target ~16) per the section 3 map · short illustrative quotes only · introduce `systems-thinking` (default) or reuse `systems` per operator confirmation.
3. Run `jsonl-validation` (6 checks) + em-dash sweep + a NEW-domain note.
4. Write summary + source index + logs + completion marker.
5. Stop after validation + reporting · await `master-consolidation` authorization.

After this mini-batch consolidates (target 946 -> ~958-965), the last queued literary lane per `STAGING_PLAN_2026-05-19_INTAKE.md` §5 is LITERARY_CANON_GENERAL, then BATCH_008 AI/tech canon. Beloved re-acquisition remains flagged.

---

## 11 · Open operator decisions surfaced

| # | Decision | Default recommendation |
|--:|---|---|
| 1 | `systems-thinking` NEW domain vs reuse existing `systems`? | Introduce `systems-thinking` as the NEW 60th domain (operator brief names it · more precise) · confirm at chunk-write |
| 2 | Study guides (1984 SparkNotes · Fahrenheit 451 Bloom's)? | Keep SKIPPED (not in lane · orphaned secondaries) |
| 3 | Brave New World Revisited treated as nonfiction essays (not the novel)? | YES · chunk it as Huxley's systems-warning essays · the strongest operator-warning source |

---

## 12 · Revision log

- **rev 1 (2026-05-20 · this version):** First plan for LITERARY_CANON_DYSTOPIAN. 3 files confirmed in the lane · all 3 pre-flight-checked as REAL full texts (no stubs · the Beloved lesson applied): Animal Farm (epub · 30,156 words), The Handmaid's Tale (mobi · real-novel markers · word count to verify at extraction), Brave New World Revisited (pdf · 93pp / 34,610 words · 1958 nonfiction essays, NOT the novel). 2 study guides confirmed absent · skipped per staging-plan default. Extraction: stdlib zipfile + ebook-convert + pdftotext · no OCR · no new deps. 12-19 chunk estimate · target ~16. `systems-thinking` flagged as a NEW domain (operator-approved · adjacent to existing `systems` · default introduce it). Cross-references mapped to B6, B7, N8N (the systems these warn about), PROMPT_TEMPLATES_DEEP (language control), and future BATCH_008 (the ethical counterweight). In-copyright brief-quote discipline specified.
