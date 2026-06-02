# LITERARY_CANON_BLACK source index · 2026-05-20

3 usable source files · 28 chunks · batch_id `LITERARY_CANON_BLACK`. 4 staged · Beloved deferred (0 chunks). TKAM not in lane.

## Sources

| # | Extracted file | Author / Novels | Chunks | Original source |
|--:|---|---|---|---|
| 1 | `bluest_eye_morrison.txt` | Toni Morrison · The Bluest Eye (1970) | 001-006 (6) | `raw/02_TIER_1_CANON_BOOKS/literary_canon_black/Toni Morrison - The Bluest Eye (2007, Knopf Doubleday) - libgen.li.mobi` |
| 2 | `their_eyes_hurston.txt` | Zora Neale Hurston · Their Eyes Were Watching God (1937) | 007-013 (7) | `raw/.../Zora Neale Hurston - Their Eyes Were Watching God (2009, HarperCollins) - libgen.li.zip` (EPUB-in-zip) |
| 3 | `color_purple_collection_walker.txt` | Alice Walker · The Color Purple (1982) + The Temple of My Familiar (1989) + Possessing the Secret of Joy (1992) | 014-021 (8) + cited by some synthesis | `raw/.../[The Color Purple 1...] The Color Purple Collection {Walker, Alice}(2012, Open Road) - libgen.li.epub` |
| (synthesis) | cites the most representative file | SNIPED cross-author | 022-028 (7) | n/a |

Extracted via stdlib zipfile+HTML-strip (epubs) + ebook-convert (mobi) · no OCR · no new deps · 382,001 words total (INTERNAL chunk-authoring reference only).

## Deferred / excluded

| Item | Status |
|---|---|
| Beloved (Morrison · `.pdf`) | DEFERRED · publisher-blurb / SEO-spam stub (698 words · not the novel) · 0 chunks · NOT extracted · re-acquire later |
| To Kill a Mockingbird (Lee) | NOT in lane · excluded from LITERARY_CANON_BLACK · route to a future GENERAL pass if wanted |

## Per-chunk concept + domain + source map

| chunk_id | Concept | Domain | source_file (novel) |
|---|---|---|---|
| 001 | Dick-and-Jane primer as imposed white-family ideal | culture | bluest_eye (Bluest Eye) |
| 002 | Beauty-standard wound · Pecola's prayer for blue eyes | culture | bluest_eye |
| 003 | Accepting rejection as legitimate · death of self-esteem | culture | bluest_eye |
| 004 | Quiet as it's kept · marigolds, communal witness, seasons | lineage | bluest_eye |
| 005 | The fractured primer as form · whose legibility | aesthetics | bluest_eye |
| 006 | Pecola as the unloved · the gaze that erases vs confers | culture | bluest_eye |
| 007 | Ships vs the horizon · men's wishes, women act on truth | culture | their_eyes (Their Eyes) |
| 008 | The pear tree · awakening, organic union, personal ideal | aesthetics | their_eyes |
| 009 | Vernacular as serious craft · free indirect voice | aesthetics | their_eyes |
| 010 | The porch · communal storytelling, dignity after labor | lineage | their_eyes |
| 011 | Finding her voice · silenced under Joe, reclaimed | culture | their_eyes |
| 012 | The horizon pulled in · living fully and the return | culture | their_eyes |
| 013 | Folklore, judgment, the right to narrate one's world | lineage | their_eyes |
| 014 | Epistolary voice · letters to God in Celie's vernacular | aesthetics | color_purple (The Color Purple) |
| 015 | The unspeakable made speakable · writing as survival | culture | color_purple |
| 016 | Sisterhood and solidarity · Celie, Nettie, Shug | culture | color_purple |
| 017 | From object to subject · Celie's self-authorship arc | culture | color_purple |
| 018 | Spirituality reimagined · God into trees/stars/Ancestor | lineage | color_purple |
| 019 | Refusing to be silenced · Celie's turn against Mr. | culture | color_purple |
| 020 | The Temple of My Familiar · ancestral memory (light) | lineage | color_purple (Temple) |
| 021 | Possessing the Secret of Joy · cultural trauma, witness (light) | culture | color_purple (Possessing) |
| 022 | The canon as Lineage-Doctrine backing · from inside | lineage | their_eyes (synthesis) |
| 023 | Voice/vernacular as craft and dignity · anti-shallow-content | lineage | color_purple (synthesis) |
| 024 | Black interiority + double-consciousness · who narrates | culture | bluest_eye (synthesis) |
| 025 | Cultural memory, survival, inherited story through-line | lineage | their_eyes (synthesis) |
| 026 | Artistic seriousness as refusal · the canon SNIPED measures against | operator-doctrine | bluest_eye (synthesis) |
| 027 | Witness, dignity, the gaze · the canon behind SNIPED portraiture | aesthetics | bluest_eye (synthesis) |
| 028 | Reclaiming the frame · authority, naming, self-definition | operator-doctrine | color_purple (synthesis) |

## NEW domain

`lineage` (8 chunks: 004, 010, 013, 018, 020, 022, 023, 025) is introduced by this mini-batch · it does NOT yet exist in `MASTER_CHUNK_MAP.json` and is registered at master-consolidation (the corpus's 59th domain · operator-approved).

## Cross-batch reinforcement summary

This mini-batch is the **literary foundation of the lineage**. The `culture` + new `lineage` domains established here are the buckets the future BATCH_010 (hip-hop / music-industry memoirs · Charnas / Ross / Gucci Mane / Jay-Z) will extend.

| LCB chunk | Link |
|---|---|
| 022, 025, 010, 013, 021 | feedback_lineage_doctrine (from-inside, never tourist) + B7 |
| 002, 006, 024, 027 | B5 photography canon + intel_photo_theory (the gaze · portraiture-as-dignity) |
| 005, 008, 009, 023 | B4 aesthetic doctrine (form-as-argument · vernacular-as-craft · the personal ideal) |
| 026 | INTELLECTUAL_ARTIST_FRAME (artistic-seriousness-as-refusal · performance + literature, same bar) |
| 016, 025 | feedback_scene_density_thinking (depth in a community over breadth) |
| 028 | SNIPED positioning (reclaiming the frame · refusal-positioning) |

## Copyright-safe quote discipline

`direct_quotes` are SHORT illustrative lines only (longest 33 words · a sentence or two · fair-use scale). No long passages reproduced. Extracted full text is internal reference, not redistributed.

## Excluded material (NOT chunked)

| Material | Reason |
|---|---|
| Beloved `.pdf` | Stub (blurb + SEO spam) · 0 chunks · deferred · re-acquire |
| To Kill a Mockingbird | Not in lane · white-authored Southern lit · would dilute the Black-canon thesis |
| Front/back-matter, copyright pages, publisher framing | Used only to source short quotes · not chunked as canon |
| Long passages of in-copyright text | Not reproduced · short illustrative quotes only |
| Dystopian / general literary intake | Out of scope · separate lanes · not touched |
