# OPERATOR NOTE , LOT 00, first clean proof of the production machine (2026-06-04)
> Banked as the first shippable campaign asset. Short, for review. No motion, no layout, no posting, no launch.

## 1. What made 1K fail
The concept was right on the first try (it beat the brutalist proof cell), but the 1k source created two failures at once. The LOT 00 wrist tag did not have enough pixels to render legible text, and the 7-spec export package had to upscale 6 of 7 crops past the source, so the post-production gate returned **REJECT** on `text_legible` + `no_enlarge`. The bottleneck was source resolution, not direction.

## 2. What made 4K pass
One 4K regenerate (3584x4800, 4 credits) of the same concept, changing only the three known misses. At 4K the held tag reads **LOT 00** in serif and the ancestor tags read their climbing numbers (45 / 128 / 203 / 315), the auction-red strings became the only saturated color after grade + color-law, and the three-quarter portrait-sitter stance with the held glove resolved the body signature while the face stayed in lost profile (faceless held). The same gate then returned **SHIP**: all 7 exports no-enlarge OK, text legible, identity withheld, beats source.

## 3. What the post-production layer now proves
The OS no longer just generates images, it produces gated campaign assets. The reference chain is ACTIVE and repeatable: **raw still , 4K source , grade , color-law , export package , post-production gate , SHIP.** Six `os_adobe_*` scripts, 12/12 tests passing, every artifact logged, the gate proven honest because it rejected the under-spec version and shipped the corrected one. "ACTIVE" now has a worked example, not an assertion.

## 4. What still needs to be built later
- **Illustrator/InDesign layout (RED):** turn a passing hero into a titled poster/banner with the masthead in the negative space (Adobe `document_render`). No generation credits.
- **Premiere/AE multi-clip edit (AMBER):** `os_adobe_cut.py` finishes single clips; sequence assembly + titling not built.
- **Adobe-MCP generative escalation (AMBER):** wired and logged, one approval from GREEN; not needed for LOT 00 legibility, kept for optional seamless cleanup.
- **Danger gaps from the audit, still open before any public loop:** offsite backup, `os_privacy_gate.py`, USD cost-rate, live legal stubs, payment path.

## 5. Next approval options (hold until you choose)
- **A. Hold** , LOT 00 banked, review. (current)
- **B. Build the layout layer** (`os_adobe_layout.py` via Adobe document_render) , zero generation spend.
- **C. First LOT 00 motion** , 4s clip then `os_adobe_cut.py` finish. Needs generation approval (~18 cr).
- **D. Close a danger gap** , start the audit's first-10 (backup , privacy gate , cost-rate). Cheap, safety-first.

## Banked asset
- Concept: LOT 00 (THE SITTER), world THE ESTATE OF HER (placeholder names, internal).
- Source: job 706e806e, 3584x4800. Chain SHIP. Run spend 6 of 100 cap. Balance 853.
- Record: `postproduction/lot00_4k_001/PROOF_PACKAGE.md`. Registry: OS_PRODUCTION_REGISTRY.csv (lot00_4k_001, shipped).
