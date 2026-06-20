# OS CERTIFICATION WAVE 002-C , PLAN (Sonnet, no certification yet)

State truth (post 002-B): 39 ACTIVE_DOCTRINE_BOUND, 233 DOCTRINE_EXTRACTION_SCHEDULED, 5 REFERENCE_ACTIVE (terminal), 14 artifacts, 6 duplicates, 297 reconcile, checkpoint CLEAN, OS NOT complete. Plan only, then wait for go.

Model routing: Sonnet for reader/synthesis/verify (Opus reserved for contradiction resolution). Haiku/Bash for extraction + reconciliation. Adaptive parallel batching toward 30-60 concurrent, back off on rate limits, big books split into <=80k-word reader units.

## 002-C scope: the operating-spine remainder (psychology + power + luxury_status + creator_economy)
The giant business lane (113) is deferred to 002-D so 002-C stays bounded and high-leverage. 002-C = 41 candidate rows in these 4 lanes, all on disk.

### Lane-0 hygiene first (no reading, deterministic)
- 13 MISSING paths -> EXCEPTION (missing source). These are stubs/worksheets not on disk: 6 ai_automation "Prompt Template" files, 4 business, 3 operations. (None are in the 002-C lanes.)
- 2 intra-candidate DUPLICATES collapse -> DUPLICATE_OR_SUPERSEDED: "Made to Stick" (2 pdf copies) and "Building a StoryBrand" (mobi + epub). Keep one each.
- Net 002-C certify target = 41 - 2 dups = 39 unique books.

### Exact 002-C source list (39 unique, by lane)
PSYCHOLOGY (17): Elon Musk (Isaacson, cited), Thinking Fast and Slow (Kahneman), Alchemy (Sutherland), The Choice Factory (Shotton), Cashvertising (Whitman), Positioning (Ries/Kotler), The Coddling of the American Mind (Lukianoff/Haidt), The Crowd (Le Bon), Creativity/Flow (Csikszentmihalyi, djvu), Man's Search for Meaning (Frankl), Onward (Schultz), Grinding It Out (Kroc), Total Recall (Schwarzenegger), Tribes (Godin), Live From New York (Shales/Miller), Hello My Name Is Awesome (Watkins), + 1 Kauffman entrepreneurship title.
POWER (13): Napoleon (cited), Alexander the Great (Freeman, cited), Washington: A Life (Chernow), Working Backwards (Bryar/Carr), DisneyWar (Stewart), The Art of War (pdf), Pour Your Heart Into It (Schultz), Combo Prospecting (Hughes), The Prince (Machiavelli), The Adweek Copywriting Handbook, Security Analysis (Graham/Dodd), Hit Men (Dannen), + 1 Dover history title.
LUXURY_STATUS (9): Deluxe (Dana Thomas), The Luxury Strategy (Kapferer/Bastien), The Status Game (Storr), Building a StoryBrand (Miller, keep 1), Trading Up (Silverstein/Fiske), Brand Naming (Meyerson), The Brand Gap (Neumeier), The Great Online Game (Not Boring).
CREATOR_ECONOMY (2->1): Made to Stick (Heath, keep 1).

## Batch split (Sonnet, parallel)
- Extract-triage all 39 first (ebook-convert/pdftotext); verify wordcounts; any pdf that extracts to near-zero -> OCR (tesseract/ocrmypdf) or EXCEPTION if illegible. Split any book >100k words into <=80k-word reader units (likely: Elon Musk ~206k, Washington, Thinking Fast and Slow ~175k, Security Analysis, Napoleon, Total Recall, Alexander).
- Run as ~6 Sonnet batches of ~6-7 books (proven-stable ~18-agent shape), and run 2-3 batches IN PARALLEL to reach 30-60 concurrent (Sonnet sustained this where Opus did not). Back off 25-40% on rate limits; resume failed-only; never duplicate completed reads.
- Each book: reader(s) whole-read + segment ledger -> synthesis 5-field doctrine -> independent adversarial verify. A book is done only with full part coverage + 5-field record + whole-read verdict.

## Expected count movement (if all 39 extract clean)
- 13 missing -> EXCEPTION: scheduled 233 -> 220; EXCEPTION 0 -> 13.
- 2 dups -> DUPLICATE: scheduled 220 -> 218; DUPLICATE 6 -> 8.
- 39 certified -> ACTIVE_DOCTRINE_BOUND: scheduled 218 -> 179; BOUND 39 -> 78.
- After 002-C: BOUND 78, SCHEDULED 179, REFERENCE 5, ARTIFACT 14, DUPLICATE 8, EXCEPTION 13 = 297. Checkpoint reconciled only after verification.
- Honest caveat: any scanned pdf in the 16 pdf/djvu that fails text extraction reduces the certified count for this wave (deferred to OCR or marked EXCEPTION), and is reported, not hidden.

## Risks
- OCR (16 pdf/djvu in the 39): likely-scanned candidates to watch = ArtOfWar.pdf, The Prince, Security Analysis, The Crowd (Le Bon), the Dover history, Creativity (djvu). Triage decides text-cert vs OCR vs EXCEPTION.
- DUPLICATES: 2 (Made to Stick, Building a StoryBrand) collapse pre-cert.
- MISSING: 13 (other lanes) -> EXCEPTION in Lane-0.
- VISUAL: none in 002-C (the lone visual-title flag, Purple Cow, is in the business lane / 002-D).
- LARGE-SPLIT needed: ~6-7 books >100k words; must split or a part drops silently (the 002-B lesson).

## Remaining runway after 002-C
002-D = business (113), 002-E = taste_culture (39), 002-F = operations (30) + ai_automation (2 after missing) , 002-G = photography (2). REFERENCE_ACTIVE visual (5) stay terminal, on-demand. OS complete only when SCHEDULED hits 0.

## Decisions for go
1. Confirm 002-C = the 39 operating-spine books (or fold in more lanes).
2. Confirm Lane-0 (13 missing -> EXCEPTION, 2 dups -> DUPLICATE) runs first.
3. Confirm parallel-Sonnet batching (2-3 concurrent batches).

No certification yet. Awaiting go.
