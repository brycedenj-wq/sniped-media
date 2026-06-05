# NEXT_ACTION

Top-25 book wave RUNNING (task wfz5q11c7, 12 books / 161 segments, sonnet single + haiku-shard/sonnet-consolidate).

When complete:
1. Read /tmp/top25_out/<book>.json, verify segments_read==expected, mark ledgers, flag mismatch (don't certify fails).
2. Write OS_BOOK_TOP25_CERTIFICATION_REPORT.md (per book: paths, segments, coverage, cert, doctrine, supports, contradictions, chunk-accuracy, candidates).
3. Update OS_BOOK_COVERAGE_LEDGER.csv + manifest (12 -> coverage_proven) + cert dashboard delta.
4. Chunk-accuracy audit summary + doctrine corrections + ranked candidates (curate-only, no build).
5. Recommend doctrine to reconcile.
6. LOG EXCEPTIONS (cannot certify , no extracted full text): Hit Makers (source MISSING), Trading Up (.pdf not extracted), 7 Powers (not extracted), The Trusted Advisor/Trust-Equation book (only .mobi; Maister covered instead via Managing the Professional Service Firm). These cited-doctrine sources are NOT certified.
7. STOP after Top-25 report.

NEXT MISSION after this (per operator): doctrine reconciliation , fold Top-10 + Top-25 corrections into intel_* docs, update router confidence labels, mark certified vs provisional principles, preserve disagreement (do not force one rule). NOT started.
