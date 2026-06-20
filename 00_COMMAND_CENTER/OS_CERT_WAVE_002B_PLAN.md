# OS CERTIFICATION WAVE 002-B+ , PLAN (metabolization scheme, no certification yet)

DOCTRINE (operator, 2026-06-19): every intentionally added source must be METABOLIZED. The remaining books are not optional long-tail. The OS is here to steal from the greats, learn from them, and condense the useful patterns into operating doctrine. Project Context Firewall still applies (not every book loads into every chat), but every book must end in one of the 7 metabolization outcomes. Do not crown the OS complete until every intentionally added source is metabolized, scheduled, rejected-with-reason, duplicate, artifact, or exception.

Plan update only. No certification this turn. The ledger (`BOOK_CANON_CERTIFICATION_LEDGER.csv`) now carries `status_v2` + `lane` + `reason` for all 297.

## Status reconciliation (297)
| status | count | meaning |
|---|---|---|
| ACTIVE_DOCTRINE_BOUND | 9 | certified in 002-A |
| DOCTRINE_EXTRACTION_SCHEDULED | 266 | assigned to a wave below, with a lane + intent |
| REFERENCE_ACTIVE_WHEN_RELEVANT | 5 | visual monographs + primary-source histories; callable per domain |
| REJECTED_AFTER_REVIEW | 0 | only set after a real read (an outcome of a wave, never pre-labeled) |
| MISCLASSIFIED_PROJECT_ARTIFACT | 14 | reclassified out (002-A) |
| DUPLICATE_OR_SUPERSEDED | 3 | collapsed |
The retired statuses (CERTIFY_NOW / CERTIFY_LATER_SCHEDULED / ACTIVE_REFERENCE_PROVISIONAL / REFERENCE_ONLY_NOT_ACTIVE) are mapped forward. No "optional/someday" status remains.

## The 9 doctrine lanes , what the OS steals, and counts
(counts = scheduled for extraction; bound = already certified; ref = reference-active)

| lane | books | what the OS extracts |
|---|---|---|
| business | 126 sched, 6 bound, 3 ref | the commercial spine: pricing, positioning, offers, sales flow, capital allocation, operator playbooks. (Over-broad catch-all; sub-split as books are read.) |
| taste_culture | 42 sched | aesthetic judgment, cultural literacy, creative process, the taste engine behind direction calls |
| operations | 31 sched, 1 bound | systems thinking, process design, operator discipline, run-the-machine patterns |
| psychology | 24 sched | decision-making, persuasion, behavioral patterns, founder psychology, self-management |
| power | 17 sched | leverage, status games, maneuver/strategy (Greene, war/history), negotiation doctrine |
| luxury_status | 12 sched | status signaling, premium-as-insurance, hospitality, analog-premium moat |
| ai_automation | 8 sched | tool routing, prompt patterns, automation blueprints, production-efficiency layer |
| photography | 3 sched, 2 bound, 2 ref | composition, lighting, vision (text-craft) + the photo monographs (visual route) |
| creator_economy | 3 sched | content distribution, audience building, one-person-business growth engine |

## Certification wave schedule (by load-bearing importance)
Every scheduled book has a wave. Run each wave as the proven 002-A harness: extract -> fan-out reader-per-book whole-read + segment ledger -> adversarial verify -> reconcile. Batches of ~8-10 (002-A hit transient rate-limits at 9 concurrent; smaller batches + resume).

- **002-A , DONE (9):** the Top-10 cited (business/psychology/photo). ACTIVE_DOCTRINE_BOUND.
- **002-B , NEXT (~34 core):** the highest load-bearing Top-25-tier cited across business + psychology + luxury_status + operations (Pricing Creativity, Influence, Pre-Suasion, Breakthrough Advertising, Contagious, $100M Leads/Money Models, Thinking in Systems, Poor Charlie's, Predictably Irrational, Laws of Human Nature, Status Anxiety, Elephant in the Brain, Unreasonable Hospitality, Blockbusters, Revenge of Analog, Perennial Seller, Company of One, The Trusted Advisor, Crossing the Chasm, the Greene power set). The commercial + influence + status spine.
- **002-C , business remainder (~92):** the rest of the business lane, sub-split into real sublanes as read (pricing / positioning / sales / capital / operator-bios). Founder bios (Titan, Snowball, Sam Walton, Shoe Dog, Elon Musk, Steve Jobs) extract OPERATOR PATTERNS here, not rejected (steal from the greats).
- **002-D , power + remaining psychology + luxury_status (~40):** maneuver doctrine + behavioral + status moat.
- **002-E , operations + ai_automation + creator_economy (~42):** run-the-machine + production-efficiency + growth.
- **002-F , taste_culture (~42):** the taste engine; some route partly visual.
- **002-G , photography (~3 text + monographs):** craft text-cert; monographs via the External Visual Proof Gate.
- **REFERENCE_ACTIVE (5):** logged now, not a numbered cert wave; visual monographs go through the External Visual Proof Gate when a visual task calls them; primary-source histories callable per domain.

## Cost / time reality (honest)
This is a large, deliberate commitment, not a quick pass. 266 books whole-read + verified. 002-A was ~376k words / ~3.1M subagent tokens for 9 books + verifiers. Extrapolated: the full 266 is on the order of **80-120M subagent tokens** across ~6-8 waves, many hours of wall time with resumes. The operator has accepted this as intentional (metabolize the canon). Mitigations: batch 8-10, resume-on-limit (cached agents free), exclude duplicates, route visual/scanned correctly so no wasted reads.

## Visual / OCR / audio exceptions
- Visual (External Visual Proof Gate): Avedon + the portraiture art-education pdf + any photo monograph surfaced in 002-G. Ways of Seeing triaged.
- OCR/scanned: Poor Charlie's 184MB pdf (use epub, pdf is DUPLICATE), Predictably Irrational djvu (use epub). Any pdf extracting to near-zero words -> OCR triage, not force-read.
- Audio: none.

## State files that update ONLY after per-book verification
Per certified book (verifier returns whole-read): `OS_ENGAGEMENT_MANIFEST.csv` (status -> coverage_proven), `OS_BOOK_SOURCE_INDEX.csv` (certified_wave00X), `BOOK_CANON_CERTIFICATION_LEDGER.csv/.md` (status_v2 -> ACTIVE_DOCTRINE_BOUND), per-wave `WAVE_00X_SEGMENT_LEDGERS.json`, dashboard via `os_checkpoint.py --write`, per-wave `OS_RECEIPT.md`, `NEXT_ACTION.md` + memory. A book that a wave finds empty -> REJECTED_AFTER_REVIEW with reason (not silently dropped). Router binding stays rule-8 gated (bind only if it changes operating behavior).

## Completion rule (anti-false-crown)
The OS is NOT complete until every one of the 297 is ACTIVE_DOCTRINE_BOUND, REFERENCE_ACTIVE_WHEN_RELEVANT, REJECTED_AFTER_REVIEW (with reason), MISCLASSIFIED_PROJECT_ARTIFACT, DUPLICATE_OR_SUPERSEDED, or EXCEPTION. DOCTRINE_EXTRACTION_SCHEDULED is an in-progress state, not a terminal one; while any book sits there, the canon is not metabolized.

## DECISIONS for your go
1. Confirm the lane map + wave order (business-heavy catch-all sub-splits as read).
2. Confirm 002-B core (~34) as the next batch, or re-rank.
3. Batch size (default 8-10) and pace (run 002-B now on go, or schedule the whole 002-C..G as a standing routine).

No certification yet. Awaiting go.
