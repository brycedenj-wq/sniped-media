# HELD_OPERATOR_DOCS_INDEX · durable classification of the residual operator-authored doc tail · 2026-05-26

**This is a durable held-docs index, NOT a chunk lane.** It is the cleanup artifact authorized from `OPERATOR_DOCS_CLEANUP_PLAN.md` (`11dc97f`). It registers, on disk, the classification and disposition of every remaining non-book / operator-authored / SNIPED-authored / Claude-authored / tooling / identity-direction doc in `raw/` and `00_COMMAND_CENTER/` so no future session re-litigates "what is left and why it is not chunked." Markdown only · it creates no `*_CHUNKS.jsonl`, no `*_extracted/` dir, touches no master file, mutates no `raw/` file, touches no Bible, and creates no domain.

## 1. Purpose

- **Durable classification** of the remaining operator-authored / SNIPED-authored / tooling / identity-direction docs, so the residual tail is provably classified rather than silently dropped.
- **Prevents accidental chunking before the identity decision.** The highest-risk docs here are SNIPED-authored operating doctrine and brand-direction material; chunking them now would bake a not-yet-decided business identity into the canonical corpus as settled doctrine, against CURRENT_OPERATOR_REALITY_BRIEF ("solo operator in ideation/build mode · generate options, do not prematurely commit").
- **Points to what unlocks each held category** (see §13 decision rules and §14 unlock conditions), so the path forward is explicit and operator-gated.

## 2. Current corpus state (verified live)

- **Latest commit:** `11dc97f plan OPERATOR_DOCS_CLEANUP`
- **Total chunks:** 1,837 (reconciled three ways · header = sum of `.batches[].chunk_count` = sum of jsonl line counts = 1,837).
- **Canonical sets:** 10 numbered batches + 47 mini-batches · 62 official domains (75 combined keys).
- **No `OPERATOR_DOCS_CLEANUP` batch exists** (0 occurrences in MASTER_CHUNK_MAP.json).
- **No held-doc mini-batch exists.** This index chunks nothing.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE. **Bible:** held / excluded / not chunked.

## 3. Classification categories (the nine buckets)

1. Already canonical (`§4`) · EXCLUDE · 0 action · do not re-chunk.
2. Held / useful (`§5`) · DEFER · decision-neutral · low knowledge-delta.
3. Anchor / current-state material (`§6`) · stays anchor-only.
4. Identity-direction material (`§7`) · DEFER · unlocked by the fresh SNIPED brief.
5. Identity-risk docs (`§8`) · DEFER · dangerous to chunk before the final identity decision.
6. Implementation / tooling (`§9`) · DEFER · canon only on a real build need.
7. Raw scrapes / low-value dumps (`§10`) · DEFER/EXCLUDE · narrow before any use.
8. Out-of-scope / personal / private + stale / duplicate (`§11`) · EXCLUDE · not corpus.
9. Bible (`§12`) · held separately · do not touch until an explicit SPIRITUAL_FOUNDATION decision.

## 4. Already canonical (EXCLUDE · 0 action · do not re-chunk)

These are already represented in the corpus; re-chunking would duplicate.

| Doc / set | Where it is canonical |
|---|---|
| The Stack docs (Offer / Revenue / Production / Platform / Outbound / Copywriting / Attention / Adobe Stack) | BATCH_001 / BATCH_004 |
| Claude docs (Claude_Operating_Manual, claude cowork genius, ai after ramon, The_Claude_Stack) | CLAUDE_OPERATOR_DOCS |
| Art-series + photography docs (Art_Series, Study_*, LIGHTING / LOCATION / POSING / MOODBOARDING, Photography_Editing / Revenue_Playbook references) | BATCH_005 / 006 / 007 |
| high_level_convos.docx | HIGH_LEVEL_CONVOS |
| SNIPED OS Knowledge Dump (`sniped_os_knowledge_dump.txt`) + SNIPED OS v1 synthesis (`sniped_os_v1_synthesis.md`) | BATCH_008 / BATCH_004 |
| SNIPED content/video philosophy + Canonical Truths (`content__sniped_content_philosophy.md`, `content__sniped_video_philosophy.md`, `brief__canonical_truths.md`) | BATCH_007 |
| **Money_Wealth_Getting_Ahead.docx** (`money_wealth_getting_ahead.txt` · 4 chunks · corrected from the 2026-05-24 audit) | MONEY_OWNERSHIP |
| **Higgsfield concept** (`sniped-higgsfield-pipeline`) | BATCH_006_036 (the workflow is represented; the Higgsfield playbook docx adds low delta · see §9) |

## 5. Held / useful (DEFER · decision-neutral · low knowledge-delta)

SNIPED-authored playbooks that overlap the already-canonical Stack docs in spirit but are not net-new external doctrine. Useful as future references, NOT as canon inputs:

- Brand_Builders_Playbook.docx, Build a Brand Like Apple.docx, Digital_Products_AI_Services_Playbook.docx, Copywriting_Playbook.docx, Cold_Outreach_Sales_Pipeline_Playbook.docx.

Disposition: hold. Their knowledge over the canonical Stack / copy / brand corpus is low; chunking would mostly duplicate. Revisit only if a specific gap is identified.

## 6. Anchor / current-state material (stays anchor-only · not chunked)

- **`00_COMMAND_CENTER/CURRENT_OPERATOR_REALITY_BRIEF.md`** · the read-first current-state anchor. It is referenced in chunks' `sniped_relevance` guardrail text but is NOT a chunked source (0 as `source_file`), by design. It remains the active operator context governing every lane and stays anchor-only.

## 7. Identity-direction material (DEFER · the fresh SNIPED brief is the unlock)

SNIPED-authored brand/identity-direction docs. Held and decision-neutral; NOT chunked before the fresh current SNIPED brief:

- `00_COMMAND_CENTER/CURRENT_IDENTITY_AND_BRAND_OPTIONALITY_PLAN.md` (plan-only / NOT extracted).
- `raw/00_BRIEF/BRAND_STRATEGY_2026-05-13/` (10 md: 00_BRAND_STRATEGY_BRIEF, 01_BRAND_AUDIT, 02_NAMING_CRITERIA, 03_NAMING_CANDIDATES, 04_NAME_RECOMMENDATION, 05_BRAND_ARCHITECTURE, 06_POSITIONING_STATEMENT, 07_BRAND_VOICE, 08_VISUAL_IDENTITY_BRIEF, 09_MIGRATION_PLAN).
- The_Direction_Shift.docx, NEW TAKEOVER HANDLE WITH CARE.docx, takeover after ramon.docx.

**Unlock:** the fresh current SNIPED brief. The BRAND_STRATEGY set predates and is superseded-in-spirit by CURRENT_OPERATOR_REALITY_BRIEF; it must stay decision-neutral until the operator writes the fresh brief. CURRENT_IDENTITY's principle-only ship happens only by explicit operator authorization (§14).

## 8. Identity-risk docs (DEFER · dangerous to chunk before the final identity decision)

The sharpest identity-lock risk in the entire remaining backlog. These are SNIPED-authored operating doctrine, NOT external knowledge read decision-neutrally:

- **The_Operator_Playbook.docx** (~3,522 words) · a SNIPED operator operating posture.
- **GaryVee_Attention_Operating_System.docx** (~2,619 words) · an attention / content-economy operating posture.
- **Business_Operations_Playbook.docx** (~2,944 words) · a service-business-operations / legal / finance posture.

**Why dangerous to chunk now:** each encodes a *specific operator/business identity*. Chunking them would canonicalize a not-yet-decided business model as settled doctrine, directly against CURRENT_OPERATOR_REALITY_BRIEF ("do not let old SNIPED Media / BASEPLATE / photography-only assumptions override current reality · generate options, do not prematurely commit"). They are held as an *option set / pattern library*, never as a directive that BJ become a content operator, attention-economy creator, or service-business/agency operator.

**Unlock:** the fresh SNIPED brief. Even then, any treatment should extract transferable principles routed to existing domains (operator-doctrine / operator-process / commercial-architecture), never SNIPED-specific brand doctrine, and never a new domain.

## 9. Implementation / tooling (DEFER · canon only on a real build need)

Tool-operation and production-tooling references with low knowledge-delta. Classify as implementation/tooling, NOT canon, unless a specific build need appears:

- Higgsfield_AI_Operator_Playbook.docx, The_Higgsfield_Codex.docx, The_Kling_AI_Codex.docx (AI-video-tool operation · the Higgsfield workflow is already conceptually in BATCH_006_036).
- sniped_context_tools_only.docx (~949 words · almost certainly a redundant subset of the already-chunked SNIPED OS Knowledge Dump · verify a true content delta before ever chunking · expect redundant).
- sniped figma.docx, Pixieset_Operations_Reference.docx, Evoto_AI_Retouching_Reference.docx (production tooling references).

**Unlock:** a concrete build need that the tool doc would directly serve. Absent that, hold.

## 10. Raw scrapes / low-value dumps (DEFER/EXCLUDE · narrow before any use)

Massive raw web/chat scrapes · boilerplate-heavy · low signal density. Do NOT chunk unless narrowed to a precise question later:

- `raw/10_REFERENCE/_intake_2026-05-18/astro claude websites 3x faster.docx` · ~853,149 words.
- `raw/99_VAULT/_intake_archive_2026-05-12/MORE CLAUDE 5.docx` · ~137,411 words.

**Unlock:** a precise question that justifies a small, curated extract. Chunking the raw dumps as-is would inject noise into the corpus. Default: skip.

## 11. Out-of-scope / personal / private + stale / duplicate (EXCLUDE · not corpus)

Correctly not corpus material. No action required (optional delete only under a separately-authorized cleanup pass · deletion is hard-to-reverse and is NOT authorized by this index):

- **Operational:** `03_OUTREACH/` (campaigns, SOPs, reply scripts, sent-DM logs), `02_CONTRACTS/`, `04_CRM/`, `06_DELIVERY/`, `01_OFFERS/`, `05_PRODUCTION/` SOPs, `_skills/` + `Claude_AI_Skills_50_Upload_Ready/` (operator tooling SKILL.md), `14_WEB/` build kit, session logs, READMEs, INDEX.md, ACTIVE_THREADS.md, CRM/opportunity xlsx + pptx, png/mp4/xmp media, shell/py scripts, zips, intake html.
- **Personal / private:** life story.docx (do not chunk).
- **Stale drafts:** chat Sniped MAster thread.docx, Gemini Sniped MAster thread.docx (raw assistant-thread dumps), NEXT INFO GRABS.docx (a to-acquire scratch note).
- **Duplicate / superseded (optional future delete):** ai after ramon copy.docx, takeover after ramon copy.docx, The_Claude_Stack (1).docx (the "(1)" twin of the chunked The_Claude_Stack), the 3 superseded old djvu originals (Predictably Irrational, The Mailroom, Seagull · each replaced by a processed `_RECOVERED` file).

## 12. Bible (held separately · do not touch until an explicit SPIRITUAL_FOUNDATION decision)

**The KJV Bible was NOT touched, staged, chunked, or included, and is NOT in any disposition above.** It is not present in `raw/`, not tracked in git, and not a `source_title`/`source_file` in any chunk (the word "bible" appears in chunks only as unrelated prose such as "Style Bible"). It remains a held SPIRITUAL_FOUNDATION anchor in the source universe per NEW_SOURCE_INTAKE_PLAN. **Do not touch, stage, chunk, or include until an explicit SPIRITUAL_FOUNDATION decision is authorized.**

## 13. Decision rules (durable · apply to any future doc disposition)

1. **External knowledge can be canonical.** Third-party books and external sources are read decision-neutrally and can be chunked (this is how the 47 mini-batches were built).
2. **Operator-authored doctrine waits for the identity decision.** SNIPED-authored operating playbooks (§8) are held until the identity question is settled; they are an option set, not canon.
3. **Identity-direction docs wait for the fresh SNIPED brief.** The BRAND_STRATEGY set and CURRENT_IDENTITY (§7) stay decision-neutral and unextracted until the operator writes the fresh brief.
4. **Tooling docs only become canon if tied to a real build need.** Implementation/tooling docs (§9) are held absent a concrete build that the doc serves.
5. **Massive scrapes require narrowing before use.** The raw dumps (§10) are not chunked as-is; a precise question and a curated extract come first.
6. **No current doc should become OPERATOR_DOCS_CLEANUP chunks.** This index is classify-and-hold. There is no `OPERATOR_DOCS_CLEANUP` batch and none should be created from this residual tail.

## 14. Unlock conditions (what must happen before each held category can move)

- **Identity-direction review (§7):** unlocked by the **fresh current SNIPED brief**. Until written, hold.
- **CURRENT_IDENTITY principle-only ship:** may happen **only by explicit operator authorization** · it remains plan-only / NOT extracted until then.
- **Bible (§12):** a deliberate **SPIRITUAL_FOUNDATION decision** is required before any touch / stage / chunk.
- **Tooling docs (§9):** a **build-specific need** is required before any become canon.
- **Identity-risk docs (§8):** unlocked only after the identity decision, and even then as transferable principles routed to existing domains, never SNIPED-specific brand doctrine.

## 15. Guardrails (ACTIVE · unchanged by this index)

- **No final SNIPED direction.** SNIPED is the live operator identity / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- **No forced business identity.** The Operator / Attention / Business-Operations playbooks are NOT the decided business model.
- **No premature brand lock.** The BRAND_STRATEGY set (naming, name recommendation, migration plan) is explicitly held.
- **CURRENT_OPERATOR_REALITY_BRIEF remains the active operator context** governing every lane · photography remains one option among several.

## 16. Scope guards honored by this artifact

- Created no `*_CHUNKS.jsonl` and no `*_extracted/` dir.
- Did NOT extract, chunk, or consolidate · total_chunks stays 1,837.
- Did NOT update MASTER_CHUNK_MAP.json, MASTER_INDEX.md, or ACTIVE_KNOWLEDGE_STATE.md.
- Did NOT modify any `raw/` or source file.
- Did NOT touch the Bible.
- Created no domain.
- Wrote only this index file. Em-dash clean. (Commit gated on operator review.)
