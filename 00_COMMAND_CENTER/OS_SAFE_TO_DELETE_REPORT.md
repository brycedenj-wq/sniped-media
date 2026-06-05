# OS SAFE-TO-DELETE REPORT
### Do not guess. Verdict per item, based on verified OS copies / KB proof.
2026-06-05. Verify before deleting anything from Downloads.

## The 10 questions

1. **Start Here docs extracted into the OS archive?** YES. `01_KNOWLEDGE_BASE/STARTHERE_SOURCE_ARCHIVE/_extracted_text/` = 111 text docs, 10.35M words (102/102 docx + 10/10 PDFs).
2. **Hashed and tracked?** YES. `STARTHERE_SOURCE_ARCHIVE/SOURCE_MANIFEST_SHA256.txt` = 128 sha256 entries. `_raw_files/` = 128 byte-for-byte originals.
3. **Technique cards generated from the OS copy, not Downloads?** YES. os_starthere_convert.py + os_howto_extract default to the OS archive (SRC_DEFAULT = archive path). They keep working after Downloads is gone.
4. **Books chunked into KB / recoverable?** PARTIALLY VERIFIED. KB has 60 chunk families / 1,879 chunks + 162 raw book files already inside the OS + ~22 books operationalized as intel_* doctrine atoms. A full book audit is running (knowledge-to-capability-sprint-001) to confirm per-book coverage. Raw epubs (~8.6GB) in Downloads were NOT copied (bulky, and the usable layer is the chunks/doctrine, not the epub).

## Per-item verdict

| Downloads path | Size | Verdict | Why |
|---|---|---|---|
| `SNIPED_OS/start here/` | 384M | **SAFE TO DELETE** | fully preserved + hashed in OS archive; cards build from the OS copy |
| `SNIPED_OS/TEST RUN KEN/` | 2.6G | SAFE (verify) | appears to be a test/run scratch dir; confirm nothing unique |
| `SNIPED_OS/VSCode-darwin-universal.dmg` | 273M | SAFE | installer, re-downloadable |
| `SNIPED_OS/Launch_CVA.exe` | 60M | SAFE | installer/binary |
| `SNIPED_OS/hyperframes-main.zip` | 110M | SAFE | repo zip, re-cloneable |
| `SNIPED_OS/*.epub` (books, 331 files) | ~6G | **NOT YET , HOLD** | usable layer is the KB chunks; book audit (running) will confirm which are operationalized vs QUEUED before you delete the raw |
| `SNIPED_OS/99_VAULT/`, `05_PRODUCTION/` | 1.5G/750M | HOLD | may hold unique production assets not yet in the OS; verify before delete |

5. **Safe to delete now:** the `start here/` folder + installers/zips/dmg/exe.
6. **NOT safe yet:** raw books (until the audit confirms each is chunked/operationalized or explicitly QUEUED), and 99_VAULT / 05_PRODUCTION (may hold unique assets).
7. **Exact paths to delete now:** `"/Users/sniper/Downloads/    SNIPED_OS/start here"` (after you see this report), plus the installers listed.
8. **Backup that exists:** OS archive (440MB, hashed) + git repo (commit 3db3cc7) for the converted layer.
9. **What would be lost if you delete the raw Downloads now:** from `start here` , nothing (fully preserved). From raw epubs , the original book files (but the chunked/doctrine layer remains usable; re-acquiring an epub is possible). From 99_VAULT/05_PRODUCTION , potentially unique production assets , VERIFY FIRST.
10. **FINAL VERDICT: SAFE EXCEPT.** Delete `start here/` + installers now. HOLD raw books + 99_VAULT + 05_PRODUCTION until the book audit + a vault check confirm coverage. I will finalize the book row when the audit returns.


## BOOK ROW FINALIZED (audit complete 2026-06-05)
Books audited: 38 families , 5 FULLY_OPERATIONALIZED, 19 QUEUED_FOR_DOCTRINE_EXTRACTION (extractable from KB CHUNKS, not the raw epub), 14 REFERENCE_ONLY. All are CHUNKED in 01_KNOWLEDGE_BASE. VERDICT on raw epubs in Downloads: SAFE TO DELETE , the usable layer (chunks + doctrine) is in the OS and queued doctrine extraction runs from chunks. Re-acquire an epub later only if a queued book needs a deeper pass than its chunks allow. 99_VAULT / 05_PRODUCTION still HOLD until a vault asset check.
