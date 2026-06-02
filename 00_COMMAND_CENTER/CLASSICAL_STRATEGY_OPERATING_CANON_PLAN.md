# CLASSICAL_STRATEGY_OPERATING_CANON · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document plans the architecture for the largest remaining high-value book backlog and recommends the first lane to execute. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `44aa0c1 save session after HISTORICAL_BIOGRAPHY consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,547 · 10 numbered batches + 26 mini-batches · 62 official domains (75 combined keys).
- **Recovery program cleared; historical-biography lane cleared; non-book docs audited.** This is the next phase per ORIGINAL_SOURCE_COMPLETION_AUDIT.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate clusters found in raw/ (verified file-by-file)

### Cluster 1 · Tier-1 strategy_history (`raw/02_TIER_1_CANON_BOOKS/strategy_history/` · 14 files)
- The Prince (Machiavelli) · pdf · **net-new** · ~140,507 words
- Discourses on Livy (Machiavelli) · pdf · net-new
- Meditations (Marcus Aurelius) · epub · **net-new** · ~154,648 words
- On War (Clausewitz) · pdf · **net-new** · ~115,527 words
- Napoleon: A Life (Roberts) · epub · net-new · ~385,255 words
- The Landmark Herodotus · epub · net-new · ~437,842 words
- The Landmark Thucydides · epub · net-new
- Landmark Caesar (web essays) · pdf · **net-new** · ~187,010 words
- The Campaigns of Alexander (Arrian) · azw3 · net-new
- Alexander the Great and the Logistics of the Macedonian Army (Engels) · pdf · net-new
- The Book of Five Rings (Musashi) · **djvu · BROKEN** (no djvutxt)
- The Laws of Human Nature (Greene) · pdf · net-new TITLE (but Greene heavily represented · see 4)
- Mastery (Greene) · epub · net-new TITLE (Greene represented)
- The 50th Law (Greene/50 Cent) · mobi · net-new TITLE (Greene represented)

### Cluster 2 · operating_founder (`raw/02_TIER_1_CANON_BOOKS/operating_founder/` · 12 files)
- The Lean Startup (Ries) · pdf · net-new
- The Hard Thing About Hard Things (Horowitz) · epub · net-new
- Traction (Weinberg/Mares) · epub · net-new
- Blitzscaling (Hoffman/Yeh) · epub · net-new
- The Founder's Dilemmas (Wasserman) · epub · net-new
- The Goal (Goldratt) · pdf · net-new
- The E-Myth Revisited (Gerber) · mobi · net-new
- Built to Sell (Warrillow) · pdf · net-new
- Amp It Up (Slootman) · pdf · net-new
- Reengineering the Corporation (Hammer/Champy) · pdf · net-new
- (88 Laws / Winters · pdf · **already chunked** PERSONAL_OPERATING_CODE · exclude)
- (Moonwalk / MJ · epub · **already chunked** INTELLECTUAL_ARTIST_FRAME · exclude)

### Cluster 3 · network_distribution (5 files · all net-new)
The Inevitable + The Long Tail + New Rules for the New Economy (Kelly/Anderson) · Free (Anderson, abridged pdf) · The Great Online Game (McCormick pdf).

### Cluster 4 · sales_positioning (~17 files · mostly net-new)
$100M Offers + $100M Leads (Hormozi) · Crossing the Chasm (Moore) · Obviously Awesome (Dunford) · Play Bigger · Differentiate or Die (Trout) · Purple Cow + This Is Marketing + Tribes (Godin) · Building a StoryBrand (Miller) · The Mom Test (Fitzpatrick) · Competing Against Luck + The Innovator's Dilemma (Christensen) · Eating the Big Fish (Morgan) · Made to Stick (Heath) · Never Split the Difference (Voss). **NOTE:** several of these (Never Split the Difference, Eating the Big Fish, Competing Against Luck, This Is Marketing, Purple Cow, Tribes, StoryBrand) are likely already in BATCH_009 / BATCH_009_EXPANSION · heavy overlap · verify before any sales lane.

### Cluster 5 · brand-canon (raw root · ~6 files)
Watkins (Hello My Name Is Awesome) · Airey (Identity Designed) · Ries/Kotler (Positioning) · Wheeler (Designing Brand Identity) · Meyerson (Brand Naming) · Neumeier (The Brand Gap). **Identity-side · keep decision-neutral under optionality guardrails.**

### Cluster 6 · Tier-2 decision_judgment (~12 files · mixed)
Thinking Fast and Slow (Kahneman) · Noise (Kahneman) · The Righteous Mind + The Coddling of the American Mind (Haidt) · The True Believer (Hoffer) · The Crowd (Le Bon) · Games People Play (Berne) · Man's Search for Meaning (Frankl) · The Denial of Death (Becker · **djvu BROKEN**) · plus story-craft (McKee Story, Truby Anatomy of Story, Snyder Save the Cat, Campbell Hero with a Thousand Faces) which are really a STORYTELLING sub-cluster, not decision-judgment.

### Clusters 7-10 (leadership / consulting / fashion / systems · Tier-2)
Present in `raw/03_TIER_2_CANON_BOOKS/` subfolders (leadership_mgmt, consulting_service, fashion_luxury, systems_thinking) · not individually re-verified here · deferred to later lanes.

### Other Tier-1 root books (net-new, not in the operator's clusters but adjacent)
Zero to One (Thiel) · Shoe Dog (Knight) · Steve Jobs (Isaacson) · DisneyWar (Stewart) · ArtOfWar.pdf (**already chunked BATCH_002 · exclude**).

## 2. Source-quality / stub / scan check

- **Word-count probes (read-only, first-lane candidates):** The Prince 140,507 · Meditations 154,648 · On War 115,527 · Landmark Caesar 187,010 · Napoleon 385,255 · Landmark Herodotus 437,842. All clean, full text (pdf text-layer present, not scans).
- **Broken (exclude / re-acquire):** The Book of Five Rings (djvu), The Denial of Death (djvu) · no djvutxt on PATH.
- **Scale flag:** these are very large texts (individually 115K-440K words; the strategy_history cluster alone is ~2.5M words). Chunking MUST be curated/representative, never exhaustive (the HISTORICAL_BIOGRAPHY precedent: 16 chunks from ~912K words).

## 3. Already-chunked overlap check (verified)

- **Art of War (Sun Tzu):** ALREADY in BATCH_002 (source_title "The Art of War") · **EXCLUDE.**
- **Robert Greene:** The 48 Laws of Power AND The 33 Strategies of War ALREADY in BATCH_002 · Greene's power/strategy canon is well-represented. His strategy_history files (Laws of Human Nature, Mastery, 50th Law) are net-new TITLES but **DEFER** (Greene-as-author is covered; lower marginal value; verify against BATCH_002 first).
- **The Prince, Discourses, Meditations, On War/Clausewitz, Napoleon: A Life, Herodotus, Thucydides, Caesar, Arrian, Engels:** all **net-new** (0 chunks as source · the "Napoleon"/"On War"/"Alexander"/"Mastery" grep hits are the common words/mentions in other chunks, not these source_titles).
- **sales_positioning cluster:** HIGH overlap risk with BATCH_009 / BATCH_009_EXPANSION (Never Split the Difference, Eating the Big Fish, Competing Against Luck, This Is Marketing, Purple Cow, Tribes, StoryBrand, Made to Stick are likely already canonical) · must be overlap-audited before any sales lane.
- **operating_founder, network_distribution, decision_judgment classics:** net-new (no prior numbered batch covered these · BATCH_008 was AI/tech canon, not general operating/strategy).

## 4. Recommendation on batch architecture

**A SEQUENCE of curated mini-batches, one per coherent cluster · NOT one mega-batch and NOT a numbered batch.**

Rationale:
- The candidate set spans ~50+ net-new books across 6+ thematically distinct clusters and ~5M+ words. One mini-batch cannot hold it; one numbered batch is wrong (numbered batches are the locked legacy series per AGENTS.md · new work goes to named mini-batches).
- Each cluster is internally coherent and maps cleanly to one curated mini-batch, exactly as every lane since MONEY_OWNERSHIP has run (2-8 sources, ~12-27 chunks, curated).
- Sequencing lets each lane get its own plan/ship/consolidate/save cycle, overlap-audit, and domain check, and lets the operator stop/redirect between lanes.

**Proposed sequence (operator decides order; each its own future plan):**
1. **CLASSICAL_STRATEGY** (the namesake · cleanest, most iconic, fully net-new) · the recommended FIRST lane (see 5).
2. **CLASSICAL_HISTORY** (the two Landmark Greek histories + the Alexander pair · Herodotus, Thucydides, Arrian, Engels) · huge primary histories, curated.
3. **OPERATING_FOUNDER** (Lean Startup, Hard Thing, Traction, Blitzscaling, Founder's Dilemmas, The Goal, E-Myth, Built to Sell, Amp It Up, Reengineering) · the startup/operations canon.
4. **NETWORK_DISTRIBUTION** (Kelly, Anderson, McCormick) · the connected-economy canon.
5. **SALES_POSITIONING** (only AFTER a BATCH_009 overlap audit · chunk only the net-new remainder).
6. **DECISION_JUDGMENT** (Kahneman, Haidt, Hoffer, Le Bon, Frankl, Berne) · the judgment/crowd-psychology canon · note the storytelling sub-cluster (McKee/Truby/Snyder/Campbell) could be its own STORYTELLING lane.
7. **Tier-2 leadership / consulting / fashion / systems** · later curated lanes.
8. **BRAND_CANON** (identity-side · keep decision-neutral · arguably hold until the fresh SNIPED brief, given the optionality guardrails).

## 5. Recommended FIRST lane: CLASSICAL_STRATEGY

The lane's namesake, the most iconic and coherent cluster, fully net-new, and the highest-signal-per-chunk material in the backlog.

### Recommended include / defer / exclude (first lane)

- **INCLUDE (4 · CORE · curated):**
  - **The Prince (Machiavelli)** · pdf · ~140,507 words · Renaissance statecraft / power.
  - **On War (Clausewitz)** · pdf · ~115,527 words · modern war theory (friction, fog of war, center of gravity, the culminating point, war as politics by other means).
  - **Meditations (Marcus Aurelius)** · epub · ~154,648 words · Stoic self-command / leadership character.
  - **Landmark Caesar (web essays)** · pdf · ~187,010 words · ancient Roman military command / the commander's primary record.
  - Combined ~597K words · curated, not exhaustive.
- **DEFER (to CLASSICAL_HISTORY / later classical lanes):** Napoleon: A Life (Roberts · 385K · also overlaps the HISTORICAL_BIOGRAPHY register), The Landmark Herodotus (438K), The Landmark Thucydides, The Campaigns of Alexander (Arrian), Alexander logistics (Engels), Discourses on Livy (Machiavelli), and the Greene trio (Laws of Human Nature / Mastery / 50th Law · verify vs BATCH_002 first).
- **EXCLUDE (0 chunks):**
  - Art of War (Sun Tzu) · already in BATCH_002.
  - The 48 Laws of Power + The 33 Strategies of War (Greene) · already in BATCH_002.
  - The Book of Five Rings (Musashi) · djvu · broken.
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every other already-canonical source.

### Estimated chunk range (first lane)

- **Target:** ~16-20 chunks · **Range:** 12-22 (halt-and-report if outside).
- **Synthesis:** 1-2 closing synthesis chunks (the classical-strategy pattern + the optionality guardrail).
- **Provisional per-source split:** The Prince ~4-5 · On War ~4-5 · Meditations ~4-5 · Caesar ~3-4 · + 1-2 synthesis. Curated/representative, not chapter-by-chapter (the HISTORICAL_BIOGRAPHY precedent).

### Recommended domains (EXISTING domains only · NO new domain)

Verified to exist: `strategy` (182), `power` (17), `leadership` (42), `operator-doctrine` (90), `operator-process` (77), `ethics` (44), `mental-models` (1), `mindset` (10), `decision-making` (5), `patience` (1), `culture` (55).

| Domain | Planned use in the first lane |
|---|---|
| `strategy` (anchor) | Machiavelli statecraft; Clausewitz war theory (friction, center of gravity, fog of war, culminating point, war-as-politics); Caesar's campaigns. |
| `power` | Machiavelli's power dynamics (the lion and the fox, feared vs loved, fortune vs virtù). |
| `leadership` | Command lessons (Caesar in the field; Clausewitz's military genius / the commander). |
| `operator-doctrine` | Meditations' duty/self-discipline; the doctrine of the commander; the synthesis + optionality guardrail. |
| `mindset` | Meditations' Stoic mindset (the inner citadel, control-what-you-can, memento mori, amor fati). |
| `ethics` | Machiavelli's ends-vs-means realpolitik (read honestly, not endorsed); Stoic ethics; the morality of war. |
| `mental-models` | Clausewitz's friction / fog of war / center of gravity as durable models; Machiavelli's fortune-vs-virtù (grows a thin domain · count 1). |
| `decision-making` | Judgment under uncertainty and incomplete information (Clausewitz, Machiavelli). |

### Domain issue to flag (important)

- **`philosophy`, `statecraft`, `war`, `history` do NOT exist** (ABSENT). **None will be created.** Routing: philosophy/Stoicism -> `mindset` / `operator-doctrine` / `ethics`; statecraft -> `strategy` / `power`; war-theory -> `strategy` / `mental-models` / `leadership`; history -> `culture` / `strategy`.
- **`mental-models` (count 1) and `patience` (count 1) are thin existing domains** this lane can legitimately grow · used where squarely warranted.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 6. Bible exclusion confirmation

**The KJV Bible remains OUTSIDE `raw/`, UNCHUNKED, held as a SPIRITUAL_FOUNDATION anchor** per NEW_SOURCE_INTAKE_PLAN. It is NOT part of any cluster here and will NOT be touched, staged, chunked, or included. (Meditations is Stoic philosophy, not scripture; it is treated as a secular leadership/mindset text, and no faith/spiritual lane is created.)

## 7. Identity optionality confirmation

- **No final SNIPED direction. No final SNIPED Media direction. No final BASEPLATE direction.**
- The entire remaining canon (classical strategy, operating-founder, network, sales, decision, brand) is held as a **decision-support / pattern-library layer** read against CURRENT_OPERATOR_REALITY_BRIEF · NOT a directive about what BJ should build or become. The brand-canon cluster especially stays decision-neutral (it touches identity/naming · held, arguably until the fresh SNIPED brief). Machiavelli/Clausewitz are read as strategy/power pattern libraries, NOT a directive that BJ pursue ruthless power tactics; the realpolitik/ethics chunks stay honest, not endorsements. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 8. Deliverables for the first lane (NOT created now · when CLASSICAL_STRATEGY is authorized)

`01_KNOWLEDGE_BASE/batches/CLASSICAL_STRATEGY_CHUNKS.jsonl` · `.../batches/classical_strategy_extracted/` · `.../summaries/CLASSICAL_STRATEGY_SUMMARY.md` · `.../indexes/CLASSICAL_STRATEGY_SOURCE_INDEX.md` · `00_COMMAND_CENTER/batch_logs/CLASSICAL_STRATEGY_EXTRACTION_LOG.md` + `..._COMPLETE.md` · `scripts/extract_classical_strategy.py` + `scripts/write_classical_strategy_chunks.py`. Canonical 12-field schema · `batch_id` = `CLASSICAL_STRATEGY` · per-source attribution.

## 9. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,547.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdfinfo` / `ebook-convert`+`pdftotext`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 10. Next step (operator decision · do not start without authorization)

Authorize the **CLASSICAL_STRATEGY** first lane (4 core texts · The Prince + On War + Meditations + Landmark Caesar · target ~16-20 · existing domains only · `strategy` anchor · no new domain · Art of War / 48 Laws / 33 Strategies / Book of Five Rings / Bible excluded · curated, not exhaustive), then commit the ship outputs, then consolidate. Subsequent lanes (CLASSICAL_HISTORY, OPERATING_FOUNDER, NETWORK_DISTRIBUTION, SALES_POSITIONING [post-overlap-audit], DECISION_JUDGMENT, Tier-2, BRAND_CANON) follow as separate plan/ship/consolidate cycles.
