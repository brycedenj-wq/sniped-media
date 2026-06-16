---
name: sniped-web-builder
description: Plan and write a conversion page (landing / offer / simple site / campaign / service / product drop) in SNIPED voice, doctrine-correct at birth. Use when the user says "build a landing page", "offer page", "service page", "campaign page", "product drop page", "make a website", "web build", or hands a deploy-this brief. This skill plans and writes the page; the vercel:* / figma:* plugins build and deploy it.

---

# SNIPED Web Builder
Turn an offer into a doctrine-gated conversion page: page strategy, section wireframe, in-world copy blocks, design notes, conversion QA. Plans and writes only; deploy via plugins.

## When it fires
- A landing / offer / simple-site / campaign / service / product-drop page is requested.
- Trigger phrases: "build a landing page", "offer page", "service page", "product drop page", "campaign page", "web build", "make a one-pager site".
- NOT for: copy review of existing pages (use sniped-positioning-phrases), pricing-only decisions (use sniped-pricing-decision), or the actual deploy (use vercel:* / figma:* plugins).

## Inputs required
- Offer / page goal (what one action the visitor takes).
- Audience and their core desire (the status psychology · what they want to BE seen as).
- Real proof: testimonials, case results, named clients, before/after, or numbers. (If none, see Ask the human.)
- Confirmed price or price-frame. (If none, see Ask the human.)
- Brand kit: typeface, color, logo, voice notes. (If none, default to the layout_type owned-editorial kit and flag it.)

## Steps (numbered, executable)
1. Load the doctrine at the moment of creation. Run `python3 00_COMMAND_CENTER/scripts/os_doctrine.py load copy` and `python3 00_COMMAND_CENTER/scripts/os_doctrine.py load layout_type`. Inject both packs into your writing context so the page is doctrine-correct at birth (copy pack rules + layout_type pack rules).
2. Identify the offer and the page goal. One page, one job, one CTA. Name the single conversion action in one sentence. (copy pack: one big idea per piece.)
3. Audience + core desire via status psychology. Write the one-line ICP and the status they are buying (what they want to be seen as, not the feature). Pull positioning language with `sniped-positioning-phrases` (phrase bank + 5 failure modes).
4. Hero section. Headline = a complete thought, the 80% of the spend (copy pack, Ogilvy rule), benefit-and-meaning not feature, in the world's voice, no hype, no em-dash. Add one subhead line and the primary CTA. (copy pack rubric: complete_thought, one_big_idea, in_world_voice_not_bible.)
5. Promise. One specific outcome the visitor gets. Concrete noun beats abstract claim (copy pack: specific_not_abstract).
6. Proof. Lay out real testimonials / results / named logos / numbers. Frame trust with `sniped-trust-equation`: raise credibility + reliability + intimacy, lower self-orientation; proof beats claim. If proof is missing, insert a `[NEEDS: real proof]` placeholder and do not invent it.
7. Offer stack. List what they get and the value frame. For the price tier and anchor, route through `sniped-pricing-decision` (3-option architecture, premium-as-insurance, hold the floor). Insert `[NEEDS: confirmed price]` if unconfirmed.
8. Objections. Name the top 3 objections and answer each in one line in-world (no defensiveness, no hype).
9. CTA. One clear primary CTA repeated at hero and page end. Same action, same words. Secondary CTA only if it does not split the decision.
10. Full page section list. Output the ordered section list (hero, promise, proof, offer stack, objections, FAQ if needed, final CTA, footer).
11. Design notes (layout_type pack). Owned editorial kit (Didot/Baskerville register or the supplied brand kit), copy on dark/controlled ground for legible contrast, one masthead + one line + one mark hierarchy, deliberate negative space, no template look, no filler sections.
12. Mobile + clarity check. State the mobile-first stack order, tap-target CTA size, and that the hero headline + CTA read above the fold on a phone.
13. Run the gates (see Quality gate). Then write the proof/receipt block.
14. Hand off to build. Note that `vercel:*` (bootstrap/deploy/env) or `figma:*` (generate-design) plugins build and deploy. This skill outputs the spec; the operator authorizes the deploy. Run `os-quality-gates` (gate 5 legal/identity, gate 7 usefulness, gate 8 completion) before any deploy is crowned, and log a receipt via `00_COMMAND_CENTER/scripts/os_receipt.py` / `os_proof_manifest.py` if this page is a client deliverable.

## Output format (the exact deliverable shape)
1. PAGE STRATEGY: page goal (one sentence), ICP + core desire (one line), the single CTA.
2. SECTION-BY-SECTION WIREFRAME: ordered list (hero -> promise -> proof -> offer stack -> objections -> [FAQ] -> final CTA -> footer), one line of intent per section.
3. COPY BLOCKS: per section, the actual copy (headline, subhead, body, CTA label), in-world voice, no hype, no em-dash. Missing real inputs as `[NEEDS: ...]` placeholders, never invented.
4. DESIGN NOTES: type kit, color discipline (one saturated color max), contrast rule, hierarchy, negative space, mobile stack order.
5. CONVERSION QA CHECKLIST: the pass/fail table from the Quality gate.

## Quality gate (pass/fail)
- copy pack self-check on every headline/CTA: run `python3 00_COMMAND_CENTER/scripts/os_doctrine.py check copy --text "<line>"`. PASS requires complete_thought, one_big_idea (one idea per block), no_generic_hype, no_em_dash. Any FAIL blocks done; fix or rewrite, do not ship.
- Legible contrast: copy never sits illegibly over a bright/busy area (layout_type pack). FAIL = redo ground.
- One clear CTA: exactly one primary action, repeated, same words. Two competing primaries = FAIL.
- Mobile-first: hero headline + CTA above the fold on phone, tap targets large enough. FAIL = restack.
- No filler / not-a-template (layout_type rubric): every section earns its place. FAIL = cut it.

## Proof / receipt (log this)
- Page goal and the single CTA.
- Files used: `00_COMMAND_CENTER/scripts/os_doctrine.py` (copy + layout_type packs), and which of `sniped-positioning-phrases`, `sniped-pricing-decision`, `sniped-trust-equation`, `os-quality-gates` were run.
- Sections built (the ordered list).
- Copy blocks shipped (or `[NEEDS: ...]` placeholders left open).
- Assumptions made (brand kit defaulted? price-frame inferred?).
- Doctrine fired: copy, layout_type (and any pricing/trust packs touched).
- QA result per check: PASS / FAIL.
- Human-approval-needed: list (real proof, confirmed price, brand kit, deploy authorization).
- For a client deliverable: write the receipt via `os_receipt.py` and verify the gate with `os_proof_manifest.py` before "done."

## Ask the human when
- No real proof / testimonials / results exist (do not invent social proof; leave `[NEEDS: real proof]`).
- No confirmed price or price tier (route the frame through `sniped-pricing-decision`, but get the number before shipping).
- No brand kit (typeface / color / logo) and the default owned-editorial kit may not match the brand.
- The page goal or single CTA is ambiguous (one page, one job · ask which action wins).
- A deploy is requested (operator authorizes spend/publish at the boundary, not mid-build).

## Depends on
- `00_COMMAND_CENTER/scripts/os_doctrine.py` · copy pack + layout_type pack (rules, rubric, `load`/`check`).
- `sniped-positioning-phrases` · phrase bank + 5 failure modes for the copy blocks.
- `sniped-pricing-decision` · the offer-stack price tiers and anchor.
- `sniped-trust-equation` · the proof / trust section framing.
- `os-quality-gates` · gate 5 (legal/identity), gate 7 (usefulness), gate 8 (completion) before deploy.
- `os_receipt.py` + `os_proof_manifest.py` · the Stop-hook proof gate for client deliverables.
- `vercel:*` (bootstrap / deploy / env) and `figma:*` (generate-design) plugin skills · they build and deploy the page this skill specifies.

## External-resource gap
- Current vercel:* / figma:* plugin parameter schemas and any 2026 deploy-flow changes are NOT pinned here. Read the live plugin skill (vercel:bootstrap / vercel:deploy / figma:figma-generate-design) at build time for exact tool inputs. Do not block planning on this; resolve it at the build step.

