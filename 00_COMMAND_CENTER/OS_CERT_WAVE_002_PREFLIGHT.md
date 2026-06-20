# OS CERTIFICATION WAVE 002 · PREFLIGHT (plan only, nothing certified)

Mission: certify / terminally disposition the 297 `provisional_chunked_not_certified` source rows, the real remaining completeness gap (the finite unresolved pile is closed, but these 297 were chunked, not whole-read + segment-ledger proven). PREFLIGHT ONLY. Nothing marked verified. No rewrite/delete/move/generate/spend/post/crown. Read-only analysis of the manifest (the arbiter).

Date: 2026-06-19. Source of truth: `OS_ENGAGEMENT_MANIFEST.csv`, `OS_BOOK_SOURCE_INDEX.csv`, `OS_BOOK_TARGETED_CERTIFICATION_QUEUE.md`.

---

## 1. COUNT RECONCILIATION (exact, matches the checkpoint)

class=source universe = 1260:
- 953 read_verified
- **297 provisional_chunked_not_certified**  ← Wave 002 target
- 5 coverage_proven_via_starthere
- 3 duplicate
- 1 exception_corrupt_source
- 1 exception_missing_source

953 + 297 + 5 + 3 + 1 + 1 = 1260. Confirmed.
(There are 374 provisional rows across ALL classes; the other 77 are non-source derivatives/mirrors, OUT of scope. Wave 002 = the 297 source rows only.)

## 2. WHAT THE 297 ACTUALLY ARE (decisive finding)

All 297 are documents with no extracted wordcount (binary formats), not text rows. Breakdown:
- By format: 136 epub, 119 pdf, 25 mobi, 10 azw3, 6 djvu, 1 doc.
- By location: 282 in the `~/Downloads/    SNIPED_OS` book library, 14 misclassified project artifacts, 1 stray (`raw/02_TIER_1_CANON_BOOKS/ai_tech`).
- Duplicates: 0 md5 dupes within the 297; 0 whose md5 matches an already-verified source. So no free promote-by-dedup wins.

So Wave 002 is fundamentally a BOOK-CERTIFICATION wave (whole-read + segment ledger), plus a small reclassification cleanup.

## 3. CLASSIFICATION (duplicates / promoted / dead / needs-read)

- **MISCLASSIFIED PROJECT ARTIFACTS (14): not external books, do NOT certify as doctrine.** These are our own Kingdom of the Sun deliverables and dossiers: `sample_dossier_v1`, `KOTS_2026_Refresh_Concept_v1/v2`, `Kingdom_Food_Play`, `Kingdom_Revenue_Share_Proposal`, `Kingdom_Media_Fee_Model`, `Vanguard_School_Commitment`, `Kingdom_Final_Six_Strategy`, `Kingdom_Sponsor_Packet`, `Vanguard_Season_Social_Playbook`, `Vanguard_Booster_Club_Framework`, `Kingdom_Media_Money_Model`, `How_To_Get_Sponsors_Coach_Jones`, `0_START_HERE_Coach_Jones`. Disposition: RECLASSIFY out of class=source (they are project outputs, class=derivative/build artifact). Closes 14 rows with zero reading.
- **ALREADY-PROMOTED / LOAD-BEARING (the certify-first set):** `OS_BOOK_SOURCE_INDEX.csv` flags 64 books as `cited_by_doctrine` (the OS actually leans on these). These are the real certification targets. The 2026-06-04 queue already ranks them: Top 10 (~68 segments) then Top 25.
- **VISUAL-REVIEW BOOKS (~14): not text-cert.** Eggleston's Guide, Avedon In the American West, Ernst Haas, Virgil Abloh, and the visual_art_photo_book set carry meaning in images. These route through a VISUAL pass and trigger the External Visual Proof Gate (`_standards/OS_EXTERNAL_VISUAL_PROOF_GATE.md`), not a text ledger.
- **OCR-FIRST (~10-15): scanned photo/lighting/composition canon** (the 6 djvu + scanned photo pdfs). OCR, then text-cert. Do NOT OCR the whole pdf pile, only the visual-lane canon the OS uses.
- **LONG-TAIL, LEAVE PROVISIONAL (~200+): do NOT certify.** Uncited founder bios (Titan, Shoe Dog, Snowball, etc.), histories, literary canon, uncited finance classics. The OS does not lean on them. Per the existing cost-discipline rule, whole-reading these is the banned 21M-word path.

## 4. THE SCOPE DECISION (the one thing to resolve before execution)

The literal mission "certify all 297" collides with the OS's own locked cost-discipline (`OS_BOOK_TARGETED_CERTIFICATION_QUEUE.md`): certify only the ~25-65 load-bearing books, leave the long tail provisional-but-labeled, never bulk-read 21M words.

Recommended reframe (closes the gap honestly without the banned bulk-read): every one of the 297 reaches a TERMINAL disposition, where "terminal" = one of:
1. CERTIFIED (segment ledger + whole-read / visual / OCR) , the cited/load-bearing + visual + OCR-photo subset.
2. RECLASSIFIED OUT , the 14 project artifacts.
3. LEAVE-PROVISIONAL-REFERENCE-ONLY (a logged DECISION, labeled, not an open gap) , the uncited long tail.

Under this reframe the 297 unresolved goes to 0 by disposition, and the OS stops claiming false completeness, without reading 21M words. This needs your call: full-certify-297 (expensive, contradicts cost discipline) vs terminal-disposition-297 (recommended).

## 5. ESTIMATED WORK

- Reclassify 14 artifacts: trivial, manifest edit, no reading.
- Certify Top 10 cited: ~68 segments, one bounded workflow wave (the queue's estimate).
- Certify Top 25 cited (rest of the 64): a second bounded wave, ~150 more segments.
- Visual-review ~14: per-book visual pass + External Visual Proof Gate, not text segments.
- OCR ~10-15 photo books: per-item OCR then ledger.
- Long-tail ~200+: zero reading, one logged disposition decision (delta-read only on demand).

## 6. HARNESS PLAN (how Wave 002 executes, on your go)

- LANE 0 · Manifest hygiene: reclassify the 14 artifacts + the 1 stray. No reading. (closes ~15)
- LANE A · Text-cert cited books (Top 10 then Top 25): fan-out WORKFLOW, one reader agent per book, whole-read (no sampling), each emits a SEGMENT LEDGER; then an adversarial-verify phase (fresh-context: prove whole-coverage, not sampling) before any status flip; bind each certified book to the `intel_*`/doctrine it backs (cited_by_doctrine map). Bounded wave, Top 10 as the pilot.
- LANE B · Visual-review books (~14): package page/plate strips, route to the External Visual Proof Gate (operator/ChatGPT/Gemini), record verdict; never a text ledger.
- LANE C · OCR photo canon (~10-15): OCR pass, then fold into LANE A text-cert.
- LANE D · Long-tail disposition: one logged decision marking ~200+ as leave-provisional-reference-only (labeled), not certified. Delta-read a single book only when a task depends on it.
- Every lane: status flips to `coverage_proven` ONLY after ledger + adversarial verify pass; dashboard/manifest reconciled from the manifest; OS_RECEIPT per wave.

Failure-mode defenses: laziness (count segments-done vs total per book), self-preferential bias (separate verify agent, never self-crown), goal drift (re-read the leave-provisional rule each wave so the long tail is never bulk-read).

## 7. RECOMMENDED WAVE 002 SEQUENCE
1. LANE 0 (reclassify 14 artifacts) , instant, removes false "book" rows.
2. LANE A pilot: Top 10 cited books , proves the fan-out cert pipeline end to end.
3. LANE A wave 2: rest of the 64 cited + LANE C OCR photo books.
4. LANE B: visual-review books through the External Visual Proof Gate.
5. LANE D: log the long-tail leave-provisional disposition.

STOP. Awaiting operator go. Nothing certified, nothing reclassified, nothing mutated yet.
