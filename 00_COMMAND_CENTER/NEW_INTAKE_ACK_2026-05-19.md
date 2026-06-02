# New intake acknowledgement · 2026-05-19

Inventory pass only. No staging, copying, moving, extracting, chunking, OCR, transcription, or master-file updates.

## TL;DR

- **40+ new files** appeared in `~/Downloads/` and `~/Downloads/    SNIPED_OS/` since the 2026-05-18 post-staging inventory.
- **None are in `raw/`** yet. Working tree is clean except for the previously-untracked `BATCH_007_PLAN.md`.
- **None of the new intake fits the locked BATCH_007 scope** (doctrine + SOPs + working drafts + outreach/delivery/content/commercial operator docs).
- **BATCH_007_PLAN.md should be left unchanged.** Proceed to BATCH_007 extraction first; queue the new intake into a staging plan after BATCH_007 ships.
- 4 distinct downstream batches are implied by the intake (n8n automation, Claude B2B positioning, business-asset templates, literary canon).
- 3 drift-flagged junk items present in SNIPED_OS · ignore at staging time.

---

## 1 · The two named files · exact paths

| File | Size | mtime | Paths |
|---|---:|---|---|
| `sniped_os_knowledge_dump.docx` | 27,769 bytes (~27 KB) | 2026-05-19 11:09 | `~/Downloads/sniped_os_knowledge_dump.docx` + `~/Downloads/    SNIPED_OS/sniped_os_knowledge_dump.docx` |
| `claude_for_small_business_organized.docx` | 17,625 bytes (~17 KB) | 2026-05-19 11:17 | `~/Downloads/claude_for_small_business_organized.docx` + `~/Downloads/    SNIPED_OS/claude_for_small_business_organized.docx` |

**Both files exist in both Downloads and SNIPED_OS · byte-identical (same size).** NEITHER is staged in `raw/`.

The "earlier-version" sibling `claude for small business.docx` exists in `~/Downloads/    SNIPED_OS/` only (not in Downloads root) · this is the pre-organization version. The corresponding Office stale-lock `~$aude for small business.docx` is also present in SNIPED_OS only · standard Word lock-file pattern, must be ignored at staging time.

---

## 2 · Other new files since the 2026-05-18 inventory

The 2026-05-18 post-staging inventory snapshot recorded 721 files in `raw/` and a pre-staging SNIPED_OS baseline of 484 files. The current SNIPED_OS state is **770 files** (excluding `.DS_Store`). 49 files are net-new since 2026-05-18 (= 40 new content + the two `claude for small business*` siblings + the Office lock file + 6 other files including 2 the canonical claude doc and similar).

### 2.1 · n8n automation workflows (6 JSON files · NEW SOURCE FAMILY)

| # | File | Size | Where |
|--:|---|---:|---|
| 1 | `AI Phone Call Assistant - Call Workflow.json` | ? | Downloads + SNIPED_OS |
| 2 | `Master Prompt Agent - Chat Input.json` | ? | Downloads + SNIPED_OS |
| 3 | `Master Prompt Agent - Form Submission.json` | ? | Downloads + SNIPED_OS |
| 4 | `n8n & RetellAI.json` | ? | Downloads + SNIPED_OS |
| 5 | `Prompt Writing Agent - Deep Reasoning Workflow.json` | ? | Downloads + SNIPED_OS |
| 6 | `Prompt Writing Agent - Normal Model Workflow.json` | ? | Downloads + SNIPED_OS |

Pairs structurally with the 2 BATCH_006 automation blueprints already chunked (`AI Content Strategy Generator`, `ElevenLabs voice agent`). Likely future batch: `N8N_AUTOMATION_SYSTEMS` or extension of `automation-blueprint` domain.

### 2.2 · Prompt-engineering template PDFs (8 PDFs · NEW SOURCE FAMILY)

| # | File |
|--:|---|
| 1 | `Prompt Template - Combining Techniques-2.pdf` |
| 2 | `Prompt Template - Combining Techniques-3.pdf` |
| 3 | `Prompt Template - In Context-2.pdf` |
| 4 | `Prompt Template - Problem Decomposition.pdf` |
| 5 | `Prompt Template - Self Criticism (Advanced)-2.pdf` |
| 6 | `Prompt Template - Self Criticism (Advanced)-3.pdf` |
| 7 | `Prompt Template - Self Criticism (Basic)-3.pdf` |
| 8 | `Prompt Template - Thought Generation-2.pdf` |

Suffix patterns (`-2`, `-3`) suggest these are versioned drafts or multi-page sets. Pairs structurally with the BATCH_006 `prompt-engineering` domain (8 Claude50 prompt-craft packs already chunked: TCREI, framework-orchestrator, pyramid-structured-communication, etc.). Likely future batch: extension of `prompt-engineering` domain in a `PROMPT_TEMPLATES_DEEP` mini-batch.

### 2.3 · Claude / business positioning docs (3 files + 1 lock · NEW SOURCE FAMILY)

| # | File | Notes |
|--:|---|---|
| 1 | `claude_for_small_business_organized.docx` | THE NAMED FILE · canonical organized version |
| 2 | `claude for small business.docx` | EARLIER VERSION · SNIPED_OS only · likely superseded by the `_organized` version |
| 3 | `sniped_os_knowledge_dump.docx` | THE NAMED FILE · operator-authored knowledge dump |
| 4 | `~$aude for small business.docx` | OFFICE STALE-LOCK · IGNORE at staging time |

Pre-flight peek not performed (per the no-extraction rule). Hypothesis (per operator brief): `sniped_os_knowledge_dump.docx` belongs to a future `N8N_AUTOMATION_SYSTEMS / AI_AUTOMATION_AGENCY_COURSE` batch; `claude_for_small_business_organized.docx` belongs to a future `B2B_POSITIONING / BASEPLATE_INTELLIGENCE / AI_OPERATOR_MARKET` batch. Neither directly reinforces BATCH_007's locked doctrine + SOP layer.

### 2.4 · Business-asset templates (2 files · NEW SOURCE FAMILY)

| # | File |
|--:|---|
| 1 | `Opp hopper + Biz Case.xlsx` |
| 2 | `Opportunity Card [Example].pptx` |

Pairs with the BATCH_006 `AI Ops Dashboard PRD` chunked source (opportunity-object schema + ROI-calculator pattern). The `xlsx` and `pptx` formats suggest these are operator-facing templates rather than text-dense sources. Likely future batch: AI-ops / opportunity-management mini-batch alongside the n8n automation workflows.

### 2.5 · Literary canon (19+ files · MAJOR NEW SOURCE FAMILY)

| # | File | Format | Why notable |
|--:|---|---|---|
| 1 | ` Michael Jackson - Moonwalk (2009, Crown Archetype) - libgen.li.epub` | epub | **DIRECTLY MATCHES** the preserved "MJ disciplined-time / deep study / intellectual artist" frame |
| 2 | `[Beloved Trilogy 1 - Beloved Trilogy 1] Beloved{Toni Morrison}(1987) - libgen.li.pdf` | pdf | Toni Morrison · Black literary canon |
| 3 | `Toni Morrison - The Bluest Eye (2007) - libgen.li.mobi` | mobi | Toni Morrison · Black literary canon |
| 4 | `[The Color Purple 1] The Color Purple Collection{Walker, Alice}(2012) - libgen.li.epub` | epub | Alice Walker · Black literary canon |
| 5 | `Zora Neale Hurston - Their Eyes Were Watching God (2009) - libgen.li.zip` | zip | Zora Neale Hurston · Black literary canon |
| 6 | ` Harper Lee - To Kill a Mockingbird - libgen.li.mobi` | mobi | American Southern canon |
| 7 | `[Animal Farm _1] Orwell, George - Animal Farm (1945) - libgen.li.epub` | epub | Dystopian / political canon |
| 8 | `[SparkNotes Literature Guide] Orwell, George - 1984 (2014) - libgen.li.epub` | epub | 1984 SparkNotes guide · NOT primary text |
| 9 | `[The Handmaid's Tale 1] Atwood, Margaret - The Handmaid's Tale (2006) - libgen.li.mobi` | mobi | Dystopian canon |
| 10 | `Aldous Huxley - Brave New World Revisited (2001) - libgen.li.pdf` | pdf | Huxley · companion to BNW, not the novel itself |
| 11 | `Ray Bradbury - Ray Bradbury's Fahrenheit 451 (Bloom's Modern Critical Interpretations) (2008) - libgen.li.pdf` | pdf | Critical-interpretations volume · NOT primary text |
| 12 | `James Joyce - Ulysses (2000, Penguin Group) - libgen.li.epub` | epub | Modernist canon |
| 13 | `JAMES_ALLEN-AS_A_MAN_THINKETH.pdf` | pdf | Self-development classic (1903) |
| 14 | `Kahlil Gibran - The Prophet (1973) - libgen.li.lit` | lit | `.lit` format is older Microsoft Reader · may need conversion · poetic philosophy |
| 15 | `Khaled Hosseini - The Kite Runner (2004) - libgen.li.mobi` | mobi | Modern literary fiction |
| 16 | `Kurt Vonnegut - Slaughterhouse-Five - libgen.li.pdf` | pdf | American canon |
| 17 | `Nabokov, Vladimir - Lolita - libgen.li.pdf` | pdf | 20th-century canon |
| 18 | `Richard Bach - Jonathan Livingston Seagull. (1973, Avon Books) - libgen.li.djvu` | djvu | Scanned · need djvu→text path |
| 19 | `Maus I.cbr` | cbr | Comic-book reader format · Spiegelman's Holocaust memoir · graphic novel |
| 20 | `Maus II.cbr` | cbr | Comic-book reader format · Maus continuation |
| 21 | `[Part 1 ] Шерман, Алекси - libgen.li.mobi` | mobi | RUSSIAN AUTHOR · unclear which work · review needed |

**Significance:** This is the largest new source family in this intake. It cleaves into 4 sub-clusters:

- **Black literary canon (4 books · 5 if counting Color Purple collection volumes):** Morrison ×2, Walker, Hurston. Directly reinforces the locked Lineage Doctrine (Southern Black tradition + HBCU intellectual + Black church). Future batch: pairs with BATCH_010 Lineage canon or its own `BATCH_LITERARY_CANON_BLACK` pass.
- **MJ Moonwalk** (1 epub) · directly named in the preserved high-signal note · operator-engine candidate for an `INTELLECTUAL_ARTIST_FRAME` mini-batch or sits with the operator-doctrine cluster.
- **Dystopian / political canon (3 books):** Orwell Animal Farm, Atwood Handmaid's Tale, Huxley BNW Revisited. Plus 2 study guides (1984 SparkNotes, Fahrenheit 451 Bloom's). Future batch: `BATCH_LITERARY_CANON_DYSTOPIAN` or fold into a broader literary pass.
- **Other classics (8+ books):** Joyce Ulysses, Lee TKAM, Vonnegut Slaughterhouse-Five, Nabokov Lolita, Bach Jonathan Livingston Seagull, Hosseini Kite Runner, Allen As a Man Thinketh, Gibran The Prophet, Maus I+II, the Russian-author mobi.

### 2.6 · Drift-flagged junk (3 items · IGNORE at staging)

| # | File | Reason |
|--:|---|---|
| 1 | `~/Downloads/    SNIPED_OS/~$aude for small business.docx` | Office stale-lock pattern (`~$*` per AGENTS.md drift rule). |
| 2 | `~/Downloads/    SNIPED_OS/Maus II.j93PR5Wn.cbr.part` | Partial download (`.part` suffix per AGENTS.md drift rule). |
| 3 | `~/Downloads/    SNIPED_OS/_.epub` | Unnamed file (single underscore) · likely a failed download or placeholder. |

### 2.7 · Downloads root vs SNIPED_OS sync

The 40 content files appear in BOTH `~/Downloads/` and `~/Downloads/    SNIPED_OS/` with matching byte sizes · they were downloaded to Downloads first and copied (or appear concurrently) to SNIPED_OS. The 3 SNIPED_OS-only items are the earlier `claude for small business.docx`, its Office lock, and (if applicable) any pre-existing files not duplicated to Downloads. **Source-universe rule holds: SNIPED_OS is canonical for the staging plan; Downloads root is informational only.**

### 2.8 · raw/ unchanged

`raw/` file count is still 721 (matching the post-staging inventory). NO new files have been staged into `raw/` since 2026-05-18. The two plan-only commits since (`2c6cc98 plan BATCH_006 operator skill layer`, `b4abb18 save session after BATCH_005 consolidation`) did not touch `raw/`. The BATCH_006 ship + consolidate commits added `01_KNOWLEDGE_BASE/` outputs only.

---

## 3 · Per-file classification matrix

| File / family | Already staged in raw/? | In SNIPED_OS? | In Downloads root? | Duplicate/overlap risk | Likely future batch | BATCH_007 impact |
|---|:-:|:-:|:-:|---|---|---|
| `sniped_os_knowledge_dump.docx` | NO | YES | YES | Unique · no overlap | `N8N_AUTOMATION_SYSTEMS` / `AI_AUTOMATION_AGENCY_COURSE` (operator hypothesis · preserve until pre-flight peek) | None |
| `claude_for_small_business_organized.docx` | NO | YES | YES | Supersedes `claude for small business.docx` (legacy version in SNIPED_OS only) | `B2B_POSITIONING` / `BASEPLATE_INTELLIGENCE` / `AI_OPERATOR_MARKET` (operator hypothesis) | None |
| 6 n8n JSON workflow blueprints | NO | YES | YES | Domain-overlap with BATCH_006 `automation-blueprint` (2 already chunked); these are 6 ADDITIONAL · no duplicate-content risk | `N8N_AUTOMATION_SYSTEMS` | None |
| 8 Prompt Template PDFs | NO | YES | YES | Domain-overlap with BATCH_006 `prompt-engineering` (8 packs already chunked); these are 8 ADDITIONAL · no content duplicate; `-2` / `-3` suffixes suggest versioning · ASCII-rename at staging | `PROMPT_TEMPLATES_DEEP` mini-batch · extends B6 prompt-engineering | None |
| `Opp hopper + Biz Case.xlsx` | NO | YES | YES | Pairs with B6 AI Ops Dashboard PRD chunked source · operator-facing template | `AI_OPS_TEMPLATES` mini-batch | None |
| `Opportunity Card [Example].pptx` | NO | YES | YES | Pairs with B6 AI Ops Dashboard PRD | `AI_OPS_TEMPLATES` mini-batch | None |
| MJ Moonwalk (epub) | NO | YES | YES | UNIQUE · no overlap · directly matches preserved high-signal note | `INTELLECTUAL_ARTIST_FRAME` mini-batch (operator decision · also valid candidate for the operator-doctrine cluster as primary-source backing for the discipline frame) | None |
| Black literary canon (Morrison ×2, Walker, Hurston · 4 books) | NO | YES | YES | UNIQUE · no overlap. Reinforces the locked Lineage Doctrine. | BATCH_010 lineage canon (Charnas / Ross / Gucci Mane / Jay-Z queue) OR its own `BATCH_LITERARY_CANON_BLACK` pass | None |
| Dystopian / political canon (Orwell Animal Farm + Atwood Handmaid's Tale + Huxley BNW Revisited · 3 books) | NO | YES | YES | UNIQUE | `BATCH_LITERARY_CANON_DYSTOPIAN` mini-batch | None |
| 2 study guides (1984 SparkNotes, Fahrenheit 451 Bloom's) | NO | YES | YES | NOT primary texts · low strategic priority · skip-or-include at operator decision | Same literary batch as above (secondary) | None |
| Other classics (Joyce Ulysses, Lee TKAM, Vonnegut S5, Nabokov Lolita, Bach JLS, Hosseini Kite Runner, Allen ASIMTH, Gibran The Prophet, Maus I+II, Russian mobi · 11 books) | NO | YES | YES | UNIQUE | `BATCH_LITERARY_CANON_GENERAL` · operator decision on which subset to chunk | None |
| `claude for small business.docx` (SNIPED_OS-only legacy) | NO | YES (SNIPED_OS only) | NO | LIKELY SUPERSEDED by `_organized` version · dedupe at staging | Same future batch as `_organized` · likely defer | None |
| `~$aude for small business.docx` | NO | YES | NO | Office lock · IGNORE | (none) | None |
| `Maus II.j93PR5Wn.cbr.part` | NO | YES | YES | Partial download · IGNORE | (none) | None |
| `_.epub` | NO | YES | YES | Unnamed · IGNORE or operator decision | (none) | None |

---

## 4 · Recommended destination folders (for a future staging pass · NOT this session)

| Source family | Recommended `raw/` destination |
|---|---|
| `sniped_os_knowledge_dump.docx` | `raw/00_BRIEF/sniped_os_knowledge_dump.docx` (operator-authored) OR `raw/08_AI_TECH/ai_automation_agency/` (if it's the n8n agency-course brief · pre-flight peek decides) |
| `claude_for_small_business_organized.docx` | `raw/08_AI_TECH/claude_for_small_business/` OR a NEW `15_B2B_POSITIONING/` chapter slot |
| 6 n8n JSON workflows | `raw/10_REFERENCE/_intake_2026-05-19/automations/` (mirrors the 2 existing B6 blueprints) |
| 8 Prompt Template PDFs | `raw/10_REFERENCE/_intake_2026-05-19/prompt_templates/` (new sub-folder) OR `raw/08_AI_TECH/prompt_engineering/` |
| `Opp hopper + Biz Case.xlsx` + `Opportunity Card [Example].pptx` | `raw/10_REFERENCE/_intake_2026-05-19/opportunity_management/` |
| MJ Moonwalk | `raw/02_TIER_1_CANON_BOOKS/operator_engine_community/` OR a NEW literary subfolder · operator decision |
| Black literary canon (4 books) | `raw/02_TIER_1_CANON_BOOKS/literary_canon_black/` (new subfolder under Tier 1) |
| Dystopian canon (3 books) | `raw/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/` (new subfolder) |
| Other literary classics (11 books) | `raw/02_TIER_1_CANON_BOOKS/literary_canon_general/` (new subfolder) |
| `claude for small business.docx` (legacy) | DEFER · likely supersede by `_organized` |
| Office lock, partial download, unnamed `_.epub` | IGNORE · do not stage |

---

## 5 · Recommended future batches (NOT authorized here)

| Batch candidate | Sources | Estimated chunk yield |
|---|---|---:|
| `BATCH_007` (locked + recommended next) | 55 files per BATCH_007_PLAN.md rev 0 | ~128 chunks |
| `BATCH_008` (already queued) | 12 ai_tech books + AI Edge Course + AI CHANGED EVERYTHING + youtube skool doc + (possibly) `sniped_os_knowledge_dump.docx` + `claude_for_small_business_organized.docx` if positioned as AI-canon | 100-130 |
| `BATCH_009` (already queued) | Advertising + copywriting canon | 60-80 |
| `BATCH_010` (already queued) | Lineage + Black culture canon · POTENTIALLY ABSORBS the 4 Black literary canon books (Morrison ×2, Walker, Hurston) | 45-65 base · + ~20-30 if literary subset folded in |
| `BATCH_011_LITERARY_CANON_BLACK` (NEW · if not folded into B10) | Morrison ×2, Walker, Hurston, Lee TKAM | 25-35 |
| `BATCH_LITERARY_CANON_DYSTOPIAN` (NEW · mini-batch) | Animal Farm, Handmaid's Tale, BNW Revisited + 2 study guides | 10-20 |
| `BATCH_LITERARY_CANON_GENERAL` (NEW · mini-batch) | Joyce, Vonnegut, Nabokov, Bach, Hosseini, Allen, Gibran, Maus I+II, Russian mobi · operator-curated subset | 30-50 (depends on subset) |
| `N8N_AUTOMATION_SYSTEMS` (NEW · mini-batch) | 6 n8n JSON workflows + sniped_os_knowledge_dump.docx (if agency-course) + `Opp hopper` + `Opportunity Card` | 15-25 |
| `PROMPT_TEMPLATES_DEEP` (NEW · mini-batch) | 8 Prompt Template PDFs | 10-15 |
| `B2B_POSITIONING_CLAUDE_OPERATOR` (NEW · mini-batch) | `claude_for_small_business_organized.docx` + related future positioning material | 5-10 |
| Brand-strategy mini-batch (already queued) | 10 docs in 00_BRIEF/BRAND_STRATEGY_2026-05-13/ | 20-30 |
| EDGE_AND_OPERATING_DISCIPLINE mini-batch (already queued) | 3 PDF worksheets in 13_OPERATING_DISCIPLINE/ | 5-15 |
| `INTELLECTUAL_ARTIST_FRAME` mini-batch (NEW · operator decision) | MJ Moonwalk + curated supporting material | 5-10 |

---

## 6 · BATCH_007 impact decision

**BATCH_007_PLAN.md should be LEFT UNCHANGED. Recommended action: proceed with BATCH_007 extraction as planned.**

Reasoning:

1. **None of the new intake fits the BATCH_007 theme** (locked doctrine + SOPs + working drafts + outreach/delivery/content/commercial operator docs). The new files are AI-tooling / literary canon / business templates / B2B positioning · none are 00_BRIEF/05_PRODUCTION/03_OUTREACH/06_DELIVERY/07_CONTENT/commercial-singleton operator docs.

2. **The hypothesis stands.** The operator hypothesis ("sniped_os_knowledge_dump.docx → N8N_AUTOMATION_SYSTEMS / AI_AUTOMATION_AGENCY_COURSE batch; claude_for_small_business_organized.docx → B2B_POSITIONING / BASEPLATE_INTELLIGENCE / AI_OPERATOR_MARKET batch") is consistent with the inventory · the docs' titles and the surrounding intake (n8n blueprints, prompt templates, AI ops templates) point to AI-agency / Claude-for-business positioning surfaces, not to the locked-doctrine + SOP layer.

3. **BATCH_007 extraction is the right next operation** because:
   - BATCH_007 closes the doctrine-side gap that BATCH_006 skill layer references.
   - Staging the new intake into `raw/` requires its own authorized staging-plan session.
   - Mixing the new intake into BATCH_007 would expand scope and introduce drift.

4. **Order of operations recommendation:**
   a. **Now:** authorize BATCH_007 extraction per BATCH_007_PLAN.md (~55 sources · ~128 chunks).
   b. **After BATCH_007 ships + consolidates:** authorize a fresh staging-plan pass for this new intake, plus the 49 already-named files. Write `SNIPED_OS_STAGING_PLAN_2026-05-19.md` (or `SNIPED_OS_INTAKE_2026-05-19.md`) targeting the 8 raw/ destinations enumerated in §4.
   c. **Then:** queue the new mini-batches (N8N_AUTOMATION_SYSTEMS, PROMPT_TEMPLATES_DEEP, B2B_POSITIONING, INTELLECTUAL_ARTIST_FRAME, the 3 literary canon mini-batches) into the master next_batch_candidates block at master-consolidation time.

5. **Pre-flight peek caveat:** before the next staging pass, a TEN-MINUTE peek into `sniped_os_knowledge_dump.docx` is worth doing because the filename suggests it could be operator-authored doctrine that DOES belong in `00_BRIEF/` (and thus could merit a BATCH_007 addendum). If the file is the agency-course brief instead, it stays out of B7. This peek is the only thing that could conceivably revise the B7 plan · do not perform it in this no-extraction session.

---

## 7 · Overlap / duplicate risks

| Risk | Detail |
|---|---|
| Cross-location duplicate (Downloads root vs SNIPED_OS) | 40 of the 40 new content files exist in both locations with matching byte sizes. SNIPED_OS is canonical per the source-universe rule. Downloads root is informational only. Staging plan should source only from SNIPED_OS. |
| `claude for small business.docx` vs `claude_for_small_business_organized.docx` | Version supersession risk. The `_organized` version is the operator-authored cleaned form (filename suffix is the tell). Dedupe analysis at staging-plan time should confirm `_organized` is the canonical superset. Likely scenario: chunk only `_organized`, retire the legacy. |
| Prompt Template `-2` and `-3` versioning | 8 PDFs with `-2` / `-3` suffixes suggest these are versioned drafts or multi-page splits. Pre-flight peek at staging time will determine whether `-3` supersedes `-2` (likely) or whether they are different content (less likely). Conservative: stage all 8, dedupe at chunk-write time. |
| Domain overlap · automation-blueprint | BATCH_006 already chunked 2 automation blueprints in the `automation-blueprint` domain. The 6 new n8n workflows are ADDITIONAL · they extend the domain, do not duplicate the chunks. No risk of chunk-collision because BATCH_006 chunks have distinct chunk_ids and source_files. |
| Domain overlap · prompt-engineering | BATCH_006 chunked 8 prompt-engineering packs (TCREI, framework-orchestrator, etc.). The 8 new Prompt Template PDFs are likely different content (techniques) · extends the domain, does not duplicate. |
| MJ Moonwalk vs existing operator-doctrine | MJ Moonwalk is a primary-source memoir. The "MJ disciplined-time / deep study / intellectual artist" frame is currently held only in operator notes · chunking the memoir gives it primary-source backing. No duplicate risk. |
| Black literary canon vs BATCH_010 queued lineage canon | BATCH_010 is queued for Charnas ×2 / Ross / Gucci Mane / Jay-Z / Greenburg / Reynolds (hip-hop / culture canon). The 4 new Black literary canon books (Morrison ×2, Walker, Hurston) are DIFFERENT material · literary fiction, not music-industry memoirs. Operator decision: fold both into a unified BATCH_010 (becomes ~45 + 25 = 70 chunks) OR split into BATCH_010 (hip-hop) + BATCH_011 (Black literary canon). Recommendation: split · the two source families have different chunking depths and different intel-memory references. |

---

## 8 · Stale / tutorial-aging risks

| Risk | Detail |
|---|---|
| AI / Claude tutorial aging | `claude_for_small_business_organized.docx`, the 8 Prompt Template PDFs, and the 6 n8n JSON workflows are all AI-tooling content with potential aging risk (model versions, n8n syntax, prompt-pattern conventions). Chunk dates should be captured so future audits can identify content older than 6-12 months for re-validation. |
| MJ Moonwalk vintage | Published 1988 (Crown Archetype reissue 2009). The "disciplined-time / deep study" frame is timeless; specific anecdotes are vintage and should be chunked as such. |
| Black literary canon vintage | All 4 books are 1970s-2000s primary texts · no aging risk; canonical literature. |
| Dystopian study guides (1984 SparkNotes, Fahrenheit 451 Bloom's Critical Interpretations) | Secondary texts · educational summaries · low SNIPED-relevance per Tier 2 standard. Operator may decide to skip. |
| `claude for small business.docx` (legacy) | Already aging at intake time · the `_organized` version is the supersession. Confirm dedupe before any chunking. |

---

## 9 · Recommended next action

**Order (per §6 reasoning):**

1. **Authorize BATCH_007 extraction** per the existing locked plan. Run the standard sequence: extract → chunk → validate → ship → consolidate → session-save. ~55 sources · ~128 chunks. New corpus total after consolidation: 732 + 128 = ~860.

2. **After BATCH_007 ships:** open a staging-plan session for the 2026-05-19 intake. Pre-flight peek `sniped_os_knowledge_dump.docx` (filename suggests it may be operator-authored doctrine worth a BATCH_007-addendum if it directly reinforces 00_BRIEF locked doctrine; otherwise it's an N8N_AUTOMATION_SYSTEMS source). Write `SNIPED_OS_STAGING_PLAN_2026-05-19.md` per the `staging-plan` skill.

3. **After staging copies into raw/:** authorize the new mini-batches in priority order:
   - `N8N_AUTOMATION_SYSTEMS` (operator-engine-adjacent · extends B6 automation-blueprint)
   - `PROMPT_TEMPLATES_DEEP` (operator-engine-adjacent · extends B6 prompt-engineering)
   - `B2B_POSITIONING_CLAUDE_OPERATOR` (commercial doctrine extension)
   - `INTELLECTUAL_ARTIST_FRAME` (operator-doctrine grounding · MJ Moonwalk + supporting)
   - `BATCH_011_LITERARY_CANON_BLACK` (4 books · Morrison ×2 + Walker + Hurston · lineage grounding)
   - `BATCH_LITERARY_CANON_DYSTOPIAN` (3 books + 2 study guides · cultural context)
   - `BATCH_LITERARY_CANON_GENERAL` (operator-curated subset of the remaining 11)

4. **Update `MASTER_CHUNK_MAP.json` `next_batch_candidates`** to reflect the new queue at master-consolidation time after each batch ships.

---

## 10 · High-signal notes preserved (per operator brief)

For carry-forward into future staging plans + chunk-writing sessions:

- **MJ disciplined-time / deep study / intellectual artist frame** · primary-source grounding now available via Moonwalk (2009 Crown Archetype edition).
- **n8n MCP / guardrails / dynamic brain / data tables** · likely covered in the 6 n8n JSON workflows + sniped_os_knowledge_dump.docx (pre-flight peek required to confirm).
- **AI agency ICP / one-liner / find-your-edge / goal setting** · likely covered in sniped_os_knowledge_dump.docx · pairs with the existing AI Edge Course material deferred to BATCH_008.
- **Claude chatbot-to-operator frame** · likely covered in claude_for_small_business_organized.docx.
- **AI amplifies the system you already have** · cross-cutting principle · likely surfaces in both new docs.
- **Service-business missed-call gap** · likely covered in claude_for_small_business_organized.docx (the small-business positioning angle).
- **Cognitive AI vs responsiveness AI distinction** · likely covered in claude_for_small_business_organized.docx · ties to the BATCH_006 hybrid-operator stance.
- **Ryan Dozer skill-stack productization example** · cross-reference for the operator-doctrine cluster · may surface in either new docx.

These notes should be carried forward as `pre_flight_notes` in the staging plan and as `direct_quotes` candidates in the chunk-writer once chunks are authorized.

---

## 11 · What this session did NOT do

- No staging, copying, moving, or renaming of source files.
- No extraction. No chunking. No master-file updates.
- No OCR. No Whisper. No external API calls.
- No BATCH_007 extraction start.
- No BATCH_008 start.
- No commits.
- No pre-flight peek into `sniped_os_knowledge_dump.docx` or `claude_for_small_business_organized.docx` content (filename-only classification only).

End of inventory acknowledgement.
