# OPERATOR_DOCS_CLEANUP · plan only · 2026-05-26

**Status:** PLAN ONLY. No extraction-for-chunking, no chunking, no master-file changes, no raw mutation, no Bible touch, no new domain, no lane started. This document locates the remaining non-book / operator-authored / SNIPED-authored / Claude-authored docs in `raw/` and `00_COMMAND_CENTER/` that are not yet clearly classified, separates them into the operator's nine categories, runs an authoritative already-chunked overlap check, recommends an architecture, gives exact include/defer/exclude sets, and stops. Nothing is extracted or chunked here. This plan supersedes the deferred-docs section of the 2026-05-24 NON_BOOK_DOCS_COMPLETION_AUDIT with two corrections found live (see §3).

## 0. Verified starting state

- **Head commit:** `8a82d64 save session after EXPERTISE_CREATIVITY consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,837 (reconciled three ways · header = sum of `.batches[].chunk_count` = sum of jsonl line counts = 1,837).
- **Canonical sets:** 10 numbered batches + 47 mini-batches · 62 official domains (75 combined keys).
- **ADJACENT_TIER_2_CLUSTERS group COMPLETE** (CONSULTING_SERVICE + LEADERSHIP_MGMT + SYSTEMS_THINKING + EXPERTISE_CREATIVITY all canonical).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked (not in `raw/`, not tracked).

## 1. Scope of this pass

"Operator docs" here means the **non-book** files that are operator-authored, SNIPED-authored, or Claude-authored: the `.docx` / `.md` / `.txt` set in `raw/` (root and sub-folders) and the `00_COMMAND_CENTER/` planning/brief docs. Book-format files are out of scope (covered by ORIGINAL_SOURCE_COMPLETION_AUDIT and the closed book lanes). Photography/media binaries, spreadsheets, scripts, and web build assets are operational, not knowledge sources.

The prior audits established that the **knowledge-bearing** SNIPED docs are largely already canonical. This pass focuses on the **residual unclassified / deferred tail** and confirms the rest stays correctly out-of-scope or held.

## 2. Candidate residual docs located (verified · read-only `ls` / `stat` / word-count probes to /tmp · temp deleted · mtimes unchanged)

The genuinely-deferred-or-unclassified `.docx` at `raw/` root (read-only word probes via pandoc):

| Doc | Words (probe) | First read |
|---|--:|---|
| The_Operator_Playbook.docx | 3,522 | SNIPED operator operating doctrine |
| GaryVee_Attention_Operating_System.docx | 2,619 | attention / content operating doctrine |
| Business_Operations_Playbook.docx | 2,944 | business-ops / legal / finance operating doctrine |
| Higgsfield_AI_Operator_Playbook.docx | 1,754 | AI-video-tool (Higgsfield) implementation doc |
| sniped_context_tools_only.docx | 949 | SNIPED-context tooling summary |
| Money_Wealth_Getting_Ahead.docx | 1,687 | money/ownership notes |

The 2 optional salvage scrapes (read-only word probes):

| Scrape | Words (probe) | First read |
|---|--:|---|
| `10_REFERENCE/_intake_2026-05-18/astro claude websites 3x faster.docx` | 853,149 | massive raw web scrape (Astro / Claude site content · boilerplate-heavy) |
| `99_VAULT/_intake_archive_2026-05-12/MORE CLAUDE 5.docx` | 137,411 | large raw web/chat scrape |

The identity-side `.md` set (verified present):

- `00_COMMAND_CENTER/CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_PLAN.md` (plan-only).
- `raw/00_BRIEF/BRAND_STRATEGY_2026-05-13/` (10 md: 00_BRAND_STRATEGY_BRIEF, 01_BRAND_AUDIT, 02_NAMING_CRITERIA, 03_NAMING_CANDIDATES, 04_NAME_RECOMMENDATION, 05_BRAND_ARCHITECTURE, 06_POSITIONING_STATEMENT, 07_BRAND_VOICE, 08_VISUAL_IDENTITY_BRIEF, 09_MIGRATION_PLAN).

Plus the broad `raw/`-root SNIPED-authored set already covered by the prior audits (Stack docs, Claude docs, playbooks, photography docs, codex/tooling docs, thread dumps), classified at the category level in §4.

## 3. Already-chunked overlap check (authoritative · by source_title / source_file across all 57 jsonls)

Two live findings correct the 2026-05-24 audit's deferred list:

- **Money_Wealth_Getting_Ahead.docx is ALREADY CANONICAL.** It is chunked in MONEY_OWNERSHIP as `source_title` "Money, Wealth & Getting Ahead" / `source_file` `money_wealth_getting_ahead.txt` (4 chunks: MONEY_OWNERSHIP_017/019/020 + one more). **Remove it from the deferred list · EXCLUDE (already canonical · 0 action).**
- **The SNIPED OS Knowledge Dump is ALREADY CANONICAL.** `sniped_os_knowledge_dump.txt` is a chunked source in BATCH_008, and `sniped_os_v1_synthesis.md` in BATCH_004. **`sniped_context_tools_only.docx` (949 words) is almost certainly a redundant subset of that already-chunked SNIPED-context material** · treat as likely-duplicate · verify a true content delta before ever chunking (recommended: do not chunk).
- **Higgsfield is partially represented.** BATCH_006_036 `sniped-higgsfield-pipeline` already holds the Higgsfield workflow conceptually. `Higgsfield_AI_Operator_Playbook.docx` itself is not a chunked source, but its knowledge-delta over the existing BATCH_006 Higgsfield material is low · it is a tooling/implementation doc, not net-new doctrine.

Genuinely NOT chunked (0 source hits): The_Operator_Playbook, GaryVee_Attention_Operating_System, Business_Operations_Playbook, sniped_context_tools_only, Higgsfield_AI_Operator_Playbook (as a doc), the 2 scrapes, the BRAND_STRATEGY 10-md set, CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_PLAN.

Already canonical (verified at category level by the prior audits, re-confirmed by spot source hits): the Stack docs (The Offer/Revenue/Production/Platform/Outbound/Copywriting/Attention/Adobe Stack · BATCH_001/004), the Claude docs (Claude_Operating_Manual, claude cowork genius, ai after ramon, The_Claude_Stack · CLAUDE_OPERATOR_DOCS), the art-series / photography docs (BATCH_005/006/007), high_level_convos.docx (HIGH_LEVEL_CONVOS), the SNIPED content/video philosophy + Canonical Truths (BATCH_007), sniped_os_v1_synthesis (BATCH_004).

## 4. Classification (the operator's nine categories)

### 4a. Already canonical (EXCLUDE · 0 action · do not re-chunk)
- Stack docs (Offer/Revenue/Production/Platform/Outbound/Copywriting/Attention/Adobe) · BATCH_001/004.
- Claude docs (Claude_Operating_Manual, claude cowork genius, ai after ramon, The_Claude_Stack) · CLAUDE_OPERATOR_DOCS.
- Art-series + photography docs (Art_Series, Study_*, LIGHTING/LOCATION/POSING/MOODBOARDING, Photography_Editing/Revenue_Playbook references) · BATCH_005/006/007.
- high_level_convos.docx · HIGH_LEVEL_CONVOS. SNIPED OS Knowledge Dump + SNIPED OS v1 synthesis · BATCH_008/004. SNIPED content/video philosophy + Canonical Truths · BATCH_007.
- **Money_Wealth_Getting_Ahead.docx · MONEY_OWNERSHIP (corrected from the 2026-05-24 audit).**

### 4b. Useful but should remain held (DEFER · decision-neutral)
- SNIPED-authored playbooks that overlap the chunked Stack docs in spirit but are not net-new doctrine: Brand_Builders_Playbook, Build a Brand Like Apple, Digital_Products_AI_Services_Playbook, Copywriting_Playbook, Cold_Outreach_Sales_Pipeline_Playbook. Knowledge-delta over the canonical Stack/copy/brand corpus is low; hold rather than chunk.

### 4c. Current-state / brief material (ANCHOR · not chunked)
- `CURRENT_OPERATOR_REALITY_BRIEF.md` · the read-first current-state anchor · referenced in chunks' `sniped_relevance`, never a chunked source. Stays anchor-only.

### 4d. Identity-direction material (DEFER · identity track · do NOT chunk before the fresh SNIPED brief)
- `CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_PLAN.md` (plan-only).
- The `00_BRIEF/BRAND_STRATEGY_2026-05-13/` 10-md set (brief, audit, naming, name recommendation, architecture, positioning, voice, visual identity, migration).
- The_Direction_Shift.docx, NEW TAKEOVER HANDLE WITH CARE.docx, takeover after ramon.docx (handle/brand-transition material).

### 4e. Implementation / tooling docs (DEFER · low knowledge-delta)
- Higgsfield_AI_Operator_Playbook.docx, The_Higgsfield_Codex.docx, The_Kling_AI_Codex.docx (AI-video-tool operation · Higgsfield already conceptually in BATCH_006).
- sniped_context_tools_only.docx (likely-redundant with the chunked SNIPED OS Knowledge Dump · §3).
- sniped figma.docx, Pixieset_Operations_Reference.docx, Evoto_AI_Retouching_Reference.docx (production tooling references).

### 4f. Stale drafts (EXCLUDE · no action / optional delete in a future authorized cleanup)
- chat Sniped MAster thread.docx, Gemini Sniped MAster thread.docx (raw assistant-thread dumps).
- NEXT INFO GRABS.docx (a to-acquire scratch note).

### 4g. Out-of-scope / personal / private (EXCLUDE · not corpus)
- life story.docx (personal · do not chunk).
- Operational: `03_OUTREACH/`, `02_CONTRACTS/`, `04_CRM/`, `06_DELIVERY/`, `01_OFFERS/`, `05_PRODUCTION/` SOPs, `_skills/` + `Claude_AI_Skills_50_Upload_Ready/` (operator tooling SKILL.md), `14_WEB/` build kit, session logs, READMEs, INDEX.md, ACTIVE_THREADS.md, CRM/opportunity xlsx + pptx, png/mp4/xmp media, shell/py scripts, zips, intake html.

### 4h. Duplicate / superseded (EXCLUDE · optional delete in a future authorized cleanup)
- ai after ramon copy.docx, takeover after ramon copy.docx (the " copy" twins of already-canonical/identity docs).
- The_Claude_Stack (1).docx (the "(1)" twin of the chunked The_Claude_Stack).
- The superseded old djvu originals noted in ORIGINAL_SOURCE_COMPLETION_AUDIT §8 (Predictably Irrational, The Mailroom, Seagull · each replaced by a processed `_RECOVERED` file).

### 4i. Dangerous to chunk before the final identity decision (DEFER · the core risk flag)
- **The_Operator_Playbook.docx, GaryVee_Attention_Operating_System.docx, Business_Operations_Playbook.docx** · these encode a **specific operator/business identity** (a content/attention/media-operator posture, a service-business-operations posture). They are SNIPED-authored doctrine, not external decision-neutral knowledge.
- The BRAND_STRATEGY 10-md set and The_Direction_Shift (also 4d) are the sharpest identity-lock risk.

Chunking 4i now would bake a not-yet-decided business identity into the canonical corpus as settled doctrine, directly against CURRENT_OPERATOR_REALITY_BRIEF ("solo operator in ideation/build mode · generate options, do not prematurely commit · do not let old SNIPED Media / BASEPLATE / photography-only assumptions override current reality").

## 5. Should any doc be chunked now? (task 4)

**No. Recommend chunking nothing in this pass.** Rationale:
- The genuinely-deferred docx are either already canonical (Money_Wealth), likely-redundant (sniped_context_tools vs SNIPED OS Knowledge Dump), low knowledge-delta tooling (Higgsfield/Kling codex + playbook), or identity-locking SNIPED doctrine (Operator_Playbook, GaryVee, Business_Operations).
- The 2 scrapes are enormous raw web dumps (853K + 137K words), overwhelmingly boilerplate · not curated knowledge · chunking them would inject noise.
- The identity-side material (BRAND_STRATEGY set, CURRENT_IDENTITY plan) is explicitly held pending the fresh SNIPED brief.

There is no net-new, decision-neutral, external knowledge in this residual tail that warrants a chunk lane right now. The high-value SNIPED knowledge is already canonical.

## 6. Recommended architecture (task 5)

**Primary recommendation: a held-docs index + no-op cleanup. NOT a chunking mini-batch.**

1. **Held-docs index (recommended deliverable for a FUTURE authorized step):** write `00_COMMAND_CENTER/HELD_OPERATOR_DOCS_INDEX.md` that registers the residual docs with their classification (4a-4i above) and their disposition (canonical / held / tooling / stale / out-of-scope / dangerous-to-chunk). This makes the "what is left and why it is not chunked" decision durable on disk, so no future session re-litigates it. This index is markdown-only, chunks nothing, touches no master file.
2. **No-op cleanup for the rest:** the already-canonical (4a) and operational (4g) docs need no action. The duplicate/superseded/stale (4f, 4h) can be deleted later only under an explicit, separately-authorized cleanup pass (not part of this plan · deletion is a hard-to-reverse action and is not authorized here).
3. **Tee up the real unlock:** the genuine next move for this material is the **fresh current SNIPED brief / CURRENT_IDENTITY principle-only ship** (a separate, operator-led track). That is what unlocks 4d (and makes a later, decision-neutral, principle-only treatment of 4b/4i safe). Until then, hold.

**Why not the other menu options:**
- **Small principle-only mini-batch (now):** not advised. The candidate 4i docs are identity-locking, not decision-neutral; chunking them now violates the optionality guardrails. (A principle-only mini-batch becomes viable only AFTER the fresh SNIPED brief, and even then should extract transferable principles, not SNIPED-specific brand doctrine.)
- **Fresh SNIPED brief prep pass (now):** valuable, but that is the identity track, not "operator-docs cleanup" · recommend it as the sequenced next step (§6.3), not as this pass.
- **No-op only:** too weak on its own · the residual tail deserves the durable held-docs index so it is provably classified, not silently dropped.

## 7. Recommended include / defer / exclude set (task 6 · exact)

| Disposition | Items |
|---|---|
| **INCLUDE (chunk now)** | **NONE.** |
| **DEFER · identity track (hold until the fresh SNIPED brief)** | The_Operator_Playbook.docx, GaryVee_Attention_Operating_System.docx, Business_Operations_Playbook.docx, the `BRAND_STRATEGY_2026-05-13/` 10-md set, CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_PLAN.md, The_Direction_Shift.docx, NEW TAKEOVER HANDLE WITH CARE.docx, takeover after ramon.docx |
| **DEFER · low-priority / verify-overlap** | sniped_context_tools_only.docx (verify delta vs SNIPED OS Knowledge Dump · expect redundant), Higgsfield_AI_Operator_Playbook.docx, The_Higgsfield_Codex.docx, The_Kling_AI_Codex.docx, the 2 scrapes (curate a small extract ONLY if a specific signal is wanted · default: skip), the 4b held playbooks |
| **EXCLUDE · already canonical (0 action)** | Stack docs, Claude docs, art-series/photography docs, high_level_convos.docx, SNIPED OS Knowledge Dump + v1 synthesis, SNIPED content/video philosophy + Canonical Truths, **Money_Wealth_Getting_Ahead.docx** |
| **EXCLUDE · out-of-scope / operational / personal** | outreach / contracts / CRM / delivery / offers / production SOPs, `_skills/` + `Claude_AI_Skills_50_Upload_Ready/`, `14_WEB/` kit, session logs, READMEs, INDEX.md, ACTIVE_THREADS.md, xlsx/pptx/csv, png/mp4/xmp, scripts, zips, intake html, life story.docx |
| **EXCLUDE · stale / duplicate / superseded (optional future delete only)** | chat/Gemini Sniped MAster thread.docx, NEXT INFO GRABS.docx, ai after ramon copy.docx, takeover after ramon copy.docx, The_Claude_Stack (1).docx, the 3 superseded old djvu originals |
| **EXCLUDE always** | the KJV Bible (held SPIRITUAL_FOUNDATION anchor) |

## 8. Identity-risk notes (task 11)

These docs are the highest identity-lock risk in the entire remaining backlog, because they are SNIPED-authored operating doctrine, not external knowledge read decision-neutrally. The optionality guardrails hold and this plan preserves them:
- **No final SNIPED direction.** SNIPED is the live operator identity / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- **No forced business identity.** The Operator/Attention/Business-Operations playbooks are NOT to be treated as the decided business model.
- **No premature brand lock.** The BRAND_STRATEGY set (naming, name recommendation, migration plan) is explicitly held; it predates and is superseded-in-spirit by CURRENT_OPERATOR_REALITY_BRIEF.
- All of this material is held as a **decision-support / pattern-library / option set**, read against CURRENT_OPERATOR_REALITY_BRIEF, applied to BJ's solo build-mode stage · NOT a directive that BJ become a content operator, attention-economy creator, agency/service-business operator, or that he adopt the drafted brand name/architecture. Photography remains one option among several.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted** unless the operator explicitly authorizes it (task 10). This plan does not extract it.

## 9. Bible exclusion confirmation (task 9)

**The KJV Bible was NOT touched, staged, probed, chunked, or included in this planning pass and will NOT be in any disposition above.** It is not present in `raw/`, not tracked in git, and not a `source_title`/`source_file` in any chunk (verified · "bible" appears in chunks only as unrelated prose such as "Style Bible"). It remains a held SPIRITUAL_FOUNDATION anchor in the source universe per NEW_SOURCE_INTAKE_PLAN.

## 10. Recommended next step (operator decision · do not start without authorization)

1. **(Recommended now)** Authorize the **held-docs index** deliverable: write `00_COMMAND_CENTER/HELD_OPERATOR_DOCS_INDEX.md` registering §4's classification. Markdown-only · chunks nothing · touches no master file · keeps the residual tail provably classified.
2. **(Sequenced next · the real unlock)** The **fresh current SNIPED brief / CURRENT_IDENTITY principle-only ship** (operator-led identity track). This is what makes any later treatment of the 4d/4i material safe and decision-neutral.
3. **(Optional · later)** A separately-authorized **delete-cleanup pass** for the stale/duplicate/superseded files (4f/4h) · deletion is hard-to-reverse and is NOT authorized by this plan.
4. **(Default)** Otherwise this is a **no-op**: the corpus is correct as-is; the residual tail is held or out-of-scope by design.

The operator-docs cleanup is therefore best understood as **classify-and-hold**, not **chunk**. No high-value knowledge is lost by holding; real risk is incurred by chunking identity-locking doctrine prematurely.

## 11. Scope guards honored by this planning pass (tasks 7, 8, 12-15)

- Did NOT extract-for-chunking, chunk, consolidate, or modify master files · total_chunks stays 1,837.
- Did NOT modify any `raw/` or source file (read-only `ls` / `stat` / `find` / `grep` + pandoc word-probes to `/tmp`, temp deleted · all mtimes unchanged · Apr 15 to May 12).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT extract into knowledge-base folders.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created or proposed (if a future principle-only treatment ever runs, it would route to existing operator-doctrine / operator-process / commercial-architecture only · no new domain).
- CURRENT_IDENTITY remains plan-only / NOT extracted.
- Identity optionality guardrails preserved (no final SNIPED / SNIPED Media / BASEPLATE direction · no forced business identity · no premature brand lock).
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).
