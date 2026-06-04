# OS FULL-BURN PLAN (controlled)

Method: preserve everything, verify everything, read before judging, distill before deciding, do not blow up the Mac. Nothing is deleted, ever. Importance is never decided under 50% coverage.

## 1. VERIFIED CORPUS COUNT (hash-proven, 2026-06-03)

| Bucket | Count | Note |
|---|---|---|
| Total doc files | 3,855 | md/txt/docx/pdf/epub/mobi/azw3/djvu/rtf/jsonl across 3 roots |
| Unique content hashes | 2,669 | the real distinct-content number |
| **TRUE UNIQUE SOURCES** | **1,617** | **862 text (3.94M words) + 755 books (~3.6GB)** |
| Mirror (raw/ = Downloads copy) | 673 | preserved, not read twice |
| Derivative (chunks/extracts/index) | 1,388 | generated from sources, skip |
| Old export (chat json/md) | 74 | preserved, read as source-class where unique |
| Exact duplicate | 59 | preserved |
| Build artifact | 39 | node_modules etc |
| Backup | 5 | .bak/.prev |
| Unknown | 0 | none unclassifiable |

The "1,216 books" was inflated by mirrors + dupes. Real = **755 books.**

## 2. MAC STORAGE + SAFETY GATE

- Disk: 460GB, **41GB free, 91% full.** Tight. No giant duplicate files. Doctrine output is KB-scale, safe.
- `.git` = **4.4GB** of book objects committed before the ignore rules (violates rule 14). Reclaimable by history clean.
- `raw/` = **4.5GB**, a hash-identical mirror of the Downloads corpus. Redundant on the hot disk.
- 49 files >100MB, 16 videos, 1.2GB photo/video folder.

**Safely archivable/offloadable (preserve, never delete), reclaims ~8-12GB:**
1. `raw/` mirror → compress to a single archive or offload (it is a verified hash-copy; the Downloads corpus is the canonical).
2. `.git` book history → run a history clean (git filter-repo) to drop committed books; reclaims ~4GB AND fixes rule 14.
3. The 1.2GB books/videos folder + 49 large files → offload to external/cloud; they are sources, kept, just not needed on hot disk to read text.
Recommendation only. Nothing runs without your go.

## 3. COST / LOAD GATE (the "do I need to add money" answer)

Estimated processing tokens to fully engage:
- Text layer (3.94M words): ~5.3M read-tokens + distill. 
- Book layer (755 books ≈ 60M words): ~80M read-tokens + distill. The expensive part.

**The lever: model-tiering.** Cheap model (Haiku) does the high-volume WHOLE-READS; a stronger model (Sonnet/Opus) does the DISTILL + consolidation. This cuts the book layer roughly 5 to 10x.

| Layer | Tiered (Haiku read / Sonnet distill) | All-Opus |
|---|---|---|
| Text layer (862 docs) | ~$40 to $80 | ~$120 |
| Book layer (755 books) | ~$200 to $450 | ~$1,500 to $2,500 |
| **Full engagement** | **~$250 to $530** | ~$1,700 to $2,700 |

Each batch logs its estimate before it runs. **Recommendation: tiered full-burn.** A few hundred dollars engages the entire OS, likely no account top-up needed for the text layer; decide on the book layer after seeing text-layer value.

## 4. BATCH ORDER

1. **Phase 1, TEXT LAYER** (862 docs, ~25 to 30 batches of ~30). Cheap, strategy-bearing, runs now.
2. **Phase 2, CANON VERIFY** (~25 to 30 already-summarized canon books, whole-read to verify the memory distillations against real reads). 1 to 2 batches.
3. **Phase 3, BOOK LAYER** (755 books in waves, segmented + coverage-proven, Haiku-read, budget-gated per wave).

Sequencing is throughput, never importance. No doc is skipped. No doc is judged useless under 50 to 75% coverage.

## 5. EXPECTED TIME

- Text layer: a handful of hours of run time across ~25 to 30 batches (back to back, concurrency-capped).
- Book layer: a multi-day paced campaign (segmented reads, each book proven).

## 6. DASHBOARD FIELDS (updated set)

total docs · unique hashes · true sources · text vs books · mirrors/derivatives/dupes/exports/backups · docs fully read · partially read (preview only) · not read · % engaged (by docs AND by words) · doctrines created · skills extracted · gaps found · contradictions flagged · storage before/after · est. + actual token cost per batch · next-in-queue · what-done-means progress.

## 7. FIRST 3 BATCHES

- **Batch 002:** next ~30 unread TEXT sources (00_BRIEF remainder, command-center, future_sources).
- **Batch 003:** ~30 unread TEXT sources (brand/strategy/transcript md, chat-derived sources).
- **Batch 004:** ~30 unread TEXT sources (continue the text layer sweep).

## 8. WHAT "DONE" MEANS

- 100% of 862 text sources whole-read + distilled + journaled, coverage proven.
- 100% of 755 books segment-read with coverage proof + distilled.
- Master OS doctrine assembled from all distillations, loadable by default.
- Every contradiction surfaced and reconciled or flagged.
- Dashboard shows ~100% engaged with per-doc proof.
- ONLY THEN do major strategy questions get the full-OS treatment, possibilities across every lane, proof picks the throne.

## 9. THE 14 RULES (in force)
Recount honestly · hash-separate sources · no-delete manifest · whole-read sources · segment long docs with coverage proof · distill every source · extract skills · journal deltas · master doctrine only after enough engaged · track token/cost/load pre-run · track storage per batch · no giant duplicate files · preserve raw sources · protect git (only doctrine/skills/manifests/dashboards/maps committed, never books/videos/node_modules/raw PDFs/caches).
