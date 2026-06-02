# BATCH_002_TIER_1_CANON_BOOKS · Source Index

**Date:** 2026-05-16
**Total chunks:** 152
**Source files:** 19 (1 deduplicated vs BATCH_001)

This index maps each source file to its chunk count, primary domains covered, and the chunk_id ranges so a downstream retrieval system can resolve any chunk back to its origin file in `01_KNOWLEDGE_BASE/batches/batch_002_extracted/`.

---

## Index by source file (sorted by chunk count, desc)

| Chunks | Source title | Source file | Author | Primary domains |
|-------:|--------------|-------------|--------|------------------|
| 16 | The 48 Laws of Power | `48_laws_of_power_greene.md` | Robert Greene | power, strategy |
| 14 | Poor Charlie's Almanack | `poor_charlies_almanack_munger.md` | Charles T. Munger | leadership, mental-models, decision-making |
| 11 | Zero to One | `zero_to_one_thiel.md` | Peter Thiel + Blake Masters | strategy, founder-psychology, network-effects |
| 11 | The 33 Strategies of War | `33_strategies_of_war_greene.md` | Robert Greene | strategy, power |
| 10 | Steve Jobs | `steve_jobs_isaacson.md` | Walter Isaacson | leadership, taste, creative-process |
| 10 | The Everything Store | `everything_store_bezos_stone.md` | Brad Stone | strategy, systems, leadership |
| 9 | The Art of War | `art_of_war_sun_tzu.txt` | Sun Tzu (tr. Lionel Giles) | strategy, leadership |
| 9 | The Ride of a Lifetime | `ride_of_a_lifetime_iger.md` | Robert Iger (with Joel Lovell) | leadership |
| 8 | Creativity, Inc. | `creativity_inc_catmull.md` | Ed Catmull (with Amy Wallace) | leadership, creative-process |
| 8 | Working Backwards | `working_backwards_bryar_carr.md` | Colin Bryar + Bill Carr | systems, leadership |
| 8 | Powerhouse Talk · Silicon Valley | `stoute_powerhouse_talk.txt` | Steve Stoute | brand, strategy |
| 7 | The Tanning of America | `tanning_of_america_stoute.md` | Steve Stoute | brand, culture |
| 6 | Shoe Dog | `shoe_dog_knight.txt` | Phil Knight | leadership, finance |
| 5 | The Outsiders | `outsiders_thorndike.md` | William N. Thorndike | capital-allocation, strategy |
| 5 | Genghis Khan and the Making of the Modern World | `genghis_khan_weatherford.md` | Jack Weatherford | empire-building, leadership |
| 5 | The Cold Start Problem | `cold_start_problem_chen.md` | Andrew Chen | network-effects, distribution |
| 4 | Alexander the Great | `alexander_the_great_freeman.md` | Philip Freeman | empire-building, leadership |
| 3 | The Song Machine | `song_machine_seabrook.md` | John Seabrook | distribution, brand |
| 3 | DisneyWar | `disneywar_stewart.md` | James B. Stewart | leadership, hiring |

**Total: 152 chunks across 19 source files**

---

## Index by author

| Chunks | Author | Books represented |
|-------:|--------|--------------------|
| 27 | Robert Greene | The 48 Laws of Power, The 33 Strategies of War |
| 15 | Steve Stoute | The Tanning of America, Powerhouse Talk |
| 14 | Charles T. Munger | Poor Charlie's Almanack |
| 11 | Peter Thiel (+ Blake Masters) | Zero to One |
| 10 | Walter Isaacson | Steve Jobs |
| 10 | Brad Stone | The Everything Store |
| 9 | Sun Tzu | The Art of War |
| 9 | Robert Iger | The Ride of a Lifetime |
| 8 | Ed Catmull (+ Amy Wallace) | Creativity, Inc. |
| 8 | Colin Bryar + Bill Carr | Working Backwards |
| 6 | Phil Knight | Shoe Dog |
| 5 | William N. Thorndike | The Outsiders |
| 5 | Jack Weatherford | Genghis Khan |
| 5 | Andrew Chen | The Cold Start Problem |
| 4 | Philip Freeman | Alexander the Great |
| 3 | John Seabrook | The Song Machine |
| 3 | James B. Stewart | DisneyWar |

Note: a small number of chunks were authored with slight variations in the `author` field (e.g., "Peter Thiel" vs "Peter Thiel + Blake Masters", "Ed Catmull" vs "Ed Catmull (with Amy Wallace)"). These all refer to the same person/team and are coalesced above for the count.

---

## Index by domain (cross-cuts sources)

| Chunks | Domain | What this captures |
|-------:|--------|---------------------|
| 47 | strategy | Narrow-market positioning, grand-strategy thinking, refusal-as-positioning, social-proof defense, contrarian truth, decade-arc patience |
| 36 | leadership | Founder-mode evolution, mood propagation, talent retention, succession discipline, end-to-end control, optimism as OS |
| 13 | power | Greene's laws applied to hierarchies, attention-courting, never-outshine-the-master, boldness-in-execution |
| 13 | brand | Cultural authority conversion, authenticity-as-asset, community ownership, refusal-positioning, the Cristal failure mode |
| 6 | systems | Working-backwards docs, single-threaded leadership, type-1/type-2 decisions, structured candor (Braintrust) |
| 5 | founder-psychology | The crazy idea, obsession, contrarian conviction, the comparison trap |
| 5 | network-effects | Cold-start problem, atomic network sizing, the hard side of network, network effect monetization |
| 4 | empire-building | Genghis's meritocracy, Alexander's mythology, the integration of conquered cultures |
| 4 | distribution | The 99-mile authority before the last-mile distribution, hit-makers mechanics, song-machine factory |
| 4 | capital-allocation | Outsider CEO playbook, 5 capital deployment options, allocation > operations |
| 3 | taste | Jobs's intersection of liberal arts + technology, the bridge premium, design as primary not decoration |
| 3 | creative-process | Catmull's protect-the-new, the Braintrust, originality is fragile |
| 2 | hiring | Talent flight, A-player retention |
| 2 | operations | Day 1 vs Day 2, the operating-discipline triad |
| 2 | culture | Stoute's tanning thesis, generational color-blindness |
| 1 | mental-models | Munger's latticework |
| 1 | decision-making | Bezos type-1/type-2 reversibility test |
| 1 | finance | Cash flow as oxygen (Knight) |

---

## Index by SNIPED-relevance tag (most strategically actionable filters)

Use these tags to retrieve chunks that point at specific SNIPED operating decisions:

| Tag | Chunks | What you'll find |
|-----|-------:|------------------|
| `anti-ai-positioning` | ~6 | Chunks defending and structuring SNIPED's anti-AI craft moat |
| `direction-stack-positioning` | ~5 | Chunks that frame the Direction Stack methodology in canonical terms |
| `premium-confidence` | ~4 | Chunks on holding price, refusing without apology, signaling confidence |
| `refusal-discipline` | ~4 | When and how to say no — narrow-market, off-scope, lane-protection |
| `client-experience` | ~3 | Hospitality-layer mechanics, lollapalooza stacking, white-glove design |
| `cultural-doc` | ~3 | Chunks supporting the Cultural Doc series (Greene Law 6, Stoute refusal-positioning) |
| `succession` | ~2 | Year 7-9 succession planning frame (Stewart, Bezos) |
| `quarterly-reset` | ~2 | Day 1 mentality applied to SNIPED's quarterly review (Bezos) |
| `constraint-audit` | ~2 | Grand-strategy alignment test (Greene 33, Munger inversion) |
| `lane-discipline` | ~3 | Stay-in-circle-of-competence chunks (Munger, Stoute, Thiel) |
| `decade-arc` | ~3 | Patient cultural-betting chunks (Stoute, Munger, Thorndike) |

---

## Chunk ID convention

All chunks use the format: `batch-002-chunk-NNN` where NNN is a zero-padded 3-digit sequence number from 001 to 152.

To resolve any chunk back to its source text:
1. Open `01_KNOWLEDGE_BASE/batches/BATCH_002_CHUNKS.jsonl`
2. Find the chunk by `chunk_id`
3. Use the `source_file` field to locate the extracted source at `01_KNOWLEDGE_BASE/batches/batch_002_extracted/<source_file>`
4. Use `direct_quotes` field as anchors to locate the relevant passage within the source text

---

**Status:** Index complete. All 19 source files have at least 3 chunks; the highest-density sources (Greene, Munger, Thiel, Isaacson, Stone) reflect their disproportionate signal density for SNIPED's specific operating questions.
