# HIGH_LEVEL_CONVOS extraction log · curated operator-conversation transcripts · 2026-05-24

## Source (1 of 1 · single staged source)

| Field | Value |
|---|---|
| Title | high level convos (collected transcripts) |
| Repo path | `raw/07_CONTENT/high_level_convos.docx` (staged in commit `c815461`) |
| Format | docx (Word 2007+) |
| Method | pandoc to plain text |
| Output | `01_KNOWLEDGE_BASE/batches/high_level_convos_extracted/high_level_convos.txt` |
| Yield | 684,626 words · 3,796,616 chars · 102,682 lines |
| OCR | none |
| New dependencies | none |

## Process

1. `scripts/extract_high_level_convos.py` converted the staged docx to plain text via pandoc. Reads from `raw/` only; the original is not modified. Refuses to overwrite an existing extracted file.
2. The document is a collection of ~20+ podcast/video transcripts (timestamped) from a dominant source, **Earn Your Leisure (EYL)**, plus a **Miss Pinky** investment-basics intro and a music-industry / creator-equity segment.
3. No other source was extracted. The Bible (`The-Holy-Bible-King-James-Version.pdf`) was NOT touched, staged, or extracted; no other `raw/07_CONTENT/` file was used.

## Transcript map (used to ground curated, attributed chunks)

- **Miss Pinky · investment basics:** equity = ownership, valuation, cap tables, dilution.
- **Earn Your Leisure · club owner (Mark Barnes · Dream/Park, DC nightlife):** 32%-interest launch financing, parking/coat-check cash lines, corporate-event margins, membership model, hospitality/ambiance, crowd economics, succession, Black entrepreneurship.
- **Earn Your Leisure · AI Future Shock:** AI and the future of work/skills.
- **Earn Your Leisure · Malka/OWN (Jeff Fromer):** distribution flywheel, shared ownership / creator option pool, exit terms + due diligence ("founders hide the truth"), get-cash-upfront, creators-and-equity playbook, AI-era trust moats, virtual-influencer ethics, creator marketplace, pricing/audience fit, negotiation, ownership mindset.
- **Earn Your Leisure · multiple income streams (Rashad/Ian/Troy):** network leverage + reinvestment, layered income (business to long-term investment to speculation), frugality + execution speed.

## Curation discipline

- Stripped timestamps, filler, host banter, and ad-reads.
- **Deferred/excluded (0 chunks):** fringe-esoteric asides (e.g., "emerald tablets") and any personal spiritual-journey narrative (the no-faith-lane guardrail; the Christian-hip-hop artist's faith content was NOT chunked as doctrine). The Bible is excluded entirely.
- Curated principle extraction, NOT exhaustive transcript chunking.

## Deviations

None. Single staged source as planned. No OCR, no new dependency, no master-file change, no raw modification.
