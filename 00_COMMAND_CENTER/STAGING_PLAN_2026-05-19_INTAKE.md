# Staging plan · 2026-05-19 SNIPED_OS intake · 2026-05-19

Plan to stage the new 2026-05-19 intake from `~/Downloads/    SNIPED_OS/` (which mirrors `~/Downloads/`) into `~/AI-Brain-Refinery/raw/` for future batch processing.

**Source universe:** `~/Downloads/    SNIPED_OS/` ONLY (canonical). Files also appear byte-identical in `~/Downloads/` root; source the staging copy pass from SNIPED_OS per the locked rule.
**Destination:** `~/AI-Brain-Refinery/raw/` (existing chapter tree, extended in §1).
**Constraints respected:** No files moved, deleted, renamed, extracted, chunked. No master files updated. Commands below are **recommendations only · do NOT execute as part of this plan**. Authorization required in a separate session before the copy pass runs.

Based on:
- `NEW_INTAKE_ACK_2026-05-19.md` (the inventory acknowledgement note · 290 lines · commit `568b602`)
- Live `find` against `~/Downloads/    SNIPED_OS/` at 2026-05-19 12:25 (this session)
- Cross-check against `RAW_POST_STAGING_INVENTORY_2026-05-18.md` (post-2026-05-18 staging state)
- Cross-check against current `raw/` (721 files · no overlap with 2026-05-19 intake confirmed)

## Headline numbers

- **Total 2026-05-19 candidates surveyed:** 43 files in SNIPED_OS dated newer than 2026-05-18
- **Recommended staged count:** 35 files (across 8 destination subfolders · 6 NEW chapter slots)
- **Recommended ignored / deferred count:** 8 files (1 zero-byte download, 4 partial `.part` downloads including 3 older non-2026-05-19, 3 Office stale-lock files)
- **Recommended next operation after staging:** `INTELLECTUAL_ARTIST_FRAME` mini-batch (1 source · 5-10 chunks) as the smallest validation of the staging copy pass. Then `B2B_POSITIONING_CLAUDE_OPERATOR` mini-batch (2 sources · 5-10 chunks). Then queue the larger mini-batches and BATCH_008 per the order in §5.

## What changed since `SNIPED_OS_STAGING_PLAN_2026-05-18.md`

The 2026-05-18 plan staged 216 of 217 named files (the only outstanding one was `MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx` · still pending second-staging authorization). That plan covered the photography canon + AI Edge course + Claude Code course material. The 2026-05-19 intake is **a separate, smaller drop of 43 files** with a different theme mix (literary canon + AI agency / n8n automation + B2B positioning + prompt-engineering deep templates).

---

## 0 · Reading guide

This plan has 6 parts:

1. **§1 Target structure** · 6 NEW destination subfolders under `raw/` (new chapter slots + sub-categorization).
2. **§2 Copy plan** · 8 lane-based `cp` blocks, one per future-batch lane.
3. **§3 Ignore / defer list** · 8 explicit files NOT being staged (zero-byte, `.part`, stale Office locks).
4. **§4 Overlap check** · 0 overlaps with current `raw/` confirmed.
5. **§5 Recommended next operation + batch routing** · post-staging order of operations.
6. **§6 What this plan does NOT do** · the constraint envelope.

**All commands use:**
```bash
SRC="$HOME/Downloads/    SNIPED_OS"
DST="$HOME/AI-Brain-Refinery/raw"
```

Quote `SRC` exactly because the folder has 4 leading spaces.

---

## 1 · Target raw subfolder structure

Recommended `mkdir` block. 6 NEW destination subfolders. Existing chapter dirs (00_BRIEF, 02_TIER_1_CANON_BOOKS, 05_AI_EDGE_COURSE, etc.) are untouched.

```bash
SRC="$HOME/Downloads/    SNIPED_OS"
DST="$HOME/AI-Brain-Refinery/raw"

# NEW: 2026-05-19 intake destinations
mkdir -p "$DST/10_REFERENCE/_intake_2026-05-19/automations"
mkdir -p "$DST/10_REFERENCE/_intake_2026-05-19/prompt_templates"
mkdir -p "$DST/10_REFERENCE/_intake_2026-05-19/opportunity_management"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/literary_canon_black"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/literary_canon_dystopian"
mkdir -p "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general"

# REUSED: existing chapter slots
# - raw/00_BRIEF/  · sniped_os_knowledge_dump.docx (if operator-authored doctrine per pre-flight peek)
# - raw/08_AI_TECH/  · claude_for_small_business_organized.docx (B2B positioning)
```

**Chapter-slot rationale:**

- `10_REFERENCE/_intake_2026-05-19/` mirrors the existing `_intake_2026-05-18/` pattern (already populated with Claude Code Superpowers, Plugin, AI Ops Dashboard, REMOTION, 2 automation blueprints).
- `02_TIER_1_CANON_BOOKS/literary_canon_black/` is a NEW subfolder mirroring the existing 8 Tier-1 subfolders (`advertising/`, `ai_tech/`, `culture/`, `network_distribution/`, `operating_founder/`, `photography/`, `sales_positioning/`, `strategy_history/`).
- `02_TIER_1_CANON_BOOKS/literary_canon_dystopian/` + `_general/` continue the literary-canon sub-categorization.

**Chapter-slot collisions:** None. All 6 new slots are nested inside existing chapter dirs.

---

## 2 · Copy plan · 8 lanes

### 2.1 · Lane A: `N8N_AUTOMATION_SYSTEMS` · 6 JSON workflows

Future batch lane. Extends BATCH_006 `automation-blueprint` domain (2 blueprints already chunked). 6 new n8n JSON workflows.

```bash
cp -p "$SRC/AI Phone Call Assistant - Call Workflow.json"             "$DST/10_REFERENCE/_intake_2026-05-19/automations/"
cp -p "$SRC/Master Prompt Agent - Chat Input.json"                    "$DST/10_REFERENCE/_intake_2026-05-19/automations/"
cp -p "$SRC/Master Prompt Agent - Form Submission.json"               "$DST/10_REFERENCE/_intake_2026-05-19/automations/"
cp -p "$SRC/n8n & RetellAI.json"                                      "$DST/10_REFERENCE/_intake_2026-05-19/automations/"
cp -p "$SRC/Prompt Writing Agent - Deep Reasoning Workflow.json"      "$DST/10_REFERENCE/_intake_2026-05-19/automations/"
cp -p "$SRC/Prompt Writing Agent - Normal Model Workflow.json"        "$DST/10_REFERENCE/_intake_2026-05-19/automations/"
```

Files: 6 · Size: ~5-50 KB each. Future batch: `N8N_AUTOMATION_SYSTEMS` · 15-25 chunks (1-3 per blueprint, pairing trigger + LLM + workflow + persistence layers per file).

### 2.2 · Lane B: `PROMPT_TEMPLATES_DEEP` · 8 Prompt Template PDFs

Future batch lane. Extends BATCH_006 `prompt-engineering` domain (8 framework prompts already chunked). 8 new prompt-engineering PDFs.

```bash
cp -p "$SRC/Prompt Template - Combining Techniques-2.pdf"             "$DST/10_REFERENCE/_intake_2026-05-19/prompt_templates/"
cp -p "$SRC/Prompt Template - Combining Techniques-3.pdf"             "$DST/10_REFERENCE/_intake_2026-05-19/prompt_templates/"
cp -p "$SRC/Prompt Template - In Context-2.pdf"                       "$DST/10_REFERENCE/_intake_2026-05-19/prompt_templates/"
cp -p "$SRC/Prompt Template - Problem Decomposition.pdf"              "$DST/10_REFERENCE/_intake_2026-05-19/prompt_templates/"
cp -p "$SRC/Prompt Template - Self Criticism (Advanced)-2.pdf"        "$DST/10_REFERENCE/_intake_2026-05-19/prompt_templates/"
cp -p "$SRC/Prompt Template - Self Criticism (Advanced)-3.pdf"        "$DST/10_REFERENCE/_intake_2026-05-19/prompt_templates/"
cp -p "$SRC/Prompt Template - Self Criticism (Basic)-3.pdf"           "$DST/10_REFERENCE/_intake_2026-05-19/prompt_templates/"
cp -p "$SRC/Prompt Template - Thought Generation-2.pdf"               "$DST/10_REFERENCE/_intake_2026-05-19/prompt_templates/"
```

Files: 8 · Size: ~10 MB each (notably large for PDFs · likely high-res slide decks or image-heavy templates; extraction may need `pdftotext -layout` rather than pandoc · word-count may be sparse).

**Versioning note:** The `-2` / `-3` suffixes suggest paired versions. Pre-flight peek at staging time should confirm whether `-3` supersedes `-2`. Conservative recommendation: stage all 8, dedupe at chunk-write time (set `-3` as canonical if content is identical · pair as "draft + revision" if they differ).

Future batch: `PROMPT_TEMPLATES_DEEP` · 10-15 chunks.

### 2.3 · Lane C: `B2B_POSITIONING / BASEPLATE_INTELLIGENCE` · 2 Claude business docs

Future batch lane. Operator-hypothesized · `claude_for_small_business_organized.docx` is the canonical operator-authored doc; `claude for small business.docx` is the earlier (legacy) version. Per `NEW_INTAKE_ACK_2026-05-19.md` §6: pre-flight peek required to confirm.

```bash
# Canonical (organized version)
cp -p "$SRC/claude_for_small_business_organized.docx" "$DST/08_AI_TECH/claude_for_small_business/"

# Legacy (earlier version · may be superseded · stage for dedupe at chunk-write time)
cp -p "$SRC/claude for small business.docx"           "$DST/08_AI_TECH/claude_for_small_business/_legacy/"

# Requires the subfolder to be created first
# Add to the §1 mkdir block:
#   mkdir -p "$DST/08_AI_TECH/claude_for_small_business/_legacy"
```

Files: 2 (1 canonical + 1 legacy) · Size: 17.6 KB + ~similar legacy. Future batch: `B2B_POSITIONING_CLAUDE_OPERATOR` mini-batch · 5-10 chunks (chunk `_organized` as canonical; legacy used only if dedupe proves unique material).

**Pre-flight peek recommendation:** Before authorizing the copy pass, run `pandoc -f docx -t plain "$SRC/claude_for_small_business_organized.docx" | head -100` to confirm the doc's actual content + classification. If the doc reads more as N8N_AUTOMATION_SYSTEMS / AI_AUTOMATION_AGENCY_COURSE territory, route to `08_AI_TECH/ai_history_case_studies/` or `05_AI_EDGE_COURSE/` instead.

### 2.4 · Lane D: `CLAUDE_OPERATOR_MARKET` / agency-course brief · 1 SNIPED-internal knowledge dump

Future batch lane. Filename `sniped_os_knowledge_dump.docx` is ambiguous · could be operator-authored SNIPED doctrine (B7-addendum candidate) or AI-agency course brief (CLAUDE_OPERATOR_MARKET / BATCH_008 territory).

```bash
# OPERATOR DECISION POINT · choose ONE destination after pre-flight peek
# Option A (if operator-authored SNIPED doctrine):
cp -p "$SRC/sniped_os_knowledge_dump.docx" "$DST/00_BRIEF/sniped_os_knowledge_dump.docx"

# Option B (if AI-agency course brief or external knowledge dump):
cp -p "$SRC/sniped_os_knowledge_dump.docx" "$DST/08_AI_TECH/ai_history_case_studies/"

# Default recommendation pending peek: Option B (the filename pattern matches the existing
# `AI CHANGED EVERYTHING.docx` and similar dump-format docs in 08_AI_TECH/).
```

Files: 1 · Size: 27.8 KB. Future batch: depends on classification · operator-doctrine addendum to BATCH_007 (re-do consolidation) OR `CLAUDE_OPERATOR_MARKET` mini-batch alongside the B2B positioning doc · 3-8 chunks.

**Pre-flight peek MANDATORY:** Before authorizing the copy pass, run `pandoc -f docx -t plain "$SRC/sniped_os_knowledge_dump.docx" | head -150` to confirm authorship voice. Operator-voice (Bryce/BJ) → 00_BRIEF. Third-party agency brief → 08_AI_TECH.

### 2.5 · Lane E: `OPPORTUNITY_MANAGEMENT` · 2 business-asset templates

Future mini-batch lane. Pairs with BATCH_006 AI Ops Dashboard PRD (already chunked · opportunity-object schema + ROI-calculator). The xlsx + pptx are operator-facing templates.

```bash
cp -p "$SRC/Opp hopper + Biz Case.xlsx"         "$DST/10_REFERENCE/_intake_2026-05-19/opportunity_management/"
cp -p "$SRC/Opportunity Card [Example].pptx"    "$DST/10_REFERENCE/_intake_2026-05-19/opportunity_management/"
```

Files: 2 · Size: ~6 MB (pptx is image-heavy) + small xlsx. Future batch: folded into `N8N_AUTOMATION_SYSTEMS` mini-batch OR its own `OPPORTUNITY_MANAGEMENT_TEMPLATES` mini-batch · 2-5 chunks (xlsx schema + pptx slide-summary).

**Extraction note:** `.xlsx` extraction requires `pandoc` (which converts cells to markdown tables) OR Python `openpyxl` for richer schema-preservation. `.pptx` extraction via `pandoc` produces slide-by-slide text. Both formats are unusual for SNIPED's text-heavy chunk pattern · expect lower chunk density than .md/.docx sources.

### 2.6 · Lane F: `INTELLECTUAL_ARTIST_FRAME` · 1 primary-source memoir

Future mini-batch lane. MJ Moonwalk (2009 Crown Archetype reissue · 1988 original) directly matches the preserved "disciplined-time / deep study / intellectual artist" frame held in operator notes. Grounds the operator-doctrine cluster with primary-source backing.

```bash
cp -p "$SRC/ Michael Jackson - Moonwalk (2009, Crown Archetype) - libgen.li.epub"  "$DST/02_TIER_1_CANON_BOOKS/operating_founder/"
```

**Note on leading space in filename:** The original filename starts with a space (likely accidental from libgen.li). Stage as-is (preserves provenance). Rename at extraction time only if it breaks tooling.

Files: 1 · Size: ~? (smaller epub). Future batch: `INTELLECTUAL_ARTIST_FRAME` mini-batch · 5-10 chunks. Destination `operating_founder/` reuses the existing Tier 1 sub-category (Stoute, Iger, Knight, Catmull live there).

**Alternative destination:** A NEW `02_TIER_1_CANON_BOOKS/intellectual_artist/` subfolder if operator wants a clean lane for future similar acquisitions (Quincy Jones autobiography, Miles Davis autobiography, etc.). For now, `operating_founder/` is the closest existing slot.

### 2.7 · Lane G: `LITERARY_CANON_BLACK` · 4 primary-source books (+ optional 5th)

Future batch lane. Reinforces the locked Lineage Doctrine (Southern Black tradition · HBCU intellectual · gospel · Black founder LA) with primary-source Black literary canon.

```bash
cp -p "$SRC/[Beloved Trilogy 1 - Beloved Trilogy 1] Beloved{Toni Morrison}(1987){112430403} libgen.li.pdf" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_black/"
cp -p "$SRC/Toni Morrison - The Bluest Eye (2007, Knopf Doubleday Publishing Group) - libgen.li.mobi" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_black/"
cp -p "$SRC/[The Color Purple 1 - The Color Purple 1] The Color Purple Collection_ The Color Purple, The Temple of My Familiar, and Possessing the Secr...{Walker, Alice}(2012, Open Road){112044773} libgen.li.epub" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_black/"
cp -p "$SRC/Zora Neale Hurston - Their Eyes Were Watching God (2009, HarperCollins e-books) - libgen.li.zip" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_black/"

# OPTIONAL: Lee TKAM if operator wants Southern-canon adjacency (not strictly Black canon but cultural overlap)
cp -p "$SRC/ Harper Lee - To Kill a Mockingbird - libgen.li.mobi" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_black/"
# OR route Lee TKAM to literary_canon_general/ if operator wants strict Black-canon scope
```

Files: 4 strict + 1 optional (Lee TKAM has cultural overlap but is white-authored Southern lit · operator decision on which subfolder).

**Format mix:** 1 PDF + 1 mobi + 1 epub + 1 zip (Their Eyes Were Watching God is zipped · unzip at extraction time, not staging) + optional 1 mobi for Lee. Extraction pipeline: pdf→pdftotext, mobi→ebook-convert, epub→ebook-convert, zip→unzip then re-classify.

Future batch: `LITERARY_CANON_BLACK` mini-batch · 25-35 chunks (Morrison gets ~10, Walker collection ~8 across 3 novels, Hurston ~5, Lee optional ~5). MAY fold into BATCH_010 lineage + Black culture canon.

### 2.8 · Lane H: `DYSTOPIAN_CANON` · 3 primary texts + 2 study guides

Future mini-batch lane. Dystopian / political canon. Cultural context for the SNIPED operator's stance on AI commodification + surveillance + the broader 2027+ external-proof positioning.

```bash
cp -p "$SRC/[Animal Farm _1] Orwell, George - Animal Farm (1945, Secker & Warburg) - libgen.li.epub" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/"
cp -p "$SRC/[The Handmaid's Tale 1 ] Atwood, Margaret - The Handmaid's Tale (2006_2017, Everyman's Library_Anchor Books) - libgen.li.mobi" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/"
cp -p "$SRC/Aldous Huxley - Brave New World Revisited (2001) - libgen.li.pdf" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/"

# Secondary / study guides · operator decision: stage or skip
cp -p "$SRC/[SparkNotes Literature Guide ] Orwell, George - 1984, George Orwell (1984_2014, Spark Publishing) - libgen.li.epub" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/_study_guides/"
cp -p "$SRC/Ray Bradbury - Ray Bradbury's Fahrenheit 451 (Bloom's Modern Critical Interpretations) (2008) - libgen.li.pdf" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/_study_guides/"

# Add to §1 mkdir block:
#   mkdir -p "$DST/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/_study_guides"
```

Files: 3 strict + 2 study guides = 5 total. The 2 study guides are SECONDARY texts (SparkNotes is for 1984 itself, which is NOT in this intake · context only; Bloom's Critical Interpretations is for Fahrenheit 451 which is also NOT in this intake). Operator decision: stage for completeness OR skip (low strategic priority).

**Default recommendation:** stage the 3 strict + skip the 2 secondary (study guides without their primary texts are weak strategic chunks). Update count if skipped: 35 → 33 staged.

Future batch: `DYSTOPIAN_CANON` mini-batch · 10-20 chunks across 3 primary texts (Animal Farm ~4, Handmaid's Tale ~6, Huxley BNW Revisited ~5).

### 2.9 · Lane I: `GENERAL_LITERARY_CANON` · 9 primary-source classics (after curation)

Future mini-batch lane. Remaining literary classics · operator-curated subset.

```bash
cp -p "$SRC/James Joyce - Ulysses (2000, Penguin Group) - libgen.li.epub" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general/"
cp -p "$SRC/JAMES_ALLEN-AS_A_MAN_THINKETH.pdf" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general/"
cp -p "$SRC/Kahlil Gibran - The Prophet (1973) - libgen.li.lit" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general/"
cp -p "$SRC/Khaled Hosseini - The Kite Runner (2004, Riverhead Trade) - libgen.li.mobi" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general/"
cp -p "$SRC/Kurt Vonnegut - Slaughterhouse-Five - libgen.li.pdf" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general/"
cp -p "$SRC/Nabokov, Vladimir - Lolita (Vladimir Nabokov) - libgen.li.pdf" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general/"
cp -p "$SRC/Richard Bach - Jonathan Livingston Seagull. (1973, Avon Books, N. Y.) - libgen.li.djvu" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general/"

# Graphic novel · Maus I only (Maus II is broken · see §3)
cp -p "$SRC/Maus I.cbr" \
      "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general/"

# Russian-author file · UNCERTAIN PROVENANCE · operator decision before staging
# cp -p "$SRC/[Part 1 ] Шерман, Алекси _ - libgen.li.mobi" \
#       "$DST/02_TIER_1_CANON_BOOKS/literary_canon_general/"
```

Files: 8 staged (assuming Russian-author file is held for operator verification) + 1 held = 9 candidates.

**Russian-author file flag:** `[Part 1 ] Шерман, Алекси _ - libgen.li.mobi` (2.7 MB) has uncertain provenance · Cyrillic-only filename with no English title context. Operator should verify the author (Alexei Sherman? · could be a novel, a non-fiction work, or junk) before authorizing staging. Default recommendation: HOLD until operator confirms what the book is.

**Format mix:** 2 epub + 1 mobi + 4 pdf + 1 djvu + 1 lit + 1 cbr. The `.djvu` (Jonathan Livingston Seagull) needs `djvu2text` or conversion via `ebook-convert`. The `.lit` (Gibran The Prophet) is older Microsoft Reader · needs conversion. The `.cbr` (Maus I) is comic-book reader · NOT text-extractable directly · needs OCR or operator decision to chunk only intro/colophon material.

**Maus extraction caveat:** Maus I is a comic-book graphic novel (Spiegelman's Holocaust memoir). The `.cbr` format wraps RAR-compressed images · no native text. Either (a) OCR every page (expensive, slow), (b) chunk only the metadata + 1-2 hand-authored summary chunks naming the work + its thematic load-bearing weight, or (c) skip entirely. Default recommendation: stage Maus I but flag for hand-authored summary-only chunks in the future batch.

Future batch: `GENERAL_LITERARY_CANON` mini-batch · 30-50 chunks across 7-8 books (operator-curated · some books may be skipped at chunk time if strategic value is unclear).

---

## 3 · Ignore / defer list · 8 files

8 files in SNIPED_OS dated newer than 2026-05-18 (or older `.part` carryover) that are NOT being staged.

| # | File | Size | Reason | Action |
|--:|---|---:|---|---|
| 1 | `Maus II.cbr` | **0 bytes** | ZERO-BYTE DOWNLOAD · download failed · the `.part` sibling has the real partial data | IGNORE · do not stage · operator should re-download from source |
| 2 | `Maus II.j93PR5Wn.cbr.part` | 15 MB | PARTIAL DOWNLOAD · `.part` suffix per AGENTS.md drift rule | IGNORE · do not stage |
| 3 | `~$aude for small business.docx` | small | OFFICE STALE-LOCK pattern (`~$*` per AGENTS.md drift rule) | IGNORE · do not stage |
| 4 | `~$iped figma.docx` | small | OFFICE STALE-LOCK · existed before 2026-05-19 but worth flagging here for completeness | IGNORE · do not stage · operator may delete the lock |
| 5 | `~$FIGMA.docx` | small | OFFICE STALE-LOCK · existed before 2026-05-19 but worth flagging | IGNORE · do not stage · operator may delete the lock |
| 6 | `_.epub` | small | UNNAMED FILE · single underscore as filename · likely a failed download or placeholder | IGNORE · operator should verify or delete |
| 7 | `Petre, Peter_Schwarzenegger, Arnold - Total recall...epub.part` | partial | PARTIAL DOWNLOAD · `.part` · existed before 2026-05-19 but worth flagging | IGNORE · operator should re-download |
| 8 | `Gabriel Weinberg, Justin Mares - Traction...epub.part` | partial | PARTIAL DOWNLOAD · `.part` · existed before 2026-05-19 but worth flagging | IGNORE · operator should re-download |

Plus: `Coddington, Grace - Grace_ A Memoir...epub.part` · partial · IGNORE.

**House-keeping note:** Items 4-5 (Office lock files), 7-8 (partial downloads from prior intake), and the Coddington `.part` are NOT 2026-05-19 intake · they were in SNIPED_OS before 2026-05-19 but were never staged (correctly). They appear in the broader SNIPED_OS drift-safety scan (rule 1 in AGENTS.md) and are documented here as a holistic cleanup recommendation: the operator can safely delete these from SNIPED_OS at any time without affecting staging or batching.

---

## 4 · Overlap check · 0 overlaps with current `raw/`

Confirmed via `find raw -type f` against all 43 candidate filenames + 17 literary-canon titles:

- 0 matches for any 2026-05-19 docx/json/pdf in `raw/`
- 0 matches for any of the 17 literary-canon book titles in `raw/`
- 0 matches for `sniped_os_knowledge_dump*`, `claude_for_small_business*`, `Master Prompt Agent*`, `AI Phone*`, `n8n*Retell*`, `Prompt Writing Agent*`, `Prompt Template*`, `Opp hopper*`, `Opportunity Card*`, `Maus*`, `Moonwalk*` in `raw/`

The 2026-05-19 intake is **genuinely net-new to `raw/`**. No de-duplication needed at staging time.

**Internal duplicates within the intake (1 pair):**

- `claude_for_small_business_organized.docx` (canonical · 17.6 KB) supersedes `claude for small business.docx` (legacy · ~similar). Both staged into a parent + `_legacy/` sibling subfolder per §2.3 to preserve version provenance. Dedupe decision is made at chunk-write time, not at staging time.

**Internal version pairs within Lane B (4 potential pairs):**

- `Prompt Template - Combining Techniques-2.pdf` ↔ `-3.pdf` (same size to the byte: 10,364,835 bytes each · IDENTICAL FILE · likely two saves of the same content · DEDUPE candidate)
- `Prompt Template - Self Criticism (Advanced)-2.pdf` ↔ `-3.pdf` (same size to the byte: 10,361,550 bytes each · IDENTICAL · DEDUPE candidate)
- `Prompt Template - In Context-2.pdf` (no `-3` pair) · stage solo
- `Prompt Template - Self Criticism (Basic)-3.pdf` (no `-2` pair) · stage solo
- `Prompt Template - Thought Generation-2.pdf` (no `-3` pair) · stage solo
- `Prompt Template - Problem Decomposition.pdf` (no version suffix) · stage solo

**Recommendation:** Stage all 8 PDFs verbatim (preserves provenance), but at chunk-write time check the 2 identical-size pairs · if md5 confirms identity, chunk only the `-3` version of each pair (the higher-numbered suggesting a revision). Net chunk count: 6 PDFs effectively (8 staged - 2 redundant pairs = 6 unique).

---

## 5 · Recommended next operation + batch routing

### Order of operations

1. **Now:** operator reviews this plan. Authorize the copy pass in a separate session.
2. **Pre-copy peeks (3-5 min each):**
   - `pandoc -f docx -t plain "$SRC/sniped_os_knowledge_dump.docx" | head -150` · confirms classification (00_BRIEF doctrine vs 08_AI_TECH agency-brief).
   - `pandoc -f docx -t plain "$SRC/claude_for_small_business_organized.docx" | head -150` · confirms B2B positioning content.
   - `pdftotext "$SRC/Prompt Template - Combining Techniques-2.pdf" - | head -50` · sample a Prompt Template to confirm format (slide-style or text-style).
   - Verify the Russian-author file `[Part 1 ] Шерман, Алекси _.mobi` provenance (translate the author name + content).
3. **Authorized copy pass:** run §1 mkdir + §2 lane commands. Verify with `find raw/10_REFERENCE/_intake_2026-05-19 raw/02_TIER_1_CANON_BOOKS/literary_canon_* -type f | wc -l` (expected 35 if all lanes staged · 33 if dystopian study guides skipped · 28 if Russian-author held).
4. **Update `RAW_POST_STAGING_INVENTORY_2026-05-18.md`** (or write `RAW_POST_STAGING_INVENTORY_2026-05-19.md`) to reflect the post-copy state.
5. **Authorize the first downstream batch.** Recommended order (smallest first to validate the pipeline):

### Recommended batch sequence post-staging

| Order | Batch / mini-batch | Sources | Est. chunks | Why this order |
|---|---|---:|---:|---|
| 1 | `INTELLECTUAL_ARTIST_FRAME` mini-batch | 1 (MJ Moonwalk) | 5-10 | Smallest validation pass · 1 epub source · simple extraction pipeline · operator-doctrine grounding |
| 2 | `B2B_POSITIONING_CLAUDE_OPERATOR` mini-batch | 1-2 (claude_for_small_business_organized + optional legacy) | 5-10 | Quick lane · 1-2 docx · pandoc extraction · validates the new `08_AI_TECH/claude_for_small_business/` subfolder |
| 3 | `OPPORTUNITY_MANAGEMENT_TEMPLATES` mini-batch | 2 (xlsx + pptx) | 2-5 | Validates xlsx + pptx extraction methods · low chunk yield but high coverage of new format types |
| 4 | `N8N_AUTOMATION_SYSTEMS` mini-batch | 6 (JSON) | 15-25 | Extends B6 `automation-blueprint` domain · JSON parsing only · no pandoc needed |
| 5 | `PROMPT_TEMPLATES_DEEP` mini-batch | 6-8 (PDF · after dedupe) | 10-15 | Extends B6 `prompt-engineering` domain · pdftotext extraction · 2 identical-size pairs deduplicated |
| 6 | `CLAUDE_OPERATOR_MARKET` mini-batch | 1 (sniped_os_knowledge_dump.docx) | 3-8 | Depends on peek classification · may be B7-addendum instead of separate mini-batch |
| 7 | `INTELLECTUAL_ARTIST_FRAME` extension | + curated supporting (when acquired) | ~ | Defer until more intellectual-artist canon arrives |
| 8 | `BATCH_LITERARY_CANON_BLACK` | 4-5 books | 25-35 | Reinforces Lineage Doctrine · MAY fold into BATCH_010 |
| 9 | `BATCH_LITERARY_CANON_DYSTOPIAN` | 3 (or 5 with study guides) | 10-20 | Smaller cluster · validates literary chunking patterns |
| 10 | `BATCH_LITERARY_CANON_GENERAL` | 7-8 (operator-curated) | 30-50 | Largest literary cluster · ebook-convert + djvu2text + lit conversion pipeline · save for last |
| 11 | `BATCH_008 · AI / tech / Claude Code canon` | 12 ai_tech books + AI Edge + AI CHANGED + youtube skool | 100-130 | The originally-planned BATCH_008 · runs AFTER the 2026-05-19 mini-batches |

### Should the new intake become BATCH_008?

**Recommendation: No. Run the new intake as 6-7 mini-batches before BATCH_008.** Reasoning:

1. **The new intake is thematically heterogeneous** (literary canon + automation + prompt engineering + B2B positioning + AI agency course brief). Combining all 35 staged files into a single BATCH_008 would cross 4-5 distinct domain lanes and dilute the per-batch coherence that BATCH_005-007 established.
2. **The originally-planned BATCH_008 (AI / tech / Claude Code canon · 12 books + AI Edge Course + AI CHANGED + youtube skool) has its own thematic coherence** · AI-canon as a primary-source pass.
3. **Mini-batch ordering validates the pipeline incrementally.** Running INTELLECTUAL_ARTIST_FRAME (1 source · 5-10 chunks) first proves the new-folder + ebook-convert pipeline works before committing to the 30-50 chunk GENERAL literary canon pass.
4. **The 2 new operator-engine-extending mini-batches (N8N_AUTOMATION_SYSTEMS + PROMPT_TEMPLATES_DEEP) naturally extend BATCH_006's `automation-blueprint` + `prompt-engineering` domains** · they belong as B6-extensions, not B8-merged.
5. **`sniped_os_knowledge_dump.docx` classification is unresolved** · running it solo as a `CLAUDE_OPERATOR_MARKET` mini-batch (or as a B7-addendum) lets the operator review the peek-classification before the bigger commitments.

**Alternative if operator prefers fewer batches:** combine all 6 operator-engine-extension mini-batches (Lanes A-E + the Russian-author held file if cleared) into a single `BATCH_008_2026-05-19_INTAKE` (operator skill / automation / B2B positioning + intellectual artist) and run the 3 literary-canon passes separately as `BATCH_009/010/011`. Renaming `BATCH_008` from AI/tech canon to 2026-05-19-intake-bundle is a clean signal that the new intake was prioritized. AI/tech canon would then become `BATCH_012`. Operator decision.

**Default recommendation: keep mini-batch granularity.** Mini-batches are easier to validate, easier to roll back, and produce cleaner master_index sections. Use multiple mini-batches before BATCH_008.

---

## 6 · Post-staging verification block

Recommended verification after the authorized copy pass:

```bash
# Count new staged files
find raw/10_REFERENCE/_intake_2026-05-19 -type f | wc -l
# Expected: 16 (6 automations + 8 prompt templates + 2 opportunity-mgmt)

find raw/02_TIER_1_CANON_BOOKS/literary_canon_black -type f | wc -l
# Expected: 4 strict (+ 1 if Lee TKAM routed here)

find raw/02_TIER_1_CANON_BOOKS/literary_canon_dystopian -type f | wc -l
# Expected: 3 strict (+ 2 if study guides also staged)

find raw/02_TIER_1_CANON_BOOKS/literary_canon_general -type f | wc -l
# Expected: 8 (or 7 if Russian-author held; or 9 if Lee TKAM routed here)

find raw/02_TIER_1_CANON_BOOKS/operating_founder -name "*Moonwalk*" -o -name "*Michael Jackson*"
# Expected: 1 match

find raw/08_AI_TECH/claude_for_small_business -type f
# Expected: 1-2 files

# Drift-safety scan in new destinations
find raw/10_REFERENCE/_intake_2026-05-19 raw/02_TIER_1_CANON_BOOKS/literary_canon_* -name "*.part" -o -name '~$*' -o -name ".DS_Store" -o -name "_.epub" -o -size 0c
# Expected: 0 results
```

---

## 7 · Open operator decisions surfaced (4 items · pre-flight peek dependent)

| # | Decision | Default recommendation | Trigger |
|--:|---|---|---|
| 1 | `sniped_os_knowledge_dump.docx` → 00_BRIEF/ or 08_AI_TECH/? | 08_AI_TECH (pending peek) | Pandoc peek at copy-pass authorization time |
| 2 | Russian-author `[Part 1 ] Шерман, Алекси _.mobi` · stage or hold? | HOLD until provenance confirmed | Operator translates author name + opens file |
| 3 | Lee TKAM · `literary_canon_black/` or `literary_canon_general/`? | `literary_canon_black/` (Southern-canon cultural-overlap) OR operator preference | Operator decision at copy-pass time |
| 4 | Dystopian study guides · stage or skip? | SKIP (secondary texts without primary in intake) | Operator decision at copy-pass time |

---

## 8 · What this plan does NOT do

- No file moves, copies, deletions, renames, or extractions.
- No master file updates (`MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` untouched).
- No chunking. No JSONL writes.
- No batch extraction. No BATCH_008 start.
- No commits.
- No new dependencies beyond what's already on PATH (`pandoc`, `pdftotext`, `ebook-convert`).
- No OCR. No Whisper.
- No web codebase changes.

Authorization required before any of the above. Stop here.

---

## 9 · Revision log

- **rev 1 (2026-05-19 12:25 · this version):** First plan for the 2026-05-19 intake. 43 candidates surveyed · 35 recommended staged · 8 ignored/deferred. 8 future-batch lanes identified. 6 NEW destination subfolders proposed. 4 operator decisions surfaced. Default next operation: `INTELLECTUAL_ARTIST_FRAME` mini-batch (smallest pipeline validation pass) followed by `B2B_POSITIONING_CLAUDE_OPERATOR` and 5 more mini-batches before BATCH_008.
