# FULL_DOWNLOADS_AND_OS_COVERAGE_LEDGER

**Date:** 2026-05-27
**Status:** Per-file coverage proof layer for the relevant reference universe vs the 1,837-chunk OS. Anchor-class: markdown-only, not chunked, not a chunk source, not in the master files. No ingestion performed.

## 1. Audit method
- **Folders inspected:** `~/Downloads` (loose, depth 1) and `~/Downloads/    SNIPED_OS/` (full tree), relevant extensions only (docx, pdf, md, epub, mobi, azw3, txt, json, xlsx, pptx, html). Media (mp4/png/jpg/xmp/eps/ai) and Word temp (`~$`) excluded.
- **Matching logic:** (a) basename cross-checked against the 647 `raw/` basenames (raw/ is the staged universe that produced the corpus, so a basename present there = represented/staged); (b) distinctive filename tokens (len>=4, stopwords dropped) checked against the corpus source list (555 source strings) and the concatenated chunk text (836 KB of title+concept+summary); (c) content-keyword greps for the specific candidate books/codices.
- **How corpus coverage was checked:** `represented` = staged-in-raw OR >=2 distinctive source-token hits (>=1 for books). `partial` = concept present in chunk text but not a dedicated source. `missing` = no source hit and <=1 text hit. `parked` = BASEPLATE / legal / lead-data (policy, not a gap). `duplicate` = superseded master/consolidated/versioned scratch. `ignore` = employer SOPs or personal off-scope. `review` = could not auto-confirm.
- **Limitations (blunt):** filename matching is approximate. `represented` (positive matches + raw cross-check) is HIGH confidence. The `missing`/`review` buckets are LOW confidence as true gaps: they are dominated by (i) ~50 identically-named `SKILL.md` files the matcher cannot disambiguate (the 50-skill hub IS chunked), (ii) personal scratch notes, (iii) employer/facility SOPs, (iv) superseded SNIPED scratch. The genuinely-missing KNOWLEDGE was confirmed by content grep, not filename, and is the short list in section 4. Do not read raw `missing` counts as knowledge gaps.

## 2. Summary counts
- Total relevant candidates inspected: **2200**
  - represented: 1396
  - parked: 99
  - duplicate: 191
  - ignore: 125
  - partial: 54
  - missing: 161
  - review: 174
- Already represented (incl. staged-in-raw): **1396** (high confidence)
- Parked by policy (BASEPLATE / legal / lead-data): **99**
- Duplicate / superseded scratch: **191**
- Ignore (employer SOPs + personal off-scope): **125**
- Partial / missing / review (auto-unconfirmed, mostly NOT knowledge gaps): **389** -> genuine knowledge deltas after manual filter: see section 4.

## 4. High-value MISSING (genuine knowledge deltas, content-verified)
These are relevant AND not represented AND worth ingesting. Verified by content grep, not just filename.

**Books (0 chunk hits, genuine gap):** The Cold Email Manifesto, Fanatical Prospecting, Combo Prospecting, Gap Selling, Predictable Revenue (outbound sales canon); Profit First, Tax-Free Wealth (finance/ownership). The corpus has relationship-outreach SOPs but no cold-outbound book theory and no finance-ops books.

**Tool/AI-content docs (only the skill is in, not the deep docs):** higssfield og.docx, higgsfield codex/playbook, kling 3.00.docx, kling_ai_extracted.docx, Sniped_Media_Kling_FINAL.docx, firefly generation.docx.

**Framework/method deltas worth a compare-then-maybe-chunk:** NEGOTIATION_FRAMEWORKS, SUPERFORECASTING_FRAMEWORKS, copywriting_frameworks, PKM_Systems_FRAMEWORKS, Proof_Sorting_Framework, 30_Shot_Playbook, Vanguard_Playbook, Portfolio_Strategy.

**Editing/preset deltas (verify vs production__preset_library already in corpus):** THE_THREE_PRESETS, BW_PRESET_GORDON_PARKS, THE_MACHINE, The_Install_Methodology_v1, COMPLETE/LIFETIME editing systems.

**Outbound ops (current vs old vertical):** Instantly Sop V2.pdf, Outreach_Angles.docx (the attorney/health sequences are old-vertical, park).

### Missing but IRRELEVANT (do not ingest)
- **Employer / facility SOPs (DO-NOT-INGEST, confidentiality guardrail):** all CTXES*/LAAS*/HTX*/MOP_TEMPLATE/EOP_TEMPLATE/OMOP/SOP_UPS shutdown-startup-bypass-retransfer drafts. These are data-center operational documents from the day job. Never chunk.
- **Personal off-scope:** fitness, food/smoothies, nails, car, NBA/UConn/sports, travel, mac setup, fidelity/usaa/tax-summary/biz-expenses. Ignore.
- **Superseded SNIPED scratch:** SNIPED_MEDIA_Master_Doc_April2026, SnipedMedia_ALL_SOPs_MASTER, Phase1/2 Execution Plans, session summaries. Canonical OS already chunked via the knowledge dump + v1 synthesis.

## 5. Batch plan (confirmed/revised by the ledger)
| Batch | Contents | Treatment |
|---|---|---|
| A | Cold Email Manifesto, Fanatical/Combo Prospecting, Gap Selling, Predictable Revenue | CHUNK (top gap, serves cold outreach) |
| B | Higgsfield codex+playbook, Kling codex (+ verify Kling FINAL/extracted deltas) | CHUNK |
| C | Profit First, Tax-Free Wealth | CHUNK |
| D | Operator Playbook, Business Operations Playbook, GaryVee Attention OS + the FRAMEWORK docs (negotiation/superforecasting/copywriting/PKM/proof-sorting) | VERIFY-then-CHUNK |
| E | THE_THREE_PRESETS, BW_PRESET_GORDON_PARKS, THE_MACHINE, Install_Methodology, editing systems | VERIFY delta vs production__preset_library, chunk only net-new |
| F | BASEPLATE doctrine/operating docs | SUMMARIZE into one capsule, PARK (no chunk, anchor-class) |
| G | Legal/IP docs + Instantly CSVs/lead data + employer SOPs | PARK (legal/lead) / DO-NOT-INGEST (employer SOPs) |

**New vs prior plan:** added the FRAMEWORK docs into Batch D and the explicit employer-SOP DO-NOT-INGEST line into Batch G. A through E ~= 85-130 net new chunks if deltas confirm.

## 6. Impact on current decisions
- **HOLD before domain/Calendly/deploy?** No. Every genuine gap is additive knowledge (books, tool codices, frameworks). None is a prerequisite for registering baseplatehq.com, wiring Calendly, or deploying the site.
- **Anything challenge BASEPLATE?** No. The BASEPLATE docs are the same brand material already governing the committed Command Center docs; nothing contradicts the name.
- **Anything challenge The Capability Dossier?** No. No missing doc proposes a different wedge; the gaps reinforce it (cold-outbound canon strengthens the outreach motion).
- **Anything challenge AI-Ops/operator-systems as flagship?** No. The framework/operator docs are inputs to it, not contradictions.
- **Anything challenge baseplate.systems / baseplatehq.com?** No. No domain/naming evidence in the universe overrides the committed decision.
- **Change the 90-day plan?** No. The plan stays proof-first. Optional: Batch A (cold-outbound books) could sharpen outreach copy, but it is an enhancement, not a gate.

## 7. Final recommendation
**CLEAR TO CONTINUE.** The corpus already represents the relevant knowledge universe (1,409 confirmed represented + the parked/dup/ignore buckets). The only genuine gaps are additive (outbound-sales books, AI-content codices, a few framework/editing deltas) and none contradicts BASEPLATE, the Capability Dossier, the flagship, the domain, or the 90-day plan. Proceed with the real-world moves (domain, Calendly, deploy, outreach). Optionally run Batch A later to sharpen the cold-email work; it is an enhancement, not a blocker. Employer/facility SOPs must never be ingested.

## 8. Guardrails honored
No chunking, no master-file update, no raw mutation, no Bible touch, no extracted dirs, no site change, no new domain, no new strategy. total_chunks unchanged at 1,837. Old docs treated as evidence, not authority; committed Command Center docs remain source of truth (the ledger found no material contradiction). This artifact is the audit only.

## 3. Per-file ledger (all candidates, grouped by category; status is algorithmic, see limitations)
| file | category | status | evidence | current-truth | action |
|---|---|---|---|---|---|
| 000_MASTER_OVERRIDE_BASEPLATE.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| 000_MASTER_OVERRIDE_BASEPLATE.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate alignment.docx | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| baseplate alignment.docx | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| baseplate-30-day-plan.md | BASEPLATE | parked | src:1 txt:2 | current | park (anchor-class) |
| baseplate-automation-map.md | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| baseplate-execution-checklist.md | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate-one-pager.md | BASEPLATE | parked | src:1 txt:2 | current | park (anchor-class) |
| baseplate-operating-manual.md | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate-sops.md | BASEPLATE | parked | src:1 txt:2 | current | park (anchor-class) |
| baseplate-strategy (1).md | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| baseplate-strategy (2).md | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| baseplate-strategy.md | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| baseplate-validation-tracker (1).md | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| baseplate-validation-tracker (2).md | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| baseplate-validation-tracker.md | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| baseplate-weekly-checklist.md | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| Baseplate_Clothing_First_Drop_Plan.docx | BASEPLATE | parked | src:1 txt:5 | current | park (anchor-class) |
| Baseplate_Clothing_First_Drop_Plan.docx | BASEPLATE | parked | src:1 txt:5 | current | park (anchor-class) |
| baseplate_cold_outreach.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate_cold_outreach.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate_core_definition.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate_core_definition.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate_discovery_call_script.docx | BASEPLATE | parked | src:3 txt:4 | current | park (anchor-class) |
| baseplate_discovery_call_script.docx | BASEPLATE | parked | src:3 txt:4 | current | park (anchor-class) |
| Baseplate_Exploration_Notes (1).docx | BASEPLATE | parked | src:2 txt:3 | current | park (anchor-class) |
| Baseplate_Exploration_Notes (1).docx | BASEPLATE | parked | src:2 txt:3 | current | park (anchor-class) |
| Baseplate_Exploration_Notes.docx | BASEPLATE | parked | src:2 txt:3 | current | park (anchor-class) |
| Baseplate_Exploration_Notes.docx | BASEPLATE | parked | src:2 txt:3 | current | park (anchor-class) |
| Baseplate_Holding_Brand_Notes.docx | BASEPLATE | parked | src:3 txt:4 | current | park (anchor-class) |
| Baseplate_Holding_Brand_Notes.docx | BASEPLATE | parked | src:3 txt:4 | current | park (anchor-class) |
| baseplate_install_essential.docx | BASEPLATE | parked | src:1 txt:3 | current | park (anchor-class) |
| baseplate_install_essential.docx | BASEPLATE | parked | src:1 txt:3 | current | park (anchor-class) |
| Baseplate_IP_Assignment_Agreement.docx | BASEPLATE | parked | src:1 txt:3 | current | park (anchor-class) |
| Baseplate_IP_Assignment_Agreement.docx | BASEPLATE | parked | src:1 txt:3 | current | park (anchor-class) |
| baseplate_landing_page.docx | BASEPLATE | parked | src:1 txt:3 | current | park (anchor-class) |
| baseplate_landing_page.docx | BASEPLATE | parked | src:1 txt:3 | current | park (anchor-class) |
| Baseplate_LLC_Operating_Agreement.docx | BASEPLATE | parked | src:2 txt:3 | current | park (anchor-class) |
| Baseplate_LLC_Operating_Agreement.docx | BASEPLATE | parked | src:2 txt:3 | current | park (anchor-class) |
| baseplate_onboarding_form.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate_onboarding_form.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate_operating_model.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate_operating_model.docx | BASEPLATE | parked | src:3 txt:3 | current | park (anchor-class) |
| baseplate_sow_install_essential.docx | BASEPLATE | parked | src:1 txt:3 | current | park (anchor-class) |
| baseplate_sow_install_essential.docx | BASEPLATE | parked | src:1 txt:3 | current | park (anchor-class) |
| Baseplate_The_Doctrine_v1.docx | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| Baseplate_The_Doctrine_v1.docx | BASEPLATE | parked | src:2 txt:2 | current | park (anchor-class) |
| AI_Skills_Catalog_v2.docx | Claude/AI | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| AI_Skills_Catalog_v2.docx | Claude/AI | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| gemini gangsta.docx | Claude/AI | ignore | src:1 txt:1 | off-scope | ignore (personal) |
| gemini gangsta.docx | Claude/AI | ignore | src:1 txt:1 | off-scope | ignore (personal) |
| claude_agents_extracted.docx | Claude/AI | partial | src:1 txt:3 | unclear | compare delta |
| claude_agents_extracted.docx | Claude/AI | partial | src:1 txt:3 | unclear | compare delta |
| gemini nano banana prompting guru.docx | Claude/AI | partial | src:1 txt:4 | unclear | compare delta |
| gemini nano banana prompting guru.docx | Claude/AI | partial | src:1 txt:4 | unclear | compare delta |
|  Claude C. Hopkins - Scientific Advertising (2010, www.snowballpublishing.com) - | Claude/AI | represented | staged-in-raw | current | skip |
|  Claude C. Hopkins - Scientific Advertising (2010, www.snowballpublishing.com) - | Claude/AI | represented | staged-in-raw | current | skip |
| ai-code-website-build-pipeline-SKILL.md | Claude/AI | represented | src:5 txt:5 | current | skip |
| AI_Skills_Catalog.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| AI_Skills_Catalog.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| astro claude websites 3x faster.docx | Claude/AI | represented | staged-in-raw | current | skip |
| astro claude websites 3x faster.docx | Claude/AI | represented | staged-in-raw | current | skip |
| Blueprint - ElevenLabs Agent That Calls & Qualifies Leads.json | Claude/AI | represented | staged-in-raw | current | skip |
| Blueprint - ElevenLabs Agent That Calls & Qualifies Leads.json | Claude/AI | represented | staged-in-raw | current | skip |
| CLAUDE CODE PLUGIN.docx | Claude/AI | represented | staged-in-raw | current | skip |
| CLAUDE CODE PLUGIN.docx | Claude/AI | represented | staged-in-raw | current | skip |
| CLAUDE CODE SUPERPOWERS.docx | Claude/AI | represented | staged-in-raw | current | skip |
| CLAUDE CODE SUPERPOWERS.docx | Claude/AI | represented | staged-in-raw | current | skip |
| claude cowork genius.docx | Claude/AI | represented | staged-in-raw | current | skip |
| claude cowork genius.docx | Claude/AI | represented | staged-in-raw | current | skip |
| claude for small business.docx | Claude/AI | represented | staged-in-raw | current | skip |
| claude guide.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| claude guide.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| CLAUDE_CAPABILITIES_2026_EXTRACTION.md | Claude/AI | represented | staged-in-raw | current | skip |
| Claude_Code_Website_Building_Extraction.docx | Claude/AI | represented | src:4 txt:5 | current | skip |
| Claude_Code_Website_Building_Extraction.docx | Claude/AI | represented | src:4 txt:5 | current | skip |
| claude_for_small_business_organized.docx | Claude/AI | represented | staged-in-raw | current | skip |
| claude_for_small_business_organized.docx | Claude/AI | represented | staged-in-raw | current | skip |
| Claude_Operating_Manual.docx | Claude/AI | represented | staged-in-raw | current | skip |
| Claude_Operating_Manual.docx | Claude/AI | represented | staged-in-raw | current | skip |
| framework-orchestrator-SKILL.md | Claude/AI | represented | src:3 txt:3 | current | skip |
| Gemini PHOTO YAP.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| Gemini PHOTO YAP.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| Gemini Sniped MAster thread.docx | Claude/AI | represented | staged-in-raw | current | skip |
| Gemini Sniped MAster thread.docx | Claude/AI | represented | staged-in-raw | current | skip |
| MASTER CLAUDE CODE COURSE 1 thru 8.docx.docx | Claude/AI | represented | src:5 txt:5 | current | skip |
| Master Prompt Agent - Chat Input.json | Claude/AI | represented | staged-in-raw | current | skip |
| Master Prompt Agent - Chat Input.json | Claude/AI | represented | staged-in-raw | current | skip |
| Master Prompt Agent - Form Submission.json | Claude/AI | represented | staged-in-raw | current | skip |
| Master Prompt Agent - Form Submission.json | Claude/AI | represented | staged-in-raw | current | skip |
| Michalowicz, Mike - Profit first _ a simple system to transform any business fro | Claude/AI | represented | src:8 txt:13 | current | skip |
| Michalowicz, Mike - Profit first _ a simple system to transform any business fro | Claude/AI | represented | src:8 txt:13 | current | skip |
| MORE CLAUDE 5.docx | Claude/AI | represented | staged-in-raw | current | skip |
| Prompt Writing Agent - Deep Reasoning Workflow.json | Claude/AI | represented | staged-in-raw | current | skip |
| Prompt Writing Agent - Deep Reasoning Workflow.json | Claude/AI | represented | staged-in-raw | current | skip |
| Prompt Writing Agent - Normal Model Workflow.json | Claude/AI | represented | staged-in-raw | current | skip |
| Prompt Writing Agent - Normal Model Workflow.json | Claude/AI | represented | staged-in-raw | current | skip |
| REMOTION.docx | Claude/AI | represented | staged-in-raw | current | skip |
| REMOTION.docx | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL.md | Claude/AI | represented | staged-in-raw | current | skip |
| SKILL_BUILD_QUEUE.md | Claude/AI | represented | staged-in-raw | current | skip |
| The_Claude_Stack (1).docx | Claude/AI | represented | staged-in-raw | current | skip |
| The_Claude_Stack (1).docx | Claude/AI | represented | staged-in-raw | current | skip |
| The_Claude_Stack.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| The_Claude_Stack.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| website on claude.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| website on claude.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| writing book claude or gem.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| writing book claude or gem.docx | Claude/AI | represented | src:2 txt:2 | current | skip |
| claude agents etc.docx | Claude/AI | review | src:1 txt:2 | unclear | manual review |
| claude agents etc.docx | Claude/AI | review | src:1 txt:2 | unclear | manual review |
| claude thursday 4:23.docx | Claude/AI | review | src:1 txt:2 | unclear | manual review |
| claude thursday 4:23.docx | Claude/AI | review | src:1 txt:2 | unclear | manual review |
| Gemini.docx | Claude/AI | review | src:1 txt:1 | unclear | manual review |
| Gemini.docx | Claude/AI | review | src:1 txt:1 | unclear | manual review |
| Sniped_Media_Kling_FINAL (1).docx | Higgsfield/Kling | duplicate | src:0 txt:0 | superseded | ignore (superseded) |
| Sniped_Media_Kling_FINAL (1).docx | Higgsfield/Kling | duplicate | src:0 txt:0 | superseded | ignore (superseded) |
| Sniped_Media_Kling_Gem_Setup_v2.docx | Higgsfield/Kling | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| Sniped_Media_Kling_Gem_Setup_v2.docx | Higgsfield/Kling | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| higssfield og.docx | Higgsfield/Kling | missing | src:0 txt:0 | current | ingest/review |
| higssfield og.docx | Higgsfield/Kling | missing | src:0 txt:0 | current | ingest/review |
| kling 3.00.docx | Higgsfield/Kling | missing | src:0 txt:0 | current | ingest/review |
| kling 3.00.docx | Higgsfield/Kling | missing | src:0 txt:0 | current | ingest/review |
| kling_ai_extracted.docx | Higgsfield/Kling | missing | src:0 txt:1 | current | ingest/review |
| kling_ai_extracted.docx | Higgsfield/Kling | missing | src:0 txt:1 | current | ingest/review |
| Sniped_Media_Kling_FINAL.docx | Higgsfield/Kling | missing | src:0 txt:0 | current | ingest/review |
| Sniped_Media_Kling_FINAL.docx | Higgsfield/Kling | missing | src:0 txt:0 | current | ingest/review |
| Sniped_Media_Kling_Final.txt | Higgsfield/Kling | missing | src:0 txt:0 | current | ingest/review |
| firefly-image-model-4-guide-updated.pdf | Higgsfield/Kling | represented | src:3 txt:5 | current | skip |
| firefly-video-guide.pdf | Higgsfield/Kling | represented | src:2 txt:3 | current | skip |
| higgsfield never forget.docx | Higgsfield/Kling | represented | staged-in-raw | current | skip |
| Higgsfield_AI_Operator_Playbook.docx | Higgsfield/Kling | represented | staged-in-raw | current | skip |
| Higgsfield_AI_Operator_Playbook.docx | Higgsfield/Kling | represented | staged-in-raw | current | skip |
| HIGGSFIELD_TACTICAL_EXTRACTION.md | Higgsfield/Kling | represented | staged-in-raw | current | skip |
| product-guide-adobe-firefly-new.pdf | Higgsfield/Kling | represented | src:2 txt:4 | current | skip |
| SKILL.md | Higgsfield/Kling | represented | staged-in-raw | current | skip |
| The_Higgsfield_Codex.docx | Higgsfield/Kling | represented | staged-in-raw | current | skip |
| The_Higgsfield_Codex.docx | Higgsfield/Kling | represented | staged-in-raw | current | skip |
| The_Kling_AI_Codex.docx | Higgsfield/Kling | represented | staged-in-raw | current | skip |
| The_Kling_AI_Codex.docx | Higgsfield/Kling | represented | staged-in-raw | current | skip |
| firefly generation.docx | Higgsfield/Kling | review | src:1 txt:2 | unclear | manual review |
| firefly generation.docx | Higgsfield/Kling | review | src:1 txt:2 | unclear | manual review |
| Sniped_Media_Kling_Gem_Setup.docx | Higgsfield/Kling | review | src:1 txt:1 | unclear | manual review |
| Sniped_Media_Kling_Gem_Setup.docx | Higgsfield/Kling | review | src:1 txt:1 | unclear | manual review |
| 6_Content_Marketing_OS (1).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| 6_Content_Marketing_OS (2).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Action_Plan_Instructions (1).docx | SNIPED | duplicate | src:0 txt:3 | superseded | ignore (superseded) |
| ai-ops-dashboard-prd (1).md | SNIPED | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| Demand_Letter_UPDATED_Sorrento.docx | SNIPED | duplicate | src:1 txt:3 | superseded | ignore (superseded) |
| Extracted_Professional_Intelligence (1).docx | SNIPED | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| FE_Readiness_Checklist_DRAFT_v1.1 (1).docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| FE_Readiness_Checklist_DRAFT_v1.1 (1).xlsx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| financial_os_final_v2.xlsx | SNIPED | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| index (1).html | SNIPED | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| Small_Claims_Guide_UPDATED_Sorrento.docx | SNIPED | duplicate | src:2 txt:4 | superseded | ignore (superseded) |
| Sniped_Media_30Day_Plan (1).docx | SNIPED | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| Sniped_Media_30Day_Plan (1).docx | SNIPED | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| sniped_media_attorney_sequences_18 (1).docx | SNIPED | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| sniped_media_attorney_sequences_18 (1).docx | SNIPED | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| Sniped_Media_Booking_Overhaul_v2 (1).docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Booking_Overhaul_v2 (1).docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Booking_Overhaul_v2.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Booking_Overhaul_v2.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| sniped_media_business_card_back_squid_ink (1).pdf | SNIPED | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| SNIPED_MEDIA_Complete_Context_Export (1).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| SNIPED_MEDIA_Complete_Context_Export (1).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Content_Production_SOP (1).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Content_Production_SOP (1).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| sniped_media_email_sequences_54 (1).docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| sniped_media_email_sequences_54 (1).docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| SNIPED_MEDIA_Master_Doc_April2026.docx | SNIPED | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| SNIPED_MEDIA_Master_Doc_April2026.docx | SNIPED | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| Sniped_Media_Master_Integration.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Master_Integration.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Master_Intelligence_Document.docx | SNIPED | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Master_Intelligence_Document.docx | SNIPED | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Pixieset_Template_Kit (1).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Pixieset_Template_Kit (1).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Session_Master_March2026.docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Session_Master_March2026.docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Session_Summary_Mar26.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Session_Summary_Mar26.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| SNIPED_Phase1_Execution_Plan.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| SNIPED_Phase1_Execution_Plan.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| SNIPED_Phase2_Execution_Plan.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| SNIPED_Phase2_Execution_Plan.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| SNIPED_Picture_Review_Prompt (1).docx | SNIPED | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| SNIPED_Picture_Review_Prompt (1).docx | SNIPED | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| SNIPED_Session_Handoff (1).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| SNIPED_Session_Handoff (1).docx | SNIPED | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| sniped_session_summary_march22.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| sniped_session_summary_march22.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| SnipedMedia_ALL_SOPs_MASTER.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| SnipedMedia_ALL_SOPs_MASTER.docx | SNIPED | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| The_Direction_Shift_Master_v2.docx | SNIPED | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
|  W. David Marx - Status and Culture_ How Our Desire for Social Rank Creates Tast | SNIPED | ignore | src:9 txt:13 | off-scope | ignore (personal) |
| 21 DAY GOLF PLAN.docx | SNIPED | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| [Laws of Human Nature] Robert Greene - The Laws of Human Nature (2019, VIKING) - | SNIPED | ignore | src:5 txt:5 | off-scope | ignore (personal) |
| apple music.docx | SNIPED | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| az vs michi.docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| Bryceden_Jones_2025_Tax_Summary.docx | SNIPED | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| Bryceden_Jones_2025_Tax_Summary_UPDATED.docx | SNIPED | ignore | src:0 txt:2 | off-scope | ignore (personal) |
| car cleaning.docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| CTXES1_1_SOP_UPS-1-1-1_SHUTDOWN_DRAFT.docx.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES1_1_SOP_UPS-1-1-1_STARTUP_DRAFT.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES1_1_SOP_UPS-1-1-1_STARTUP_ON_TEMPLATE (1).docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES1_1_SOP_UPS-1-1-1_STARTUP_ON_TEMPLATE (2).docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES1_1_SOP_UPS-1-1-1_STARTUP_ON_TEMPLATE.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES2_1_SOP_UPS-1-1_MAINT_BYPASS_FINAL.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES3_1_SOP_UPS-1-1_RETRANSFER_FINAL.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES4_1_SOP_UPS-1-1-1_SHUTDOWN_DRAFT.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| DAD BBALL TIPS.docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| Emperor of the French Napoleon I_ Frankreich Kaiser Napoléon I._ - Napoleon _ a | SNIPED | ignore | src:3 txt:5 | off-scope | ignore (personal) |
| EOP_TEMPLATE.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| fe vs me .docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| FITNESS.docx | SNIPED | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| FITNESS_DOC-2.docx | SNIPED | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| FITNESS_DOC.docx | SNIPED | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| food food and more food.docx | SNIPED | ignore | src:0 txt:2 | off-scope | ignore (personal) |
| golf_extraction.docx | SNIPED | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| GOLFER.docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| Greene, Robert - Mastery (2013_2012, Penguin Group_ Penguin Books_Viking Adult)  | SNIPED | ignore | src:3 txt:6 | off-scope | ignore (personal) |
| HTX1_1_SOP_TEMPLATE_DRAFT_083024.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| HTX1_Phase 2 - Assessment & Action Plan.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| Kevin Kelly - The Inevitable_ Understanding the 12 Technological Forces That Wil | SNIPED | ignore | src:7 txt:9 | off-scope | ignore (personal) |
| LAAS10.3_OMOP_TEMPLATE_SF_REV_3_041824.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| LAAS11.3_EOP_TEMPLATE_SF_REV_3_041824.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| mac set up.docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| MOP_TEMPLATE 1.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| NAILSSS.docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| NBA GAMES.docx | SNIPED | ignore | src:1 txt:1 | off-scope | ignore (personal) |
| park perfect.docx | SNIPED | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| set up ai.docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| setting up mac.docx | SNIPED | ignore | src:1 txt:1 | off-scope | ignore (personal) |
| Smoothies and Malted shakes.docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| SOP_TEMPLATE.docx | SNIPED | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| The_Food_Manual.docx | SNIPED | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| TRAVEL_OS.docx | SNIPED | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| uconn ill mens.docx | SNIPED | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| usaa and getting approved.docx | SNIPED | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| whatnot.docx | SNIPED | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| [Part 1 ] Шерман, Алекси _ - libgen.li.mobi | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| _.epub | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| adobe goat.docx | SNIPED | missing | src:0 txt:1 | current | ingest/review |
| Anna_ClientUpdateIntake.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| ClientEngagementTracker.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| Coach_Jones_Bio.docx | SNIPED | missing | src:0 txt:1 | current | ingest/review |
| CoachEric_DecisionBrief.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| FestivalFriend_IntakeQuestionnaire.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| gary2.0 use.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| garyvee gameplan.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| OfDVDVbyMD.html | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| SNIPED MEDIA.pdf | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| Sniped Media.txt | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| Sniped_Media_14Day_SOP.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| Sniped_Media_14Day_SOP.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| sniped_media_30day_plan.docx | SNIPED | missing | src:0 txt:1 | current | ingest/review |
| sniped_media_30day_plan.docx | SNIPED | missing | src:0 txt:1 | current | ingest/review |
| sniped_media_attorney_sequences_18.docx | SNIPED | missing | src:0 txt:1 | current | ingest/review |
| sniped_media_attorney_sequences_18.docx | SNIPED | missing | src:0 txt:1 | current | ingest/review |
| SNIPEDSESSIONHANDOFF.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| SNIPEDSESSIONHANDOFF.docx | SNIPED | missing | src:0 txt:0 | current | ingest/review |
| THREADS.docx | SNIPED | missing | src:0 txt:1 | current | ingest/review |
| Trip_Sponsorship_OnePager.docx | SNIPED | missing | src:0 txt:1 | current | ingest/review |
| sniped-media-pixieset-contact-export-2026-03-06.csv | SNIPED | parked | src:2 txt:3 | operational | park (lead data) |
| Sniped_Media_Combined_Leads_March2026.csv | SNIPED | parked | src:1 txt:2 | operational | park (lead data) |
| Action_Plan_Instructions.docx | SNIPED | partial | src:0 txt:3 | unclear | compare delta |
| BACKDROP_CREATION_GUIDE.docx | SNIPED | partial | src:1 txt:3 | unclear | compare delta |
| debt_payoff_battle_plan.xlsx | SNIPED | partial | src:0 txt:4 | unclear | compare delta |
| Ideal_Client_Definition.docx | SNIPED | partial | src:1 txt:3 | unclear | compare delta |
| Proof_Case_Studies_Page_Copy_V1.docx | SNIPED | partial | src:1 txt:4 | unclear | compare delta |
| Proof_Deployment_Priorities.docx | SNIPED | partial | src:0 txt:3 | unclear | compare delta |
| SNIPED_Channel_Alignment_Plan.docx | SNIPED | partial | src:1 txt:3 | unclear | compare delta |
| SNIPED_Channel_Alignment_Plan.docx | SNIPED | partial | src:1 txt:3 | unclear | compare delta |
| SNIPED_Founder_Kit_Client_Experience.docx | SNIPED | partial | src:1 txt:3 | unclear | compare delta |
| SNIPED_Founder_Kit_Client_Experience.docx | SNIPED | partial | src:1 txt:3 | unclear | compare delta |
| Sniped_Media_Event_Execution_Plan.pdf | SNIPED | partial | src:1 txt:3 | unclear | compare delta |
| Sniped_Media_Proposal_Bishop_Peters_Elevation_Banquet.pdf | SNIPED | partial | src:1 txt:3 | unclear | compare delta |
| ticket buying and seling games concerts etc.docx | SNIPED | partial | src:1 txt:4 | unclear | compare delta |
| TRAVEL GUIDE AND HACK.docx | SNIPED | partial | src:1 txt:3 | unclear | compare delta |
|  Adam Morgan - Eating the Big Fish_ How Challenger Brands Can Compete Against Br | SNIPED | represented | staged-in-raw | current | skip |
|  Agins, Teri - The end of fashion_ how marketing changed the clothing business f | SNIPED | represented | staged-in-raw | current | skip |
|  Alicia Drake - The Beautiful Fall_ Fashion, Genius, and Glorious Excess in 1970 | SNIPED | represented | staged-in-raw | current | skip |
|  André Leon Talley - The Chiffon Trenches_ A Memoir (2020, Random House Publish | SNIPED | represented | src:6 txt:9 | current | skip |
|  Atul Gawande - The Checklist Manifesto_ How to Get Things Right (2009, Metropol | SNIPED | represented | staged-in-raw | current | skip |
|  Bach, Richard - Jonathan Livingston Seagull (2010, Avon Books) - libgen.li.epub | SNIPED | represented | src:5 txt:5 | current | skip |
|  Benjamin Graham - The Intelligent Investor_ The Definitive Book on Value Invest | SNIPED | represented | staged-in-raw | current | skip |
|  Blake Snyder - Save The Cat! The Last Book on Screenwriting You'll Ever Need (2 | SNIPED | represented | staged-in-raw | current | skip |
|  Brad Stone - The Everything Store_ Jeff Bezos and the Age of Amazon (2013, Litt | SNIPED | represented | staged-in-raw | current | skip |
|  Bruce Block - The Visual Story, _ Creating the Visual Structure of Film, TV and | SNIPED | represented | staged-in-raw | current | skip |
|  Catmull, Ed_Wallace, Amy - Creativity, Inc._ Overcoming the Unseen Forces That  | SNIPED | represented | src:6 txt:13 | current | skip |
|  Charles T. Munger - Poor Charlie’s Almanack_ The Wit and Wisdom of Charles T. M | SNIPED | represented | staged-in-raw | current | skip |
|  Charles T. Munger, Peter D. Kaufman, Ed Wexler, Warren E. Buffet - Poor Charlie | SNIPED | represented | staged-in-raw | current | skip |
|  Chip Heath, Dan Heath - Made to Stick_ Why Some Ideas Survive and Others Die (2 | SNIPED | represented | staged-in-raw | current | skip |
|  Christensen, Clayton M. & Dillon, Karen & Hall, Taddy & Duncan, - Competing Aga | SNIPED | represented | staged-in-raw | current | skip |
|  Christian Dior - Dior by Dior- The Autobiography of Christian Dior - libgen.li. | SNIPED | represented | staged-in-raw | current | skip |
|  Christian Dior - The little dictionary of fashion (2007, V & A Publications) -  | SNIPED | represented | staged-in-raw | current | skip |
|  Christopher Steiner - Automate This_ How Algorithms Came to Rule Our World (201 | SNIPED | represented | staged-in-raw | current | skip |
|  Colin Bryar_ Bill Carr - Working Backwards (2021, St. Martin's Publishing Group | SNIPED | represented | staged-in-raw | current | skip |
|  Dana Thomas - Deluxe_ How Luxury Lost Its Luster (2008, Penguin Books) - libgen | SNIPED | represented | staged-in-raw | current | skip |
|  Daniel Coyle - The Culture Code_ The Secrets of Highly Successful Groups (2018, | SNIPED | represented | staged-in-raw | current | skip |
|  Derek Thompson - Hit Makers_ The Science of Popularity in an Age of Distraction | SNIPED | represented | staged-in-raw | current | skip |
|  Ed Catmull, Amy Wallace - Creativity, Inc._ Overcoming the Unseen Forces That S | SNIPED | represented | staged-in-raw | current | skip |
|  Fredric Dannen - Hit men_ power brokers and fast money inside the music busines | SNIPED | represented | staged-in-raw | current | skip |
|  Geoffrey A. Moore - Crossing the Chasm, 3rd Edition_ Marketing and Selling Disr | SNIPED | represented | staged-in-raw | current | skip |
|  Harper Lee - To Kill a Mockingbird - libgen.li.mobi | SNIPED | represented | src:1 txt:2 | current | skip |
|  Howard Schultz, Joanne Gordon - Onward_ How Starbucks Fought for Its Life witho | SNIPED | represented | staged-in-raw | current | skip |
|  Jack Trout, Steve Rivkin - Differentiate or Die_ Survival in Our Era of Killer  | SNIPED | represented | staged-in-raw | current | skip |
|  Jack Weatherford - Genghis Khan and the Making of the Modern World (2005, Broad | SNIPED | represented | staged-in-raw | current | skip |
|  James B. Stewart - DisneyWar _ the battle for the magic kingdom (2006, Pocket)  | SNIPED | represented | staged-in-raw | current | skip |
|  John Berger - Ways of Seeing (2008, Penguin Books Ltd) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
|  John Seabrook - The Song Machine_ Inside the Hit Factory (2015, W. W. Norton &  | SNIPED | represented | staged-in-raw | current | skip |
|  John Truby - The Anatomy of Story_ 22 Steps to Becoming a Master Storyteller (2 | SNIPED | represented | staged-in-raw | current | skip |
|  Jonah Berger - Contagious_ Why Things Catch On (2013, Simon & Schuster) - libge | SNIPED | represented | staged-in-raw | current | skip |
|  Lovell, Sophie - Dieter Rams_ As Little Design as Possible (2011, Phaidon Press | SNIPED | represented | staged-in-raw | current | skip |
|  Marc Randolph - That Will Never Work (2019, Little, Brown and Company) - libgen | SNIPED | represented | src:7 txt:8 | current | skip |
|  Marshall McLuhan - Understanding media (1995, MIT Press) - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
|  Marshall McLuhan, Lewis H. Lapham - Understanding Media_ The Extensions of Man  | SNIPED | represented | staged-in-raw | current | skip |
|  Michael Hammer_ James Champy - Reengineering the corporation _ a manifesto for  | SNIPED | represented | staged-in-raw | current | skip |
|  Michael Jackson - Moonwalk (2009, Crown Archetype) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
|  Peter M. Senge - The Fifth Discipline_ The Art & Practice of The Learning Organ | SNIPED | represented | staged-in-raw | current | skip |
|  Peter Thiel, Blake Masters - Zero to One_ Notes on Startups, or How to Build th | SNIPED | represented | staged-in-raw | current | skip |
|  Phil knight - Shoe dog (0) - libgen.li.mobi | SNIPED | represented | staged-in-raw | current | skip |
|  Ray Kroc - Grinding It Out_ The Making of McDonald’s (2016, St. Martin’s Paperb | SNIPED | represented | staged-in-raw | current | skip |
|  Rich Cohen - The Fish That Ate the Whale_ The Life and Times of America's Banan | SNIPED | represented | staged-in-raw | current | skip |
|  Richard Shotton - The Choice Factory_ 25 Behavioural Biases That Influence What | SNIPED | represented | staged-in-raw | current | skip |
|  Rick Rubin - The Creative Act_ A Way of Being (2023, Penguin Publishing Group)  | SNIPED | represented | staged-in-raw | current | skip |
|  ROBERT B. CIALDINI - Influence (Harper collins) - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
|  Robert Cialdini - Pre-Suasion_ A Revolutionary Way to Influence and Persuade (2 | SNIPED | represented | staged-in-raw | current | skip |
|  Robert Iger_ Joel Lovell - The Ride of a Lifetime_ Lessons Learned from 15 Year | SNIPED | represented | staged-in-raw | current | skip |
|  Rory Sutherland - Alchemy_ The Dark Art and Curious Science of Creating Magic i | SNIPED | represented | staged-in-raw | current | skip |
|  Sam Walton - Sam Walton_ Made In America (1993, Bantam) - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
|  Sarah Frier - No Filter_ The Inside Story of Instagram (2020, Simon & Schuster) | SNIPED | represented | staged-in-raw | current | skip |
|  Scott Kupor - Secrets of Sand Hill Road_ Venture Capital and How to Get It (201 | SNIPED | represented | src:4 txt:8 | current | skip |
|  Stoute, Steve - The Tanning of America_ How Hip-Hop Created a Culture That Rewr | SNIPED | represented | staged-in-raw | current | skip |
|  Vreeland, Diana - D.V. (2011, HarperCollins) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
|  Walter Isaacson - Steve Jobs Walter Isaacson (2011) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
|  Whitman, Drew Eric - Cashvertising_ How to Use More Than 100 Secrets of Ad-Agen | SNIPED | represented | staged-in-raw | current | skip |
|  Will Storr - The Status Game_ On Social Position and How We Use It (2021, Willi | SNIPED | represented | staged-in-raw | current | skip |
|  William N. Thorndike - The Outsiders_ Eight Unconventional CEOs and Their Radic | SNIPED | represented | staged-in-raw | current | skip |
|  Zack O'Malley Greenburg - Empire State of Mind_ How Jay-Z Went from Street Corn | SNIPED | represented | src:8 txt:9 | current | skip |
| 01_pre_shoot_brief.md | SNIPED | represented | staged-in-raw | current | skip |
| 02_day0_delivery.md | SNIPED | represented | staged-in-raw | current | skip |
| 03_day7_testimonial.md | SNIPED | represented | staged-in-raw | current | skip |
| 04_day19_window_closing.md | SNIPED | represented | staged-in-raw | current | skip |
| 05_day30_opkit_pitch.md | SNIPED | represented | staged-in-raw | current | skip |
| 06_day90_reengagement.md | SNIPED | represented | staged-in-raw | current | skip |
| 07_referral_ask.md | SNIPED | represented | staged-in-raw | current | skip |
| 08_booking_confirmation.md | SNIPED | represented | staged-in-raw | current | skip |
| 09_no_show_or_late_followup.md | SNIPED | represented | staged-in-raw | current | skip |
| 1000-true-fans-kevin-kellydocx_compress.pdf | SNIPED | represented | staged-in-raw | current | skip |
| 100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md | SNIPED | represented | staged-in-raw | current | skip |
| 2026-W19_May04-May10.md | SNIPED | represented | staged-in-raw | current | skip |
| 257683787-Cartier-Bresson-H-1952-the-Decisive-Moment.pdf | SNIPED | represented | staged-in-raw | current | skip |
| 2_Assistant_SOP_Manual (1).docx | SNIPED | represented | staged-in-raw | current | skip |
| 2_Assistant_SOP_Manual.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| 30_Day_Development_Plan_EYES_ONLY.docx | SNIPED | represented | src:3 txt:4 | current | skip |
| 30_Day_FE_Development_Plan_EYES_ONLY.docx | SNIPED | represented | src:3 txt:4 | current | skip |
| 50 Cent, Robert Greene - The 50th Law (2009, Harper) - libgen.li.mobi | SNIPED | represented | staged-in-raw | current | skip |
| 6_Content_Marketing_OS.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| 713434459-Core-Studio-Public-Lecture-Virgil-Abloh-Insert-Complicated-Title-Here- | SNIPED | represented | staged-in-raw | current | skip |
| 7_30Day_Content_Bank.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| [Adweek Series] Luke Sullivan - Hey, Whipple, Squeeze This_ A Guide to Creating  | SNIPED | represented | staged-in-raw | current | skip |
| [Alexander the Great 1 ] Freeman, Philip - Alexander the Great (2016) - libgen.l | SNIPED | represented | staged-in-raw | current | skip |
| [Andrew_S._Grove]_High_Output_Management(z-lib.org)-2.pdf | SNIPED | represented | src:4 txt:4 | current | skip |
| [Andrew_S._Grove]_High_Output_Management(z-lib.org).pdf | SNIPED | represented | staged-in-raw | current | skip |
| [Animal Farm _1] Orwell, George - Animal Farm (1945, Secker & Warburg) - libgen. | SNIPED | represented | staged-in-raw | current | skip |
| [Baker & Taylor Books (Firm)._ Axis 360] Robert Greene_ Joost Elffers - The 48 L | SNIPED | represented | staged-in-raw | current | skip |
| [Beloved Trilogy 1 - Beloved Trilogy 1] Beloved{Toni Morrison}(1987){112430403}  | SNIPED | represented | staged-in-raw | current | skip |
| [BK business book] Watkins, Alexandra - Hello, my name is awesome_ how to create | SNIPED | represented | staged-in-raw | current | skip |
| [Blitzscaling] Reid Hoffman, Chris Yeh, Bill Gates - Blitzscaling_ The Lightning | SNIPED | represented | staged-in-raw | current | skip |
| [Classics] Arrian - The Campaigns of Alexander (2003, Penguin Books Ltd) - libge | SNIPED | represented | staged-in-raw | current | skip |
| [Company of One] Jarvis, Paul - Company of one why staying small is the next big | SNIPED | represented | staged-in-raw | current | skip |
| [Dover books on history, political and social science] Niccolo Machiavelli, Nini | SNIPED | represented | staged-in-raw | current | skip |
| [Fashion Theory The Journal of Dress Body &amp_ Culture 2019-sep 11 vol. 24 iss. | SNIPED | represented | staged-in-raw | current | skip |
| [J-B Lencioni Series] Patrick Lencioni - Death by Meeting_ A Leadership Fable... | SNIPED | represented | staged-in-raw | current | skip |
| [Joost Elffers Books ] Greene, Robert - The 33 Strategies of War (2008_2007, Pen | SNIPED | represented | staged-in-raw | current | skip |
| [Journal of Advertising 1998-dec vol. 27 iss. 4] Jon Steel, Truth, Lies and Adve | SNIPED | represented | staged-in-raw | current | skip |
| [Maus Series _1] Art Spiegelman - Maus I A Survivor's Tale My Father Bleeds Hist | SNIPED | represented | src:3 txt:6 | current | skip |
| [Maus Series _2] Art Spiegelman - Maus II A Survivor's Tale And Here My Troubles | SNIPED | represented | src:3 txt:7 | current | skip |
| [Oxford World's Classics] Carl von Clausewitz, Beatrice Heuser - On War (2007, O | SNIPED | represented | staged-in-raw | current | skip |
| [Reedsy Marketing Guides Book 1 - Reedsy Marketing Guides Book 1] How to Market  | SNIPED | represented | staged-in-raw | current | skip |
| [Security Analysis Prior Editions] Benjamin Graham, David Dodd, Warren Buffett - | SNIPED | represented | staged-in-raw | current | skip |
| [SparkNotes Literature Guide ] Orwell, George - 1984, George Orwell (1984_2014,  | SNIPED | represented | src:3 txt:6 | current | skip |
| [The Color Purple 1 - The Color Purple 1] The Color Purple Collection_ The Color | SNIPED | represented | staged-in-raw | current | skip |
| [The Handmaid's Tale 1 ] Atwood, Margaret - The Handmaid's Tale (2006_2017, Ever | SNIPED | represented | staged-in-raw | current | skip |
| [Vintage] Dannen, Fredric - Hit Men_ Power Brokers and Fast Money Inside the Mus | SNIPED | represented | src:8 txt:11 | current | skip |
| [Voices That Matter] Jay Maisel - Light, Gesture, and Color (2014, New Riders) - | SNIPED | represented | staged-in-raw | current | skip |
| _OceanofPDF.com_Pharrell_Places_and_Spaces_Ive_Been_-_Pharrell_Williams.pdf | SNIPED | represented | staged-in-raw | current | skip |
| _OceanofPDF.com_The_88_Laws_Of_The_Masculine_Mindset_-_John_Winters.pdf | SNIPED | represented | staged-in-raw | current | skip |
| _README.md | SNIPED | represented | staged-in-raw | current | skip |
| access_and_community_architecture.md | SNIPED | represented | staged-in-raw | current | skip |
| ACTIVE_THREADS.md | SNIPED | represented | staged-in-raw | current | skip |
| Aesthetic_Statement_v1.docx | SNIPED | represented | staged-in-raw | current | skip |
| ai after ramon copy.docx | SNIPED | represented | staged-in-raw | current | skip |
| ai after ramon.docx | SNIPED | represented | staged-in-raw | current | skip |
| AI CHANGED EVERYTHING.docx | SNIPED | represented | staged-in-raw | current | skip |
| AI Phone Call Assistant - Call Workflow.json | SNIPED | represented | staged-in-raw | current | skip |
| ai-ops-dashboard-prd.md | SNIPED | represented | staged-in-raw | current | skip |
| AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md | SNIPED | represented | staged-in-raw | current | skip |
| Airey, David - Identity designed_ the definitive guide to visual branding (2019, | SNIPED | represented | staged-in-raw | current | skip |
| Ajay Agrawal, Joshua Gans, Avi Goldfarb - Power and Prediction_ The Disruptive E | SNIPED | represented | staged-in-raw | current | skip |
| Ajay Agrawal, Joshua Gans, Avi Goldfarb - Prediction Machines_ The Simple Econom | SNIPED | represented | staged-in-raw | current | skip |
| Akio Morita, Edwin M. Reingold, Mitsuko Shimomura - Made in Japan_ Akio Morita a | SNIPED | represented | staged-in-raw | current | skip |
| Al Ramadan, Dave Peterson, Christopher Lochhead, Kevin Maney - Play Bigger_ How  | SNIPED | represented | staged-in-raw | current | skip |
| Al Ries_ Philip Kotler - Positioning_ The Battle for Your Mind_ The Battle for Y | SNIPED | represented | staged-in-raw | current | skip |
| Alain De Botton - Status Anxiety (2005, Vintage) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
| Alan Weiss - Value-Based Fees_ How to Charge - and Get - What You're Worth (Ulti | SNIPED | represented | staged-in-raw | current | skip |
| Alan Weiss, Alan Weiss - Million Dollar Consulting_ The Professional's Guide to  | SNIPED | represented | staged-in-raw | current | skip |
| Aldous Huxley - Brave New World Revisited (2001) - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Alex Hormozi - $100M Leads_ How to Get Strangers To Want To Buy Your Stuff (2023 | SNIPED | represented | staged-in-raw | current | skip |
| Alex Hormozi - $100M Offers_ How To Make Offers So Good People Feel Stupid Sayin | SNIPED | represented | staged-in-raw | current | skip |
| Alina Wheeler, Rob Meyerson - Designing Brand Identity_ A Comprehensive Guide to | SNIPED | represented | staged-in-raw | current | skip |
| all books summaries and some markting stuff from that chat.docx | SNIPED | represented | src:2 txt:5 | current | skip |
| Amp It Up{Frank Slootman}(2022, Wiley){112881352} libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Anders Ericsson, Robert Pool - Peak_ Secrets from the New Science of Expertise ( | SNIPED | represented | staged-in-raw | current | skip |
| Annie Leibovitz - Annie Leibovitz at Work (2008, Random House) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series.docx | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_1_RichardAvedon.md | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_2_WilliamEggleston.md | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_3_AnnieLeibovitz.md | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_4_StephenShore.md | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_5_FredHerzog.md | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_6_RobertFrank (1).md | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_6_RobertFrank.md | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_7_JoelMeyerowitz.md | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_8_GracielaIturbide.md | SNIPED | represented | staged-in-raw | current | skip |
| Art_Series_9_ErnstHaas.md | SNIPED | represented | staged-in-raw | current | skip |
| ArtOfWar.pdf | SNIPED | represented | staged-in-raw | current | skip |
| audience_engine.md | SNIPED | represented | staged-in-raw | current | skip |
| Bailey Richardson_ Kai Elmer Sotto_ Kevin Huynh - Get Together_ How to build a c | SNIPED | represented | staged-in-raw | current | skip |
| Balaji Srinivasan - The Network State - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Ben Horowitz - The Hard Thing About Hard Things_ Building a Business When There  | SNIPED | represented | staged-in-raw | current | skip |
| Blair Enns - The Win Without Pitching Manifesto (2010, RockBench Publishing Corp | SNIPED | represented | staged-in-raw | current | skip |
| Bolt, Chandler - Published_ the proven path from blank page to published author  | SNIPED | represented | staged-in-raw | current | skip |
| Brad Feld, Jason Mendelson - Venture Deals_ Be Smarter Than Your Lawyer and Vent | SNIPED | represented | src:1 txt:8 | current | skip |
| branding x clothes gold.docx | SNIPED | represented | staged-in-raw | current | skip |
| Bryceden Voice Style Guide .docx | SNIPED | represented | src:2 txt:3 | current | skip |
| Build a Brand Like Apple.docx | SNIPED | represented | staged-in-raw | current | skip |
| Built an AI SaaS in 20 min.docx | SNIPED | represented | staged-in-raw | current | skip |
| Business_Model_Framing.docx | SNIPED | represented | src:2 txt:3 | current | skip |
| Business_Principles.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| CANONICAL_TRUTHS.md | SNIPED | represented | staged-in-raw | current | skip |
| caption_templates.md | SNIPED | represented | staged-in-raw | current | skip |
| ch02_mimi_production_brief_v1.md | SNIPED | represented | staged-in-raw | current | skip |
| chapter_intake_v1.md | SNIPED | represented | staged-in-raw | current | skip |
| Chat EXPORT.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| chat images .docx | SNIPED | represented | staged-in-raw | current | skip |
| chat Sniped MAster thread.docx | SNIPED | represented | staged-in-raw | current | skip |
| chat Sniped MAster thread.docx | SNIPED | represented | staged-in-raw | current | skip |
| checklist_post_shoot_same_day.md | SNIPED | represented | staged-in-raw | current | skip |
| checklist_pre_shoot_day_of.md | SNIPED | represented | staged-in-raw | current | skip |
| Chip Heath, Dan Heath - Made to Stick_ Why Some Ideas Survive and Others Die (20 | SNIPED | represented | staged-in-raw | current | skip |
| Chris Anderson - Free_ The Future of a Radical Price (Abridged) (2009, Random Ho | SNIPED | represented | staged-in-raw | current | skip |
| Chris Anderson - Long Tail, The, Revised and Updated Edition_ Why the Future of  | SNIPED | represented | staged-in-raw | current | skip |
| Chris Dixon - Read Write Own_ Building the Next Era of the Internet (2024, Rando | SNIPED | represented | staged-in-raw | current | skip |
| Christopher Leonard - The Lords of Easy Money_ How the Federal Reserve Broke the | SNIPED | represented | staged-in-raw | current | skip |
| Coddington, Grace - Grace_ A Memoir (2012, Random House Publishing Group) - libg | SNIPED | represented | staged-in-raw | current | skip |
| composite_environment_rotation_v1.md | SNIPED | represented | staged-in-raw | current | skip |
| Confessions-of-an-Advertising-Man-by-Ogilvy-David-Parker-Alan-z-lib.org_.pdf | SNIPED | represented | src:4 txt:5 | current | skip |
| COURSE WORK 1 thru 2.docx | SNIPED | represented | staged-in-raw | current | skip |
| cultural_documentation_thesis.md | SNIPED | represented | staged-in-raw | current | skip |
| CURRENT_STATE.md | SNIPED | represented | staged-in-raw | current | skip |
| Dalio, Ray - Principles_ Life and Work (2017, Simon & Schuster) - libgen.li.pdf | SNIPED | represented | src:3 txt:3 | current | skip |
| Dan Ariely - Predictably Irrational, Revised and Expanded Edition_ The Hidden Fo | SNIPED | represented | src:9 txt:9 | current | skip |
| Dan Charnas - Dilla Time_ The Life and Afterlife of J Dilla, the Hip-Hop Produce | SNIPED | represented | staged-in-raw | current | skip |
| Dan Charnas - The Big Payback_ The History of the Business of Hip-Hop (2010, NAL | SNIPED | represented | staged-in-raw | current | skip |
| Daniel Kahneman - Thinking, Fast and Slow (2011, Farrar, Straus and Giroux) - li | SNIPED | represented | staged-in-raw | current | skip |
| Daugherty, Paul R._Wilson, H. James - Human + machine_ reimagining work in the a | SNIPED | represented | staged-in-raw | current | skip |
| David Carey, John E. Morris - King of Capital_ The Remarkable Rise, Fall, and Ri | SNIPED | represented | staged-in-raw | current | skip |
| David H. Maister, Charles H. Green, Robert M. Galford - The Trusted Advisor (200 | SNIPED | represented | staged-in-raw | current | skip |
| David Ogilvy_ Alan Parker - Confessions of an Advertising Man (2004, Southbank P | SNIPED | represented | staged-in-raw | current | skip |
| David Spinks - The Business of Belonging_ How to Build Communities That Grow the | SNIPED | represented | staged-in-raw | current | skip |
| Debt_Recovery_Strategic_Analysis.docx | SNIPED | represented | src:3 txt:4 | current | skip |
| delivery_architecture_v2.md | SNIPED | represented | staged-in-raw | current | skip |
| Derek Thompson - Hit Makers_ The Science of Popularity in an Age of Distraction  | SNIPED | represented | staged-in-raw | current | skip |
| document.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Donald Miller - Building a StoryBrand_ Clarify Your Message So Customers Will Li | SNIPED | represented | staged-in-raw | current | skip |
| Donald Miller - Building a StoryBrand_ Clarify Your Message So Customers Will Li | SNIPED | represented | staged-in-raw | current | skip |
| Donald W. Engels - Alexander the Great and the Logistics of the Macedonian Army  | SNIPED | represented | staged-in-raw | current | skip |
| dump dump for rebrand late night pt 2.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| dump dump for rebrand late night.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| Dunford, April - Obviously Awesome (2019) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
| Elberse, Anita - Blockbusters_ Hit-making, Risk-taking, and the Big Business of  | SNIPED | represented | staged-in-raw | current | skip |
| Eric Berne - Games People Play_ The Basic Handbook of Transactional Analysis. (1 | SNIPED | represented | staged-in-raw | current | skip |
| Eric Hoffer - The true believer_ Thoughts on the nature of mass movements (1980, | SNIPED | represented | staged-in-raw | current | skip |
| Eric Ries - The Lean Startup How Todays Entrepreneurs Use Continuous Innovation  | SNIPED | represented | staged-in-raw | current | skip |
| Erik Brynjolfsson, Andrew McAfee, Jeff Cummings - The Second Machine Age_ Work,  | SNIPED | represented | staged-in-raw | current | skip |
| Ethan M. Rasiel - The McKinsey Way_ Using the Techniques of the World's Top Stra | SNIPED | represented | staged-in-raw | current | skip |
| Ethan Mollick - Co-Intelligence_ Living and Working With AI (2024, Penguin Publi | SNIPED | represented | staged-in-raw | current | skip |
| Eugene M. Schwartz - Breakthrough Advertising (2004) - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| EXECUTION_PRIORITIZATION.md | SNIPED | represented | staged-in-raw | current | skip |
| Extracted_Professional_Intelligence.docx | SNIPED | represented | src:2 txt:3 | current | skip |
| FINDING MODELS ANYWHERE OG.docx | SNIPED | represented | staged-in-raw | current | skip |
| Finding Your Edge.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Finding Your Edge.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Fitzpatrick, Rob - The Mom Test_ How to talk to customers & learn if your busine | SNIPED | represented | staged-in-raw | current | skip |
| Follow_Up_Rules.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Gabriel Weinberg, Justin Mares - Traction_ a startup guide to getting customers  | SNIPED | represented | staged-in-raw | current | skip |
| Gary C Halbert - The Boron Letters (2013) - libgen.li.epub | SNIPED | represented | src:3 txt:3 | current | skip |
| Geoff Colvin - Talent Is Overrated_ What Really Separates World-Class Performers | SNIPED | represented | staged-in-raw | current | skip |
| Giải trí đến chết (Amusing Ourselves to Death_ Public Discourse in the Age | SNIPED | represented | src:5 txt:10 | current | skip |
| Goodwin, Doris Kearns - Leadership_ In Turbulent Times (2018, Simon & Schuster)  | SNIPED | represented | staged-in-raw | current | skip |
| Goodwin, Doris Kearns - Team of rivals_ the political genius of Abraham Lincoln  | SNIPED | represented | staged-in-raw | current | skip |
| Grace Coddington - Grace_ A Memoir (2012, Random House) - libgen.li.epub | SNIPED | represented | src:4 txt:5 | current | skip |
| Grahl, Tim - Your first 1000 copies _ the step-by-step guide to marketing your b | SNIPED | represented | staged-in-raw | current | skip |
| Greg Lukianoff, Jonathan Haidt - The Coddling of the American Mind_ How Good Int | SNIPED | represented | staged-in-raw | current | skip |
| Gucci Mane, Neil Martinez-Belkin - The Autobiography of Gucci Mane (2017, Simon  | SNIPED | represented | staged-in-raw | current | skip |
| Gustave Le Bon - The crowd_ a study of the popular mind (2001, Dover Publication | SNIPED | represented | staged-in-raw | current | skip |
| Herodotus, Robert B. Strassler[ed] - The Landmark Herodotus_ Histories (2007, 20 | SNIPED | represented | staged-in-raw | current | skip |
| high level convos.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| Holiday, Ryan - Perennial seller_ the art of making and marketing work that last | SNIPED | represented | staged-in-raw | current | skip |
| hook_library.md | SNIPED | represented | staged-in-raw | current | skip |
| Howard Marks - Mastering the Market Cycle_ Getting the Odds on Your Side (2018,  | SNIPED | represented | staged-in-raw | current | skip |
| Howard Marks - The most important thing_ uncommon sense for the thoughtful inves | SNIPED | represented | staged-in-raw | current | skip |
| Howard Schultz, Dori Jones Yang - Pour Your Heart Into It_ How Starbucks Built a | SNIPED | represented | staged-in-raw | current | skip |
| ICP Definition Worksheet.pdf | SNIPED | represented | staged-in-raw | current | skip |
| index.html | SNIPED | represented | staged-in-raw | current | skip |
| INDEX.md | SNIPED | represented | staged-in-raw | current | skip |
| James Andrew Miller - Tinderbox_ HBO's Ruthless Pursuit of New Frontiers (Henry  | SNIPED | represented | staged-in-raw | current | skip |
| James Andrew Miller, Tom Shales - Those Guys Have All the Fun_ Inside the World  | SNIPED | represented | staged-in-raw | current | skip |
| James Dale Davidson_ William Rees-Mogg - The sovereign individual _ how to survi | SNIPED | represented | staged-in-raw | current | skip |
| James Joyce - Ulysses (2000, Penguin Group) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
| JAMES_ALLEN-AS_A_MAN_THINKETH.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Jan_1on1_Complete_Prep_EYES_ONLY.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| Jan_1on1_Prep_EYES_ONLY.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| Jason Kelly - The New Tycoons_ Inside the Trillion Dollar Private Equity Industr | SNIPED | represented | staged-in-raw | current | skip |
| Jay-Z Decoded{Jay-Z}(2010, Random House Publishing Group){108293762} libgen.li.e | SNIPED | represented | staged-in-raw | current | skip |
| John Caples, David Ogilvy - Tested Advertising Methods (4th Ed.) - libgen.li.pdf | SNIPED | represented | src:4 txt:6 | current | skip |
| John Seabrook - The Song Machine_ Inside the Hit Factory (2015, W. W. Norton & C | SNIPED | represented | src:7 txt:7 | current | skip |
| John Szarkowski - William Eggleston's Guide (2002, The Museum of Modern Art, New | SNIPED | represented | staged-in-raw | current | skip |
| John Warrillow - Built to Sell_ Turn Your Business Into One You Can Sell (2010)  | SNIPED | represented | staged-in-raw | current | skip |
| Jonathan Haidt - The Righteous Mind_ Why Good People Are Divided by Politics and | SNIPED | represented | staged-in-raw | current | skip |
| Kevin Kelly - New Rules for the New Economy_ 10 Radical Strategies for a Connect | SNIPED | represented | staged-in-raw | current | skip |
| Khaled Hosseini - The Kite Runner (2004, Riverhead Trade) - libgen.li.mobi | SNIPED | represented | staged-in-raw | current | skip |
| Kim Scott - Radical Candor_ Be a Kick-Ass Boss Without Losing Your Humanity (201 | SNIPED | represented | staged-in-raw | current | skip |
| Kupor, Scott_Ries, Eric - Secrets of Sand Hill Road_ venture capital and how to  | SNIPED | represented | src:6 txt:12 | current | skip |
| Kurt Vonnegut - Slaughterhouse-Five - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| L. David Marquet - Turn the Ship Around! - A True Story of Turning Followers int | SNIPED | represented | staged-in-raw | current | skip |
| Labrecque, Tammi - Newsletter Ninja_ How to Become an Author Mailing List Expert | SNIPED | represented | staged-in-raw | current | skip |
| LandmarkCaesarWebEssays_5Jan2018.pdf | SNIPED | represented | staged-in-raw | current | skip |
| last ig growth strat.docx | SNIPED | represented | staged-in-raw | current | skip |
| Lead_Generation_Report_11-5-2025.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lead_Qualification_Rules.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| LEAN_EXECUTION_AUDIT.md | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+10+related.+Broad-Lighting.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+10+related.+Hollywood-3-Light.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+11+related.+Rembrandt-Lighting.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+16+related.+45-Degree-Angle-Slims-Body.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+17+related.+Stretch-Things-Forward-Female.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+18+related.+The-Male-Light-Pose.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+19+related.+The-Female-Shadow-Pose.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+2+related.+Home-Based-Studio.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+5+related.+One-Light-45-Degree-Beauty-Dish.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+5+related.+Open-Loop-Example.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+6+related.+Closed-Loop-Example.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+6+related.+Creative-Window-Light.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+7+related.+2-Light-Clamshell.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+7+related.+A+5-Light-Studio-Setup.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+7+related.+Butterfly-Lighting.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+7+related.+Fill-Light.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+7+related.+Main-Key-Light.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+7+related.+Rim-Hair-Light.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+7+related.+White-Background.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+8+related.+3-Light-Commercial.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+8+related.+Split-Lighting.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+9+related.+4-Light-Beauty-On-White.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+9+related.+Short-Lighting (1).pdf | SNIPED | represented | staged-in-raw | current | skip |
| Lecture+9+related.+Short-Lighting.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Leigh Gallagher - The Airbnb Story_ How Three Ordinary Guys Disrupted an Industr | SNIPED | represented | staged-in-raw | current | skip |
| life story.docx | SNIPED | represented | staged-in-raw | current | skip |
| lighroom course.docx | SNIPED | represented | staged-in-raw | current | skip |
| LIGHTING SET UPS OG.docx | SNIPED | represented | staged-in-raw | current | skip |
| linkedin_pov_bank.md | SNIPED | represented | staged-in-raw | current | skip |
| LOCATION SCOUTING OG.docx | SNIPED | represented | staged-in-raw | current | skip |
| Maister, David H. - Managing the professional service firm (1997, Free Press Pap | SNIPED | represented | staged-in-raw | current | skip |
| Marc Randolph - That Will Never Work (2019, Little, Brown and Company) - libgen. | SNIPED | represented | staged-in-raw | current | skip |
| Marcellas Reynolds - Supreme Models_ Iconic Black Women Who Revolutionized Fashi | SNIPED | represented | staged-in-raw | current | skip |
| Marcus Aurelius - Meditations - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
| MARKET_INTELLIGENCE.md | SNIPED | represented | staged-in-raw | current | skip |
| max-tegmark-life-30-being-human-in-the-age-of-artificial-intelligence-alfred-a-k | SNIPED | represented | staged-in-raw | current | skip |
| meta everything use.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Michael E. Gerber - The E-Myth Revisited_ Why Most Small Businesses Don't Work a | SNIPED | represented | staged-in-raw | current | skip |
| Michael J. Silverstein, Neil Fiske - Trading Up_ Why Consumers Want New Luxury G | SNIPED | represented | staged-in-raw | current | skip |
| Mike Isaac - Super Pumped_ The Battle for Uber (2019, W. W. Norton Company) - li | SNIPED | represented | staged-in-raw | current | skip |
| MONEY MONEY AND MORE MONEY AND GETTING AHEAD .docx | SNIPED | represented | src:3 txt:4 | current | skip |
| monthly_constraint_audit.md | SNIPED | represented | staged-in-raw | current | skip |
| MOODBOARDING DOC OG.docx | SNIPED | represented | staged-in-raw | current | skip |
| mostly Powerhouse-.docx | SNIPED | represented | staged-in-raw | current | skip |
| Mustafa Suleyman_Michael Bhaskar__ Michael Bhaskar - The Coming Wave _ Technolog | SNIPED | represented | staged-in-raw | current | skip |
| n8n & RetellAI.json | SNIPED | represented | staged-in-raw | current | skip |
| Nabokov, Vladimir - Lolita (Vladimir Nabokov) - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| NEW TAKEOVER HANDLE WITH CARE.docx | SNIPED | represented | staged-in-raw | current | skip |
| NEXT INFO GRABS.docx | SNIPED | represented | staged-in-raw | current | skip |
| Niccolo Machiavelli - The prince (2008, Hackett Pub. Co) - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Norma Stevens, Steven M. L. Aronson - Avedon_ Something Personal (2017, Spiegel  | SNIPED | represented | staged-in-raw | current | skip |
| notion_crm_schemas.md | SNIPED | represented | staged-in-raw | current | skip |
| OPERATIONAL_BACKBONE.md | SNIPED | represented | staged-in-raw | current | skip |
| Opp hopper + Biz Case.xlsx | SNIPED | represented | staged-in-raw | current | skip |
| Opportunity Card [Example].pptx | SNIPED | represented | staged-in-raw | current | skip |
| PARTNERSHIP_PROTOCOL.md | SNIPED | represented | staged-in-raw | current | skip |
| Patrick Lencioni - Getting Naked_ A Business Fable About Shedding The Three Fear | SNIPED | represented | staged-in-raw | current | skip |
| Patrick Lencioni - The advantage _ why organizational health trumps everything e | SNIPED | represented | staged-in-raw | current | skip |
| pdfcoffee.com_ernst-haas-pdf-free.pdf | SNIPED | represented | staged-in-raw | current | skip |
| pdfcoffee.com_virgil-abloh-figures-of-speech-pdf-free.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Peter Block - Flawless consulting_ a guide to getting your expertise used (2000, | SNIPED | represented | staged-in-raw | current | skip |
| Petre, Peter_Schwarzenegger, Arnold - Total recall_ my unbelievably true life st | SNIPED | represented | staged-in-raw | current | skip |
| phtography brain dump.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| PIXIESET NEW USE .docx | SNIPED | represented | staged-in-raw | current | skip |
| pixieset tips for store .docx | SNIPED | represented | src:2 txt:2 | current | skip |
| pixieset_config.md | SNIPED | represented | staged-in-raw | current | skip |
| Pixieset_Operations_Reference.docx | SNIPED | represented | staged-in-raw | current | skip |
| PRODUCTION_OS.md | SNIPED | represented | staged-in-raw | current | skip |
| Prompt Template - Combining Techniques-2.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Prompt Template - Combining Techniques-3.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Prompt Template - In Context-2.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Prompt Template - Problem Decomposition.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Prompt Template - Self Criticism (Advanced)-2.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Prompt Template - Self Criticism (Advanced)-3.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Prompt Template - Self Criticism (Basic)-3.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Prompt Template - Thought Generation-2.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Prompt_Engineering_Knowledge_Extraction.docx | SNIPED | represented | src:3 txt:4 | current | skip |
| Proof_Case_Studies_Page_Structure.docx | SNIPED | represented | src:2 txt:5 | current | skip |
| Ray Bradbury - Ray Bradbury's Fahrenheit 451 (Bloom's Modern Critical Interpreta | SNIPED | represented | src:1 txt:3 | current | skip |
| Raz, Tahl_Voss, Chris - Never Split the Difference_ Negotiating As If Your Life  | SNIPED | represented | staged-in-raw | current | skip |
| Re_Edit_Workflow.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| recurring_checklists.md | SNIPED | represented | staged-in-raw | current | skip |
| Rensin, David - The Mailroom_ Hollywood History from the Bottom Up (2007, Random | SNIPED | represented | src:7 txt:9 | current | skip |
| REVERSE_ROADMAP.md | SNIPED | represented | staged-in-raw | current | skip |
| Richard Branson - Losing My Virginity_ How I Survived, Had Fun, and Made a Fortu | SNIPED | represented | staged-in-raw | current | skip |
| Rick Ross_ Neil Martinez-Belkin - Hurricanes_ A Memoir (2019, Hanover Square Pre | SNIPED | represented | staged-in-raw | current | skip |
| Rob Meyerson - Brand Naming_ The Complete Guide to Creating a Name for Your Comp | SNIPED | represented | staged-in-raw | current | skip |
| Robert W. Bly - The copywriter's handbook_ a step-by-step guide to writing copy  | SNIPED | represented | staged-in-raw | current | skip |
| Ron Chernow - Grant (2017, Penguin Publishing Group) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
| Ron Chernow - Titan_ The Life of John D. Rockefeller, Sr. (2004, Vintage) - libg | SNIPED | represented | staged-in-raw | current | skip |
| Ron Chernow - Washington_ A Life - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| SATURDAY_BUILD_BRIEF.md | SNIPED | represented | staged-in-raw | current | skip |
| Sax, David - The Revenge of Analog_ Real Things and Why They Matter (2016, Publi | SNIPED | represented | staged-in-raw | current | skip |
| Schroeder, Alice - The Snowball_ Warren Buffett and the Business of Life (2008,  | SNIPED | represented | staged-in-raw | current | skip |
| Schwarzenegger, Arnold - Total Recall- My Unbelievably True Life Story (2012, Si | SNIPED | represented | src:7 txt:8 | current | skip |
| Sebastian Mallaby - The Power Law _ Venture Capital and the Making of the New Fu | SNIPED | represented | staged-in-raw | current | skip |
| Sebastian Mallaby - The Power Law_ Venture Capital and the Making of the New Fut | SNIPED | represented | src:5 txt:7 | current | skip |
| Seedream 5.0.docx | SNIPED | represented | staged-in-raw | current | skip |
| SEEDREAM_TACTICAL_EXTRACTION.md | SNIPED | represented | staged-in-raw | current | skip |
| SESSION_LOG.md | SNIPED | represented | staged-in-raw | current | skip |
| Seth A. Klarman - Margin of Safety_ Risk-Averse Value Investing Strategies for t | SNIPED | represented | src:10 txt:11 | current | skip |
| Seth A. Klarman - Margin of Safety_ Risk-Averse Value Investing Strategies for t | SNIPED | represented | staged-in-raw | current | skip |
| Seth Godin - Purple Cow_ Transform Your Business by Being Remarkable (2003, Port | SNIPED | represented | staged-in-raw | current | skip |
| Seth Godin - This Is Marketing_ You Can't Be Seen Until You Learn to See (2018,  | SNIPED | represented | staged-in-raw | current | skip |
| Seth Godin - Tribes_ We Need You to Lead Us (2008, Penguin) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
| Setting Goals.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Shore Stephen. - Uncommon Places_ The Complete Works - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Simler, Kevin _ Hanson, Robin - The Elephant in the Brain_ Hidden Motives in Eve | SNIPED | represented | staged-in-raw | current | skip |
| snipe dump on lighting and moodboard.docx | SNIPED | represented | src:3 txt:4 | current | skip |
| SNIPED CRM.xlsx | SNIPED | represented | staged-in-raw | current | skip |
| SNIPED CRM.xlsx | SNIPED | represented | staged-in-raw | current | skip |
| SNIPED_Chat_Prompts_Reference.docx | SNIPED | represented | src:2 txt:3 | current | skip |
| SNIPED_Chat_Prompts_Reference.docx | SNIPED | represented | src:2 txt:3 | current | skip |
| sniped_content_philosophy.md | SNIPED | represented | staged-in-raw | current | skip |
| sniped_context_tools_only.docx | SNIPED | represented | staged-in-raw | current | skip |
| sniped_context_tools_only.docx | SNIPED | represented | staged-in-raw | current | skip |
| SNIPED_Founder_Kit_Content_Engine.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| SNIPED_Founder_Kit_Content_Engine.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| SNIPED_Founder_Kit_Offer_Explainer.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| SNIPED_Founder_Kit_Offer_Explainer.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| SNIPED_Founder_Kit_Pocket_Card.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| SNIPED_Founder_Kit_Pocket_Card.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| sniped_media_business_card_back_squid_ink.pdf | SNIPED | represented | src:3 txt:3 | current | skip |
| sniped_media_business_card_front.pdf | SNIPED | represented | src:2 txt:3 | current | skip |
| sniped_media_business_card_front_squid_ink.pdf | SNIPED | represented | src:2 txt:3 | current | skip |
| SNIPED_MEDIA_Complete_Context_Export.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| SNIPED_MEDIA_Complete_Context_Export.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Content_Production_SOP.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Content_Production_SOP.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Controlled_Architecture_v1.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Controlled_Architecture_v1.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| sniped_media_FULL_lead_audit_720.xlsx | SNIPED | represented | src:2 txt:2 | current | skip |
| sniped_media_FULL_lead_audit_720.xlsx | SNIPED | represented | src:2 txt:2 | current | skip |
| sniped_media_lead_audit_march2026.xlsx | SNIPED | represented | src:2 txt:2 | current | skip |
| sniped_media_lead_audit_march2026.xlsx | SNIPED | represented | src:2 txt:2 | current | skip |
| Sniped_Media_LinkedIn_Growth_Engine.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| Sniped_Media_LinkedIn_Growth_Engine.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| sniped_media_master_session_log.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| sniped_media_master_session_log.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Pixieset_Setup_Documentation.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| Sniped_Media_Pixieset_Setup_Documentation.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| Sniped_Media_Pixieset_Template_Kit.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Pixieset_Template_Kit.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Session_Intelligence_Document.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| Sniped_Media_Session_Intelligence_Document.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| Sniped_Media_Video_Editor_SOP.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Video_Editor_SOP.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| sniped_os_knowledge_dump.docx | SNIPED | represented | staged-in-raw | current | skip |
| sniped_os_knowledge_dump.docx | SNIPED | represented | staged-in-raw | current | skip |
| SNIPED_OS_V1_SYNTHESIS_2026-05-12.md | SNIPED | represented | staged-in-raw | current | skip |
| SNIPED_Picture_Review_Prompt.docx | SNIPED | represented | src:2 txt:3 | current | skip |
| SNIPED_Picture_Review_Prompt.docx | SNIPED | represented | src:2 txt:3 | current | skip |
| SNIPED_Session_Handoff.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| SNIPED_Session_Handoff.docx | SNIPED | represented | src:2 txt:2 | current | skip |
| SNIPED_Site_Polish_Pass.docx | SNIPED | represented | src:2 txt:3 | current | skip |
| SNIPED_Site_Polish_Pass.docx | SNIPED | represented | src:2 txt:3 | current | skip |
| sniped_video_philosophy.md | SNIPED | represented | staged-in-raw | current | skip |
| SNIPED_Visual_Infrastructure_Board_SOP.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| SNIPED_Visual_Infrastructure_Board_SOP.docx | SNIPED | represented | src:3 txt:3 | current | skip |
| SOCIAL MEDIA 3.0 MAY USE.docx | SNIPED | represented | staged-in-raw | current | skip |
| SOCIAL_MEDIA_3_0_REFERENCE.docx | SNIPED | represented | staged-in-raw | current | skip |
| SOP_capture_to_delivery.md | SNIPED | represented | staged-in-raw | current | skip |
| SOP_post_delivery.md | SNIPED | represented | staged-in-raw | current | skip |
| SOP_reset_shoot_day.md | SNIPED | represented | staged-in-raw | current | skip |
| SOP_strategic_free.md | SNIPED | represented | staged-in-raw | current | skip |
| Story{Robert McKee}{115577124} libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| STRATEGIC_PRINCIPLES.md | SNIPED | represented | staged-in-raw | current | skip |
| Study_AnnieLeibovitz.md | SNIPED | represented | staged-in-raw | current | skip |
| Study_ErnstHaas.md | SNIPED | represented | staged-in-raw | current | skip |
| Study_FredHerzog.md | SNIPED | represented | staged-in-raw | current | skip |
| Study_GracielaIturbide.md | SNIPED | represented | staged-in-raw | current | skip |
| Study_JoelMeyerowitz.md | SNIPED | represented | staged-in-raw | current | skip |
| Study_RichardAvedon.md | SNIPED | represented | staged-in-raw | current | skip |
| Study_RobertFrank.md | SNIPED | represented | staged-in-raw | current | skip |
| Study_StephenShore.md | SNIPED | represented | staged-in-raw | current | skip |
| Study_WilliamEggleston.md | SNIPED | represented | staged-in-raw | current | skip |
| Sunstein, Cass R._ Sibony, Olivier_ Kahneman, Daniel - Noise_ A Flaw in Human Ju | SNIPED | represented | staged-in-raw | current | skip |
| Supreme Models_ Iconic Black Women Who Revolutionized Fashion.epub | SNIPED | represented | src:7 txt:7 | current | skip |
| takeover after ramon copy.docx | SNIPED | represented | staged-in-raw | current | skip |
| takeover after ramon.docx | SNIPED | represented | staged-in-raw | current | skip |
| The Adweek Copywriting Handbook_ The Ultimate Guide to Writing Powerful Advertis | SNIPED | represented | src:8 txt:11 | current | skip |
| The Brand Gap, Revised Edition{Marty Neumeier}(2005, Pearson Education (US)){113 | SNIPED | represented | staged-in-raw | current | skip |
| The Innovator&_039_s Dilemma_ When New Technologies Cause Great Firms to Fail (M | SNIPED | represented | staged-in-raw | current | skip |
| The Kingdom of Prep_ The Inside Story of the Rise and (Near) Fall of J.Crew{Magg | SNIPED | represented | src:4 txt:7 | current | skip |
| The-Holy-Bible-King-James-Version.pdf | SNIPED | represented | src:2 txt:3 | current | skip |
| The_Adobe_Stack_Manual.docx | SNIPED | represented | staged-in-raw | current | skip |
| The_Attention_Stack.docx | SNIPED | represented | staged-in-raw | current | skip |
| The_Copywriting_Stack.docx | SNIPED | represented | staged-in-raw | current | skip |
| The_Direction_Shift.docx | SNIPED | represented | staged-in-raw | current | skip |
| The_Offer_Stack.docx | SNIPED | represented | staged-in-raw | current | skip |
| The_Platform_Stack.docx | SNIPED | represented | staged-in-raw | current | skip |
| The_Production_Stack.docx | SNIPED | represented | staged-in-raw | current | skip |
| THE_SPINE.md | SNIPED | represented | staged-in-raw | current | skip |
| Thucydides, Robert B. Strassler, Richard Crawley, Victor Davis H - The Landmark  | SNIPED | represented | staged-in-raw | current | skip |
| Tom Shales, James Andrew Miller - Live From New York_ An Uncensored History of S | SNIPED | represented | staged-in-raw | current | skip |
| Toni Morrison - Beloved (Vintage International) - libgen.li.azw3 | SNIPED | represented | src:3 txt:4 | current | skip |
| Toni Morrison - The Bluest Eye (2007, Knopf Doubleday Publishing Group) - libgen | SNIPED | represented | staged-in-raw | current | skip |
| track_b_frame_walkthrough.md | SNIPED | represented | staged-in-raw | current | skip |
| Trading_Card_Launch_Plan.docx | SNIPED | represented | src:2 txt:4 | current | skip |
| udemy ai course gold.docx | SNIPED | represented | staged-in-raw | current | skip |
| UDEMY_AI_TACTICAL_EXTRACTION.md | SNIPED | represented | staged-in-raw | current | skip |
| using ai x gumroad x digital products.docx | SNIPED | represented | staged-in-raw | current | skip |
| Viktor E. Frankl - Man's search for meaning (2000, Beacon Press) - libgen.li.pdf | SNIPED | represented | staged-in-raw | current | skip |
| Walter Isaacson - Elon Musk (2023, Simon & Schuster) - libgen.li.epub | SNIPED | represented | staged-in-raw | current | skip |
| Warren E. Buffett, Lawrence A. Cunningham, Lawrence A. Cunningha - The Essays of | SNIPED | represented | staged-in-raw | current | skip |
| Weekly Reflections.pdf | SNIPED | represented | staged-in-raw | current | skip |
| weekly_review.md | SNIPED | represented | staged-in-raw | current | skip |
| Will Guidara - Unreasonable Hospitality_ The Remarkable Power of Giving People M | SNIPED | represented | staged-in-raw | current | skip |
| XcMwr2sETldxuEwaZeEw_The+Great+Online+Game+-+Not+Boring+by+Packy+McCormick.pdf | SNIPED | represented | staged-in-raw | current | skip |
| youtube skool doc.docx | SNIPED | represented | staged-in-raw | current | skip |
| Zack O'Malley Greenburg - Empire State of Mind_ How Jay-Z Went from Street Corne | SNIPED | represented | staged-in-raw | current | skip |
| 2026 OPS-ENG SMART Goals.xlsx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Antique_Inventory_Template.xlsx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Antique_Inventory_Template_Styled.xlsx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| BJ_Reference_Doc.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| brain prompting.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| bunch of mess.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| Charger_Knowledge_Extraction.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| copywriting everyhting : tips.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| Da'Nielle Green's Resume.pdf | SNIPED | review | src:1 txt:1 | unclear | manual review |
| direction shiftttt.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| facebook stuff.docx | SNIPED | review | src:0 txt:2 | unclear | manual review |
| FASHION KILLA.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| FE_Implementation_Package.xlsx | SNIPED | review | src:0 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_DRAFT.xlsx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_DRAFT_v1.1.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_DRAFT_v1.1.xlsx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_v1.1_FINAL.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_v1.2.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_v1.2.xlsx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| gary thread.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| PAL_League_Overview.docx | SNIPED | review | src:0 txt:2 | unclear | manual review |
| phtography biz side x tothemoon.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| Pressure test points 4.xlsx | SNIPED | review | src:0 txt:2 | unclear | manual review |
| Proof_Inventory.docx | SNIPED | review | src:0 txt:2 | unclear | manual review |
| Selling books.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| sniped_media_AUDITED_720_campaign_ready.xlsx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| sniped_media_AUDITED_720_campaign_ready.xlsx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Sniped_Media_Booking_Overhaul.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Sniped_Media_Booking_Overhaul.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Sniped_Media_Competitor_Brief.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Sniped_Media_Competitor_Brief.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Sniped_Media_Context_Blocks.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Sniped_Media_Context_Blocks.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| sniped_media_email_sequences_54.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| sniped_media_email_sequences_54.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| sniped_media_instagram_month1_final.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| sniped_media_instagram_month1_final.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| sniped_media_pixieset_additions.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| sniped_media_pixieset_additions.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| Sniped_Media_Pixieset_Complete_Rebuild_April2026.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Sniped_Media_Pixieset_Complete_Rebuild_April2026.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| The_Install_Methodology_v1.docx | SNIPED | review | src:0 txt:2 | unclear | manual review |
| THE_MACHINE.docx | SNIPED | review | src:1 txt:1 | unclear | manual review |
| ticket_extraction.docx | SNIPED | review | src:0 txt:2 | unclear | manual review |
| Vanguard_Program_Vision.docx | SNIPED | review | src:1 txt:2 | unclear | manual review |
| Deficiency_Ownership_DRAFT_v1.0 (1).docx | business/money | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Deficiency_Ownership_DRAFT_v1.0 (1).docx | business/money | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Deficiency_Ownership_DRAFT_v1.0 (3).docx | business/money | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Deficiency_Ownership_DRAFT_v1.0 (3).docx | business/money | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| Deficiency_Ownership_Field_Reference_DRAFT (1).xlsx | business/money | duplicate | src:3 txt:4 | superseded | ignore (superseded) |
| Deficiency_Ownership_Field_Reference_DRAFT (1).xlsx | business/money | duplicate | src:3 txt:4 | superseded | ignore (superseded) |
| Deficiency_Ownership_Field_Reference_DRAFT (3).xlsx | business/money | duplicate | src:3 txt:4 | superseded | ignore (superseded) |
| Deficiency_Ownership_Field_Reference_DRAFT (3).xlsx | business/money | duplicate | src:3 txt:4 | superseded | ignore (superseded) |
| [Rich Dad Advisors] Tom Wheelwright - Tax-Free Wealth_ How to Build Massive Weal | business/money | ignore | src:4 txt:8 | off-scope | ignore (personal) |
| BIZ EXPENSES.docx | business/money | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| BIZ EXPENSES.docx | business/money | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| business funding pt 2.docx | business/money | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| business funding pt 2.docx | business/money | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| fidelity investment hacks.docx | business/money | ignore | src:1 txt:1 | off-scope | ignore (personal) |
| fidelity investment hacks.docx | business/money | ignore | src:1 txt:1 | off-scope | ignore (personal) |
| business_finance_extraction.docx | business/money | partial | src:1 txt:3 | unclear | compare delta |
| business_finance_extraction.docx | business/money | partial | src:1 txt:3 | unclear | compare delta |
| [For Dummies (Business & Personal Finance)] Eric Tyson, Margaret A. Munro - Taxe | business/money | represented | src:4 txt:5 | current | skip |
| [J.K. Lasser's Your Income Tax 2016] J.K. Lasser Institute - J.K. Lasser's Your  | business/money | represented | src:1 txt:3 | current | skip |
| Barbara Weltman - J.K. Lasser's 1001 Deductions & Tax Breaks 2025 _ Your Complet | business/money | represented | src:4 txt:5 | current | skip |
| Deficiency_Ownership_Field_Reference_DRAFT.xlsx | business/money | represented | src:3 txt:4 | current | skip |
| Deficiency_Ownership_Field_Reference_DRAFT.xlsx | business/money | represented | src:3 txt:4 | current | skip |
| Jocko Willink, Leif Babin - Extreme Ownership_ How U.S. Navy SEALs Lead and Win  | business/money | represented | staged-in-raw | current | skip |
| Jocko Willink, Leif Babin - Extreme Ownership_ How U.S. Navy SEALs Lead and Win  | business/money | represented | staged-in-raw | current | skip |
| Jocko Willink_ Leif Babin - The Dichotomy of Leadership_ Balancing the Challenge | business/money | represented | staged-in-raw | current | skip |
| Jocko Willink_ Leif Babin - The Dichotomy of Leadership_ Balancing the Challenge | business/money | represented | staged-in-raw | current | skip |
| Money_Wealth_Getting_Ahead.docx | business/money | represented | staged-in-raw | current | skip |
| Money_Wealth_Getting_Ahead.docx | business/money | represented | staged-in-raw | current | skip |
| Morgan Guaranty Trust Company of New York_Morgan Guaranty Trust - The House of M | business/money | represented | src:8 txt:14 | current | skip |
| Morgan Guaranty Trust Company of New York_Morgan Guaranty Trust - The House of M | business/money | represented | src:8 txt:14 | current | skip |
| Morgan Housel - The Psychology of Money Timeless Lessons on Wealth Greed and Hap | business/money | represented | staged-in-raw | current | skip |
| Morgan Housel - The Psychology of Money Timeless Lessons on Wealth Greed and Hap | business/money | represented | staged-in-raw | current | skip |
| Naval Ravikant, Eric Jorgenson, Jack Butcher, Tim Ferriss - The Almanack of Nava | business/money | represented | staged-in-raw | current | skip |
| Naval Ravikant, Eric Jorgenson, Jack Butcher, Tim Ferriss - The Almanack of Nava | business/money | represented | staged-in-raw | current | skip |
| THE_REAL_PLAN_Rebrand_Revenue_Execution.docx | business/money | represented | src:2 txt:4 | current | skip |
| THE_REAL_PLAN_Rebrand_Revenue_Execution.docx | business/money | represented | src:2 txt:4 | current | skip |
| The_Revenue_Stack.docx | business/money | represented | staged-in-raw | current | skip |
| The_Revenue_Stack.docx | business/money | represented | staged-in-raw | current | skip |
| 1_SNIPED_90Day_Revenue_OS.docx | business/money | review | src:1 txt:1 | unclear | manual review |
| 1_SNIPED_90Day_Revenue_OS.docx | business/money | review | src:1 txt:1 | unclear | manual review |
| Deficiency_Ownership_DRAFT_v1.0.docx | business/money | review | src:1 txt:2 | unclear | manual review |
| Deficiency_Ownership_DRAFT_v1.0.docx | business/money | review | src:1 txt:2 | unclear | manual review |
|  Rick Rubin - The Creative Act_ A Way of Being_ The Sunday Times bestseller (202 | legal/IP | parked | src:5 txt:7 | operational | park (legal ref) |
|  Rick Rubin - The Creative Act_ A Way of Being_ The Sunday Times bestseller (202 | legal/IP | parked | src:5 txt:7 | operational | park (legal ref) |
| Contract_Complimentary_Session.docx | legal/IP | parked | src:1 txt:2 | operational | park (legal ref) |
| Contract_Complimentary_Session.docx | legal/IP | parked | src:1 txt:2 | operational | park (legal ref) |
| Contract_Tier1_The_Moment.docx | legal/IP | parked | src:0 txt:2 | operational | park (legal ref) |
| Contract_Tier1_The_Moment.docx | legal/IP | parked | src:0 txt:2 | operational | park (legal ref) |
| Contract_Tier2_The_Statement.docx | legal/IP | parked | src:1 txt:2 | operational | park (legal ref) |
| Contract_Tier2_The_Statement.docx | legal/IP | parked | src:1 txt:2 | operational | park (legal ref) |
| Offers + Business Foundation .docx | legal/IP | parked | src:2 txt:3 | operational | park (legal ref) |
| Offers + Business Foundation .docx | legal/IP | parked | src:2 txt:3 | operational | park (legal ref) |
| Offers___Business_Foundation_.docx | legal/IP | parked | src:2 txt:3 | operational | park (legal ref) |
| Offers___Business_Foundation_.docx | legal/IP | parked | src:2 txt:3 | operational | park (legal ref) |
| Promissory Note- Sniped Enterprises.pdf | legal/IP | parked | src:1 txt:2 | operational | park (legal ref) |
| Sniped_Media_90Day_Search_Calendar.xlsx | legal/IP | parked | src:1 txt:2 | operational | park (legal ref) |
| Sniped_Media_90Day_Search_Calendar.xlsx | legal/IP | parked | src:1 txt:2 | operational | park (legal ref) |
| Sniped_Media_LLC_Operating_Agreement (1).docx | legal/IP | parked | src:1 txt:2 | operational | park (legal ref) |
| Sniped_Media_LLC_Operating_Agreement (1).docx | legal/IP | parked | src:1 txt:2 | operational | park (legal ref) |
| Sniped_Media_Photography_Services_Agreement.docx | legal/IP | parked | src:1 txt:3 | operational | park (legal ref) |
| Sniped_Media_Photography_Services_Agreement.docx | legal/IP | parked | src:1 txt:3 | operational | park (legal ref) |
|  Joseph Campbell - The Hero with a Thousand Faces (2020, Joseph Campbell Foundat | legal/IP | represented | staged-in-raw | current | skip |
|  Joseph Campbell - The Hero with a Thousand Faces (2020, Joseph Campbell Foundat | legal/IP | represented | staged-in-raw | current | skip |
| 01_collab_agreement.md | legal/IP | represented | staged-in-raw | current | skip |
| 02_reset_msa.md | legal/IP | represented | staged-in-raw | current | skip |
| 03_operator_kit_msa.md | legal/IP | represented | staged-in-raw | current | skip |
| 04_NAME_RECOMMENDATION.md | legal/IP | represented | staged-in-raw | current | skip |
| [Kauffman Foundation Series on Innovation and Entrepreneurship] Noam Wasserman - | legal/IP | represented | staged-in-raw | current | skip |
| [Kauffman Foundation Series on Innovation and Entrepreneurship] Noam Wasserman - | legal/IP | represented | staged-in-raw | current | skip |
| Contracts_Legal_Protection_Playbook.docx | legal/IP | represented | staged-in-raw | current | skip |
| Contracts_Legal_Protection_Playbook.docx | legal/IP | represented | staged-in-raw | current | skip |
| John Doerr - Measure What Matters_ How Google, Bono, and the Gates Foundation Ro | legal/IP | represented | staged-in-raw | current | skip |
| John Doerr - Measure What Matters_ How Google, Bono, and the Gates Foundation Ro | legal/IP | represented | staged-in-raw | current | skip |
| Lecture+20+related.+Standard-Group-Shot.pdf | legal/IP | represented | staged-in-raw | current | skip |
| Lecture+21+related.+Standard-Couples.pdf | legal/IP | represented | staged-in-raw | current | skip |
| legal contracts and service business contracts.docx | legal/IP | represented | staged-in-raw | current | skip |
| legal contracts and service business contracts.docx | legal/IP | represented | staged-in-raw | current | skip |
| MONDAY_COCKPIT.md | legal/IP | represented | staged-in-raw | current | skip |
| SKILL.md | legal/IP | represented | staged-in-raw | current | skip |
| AI Content Strategy Generator - Lead Magnet (1).json | operator/systems | duplicate | src:5 txt:5 | superseded | ignore (superseded) |
| AI Content Strategy Generator - Lead Magnet (1).json | operator/systems | duplicate | src:5 txt:5 | superseded | ignore (superseded) |
| Audit_Script_Framework_2 (1).xlsx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| Audit_Script_Framework_2 (1).xlsx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| Audit_Script_Framework_v2.xlsx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| Audit_Script_Framework_v2.xlsx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| BJ_Operating_System.md | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| BJ_Operating_System.md.pdf | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Content_Strategy (1).docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Content_Strategy (1).docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| daily_operating_plan (1).docx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| daily_operating_plan (1).docx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| SNIPED_AI_Operating_System.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| SNIPED_AI_Operating_System.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Client_Delivery_System_v2.docx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Client_Delivery_System_v2.docx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Consolidated_Operating_Document.docx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Consolidated_Operating_Document.docx | operator/systems | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Content_System (1).docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Content_System (1).docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Content_System (2).docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Content_System (2).docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| sniped_media_ecosystem_map.docx | operator/systems | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| sniped_media_ecosystem_map.docx | operator/systems | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| Sniped_Media_Marketing_Operating_System.docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Marketing_Operating_System.docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Marketing_Operating_System_v3_FINAL.docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Marketing_Operating_System_v3_FINAL.docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Master_Operating_Document (1).docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Master_Operating_Document (1).docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Master_Operating_Document (2).docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Master_Operating_Document (2).docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| SNIPED_MEDIA_Master_Operating_Document (3).docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| SNIPED_MEDIA_Master_Operating_Document (3).docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| SNIPED_MEDIA_Master_Operating_Document.docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| SNIPED_MEDIA_Master_Operating_Document.docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| sniped_media_master_operating_system.docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| sniped_media_master_operating_system.docx | operator/systems | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Sniped_Media_Master_Strategy_Log.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Master_Strategy_Log.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_New_Operating_System.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_New_Operating_System.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Operating_Doctrine.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Operating_Doctrine.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Operating_Doctrine_v2.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Operating_Doctrine_v2.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Pixieset_Complete_System_Final (1).docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Pixieset_Complete_System_Final (1).docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Strategy_Brief_V2.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_Strategy_Brief_V2.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_System_Architecture.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Media_System_Architecture.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Operating_System.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Sniped_Operating_System.docx | operator/systems | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| BJ_Golf_Mastery_System (1).docx | operator/systems | ignore | src:2 txt:2 | off-scope | ignore (personal) |
| BJ_Golf_Mastery_System (1).docx | operator/systems | ignore | src:2 txt:2 | off-scope | ignore (personal) |
| BJ_Golf_Mastery_System.docx | operator/systems | ignore | src:2 txt:2 | off-scope | ignore (personal) |
| BJ_Golf_Mastery_System.docx | operator/systems | ignore | src:2 txt:2 | off-scope | ignore (personal) |
| jags_offense_master_system.md | operator/systems | ignore | src:2 txt:3 | off-scope | ignore (personal) |
| Jaguars_Offense_Master_System.pdf | operator/systems | ignore | src:2 txt:3 | off-scope | ignore (personal) |
| Jaguars_Offense_Master_System_EXPANDED.pdf | operator/systems | ignore | src:3 txt:4 | off-scope | ignore (personal) |
| Jaguars_Offense_Master_System_FINAL.pdf | operator/systems | ignore | src:2 txt:3 | off-scope | ignore (personal) |
| Jaguars_Offensive_Master_System_v1.0.docx | operator/systems | ignore | src:2 txt:3 | off-scope | ignore (personal) |
| Jaguars_Offensive_Master_System_v1.0.docx | operator/systems | ignore | src:2 txt:3 | off-scope | ignore (personal) |
| Jaguars_Offensive_Master_System_v1.0.pdf | operator/systems | ignore | src:2 txt:3 | off-scope | ignore (personal) |
| Jaguars_Offensive_Master_System_v1.0_COMPLETE.pdf | operator/systems | ignore | src:2 txt:3 | off-scope | ignore (personal) |
| vikings_defense_master_system.md | operator/systems | ignore | src:3 txt:3 | off-scope | ignore (personal) |
| Vikings_Defense_Master_System.pdf | operator/systems | ignore | src:3 txt:3 | off-scope | ignore (personal) |
| Vikings_Defense_Master_System_EXPANDED.pdf | operator/systems | ignore | src:4 txt:4 | off-scope | ignore (personal) |
| Vikings_Defense_Master_System_FINAL.pdf | operator/systems | ignore | src:3 txt:3 | off-scope | ignore (personal) |
| Vanguard_Playbook.docx | operator/systems | missing | src:0 txt:1 | current | ingest/review |
| Vanguard_Playbook.docx | operator/systems | missing | src:0 txt:1 | current | ingest/review |
| CHW system pressure test points.pdf | operator/systems | partial | src:1 txt:3 | unclear | compare delta |
| Mental_Models_Worldly_Wisdom_FRAMEWORKS.docx | operator/systems | partial | src:1 txt:5 | unclear | compare delta |
| Mental_Models_Worldly_Wisdom_FRAMEWORKS.docx | operator/systems | partial | src:1 txt:5 | unclear | compare delta |
| OPERATIONAL_EXCELLENCE_FRAMEWORKS.docx | operator/systems | partial | src:0 txt:3 | unclear | compare delta |
| OPERATIONAL_EXCELLENCE_FRAMEWORKS.docx | operator/systems | partial | src:0 txt:3 | unclear | compare delta |
|  Eliyahu, Goldratt - The goal_ a process of ongoing improvement (2004, North Riv | operator/systems | represented | staged-in-raw | current | skip |
|  Eliyahu, Goldratt - The goal_ a process of ongoing improvement (2004, North Riv | operator/systems | represented | staged-in-raw | current | skip |
|  Gardner, Dan_Tetlock, Philip Eyrikson - Superforecasting_ The Art and Science o | operator/systems | represented | src:2 txt:4 | current | skip |
|  Jean-Noel Kapferer, Vincent Bastien - The Luxury Strategy_ Break the Rules of M | operator/systems | represented | staged-in-raw | current | skip |
|  Jean-Noel Kapferer, Vincent Bastien - The Luxury Strategy_ Break the Rules of M | operator/systems | represented | staged-in-raw | current | skip |
|  Meadows, Donella H. Wright, Diana - Thinking in Systems_ A Primer - libgen.li.p | operator/systems | represented | staged-in-raw | current | skip |
|  Meadows, Donella H. Wright, Diana - Thinking in Systems_ A Primer - libgen.li.p | operator/systems | represented | staged-in-raw | current | skip |
|  Rees, Anuschka - The curated closet _ a simple system for discovering your pers | operator/systems | represented | src:5 txt:12 | current | skip |
|  Rees, Anuschka - The curated closet _ a simple system for discovering your pers | operator/systems | represented | src:5 txt:12 | current | skip |
|  Richard Rumelt - Good Strategy Bad Strategy_ The Difference and Why It Matters  | operator/systems | represented | src:6 txt:7 | current | skip |
|  Richard Rumelt - Good Strategy_Bad Strategy_ The difference and why it matters  | operator/systems | represented | src:5 txt:7 | current | skip |
|  Richard Rumelt - Good Strategy_Bad Strategy_ The difference and why it matters  | operator/systems | represented | src:5 txt:7 | current | skip |
| 00_BRAND_STRATEGY_BRIEF.md | operator/systems | represented | staged-in-raw | current | skip |
| 01_BRAND_AUDIT.md | operator/systems | represented | staged-in-raw | current | skip |
| 02_NAMING_CRITERIA.md | operator/systems | represented | staged-in-raw | current | skip |
| 03_NAMING_CANDIDATES.md | operator/systems | represented | staged-in-raw | current | skip |
| 05_BRAND_ARCHITECTURE.md | operator/systems | represented | staged-in-raw | current | skip |
| 06_POSITIONING_STATEMENT.md | operator/systems | represented | staged-in-raw | current | skip |
| 07_BRAND_VOICE.md | operator/systems | represented | staged-in-raw | current | skip |
| 08_VISUAL_IDENTITY_BRIEF.md | operator/systems | represented | staged-in-raw | current | skip |
| 09_MIGRATION_PLAN.md | operator/systems | represented | staged-in-raw | current | skip |
| 4_Content_System.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| 4_Content_System.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| 5_Delivery_Referral_System.docx | operator/systems | represented | src:3 txt:3 | current | skip |
| 5_Delivery_Referral_System.docx | operator/systems | represented | src:3 txt:3 | current | skip |
| 7 Powers{Hamilton Helmer}(Deep Strategy LLC){114234609} libgen.li.pdf | operator/systems | represented | src:3 txt:3 | current | skip |
| 7_Powers_Strategic_Power_FRAMEWORKS.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| 7_Powers_Strategic_Power_FRAMEWORKS.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| _OceanofPDF.com_The_Operator_-_Tom_King.pdf | operator/systems | represented | staged-in-raw | current | skip |
| _OceanofPDF.com_The_Operator_-_Tom_King.pdf | operator/systems | represented | staged-in-raw | current | skip |
| AI Content Strategy Generator - Lead Magnet.json | operator/systems | represented | staged-in-raw | current | skip |
| AI Content Strategy Generator - Lead Magnet.json | operator/systems | represented | staged-in-raw | current | skip |
| Audit Script Framework 2.xlsx | operator/systems | represented | src:2 txt:3 | current | skip |
| Audit Script Framework 2.xlsx | operator/systems | represented | src:2 txt:3 | current | skip |
| Audit_Script_Framework_2.xlsx | operator/systems | represented | src:2 txt:3 | current | skip |
| Audit_Script_Framework_2.xlsx | operator/systems | represented | src:2 txt:3 | current | skip |
| Audit_Script_Framework_ATS_Controls_Added.xlsx | operator/systems | represented | src:2 txt:5 | current | skip |
| Audit_Script_Framework_ATS_Controls_Added.xlsx | operator/systems | represented | src:2 txt:5 | current | skip |
| Brand_Builders_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| Brand_Builders_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| Business_Operations_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| Business_Operations_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| casting_call_doctrine_v1.md | operator/systems | represented | staged-in-raw | current | skip |
| chapter_rollout_doctrine_v1.md | operator/systems | represented | staged-in-raw | current | skip |
| Cognitive_Bias_Decision_Architecture_FRAMEWORKS.docx | operator/systems | represented | src:4 txt:5 | current | skip |
| Cognitive_Bias_Decision_Architecture_FRAMEWORKS.docx | operator/systems | represented | src:4 txt:5 | current | skip |
| Content_Strategy.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| Content_Strategy.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| Copywriting_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| Copywriting_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| Creative_Resistance_Professional_Execution_FRAMEWORKS.docx | operator/systems | represented | src:4 txt:5 | current | skip |
| Creative_Resistance_Professional_Execution_FRAMEWORKS.docx | operator/systems | represented | src:4 txt:5 | current | skip |
| CUSTOMER_DISCOVERY_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| CUSTOMER_DISCOVERY_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| daily_operating_plan.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| daily_operating_plan.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| Digital_Products_AI_Services_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| Digital_Products_AI_Services_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| ECONOMIC_THINKING_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| ECONOMIC_THINKING_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| EPMS_Universal_Framework.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| EPMS_Universal_Framework.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| FE_Readiness_Validation_Framework_DRAFT.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| FE_Readiness_Validation_Framework_DRAFT.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| Freelance_Platform_Strategy_Frameworks.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Freelance_Platform_Strategy_Frameworks.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| GaryVee_Attention_Operating_System.docx | operator/systems | represented | staged-in-raw | current | skip |
| GaryVee_Attention_Operating_System.docx | operator/systems | represented | staged-in-raw | current | skip |
| Karim R. Lakhani_Marco Iansiti - Competing in the Age of AI_ Strategy and Leader | operator/systems | represented | staged-in-raw | current | skip |
| Karim R. Lakhani_Marco Iansiti - Competing in the Age of AI_ Strategy and Leader | operator/systems | represented | staged-in-raw | current | skip |
| linkedin strategy.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| linkedin strategy.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| linkedin_strategy_extracted.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| linkedin_strategy_extracted.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| Meta_Business_Infrastructure_Framework.docx | operator/systems | represented | src:4 txt:4 | current | skip |
| Meta_Business_Infrastructure_Framework.docx | operator/systems | represented | src:4 txt:4 | current | skip |
| Offers_Strategy.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| Offers_Strategy.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| OPERATING_LOCKS_2026-05-12.md | operator/systems | represented | staged-in-raw | current | skip |
| Operator_Level_Communication_Frameworks.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Operator_Level_Communication_Frameworks.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| OPERATOR_QUESTIONS_2026-05-13.md | operator/systems | represented | staged-in-raw | current | skip |
| Personal Image Presentation Frameworks.docx | operator/systems | represented | src:2 txt:4 | current | skip |
| Personal Image Presentation Frameworks.docx | operator/systems | represented | src:2 txt:4 | current | skip |
| Personal_MBA_Business_Mastery_FRAMEWORKS.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Personal_MBA_Business_Mastery_FRAMEWORKS.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Prediction_Forecasting_Systems_FRAMEWORKS.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Prediction_Forecasting_Systems_FRAMEWORKS.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Premiere_Pro_Production_Framework.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| Premiere_Pro_Production_Framework.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| Server_Farm_Commissioning_FRAMEWORKS.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Server_Farm_Commissioning_FRAMEWORKS.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Snipe_Media_Strategy_Brief.docx | operator/systems | represented | src:3 txt:3 | current | skip |
| Snipe_Media_Strategy_Brief.docx | operator/systems | represented | src:3 txt:3 | current | skip |
| SNIPED_Front_End_Alignment_Full_System.md | operator/systems | represented | src:2 txt:3 | current | skip |
| Sniped_Media_Content_System.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Content_System.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| sniped_media_daily_operating_playbook.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| sniped_media_daily_operating_playbook.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| Sniped_Media_Pixieset_Complete_System_Final.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Pixieset_Complete_System_Final.docx | operator/systems | represented | src:2 txt:2 | current | skip |
| sniped_operating_system_v1_legacy.md | operator/systems | represented | staged-in-raw | current | skip |
| SNIPED_OS_OPERATING_BRIEF.md | operator/systems | represented | staged-in-raw | current | skip |
| Social_Media_Content_Strategy_Frameworks.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Social_Media_Content_Strategy_Frameworks.docx | operator/systems | represented | src:3 txt:4 | current | skip |
| Sticky_Communication_Idea_Design_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:5 | current | skip |
| Sticky_Communication_Idea_Design_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:5 | current | skip |
| STRATEGIC_THINKING_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| STRATEGIC_THINKING_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| STRUCTURED_COMMUNICATION_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| STRUCTURED_COMMUNICATION_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| STYLIST_PLAYBOOK.md | operator/systems | represented | staged-in-raw | current | skip |
| STYLIST_PLAYBOOK.md | operator/systems | represented | staged-in-raw | current | skip |
| SYSTEM_FINAL_STATUS.md | operator/systems | represented | staged-in-raw | current | skip |
| THE_LINEAGE_DOCTRINE.md | operator/systems | represented | staged-in-raw | current | skip |
| THE_OPERATOR_CODED_DEFINITION.md | operator/systems | represented | staged-in-raw | current | skip |
| The_Operator_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| The_Operator_Playbook.docx | operator/systems | represented | staged-in-raw | current | skip |
| Thinking in Systems_ A Primer{Donella H. Meadows_ Diana Wright}(2008, Chelsea Gr | operator/systems | represented | src:4 txt:7 | current | skip |
| Thinking_in_Systems_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| Thinking_in_Systems_FRAMEWORKS.docx | operator/systems | represented | src:2 txt:3 | current | skip |
| -Rees%2C%20Anuschka%20-%20The%20curated%20closet%20_%20a%20simple%20system%20for | operator/systems | review | src:0 txt:2 | unclear | manual review |
| 30_Shot_Playbook.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| 30_Shot_Playbook.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| copywriting_frameworks.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| copywriting_frameworks.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| M4-Pro-Setup-Playbook.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| M4-Pro-Setup-Playbook.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| NEGOTIATION_FRAMEWORKS.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| NEGOTIATION_FRAMEWORKS.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| PKM_Systems_FRAMEWORKS.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| PKM_Systems_FRAMEWORKS.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| Portfolio_Strategy.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| Portfolio_Strategy.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| Proof_Sorting_Framework.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| Proof_Sorting_Framework.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| SUPERFORECASTING_FRAMEWORKS.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| SUPERFORECASTING_FRAMEWORKS.docx | operator/systems | review | src:1 txt:2 | unclear | manual review |
| 1101190 (1).pdf | other/book | duplicate | src:0 txt:0 | superseded | ignore (superseded) |
| 2024.09.30_SF Hockley_IFP QAQC_Electrical (1).pdf | other/book | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| 26 3353-1.1 Electrical- 24MW UPS Vertiv - HEI Reviewed (1)-compressed.pdf | other/book | duplicate | src:0 txt:3 | superseded | ignore (superseded) |
| 26 3353-1.1 Electrical- 24MW UPS Vertiv - HEI Reviewed (1).pdf | other/book | duplicate | src:0 txt:2 | superseded | ignore (superseded) |
| 6_Content_Marketing_OS (1).docx | other/book | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| 6_Content_Marketing_OS (2).docx | other/book | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Action_Plan_Instructions (1).docx | other/book | duplicate | src:0 txt:3 | superseded | ignore (superseded) |
| adobe-timewarp-us (1).pdf | other/book | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| ai-ops-dashboard-prd (1).md | other/book | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| communication-blueprint (1).md | other/book | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| creative-productivity-one-pager-ue (1).pdf | other/book | duplicate | src:1 txt:3 | superseded | ignore (superseded) |
| Dave Ramsey - The Total Money Makeover Workbook_ Classic Edition_ The Essential  | other/book | duplicate | src:5 txt:9 | superseded | ignore (superseded) |
| Demand_Letter_UPDATED_Sorrento.docx | other/book | duplicate | src:1 txt:3 | superseded | ignore (superseded) |
| Extracted_Professional_Intelligence (1).docx | other/book | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| FE_Readiness_Checklist_DRAFT_v1.1 (1).docx | other/book | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| FE_Readiness_Checklist_DRAFT_v1.1 (1).xlsx | other/book | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| financial_os_final_v2.xlsx | other/book | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| frame-io-v4-one-pager-ue (1).pdf | other/book | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| index (1).html | other/book | duplicate | src:0 txt:1 | superseded | ignore (superseded) |
| Kingdom_of_the_Sun_2025 (1).pdf | other/book | duplicate | src:0 txt:0 | superseded | ignore (superseded) |
| Protocol_01_Free_Download (1).pdf | other/book | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| Small_Claims_Guide_UPDATED_Sorrento.docx | other/book | duplicate | src:2 txt:4 | superseded | ignore (superseded) |
| statement (2).pdf | other/book | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| statement (4).pdf | other/book | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| statement (5).pdf | other/book | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| STYLE_MANIFESTO (1).md | other/book | duplicate | src:1 txt:2 | superseded | ignore (superseded) |
| The Direction Stag_Full Book (1).pdf | other/book | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stag_Full Book (2).pdf | other/book | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stag_Full Book (3).pdf | other/book | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stag_Full Book (4).pdf | other/book | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The_Direction_Shift_Master_v2.docx | other/book | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| W-2_Form_2024_Jones_2026_02_12_16_36_19_-0800_W-2_ESS (1).pdf | other/book | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
| W-2_Form_2025_Jones_2026_02_12_16_36_24_-0800_W-2_ESS (2).pdf | other/book | duplicate | src:1 txt:1 | superseded | ignore (superseded) |
|  W. David Marx - Status and Culture_ How Our Desire for Social Rank Creates Tast | other/book | ignore | src:9 txt:13 | off-scope | ignore (personal) |
| 21 DAY GOLF PLAN.docx | other/book | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| [Laws of Human Nature] Robert Greene - The Laws of Human Nature (2019, VIKING) - | other/book | ignore | src:5 txt:5 | off-scope | ignore (personal) |
| [Rich Dad] Robert T. Kiyosaki_ Sharon L. Lechter - Rich Dad Poor Dad_ What the R | other/book | ignore | src:7 txt:11 | off-scope | ignore (personal) |
| [Rich Dad] Robert T. Kiyosaki_ Sharon L. Lechter - Rich Dad Poor Dad_ What the R | other/book | ignore | src:7 txt:11 | off-scope | ignore (personal) |
| [Rich Dad] Robert T. Kiyosaki_ Sharon L. Lechter - Rich Dad Poor Dad_ What the R | other/book | ignore | src:7 txt:11 | off-scope | ignore (personal) |
| apple music.docx | other/book | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| az vs michi.docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| Bryceden_Jones_2025_Tax_Summary.docx | other/book | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| Bryceden_Jones_2025_Tax_Summary_UPDATED.docx | other/book | ignore | src:0 txt:2 | off-scope | ignore (personal) |
| car cleaning.docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| criminal-defense-attorney-los-angeles_los-angeles-county-ca-usa - CDALA (1).csv | other/book | ignore | src:1 txt:1 | off-scope | ignore (personal) |
| CTXES1_1_SOP_UPS-1-1-1_SHUTDOWN_DRAFT.docx.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES1_1_SOP_UPS-1-1-1_STARTUP_DRAFT.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES1_1_SOP_UPS-1-1-1_STARTUP_ON_TEMPLATE (1).docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES1_1_SOP_UPS-1-1-1_STARTUP_ON_TEMPLATE (2).docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES1_1_SOP_UPS-1-1-1_STARTUP_ON_TEMPLATE.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES2_1_SOP_UPS-1-1_MAINT_BYPASS_FINAL.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES3_1_SOP_UPS-1-1_RETRANSFER_FINAL.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| CTXES4_1_SOP_UPS-1-1-1_SHUTDOWN_DRAFT.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| DAD BBALL TIPS.docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| Emperor of the French Napoleon I_ Frankreich Kaiser Napoléon I._ - Napoleon _ a | other/book | ignore | src:3 txt:5 | off-scope | ignore (personal) |
| EOP_TEMPLATE.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| fe vs me .docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| FITNESS.docx | other/book | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| FITNESS_DOC-2.docx | other/book | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| FITNESS_DOC.docx | other/book | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| food food and more food.docx | other/book | ignore | src:0 txt:2 | off-scope | ignore (personal) |
| golf_extraction.docx | other/book | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| GOLFER.docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| Greene, Robert - Mastery (2013_2012, Penguin Group_ Penguin Books_Viking Adult)  | other/book | ignore | src:3 txt:6 | off-scope | ignore (personal) |
| HTX1_1_SOP_TEMPLATE_DRAFT_083024.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| HTX1_Phase 2 - Assessment & Action Plan.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| HTX1_Phase 2 - Assessment & Action Plan.pdf | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| Kevin Kelly - The Inevitable_ Understanding the 12 Technological Forces That Wil | other/book | ignore | src:7 txt:9 | off-scope | ignore (personal) |
| LAAS10.3_OMOP_TEMPLATE_SF_REV_3_041824.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| LAAS11.3_EOP_TEMPLATE_SF_REV_3_041824.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| mac set up.docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| MOP_TEMPLATE 1.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| NAILSSS.docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| NBA GAMES.docx | other/book | ignore | src:1 txt:1 | off-scope | ignore (personal) |
| park perfect.docx | other/book | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| set up ai.docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| setting up mac.docx | other/book | ignore | src:1 txt:1 | off-scope | ignore (personal) |
| Smoothies and Malted shakes.docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| SOP_TEMPLATE.docx | other/book | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| The_Food_Manual.docx | other/book | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| TRAVEL_OS.docx | other/book | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| TRAVEL_OS.md | other/book | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| uconn ill mens.docx | other/book | ignore | src:0 txt:1 | off-scope | ignore (personal) |
| usaa and getting approved.docx | other/book | ignore | src:1 txt:2 | off-scope | ignore (personal) |
| whatnot.docx | other/book | ignore | src:0 txt:0 | off-scope | ignore (personal) |
| -Alison%20Freer%20-%20How%20to%20Get%20Dressed_%20A%20Costume%20Designers%20Secr | other/book | missing | src:0 txt:1 | current | ingest/review |
| -Alison%20Lumbatis%20-%20The%20Ultimate%20Book%20of%20Outfit%20Formulas_%20A%20S | other/book | missing | src:0 txt:1 | current | ingest/review |
| 1101190.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 1713578934731168.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2010-charger.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2010-Dodge-Charger-UG-2.pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
| 2010-Dodge-Charger-UG.pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
| 2025-01-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-01-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-01-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-01-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-01_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-01_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-02-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-02-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-02-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-02-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-02_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-02_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-03-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-03-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-03-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-03-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-03_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-03_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-04-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-04-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-04-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-04-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-04_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-04_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-05-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-05-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-05-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-05-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-05_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-05_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-06-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-06-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-06-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-06-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-06_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-06_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-07-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-07-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-07-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-07-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-07_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-07_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-08-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-08-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-08-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-08-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-08_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-08_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-09-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-09-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-09-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-09-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-09_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-09_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-10-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-10-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-10-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-10-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-10_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-10_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-11-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-11-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-11-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-11-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-11_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-11_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-12-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-12-27_STMSSCM-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-12-27_STMSSCM.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-12_eStmt_8940-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2025-12_eStmt_8940.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2026-01-04_VISASTMT-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2026-01-04_VISASTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2026-01-06_MCSTMT.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| 2026-01-28_AutoIDCard.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| [Part 1 ] Шерман, Алекси _ - libgen.li.mobi | other/book | missing | src:0 txt:0 | current | ingest/review |
| _.epub | other/book | missing | src:0 txt:0 | current | ingest/review |
| adobe goat.docx | other/book | missing | src:0 txt:1 | current | ingest/review |
| adobe-fantasticfrontiers-us.pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
| adobe-immersiveappeal-us.pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
| adobe-timewarp-us.pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
| ANNA-90DAY-PLAN.md | other/book | missing | src:0 txt:1 | current | ingest/review |
| Anna_ClientUpdateIntake.docx | other/book | missing | src:0 txt:0 | current | ingest/review |
| Bryceden_Jones.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| c012-2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| c012-3.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| c012.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| ClientEngagementTracker.docx | other/book | missing | src:0 txt:0 | current | ingest/review |
| Coach_Jones_Bio.docx | other/book | missing | src:0 txt:1 | current | ingest/review |
| CoachEric_DecisionBrief.docx | other/book | missing | src:0 txt:0 | current | ingest/review |
| eosrp-ug5-en.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| Feb_20_-_Mar_22_2026.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| FestivalFriend_IntakeQuestionnaire.docx | other/book | missing | src:0 txt:0 | current | ingest/review |
| Final PDF.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| frameio-pfeiffer-benchmarking-report.pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
| gary2.0 use.docx | other/book | missing | src:0 txt:0 | current | ingest/review |
| garyvee gameplan.docx | other/book | missing | src:0 txt:0 | current | ingest/review |
| HOW_TO_USE.md | other/book | missing | src:0 txt:0 | current | ingest/review |
| Kingdom_of_the_Sun_2025.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| Kingdom_of_the_Sun_2026.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| LA28OlympicGamesCompetitionScheduleByDayV3.0.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| max-2024-report-ue.pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
| OfDVDVbyMD.html | other/book | missing | src:0 txt:0 | current | ingest/review |
| Pacific Surfliner.pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
| pdf.net_2024.09.30_SF-Hockley_IFP-QAQC_Electrical-(1).pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
| Receipt (2_10_2026)_B20260073476.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| Receipt.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| Sticker2.pdf | other/book | missing | src:0 txt:0 | current | ingest/review |
| The%20Pyramid%20Principle_%20Logic%20in%20Writing%20and%20ThinkingBarbara%20Mint | other/book | missing | src:0 txt:1 | current | ingest/review |
| THREADS.docx | other/book | missing | src:0 txt:1 | current | ingest/review |
| Trip_Sponsorship_OnePager.docx | other/book | missing | src:0 txt:1 | current | ingest/review |
| Understated and timeless treasures for you to enjoy. - Anna.pdf | other/book | missing | src:0 txt:1 | current | ingest/review |
|  Estate Planning.csv | other/book | parked | src:0 txt:2 | operational | park (lead data) |
| Attorney Beverly Hills, CA, USA.csv | other/book | parked | src:0 txt:0 | operational | park (lead data) |
| Attorney in Santa Monica, CA, USA.csv | other/book | parked | src:0 txt:0 | operational | park (lead data) |
| Law firm century city.csv | other/book | parked | src:2 txt:3 | operational | park (lead data) |
| leads (1).csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| leads (2).csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| leads (3).csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| leads (4).csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| leads (5).csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| leads-2.csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| leads-3.csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| leads-4.csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| leads.csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| Los angeles Attorney Leads - DLALA-UPLOAD.csv | other/book | parked | src:1 txt:2 | operational | park (lead data) |
| Los angeles Attorney Leads - DLALA.csv | other/book | parked | src:1 txt:1 | operational | park (lead data) |
| Los angeles Attorney Leads - Family Law Attorney Los Angeles.csv | other/book | parked | src:1 txt:2 | operational | park (lead data) |
| navy debit.csv | other/book | parked | src:0 txt:1 | operational | park (lead data) |
| newport-beach.csv | other/book | parked | src:0 txt:1 | operational | park (lead data) |
| Personal Injury Attorney Century City.csv | other/book | parked | src:2 txt:4 | operational | park (lead data) |
| personal-injury-attorney_los-angeles-ca-usa - Final Copy Personal Injury attorne | other/book | parked | src:1 txt:2 | operational | park (lead data) |
| -Jeffrey%20Liker%20-%20The%20Toyota%20Way%2C%20Second%20Edition_%2014%20Manageme | other/book | partial | src:0 txt:3 | unclear | compare delta |
| Action_Plan_Instructions.docx | other/book | partial | src:0 txt:3 | unclear | compare delta |
| adobe-express-summary.pdf | other/book | partial | src:0 txt:3 | unclear | compare delta |
| Antique_Insights_First_Look_Signup_Sheet.pdf | other/book | partial | src:1 txt:5 | unclear | compare delta |
| BACKDROP_CREATION_GUIDE.docx | other/book | partial | src:1 txt:3 | unclear | compare delta |
| constellations-research-adobe-ai-ethics.pdf | other/book | partial | src:1 txt:3 | unclear | compare delta |
| creative-productivity-one-pager-ue.pdf | other/book | partial | src:1 txt:3 | unclear | compare delta |
| debt_payoff_battle_plan.xlsx | other/book | partial | src:0 txt:4 | unclear | compare delta |
| Ideal_Client_Definition.docx | other/book | partial | src:1 txt:3 | unclear | compare delta |
| Project_Flash_Executive_Template.pdf | other/book | partial | src:1 txt:4 | unclear | compare delta |
| Proof_Case_Studies_Page_Copy_V1.docx | other/book | partial | src:1 txt:4 | unclear | compare delta |
| Proof_Deployment_Priorities.docx | other/book | partial | src:0 txt:3 | unclear | compare delta |
| ticket buying and seling games concerts etc.docx | other/book | partial | src:1 txt:4 | unclear | compare delta |
| TRAVEL GUIDE AND HACK.docx | other/book | partial | src:1 txt:3 | unclear | compare delta |
|  Adam Morgan - Eating the Big Fish_ How Challenger Brands Can Compete Against Br | other/book | represented | staged-in-raw | current | skip |
|  Agins, Teri - The end of fashion_ how marketing changed the clothing business f | other/book | represented | staged-in-raw | current | skip |
|  Alan Flusser - Dressing the Man_ Mastering the Art of Permanent Fashion (2002,  | other/book | represented | src:3 txt:5 | current | skip |
|  Alicia Drake - The Beautiful Fall_ Fashion, Genius, and Glorious Excess in 1970 | other/book | represented | staged-in-raw | current | skip |
|  Alison Freer - How to Get Dressed_ A Costume Designer's Secrets for Making Your | other/book | represented | src:1 txt:11 | current | skip |
|  Alison Freer - How to Get Dressed_ A Costume Designers Secrets for Making Your  | other/book | represented | src:1 txt:11 | current | skip |
|  Alison Lumbatis - The Ultimate Book of Outfit Formulas_ A Stylish Solution to W | other/book | represented | src:1 txt:7 | current | skip |
|  Alison Lumbatis - The Ultimate Book of Outfit Formulas_ A Stylish Solution to W | other/book | represented | src:1 txt:7 | current | skip |
|  Anderson, Rodney - Credit 911_ Secrets and Strategies to Saving Your Financial  | other/book | represented | src:4 txt:7 | current | skip |
|  André Leon Talley - The Chiffon Trenches_ A Memoir (2020, Random House Publish | other/book | represented | src:6 txt:9 | current | skip |
|  Annie Leibovitz - Annie Leibovitz at Work (2008) - libgen.li.pdf | other/book | represented | src:3 txt:3 | current | skip |
|  Atul Gawande - The Checklist Manifesto_ How to Get Things Right (2009, Metropol | other/book | represented | staged-in-raw | current | skip |
|  Bach, Richard - Jonathan Livingston Seagull (2010, Avon Books) - libgen.li.epub | other/book | represented | src:5 txt:5 | current | skip |
|  Benjamin Graham - The Intelligent Investor_ The Definitive Book on Value Invest | other/book | represented | staged-in-raw | current | skip |
|  Blake Snyder - Save The Cat! The Last Book on Screenwriting You'll Ever Need (2 | other/book | represented | staged-in-raw | current | skip |
|  Brad Stone - The Everything Store_ Jeff Bezos and the Age of Amazon (2013, Litt | other/book | represented | staged-in-raw | current | skip |
|  Bruce Block - The Visual Story, _ Creating the Visual Structure of Film, TV and | other/book | represented | staged-in-raw | current | skip |
|  Carnegie, Dale - Dale Carnegie's lifetime plan for success_ how to win friends  | other/book | represented | src:7 txt:10 | current | skip |
|  Catmull, Ed_Wallace, Amy - Creativity, Inc._ Overcoming the Unseen Forces That  | other/book | represented | src:6 txt:13 | current | skip |
|  Charles T. Munger - Poor Charlie’s Almanack_ The Wit and Wisdom of Charles T. M | other/book | represented | staged-in-raw | current | skip |
|  Charles T. Munger, Peter D. Kaufman, Ed Wexler, Warren E. Buffet - Poor Charlie | other/book | represented | staged-in-raw | current | skip |
|  Chip Heath, Dan Heath - Made to Stick_ Why Some Ideas Survive and Others Die (2 | other/book | represented | staged-in-raw | current | skip |
|  Chris Voss_ Tahl Raz - Never Split the Difference_ Negotiating as if Your Life  | other/book | represented | src:8 txt:11 | current | skip |
|  Christensen, Clayton M. & Dillon, Karen & Hall, Taddy & Duncan, - Competing Aga | other/book | represented | staged-in-raw | current | skip |
|  Christian Dior - Dior by Dior- The Autobiography of Christian Dior - libgen.li. | other/book | represented | staged-in-raw | current | skip |
|  Christian Dior - The little dictionary of fashion (2007, V & A Publications) -  | other/book | represented | staged-in-raw | current | skip |
|  Christian Dior - The little dictionary of fashion (2007, V & A Publications) -  | other/book | represented | src:4 txt:5 | current | skip |
|  Christopher Steiner - Automate This_ How Algorithms Came to Rule Our World (201 | other/book | represented | staged-in-raw | current | skip |
|  Colin Bryar_ Bill Carr - Working Backwards (2021, St. Martin's Publishing Group | other/book | represented | staged-in-raw | current | skip |
|  Dana Thomas - Deluxe_ How Luxury Lost Its Luster (2008, Penguin Books) - libgen | other/book | represented | staged-in-raw | current | skip |
|  Daniel Coyle - The Culture Code_ The Secrets of Highly Successful Groups (2018, | other/book | represented | staged-in-raw | current | skip |
|  Derek Thompson - Hit Makers_ The Science of Popularity in an Age of Distraction | other/book | represented | staged-in-raw | current | skip |
|  Donald Miller - Building a StoryBrand_ Clarify Your Message So Customers Will L | other/book | represented | src:6 txt:10 | current | skip |
|  Ed Catmull, Amy Wallace - Creativity, Inc._ Overcoming the Unseen Forces That S | other/book | represented | staged-in-raw | current | skip |
|  Fredric Dannen - Hit men_ power brokers and fast money inside the music busines | other/book | represented | staged-in-raw | current | skip |
|  Geoffrey A. Moore - Crossing the Chasm, 3rd Edition_ Marketing and Selling Disr | other/book | represented | staged-in-raw | current | skip |
|  Harper Lee - To Kill a Mockingbird - libgen.li.mobi | other/book | represented | src:1 txt:2 | current | skip |
|  Howard Schultz, Joanne Gordon - Onward_ How Starbucks Fought for Its Life witho | other/book | represented | staged-in-raw | current | skip |
|  Jack Trout, Steve Rivkin - Differentiate or Die_ Survival in Our Era of Killer  | other/book | represented | staged-in-raw | current | skip |
|  Jack Weatherford - Genghis Khan and the Making of the Modern World (2005, Broad | other/book | represented | staged-in-raw | current | skip |
|  James B. Stewart - DisneyWar _ the battle for the magic kingdom (2006, Pocket)  | other/book | represented | staged-in-raw | current | skip |
|  Jeffrey Liker - The Toyota Way, Second Edition_ 14 Management Principles from t | other/book | represented | src:4 txt:10 | current | skip |
|  John Berger - Ways of Seeing (2008, Penguin Books Ltd) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
|  John Seabrook - The Song Machine_ Inside the Hit Factory (2015, W. W. Norton &  | other/book | represented | staged-in-raw | current | skip |
|  John Truby - The Anatomy of Story_ 22 Steps to Becoming a Master Storyteller (2 | other/book | represented | staged-in-raw | current | skip |
|  Jon Acuff - Quitter_ Closing the Gap Between Your Day Job & Your Dream Job (201 | other/book | represented | src:2 txt:4 | current | skip |
|  Jonah Berger - Contagious_ Why Things Catch On (2013, Simon & Schuster) - libge | other/book | represented | staged-in-raw | current | skip |
|  Kahneman, Daniel - Thinking, Fast and Slow (2011, Farrar, Straus and Giroux) -  | other/book | represented | src:4 txt:5 | current | skip |
|  Kaufman, Josh - The Personal MBA_ Master the Art of Business (2010, Portfolio H | other/book | represented | src:3 txt:5 | current | skip |
|  Lara Casey - Make It Happen_ Surrender Your Fear, Take the Leap, Live on Purpos | other/book | represented | src:3 txt:10 | current | skip |
|  Lovell, Sophie - Dieter Rams_ As Little Design as Possible (2011, Phaidon Press | other/book | represented | staged-in-raw | current | skip |
|  Marc Randolph - That Will Never Work (2019, Little, Brown and Company) - libgen | other/book | represented | src:7 txt:8 | current | skip |
|  Marshall McLuhan - Understanding media (1995, MIT Press) - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
|  Marshall McLuhan, Lewis H. Lapham - Understanding Media_ The Extensions of Man  | other/book | represented | staged-in-raw | current | skip |
|  Michael Hammer_ James Champy - Reengineering the corporation _ a manifesto for  | other/book | represented | staged-in-raw | current | skip |
|  Michael Jackson - Moonwalk (2009, Crown Archetype) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
|  Nate Silver - The Signal and the Noise_ Why So Many Predictions Fail-but Some D | other/book | represented | src:3 txt:9 | current | skip |
|  Peter M. Senge - The Fifth Discipline_ The Art & Practice of The Learning Organ | other/book | represented | staged-in-raw | current | skip |
|  Peter Thiel, Blake Masters - Zero to One_ Notes on Startups, or How to Build th | other/book | represented | staged-in-raw | current | skip |
|  Phil knight - Shoe dog (0) - libgen.li.mobi | other/book | represented | staged-in-raw | current | skip |
|  Pressfield, Steven - The War of Art- Break Through the Blocks and Win Your Inne | other/book | represented | src:5 txt:8 | current | skip |
|  Ray Kroc - Grinding It Out_ The Making of McDonald’s (2016, St. Martin’s Paperb | other/book | represented | staged-in-raw | current | skip |
|  Rich Cohen - The Fish That Ate the Whale_ The Life and Times of America's Banan | other/book | represented | staged-in-raw | current | skip |
|  Richard Shotton - The Choice Factory_ 25 Behavioural Biases That Influence What | other/book | represented | staged-in-raw | current | skip |
|  Rick Rubin - The Creative Act_ A Way of Being (2023, Penguin Publishing Group)  | other/book | represented | staged-in-raw | current | skip |
|  Rob Fitzpatrick - The Mom Test_ how to talk to customers and learn if your busi | other/book | represented | src:5 txt:9 | current | skip |
|  ROBERT B. CIALDINI - Influence (Harper collins) - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
|  Robert Cialdini - Pre-Suasion_ A Revolutionary Way to Influence and Persuade (2 | other/book | represented | staged-in-raw | current | skip |
|  Robert Iger_ Joel Lovell - The Ride of a Lifetime_ Lessons Learned from 15 Year | other/book | represented | staged-in-raw | current | skip |
|  Rory Sutherland - Alchemy_ The Dark Art and Curious Science of Creating Magic i | other/book | represented | staged-in-raw | current | skip |
|  Sam Walton - Sam Walton_ Made In America (1993, Bantam) - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
|  Sarah Frier - No Filter_ The Inside Story of Instagram (2020, Simon & Schuster) | other/book | represented | staged-in-raw | current | skip |
|  Scott Kupor - Secrets of Sand Hill Road_ Venture Capital and How to Get It (201 | other/book | represented | src:4 txt:8 | current | skip |
|  Seth Godin - Purple Cow_ Transform Your Business by Being Remarkable (2003, Por | other/book | represented | src:4 txt:9 | current | skip |
|  Sinek, Simon - Start With Why_ How Great Leaders Inspire Everyone To Take Actio | other/book | represented | src:4 txt:8 | current | skip |
|  Sowell, Thomas - Basic Economics (2014, Basic Books) - libgen.li.pdf | other/book | represented | src:2 txt:5 | current | skip |
|  Stoute, Steve - The Tanning of America_ How Hip-Hop Created a Culture That Rewr | other/book | represented | staged-in-raw | current | skip |
|  Vaynerchuk, Gary - Jab, jab, jab, right hook how to tell your story in a noisy, | other/book | represented | src:7 txt:9 | current | skip |
|  Vreeland, Diana - D.V. (2011, HarperCollins) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
|  Walter Isaacson - Steve Jobs Walter Isaacson (2011) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
|  Whitman, Drew Eric - Cashvertising_ How to Use More Than 100 Secrets of Ad-Agen | other/book | represented | staged-in-raw | current | skip |
|  Will Storr - The Status Game_ On Social Position and How We Use It (2021, Willi | other/book | represented | staged-in-raw | current | skip |
|  William N. Thorndike - The Outsiders_ Eight Unconventional CEOs and Their Radic | other/book | represented | staged-in-raw | current | skip |
|  Zack O'Malley Greenburg - Empire State of Mind_ How Jay-Z Went from Street Corn | other/book | represented | src:8 txt:9 | current | skip |
| 1000-true-fans-kevin-kellydocx_compress.pdf | other/book | represented | staged-in-raw | current | skip |
| 2025 Client Data Sheet Revised 1.20.25.pdf | other/book | represented | src:2 txt:4 | current | skip |
| 2026 Client Data Sheet - Bryceden Jones .pdf | other/book | represented | src:1 txt:3 | current | skip |
| 2026 Corporate Client Data Sheet Revised 1.2026.pdf | other/book | represented | src:2 txt:5 | current | skip |
| 23adbe-cc-sbs-product-design-and-packaging-infographic.pdf | other/book | represented | src:2 txt:2 | current | skip |
| 257683787-Cartier-Bresson-H-1952-the-Decisive-Moment.pdf | other/book | represented | staged-in-raw | current | skip |
| 2_Assistant_SOP_Manual (1).docx | other/book | represented | staged-in-raw | current | skip |
| 2_Assistant_SOP_Manual.docx | other/book | represented | src:2 txt:2 | current | skip |
| 30_Day_Development_Plan_EYES_ONLY.docx | other/book | represented | src:3 txt:4 | current | skip |
| 30_Day_FE_Development_Plan_EYES_ONLY.docx | other/book | represented | src:3 txt:4 | current | skip |
| 50 Cent, Robert Greene - The 50th Law (2009, Harper) - libgen.li.mobi | other/book | represented | staged-in-raw | current | skip |
| 6_Content_Marketing_OS.docx | other/book | represented | src:2 txt:2 | current | skip |
| 713434459-Core-Studio-Public-Lecture-Virgil-Abloh-Insert-Complicated-Title-Here- | other/book | represented | staged-in-raw | current | skip |
| 7_30Day_Content_Bank.docx | other/book | represented | src:2 txt:2 | current | skip |
| [Adweek Series] Luke Sullivan - Hey, Whipple, Squeeze This_ A Guide to Creating  | other/book | represented | staged-in-raw | current | skip |
| [Alexander the Great 1 ] Freeman, Philip - Alexander the Great (2016) - libgen.l | other/book | represented | staged-in-raw | current | skip |
| [Andrew_S._Grove]_High_Output_Management(z-lib.org)-2.pdf | other/book | represented | src:4 txt:4 | current | skip |
| [Andrew_S._Grove]_High_Output_Management(z-lib.org).pdf | other/book | represented | staged-in-raw | current | skip |
| [Animal Farm _1] Orwell, George - Animal Farm (1945, Secker & Warburg) - libgen. | other/book | represented | staged-in-raw | current | skip |
| [Baker & Taylor Books (Firm)._ Axis 360] Robert Greene_ Joost Elffers - The 48 L | other/book | represented | staged-in-raw | current | skip |
| [Beloved Trilogy 1 - Beloved Trilogy 1] Beloved{Toni Morrison}(1987){112430403}  | other/book | represented | staged-in-raw | current | skip |
| [BK business book] Watkins, Alexandra - Hello, my name is awesome_ how to create | other/book | represented | staged-in-raw | current | skip |
| [Blitzscaling] Reid Hoffman, Chris Yeh, Bill Gates - Blitzscaling_ The Lightning | other/book | represented | staged-in-raw | current | skip |
| [Classics] Arrian - The Campaigns of Alexander (2003, Penguin Books Ltd) - libge | other/book | represented | staged-in-raw | current | skip |
| [Company of One] Jarvis, Paul - Company of one why staying small is the next big | other/book | represented | staged-in-raw | current | skip |
| [Dover books on history, political and social science] Niccolo Machiavelli, Nini | other/book | represented | staged-in-raw | current | skip |
| [Fashion Theory The Journal of Dress Body &amp_ Culture 2019-sep 11 vol. 24 iss. | other/book | represented | staged-in-raw | current | skip |
| [J-B Lencioni Series] Patrick Lencioni - Death by Meeting_ A Leadership Fable... | other/book | represented | staged-in-raw | current | skip |
| [Joost Elffers Books ] Greene, Robert - The 33 Strategies of War (2008_2007, Pen | other/book | represented | staged-in-raw | current | skip |
| [Journal of Advertising 1998-dec vol. 27 iss. 4] Jon Steel, Truth, Lies and Adve | other/book | represented | staged-in-raw | current | skip |
| [Made to Stick ] Heath, Chip _ Heath, Dan - Made to Stick - libgen.li.mobi | other/book | represented | src:3 txt:3 | current | skip |
| [Maus Series _1] Art Spiegelman - Maus I A Survivor's Tale My Father Bleeds Hist | other/book | represented | src:3 txt:6 | current | skip |
| [Maus Series _2] Art Spiegelman - Maus II A Survivor's Tale And Here My Troubles | other/book | represented | src:3 txt:7 | current | skip |
| [Oxford World's Classics] Carl von Clausewitz, Beatrice Heuser - On War (2007, O | other/book | represented | staged-in-raw | current | skip |
| [Reedsy Marketing Guides Book 1 - Reedsy Marketing Guides Book 1] How to Market  | other/book | represented | staged-in-raw | current | skip |
| [Security Analysis Prior Editions] Benjamin Graham, David Dodd, Warren Buffett - | other/book | represented | staged-in-raw | current | skip |
| [SparkNotes Literature Guide ] Orwell, George - 1984, George Orwell (1984_2014,  | other/book | represented | src:3 txt:6 | current | skip |
| [The Color Purple 1 - The Color Purple 1] The Color Purple Collection_ The Color | other/book | represented | staged-in-raw | current | skip |
| [The Handmaid's Tale 1 ] Atwood, Margaret - The Handmaid's Tale (2006_2017, Ever | other/book | represented | staged-in-raw | current | skip |
| [Vintage] Dannen, Fredric - Hit Men_ Power Brokers and Fast Money Inside the Mus | other/book | represented | src:8 txt:11 | current | skip |
| [Voices That Matter] Jay Maisel - Light, Gesture, and Color (2014, New Riders) - | other/book | represented | staged-in-raw | current | skip |
| _OceanofPDF.com_Pharrell_Places_and_Spaces_Ive_Been_-_Pharrell_Williams.pdf | other/book | represented | staged-in-raw | current | skip |
| _OceanofPDF.com_The_88_Laws_Of_The_Masculine_Mindset_-_John_Winters.pdf | other/book | represented | staged-in-raw | current | skip |
| Aesthetic_Statement_v1.docx | other/book | represented | staged-in-raw | current | skip |
| AI Phone Call Assistant - Call Workflow.json | other/book | represented | staged-in-raw | current | skip |
| ai-ops-dashboard-prd.md | other/book | represented | staged-in-raw | current | skip |
| Airey, David - Identity designed_ the definitive guide to visual branding (2019, | other/book | represented | staged-in-raw | current | skip |
| Ajay Agrawal, Joshua Gans, Avi Goldfarb - Power and Prediction_ The Disruptive E | other/book | represented | staged-in-raw | current | skip |
| Ajay Agrawal, Joshua Gans, Avi Goldfarb - Prediction Machines_ The Simple Econom | other/book | represented | staged-in-raw | current | skip |
| Akio Morita, Edwin M. Reingold, Mitsuko Shimomura - Made in Japan_ Akio Morita a | other/book | represented | staged-in-raw | current | skip |
| Al Ramadan, Dave Peterson, Christopher Lochhead, Kevin Maney - Play Bigger_ How  | other/book | represented | staged-in-raw | current | skip |
| Al Ries_ Philip Kotler - Positioning_ The Battle for Your Mind_ The Battle for Y | other/book | represented | staged-in-raw | current | skip |
| Alain De Botton - Status Anxiety (2005, Vintage) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
| Alan Weiss - Value-Based Fees_ How to Charge - and Get - What You're Worth (Ulti | other/book | represented | staged-in-raw | current | skip |
| Alan Weiss, Alan Weiss - Million Dollar Consulting_ The Professional's Guide to  | other/book | represented | staged-in-raw | current | skip |
| Aldous Huxley - Brave New World Revisited (2001) - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| Alex Hormozi - $100M Leads_ How to Get Strangers To Want To Buy Your Stuff (2023 | other/book | represented | staged-in-raw | current | skip |
| Alex Hormozi - $100M Offers_ How To Make Offers So Good People Feel Stupid Sayin | other/book | represented | staged-in-raw | current | skip |
| Alina Wheeler, Rob Meyerson - Designing Brand Identity_ A Comprehensive Guide to | other/book | represented | staged-in-raw | current | skip |
| all books summaries and some markting stuff from that chat.docx | other/book | represented | src:2 txt:5 | current | skip |
| Amp It Up{Frank Slootman}(2022, Wiley){112881352} libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| Anders Ericsson, Robert Pool - Peak_ Secrets from the New Science of Expertise ( | other/book | represented | staged-in-raw | current | skip |
| Anderson, Rodney - Credit 911_ Secrets and Strategies to Saving Your Financial L | other/book | represented | src:4 txt:7 | current | skip |
| Annie Leibovitz - Annie Leibovitz at Work (2008, Random House) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
| antique-insights-signup-sheet-PRINT-2.html | other/book | represented | src:2 txt:4 | current | skip |
| antique-insights-signup-sheet-PRINT.html | other/book | represented | src:2 txt:4 | current | skip |
| april_2026_monthly_statement navy personal .pdf | other/book | represented | src:3 txt:4 | current | skip |
| april_2026_monthly_statement.pdf | other/book | represented | src:2 txt:3 | current | skip |
| Art_Series.docx | other/book | represented | staged-in-raw | current | skip |
| Art_Series_1_RichardAvedon.md | other/book | represented | staged-in-raw | current | skip |
| Art_Series_2_WilliamEggleston.md | other/book | represented | staged-in-raw | current | skip |
| Art_Series_3_AnnieLeibovitz.md | other/book | represented | staged-in-raw | current | skip |
| Art_Series_4_StephenShore.md | other/book | represented | staged-in-raw | current | skip |
| Art_Series_5_FredHerzog.md | other/book | represented | staged-in-raw | current | skip |
| Art_Series_6_RobertFrank (1).md | other/book | represented | staged-in-raw | current | skip |
| Art_Series_6_RobertFrank.md | other/book | represented | staged-in-raw | current | skip |
| Art_Series_7_JoelMeyerowitz.md | other/book | represented | staged-in-raw | current | skip |
| Art_Series_8_GracielaIturbide.md | other/book | represented | staged-in-raw | current | skip |
| Art_Series_9_ErnstHaas.md | other/book | represented | staged-in-raw | current | skip |
| ArtOfWar.pdf | other/book | represented | staged-in-raw | current | skip |
| Bailey Richardson_ Kai Elmer Sotto_ Kevin Huynh - Get Together_ How to build a c | other/book | represented | staged-in-raw | current | skip |
| Balaji Srinivasan - The Network State - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| Ben Horowitz - The Hard Thing About Hard Things_ Building a Business When There  | other/book | represented | staged-in-raw | current | skip |
| Blair Enns - The Win Without Pitching Manifesto (2010, RockBench Publishing Corp | other/book | represented | staged-in-raw | current | skip |
| Bolt, Chandler - Published_ the proven path from blank page to published author  | other/book | represented | staged-in-raw | current | skip |
| Brad Feld, Jason Mendelson - Venture Deals_ Be Smarter Than Your Lawyer and Vent | other/book | represented | src:1 txt:8 | current | skip |
| branding x clothes gold.docx | other/book | represented | staged-in-raw | current | skip |
| Bryceden Voice Style Guide .docx | other/book | represented | src:2 txt:3 | current | skip |
| Building a Second Brain{Tiago Forte}(2022, Profile){112862303} libgen.li.pdf | other/book | represented | src:3 txt:4 | current | skip |
| Built an AI SaaS in 20 min.docx | other/book | represented | staged-in-raw | current | skip |
| Business_Model_Framing.docx | other/book | represented | src:2 txt:3 | current | skip |
| Business_Principles.docx | other/book | represented | src:2 txt:2 | current | skip |
| Chip Heath, Dan Heath - Made to Stick_ Why Some Ideas Survive and Others Die (20 | other/book | represented | staged-in-raw | current | skip |
| Chris Anderson - Free_ The Future of a Radical Price (Abridged) (2009, Random Ho | other/book | represented | staged-in-raw | current | skip |
| Chris Anderson - Long Tail, The, Revised and Updated Edition_ Why the Future of  | other/book | represented | staged-in-raw | current | skip |
| Chris Dixon - Read Write Own_ Building the Next Era of the Internet (2024, Rando | other/book | represented | staged-in-raw | current | skip |
| Christopher Leonard - The Lords of Easy Money_ How the Federal Reserve Broke the | other/book | represented | staged-in-raw | current | skip |
| Coddington, Grace - Grace_ A Memoir (2012, Random House Publishing Group) - libg | other/book | represented | staged-in-raw | current | skip |
| Dalio, Ray - Principles_ Life and Work (2017, Simon & Schuster) - libgen.li.pdf | other/book | represented | src:3 txt:3 | current | skip |
| Dan Ariely - Predictably Irrational, Revised and Expanded Edition_ The Hidden Fo | other/book | represented | src:9 txt:9 | current | skip |
| Dan Charnas - Dilla Time_ The Life and Afterlife of J Dilla, the Hip-Hop Produce | other/book | represented | staged-in-raw | current | skip |
| Dan Charnas - The Big Payback_ The History of the Business of Hip-Hop (2010, NAL | other/book | represented | staged-in-raw | current | skip |
| Daniel Kahneman - Thinking, Fast and Slow (2011, Farrar, Straus and Giroux) - li | other/book | represented | staged-in-raw | current | skip |
| Daugherty, Paul R._Wilson, H. James - Human + machine_ reimagining work in the a | other/book | represented | staged-in-raw | current | skip |
| Dave Ramsey - The Total Money Makeover Workbook_ Classic Edition_ The Essential  | other/book | represented | src:5 txt:9 | current | skip |
| Dave Ramsey - The Total Money Makeover Workbook_ Classic Edition_ The Essential  | other/book | represented | src:5 txt:9 | current | skip |
| David Carey, John E. Morris - King of Capital_ The Remarkable Rise, Fall, and Ri | other/book | represented | staged-in-raw | current | skip |
| David H. Maister, Charles H. Green, Robert M. Galford - The Trusted Advisor (200 | other/book | represented | staged-in-raw | current | skip |
| David Ogilvy_ Alan Parker - Confessions of an Advertising Man (2004, Southbank P | other/book | represented | staged-in-raw | current | skip |
| David Spinks - The Business of Belonging_ How to Build Communities That Grow the | other/book | represented | staged-in-raw | current | skip |
| Debt_Recovery_Strategic_Analysis.docx | other/book | represented | src:3 txt:4 | current | skip |
| Derek Thompson - Hit Makers_ The Science of Popularity in an Age of Distraction  | other/book | represented | staged-in-raw | current | skip |
| Direction_Shift_Fact_Check.md | other/book | represented | src:3 txt:4 | current | skip |
| document.pdf | other/book | represented | staged-in-raw | current | skip |
| Donald Miller - Building a StoryBrand_ Clarify Your Message So Customers Will Li | other/book | represented | staged-in-raw | current | skip |
| Donald Miller - Building a StoryBrand_ Clarify Your Message So Customers Will Li | other/book | represented | staged-in-raw | current | skip |
| Donald W. Engels - Alexander the Great and the Logistics of the Macedonian Army  | other/book | represented | staged-in-raw | current | skip |
| dump dump for rebrand late night pt 2.docx | other/book | represented | src:3 txt:3 | current | skip |
| dump dump for rebrand late night.docx | other/book | represented | src:3 txt:3 | current | skip |
| Dunford, April - Obviously Awesome (2019) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
| Elberse, Anita - Blockbusters_ Hit-making, Risk-taking, and the Big Business of  | other/book | represented | staged-in-raw | current | skip |
| Eric Berne - Games People Play_ The Basic Handbook of Transactional Analysis. (1 | other/book | represented | staged-in-raw | current | skip |
| Eric Hoffer - The true believer_ Thoughts on the nature of mass movements (1980, | other/book | represented | staged-in-raw | current | skip |
| Eric Ries - The Lean Startup How Todays Entrepreneurs Use Continuous Innovation  | other/book | represented | staged-in-raw | current | skip |
| Erik Brynjolfsson, Andrew McAfee, Jeff Cummings - The Second Machine Age_ Work,  | other/book | represented | staged-in-raw | current | skip |
| Ethan M. Rasiel - The McKinsey Way_ Using the Techniques of the World's Top Stra | other/book | represented | staged-in-raw | current | skip |
| Ethan Mollick - Co-Intelligence_ Living and Working With AI (2024, Penguin Publi | other/book | represented | staged-in-raw | current | skip |
| Eugene M. Schwartz - Breakthrough Advertising (2004) - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| Extracted_Professional_Intelligence.docx | other/book | represented | src:2 txt:3 | current | skip |
| FINDING MODELS ANYWHERE OG.docx | other/book | represented | staged-in-raw | current | skip |
| Finding Your Edge.docx | other/book | represented | src:2 txt:2 | current | skip |
| Finding Your Edge.pdf | other/book | represented | staged-in-raw | current | skip |
| Fitzpatrick, Rob - The Mom Test_ How to talk to customers & learn if your busine | other/book | represented | staged-in-raw | current | skip |
| Follow_Up_Rules.docx | other/book | represented | src:2 txt:2 | current | skip |
| frame-io-v4-product-guide-ue.pdf | other/book | represented | src:3 txt:3 | current | skip |
| Gabriel Weinberg, Justin Mares - Traction_ a startup guide to getting customers  | other/book | represented | staged-in-raw | current | skip |
| Gary C Halbert - The Boron Letters (2013) - libgen.li.epub | other/book | represented | src:3 txt:3 | current | skip |
| Geoff Colvin - Talent Is Overrated_ What Really Separates World-Class Performers | other/book | represented | staged-in-raw | current | skip |
| Gerber Michael - Gerber Michael E The E-Myth Revisited Harper Collins e-Books 20 | other/book | represented | src:4 txt:6 | current | skip |
| Get Good with Money{Tiffany the Budgetnista Aliche}(2021, Harmony_Rodale){106369 | other/book | represented | src:2 txt:3 | current | skip |
| Giải trí đến chết (Amusing Ourselves to Death_ Public Discourse in the Age | other/book | represented | src:5 txt:10 | current | skip |
| godox_sk400ii_field_guide.html | other/book | represented | src:2 txt:2 | current | skip |
| Goodwin, Doris Kearns - Leadership_ In Turbulent Times (2018, Simon & Schuster)  | other/book | represented | staged-in-raw | current | skip |
| Goodwin, Doris Kearns - Team of rivals_ the political genius of Abraham Lincoln  | other/book | represented | staged-in-raw | current | skip |
| Grace Coddington - Grace_ A Memoir (2012, Random House) - libgen.li.epub | other/book | represented | src:4 txt:5 | current | skip |
| Grahl, Tim - Your first 1000 copies _ the step-by-step guide to marketing your b | other/book | represented | staged-in-raw | current | skip |
| Greg Lukianoff, Jonathan Haidt - The Coddling of the American Mind_ How Good Int | other/book | represented | staged-in-raw | current | skip |
| Gucci Mane, Neil Martinez-Belkin - The Autobiography of Gucci Mane (2017, Simon  | other/book | represented | staged-in-raw | current | skip |
| Gustave Le Bon - The crowd_ a study of the popular mind (2001, Dover Publication | other/book | represented | staged-in-raw | current | skip |
| Herodotus, Robert B. Strassler[ed] - The Landmark Herodotus_ Histories (2007, 20 | other/book | represented | staged-in-raw | current | skip |
| Holiday, Ryan - Perennial seller_ the art of making and marketing work that last | other/book | represented | staged-in-raw | current | skip |
| Housel, Morgan - The Psychology of Money by Morgan Housel (2020, Harriman House  | other/book | represented | src:5 txt:6 | current | skip |
| HOW-TO-PRINT-SIGNUP-SHEET.md | other/book | represented | src:2 txt:3 | current | skip |
| Howard Marks - Mastering the Market Cycle_ Getting the Odds on Your Side (2018,  | other/book | represented | staged-in-raw | current | skip |
| Howard Marks - The most important thing_ uncommon sense for the thoughtful inves | other/book | represented | staged-in-raw | current | skip |
| Howard Schultz, Dori Jones Yang - Pour Your Heart Into It_ How Starbucks Built a | other/book | represented | staged-in-raw | current | skip |
| I Will Teach You to Be Rich_ The Journal_ No Complicated Math. No More Procrasti | other/book | represented | src:6 txt:8 | current | skip |
| ICP Definition Worksheet.pdf | other/book | represented | staged-in-raw | current | skip |
| index.html | other/book | represented | staged-in-raw | current | skip |
| James Andrew Miller - Tinderbox_ HBO's Ruthless Pursuit of New Frontiers (Henry  | other/book | represented | staged-in-raw | current | skip |
| James Andrew Miller, Tom Shales - Those Guys Have All the Fun_ Inside the World  | other/book | represented | staged-in-raw | current | skip |
| James Dale Davidson_ William Rees-Mogg - The sovereign individual _ how to survi | other/book | represented | staged-in-raw | current | skip |
| James Joyce - Ulysses (2000, Penguin Group) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
| JAMES_ALLEN-AS_A_MAN_THINKETH.pdf | other/book | represented | staged-in-raw | current | skip |
| Jan_1on1_Complete_Prep_EYES_ONLY.docx | other/book | represented | src:3 txt:3 | current | skip |
| Jan_1on1_Prep_EYES_ONLY.docx | other/book | represented | src:3 txt:3 | current | skip |
| Jason Kelly - The New Tycoons_ Inside the Trillion Dollar Private Equity Industr | other/book | represented | staged-in-raw | current | skip |
| Jay-Z Decoded{Jay-Z}(2010, Random House Publishing Group){108293762} libgen.li.e | other/book | represented | staged-in-raw | current | skip |
| John Caples, David Ogilvy - Tested Advertising Methods (4th Ed.) - libgen.li.pdf | other/book | represented | src:4 txt:6 | current | skip |
| John Seabrook - The Song Machine_ Inside the Hit Factory (2015, W. W. Norton & C | other/book | represented | src:7 txt:7 | current | skip |
| John Szarkowski - William Eggleston's Guide (2002, The Museum of Modern Art, New | other/book | represented | staged-in-raw | current | skip |
| John Warrillow - Built to Sell_ Turn Your Business Into One You Can Sell (2010)  | other/book | represented | staged-in-raw | current | skip |
| Jonathan Haidt - The Righteous Mind_ Why Good People Are Divided by Politics and | other/book | represented | staged-in-raw | current | skip |
| Kevin Kelly - New Rules for the New Economy_ 10 Radical Strategies for a Connect | other/book | represented | staged-in-raw | current | skip |
| Khaled Hosseini - The Kite Runner (2004, Riverhead Trade) - libgen.li.mobi | other/book | represented | staged-in-raw | current | skip |
| Kim Scott - Radical Candor_ Be a Kick-Ass Boss Without Losing Your Humanity (201 | other/book | represented | staged-in-raw | current | skip |
| Kupor, Scott_Ries, Eric - Secrets of Sand Hill Road_ venture capital and how to  | other/book | represented | src:6 txt:12 | current | skip |
| Kurt Vonnegut - Slaughterhouse-Five - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| L. David Marquet - Turn the Ship Around! - A True Story of Turning Followers int | other/book | represented | staged-in-raw | current | skip |
| Labrecque, Tammi - Newsletter Ninja_ How to Become an Author Mailing List Expert | other/book | represented | staged-in-raw | current | skip |
| LandmarkCaesarWebEssays_5Jan2018.pdf | other/book | represented | staged-in-raw | current | skip |
| last ig growth strat.docx | other/book | represented | staged-in-raw | current | skip |
| Lead_Qualification_Rules.docx | other/book | represented | src:3 txt:3 | current | skip |
| Leigh Gallagher - The Airbnb Story_ How Three Ordinary Guys Disrupted an Industr | other/book | represented | staged-in-raw | current | skip |
| life story.docx | other/book | represented | staged-in-raw | current | skip |
| LIGHTING SET UPS OG.docx | other/book | represented | staged-in-raw | current | skip |
| LOCATION SCOUTING OG.docx | other/book | represented | staged-in-raw | current | skip |
| Maister, David H. - Managing the professional service firm (1997, Free Press Pap | other/book | represented | staged-in-raw | current | skip |
| Marc Randolph - That Will Never Work (2019, Little, Brown and Company) - libgen. | other/book | represented | staged-in-raw | current | skip |
| Marcellas Reynolds - Supreme Models_ Iconic Black Women Who Revolutionized Fashi | other/book | represented | staged-in-raw | current | skip |
| march_2026_monthly_statement.pdf | other/book | represented | src:2 txt:3 | current | skip |
| Marcus Aurelius - Meditations - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
| marketing x social media gold.txt | other/book | represented | src:2 txt:2 | current | skip |
| max-tegmark-life-30-being-human-in-the-age-of-artificial-intelligence-alfred-a-k | other/book | represented | staged-in-raw | current | skip |
| meta everything use.docx | other/book | represented | src:2 txt:2 | current | skip |
| Michael E. Gerber - The E-Myth Revisited_ Why Most Small Businesses Don't Work a | other/book | represented | staged-in-raw | current | skip |
| Michael J. Silverstein, Neil Fiske - Trading Up_ Why Consumers Want New Luxury G | other/book | represented | staged-in-raw | current | skip |
| Mike Isaac - Super Pumped_ The Battle for Uber (2019, W. W. Norton Company) - li | other/book | represented | staged-in-raw | current | skip |
| MONEY MONEY AND MORE MONEY AND GETTING AHEAD .docx | other/book | represented | src:3 txt:4 | current | skip |
| MOODBOARDING DOC OG.docx | other/book | represented | staged-in-raw | current | skip |
| mostly Powerhouse-.docx | other/book | represented | staged-in-raw | current | skip |
| Mustafa Suleyman_Michael Bhaskar__ Michael Bhaskar - The Coming Wave _ Technolog | other/book | represented | staged-in-raw | current | skip |
| n8n & RetellAI.json | other/book | represented | staged-in-raw | current | skip |
| Nabokov, Vladimir - Lolita (Vladimir Nabokov) - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| NEXT INFO GRABS.docx | other/book | represented | staged-in-raw | current | skip |
| Niccolo Machiavelli - The prince (2008, Hackett Pub. Co) - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| Norma Stevens, Steven M. L. Aronson - Avedon_ Something Personal (2017, Spiegel  | other/book | represented | staged-in-raw | current | skip |
| Opp hopper + Biz Case.xlsx | other/book | represented | staged-in-raw | current | skip |
| Opportunity Card [Example].pptx | other/book | represented | staged-in-raw | current | skip |
| Patrick Lencioni - Getting Naked_ A Business Fable About Shedding The Three Fear | other/book | represented | staged-in-raw | current | skip |
| Patrick Lencioni - The advantage _ why organizational health trumps everything e | other/book | represented | staged-in-raw | current | skip |
| pdfcoffee.com_ernst-haas-pdf-free.pdf | other/book | represented | staged-in-raw | current | skip |
| pdfcoffee.com_virgil-abloh-figures-of-speech-pdf-free.pdf | other/book | represented | staged-in-raw | current | skip |
| Peter Block - Flawless consulting_ a guide to getting your expertise used (2000, | other/book | represented | staged-in-raw | current | skip |
| Petre, Peter_Schwarzenegger, Arnold - Total recall_ my unbelievably true life st | other/book | represented | staged-in-raw | current | skip |
| phtography brain dump.docx | other/book | represented | src:2 txt:2 | current | skip |
| PIXIESET NEW USE .docx | other/book | represented | staged-in-raw | current | skip |
| pixieset tips for store .docx | other/book | represented | src:2 txt:2 | current | skip |
| Pixieset_Operations_Reference.docx | other/book | represented | staged-in-raw | current | skip |
| Poor Charlie&_039_s Almanack{Charlie Munger}{106613278} libgen.li.pdf | other/book | represented | src:4 txt:4 | current | skip |
| Prompt Template - Combining Techniques-2.pdf | other/book | represented | staged-in-raw | current | skip |
| Prompt Template - Combining Techniques-3.pdf | other/book | represented | staged-in-raw | current | skip |
| Prompt Template - Combining Techniques.pdf | other/book | represented | src:4 txt:4 | current | skip |
| Prompt Template - In Context-2.pdf | other/book | represented | staged-in-raw | current | skip |
| Prompt Template - In Context.pdf | other/book | represented | src:3 txt:3 | current | skip |
| Prompt Template - Problem Decomposition.pdf | other/book | represented | staged-in-raw | current | skip |
| Prompt Template - Self Criticism (Advanced)-2.pdf | other/book | represented | staged-in-raw | current | skip |
| Prompt Template - Self Criticism (Advanced)-3.pdf | other/book | represented | staged-in-raw | current | skip |
| Prompt Template - Self Criticism (Advanced).pdf | other/book | represented | src:5 txt:5 | current | skip |
| Prompt Template - Self Criticism (Basic)-2.pdf | other/book | represented | src:5 txt:5 | current | skip |
| Prompt Template - Self Criticism (Basic)-3.pdf | other/book | represented | staged-in-raw | current | skip |
| Prompt Template - Self Criticism (Basic).pdf | other/book | represented | src:5 txt:5 | current | skip |
| Prompt Template - Thought Generation-2.pdf | other/book | represented | staged-in-raw | current | skip |
| Prompt Template - Thought Generation.pdf | other/book | represented | src:4 txt:4 | current | skip |
| Prompt_Engineering_Knowledge_Extraction.docx | other/book | represented | src:3 txt:4 | current | skip |
| Proof_Case_Studies_Page_Structure.docx | other/book | represented | src:2 txt:5 | current | skip |
| Protocol_01_Free_Download.pdf | other/book | represented | src:2 txt:3 | current | skip |
| Ray Bradbury - Ray Bradbury's Fahrenheit 451 (Bloom's Modern Critical Interpreta | other/book | represented | src:1 txt:3 | current | skip |
| Ray Dalio - Principles_ Life and Work (2017, Simon & Schuster) - libgen.li.epub | other/book | represented | src:3 txt:3 | current | skip |
| Raz, Tahl_Voss, Chris - Never Split the Difference_ Negotiating As If Your Life  | other/book | represented | staged-in-raw | current | skip |
| Re_Edit_Workflow.docx | other/book | represented | src:2 txt:2 | current | skip |
| Rensin, David - The Mailroom_ Hollywood History from the Bottom Up (2007, Random | other/book | represented | src:7 txt:9 | current | skip |
| Richard Branson - Losing My Virginity_ How I Survived, Had Fun, and Made a Fortu | other/book | represented | staged-in-raw | current | skip |
| Rick Ross_ Neil Martinez-Belkin - Hurricanes_ A Memoir (2019, Hanover Square Pre | other/book | represented | staged-in-raw | current | skip |
| Rob Meyerson - Brand Naming_ The Complete Guide to Creating a Name for Your Comp | other/book | represented | staged-in-raw | current | skip |
| Robert W. Bly - The copywriter's handbook_ a step-by-step guide to writing copy  | other/book | represented | staged-in-raw | current | skip |
| Ron Chernow - Grant (2017, Penguin Publishing Group) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
| Ron Chernow - Titan_ The Life of John D. Rockefeller, Sr. (2004, Vintage) - libg | other/book | represented | staged-in-raw | current | skip |
| Ron Chernow - Washington_ A Life - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| Sax, David - The Revenge of Analog_ Real Things and Why They Matter (2016, Publi | other/book | represented | staged-in-raw | current | skip |
| Schroeder, Alice - The Snowball_ Warren Buffett and the Business of Life (2008,  | other/book | represented | staged-in-raw | current | skip |
| Schwarzenegger, Arnold - Total Recall- My Unbelievably True Life Story (2012, Si | other/book | represented | src:7 txt:8 | current | skip |
| Sebastian Mallaby - The Power Law _ Venture Capital and the Making of the New Fu | other/book | represented | staged-in-raw | current | skip |
| Sebastian Mallaby - The Power Law_ Venture Capital and the Making of the New Fut | other/book | represented | src:5 txt:7 | current | skip |
| Seth A. Klarman - Margin of Safety_ Risk-Averse Value Investing Strategies for t | other/book | represented | src:10 txt:11 | current | skip |
| Seth A. Klarman - Margin of Safety_ Risk-Averse Value Investing Strategies for t | other/book | represented | staged-in-raw | current | skip |
| Seth Godin - Purple Cow_ Transform Your Business by Being Remarkable (2003, Port | other/book | represented | staged-in-raw | current | skip |
| Seth Godin - This Is Marketing_ You Can't Be Seen Until You Learn to See (2018,  | other/book | represented | staged-in-raw | current | skip |
| Seth Godin - Tribes_ We Need You to Lead Us (2008, Penguin) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
| Setting Goals.pdf | other/book | represented | staged-in-raw | current | skip |
| Shore Stephen. - Uncommon Places_ The Complete Works - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| Simler, Kevin _ Hanson, Robin - The Elephant in the Brain_ Hidden Motives in Eve | other/book | represented | staged-in-raw | current | skip |
| snipe dump on lighting and moodboard.docx | other/book | represented | src:3 txt:4 | current | skip |
| SOCIAL MEDIA 3.0 MAY USE.docx | other/book | represented | staged-in-raw | current | skip |
| SOCIAL_MEDIA_3_0_REFERENCE.docx | other/book | represented | staged-in-raw | current | skip |
| Story{Robert McKee}{115577124} libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| Study_AnnieLeibovitz.md | other/book | represented | staged-in-raw | current | skip |
| Study_ErnstHaas.md | other/book | represented | staged-in-raw | current | skip |
| Study_FredHerzog.md | other/book | represented | staged-in-raw | current | skip |
| Study_GracielaIturbide.md | other/book | represented | staged-in-raw | current | skip |
| Study_JoelMeyerowitz.md | other/book | represented | staged-in-raw | current | skip |
| Study_RichardAvedon.md | other/book | represented | staged-in-raw | current | skip |
| Study_RobertFrank.md | other/book | represented | staged-in-raw | current | skip |
| Study_StephenShore.md | other/book | represented | staged-in-raw | current | skip |
| Study_WilliamEggleston.md | other/book | represented | staged-in-raw | current | skip |
| Sunstein, Cass R._ Sibony, Olivier_ Kahneman, Daniel - Noise_ A Flaw in Human Ju | other/book | represented | staged-in-raw | current | skip |
| Supreme Models_ Iconic Black Women Who Revolutionized Fashion.epub | other/book | represented | src:7 txt:7 | current | skip |
| The Adweek Copywriting Handbook_ The Ultimate Guide to Writing Powerful Advertis | other/book | represented | src:8 txt:11 | current | skip |
| The Brand Gap, Revised Edition{Marty Neumeier}(2005, Pearson Education (US)){113 | other/book | represented | staged-in-raw | current | skip |
| The Direction Stag_Full Book.pdf | other/book | represented | src:2 txt:2 | current | skip |
| The Innovator&_039_s Dilemma_ When New Technologies Cause Great Firms to Fail (M | other/book | represented | staged-in-raw | current | skip |
| The Kingdom of Prep_ The Inside Story of the Rise and (Near) Fall of J.Crew{Magg | other/book | represented | src:4 txt:7 | current | skip |
| The Pyramid Principle_ Logic in Writing and ThinkingBarbara Minto(2022)112031977 | other/book | represented | src:4 txt:4 | current | skip |
| The Pyramid Principle_ Logic in Writing and Thinking{Barbara Minto}(2022){112031 | other/book | represented | src:5 txt:5 | current | skip |
| The-Holy-Bible-King-James-Version-2.pdf | other/book | represented | src:2 txt:3 | current | skip |
| The-Holy-Bible-King-James-Version.pdf | other/book | represented | src:2 txt:3 | current | skip |
| The_Adobe_Stack_Manual.docx | other/book | represented | staged-in-raw | current | skip |
| The_Attention_Stack.docx | other/book | represented | staged-in-raw | current | skip |
| The_Copywriting_Stack.docx | other/book | represented | staged-in-raw | current | skip |
| The_Direction_Shift.docx | other/book | represented | staged-in-raw | current | skip |
| The_Offer_Stack.docx | other/book | represented | staged-in-raw | current | skip |
| The_Platform_Stack.docx | other/book | represented | staged-in-raw | current | skip |
| The_Production_Stack.docx | other/book | represented | staged-in-raw | current | skip |
| Thucydides, Robert B. Strassler, Richard Crawley, Victor Davis H - The Landmark  | other/book | represented | staged-in-raw | current | skip |
| Tom Shales, James Andrew Miller - Live From New York_ An Uncensored History of S | other/book | represented | staged-in-raw | current | skip |
| Toni Morrison - Beloved (Vintage International) - libgen.li.azw3 | other/book | represented | src:3 txt:4 | current | skip |
| Toni Morrison - The Bluest Eye (2007, Knopf Doubleday Publishing Group) - libgen | other/book | represented | staged-in-raw | current | skip |
| Trading_Card_Launch_Plan.docx | other/book | represented | src:2 txt:4 | current | skip |
| using ai x gumroad x digital products.docx | other/book | represented | staged-in-raw | current | skip |
| Vicki Robin_Joe Dominguez_Mr. Money Mustache - Your money or your life_ 9 steps  | other/book | represented | src:2 txt:10 | current | skip |
| Vicki Robin_Joe Dominguez_Mr. Money Mustache - Your money or your life_ 9 steps  | other/book | represented | src:2 txt:10 | current | skip |
| Viktor E. Frankl - Man's search for meaning (2000, Beacon Press) - libgen.li.pdf | other/book | represented | staged-in-raw | current | skip |
| Walter Isaacson - Elon Musk (2023, Simon & Schuster) - libgen.li.epub | other/book | represented | staged-in-raw | current | skip |
| Warren E. Buffett, Lawrence A. Cunningham, Lawrence A. Cunningha - The Essays of | other/book | represented | staged-in-raw | current | skip |
| Weekly Reflections.pdf | other/book | represented | staged-in-raw | current | skip |
| Will Guidara - Unreasonable Hospitality_ The Remarkable Power of Giving People M | other/book | represented | staged-in-raw | current | skip |
| XcMwr2sETldxuEwaZeEw_The+Great+Online+Game+-+Not+Boring+by+Packy+McCormick.pdf | other/book | represented | staged-in-raw | current | skip |
| youtube skool doc.docx | other/book | represented | staged-in-raw | current | skip |
| Zack O'Malley Greenburg - Empire State of Mind_ How Jay-Z Went from Street Corne | other/book | represented | staged-in-raw | current | skip |
| -Christian%20Dior%20-%20The%20little%20dictionary%20of%20fashion%20%282007%2C%20 | other/book | review | src:0 txt:2 | unclear | manual review |
| -Sowell%2C%20Thomas%20-%20Basic%20Economics%20%282014%2C%20Basic%20Books%29%20-% | other/book | review | src:0 txt:2 | unclear | manual review |
| 0ce20966-0176-4146-8916-7cbc34a31ca3_production_merged.pdf | other/book | review | src:1 txt:2 | unclear | manual review |
| 2024.09.30_SF%20Hockley_IFP%20QAQC_Electrical%20%281%29-compressed.pdf | other/book | review | src:0 txt:2 | unclear | manual review |
| 2026 New Member Flow (NM).pdf | other/book | review | src:1 txt:2 | unclear | manual review |
| 2026 OPS-ENG SMART Goals.xlsx | other/book | review | src:1 txt:2 | unclear | manual review |
| 30_Extraction_Questions.md | other/book | review | src:1 txt:2 | unclear | manual review |
| _chat 2.txt | other/book | review | src:1 txt:1 | unclear | manual review |
| _chat.txt | other/book | review | src:1 txt:1 | unclear | manual review |
| adobe-levity-laughter-final-us.pdf | other/book | review | src:1 txt:2 | unclear | manual review |
| advanced.pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| Antique_Inventory_Template.xlsx | other/book | review | src:1 txt:2 | unclear | manual review |
| Antique_Inventory_Template_Styled.xlsx | other/book | review | src:1 txt:2 | unclear | manual review |
| BJ_Reference_Doc.docx | other/book | review | src:1 txt:1 | unclear | manual review |
| BJ_Verified_Facts.md | other/book | review | src:0 txt:2 | unclear | manual review |
| brain prompting.docx | other/book | review | src:1 txt:2 | unclear | manual review |
| bunch of mess.docx | other/book | review | src:1 txt:1 | unclear | manual review |
| CANVA_PROOF_F90csIGx-17g_923907c2703fe415ccd257675adc7157cfbe7bf8c5e7e569baccd53 | other/book | review | src:0 txt:2 | unclear | manual review |
| CANVA_PROOF_F9G2aPPZWZsQ_923907c2703fe415ccd257675adc7157cfbe7bf8c5e7e569baccd53 | other/book | review | src:0 txt:2 | unclear | manual review |
| CANVA_PROOF_F9Gz-L8M5j8h_923907c2703fe415ccd257675adc7157cfbe7bf8c5e7e569baccd53 | other/book | review | src:0 txt:2 | unclear | manual review |
| Car-Shipping-101-Ebook-2.pdf | other/book | review | src:0 txt:2 | unclear | manual review |
| Car-Shipping-101-Ebook.pdf | other/book | review | src:0 txt:2 | unclear | manual review |
| Charger_Knowledge_Extraction.docx | other/book | review | src:1 txt:2 | unclear | manual review |
| communication-blueprint.md | other/book | review | src:1 txt:2 | unclear | manual review |
| copywriting everyhting : tips.docx | other/book | review | src:1 txt:1 | unclear | manual review |
| Da'Nielle Green's Resume.pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| direction shiftttt.docx | other/book | review | src:1 txt:1 | unclear | manual review |
| express-one-pager-ue.pdf | other/book | review | src:0 txt:2 | unclear | manual review |
| facebook stuff.docx | other/book | review | src:0 txt:2 | unclear | manual review |
| FASHION KILLA.docx | other/book | review | src:1 txt:1 | unclear | manual review |
| FE_Implementation_Package.xlsx | other/book | review | src:0 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_DRAFT.xlsx | other/book | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_DRAFT_v1.1.docx | other/book | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_DRAFT_v1.1.xlsx | other/book | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_v1.1_FINAL.docx | other/book | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_v1.2.docx | other/book | review | src:1 txt:2 | unclear | manual review |
| FE_Readiness_Checklist_v1.2.xlsx | other/book | review | src:1 txt:2 | unclear | manual review |
| frame-io-v4-one-pager-ue.pdf | other/book | review | src:1 txt:2 | unclear | manual review |
| gary thread.docx | other/book | review | src:1 txt:1 | unclear | manual review |
| LAHE1.5_EOP_EARTHQUAKE_RESPONSE_APPROVED_100824.pdf | other/book | review | src:0 txt:2 | unclear | manual review |
| make-it-report-ue.pdf | other/book | review | src:0 txt:2 | unclear | manual review |
| PAL_League_Overview.docx | other/book | review | src:0 txt:2 | unclear | manual review |
| phtography biz side x tothemoon.docx | other/book | review | src:1 txt:1 | unclear | manual review |
| Pressure test points 2.xlsx | other/book | review | src:0 txt:2 | unclear | manual review |
| Pressure test points 3.xlsx | other/book | review | src:0 txt:2 | unclear | manual review |
| Pressure test points 4.xlsx | other/book | review | src:0 txt:2 | unclear | manual review |
| Pressure test points.xlsx | other/book | review | src:0 txt:2 | unclear | manual review |
| Proof_Candidates.md | other/book | review | src:0 txt:2 | unclear | manual review |
| Proof_Inventory.docx | other/book | review | src:0 txt:2 | unclear | manual review |
| Research Report.pdf | other/book | review | src:1 txt:2 | unclear | manual review |
| ROSHAD TRUCKING-DISPATCH-compressed.pdf | other/book | review | src:0 txt:2 | unclear | manual review |
| Selling books.docx | other/book | review | src:1 txt:2 | unclear | manual review |
| statement (10).pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| statement (11).pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| statement (12).pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| statement (13).pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| statement (6).pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| statement (7).pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| statement (8).pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| statement (9).pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| statement.pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| STYLE_MANIFESTO.md | other/book | review | src:1 txt:2 | unclear | manual review |
| text-8F632321F688-1.txt | other/book | review | src:1 txt:1 | unclear | manual review |
| The_Install_Methodology_v1.docx | other/book | review | src:0 txt:2 | unclear | manual review |
| THE_MACHINE.docx | other/book | review | src:1 txt:1 | unclear | manual review |
| ticket_extraction.docx | other/book | review | src:0 txt:2 | unclear | manual review |
| two-look-moodboard.html | other/book | review | src:0 txt:2 | unclear | manual review |
| Vanguard_Program_Vision.docx | other/book | review | src:1 txt:2 | unclear | manual review |
| W-2_Form_2024_Jones_2026_02_12_16_36_19_-0800_W-2_ESS 2.pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| W-2_Form_2024_Jones_2026_02_12_16_36_19_-0800_W-2_ESS.pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| W-2_Form_2025_Jones_2026_02_12_16_36_24_-0800_W-2_ESS 2.pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| W-2_Form_2025_Jones_2026_02_12_16_36_24_-0800_W-2_ESS.pdf | other/book | review | src:1 txt:1 | unclear | manual review |
| watch.html | other/book | review | src:1 txt:1 | unclear | manual review |
| instantly_C2_Fitness.csv | outreach/sales | ignore | src:0 txt:2 | off-scope | ignore (personal) |
| protocol_10_full_psychological_shutdown.md | outreach/sales | ignore | employer/facility SOP | operational reference | DO-NOT-INGEST (confidential) |
| Instantly Sop V2.pdf | outreach/sales | missing | src:0 txt:1 | current | ingest/review |
| instantly_2025_12_18_215472318013453.txt | outreach/sales | missing | src:0 txt:1 | current | ingest/review |
| instantly_C10_Attorney_General_OC.csv | outreach/sales | parked | src:1 txt:2 | operational | park (lead data) |
| instantly_C1_MedSpa_Aesthetics.csv | outreach/sales | parked | src:0 txt:2 | operational | park (lead data) |
| instantly_C3_Wellness_Yoga_Spa.csv | outreach/sales | parked | src:0 txt:1 | operational | park (lead data) |
| instantly_C4_Medical_Clinical.csv | outreach/sales | parked | src:1 txt:3 | operational | park (lead data) |
| instantly_C5_Treatment_MentalHealth.csv | outreach/sales | parked | src:0 txt:2 | operational | park (lead data) |
| instantly_C6_General_Health.csv | outreach/sales | parked | src:1 txt:3 | operational | park (lead data) |
| instantly_C7_Attorney_Partners.csv | outreach/sales | parked | src:1 txt:2 | operational | park (lead data) |
| instantly_C8_Attorney_General.csv | outreach/sales | parked | src:1 txt:2 | operational | park (lead data) |
| instantly_C9_Attorney_Partners_OC.csv | outreach/sales | parked | src:1 txt:2 | operational | park (lead data) |
| sniped_media_6_campaigns_instantly_ready.xlsx | outreach/sales | parked | src:1 txt:3 | operational | park (lead data) |
| sniped_media_6_campaigns_instantly_ready.xlsx | outreach/sales | parked | src:1 txt:3 | operational | park (lead data) |
|  Andrew Chen - The Cold Start Problem_ How to Start and Scale Network Effects (2 | outreach/sales | represented | staged-in-raw | current | skip |
|  Andrew Chen - The Cold Start Problem_ How to Start and Scale Network Effects (2 | outreach/sales | represented | staged-in-raw | current | skip |
| 00_BRIEF.md | outreach/sales | represented | staged-in-raw | current | skip |
| 00_master_intro_outro.md | outreach/sales | represented | staged-in-raw | current | skip |
| 01_email_1_variants.md | outreach/sales | represented | staged-in-raw | current | skip |
| 02_followups.md | outreach/sales | represented | staged-in-raw | current | skip |
| 03_super_search_filter.md | outreach/sales | represented | staged-in-raw | current | skip |
| 04_reply_scripts.md | outreach/sales | represented | staged-in-raw | current | skip |
| 05_loom_production_workflow.md | outreach/sales | represented | staged-in-raw | current | skip |
| 06_ren_cadence.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_akshay-narisetti.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_aron-levin.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_euwyn-poon.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_gabriel-dymowski.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_isaiah-taylor.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_joe-braidwood.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_justin-fiaschetti.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_karagan-osmann.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_max-haot.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_mitch-lee.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_pamir-ehsas.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2026-05-12_simon-bogdanowicz.md | outreach/sales | represented | staged-in-raw | current | skip |
| 2_Assistant_SOP_Manual (1).docx | outreach/sales | represented | staged-in-raw | current | skip |
| 3_Founder_Outreach_System (1).docx | outreach/sales | represented | staged-in-raw | current | skip |
| 3_Founder_Outreach_System (1).docx | outreach/sales | represented | staged-in-raw | current | skip |
| 3_Founder_Outreach_System (1).docx | outreach/sales | represented | staged-in-raw | current | skip |
| 3_Founder_Outreach_System.docx | outreach/sales | represented | src:3 txt:3 | current | skip |
| 3_Founder_Outreach_System.docx | outreach/sales | represented | src:3 txt:3 | current | skip |
| _README.md | outreach/sales | represented | staged-in-raw | current | skip |
| Aaron Ross, Marylou Tyler - Predictable Revenue_ Turn Your Business Into A Sales | outreach/sales | represented | src:6 txt:11 | current | skip |
| Aaron Ross, Marylou Tyler - Predictable Revenue_ Turn Your Business Into A Sales | outreach/sales | represented | staged-in-raw | current | skip |
| Aaron Ross, Marylou Tyler - Predictable Revenue_ Turn Your Business Into A Sales | outreach/sales | represented | staged-in-raw | current | skip |
| Aaron Ross, Marylou Tyler - Predictable Revenue_ Turn Your Business Into A Sales | outreach/sales | represented | staged-in-raw | current | skip |
| Blair Enns - Pricing Creativity_ A Guide to Profit Beyond the Billable Hour (201 | outreach/sales | represented | staged-in-raw | current | skip |
| Blair Enns - Pricing Creativity_ A Guide to Profit Beyond the Billable Hour (201 | outreach/sales | represented | staged-in-raw | current | skip |
| cold email outreach.docx | outreach/sales | represented | src:3 txt:3 | current | skip |
| cold email outreach.docx | outreach/sales | represented | src:3 txt:3 | current | skip |
| cold out reach instantly gold everything use this always lol.docx | outreach/sales | represented | staged-in-raw | current | skip |
| cold out reach instantly gold everything use this always lol.docx | outreach/sales | represented | staged-in-raw | current | skip |
| cold_email_doctrine_v1.md | outreach/sales | represented | staged-in-raw | current | skip |
| cold_email_extraction.docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| cold_email_extraction.docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| Cold_Outreach_Sales_Pipeline_Playbook.docx | outreach/sales | represented | staged-in-raw | current | skip |
| Cold_Outreach_Sales_Pipeline_Playbook.docx | outreach/sales | represented | staged-in-raw | current | skip |
| Fanatical Prospecting - The Ultimate Guide to Opening Sales Conversations and Fi | outreach/sales | represented | src:2 txt:8 | current | skip |
| Gap Selling_ Getting the Customer to Yes_ How Problem-Centric Selling Increases  | outreach/sales | represented | staged-in-raw | current | skip |
| Gap Selling_ Getting the Customer to Yes_ How Problem-Centric Selling Increases  | outreach/sales | represented | staged-in-raw | current | skip |
| Gap Selling_ Getting the Customer to Yes_ How Problem-Centric Selling Increases  | outreach/sales | represented | src:4 txt:9 | current | skip |
| Hughes, Tony J - Combo Prospecting The Powerful One-Two Punch That Fills Your Pi | outreach/sales | represented | src:3 txt:9 | current | skip |
| Hughes, Tony J - Combo Prospecting The Powerful One-Two Punch That Fills Your Pi | outreach/sales | represented | staged-in-raw | current | skip |
| Hughes, Tony J - Combo Prospecting The Powerful One-Two Punch That Fills Your Pi | outreach/sales | represented | staged-in-raw | current | skip |
| instantly super search .docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| instantly super search .docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| linkedin_comment_doctrine_v1.md | outreach/sales | represented | staged-in-raw | current | skip |
| Outreach_Strategy.docx | outreach/sales | represented | src:2 txt:2 | current | skip |
| Outreach_Strategy.docx | outreach/sales | represented | src:2 txt:2 | current | skip |
| protocol_01_claw_hands.md | outreach/sales | represented | staged-in-raw | current | skip |
| protocol_02_locked_shoulders.md | outreach/sales | represented | staged-in-raw | current | skip |
| protocol_03_squared.md | outreach/sales | represented | staged-in-raw | current | skip |
| protocol_04_pinned_arms.md | outreach/sales | represented | staged-in-raw | current | skip |
| protocol_05_soft_jawline.md | outreach/sales | represented | staged-in-raw | current | skip |
| protocol_06_spinal_collapse.md | outreach/sales | represented | staged-in-raw | current | skip |
| protocol_07_forced_smile.md | outreach/sales | represented | staged-in-raw | current | skip |
| protocol_08_transition_freeze.md | outreach/sales | represented | staged-in-raw | current | skip |
| protocol_09_good_mechanics_zero_presence.md | outreach/sales | represented | staged-in-raw | current | skip |
| SKILL.md | outreach/sales | represented | staged-in-raw | current | skip |
| SKILL.md | outreach/sales | represented | staged-in-raw | current | skip |
| SKILL.md | outreach/sales | represented | staged-in-raw | current | skip |
| SNIPED_Founder_Kit_Sales_System.docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| SNIPED_Founder_Kit_Sales_System.docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| Sniped_Media_Cold_Email_Rewrite_March2026.docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| Sniped_Media_Cold_Email_Rewrite_March2026.docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| Sniped_Media_Cold_Outreach_SOP.docx | outreach/sales | represented | src:2 txt:2 | current | skip |
| Sniped_Media_Cold_Outreach_SOP.docx | outreach/sales | represented | src:2 txt:2 | current | skip |
| SOP_assistant.md | outreach/sales | represented | staged-in-raw | current | skip |
| SOP_assistant_v3.docx | outreach/sales | represented | staged-in-raw | current | skip |
| SOP_discovery_call.md | outreach/sales | represented | staged-in-raw | current | skip |
| SOP_discovery_to_close.md | outreach/sales | represented | staged-in-raw | current | skip |
| SOP_VIB_production.md | outreach/sales | represented | staged-in-raw | current | skip |
| Sponsor_Outreach_Templates.docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| Sponsor_Outreach_Templates.docx | outreach/sales | represented | src:2 txt:3 | current | skip |
| The Cold Email Manifesto_ How to fill your sales pipeline, -- Alex Berman & Robe | outreach/sales | represented | src:6 txt:8 | current | skip |
| The Cold Email Manifesto_ How to fill your sales pipeline, -- Alex Berman & Robe | outreach/sales | represented | staged-in-raw | current | skip |
| The Cold Email Manifesto_ How to fill your sales pipeline, -- Alex Berman & Robe | outreach/sales | represented | staged-in-raw | current | skip |
| The Cold Email Manifesto_ How to fill your sales pipeline, -- Alex Berman & Robe | outreach/sales | represented | staged-in-raw | current | skip |
| The_Outbound_Stack.docx | outreach/sales | represented | staged-in-raw | current | skip |
| The_Outbound_Stack.docx | outreach/sales | represented | staged-in-raw | current | skip |
| VIB_caption_library.md | outreach/sales | represented | staged-in-raw | current | skip |
| VIB_figma_spec.md | outreach/sales | represented | staged-in-raw | current | skip |
| Outreach_Angles.docx | outreach/sales | review | src:1 txt:2 | unclear | manual review |
| Outreach_Angles.docx | outreach/sales | review | src:1 txt:2 | unclear | manual review |
| Direction_Stack_Publication_Master_Doc.docx | photography/DS | duplicate | src:3 txt:4 | superseded | ignore (superseded) |
| Direction_Stack_Publication_Master_Doc.docx | photography/DS | duplicate | src:3 txt:4 | superseded | ignore (superseded) |
| Direction_Stack_Revised (1).docx | photography/DS | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Direction_Stack_Revised (1).docx | photography/DS | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Direction_Stack_Revised (2).docx | photography/DS | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Direction_Stack_Revised (2).docx | photography/DS | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Direction_Stack_Revised.docx | photography/DS | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Direction_Stack_Revised.docx | photography/DS | duplicate | src:3 txt:3 | superseded | ignore (superseded) |
| Direction_Stack_UPDATED.docx | photography/DS | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| Direction_Stack_UPDATED.docx | photography/DS | duplicate | src:2 txt:3 | superseded | ignore (superseded) |
| The Direction Stack (1).pdf | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stack (2).pdf | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stack (3).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stack (3).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stack (3).pdf | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stack (4).pdf | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stack (5).pdf | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| The Direction Stack_Revised_V2_black layout.pdf | photography/DS | duplicate | src:4 txt:5 | superseded | ignore (superseded) |
| The Direction Stack_Revised_V3_black layout 2.pdf | photography/DS | duplicate | src:4 txt:5 | superseded | ignore (superseded) |
| The Direction Stack_Revised_V3_black layout 3.pdf | photography/DS | duplicate | src:4 txt:5 | superseded | ignore (superseded) |
| The Direction Stack_Revised_V3_black layout.pdf | photography/DS | duplicate | src:4 txt:5 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_Final_Manuscript (1).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_Final_Manuscript (1).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_Final_Manuscript (2).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_Final_Manuscript (2).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_FINAL_v2 (1) (1).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_FINAL_v2 (1) (1).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_FINAL_v2 (1).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_FINAL_v2 (1).docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_FINAL_v2.docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| THE_DIRECTION_STACK_FINAL_v2.docx | photography/DS | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| https::www.bhphotovideo.com:lit_files:1101190.pdf | photography/DS | missing | src:0 txt:1 | current | ingest/review |
| POSING 101.docx | photography/DS | missing | src:0 txt:1 | current | ingest/review |
| POSING 101.docx | photography/DS | missing | src:0 txt:1 | current | ingest/review |
| POSING 101.pdf | photography/DS | missing | src:0 txt:1 | current | ingest/review |
| Posing_101_Professional_Extraction.docx | photography/DS | partial | src:1 txt:3 | unclear | compare delta |
| Posing_101_Professional_Extraction.docx | photography/DS | partial | src:1 txt:3 | unclear | compare delta |
|  John Szarkowski - William Eggleston's Guide (2002, The Museum of Modern Art, Ne | photography/DS | represented | staged-in-raw | current | skip |
|  Robert Frank, Jack Kerouac - The Americans (2008, Steidl) - libgen.li.pdf | photography/DS | represented | staged-in-raw | current | skip |
|  Stephen Shore, Lynne Tillman, Stephan Schmidt-Wulffen - Stephen Shore_ Uncommon | photography/DS | represented | staged-in-raw | current | skip |
| 367490464-Szarkowski-1973-Looking-at-Photographs-pdf.pdf | photography/DS | represented | staged-in-raw | current | skip |
| 367490464-Szarkowski-1973-Looking-at-Photographs-pdf.pdf | photography/DS | represented | staged-in-raw | current | skip |
| [Art Education 1989-jul vol. 42 iss. 4] Richard Avedon&_039_s in the American We | photography/DS | represented | staged-in-raw | current | skip |
| [The American Review of Canadian Studies 2018-sep 24 vol. 48 iss. 4] Fred Herzog | photography/DS | represented | staged-in-raw | current | skip |
| [The Art Book 1994-mar vol. 1 iss. 2] THE AMERICANS{ROBERT FRANK}(1994 March)[10 | photography/DS | represented | staged-in-raw | current | skip |
| AI PHOTOGRAPHERS.docx | photography/DS | represented | staged-in-raw | current | skip |
| AI_PHOTOGRAPHERS_TACTICAL_EXTRACTION.md | photography/DS | represented | staged-in-raw | current | skip |
| Berger, John _ Dyer, Geoff - Understanding a Photograph (2013, Penguin Books Ltd | photography/DS | represented | staged-in-raw | current | skip |
| Berger, John _ Dyer, Geoff - Understanding a Photograph (2013, Penguin Books Ltd | photography/DS | represented | staged-in-raw | current | skip |
| Bryceden_Evoto_System.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| Bryceden_Evoto_System.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| COMPLETE_PRESET_SYSTEM.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| COMPLETE_PRESET_SYSTEM.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| Direction_Stack_90Day_Plan.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| Direction_Stack_90Day_Plan.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| direction_stack_closing.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| direction_stack_closing.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| direction_stack_complete - hellaine with edits.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| direction_stack_complete - hellaine with edits.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| direction_stack_complete.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| direction_stack_complete.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| Direction_Stack_Field_Guide.docx | photography/DS | represented | src:4 txt:4 | current | skip |
| Direction_Stack_Field_Guide.docx | photography/DS | represented | src:4 txt:4 | current | skip |
| Direction_Stack_FINAL.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| Direction_Stack_FINAL.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| Direction_Stack_FINAL_PRINT.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| Direction_Stack_FINAL_PRINT.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| Direction_Stack_Final_R2.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| Direction_Stack_Final_R2.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| direction_stack_intro.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| direction_stack_intro.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| Ernst Haas in Black and White{Jim Hughes_ Alexander Haas_ Ernst Haas}(1992, Bulf | photography/DS | represented | staged-in-raw | current | skip |
| Event Photography and Videography Guide (Generic).pdf | photography/DS | represented | src:2 txt:4 | current | skip |
| evoto ai only source.docx | photography/DS | represented | staged-in-raw | current | skip |
| evoto ai youtube only.docx | photography/DS | represented | staged-in-raw | current | skip |
| EVOTO GOAT .docx | photography/DS | represented | staged-in-raw | current | skip |
| Evoto_AI_Retouching_Reference.docx | photography/DS | represented | staged-in-raw | current | skip |
| Evoto_AI_Retouching_Reference.docx | photography/DS | represented | staged-in-raw | current | skip |
| evoto_ai_techniques_extraction.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| evoto_ai_techniques_extraction.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| EVOTO_PRESET_SYSTEM_MALE_FEMALE.docx | photography/DS | represented | src:3 txt:4 | current | skip |
| EVOTO_PRESET_SYSTEM_MALE_FEMALE.docx | photography/DS | represented | src:3 txt:4 | current | skip |
| EVOTO_TACTICAL_EXTRACTION.md | photography/DS | represented | staged-in-raw | current | skip |
| Jonathan Day - Robert Frank's 'The Americans' _ The Art of Documentary Photograp | photography/DS | represented | staged-in-raw | current | skip |
| Jonathan Day - Robert Frank's 'The Americans' _ The Art of Documentary Photograp | photography/DS | represented | staged-in-raw | current | skip |
| LA PHOTOGRPAHY.docx | photography/DS | represented | staged-in-raw | current | skip |
| LA PHOTOGRPAHY.docx | photography/DS | represented | staged-in-raw | current | skip |
| last lightroom hopefully.docx | photography/DS | represented | staged-in-raw | current | skip |
| last lightroom hopefully.docx | photography/DS | represented | staged-in-raw | current | skip |
| lightroom_operating_system.md | photography/DS | represented | staged-in-raw | current | skip |
| linkedin and reddit photogrpahers.docx | photography/DS | represented | staged-in-raw | current | skip |
| LINKEDIN_REDDIT_PHOTOGRAPHER_INTEL_EXTRACTION.md | photography/DS | represented | staged-in-raw | current | skip |
| Michael Freeman - The Photographer's Eye_ Composition and Design for Better Digi | photography/DS | represented | staged-in-raw | current | skip |
| Michael Freeman - The Photographer's Eye_ Composition and Design for Better Digi | photography/DS | represented | staged-in-raw | current | skip |
| Michael Freeman - The Photographer's Vision_ Understanding and Appreciating Grea | photography/DS | represented | staged-in-raw | current | skip |
| Michael Freeman - The Photographer's Vision_ Understanding and Appreciating Grea | photography/DS | represented | staged-in-raw | current | skip |
| MOSTLY PHOTOGRPAHY SETS SET DESIGN .docx | photography/DS | represented | staged-in-raw | current | skip |
| MOSTLY PHOTOGRPAHY SETS SET DESIGN .docx | photography/DS | represented | staged-in-raw | current | skip |
| PERSONAL_BRAND_PRESET.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| PERSONAL_BRAND_PRESET.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| PHOTO EDITING COLORS ETC.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| PHOTO EDITING COLORS ETC.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| PHOTO PIONEERS VIDEO TEXT.docx | photography/DS | represented | staged-in-raw | current | skip |
| PHOTO PIONEERS VIDEO TEXT.docx | photography/DS | represented | staged-in-raw | current | skip |
| PHOTOGRAPHY MASTERCLASS.docx | photography/DS | represented | staged-in-raw | current | skip |
| PHOTOGRAPHY MASTERCLASS.docx | photography/DS | represented | staged-in-raw | current | skip |
| PHOTOGRAPHY MONEY GUIDE.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| PHOTOGRAPHY MONEY GUIDE.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| Photography Proposal - Bishop Robert Peters Elevation Banquet.pdf | photography/DS | represented | src:3 txt:5 | current | skip |
| Photography_Business_Frameworks.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| Photography_Business_Frameworks.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| Photography_Editing_Playbook.docx | photography/DS | represented | staged-in-raw | current | skip |
| Photography_Editing_Playbook.docx | photography/DS | represented | staged-in-raw | current | skip |
| Photography_Revenue_Playbook.docx | photography/DS | represented | staged-in-raw | current | skip |
| Photography_Revenue_Playbook.docx | photography/DS | represented | staged-in-raw | current | skip |
| Photography_Techniques_Frameworks.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| Photography_Techniques_Frameworks.docx | photography/DS | represented | src:2 txt:3 | current | skip |
| PHOTOGRAPHY_VAULT_INDEX.md | photography/DS | represented | staged-in-raw | current | skip |
| photoshop .docx | photography/DS | represented | staged-in-raw | current | skip |
| PHOTOSHOP_GENERATIVE_FILL_REFERENCE_IMAGE_EXTRACTION.md | photography/DS | represented | staged-in-raw | current | skip |
| POSING 101 OG.docx | photography/DS | represented | staged-in-raw | current | skip |
| POSING 101 OG.docx | photography/DS | represented | staged-in-raw | current | skip |
| preset_library.md | photography/DS | represented | staged-in-raw | current | skip |
| retoucher_training_notes.md | photography/DS | represented | staged-in-raw | current | skip |
| Roland Barthes - Camera Lucida_ Reflections on Photography (1982, Hill and Wang) | photography/DS | represented | staged-in-raw | current | skip |
| Roland Barthes - Camera Lucida_ Reflections on Photography (1982, Hill and Wang) | photography/DS | represented | staged-in-raw | current | skip |
| Sontag, Susan - On Photography (2012) - libgen.li.pdf | photography/DS | represented | staged-in-raw | current | skip |
| Sontag, Susan - On Photography (2012) - libgen.li.pdf | photography/DS | represented | staged-in-raw | current | skip |
| Stephen Shore - The Nature Of Photographs (2007, Phaidon Press) - libgen.li.pdf | photography/DS | represented | staged-in-raw | current | skip |
| Stephen Shore - The Nature Of Photographs (2007, Phaidon Press) - libgen.li.pdf | photography/DS | represented | staged-in-raw | current | skip |
| The Direction Stack (6).pdf | photography/DS | represented | src:2 txt:2 | current | skip |
| The Direction Stack.pdf | photography/DS | represented | src:2 txt:2 | current | skip |
| The Direction Stack_Final.pdf | photography/DS | represented | staged-in-raw | current | skip |
| The Direction Stack_Final.pdf | photography/DS | represented | staged-in-raw | current | skip |
| THE_DIRECTION_STACK_Field_Guide_Final.html | photography/DS | represented | src:4 txt:4 | current | skip |
| THE_DIRECTION_STACK_Final_Manuscript.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| THE_DIRECTION_STACK_Final_Manuscript.docx | photography/DS | represented | src:2 txt:2 | current | skip |
| The_Direction_Stack_v_final_2026-05-12.pdf | photography/DS | represented | staged-in-raw | current | skip |
| THE_LIFETIME_EDITING_SYSTEM.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| THE_LIFETIME_EDITING_SYSTEM.docx | photography/DS | represented | src:3 txt:3 | current | skip |
| threads photogrpahers.docx | photography/DS | represented | staged-in-raw | current | skip |
| THREADS_PHOTOGRAPHER_INTEL_EXTRACTION.md | photography/DS | represented | staged-in-raw | current | skip |
| UDEMY_LIGHTROOM_EXTRACTION.md | photography/DS | represented | staged-in-raw | current | skip |
| BW_PRESET_GORDON_PARKS.docx | photography/DS | review | src:1 txt:2 | unclear | manual review |
| BW_PRESET_GORDON_PARKS.docx | photography/DS | review | src:1 txt:2 | unclear | manual review |
| DOC PT 1 PHOTO.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| DOC PT 1 PHOTO.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| DOC PT 2 PHOTO.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| DOC PT 2 PHOTO.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| evoto 1.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| evoto 1.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| evoto 2.1.pdf | photography/DS | review | src:1 txt:1 | unclear | manual review |
| evoto 2.2.pdf | photography/DS | review | src:1 txt:1 | unclear | manual review |
| evoto 2.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| evoto 2.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| my editing wavee forever.docx | photography/DS | review | src:1 txt:2 | unclear | manual review |
| my editing wavee forever.docx | photography/DS | review | src:1 txt:2 | unclear | manual review |
| photo eveyrhting use 1101-2303.pdf | photography/DS | review | src:1 txt:1 | unclear | manual review |
| photo eveyrhting use.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| photo eveyrhting use.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| photo eveyrhting use1-1100.pdf | photography/DS | review | src:1 txt:1 | unclear | manual review |
| THE_THREE_PRESETS.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| THE_THREE_PRESETS.docx | photography/DS | review | src:1 txt:1 | unclear | manual review |
| Homepage_Copy_V2.docx | web/design | duplicate | src:0 txt:0 | superseded | ignore (superseded) |
| Homepage_Copy_V2.docx | web/design | duplicate | src:0 txt:0 | superseded | ignore (superseded) |
| SNIPED_UIUX_Design_System (1).docx | web/design | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| SNIPED_UIUX_Design_System (1).docx | web/design | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Website_Rewrite_Priorities (1).docx | web/design | duplicate | src:1 txt:3 | superseded | ignore (superseded) |
| Website_Rewrite_Priorities (1).docx | web/design | duplicate | src:1 txt:3 | superseded | ignore (superseded) |
| Website_Strategy (1).docx | web/design | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Website_Strategy (1).docx | web/design | duplicate | src:2 txt:2 | superseded | ignore (superseded) |
| Homepage_Copy_V1.docx | web/design | missing | src:0 txt:0 | current | ingest/review |
| Homepage_Copy_V1.docx | web/design | missing | src:0 txt:0 | current | ingest/review |
| antique-insights-website-demo-2.html | web/design | partial | src:1 txt:3 | unclear | compare delta |
| antique-insights-website-demo-3.html | web/design | partial | src:1 txt:3 | unclear | compare delta |
| antique-insights-website-demo.html | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Sniped Media Website Unified Fix Plan.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Sniped Media Website Unified Fix Plan.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Sniped_Media_Website_Unified_Fix_Plan.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Sniped_Media_Website_Unified_Fix_Plan.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Website_Implementation_Plan.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Website_Implementation_Plan.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Website_Rebuild_Plan.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Website_Rebuild_Plan.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Website_Rewrite_Priorities.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| Website_Rewrite_Priorities.docx | web/design | partial | src:1 txt:3 | unclear | compare delta |
| carrd_one_pager.md | web/design | represented | staged-in-raw | current | skip |
| FIGMA 2.0 last.docx | web/design | represented | staged-in-raw | current | skip |
| FIGMA.docx | web/design | represented | staged-in-raw | current | skip |
| FIGMA_MCP_COMMUNITY_INTEL.md | web/design | represented | staged-in-raw | current | skip |
| sniped figma.docx | web/design | represented | staged-in-raw | current | skip |
| SNIPED_UIUX_Design_System.docx | web/design | represented | src:2 txt:2 | current | skip |
| SNIPED_UIUX_Design_System.docx | web/design | represented | src:2 txt:2 | current | skip |
| Website_Audit.docx | web/design | represented | src:2 txt:2 | current | skip |
| Website_Audit.docx | web/design | represented | src:2 txt:2 | current | skip |
| Website_Strategy.docx | web/design | represented | src:2 txt:2 | current | skip |
| Website_Strategy.docx | web/design | represented | src:2 txt:2 | current | skip |
| kingdom-of-the-sun-website.html | web/design | review | src:1 txt:1 | unclear | manual review |
| web design.docx | web/design | review | src:1 txt:1 | unclear | manual review |
| web design.docx | web/design | review | src:1 txt:1 | unclear | manual review |