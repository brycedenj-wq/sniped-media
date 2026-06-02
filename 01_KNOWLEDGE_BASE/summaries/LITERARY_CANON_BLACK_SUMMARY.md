# LITERARY_CANON_BLACK summary · Morrison · Hurston · Walker · 2026-05-20

28 chunks · 3 usable source files (4 staged · Beloved deferred) · batch_id `LITERARY_CANON_BLACK` · validated 6/6.

## What this mini-batch covers

The Black literary canon staged in the 2026-05-19 intake, read for cultural-canon signal that strengthens the locked Lineage Doctrine, cultural memory, voice, dignity, survival, identity formation, double-consciousness, witness, inherited story, Black interiority, and SNIPED's refusal to become shallow content. It is the first LITERARY (vs operator/AI) lane in the corpus and the first of the queued literary-canon mini-batches.

It introduces **`lineage` as a NEW domain** (the 59th · approved by operator brief · present in the JSONL, registered in master at consolidation).

## Sources (3 usable · 1 deferred)

| Source | Author | Method | Words | Chunks |
|---|---|---|---:|---:|
| The Bluest Eye (1970) | Toni Morrison | ebook-convert (.mobi) | 53,600 | 6 |
| Their Eyes Were Watching God (1937) | Zora Neale Hurston | stdlib zipfile + HTML-strip (.zip = epub) | 71,033 | 7 |
| The Color Purple Collection (2012) | Alice Walker | stdlib zipfile + HTML-strip (.epub · 3 novels) | 257,368 | 8 (Color Purple 6 + Temple 1 + Possessing 1) |
| Cross-author synthesis | SNIPED | n/a | n/a | 7 |

**Deferred:** *Beloved* (Morrison) · the staged PDF is a 698-word publisher-blurb + SEO-spam stub, NOT the novel · 0 chunks · re-acquire real text later.
**Excluded:** *To Kill a Mockingbird* (Lee) · not in the lane · kept out to preserve a coherent Black women's literary canon.

## Per-source chunk distribution

| Source | Chunks |
|---|---:|
| The Bluest Eye (Morrison) | 6 (001-006) |
| Their Eyes Were Watching God (Hurston) | 7 (007-013) |
| The Color Purple (Walker) | 6 (014-019) |
| The Temple of My Familiar (Walker · light) | 1 (020) |
| Possessing the Secret of Joy (Walker · light) | 1 (021) |
| Cross-author synthesis | 7 (022-028) |

## Domain distribution

| Domain | Chunks | Notes |
|---|---:|---|
| culture | 13 | beauty-standard wound, voice/interiority, sisterhood, witness |
| `lineage` | 8 | **NEW domain** · from-inside telling, cultural memory, inherited story, ancestral memory, reclaiming the frame |
| aesthetics | 5 | form-as-argument, vernacular-as-craft, the pear-tree ideal, epistolary voice, the gaze |
| operator-doctrine | 2 | artistic-seriousness-as-refusal + reclaiming-the-frame (only the 2 chunks directly tied to SNIPED identity) |

`strategy` not used. `operator-doctrine` and `aesthetics` used sparingly per the brief (only where directly tied to SNIPED identity / voice / form). **lineage** appears in the JSONL but is NOT yet in `MASTER_CHUNK_MAP.json` (registered at consolidation).

## Where this mini-batch lands canonically

### Key signal installed
1. **The imposed-ideal / beauty-standard wound** (Bluest Eye 001-003, 006) · internalized racism, the death of self-esteem, the gaze that erases vs confers worth.
2. **Voice as dignity and self-possession** (Their Eyes 007-013, Color Purple 014, 019) · vernacular as serious craft, the porch as communal storytelling, reclaiming speech as the hinge of freedom.
3. **From-inside lineage + cultural memory** (Bluest Eye 004, Their Eyes 010/013, Color Purple 018, Temple 020, synthesis 022/025) · memory carried collectively, inherited story, the from-inside stance.
4. **Self-authorship + survival** (Color Purple 015-017) · object-to-subject arc, writing as endurance, sisterhood as the mechanism of becoming.
5. **Artistic seriousness as refusal + reclaiming the frame** (synthesis 026, 028) · the canon as the bar SNIPED measures against; liberation as seizing the authority to define.

### Cross-references opened
- **BATCH_004 aesthetic doctrine:** form-as-argument (005), the precise personal ideal / pear tree (008), vernacular-as-craft (009, 023) back the SNIPED restraint + seriousness lane.
- **BATCH_005 photography canon:** the gaze that erases vs dignifies (002, 006, 024, 027) is the literary foundation under SNIPED portraiture-as-dignity.
- **BATCH_007 + the Lineage Doctrine:** the from-inside stance (022), cultural memory as maintained labor (025), and honest witness including of harm (021) are the primary-source grounding for `feedback_lineage_doctrine`.
- **INTELLECTUAL_ARTIST_FRAME:** artistic-seriousness-as-refusal (026) pairs MJ's performance-craft seriousness with this literary-craft seriousness · same bar across performance and literature.
- **Future BATCH_010 (culture / Black culture):** this is the LITERARY foundation; BATCH_010 (hip-hop / music memoirs) is the music layer. `culture` + the new `lineage` domain are the buckets BATCH_010 will extend.

### Auto-memory reinforcement
- `feedback_lineage_doctrine` LOCKED 2026-05-12 ↔ chunks 022, 025, 010, 013, 021 (work from inside, never single-visit tourism).
- `feedback_scene_density_thinking` ↔ chunks 016, 025 (depth in a community over breadth).
- `intel_photo_theory` (Berger · the gaze) ↔ chunks 024, 027.

## Extraction-method results

stdlib `zipfile` + HTML-strip for the 2 epub-family files (handled the `.zip` extension cleanly · no rename of raw/ · no new deps); `ebook-convert` for the `.mobi` (via temp file, removed after read). No OCR. No new dependencies. 382,001 words extracted total. Front/back-matter and the publisher's framing prose are present in the extracted text but were not chunked as canon (used only to source short, accurate quotes). Beloved not extracted.

## Copyright-safe quote discipline

These are in-copyright novels. `direct_quotes` are SHORT illustrative lines only · the longest is 33 words (a sentence or two · fair-use scale). No long passages reproduced. The extracted full-text files are INTERNAL chunk-authoring reference, not redistributed content.

## Validation

All 6 checks PASS: JSONL parse · required fields (12/12) · chunk_id uniqueness (0 dupes / 28) · batch_id single value · source_file resolution (3 distinct, all resolve) · counts 28 chunks / 3 sources. Em-dash sweep: 0.

Additional checks PASS: Beloved 0 chunks (not extracted) · TKAM 0 chunks (not in lane) · `lineage` present in JSONL (8 chunks) but absent from master (registered at consolidation) · quote discipline confirmed (max 33 words).

## Deviations from LITERARY_CANON_BLACK_PLAN.md

1. **Final count 28** (target ~28 · range 22-32). Exactly on target.
2. **Beloved deferred · 0 chunks** (per operator decision · stub). The plan's depth target was met without it via the Walker 3-novel collection + 7 synthesis chunks.
3. **Walker companion novels light coverage** (1 chunk each · Temple + Possessing) per operator decision · main weight on The Color Purple (6) + cross-cutting lineage/culture synthesis (7).
4. **Domain split culture 13 + lineage 8 + aesthetics 5 + operator-doctrine 2.** `lineage` is the one NEW domain (operator-approved). operator-doctrine + aesthetics used only where directly tied to SNIPED identity/voice/form. strategy not used.
5. **No structural deviations.** No source files modified. Beloved stub left in place (flagged, not deleted). No master files updated. No new dependencies. No OCR. BATCH_008 not started. No dystopian/general literary intake touched.

## What this mini-batch enables

1. The first primary-source literary grounding for the locked Lineage Doctrine · the canon SNIPED documents from inside of.
2. The `lineage` domain · a chunk-level home for cultural memory, inherited story, voice, dignity, survival, identity, and witness (extensible by BATCH_010).
3. A literary backbone for the SNIPED portrait ethic (the gaze that dignifies) and the anti-shallow-content refusal (seriousness as craft).

## End state

`01_KNOWLEDGE_BASE/batches/LITERARY_CANON_BLACK_CHUNKS.jsonl` is canonical and validated. Awaits `master-consolidation` (which registers the NEW `lineage` domain). No master files updated in this run. New corpus total after consolidation: 918 + 28 = 946 chunks across 7 numbered batches + 7 mini-batches. Beloved re-acquisition flagged as a follow-up (+5-7 chunks when real text is supplied).
