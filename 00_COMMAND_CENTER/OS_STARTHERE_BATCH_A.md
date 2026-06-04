# START HERE , BATCH A (2026-06-04)

> First controlled certify+distill pass on the `start here` folder. 5 smallest docx, each segment-ledgered, read, and coverage-proven (100%, checksums ok). Per-file truth, not a blanket "5/5 clean." No file-count confidence.

## Coverage proof (the method, proven)
Every file: re-wrapped to 180-char lines, partitioned <=40k chars, ledger with offsets + sha1, all segments read, `os_segment_ledger.py verify` = PROVEN. Ledgers in `_segments/<id>/LEDGER.csv`.

| doc | class | seg | coverage | cert_status | doctrine value |
|---|---|---|---|---|---|
| Aesthetic_Statement_v1 | clean_text_doc | 1 | PROVEN | **certified** | HIGH |
| Art_Series | clean_text_doc | 1 | PROVEN | **certified** | HIGH |
| sniped_context_tools_only | docx_source (ops) | 1 | PROVEN | **certified** | HIGH |
| MASTER CLAUDE CODE COURSE 1-8 | generated_os_artifact (session transcript) | 1 | PROVEN | **os_artifact** | NONE (not source doctrine) |
| last one for now | transcript_dump (Twitter SREF scrape) | 1 | PROVEN | **certified (coverage)** | LOW (SREF codes only, heavy boilerplate) |

## Doctrine distilled (certified files only)
**1. SNIPED Aesthetic v1** (`Aesthetic_Statement_v1`)
- One line: highly polished, commercially-driven editorial portraits on disciplined monochromatic color-blocking, clinical retouch, severe confident posing for graphic impact.
- Signatures: monochromatic / strict color-block palettes (backdrop+wardrobe+props one tonal family); commercial studio framing (center crops, A-frame bases, clean cuts between joints); editorial pose architecture (chin forward+down to define jaw; hands always tasked); clinical retouch (unify complexion, preserve pore detail, no plastic skin); graphic over atmospheric.
- Strengths (consistently 8+): color-as-structure; clean grading with pore detail protected; trained pose/presence.
- Weakness (the recurring one): depth/dimensionality , subjects flatten against the backdrop (parallel lighting, no rim).
- The two fixes: (a) add a rim/hair light by DEFAULT (place the kicker before the key); (b) "shoot the in-between" , direct the body not the face, talk through it, capture between rehearsed beats.
- On-set checklist: lock palette pre-shoot; rim before key; direct body (chin fwd+down, hands tasked); crop between joints not at them; retouch is the last 20% only.

**2. The Art Series** (`Art_Series`)
- 18-week (12-24wk) study: recreate one iconic frame from each of 9 masters to evolve the eye. Shape = confidence -> depth -> narrative -> surrender.
- Phase 1 (in-lane): Avedon (Boyd Fortin) -> Eggleston (Red Ceiling) -> Leibovitz (Whoopi/milk). Phase 2 (depth): Shore (Breakfast) -> Herzog (Man with Bandage). Phase 3 (narrative/in-between): Frank (Trolley) -> Meyerowitz (Porch). Phase 4 (break the system): Iturbide (Iguanas) -> Haas (Bullfight motion blur).
- Rule: re-run the 8-criteria audit on each recreation vs the archive baseline; the numbers say if the study is working. Drop Izis (unproductive opposite).

**3. SNIPED Tools/Infra Context** (`sniped_context_tools_only`)
- Instantly.ai: 5 sending domains x 5 inboxes = 25 inboxes, 30/day each = 150/day max, plain-text only, warm-up continuous, target 40-60% open (<30% = placement problem).
- Super Search: LinkedIn-verified leads, CITY-level only (no county/metro; suburbs roll into parent city; build city lists), 200-500 leads / 15 min, weekly target 800-1,500.
- Campaigns by niche (C1, C2…), 3-email sequence (Day 1/3/7) + A/B; replies in Unibox, respond <2 hrs.
- LinkedIn as Channel 2: 10 connects/day, DM 2-3/day to 48hr+ accepted connections (48-hour rule), 3 posts/week (Tue/Wed/Thu 9-10am PT, real shoot photos only), 5-10 substantive comments/day.
- Daily flow = 60-90 min: pull(15) -> tag(10) -> upload(10) -> LinkedIn(15) -> replies(15-30).

## Contradiction surfaced (must reconcile)
**Aesthetic v1 vs the locked visual-direction doctrine.** `Aesthetic_Statement_v1` defines the lane as **bold monochromatic COLOR-BLOCKING** (gold, green-on-green, red-on-black) , color as structure. But `feedback_visual_direction_luxury_editorial` (memory) locks SNIPED as **quiet luxury editorial restraint, Adobe Neutral, no saturated/teal-orange**. These are in tension: saturated color-block vs neutral restraint. NOT resolved here , flagged for the operator. (Possible resolution: color-blocking is the studio-portrait register; quiet-luxury-neutral is the composite/IG register , two registers, like the B&W card rule. But that's a hypothesis, not certified.)

## Skill / gate / workflow harvest (candidates, not built)
- `sniped-art-series-tracker` (skill) , drive the 9-frame study + re-run the 8-criteria audit per recreation.
- `rim-before-key` (gate/checklist line) , depth fix: place rim/kicker before the key light; reject flat-silhouette studio frames on dark wardrobe/bg.
- `shoot-the-in-between` (method) , direct the body, shoot transitions not poses; the narrative-8+ frames come from this.
- `instantly-daily-flow` (skill) , the 60-90 min outbound block (pull/tag/upload/LinkedIn/replies). Reinforces [[feedback_use_outbound_stack]].
- `sref-library` (skill) , harvest + store Midjourney SREF codes from scrapes (e.g. the codes in `last one for now`) for the visual-direction lane.

## Honest notes
- `MASTER CLAUDE CODE COURSE 1-8.docx` is misnamed , it is a prior Claude Code session transcript (git logs + staging report), NOT a course. Classified `generated_os_artifact`; contributes no source doctrine.
- `last one for now.docx` is a Twitter scrape; ~90% boilerplate (UI, trending news). Real value = a handful of Midjourney SREF codes. Covered, but doctrine value LOW.
- 3 of 5 are genuine certified doctrine. That 3/5 (not 5/5) is the point of certifying by file class.
