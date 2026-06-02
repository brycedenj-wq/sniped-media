# NON-BOOK DOCS COMPLETION AUDIT · docs/files beyond books · 2026-05-24

**Purpose:** a read-only audit of the NON-BOOK files (docx / md / txt / csv / xlsx / pptx / html and other non-book assets) in `raw/` and the original source universe, so BJ knows what remains beyond the book canon. Companion to ORIGINAL_SOURCE_COMPLETION_AUDIT (which covered book-format files). **No extraction-for-chunking, chunking, consolidation, master-file change, or raw mutation was performed. The Bible was not touched. No lane was started.**

## 0. Current corpus state (verified live)

- **Head commit:** `7515e58 save session after LITERARY_RECOVERY consolidation`
- **Working tree:** clean before this audit.
- **Total official chunks:** 1,531 · 10 numbered batches + 25 mini-batches · 62 official domains (75 combined keys).
- **All RECOVERY_STAGING_PASS recovered sources processed** (5 recovery lanes complete).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted.

## 1. Methodology + uncertainty (read before trusting any number)

This audit is **more uncertain than the book audit** for one structural reason: most non-book files are **SNIPED-authored md/docx**, which lack clean author/title metadata, so "is this file chunked?" cannot be settled by title-matching the way books can. A heuristic token-match was run and is **unreliable** (generic tokens like "stack", "brand", "claude", "lighting" produce false-positive matches; it reported ~353/378 "likely represented," which over-counts). Therefore:

- **Verified facts** (exact filename checks, folder counts, specific named-item lookups) are reported as PASS/confirmed.
- **Bulk processed-vs-unprocessed for SNIPED-authored md/docx is reported at the category level** (which folders are knowledge-sources that fed batches vs operational/tooling files that are not corpus material), carrying forward the prior audits' category-level classification, and is explicitly labelled an estimate.
- A large share of non-book files are **operational / working / tooling files, not knowledge sources at all** (outreach campaigns, contracts, CRM, website build files, SKILL.md tooling, session logs, media assets). These are classified out-of-scope, NOT "staged-not-processed."

## 2. raw/ non-book inventory (live · 456 non-book files)

Excluding book formats (pdf/epub/mobi/azw3/djvu/cbr/lit) and `.DS_Store`:

| Extension | Count | Nature |
|---|---:|---|
| md | 285 | SNIPED-authored OS docs, skills, briefs, SOPs, art-series studies, web/copy refs |
| docx | 93 | SNIPED-authored playbooks, Stack docs, brand/identity docs, deferred docs |
| png | 37 | image assets (production) · not corpus |
| mp4 | 8 | video assets · not corpus |
| json | 8 | n8n automation flows (chunked in N8N mini-batch) + config |
| xmp | 7 | Lightroom presets · not corpus |
| csv | 5 | website-design data tables · not corpus |
| sh | 3 | shell scripts · not corpus |
| zip | 2 | archives · not corpus |
| xlsx | 2 | CRM + opportunity hopper · not corpus |
| txt | 2 | Abloh lecture transcript + a Lencioni extraction note |
| py | 2 | website scanner scripts · not corpus |
| pptx | 1 | opportunity-card example · not corpus |
| html | 1 | intake artifact · not corpus |

**Doc-type subtotal (docx + md + txt = the knowledge-relevant non-book set):** 380 files.

**docx by folder:** raw root 59 · 99_VAULT 16 · 10_REFERENCE 7 · 08_AI_TECH 4 · 03_OUTREACH 3 · 09_ART_SERIES 1 · 07_CONTENT 1 · 05_AI_EDGE_COURSE 1 · 02_TIER_1 1.
**md by folder (top):** _skills 51 · Claude_AI_Skills_50_Upload_Ready 50 · 03_OUTREACH 39 · 00_BRIEF 34 · raw root 23 · 09_ART_SERIES 18 · 10_REFERENCE 16 · 05_PRODUCTION 15 · 14_WEB 14 · 06_DELIVERY 11 · 07_CONTENT 7 · 02_CONTRACTS 3 · (others 4).

## 3. Original source universe non-book counts (DOWNLOADS_INVENTORY_2026-05-18.txt)

| Extension | Original universe | Current raw/ | Note |
|---|---:|---:|---|
| docx | 563 | 93 | original grab held ~6x the docx; the difference is duplicate/scratch/superseded working copies + operational files not staged |
| md | 84 | 285 | raw/ has MORE md than the original (md were authored/expanded inside the repo after staging) |
| txt | 9 | 2 | |
| csv | 40 | 5 | mostly operational |
| xlsx | 51 | 2 | mostly operational spreadsheets not staged |
| html | 15 | 1 | |
| json | 8 | 8 | |
| (media) | jpg 394 · png 257 · heic 162 · dng 150 · tif 88 · mp4 73 · mov 11 | small subset | photography assets · not corpus |

**Reading:** the original universe was docx-heavy (563) and media-heavy; `raw/` is a curated subset where the un-staged docx are overwhelmingly duplicate/scratch/superseded working copies and operational files, not distinct knowledge sources. The md count grew in-repo (authoring), so md is not a "staging gap." This cannot be reconciled file-by-file with confidence (no clean titles); reported as a directional gap only.

## 4. Already-canonical non-book sources (verified / category-level)

- **high_level_convos.docx** (`07_CONTENT/`) · **CHUNKED** in HIGH_LEVEL_CONVOS (verified · appears as source in the jsonl). ✓
- **The Abloh public lecture transcript** (`10_REFERENCE/photography_scans/...Virgil-Abloh...English.txt`) · **represented via BATCH_005** (Abloh primary source · "abloh" appears in BATCH_005_CHUNKS.jsonl). ✓
- **The SNIPED-OS "Stack" docs** (The_Offer_Stack, The_Revenue_Stack, The_Production_Stack, The_Platform_Stack, The_Outbound_Stack, The_Copywriting_Stack, The_Attention_Stack, The_Adobe_Stack_Manual) · chunked in the SNIPED-OS depth batches (BATCH_001/004 · e.g., "The Offer Stack · Parts VIII-XIII" is an official source_title). Category-level confirmed.
- **The art-series studies** (`Art_Series_*.md`, `Study_*.md`, `09_ART_SERIES/`, Art_Series.docx) · fed BATCH_005 photography canon. Category-level confirmed.
- **The AI-Edge mini-batch sources** (n8n JSON flows, prompt-template PDFs, 88 Laws, B2B/OMT docs) · chunked in N8N_AUTOMATION_SYSTEMS / PROMPT_TEMPLATES_DEEP / PERSONAL_OPERATING_CODE / B2B_POSITIONING / OPPORTUNITY_MANAGEMENT. Confirmed by prior audits.
- **The Claude operating docs** (Claude_Operating_Manual, claude cowork genius, ai after ramon, The_Claude_Stack) · chunked in CLAUDE_OPERATOR_DOCS. Confirmed by prior audits.

**Estimate:** the large majority of the knowledge-bearing md/docx (Stack docs, art-series, playbooks, AI-Edge artifacts, Claude docs) are already canonical via the SNIPED-OS depth batches and the AI-Edge / operator mini-batches. Exact per-file confirmation is not cleanly verifiable (see §1).

## 5. Anchor-only

- **CURRENT_OPERATOR_REALITY_BRIEF.md** (`00_COMMAND_CENTER/`) · the read-first current-state anchor · referenced in chunks' `sniped_relevance` but **NOT itself a chunked source** (0 as source_file). By design.

## 6. Plan-only / not extracted (identity-side · held)

- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_PLAN.md** (`00_COMMAND_CENTER/`) · plan-only · 0 chunks as source_file. Its principle-only ship is held until BJ writes the fresh current SNIPED brief.
- **`00_BRIEF/BRAND_STRATEGY_2026-05-13/` (10 md docs)** · the SNIPED-authored brand-strategy set (BRIEF, AUDIT, NAMING_CRITERIA, NAMING_CANDIDATES, NAME_RECOMMENDATION, BRAND_ARCHITECTURE, POSITIONING_STATEMENT, BRAND_VOICE, VISUAL_IDENTITY_BRIEF, MIGRATION_PLAN). This is **identity-side material** tied to the held optionality lane. **Held / not chunked** · should stay decision-neutral under the optionality guardrails (it predates and is superseded-in-spirit by CURRENT_OPERATOR_REALITY_BRIEF). Needs an operator decision, not auto-processing.

## 7. Staged-not-processed (knowledge docs · deferred · the real non-book backlog)

The 5 deferred docx flagged in prior audits, all confirmed present in `raw/` root:
- **The_Operator_Playbook.docx** → content/distribution lane candidate.
- **GaryVee_Attention_Operating_System.docx** → content/distribution lane candidate.
- **Business_Operations_Playbook.docx** → business-ops/legal/finance lane candidate.
- **Money_Wealth_Getting_Ahead.docx** → money/ownership lane candidate (capital-adjacent).
- **sniped_context_tools_only.docx** → SNIPED-context (likely overlaps the already-chunked SNIPED OS Knowledge Dump · verify before processing).

Plus the **2 optional salvage scrapes** (held, low priority): `astro claude websites 3x faster.docx` (10_REFERENCE/_intake_2026-05-18/) and `MORE CLAUDE 5.docx` (99_VAULT/_intake_archive_2026-05-12/).

This is a small (~5-7 file) optional doc backlog, not a large lane.

## 8. Source-universe-not-staged

- The original universe held **563 docx vs raw/'s 93**. The ~470 un-staged docx are, by inspection of the curated `raw/`, overwhelmingly **duplicate / scratch / superseded working copies and operational files** (the curated mirror deliberately dropped them). **No confirmed distinct knowledge-source docx is known to be missing from raw/** (cannot be proven file-by-file without clean titles; reported as a directional gap with low expected knowledge value).
- xlsx (51 → 2) and csv (40 → 5): operational spreadsheets/data, intentionally not staged.

## 9. Needs-review

- **14_WEB (23 files · website-design / website-copy / website-seo md + reference md + csv data + py scripts)** · SNIPED-authored website build kit. Likely operational (a build asset), but could seed a small website-content lane if BJ wants the corpus to hold his web copy/SEO doctrine. Operator decision.
- **A few loose photography docx** (POSING 101 OG, MOODBOARDING DOC OG, LA PHOTOGRAPHY, `99_VAULT/.../photoshop .docx`, `threads photogrpahers.docx`) · may or may not have been folded into the BATCH_005/006/007 photography depth · low knowledge-delta · review only if a photography-doc gap is suspected.
- **The Abloh lecture .txt** · represented via BATCH_005 (above) but as a primary-source mention, not necessarily a full transcript chunking · review only if deeper Abloh coverage is wanted.

## 10. Low-value skip / out-of-scope (operational · tooling · media · NOT corpus sources)

- **Operator tooling SKILL.md:** `_skills/` (51 md) + `Claude_AI_Skills_50_Upload_Ready (1)/` (50 md) · these are Claude-skill definitions (operator tooling), not knowledge sources. Skill *names* appear inside some chunks as references, but the SKILL.md files are not corpus material.
- **Operational SOPs / working docs:** `03_OUTREACH/` (39 md · campaigns, SOPs, reply scripts, sent-DM logs), `02_CONTRACTS/` (3 md · collab agreement, MSAs), `06_DELIVERY/` (11 md · pixieset config, post-delivery SOP), `01_OFFERS/`, `04_CRM/`, `05_PRODUCTION/` (catalogs, presets), session logs, `_inbox/admin/`, READMEs, `INDEX.md`, `ACTIVE_THREADS.md`.
- **Operational data/media:** `SNIPED CRM.xlsx`, the opportunity hopper xlsx + pptx, 14_WEB csv data, 37 png, 8 mp4, 7 xmp (Lightroom presets), shell/py scripts, zips, the intake html.

These are correctly NOT chunked; they are operating-system / production files, not knowledge corpus.

## 11. Specific item-7 checks (verified)

| Item | Finding |
|---|---|
| CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources | PLAN doc only (00_COMMAND_CENTER) · plan-only · 0 as source_file. The `00_BRIEF/BRAND_STRATEGY_2026-05-13/` (10 md) is the related identity-side set · held, not chunked. |
| SNIPED / SNIPED Media docs | The Stack docs + playbooks + brand docs · the knowledge ones are chunked (B001/004); the operational ones are out-of-scope; the brand-strategy set is held. |
| website / business docs | `14_WEB` (23 files) · website build kit · needs-review / likely operational. |
| photography workflow docs | LIGHTING SET UPS, LOCATION SCOUTING, POSING 101, MOODBOARDING, Photography_Editing/Revenue_Playbook, Pixieset/Evoto refs · fed BATCH_005/006/007 photography depth (category-level); a few loose ones in needs-review. |
| transcripts | high_level_convos.docx (chunked · HIGH_LEVEL_CONVOS); the Abloh lecture .txt (represented via BATCH_005). No other transcript corpus pending. |
| planning / housing / engineering docs | **NONE found.** No civic-planning, housing, urban-planning, field-engineering, or data-center knowledge docs exist in raw/ (the "engineering/Higgsfield" name matches are the Higgsfield AI-video tool + a SNIPED network/community md, not civic/engineering material). **Gap vs CURRENT_OPERATOR_REALITY_BRIEF's hypothesis space** (AI for field engineers / data-center teams, planning/housing/community intelligence): the corpus holds no primary material in those domains. |
| uploaded legal/company docs | Contracts_Legal_Protection_Playbook.docx + "legal contracts and service business contracts.docx" (raw root · part of the Business_Operations deferred family) + `02_CONTRACTS/` operational md (out-of-scope). No incorporation/LLC/company-formation filings present. |
| Bible / spiritual files | **NONE in raw/** (verified · §12). |

## 12. Bible status

**The KJV Bible remains OUTSIDE `raw/`, UNCHUNKED, held as a reverent SPIRITUAL_FOUNDATION anchor/reference in the source universe** per NEW_SOURCE_INTAKE_PLAN. Verified: no `*bible*` / `*king*james*` / `*scripture*` / `*spiritual*` file in `raw/`, and 0 Bible matches in any `*_CHUNKS.jsonl`. No faith/spiritual lane exists or was created.

## 13. Identity optionality status

ACTIVE and unchanged. No lane finalizes SNIPED / SNIPED Media / BASEPLATE direction. CURRENT_OPERATOR_REALITY_BRIEF is the read-first anchor (not chunked); CURRENT_IDENTITY_AND_BRAND_OPTIONALITY is plan-only / not extracted; the `00_BRIEF/BRAND_STRATEGY_2026-05-13/` set is held and decision-neutral. No non-book doc was processed in this audit.

## 14. Recommended next action (operator decision · none started)

The non-book picture is reassuring: the **knowledge-bearing** non-book docs are largely already canonical (Stack docs, art-series, playbooks, AI-Edge artifacts, Claude docs, high_level_convos), and the remainder is mostly **operational/tooling/media that should NOT be chunked**. The genuine non-book backlog is small (the 5 deferred docx + 2 scrapes) and optional.

Therefore a large "non-book docs intake/staging" lane is **NOT** the highest-value next move. Recommended priority:

1. **Historical-biography lane (Grant + Washington · Chernow)** · clean staged books, the most coherent remaining high-value book lane.
2. **Classical strategy / decision / operating-founder canon** · the largest remaining high-value book backlog.
3. **(Optional, small) operator-docs cleanup mini-batch** · the 5 deferred docx (Operator_Playbook, GaryVee, Business_Operations_Playbook, Money_Wealth_Getting_Ahead, sniped_context_tools) + the 2 scrapes · only if BJ wants them in-corpus; verify sniped_context_tools doesn't duplicate the chunked SNIPED OS Knowledge Dump first.
4. **The identity-side track** (fresh current SNIPED brief + the held CURRENT_IDENTITY / BRAND_STRATEGY material) · operator-led, when ready · keep decision-neutral.
5. **Cleanup / skip ledger** · the operational/tooling files stay out-of-scope by design; no action needed beyond noting them.

**Honest gap flagged:** the corpus has **no field-engineering / data-center / urban-planning / housing knowledge sources**, which is the part of CURRENT_OPERATOR_REALITY_BRIEF's hypothesis space the source universe never covered. If BJ wants the OS to support those hypotheses, that material would need to be acquired new (it is not sitting un-staged in the universe).

## 15. Constraints honored by this audit

- Did NOT extract-for-chunking, chunk, consolidate, or modify master files · total_chunks stays 1,531.
- Did NOT modify any `raw/` or source file (read-only `find` / `wc` / `grep` / inventory parsing only).
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- No new domain. No next lane started.
- Wrote only this report. Em-dash clean. Not committed (operator will review first).
