# BIOGRAPHY_FOUNDER_MEDIA mini-batch · PLAN

**Date planned:** 2026-05-23
**Status:** PLAN ONLY · not extracted, not chunked, master files untouched, not committed.
**Batch kind:** mini-batch (descriptive slug · the 15th mini-batch) · curated CORE scale (operator-decided · see section A).

> **OPERATOR DECISIONS APPLIED (2026-05-23 · locked):**
> 1. **Curated CORE mini-batch scale** (not a full numbered batch).
> 2. **NO new domain.** Anchor on the existing `founder-psychology`; route the rest to existing domains.
> 3. **`media-business` held** as a possible FUTURE lane/domain (HBO/ESPN/SNL cluster) · NOT created here.
> 4. **6 CORE sources locked** (section 4): D.V. (Vreeland), No Filter (Frier), Losing My Virginity (Branson), Grinding It Out (Kroc), That Will Never Work (Randolph), Made in Japan (Morita).
> 5. **Deferred:** founder second tier (Uber/Super Pumped, Airbnb, Sam Walton, Elon Musk, Schultz/Starbucks, Titan/Rockefeller, Banana King); media-business cluster (ESPN, SNL, HBO/Tinderbox); Chernow histories (Grant, Washington).
> 6. **Exclude / recovery:** Hit Men (scanned), Grace (0-byte stub), Total Recall (0-byte stub), The Mailroom (`.djvu`).
> 7. **Identity optionality preserved** · founder/media arcs are pattern-library only, NOT a directive to manufacture a SNIPED myth · no final SNIPED / SNIPED Media / BASEPLATE direction.

---

## 0. Verified starting state

- **Head commit:** `d548128 save session after MONEY_OWNERSHIP consolidation`
- **Working tree:** clean before this plan.
- **Total chunks:** 1,332 · 10 numbered batches + 14 mini-batches · 61 official domains (74 combined_domain_counts keys).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **No lane started:** no `BIOGRAPHY_FOUNDER_MEDIA_CHUNKS.jsonl`, no extracted dir, no COMPLETE marker, no prior plan.

---

## 1. Goal + theme

Founder psychology, operator arcs, myth-building, media/company-building stories, personal inevitability, taste-making, leadership, ambition, resilience, distribution, brand-through-life, and how individuals turn skill, narrative, capital, and timing into durable power.

The source set is `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` (~24 files).

---

## TWO FLAGS · RESOLVED BY OPERATOR (2026-05-23)

### A. SCALE FLAG · RESOLVED: curated mini-batch
~19 net-new usable books total well over 2.5M words (Grant 495K, Washington 439K, Those Guys Have All the Fun 309K, Live From New York 234K, Elon Musk 205K, Losing My Virginity 183K, Made in Japan 136K, Super Pumped 126K, No Filter 116K, That Will Never Work 102K, Sam Walton 96K, Airbnb 88K, Grinding It Out 71K, D.V. 66K, + 5 mobi: Onward, Pour Your Heart Into It, Titan, Tinderbox, The Fish That Ate the Whale) · numbered-batch scale. **DECISION: ship the curated CORE of 6 titles as a mini-batch now** (section 4); defer the rest (section 4 DEFER).

### B. DOMAIN FLAG · RESOLVED: no new domain
Checked against `combined_domain_counts`: `founder-psychology` EXISTS (17 · the anchor); `biography`, `media-business`, `founder`, `media` are MISSING. **DECISION (operator): introduce NO new domain** · anchor on `founder-psychology` and route the rest to existing domains. **`media-business` is HELD** as a possible future lane/domain (the HBO/ESPN/SNL cluster) · NOT created now. The reference table below is retained for the audit trail.

### (reference · original domain check · per requirement #7)
Checked against `combined_domain_counts`:

| Proposed domain | Status |
|---|---|
| `founder-psychology` | **EXISTS (17)** · the natural home |
| `biography` | **MISSING** |
| `media-business` | **MISSING** |
| `operator-doctrine` | EXISTS (63) |
| `operator-process` | EXISTS (63) |
| `strategy` | EXISTS (159) |
| `brand` | EXISTS (28) |
| `lineage` | EXISTS (20) |
| `culture` | EXISTS (40) |
| `capital` | EXISTS (9) |
| `aesthetics` | EXISTS (66) |

**Recommendation (no new domain):** route everything to existing domains, anchored on `founder-psychology`, plus `operator-doctrine`, `culture`, `brand`, `strategy`, `aesthetics` (taste-making), `capital` (wealth-building arcs, light), `lineage` (light). Do NOT mint `biography` (too generic) or `media-business`. **Optional future decision:** IF the operator later runs the media-business cluster (HBO/ESPN/SNL/Hit Men/Instagram as its own lane), a `media-business` domain might then be warranted · flag it, do not create it now. No domain will be created without explicit operator approval.

---

## 2. Candidate inventory (`raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/`)

### Founder / company-building (on-theme)
| File | Author · Subject | Type | Words | Status |
|---|---|---|--:|---|
| Losing My Virginity | Branson · Virgin | epub | 183,321 | net-new |
| Grinding It Out | Ray Kroc · McDonald's | epub | 70,632 | net-new |
| That Will Never Work | Marc Randolph · Netflix | epub | 102,037 | net-new |
| Super Pumped | Mike Isaac · Uber | epub | 125,963 | net-new |
| The Airbnb Story | Leigh Gallagher · Airbnb | epub | 87,528 | net-new |
| Made in Japan | Akio Morita · Sony | pdf | 135,753 | net-new |
| Sam Walton: Made In America | Walton · Walmart | pdf | 96,353 | net-new |
| Elon Musk | Isaacson · Musk/Tesla/SpaceX | epub (86MB) | 204,776 | net-new |
| Onward · Pour Your Heart Into It | Schultz · Starbucks (2 books) | mobi | (ebook-convert) | net-new |
| Titan | Chernow · Rockefeller | mobi | (ebook-convert) | net-new |
| The Fish That Ate the Whale | Cohen · Banana King | mobi | (ebook-convert) | net-new |

### Media-business / entertainment (on-theme · distribution, taste, moguls)
| File | Subject | Type | Words | Status |
|---|---|---|--:|---|
| No Filter | Instagram | epub | 115,806 | net-new |
| Those Guys Have All the Fun | ESPN | epub | 308,626 | net-new |
| Live From New York | SNL | epub | 234,076 | net-new |
| Tinderbox | HBO | mobi | (ebook-convert) | net-new |
| Hit Men | music-business power brokers | pdf | **0 (SCANNED)** | **BROKEN · recovery** |
| The Mailroom | Hollywood agents | djvu | (blocked) | **BROKEN format · recovery** |

### Taste-making (on-theme)
| File | Subject | Type | Words | Status |
|---|---|---|--:|---|
| D.V. | Diana Vreeland · Vogue/editorial | epub | 65,705 | net-new |
| Grace: A Memoir | Grace Coddington · Vogue | epub | **0 (STUB)** | **BROKEN · recovery** |

### Historical biography (leadership · arguably off the founder/media theme)
| File | Subject | Type | Words | Status |
|---|---|---|--:|---|
| Grant | Chernow · U.S. Grant | epub | 494,971 | net-new (huge · off-theme-ish) |
| Washington: A Life | Chernow · Washington | pdf | 438,704 | net-new (huge · off-theme-ish) |

### Stub / broken (exclude · recovery)
- **Total recall** (Schwarzenegger) · epub · **0 bytes (STUB)**.

---

## 3. Pre-flight peek · source quality

- **Net-new:** all titles verified net-new ("Onward" and "Grant" overlap hits were body-text phrases, not source_titles/source_files · no Schultz/Chernow source in any chunk).
- **Broken / recovery (exclude · 0 chunks):** Hit Men (scanned · 0 words via pdftotext); Grace: A Memoir (0-byte stub); Total recall (0-byte stub); The Mailroom (`.djvu` · blocked).
- **mobi (need `ebook-convert` · calibre on PATH · no OCR):** Onward, Pour Your Heart Into It, Titan, Tinderbox, The Fish That Ate the Whale.
- **Large but real text:** Elon Musk (86MB epub · 204,776 words · fine), Made in Japan (34MB pdf · 135,753 words · text, not scanned), Grant/Washington (huge · real text).
- **Excludes BATCH_010 culture overlap:** the hip-hop / Black-music memoirs (Jay-Z, Gucci Mane, Rick Ross, etc.) live in BATCH_010 and are NOT in this folder · no overlap. Hit Men (music business) is a different book and is excluded anyway (scanned).
- **Recovery/acquisition items:** untouched · the 4 broken files above become recovery flags.

---

## 4. Recommended inclusion / defer / exclude

### INCLUDE · curated CORE (LOCKED · 6 sources)
The highest-signal titles, weighted toward SNIPED relevance (taste-making, visual media, brand-through-life, operator arcs):
1. **D.V.** (Diana Vreeland) · taste-making, the editorial eye, myth-building, brand-through-life · the most SNIPED-relevant (editorial/photography lineage).
2. **No Filter** (Instagram) · visual-media company-building, distribution, aesthetic culture, founder arc · directly SNIPED-relevant.
3. **Losing My Virginity** (Branson) · myth-building, brand-through-life, resilience, the founder-as-brand.
4. **Grinding It Out** (Ray Kroc) · the operator arc, systematization, persistence, late-bloom inevitability.
5. **That Will Never Work** (Marc Randolph · Netflix) · founder psychology, pivots, ambition, distribution disruption.
6. **Made in Japan** (Morita · Sony) · taste + product + global brand-building + the maker-operator.

### DEFER (to a numbered batch or thematic sub-lanes)
- **Founder second tier:** Super Pumped (Uber), The Airbnb Story, Sam Walton, Elon Musk, Schultz (Onward + Pour Your Heart Into It), Titan (Rockefeller), The Fish That Ate the Whale.
- **Media-business cluster (own sub-lane · may warrant a `media-business` domain):** Those Guys Have All the Fun (ESPN), Live From New York (SNL), Tinderbox (HBO).
- **Historical-biography sub-lane (off the founder/media theme):** Grant + Washington (Chernow · huge · leadership/history).

### EXCLUDE / RECOVERY
- Hit Men (scanned), Grace: A Memoir (0-byte stub), Total recall (0-byte stub), The Mailroom (`.djvu`) · re-acquire clean editions.

---

## 5. Estimated chunk yield

- **Curated CORE (6 sources):** ~18-24 chunks (3-4 per book + 1-2 synthesis). Target ~18-24, range 15-28.
- **Full memoirs folder (if escalated to a numbered batch):** ~60-80 chunks.

ID pattern `BIOGRAPHY_FOUNDER_MEDIA_NNN`. 1-2 cross-source synthesis chunks.

---

## 6. Domain set (LOCKED to existing · NO new domain · operator-confirmed)

Anchored on the existing `founder-psychology` (17). Route by content:

| Domain | Current | Use here |
|---|--:|---|
| `founder-psychology` | 17 | founder arcs, temperament, ambition, inevitability, resilience |
| `operator-doctrine` | 63 | operator judgment, standards, persistence, systematization |
| `brand` | 28 | brand-through-life, the founder-as-brand, myth-building |
| `aesthetics` | 66 | taste-making, the editorial eye (Vreeland, No Filter) |
| `culture` | 40 | media culture, distribution, taste cycles |
| `strategy` | 159 | company-building strategy, distribution disruption |
| `capital` | 9 | the wealth/ownership arc where central (light) |
| `lineage` | 20 | light · only where a genuine lineage thread appears |

**NO new domain recommended.** `biography` and `media-business` are NOT minted (see section B). Estimated distribution (indicative): founder-psychology ~6-7 · brand ~3 · aesthetics ~3 · operator-doctrine ~3 · culture ~2 · strategy ~2 · capital ~1 · lineage ~1. Finalized at chunk time.

### 7. NEW domain decision (LOCKED)

`founder-psychology` EXISTS and is the anchor. `biography`, `media-business`, `founder`, `media` are MISSING. **Operator decision: introduce NO new domain** · route to existing domains. `media-business` is HELD as a possible future lane/domain (the HBO/ESPN/SNL cluster) and is NOT created now. Any candidate new domain at chunk time must halt and re-surface to the operator.

---

## 8. How this mini-batch connects to the corpus

- **MONEY_OWNERSHIP:** capital/ownership is the economics; BIOGRAPHY_FOUNDER_MEDIA is the lived operator arc that turns skill + narrative + capital + timing into durable power · the human case studies behind the capital theory.
- **BATCH_010 lineage + Black culture canon:** BATCH_010 is the Black-music/culture lineage; this lane is the broader founder/media-mogul arc (Vreeland, Branson, Instagram, etc.) · complementary, no overlap.
- **BATCH_009 / BATCH_009_EXPANSION (commercial strategy):** the positioning/category/challenger theory, here enacted in real company-building stories (Netflix, Instagram, Sony).
- **EDGE_AND_OPERATING_DISCIPLINE:** the discipline/judgment frameworks, here shown in operator temperament and resilience across decades.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** these arcs are inspiration and pattern-library, NOT a template to copy · myth-building and brand-through-life are decision-support lenses, not a directive to manufacture a SNIPED founder myth.
- **Future SNIPED direction (without deciding it):** supplies operator-arc patterns the operator can draw from for whatever direction emerges · reversible inputs.

---

## 9. This lane does NOT finalize brand direction

Confirmed. BIOGRAPHY_FOUNDER_MEDIA chunks founder/operator/media biographies as pattern-library and decision-support. It does **not** decide SNIPED, SNIPED Media, or BASEPLATE direction, does not prescribe a founder myth for the operator, and does not commit to any path. Per the active guardrails, `sniped_relevance` frames the arcs as lenses (what these operators did and why it worked), with SNIPED's direction undecided and photography one option among several.

---

## 10. Deliverables (produced only at the authorized ship step · NOT now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/BIOGRAPHY_FOUNDER_MEDIA_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/biography_founder_media_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/BIOGRAPHY_FOUNDER_MEDIA_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/BIOGRAPHY_FOUNDER_MEDIA_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/BIOGRAPHY_FOUNDER_MEDIA_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/BIOGRAPHY_FOUNDER_MEDIA_COMPLETE.md` |
| Extract script | `scripts/extract_biography_founder_media.py` (epub via stdlib zipfile · pdf via pdftotext · mobi via ebook-convert if a mobi enters CORE) |
| Chunk writer | `scripts/write_biography_founder_media_chunks.py` |

Schema: the canonical 12-field JSONL. `batch_id` = `BIOGRAPHY_FOUNDER_MEDIA`. source_file values resolve under `biography_founder_media_extracted/`. Copyright-safe quote discipline: in-copyright trade books · short illustrative lines only (target longest <= 14 words) · most chunks paraphrase. No OCR · no new dependencies (the CORE 6 are 5 epub/pdf + Made in Japan pdf · no mobi in CORE, so even ebook-convert is optional).

---

## Constraints honored by this plan

- Did NOT extract, chunk, update master files, or commit.
- Did NOT modify any `raw/` source file · recovery/acquisition items untouched.
- No em-dashes.
- **No new domain created** · the domain issue (biography/media-business missing) is flagged for operator decision (requirement #7-8).
- Does not finalize SNIPED / SNIPED Media / BASEPLATE direction (optionality preserved).
- Stops at the plan.

## Open questions · ALL RESOLVED (2026-05-23)

1. **SCALE:** RESOLVED · curated CORE mini-batch (6 sources · ~18-24 chunks).
2. **DOMAIN:** RESOLVED · NO new domain · anchor on `founder-psychology` · `media-business` held for a future lane.
3. **CORE confirm:** RESOLVED · the 6 titles are locked (D.V., No Filter, Losing My Virginity, Grinding It Out, That Will Never Work, Made in Japan).
4. **Historical biographies:** RESOLVED · Grant + Washington deferred to a separate historical-biography lane.

Plan is ready to ship on authorization (extract -> chunk -> validate -> consolidate). No new domain; founder-psychology is the anchor.
