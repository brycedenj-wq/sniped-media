> **Retired 2026-06-28.** One or more OS_* systems referenced in this document were retired during the OS repository convergence and moved to `_HISTORY/` or `_ARCHIVE/`. Those references are historical and no longer active. See `CONVERGENCE_PLAN_2026-06-28.md`.

# OS_ROUTER_INDEX , domain → what to pull (the router reads THIS, not everything)

> The router consults this map to pull ONLY the relevant doctrine doc / skill / chunk-index for a task. Keep it small. Tag each entry `active` / `superseded` / `hypothesis`. The router ignores `superseded` by default.

## How to use
Request → classify domain → pull the listed doctrine doc(s) + skill(s). For evidence, pull chunk ids via `01_KNOWLEDGE_BASE/MASTER_INDEX.md` → `batches/*_CHUNKS.jsonl`. Never bulk-load.

## Domains
| domain | doctrine (pull one) | skills (invoke) | chunk index | status |
|---|---|---|---|---|
| corpus certification | OS_CERTIFICATION_STANDARD, OS_CERTIFICATION_REPORT | os_certify, os_segment_ledger, os-token-safe-reader | , | active |
| AI image / composite | OS_DOCTRINE_BATCH_007/008/011/012, OS_CAPABILITY_TOOL_ROUTING | sniped-crs-builder, os-face-lock, kling-production-sop | batch_006/007 | active |
| AI video / motion | OS_CAMPAIGN_HOUSE_PIPELINE | kling-production-sop, os_motion_qa, os_motion_ready | , | active |
| character + world | OS_PHASE1_ATOM, OS_PHASE3_FACELOCK | sniped-crs-builder, os-world-bible, os-face-lock | , | active |
| production harness | OS_CAMPAIGN_HOUSE_PIPELINE | os_production, os_batch, os_generate | , | active |
| brand / positioning | OS_DOCTRINE_REREAD_C_*, intel_positioning_phrases (memory) | brand-validation-machine | persuasion/positioning | hypothesis |
| outreach / sales | OS_DOCTRINE (VIB), feedback_use_outbound_stack (memory) | sniped-vib-outreach (drafted) | cold_email | hypothesis |
| content / distribution | OS_STARTHERE_* (Content-Marketing OS) | hit-mechanics (drafted) | , | active |
| Claude / automation | OS_CLAUDE_OPERATING_MANUAL, OS_BOOTLOADER_ARCHITECTURE | os-command-router, os-quality-gates | claude_operator | active |
| skill lifecycle | feedback_skill_activation_contract (memory) | os_skill | , | active |
| books / strategy classics | OS_DOCTRINE_REREAD_* / BOOKWAVE_* | , | batches/*_extracted | provisional (no segment ledger) |

## Notes
- `provisional` / `hypothesis` doctrine: usable as input, NEVER as settled fact. Attach the tag when citing.
- Update this index when a new certified doctrine doc or ACTIVE skill is added. Keep it under ~30 rows; it is a router map, not a catalog.

## Certified folders (do NOT re-read , cert ledger is the redo gate)
- `start here` (98/98 certified, 2026-06-04). Doctrine: `OS_STARTHERE_DOCTRINE.md`. Backlog: `OS_STARTHERE_BACKLOG.md`. Per-doc: `starthere_results/`. Ledger: `OS_STARTHERE_CERT_LEDGER.csv`.
  - Pull from here ONLY when the task domain matches (content/marketing, photography set-design, the Stacks, outreach, AI tooling). Pull the SPECIFIC doc, never the folder.
  - The giants (series_1/2/3/5, high_level_convos, new_hot_shit, astro_claude) are coverage-proven but diluted transcripts , query by topic, never bulk-load.

## Added doctrine rows
| domain | doctrine (pull one) | skills | status |
|---|---|---|---|
| content / 7x7 / distribution | OS_STARTHERE_DOCTRINE §A (Content OS, Stacks) | (build: sniped-7x7-repurpose) | active certified |
| photography set design | OS_STARTHERE_DOCTRINE §A (set-design, posing, lighting, moodboard) | direction-stack (merge target) | active certified |
| product / clothing launch | OS_STARTHERE_DOCTRINE §A (validation-first) | (gate: validation-before-manufacture) | active certified |

## PROVISIONAL-BOOK ROUTER RULE (locked)
- A book/source is citable as **certified doctrine ONLY if it has a segment ledger** (`coverage_proven`/`certified` in a cert ledger). Today that is ~0 classic books.
- If the router pulls a `provisional_chunked_not_certified` book (any of the 215, incl. the cited 25), the OUTPUT must carry a **`[provisional: <book>, chunk-distilled, not coverage-proven]`** tag. Never present a provisional book chunk as final truth.
- For a MAJOR decision, do not rely on a provisional book , flag it as needs-certification (see OS_BOOK_TARGETED_CERTIFICATION_QUEUE.md) and proceed only with the provisional label, or certify first.
- The book-source map is `OS_BOOK_SOURCE_INDEX.csv`; dependency map `OS_BOOK_DOCTRINE_DEPENDENCY_MAP.md`. Pull a specific book's chunks by topic; never bulk-load.

## DOCTRINE CONFIDENCE LABELS (post book-cert reconciliation 2026-06-04)
The router MUST attach these when citing doctrine. Source: OS_BOOK_DOCTRINE_RECONCILIATION_REPORT.md.
| doctrine | label | note |
|---|---|---|
| pricing (intel_pricing_logic), WWP (intel_wwp), positioning (intel_positioning_phrases) | **certified** | cite as certified |
| leverage (intel_leverage_logic), hospitality, analog_premium, perennial, company_of_one | **certified** | cite as certified |
| photo_theory (Sontag/Berger/Freeman) | **certified + conflict_preserved** | 3 lenses, don't flatten taken-vs-made |
| status_psychology, blockbuster_strategy | **certified + conflict_preserved** | de Botton↔Simler; concentration↔long-tail |
| copy doctrine (Hopkins/Schwartz/Ogilvy) | **certified + conflict_preserved** | long-copy↔brevity; max-default↔Ogilvy , contextual |
| decision/systems (Munger, Meadows), offer ($100M), capital-alloc (Outsiders), discovery (Mom Test) | **certified** | cite as certified |
| **hit_mechanics (Hit Makers)** | **source_uncertified** | source MISSING , do NOT cite as final |
| **new_luxury (Trading Up)** | **source_uncertified** | source unextracted |
| **trust_equation (Trusted Advisor)** | **source_uncertified** | .mobi only; PSF is a different certified book |
| 7 Powers (counter-positioning) | **source_uncertified** | no full text |
| ~193 other books | **provisional_chunked** | inform only, label provisional |
RULE: certified → cite freely. conflict_preserved → present BOTH positions, never one forced rule. source_uncertified / provisional → must carry the label; cannot anchor a major decision.
