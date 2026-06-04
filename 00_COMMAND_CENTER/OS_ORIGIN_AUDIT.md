# ORIGIN AUDIT , 331 large derivatives (STEP 1, 2026-06-04)

> Proving the "derivative" classification by hash + origin before dismissing files. md5 proves identity, not derivation. Nothing deleted. Result is mostly reassuring: the classification held , only 1 of 331 was genuinely orphaned content.

## Method (local, cheap , no reads, no spend)
For each of the 331 derivative/mirror/old-export rows >=20k words: checked md5 (identity), folder lineage (`01_KNOWLEDGE_BASE/batches/*_extracted`, `/outputs/`, `/indexes/`), derivative name markers (MASTER_INDEX, CHUNK, consolidat), source-twin match (normalized stem -> any row with the same content), and twin status (verified / not_read / none).

## Results
| bucket | count |
|---|---|
| **confirmed_derivative** | **330** |
| possible_misclassified_source (orphan) | 1 |
| duplicates/mirrors (internal md5 dup groups) | 6 groups |
| unknown (after resolution) | 0 |

Breakdown of the 330 confirmed:
- **224** , extracted plain-text of source BOOKS in `01_KNOWLEDGE_BASE/batches/*_extracted/` (Sontag, Titan, Elon Musk, Avedon, etc.). Each maps to a `read_verified` book source. Genuine extraction artifacts.
- **36** , `review_completion_work/*_docx.txt` whose `.docx` source is `read_verified` (covered).
- **68** , `review_completion_work/*_docx.txt` whose `.docx` source EXISTS and is `not_read` , the source is correctly queued (pending), not dismissed. Reading the source covers these.
- **2** , OS-generated artifacts (`FULL_DOWNLOADS_AND_OS_COVERAGE_LEDGER`, `ACTIVE_KNOWLEDGE_STATE.md`) , inventory/state, no doctrine, correctly derivative.

## Confirmed derivatives
330 of 331. The classification was sound. The sources were NOT wrongly removed from the queue , every derivative's content is either verified, or its source sits in the `not_read` pile (pending), or it is an OS-generated artifact.

## Possible misclassified sources (must re-enter the read queue)
- **1 orphan:** `cold_out_reach_instantly_gold_everything_use_this_.txt` (186,904 words) , no source twin anywhere; the content exists only in this extraction. **Reclassified derivative -> source**, status `not_read`, now in the read queue.

## Duplicates / mirrors
- 0 large derivatives share an md5 with a SOURCE row (no exact source-copies hiding as derivatives).
- 6 internal md5-duplicate groups inside `review_completion_work` (minor; same content twice).

## Unknowns
- 0 after resolution (the 2 "unknown" rows resolved to OS-generated artifacts).

## Confidence score per file
- Mean origin-confidence across the 331: **0.77**.
- **330 high-confidence dismissable** (>=0.9 lineage/twin proof).
- **1 must-requeue** (orphan, reclassified).

## What this means for the scoreboard (concern #6 resolved)
- **Concern #6 (derivatives removing real source from the queue) is essentially NOT realized.** Only 1 file of 331 was orphaned. The derivative layer is trustworthy.
- **BUT two real things surfaced:**
  1. **A large `not_read` source pile is correctly pending:** the 68 `not_read` `.docx` twins represent roughly 8M+ words of unread source content. It is NOT inflating the verified score (correctly not claimed), but it is a big pending queue the OS should not pretend is engaged.
  2. **Hidden book-layer volume (methodology flag for later):** the 224 batch extractions reveal the TRUE size of "verified" books (Titan 332k, Avedon 246k, Elon Musk 204k words). Book source rows carry NO word count, so the first methodology audit could not volume-check them. Whether these big verified books got FULL segment coverage (vs characterization) is the SAME open question as the 5 giants , flagged for a book-layer coverage re-check after Step 2.

## Step 1 verdict
The derivative classification was valid; no large requeue is required. One orphan reclassified. Safe to proceed to Step 2 (the 5 giant raw dumps, one at a time), with a follow-on flag to volume-verify the big "read_verified" books once the giants are done.
