---
name: brand-validation-machine
description: >
  Test-fire a clothing brand concept from raw idea to a demand-validated go/no-go,
  before any inventory spend, using real market data, the founder's taste, a real
  camera (Canon R6 Mark II), and AI for world-building only. Use when the founder
  says "validate a brand idea," "test this clothing concept," "run the validation
  machine," brings a new apparel category or angle to pressure-test, or wants to know
  whether a product idea is worth manufacturing. NOT for an already-validated brand
  that needs execution, and NOT for non-apparel products (the supply and complaint
  logic is apparel-specific). Full system doc:
  /00_COMMAND_CENTER/CLOTHING_BRAND_VALIDATION_MACHINE_2026-06-02.md
metadata:
  type: workflow
---

# Brand Validation Machine

A repeatable system that test-fires clothing brand concepts before inventory spend. The output is a machine you re-point at each new idea, not a single brand. The anti-slop firewall (component 11) runs across every step: garment, fabric, fit, after-wash proof, and faces are ALWAYS shot real on the R6; AI builds world only. Never name the aesthetic out loud.

## Inputs (the intake sheet, locked before anything is built)
Taste anchors + an explicit "not this" list; aesthetic lane (5 words or fewer); silhouettes in/out; price-point intent; customer type by behavior (not demographic); single category; founder constraints (capital ceiling, hours/week, inventory tolerance, fulfillment method); hard "never do this" constraints. Blanks allowed only if marked "resolve in Research."

## Step sequence (idea → data → brand → product → content → page → test → feedback → decision)
1. **Intake** — lock the one-page spec sheet. **[human gate: founder confirms the sheet]**
2. **Data** — market map, complaint ledger (complaints are pre-validated demand), content-format ledger, supply/manufacturing reality. Every number sourced or flagged "could not verify." Tools: WebSearch/WebFetch; test labs over crawler-blocked forums; one live printer quote beats any blog.
3. **Brand angle** — one sentence no competitor can honestly say (competitor-honesty test: if two could say it, sharpen). Plus a rejection list of saturated angles. **[human gate: founder approves the angle]**
4. **Product** — one hero product spec that physically solves the sharpest complaint and is buildable at the target price. Built against the complaint ledger, not aesthetic preference alone.
5. **Name gate** — 8 to 12 candidates through the kill-screen in order: live .com check (Vercel check_domain_availability_and_price), handle availability (flag open), search collision, apparel-class trademark (flag open, USPTO/counsel), pronunciation, memorability, say-it-aloud. Output a shortlist tagged with passed/open screens. Never auto-declare "the name." A name is not good until it survives the gate (the Afterlight rule).
6. **Visual** — real-camera shot list (R6) + AI world plan + a per-run quality-gate sheet. The product-page hero is shot, never generated.
7. **Content** — 5 to 10 winning formats from the ledger + first 20 posts (format · hook · shot note) + a batch plan. Pre-screen cuts with Higgsfield virality_predictor.
8. **Page** — mobile-first waitlist copy first (low friction), then a preorder page (hard signal). One concept, one product, one CTA. Tools: Carrd or Vercel deploy (waitlist); Shopify + PreOrder Now/Timesact (preorder).
9. **Money thresholds** — unit economics + signups/preorders/conversion thresholds, SET BEFORE the test. **[human gate: founder commits to the kill numbers]**
10. **Test** — run traffic + content live.
11. **Feedback** — weekly read, scale the winner, kill the rest, update the learning log.
12. **Decision** — thresholds met → manufacture against deposits; missed → kill or re-angle, keep the machine. **[human gate: the manufacturing spend is always a human call]**

## Default thresholds (tune per run)
Signups-to-continue: ~300 waitlist emails (below = re-angle, do not build commerce). Waitlist→preorder conversion floor: ~10% (below = the page is the problem; fix proof/price, retest once; two misses kills the angle). Preorders-to-manufacture: enough paid deposits to cover the first small run with buffer.

## Hard lines
- The after-wash / proof shot is the most important asset and must be a real, honest measurement. Faking it kills the moat permanently.
- Any AI output that does not beat its real-shot source is rejected (strongest photograph is not the most processed).
- Never publish a guarantee number not measured on the real blank.

## Tools the skill routes to
WebSearch/WebFetch (research); Vercel check_domain_availability_and_price (name gate) + Vercel deploy (waitlist); R6 + Adobe MCP (real capture + finishing); Higgsfield generate_image/generate_video/Soul ID/virality_predictor + Seedream + Nano Banana Pro (world-building, pre-post screening, NEVER the product-page hero); Shopify + preorder app; a unit-economics spreadsheet; TikTok/IG + Shopify analytics (feedback).

## Learning log
Every run appends what won, what died, and the verified numbers (real supplier quotes, real shrink figures, real conversion rates) so the machine compounds and the OS data gaps close as they are filled.


## Outputs
- Locked one-page spec sheet + market map + complaint ledger + supply/manufacturing reality (all numbers sourced or flagged)
- One-sentence brand angle that passes the competitor-honesty test
- Name shortlist (8-12 candidates) with pass/open status across all 8 kill-screens (the Afterlight rule)
- 20-post content plan (format/hook/shot note) + waitlist page + unit economics + threshold commitments
- Receipt: 'Validation machine armed for [concept]: intake locked, angle approved, thresholds committed, test live'

## Gates
- INTAKE GATE (human): founder confirms the one-page spec sheet before anything is built
- ANGLE GATE (human): founder approves the brand angle before visual or content work begins; no competitor can honestly say the same sentence
- KILL-NUMBER GATE (human): founder commits to signup/preorder thresholds (default: 300 waitlist / 10% conversion floor) before traffic runs
- HERO SHOT GATE: product-page hero and after-wash proof must be real R6 shots -- AI world-building is never the hero; any AI output that does not beat its real-shot source is rejected
- APPAREL-ONLY GATE: refuse to run for non-apparel products -- supply chain, complaint logic, and after-wash proof are apparel-specific

## Test
- case: Operator says 'run the validation machine on a gender-neutral linen basics brand under $80'. Skill requests intake sheet, sequences through all 12 steps: market map with sourced data, competitor-honesty-tested angle, name shortlist with 8 screens each, R6 shot list + AI world plan, 20-post content plan pre-screened with virality_predictor, Vercel waitlist deploy, thresholds set and committed by founder at the human gate.
- expected failure: Operator requests brand validation for a SaaS product. Skill refuses: 'Brand Validation Machine is apparel-specific. The supply chain, after-wash proof, and complaint-ledger logic do not apply to non-apparel products.'


## INVOKE WHEN
- Validate this new clothing brand concept before I spend on inventory
- Test this apparel idea through the machine
- Run the validation machine on my streetwear angle
