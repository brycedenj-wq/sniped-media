# MEDIA_BUSINESS_RECOVERY extraction log · recovered media-business institutions · 2026-05-24

## Sources (2 of 2 recovered · 0 failures)

| # | Title | Author | Recovered format | Extraction | Words | Output |
|---|---|---|---|---|--:|---|
| 1 | Hit Men: Power Brokers and Fast Money Inside the Music Business | Fredric Dannen | azw3 (`_RECOVERED`) | ebook-convert | 152,952 | `hit_men_dannen.txt` |
| 2 | The Mailroom: Hollywood History from the Bottom Up | David Rensin | epub (`_RECOVERED`) | ebook-convert | 169,850 | `the_mailroom_rensin.txt` |

Total ~322,802 words. Method: ebook-convert (calibre), pre-existing on PATH. **No OCR. No new dependencies.**

## Process

1. `scripts/extract_media_business_recovery.py` read the 2 `_RECOVERED` files from `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` (read-only · originals unmodified) and wrote normalized `.txt` to `media_business_recovery_extracted/`. Refuses to overwrite.
2. **Used the `_RECOVERED` files only.** The old scanned Hit Men PDF (0 extractable words) and the old Mailroom djvu (unsupported · no djvutxt) contributed 0.
3. No other memoirs_biographies file, no recovery item outside these 2, no CURRENT_IDENTITY source, and no already-canonical batch source was touched. The Bible was NOT touched/staged/extracted.

## Coverage map (used to ground curated, attributed chunks)

- **Hit Men (Dannen):** Top 40 airplay as the superstardom chokepoint; the Network (independent promotion · payola's successor · mob ties); fast money + artist exploitation (the dark side); indie-promotion economics ("right to the bottom line"); the power brokers (Yetnikoff/Geffen/Azoff); manager-to-label-boss (control the institution); the 1979 crash + the hype/returns machine.
- **The Mailroom (Rensin):** learn it from the absolute bottom up (the mailroom crucible); information is king (read everything); relationships/access as the agency's real asset; the trainee ethos (take care of it · find a mentor); the say-yes / glad-handing service culture; earn the desk by becoming indispensable.

## Deviations

None. 2 recovered sources as planned. No OCR, no new dependency, no master-file change, no raw modification. Bible excluded. (Note: the closing synthesis chunk was regenerated once during chunk authoring so it also carries the CURRENT_OPERATOR_REALITY_BRIEF reference + optionality guardrail tail · all 15 chunks now carry both.)
