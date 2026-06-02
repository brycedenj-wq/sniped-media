# LITERARY_CANON_DYSTOPIAN source index · 2026-05-21

3 source files · 17 chunks · batch_id `LITERARY_CANON_DYSTOPIAN`. Study guides absent (0 chunks).

## Sources

| # | Extracted file | Author / Title | Chunks | Original source |
|--:|---|---|---|---|
| 1 | `animal_farm_orwell.txt` | George Orwell · Animal Farm (1945) | 001-005 (5) | `raw/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/[Animal Farm _1] Orwell, George - Animal Farm (1945, Secker & Warburg) - libgen.li.epub` |
| 2 | `handmaids_tale_atwood.txt` | Margaret Atwood · The Handmaid's Tale (1985) | 006-010 (5) | `raw/.../[The Handmaid's Tale 1 ] Atwood, Margaret - The Handmaid's Tale (2006_2017, Everyman's Library_Anchor Books) - libgen.li.mobi` |
| 3 | `brave_new_world_revisited_huxley.txt` | Aldous Huxley · Brave New World Revisited (1958 · NONFICTION essays) | 011-015 (5) + 016-017 synthesis | `raw/.../Aldous Huxley - Brave New World Revisited (2001) - libgen.li.pdf` |

Extracted via stdlib zipfile+HTML-strip (epub) + ebook-convert (mobi) + pdftotext -layout (pdf) · no OCR · no new deps · 161,792 words total (INTERNAL chunk-authoring reference only). Handmaid's Tale passed the 30,000-word floor (97,147 words).

## Brave New World Revisited · IMPORTANT

This is Huxley's **1958 nonfiction essay collection** re-examining the themes of his novel · NOT the novel Brave New World (1932). Chunked as the systems-warning nonfiction it is. The novel was not staged.

## Per-chunk concept + domain + source map

| chunk_id | Concept | Domain | source |
|---|---|---|---|
| 001 | The revolution betrayed · the new elite becomes the old | systems-thinking | animal_farm (Animal Farm) |
| 002 | Propaganda + rewritten rules · changing the record to change the present | systems-thinking | animal_farm |
| 003 | Squealer · spin that makes a population doubt its memory | culture | animal_farm |
| 004 | Boxer · the exploited loyalty of the believing worker | culture | animal_farm |
| 005 | The dogs · violence as the enforcement behind the propaganda | systems-thinking | animal_farm |
| 006 | Theocratic control of bodies · reduction to function | systems-thinking | handmaids_tale (The Handmaid's Tale) |
| 007 | Language control · renaming, ritual greetings, banned reading | culture | handmaids_tale |
| 008 | Surveillance + informants · the Eyes | systems-thinking | handmaids_tale |
| 009 | Gradual normalization · the slope not the cliff | operator-doctrine | handmaids_tale |
| 010 | Complicity of enforcers (the Aunts) + private resistance + dignity | ethics | handmaids_tale |
| 011 | Over-organization · the person subordinated to efficiency | systems-thinking | brave_new_world_revisited (BNW Revisited) |
| 012 | Propaganda in a democratic society · manufacturing consent vs informing | systems-thinking | brave_new_world_revisited |
| 013 | The arts of selling + chemical/subconscious persuasion · comfort as control | operator-doctrine | brave_new_world_revisited |
| 014 | Brainwashing + conditioning · the engineering of belief | ethics | brave_new_world_revisited |
| 015 | Education for freedom · the antidote · teaching resistance to manipulation | operator-doctrine | brave_new_world_revisited |
| 016 | The dystopian warnings as the operator's guardrail · what NOT to build | operator-doctrine | brave_new_world_revisited (synthesis) |
| 017 | Orwell's boot vs Huxley's soma · which AI tends toward | systems-thinking | brave_new_world_revisited (synthesis) |

## NEW domain

`systems-thinking` (8 chunks: 001, 002, 005, 006, 008, 011, 012, 017) is introduced by this mini-batch · it does NOT yet exist in `MASTER_CHUNK_MAP.json` and is registered at master-consolidation (the corpus's 60th domain · operator-approved · distinct from the older `systems` bucket).

## Cross-batch reinforcement summary

This mini-batch is the **ethical / cautionary counterweight** (the do-not-build conscience) to the corpus's AI-automation build canon.

| LCD chunk | Link |
|---|---|
| 008 surveillance · 002 record-rewriting | N8N_AUTOMATION_SYSTEMS (Airtable-as-memory · data tables) + the audit-trail / human-approval guardrails (N8N 012/013) |
| 007 language control | PROMPT_TEMPLATES_DEEP (language-as-leverage · the ethical dimension) |
| 013 comfort-as-control · 017 Huxleyan failure | intel_distribution_mechanics (anti-faceless-AI · depth-over-dopamine) |
| 011 over-organization | intel_company_of_one (right-size not scale) |
| 009 normalization / bright-lines | B7 operating-locks + feedback_operating_constraints |
| 016 operator guardrail | future BATCH_008 AI/tech canon (read the build-canon against this conscience) |
| 010 dignity under pressure | LITERARY_CANON_BLACK self-possession + B5 the-gaze (whole-human ethic) |

## Excluded material (NOT chunked)

| Material | Reason |
|---|---|
| 1984 SparkNotes · Fahrenheit 451 Bloom's Critical Interpretations | NOT in lane · orphaned secondaries (primaries not staged) · 0 chunks · kept skipped |
| The novel Brave New World (1932) | Not staged · only the 1958 Revisited essays present |
| Front/back-matter, copyright pages, RosettaBooks eForeword | Stripped at extraction · not chunked |
| Long passages of in-copyright text | Not reproduced · short illustrative quotes only (max 27 words) |
| General literary intake | Out of scope · separate lane · not touched |
