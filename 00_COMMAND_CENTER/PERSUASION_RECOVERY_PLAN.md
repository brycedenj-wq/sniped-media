# PERSUASION_RECOVERY mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document plans a single-source recovery mini-batch around the recovered Predictably Irrational (Ariely) and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `27b4a94 save session after MEDIA_BUSINESS_RECOVERY consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,486 (reconciled · header = sum of `.batches[].chunk_count` = sum of jsonl line counts).
- **Canonical sets:** 10 numbered batches + 22 mini-batches · 62 official domains (75 combined keys).
- **MEDIA_BUSINESS_RECOVERY:** complete and canonical.
- **CURRENT_SOURCE_AUDIT_REFRESH:** committed (`f8a01b5`).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate source located in raw/

- **Title:** Predictably Irrational: The Hidden Forces That Shape Our Decisions (Revised and Expanded Edition)
- **Author:** Dan Ariely
- **Exact path:** `raw/03_TIER_2_CANON_BOOKS/persuasion_psych/Dan Ariely - Predictably Irrational, Revised and Expanded Edition_ The Hidden Forces That Shape Our Decisions (2009, HarperCollins) - libgen.li_RECOVERED.epub`
- **Staged:** in the authorized RECOVERY_STAGING_PASS (`_RECOVERED` suffix · copy-not-move).

## 2. Source quality / stub / scan check (read-only)

| Attribute | Finding |
|---|---|
| File type | EPUB document (confirmed via `file`) |
| Size | 614,445 bytes (~604 KB) |
| Text extractable | YES · `ebook-convert` to /tmp succeeded (temp deleted) |
| Word count | 107,959 words (matches RECOVERY_INTAKE_CHECK / RECOVERY_STAGING_REPORT · 107,959) |
| Char count | 647,297 |
| First lines | "Predictably Irrational Revised and Expanded Edition / The Hidden Forces That Shape Our Decisions / Dan Ariely" |
| Stub / scan? | NO · full-length, clean, reflowable text (not a scan, not a stub, not 0-byte) |

**Verdict: usable.** Clean, full-text epub. Extraction tooling already on PATH (`ebook-convert` / calibre · no OCR · no new dependency).

## 3. Old bad djvu / original exclusion

- **Old bad original present beside the recovered file:** `raw/03_TIER_2_CANON_BOOKS/persuasion_psych/Dan Ariely - Predictably Irrational_ The Hidden Forces That Shape Our Decisions (2010, Harper Perennial) - libgen.li.djvu` (unsupported djvu · no djvutxt on PATH · 0 extractable text in this pipeline).
- **Decision:** the old `.djvu` is EXCLUDED. The ship will extract ONLY the `_RECOVERED.epub`. The old djvu remains in place untouched (preserved per the staging rules · do not hand-delete raw originals outside an authorized cleanup pass).

## 4. Already-chunked overlap check

- **Ariely / Predictably Irrational already chunked:** NO · appears in 0 `*_CHUNKS.jsonl` files. **Net-new title.**
- **Thematic neighbors (the existing persuasion / behavioral cluster, mostly BATCH_009 + BATCH_009_EXPANSION + CULTURE_AND_STATUS + ADVERTISING_RECOVERY):**
  - `brand-psychology` (28 chunks) already holds: Influence / Cialdini (six principles · reciprocation · social proof · authority · scarcity), Pre-Suasion, Cashvertising (Life-Force 8 · emotion-then-logic), Contagious (high-arousal sharing), The Choice Factory (behavioural biases · pratfall · distinctiveness), Alchemy (psycho-logic · perceived value), Never Split the Difference, plus The Offer Stack frameworks, Status Game / Status and Culture, and the Sugarman ADVERTISING_RECOVERY chunks.
  - `decision-making` (1 chunk) holds only: Poor Charlie's Almanack · inversion.
- **Overlap risk + mitigation:** the cluster covers *compliance / influence principles* (Cialdini) and *applied advertising bias* (Choice Factory, Alchemy, Cashvertising). Predictably Irrational is the **foundational behavioral-economics primary source** behind much of that applied work, but it is distinct at the title and experiment level. To avoid restating Cialdini, PERSUASION_RECOVERY chunks will anchor on **Ariely's own named experiments/effects** (arbitrary coherence / anchoring, the high cost of zero cost / the power of FREE, social norms vs market norms, the placebo of price / expectations shape experience, the decoy / relativity effect, the endowment / ownership bias, procrastination + self-control, keeping options open, the context of our character / the fudge factor), explicitly distinguished from Cialdini's compliance principles already in `brand-psychology`. This grows the near-empty `decision-making` domain and adds the primary-source layer beneath the existing applied-persuasion canon.

## 5. Is a single-source mini-batch warranted?

**Yes.** Predictably Irrational is a foundational, full-length (107,959-word) behavioral-economics text dense with ~12-15 discrete, named, reusable experiments/effects. It is thematically coherent on its own, is the primary source beneath several already-canonical applied titles, and grows a thin domain (`decision-making` = 1). The ONWARD_TURNAROUND single-source mini-batch (12 chunks) is the direct precedent. One curated mini-batch, no split.

## 6. Recommended include / defer / exclude set

- **INCLUDE (1 · CORE):** Predictably Irrational, Revised and Expanded Edition (Ariely) · `_RECOVERED.epub`.
- **DEFER:** none (this is a clean single-source lane).
- **EXCLUDE (0 chunks):**
  - Old Predictably Irrational `.djvu` (unsupported format · superseded by the recovered epub).
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor · not touched/staged/chunked).
  - Every other persuasion_psych / canonical source already chunked (no re-chunking).

## 7. Recommended chunk target / range

- **Target:** ~12-16 chunks.
- **Range:** 10-18 (halt-and-report if outside).
- **Synthesis:** 1 closing synthesis chunk (the behavioral-economics decision-support pattern + the optionality guardrail).
- Rationale: matches the discrete-effect density of the book and the single-source precedent (ONWARD_TURNAROUND = 12). One effect/experiment per chunk keeps each chunk a distinct, reusable principle.

## 8. Recommended domains (EXISTING domains only · NO new domain)

Verified against `MASTER_CHUNK_MAP.json.combined_domain_counts` (75 keys) before listing:

| Domain | Exists? | Current count | Planned use in this lane |
|---|---|---:|---|
| `decision-making` | YES | 1 | **Primary anchor.** Arbitrary coherence/anchoring, relativity/decoy, procrastination + self-control, keeping options open, the context of our character. Grows a thin domain. |
| `brand-psychology` | YES | 28 | Consumer-behavior effects: expectations shape experience, relativity in judgment, predictable irrationality of buyers. |
| `pricing` | YES | 16 | The high cost of zero cost / the power of FREE; the placebo of price (higher price → stronger perceived effect); price anchoring. |
| `offer-design` | YES | 17 | The decoy / asymmetric-dominance option; FREE as an offer lever. |
| `sales-flow` | YES | 16 | Social norms vs market norms (do not mix money into relationship contexts; how framing a transaction changes behavior). |
| `commercial-architecture` | YES | 52 | Market-norm vs social-norm design for how a business relates to customers. |
| `strategy` | YES | 176 | Predictable irrationality as a design principle (biases are systematic and therefore anticipatable). |
| `operator-doctrine` | YES | 80 | The synthesis chunk + the identity-optionality guardrail framing. |
| `ethics` | YES (if warranted) | 37 | The (dis)honesty experiments / the fudge factor / cheating cues · included where the text explains how context shapes integrity. Kept honest, not a manipulation playbook. |

### Domain issue to flag (important)

- **`behavioral-psychology` does NOT exist** in the corpus (ABSENT · the operator's "if it exists" condition fails). It will **NOT be created.** All behavioral-psychology material routes to `decision-making` + `brand-psychology` + `strategy`.
- **`behavioral-economics`, `persuasion`, `psychology`, `decision-judgment` also do NOT exist** · NOT created · same routing.
- **`decision-making` DOES exist (count 1)** and is the correct primary anchor (the operator's "if it exists" condition passes · this lane grows it).
- **`pricing` DOES exist (count 16)** · used (the operator's "if it exists" condition passes).
- **NO new domain will be created.** All 9 planned domains pre-exist.

## 9. Connections (cross-references this lane opens)

- **ADVERTISING_RECOVERY (+ BATCH_009 / BATCH_009_EXPANSION):** the applied-persuasion canon (Cialdini, Sugarman, Cashvertising, Choice Factory, Alchemy) sits *on top of* Ariely's primary behavioral-economics findings. PERSUASION_RECOVERY supplies the underlying experiments; the advertising lane supplies the applied craft. Distinguished so they complement, not duplicate.
- **HIGH_LEVEL_CONVOS:** the creator-economy / pricing / audience-monetization threads read against Ariely's pricing-and-value irrationality (FREE, price-placebo, relativity) in a conversational register.
- **DEEP_FINANCE_EXPANSION:** investor irrationality, anchoring, and loss/ownership bias connect Ariely directly to the `capital` lane's behavioral side (Klarman/Graham margin-of-safety thinking assumes the market's predictable irrationality).
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane (see §10-11).

## 10. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the behavioral-economics findings as a **decision-support lens read against CURRENT_OPERATOR_REALITY_BRIEF**, with the closing synthesis chunk making the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 11. Persuasion / behavioral economics = decision-support only (not a directive)

Predictably Irrational is held strictly as a **decision-support and design layer**: understanding how people (including BJ himself) predictably deviate from rationality so he can design honest offers, fair pricing, and clear decisions. It is **NOT a directive that BJ become a persuasion guru, a behavioral-marketing operator, or a manipulative marketer.** The honesty/fudge-factor (`ethics`) chunks keep the material oriented toward integrity, not exploitation. The findings are a lens, not a manipulation playbook.

## 12. Deliverables for the future ship (NOT created now)

When the operator authorizes the extract/chunk step:

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/PERSUASION_RECOVERY_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/persuasion_recovery_extracted/` (1 normalized .txt) |
| Summary | `01_KNOWLEDGE_BASE/summaries/PERSUASION_RECOVERY_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/PERSUASION_RECOVERY_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/PERSUASION_RECOVERY_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/PERSUASION_RECOVERY_COMPLETE.md` |
| Extraction script | `scripts/extract_persuasion_recovery.py` |
| Chunk writer | `scripts/write_persuasion_recovery_chunks.py` |

Schema: the canonical 12-field JSONL (chunk_id, batch_id, source_title, source_file, author, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags) · `batch_id` = `PERSUASION_RECOVERY` · per-source attribution (Ariely). Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · no new domain · old djvu 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality guardrail in every chunk · quote discipline · em-dash sweep).

## 13. Projected post-consolidation state (for reference · NOT applied now)

If shipped at the mid-target (~14) and consolidated: 1,486 + ~14 = ~1,500 chunks · 10 numbered batches + 23 mini-batches · 62 domains (NO new domain · `decision-making` grows from 1 toward ~6, plus bumps to brand-psychology / pricing / offer-design / sales-flow / commercial-architecture / strategy / operator-doctrine / ethics). Exact counts finalized at ship/consolidation time.

## 14. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,486.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `ls` / `ebook-convert`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No next lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 15. Next step (operator decision · do not start without authorization)

Authorize the PERSUASION_RECOVERY extract + chunk + validate step (single source · `_RECOVERED.epub` only · target ~12-16 · existing domains only · `decision-making` anchors · no new domain · old djvu / Bible excluded), then commit the ship outputs, then authorize master-consolidation.
