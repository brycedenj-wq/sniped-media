# FOUNDER_FASHION_RECOVERY extraction log · 2026-05-24

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `grace_a_memoir_coddington.txt` | Grace: A Memoir | Grace Coddington | epub (recovered) | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Grace Coddington - Grace_ A Memoir (2012, Random House) - libgen.li_RECOVERED.epub` | 82,007 |
| `total_recall_schwarzenegger.txt` | Total Recall: My Unbelievably True Life Story | Arnold Schwarzenegger | epub (recovered) | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Schwarzenegger, Arnold - Total Recall- My Unbelievably True Life Story (2012, Simon & Schuster) - libgen.li_RECOVERED.epub` | 242,002 |

## Method

- **Tool:** `ebook-convert` (calibre · already on PATH). EPUB to plain .txt.
- **No OCR. No new dependencies.** No pip install. Both source `.epub` files were read-only (not modified).
- **Output:** `01_KNOWLEDGE_BASE/batches/founder_fashion_recovery_extracted/` (2 .txt · 324,009 words total).
- **Script:** `scripts/extract_founder_fashion_recovery.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded (0 chunks · 0 extraction)

- **Old Grace 0-byte stub** (`Coddington, Grace - Grace_ A Memoir (2012, Random House Publishing Group) - libgen.li.epub`): 0 bytes. NOT extracted. Left in place untouched.
- **Old Total Recall 0-byte stub** (`Petre, Peter_Schwarzenegger, Arnold - Total recall_ ... - libgen.li.epub`): 0 bytes. NOT extracted. Left in place untouched.
- **Grant + Washington (Chernow):** present in the same memoirs_biographies folder but DEFERRED to the separate historical-biography lane · NOT extracted here.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked.
- **Every other memoirs_biographies / already-canonical source:** NOT extracted (single curated 2-source lane).

## Note (Grace file size)

The Grace `_RECOVERED.epub` is ~103 MB because it embeds the memoir's photography/illustrations; the extracted prose is a normal ~82,007-word memoir. The image weight does not affect text extraction.

## Result

- Sources in: 2 · extracted out: 2 · failures: 0.
- Ready for chunking (completed in the same ship · see `FOUNDER_FASHION_RECOVERY_COMPLETE.md`).
