# HIGH_LEVEL_CONVOS source index · 2026-05-24

batch_id `HIGH_LEVEL_CONVOS` · 25 chunks · 1 source file (`high_level_convos.txt`) · per-transcript/guest attribution in `source_title` + `author` · NO new domain.

## Source + attribution

Single source_file: `high_level_convos.txt` (from `raw/07_CONTENT/high_level_convos.docx`). Per-transcript attribution (author):

| Attribution (author) | Transcript | Chunks |
|---|---|---:|
| Miss Pinky | investment basics | 2 |
| Mark Barnes (Earn Your Leisure) | club owner · Dream/Park, DC nightlife | 8 |
| Jeff Fromer (Earn Your Leisure) | Malka/OWN creator-equity | 10 |
| Rashad, Ian, Troy (Earn Your Leisure) | multiple income streams | 2 |
| Earn Your Leisure | AI Future Shock | 1 |
| Earn Your Leisure (collected) / SNIPED synthesis | cross-conversation synthesis | 2 |

## Chunk map

| chunk_id | domain | concept |
|---|---|---|
| 001 | capital | Equity is ownership; giving it away trades control for capital (Miss Pinky) |
| 002 | commercial-architecture | Valuation and the cap table (Miss Pinky) |
| 003 | capital | Get cash upfront: a headline exit can net nothing (Fromer) |
| 004 | operator-doctrine | Find mentors who have already been through it (Fromer) |
| 005 | capital | Layer income: business, then long-term investment, then speculative bets (EYL panel) |
| 006 | operator-doctrine | Frugality and execution speed compound (EYL panel) |
| 007 | capital | High-cost capital to seize an opportunity, with the risk named (Barnes) |
| 008 | operator-process | Own the ancillary cash lines: parking and coat check (Barnes) |
| 009 | commercial-architecture | Corporate events: highest-margin, lowest-hassle segment (Barnes) |
| 010 | commercial-architecture | Shift toward membership and recurring revenue (Barnes) |
| 011 | hospitality | Unreasonable hospitality and ambiance as the product (Barnes) |
| 012 | hospitality | Know your crowd economics and segments (Barnes) |
| 013 | culture | Build to pass on: succession and legacy (Barnes) |
| 014 | ai-tooling | AI and the future of work and skills (AI Future Shock) |
| 015 | ai-tooling | AI-era trust moats: pre-AI reputation compounds (Fromer) |
| 016 | ethics | Virtual-influencer ethics and the creator trust gap (Fromer) |
| 017 | media-business | The distribution flywheel (Fromer) |
| 018 | commercial-architecture | Share ownership: creator stock and option pools (Fromer) |
| 019 | ethics | Due diligence: founders hide the truth (Fromer) |
| 020 | content-strategy | A small, trusting audience beats a big passive one (Fromer) |
| 021 | media-business | Creator marketplace, pricing, and audience fit (Fromer) |
| 022 | strategy | Negotiation and the ownership mindset through hardship (Fromer) |
| 023 | culture | Black entrepreneurship and building in your own scene (Barnes) |
| 024 | operator-doctrine | Synthesis: the operator-conversation pattern |
| 025 | operator-doctrine | Synthesis: the optionality guardrail |

## Domain distribution (existing domains only · NO new domain)

| domain | chunks |
|---|---:|
| capital | 4 |
| commercial-architecture | 4 |
| operator-doctrine | 4 |
| media-business | 2 |
| hospitality | 2 |
| ethics | 2 |
| culture | 2 |
| ai-tooling | 2 |
| strategy | 1 |
| operator-process | 1 |
| content-strategy | 1 |

`hospitality` reused (pre-existed · count 6 before this batch). `nightlife`, `transcript`, `interview`, `conversation` were NOT created or used.

## Notes

- Two synthesis chunks (024 operator-doctrine, 025 operator-doctrine · the optionality guardrail).
- Per-guest attribution preserved (6 distinct attributions); the transcript format is handled via attribution + speaker-claim-vs-principle framing in `summary`/`usable_principle`, not a domain.
- Every chunk references CURRENT_OPERATOR_REALITY_BRIEF and carries the identity-optionality guardrail in `sniped_relevance`. The brief is NOT a chunked source.
- The Bible was NOT included; no faith/spiritual lane created here. Fringe-esoteric and personal spiritual-journey material was excluded.
