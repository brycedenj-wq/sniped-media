# CLOTHING BRAND VALIDATION MACHINE

A repeatable system for test-firing clothing brand concepts with data, taste, a real camera, and AI tooling before any inventory spend. The output is a machine you re-point at each new idea, not a single brand.

Register: prices are USD. Domain availability was checked live against the Vercel domain registry during this build (June 2026) and is flagged inline. Trademark, social handle, and search-collision checks are not done here; they are flagged as open human gates. Sourced figures carry a citation; unverified figures carry a flag.

This document has four parts: the machine (Part 1), one full run on the founder inputs (Part 2), what the OS still lacks to run this well (Part 3), and the reusable skill spec plus the first real move (Part 4).

---

# PART 1: THE MACHINE

Twelve components in sequence. Each names what it does, the exact inputs it eats, the exact outputs it produces, and the tools it runs on. Components 1 to 2 are intake and truth. 3 to 6 are construction. 7 to 9 are the test rig. 10 to 12 are the loop, the human gate, and the operating flow.

## 1. INPUT LAYER

**What it does:** Forces every required decision input onto the table before a single asset is made. No construction starts until this sheet is filled. Blanks are allowed but must be marked "unknown, resolve in Research."

**Inputs (the intake sheet):**
- Taste anchors: 1 to 3 reference brands, extracted as a bias not a template (what to steal: restraint, price logic, casting). Plus an explicit "not this" list.
- Aesthetic lane: one named lane in 5 words or fewer.
- Silhouettes: which garment shapes are in and out.
- Price point intent: target retail for the hero unit, pre-research.
- Customer type: who specifically, by behavior not demographic ("people who hunt the perfect white tee," not "men 25 to 40").
- Category: the single product category.
- Founder constraints: capital ceiling, hours/week, inventory tolerance, fulfillment method available.
- Hard constraints: the non-negotiable "never do this" list.

**Outputs:** A one-page locked intake sheet. This is the spec the rest of the machine is held against. If a later component violates the intake, the later component is wrong, not the intake.

**Tools/sources:** Founder interview. No external tools. A discipline gate, not a research gate.

## 2. RESEARCH LAYER

**What it does:** Replaces opinion with verified market data. Maps the category, locks real price bands, finds what sells, what buyers complain about, and what content already performs. Complaint mining is the highest-value output because complaints are pre-validated demand.

**Inputs:** The intake sheet (category, customer type, price intent).

**Outputs (4 artifacts):**
1. **Market map:** named competitors, their hero product, their hero price, why each works, ranked into price bands. Identifies the white space (the band or angle nobody owns).
2. **Complaint ledger:** top buyer complaints ranked by recurrence, decomposed to root cause, with the single sharpest unmet need stated as a sentence in the buyer's own voice.
3. **Content-format ledger:** which short-form formats are actually winning in this category, ranked, with real hook patterns.
4. **Supply/manufacturing reality:** real unit costs for POD vs blanks-plus-decoration vs cut-and-sew, with MOQs and lead times.

**Tools/sources:**
- Market and price bands: brand sites, retail listings, BoF State of Fashion, trade press (Sourcing Journal, Fast Company). WebSearch + WebFetch.
- Complaints: editorial test labs (NBC Select, CNN Underscored, HiConsumption, Reviewed), Amazon reviews, forum threads. Reddit is frequently blocked at the crawler level; when it is, say so and lean on test labs, do not fabricate quotes.
- Content formats: TikTok Shop search terms, IG Reels trend write-ups, creative-agency breakdowns.
- Supply: Printful/Printify catalogs, blank distributors (BlankStyle, S&S, SanMar), cut-and-sew MOQ guides (MakersRow). For final numbers, one live quote from a local printer/relabeler beats any blog.

**Rule:** every number carries a source or a "could not verify" flag. A fabricated stat poisons every downstream decision.

## 3. BRAND ANGLE LAYER

**What it does:** Compresses the research into one sharp positioning sentence that no competitor can honestly say. The angle is not a slogan, it is a claim with a moat. It must pass the competitor-honesty test: if a competitor could say it too without lying, it is not yours.

**Inputs:** Market map (the white space), complaint ledger (the unmet need), taste anchors.

**Outputs:** One positioning sentence. Plus a one-line "why no one else can say this" justification. Plus an explicit rejection list of dead angles the research proved saturated or commoditized.

**Tools/sources:** Synthesis. The test is logical, not tooled: take the sentence, hand it to each mapped competitor, check if they could claim it. If two or more could, sharpen until only you can.

## 4. PRODUCT LAYER

**What it does:** Picks one hero product (or a tiny 2 to 3 piece capsule) that is easy to mock up, validate, fulfill, and that passes the taste test. One perfected unit beats a catalog: it reduces SKU risk, sharpens the story, and concentrates all validation signal on one object.

**Inputs:** Brand angle, complaint ledger (the product must physically solve the sharpest complaint), supply reality (must be buildable at the target price), taste anchors.

**Outputs:** Hero product spec: garment, fabric weight (GSM/oz), fit, the specific complaint it solves, the blank or pattern it is built on, target landed cost, target retail. Plus the taste rationale in one paragraph.

**Tools/sources:** Blank spec sheets (Comfort Colors, LA Apparel, AS Colour, Bella+Canvas), the supply reality artifact from Research. The product is chosen against the complaint ledger, not against aesthetic preference alone.

## 5. NAME GATE

**What it does:** Generates name candidates that fit the taste, then runs each through a kill-screen. Most names die here. The gate is sequential: a name must clear every screen or it is cut. Names that pass are still flagged "candidate," never "available," until the legal and handle checks are done by a human.

**Inputs:** Taste anchors, brand angle, lane.

**The kill-screen (in order):**
1. `.com` availability (live check, registry API).
2. Social handle availability (IG, TikTok): flagged as open, requires manual check.
3. Search collision (does it fight an existing strong result).
4. Brand/trademark conflict in apparel class: flagged as open, requires USPTO/counsel check.
5. Pronunciation (one unambiguous way to say it).
6. Memorability (recallable after one hearing).
7. Say-it-aloud test (works in a voiceover without spelling it).

**Outputs:** 8 to 12 candidates, each tagged with which screens it passed and which are still open. No name is declared "the name" inside the machine. The machine hands a shortlist to the human gate.

**Tools/sources:** Vercel `check_domain_availability_and_price` for live `.com` data. WebSearch for collision. USPTO TESS and handle checks flagged for the human, not auto-run.

## 6. VISUAL LAYER

**What it does:** Builds the brand's visual world so it reads as a real brand, not "AI made it." The tell of AI merch is generic graphics with no reason to exist, plastic lighting, and no consistent world. The fix is a real camera on the product and a withheld, consistent campaign world around it.

**Inputs:** Brand angle, lane, casting intent, palette intent, taste anchors.

**Outputs:**
- Logo + wordmark direction (feel, not final art): typographic register, weight, what it must avoid.
- Palette: a narrow, related-tone neutral set. No more than 4 to 5 values.
- Campaign world: the recurring environment and mood the brand lives in.
- Casting direction: who is in frame and why (real people in a real world beats aspirational models).
- Product-page assets: the shot list (hero, fabric macro, fit-on-body, after-wash proof).
- Motion concepts: 2 to 3 short motion ideas for the campaign.

**Tools/sources:**
- Real photography (the R6 Mark II): the product itself, fabric macro, fit-on-body, and the after-wash proof shots. This is the quality signal and the moat. POD and AI cannot fake garment hand on camera.
- AI for world-construction only: campaign environments, motion, mood plates, landing-page hero backgrounds. Higgsfield (generate_image / generate_video / Soul ID for identity-consistent faces), Seedream, Nano Banana Pro, Firefly. Adobe MCP for grading, grain, and finishing.
- Hard line: identity and garment are shot real; the world can be AI. Never AI-generate the product itself for a product page.

## 7. CONTENT ENGINE

**What it does:** Turns the content-format ledger into a batch of ready-to-shoot posts. Picks 5 to 10 formats already performing in the category and writes the first 20 posts as a concrete list with hooks. Start from what works, do not invent formats.

**Inputs:** Content-format ledger (Research), brand angle, hero product, visual world.

**Outputs:**
- The chosen formats (5 to 10), each with why it fits this product.
- First 20 posts as a batch list: format + hook + 1-line shot note for each.
- A batching plan (shoot multiple posts per format in one session).

**Tools/sources:** R6 for fit checks, fabric tests, real-world wear. Phone for raw mirror/native trust content (raw beats polished in this category). AI for any campaign-world cutaways. Higgsfield virality_predictor to pre-screen a cut before posting.

## 8. FUNNEL

**What it does:** Builds the mobile-first test page that validates demand before inventory. One concept, one product, one CTA. The page is the experiment. It either collects emails (waitlist, low friction, soft signal) or collects deposits (preorder, high friction, hard signal). Hard signal is the one that gates manufacturing.

**Inputs:** Brand angle, hero product, visual world, money-path thresholds.

**Outputs:** A landing/preorder page spec with copy: headline, subhead, the one CTA, the proof section (the after-state claim with measurements), the FAQ that kills purchase objections, the founder/world section. Plus the capture mechanism (email or deposit).

**Tools/sources:**
- Waitlist (soft): Carrd or a Vercel-deployed page plus email capture. Validates interest without taking money.
- Preorder (hard): Shopify plus a vetted preorder app. Verified options: PreOrder Now (WOD) for simple drop validation with partial payments and per-variant limits; Timesact for staged drops; STOQ for back-in-stock/waitlist capture without payment; Purple Dot for larger programs. Preorder revenue funds the production run, converting inventory risk into financed, demand-proven orders.
- Build/deploy: Vercel for a custom page, Shopify for the commerce path.

## 9. MONEY PATH

**What it does:** Sets the numerical thresholds that turn the test into a go/no-go, and separates the realistic profit path from fantasy. Decisions are made on thresholds set before the test, not on feelings after it.

**Inputs:** Supply reality (unit cost), target retail, funnel results.

**Outputs:**
- Unit economics: landed cost, retail, gross margin per unit, contribution after realistic fulfillment and payment-processing drag.
- Thresholds (set before launch):
  - Signups-to-continue: minimum waitlist size to justify building the preorder page.
  - Preorders-to-manufacture: minimum paid deposits to place the run (sized to cover the MOQ run cost).
  - Conversion floor: minimum waitlist-to-preorder rate below which the angle is wrong, not the traffic.
- The realistic first profit path vs the fantasy. Fantasy is named explicitly so it stops getting modeled.

**Tools/sources:** The supply artifact for costs. The funnel for actuals. A simple spreadsheet. No tool magic; the discipline is pre-committing the thresholds.

## 10. FEEDBACK LOOP

**What it does:** Post, measure, learn, iterate. Double down on the format that wins, kill the rest fast. The loop runs weekly. It is ruthless: a format that does not produce signal in its allotted reps is cut, not "given more time."

**Inputs:** Content-engine posts live, funnel analytics, format-level performance.

**Outputs:** A weekly read: which format drove the most qualified signal (saves, profile visits, waitlist clicks, preorders), which to scale, which to kill. An updated post batch weighted toward the winner. A running learning log so the machine compounds across runs, not just within one.

**Tools/sources:** TikTok/IG native analytics, the funnel's analytics (GA or Shopify), Higgsfield virality_predictor for pre-post screening. The decision rule is set in advance: scale the top format, cut anything below the floor after N reps.

## 11. HUMAN QUALITY GATE

**What it does:** Defines exactly where a human and the real camera override AI, and where AI can run without quality dropping. This is the anti-slop firewall. It is component-specific every run, but the standing rules hold across runs.

**Standing rules:**
- **Shot real (R6, non-negotiable):** the garment itself, fabric macro, fit-on-body, the after-wash proof, real faces on real people. Garment hand and skin texture are the quality signal; AI cannot fake them and the audience reads the fake instantly.
- **Taste overrides AI:** any output that does not beat its source visually is rejected, even if it completes the task. A failed AI cleanup is worse than honest real context. The strongest image is not the most processed one.
- **Real designer/manufacturer steps in:** at the cut-and-sew ceiling (pattern, fit, neck construction, finishing) and at relabel/packaging. POD and AI cannot deliver the finishing that registers as "quality."
- **AI handles without quality drop:** campaign-world environments, motion plates, landing-page backgrounds, mood, grading, grain, and identity-consistent faces for world-building shots (not for the product page hero). Copy drafts, format ideation, research synthesis.

**Outputs:** A per-run gate sheet: a two-column list, "must be real" vs "AI is fine," specific to that brand's product and claims.

## 12. OPERATING SYSTEM (the reusable flow)

The full loop, the thing you re-run for every new idea:

```
NEW IDEA
  → INTAKE (1)         lock the spec sheet
  → DATA (2)           market map · complaint ledger · format ledger · supply reality
  → BRAND ANGLE (3)    one sentence no competitor can honestly say
  → PRODUCT (4)        one hero unit that solves the sharpest complaint
  → NAME GATE (5)      generate · domain-gate · flag the open legal/handle checks
  → VISUAL (6)         real camera on product, AI on world
  → CONTENT (7)        steal winning formats · batch first 20 posts
  → PAGE (8)           one concept, one product, one CTA, mobile-first
  → MONEY THRESHOLDS (9)  set go/no-go numbers BEFORE the test
  → TEST              run traffic to the page, run the content
  → FEEDBACK (10)     scale the winner, kill the rest, weekly
  → DECISION          threshold met? → manufacture against deposits
                      threshold missed? → kill or re-angle, keep the machine
  (HUMAN GATE (11) runs across every step as the quality firewall)
```

Decision logic at the gate: if signups clear the bar, build the preorder page. If deposits clear the bar, place the run financed by deposits. If either misses, you spent on traffic and a page, not on inventory. The brand may die; the machine does not. You re-point it at the next idea with the learning log intact.

---

# PART 2: THE FIRST RUN

Run on the founder inputs (Uniqlo bias, FUTURE UNIFORM lane, elevated basics, R6 + AI, test fast spend little) against the real research corpus.

## The white space (from Research, before angle)

The $35 to $50 accessible-elevated tee band is a knife fight where everyone says the same thing: premium materials, no markup, transparency, timeless. Three verified truths define the gap:
1. Transparency-as-positioning is dead. Everlane proved it commoditizes (sold to a strategic buyer reportedly near $100M, down from a roughly $600M valuation, killed by CAC and a market that stopped paying a premium for the story). Asket already owns the rigorous version.
2. Pure-DTC story brands die on CAC. The survivors (Buck Mason, ALD) have a real-world surface: retail, drops, or culture.
3. The middle has no point of view. COS/Arket have a house look but no narrative; Quince/Italic have price but no identity; ALD/Asket have identity but sit at $58 to $65.

Separately, the complaint research found the sharpest unmet need in the category, and it is a product gap, not a story gap:

> "I want a tee I can throw in a normal wash and dryer and trust that it will not turn see-through, will not pill, and will not lose length and turn into a crop top. I will pay for that certainty. I keep not getting it."

Sheerness is the most-repeated complaint. Length-shrinkage is the most under-served, because everyone optimizes for hand-feel at unboxing and nobody guarantees how it looks after 20 washes. The open lane: sell the after-state, in writing, with the measurements.

## The brand angle (one sentence)

**"The tee engineered for how it looks after twenty washes, not how it feels in the box: opaque, square, and the exact same length you bought, guaranteed in writing with the measurements."**

Why no competitor can honestly say it: COS, Arket, Buck Mason, Everlane, and Kotn all sell the unboxing feel and a material story. Asket sells rigor and permanence but frames it as cost-transparency and lifetime repair, not a written dimensional-stability guarantee. ALD sells culture, not durability. Quince and Italic sell price. Nobody in the band warranties the after-state with published before-and-after measurements. The claim is falsifiable, which is exactly why it is ownable: it forces a real product spec (garment-dyed, pre-shrunk, heavyweight, opaque) and dares competitors to match it. Most will not, because most cannot back it.

Dead angles rejected (research-proven saturated): radical transparency, sustainability-as-positioning, "luxury without the markup," heritage/lineage cosplay, loud logos.

## The hero product (one product, with specs)

**The Field Tee.** A single perfected heavyweight tee. Not a range.

| Spec | Value |
|---|---|
| Weight | ~6.5 oz / 220 GSM |
| Fabric | 100% combed/ring-spun cotton, garment-dyed, enzyme-washed (shrink taken out before you own it) |
| Fit | Clean, intentional cut. Neither boxy-tent nor cropped. |
| Opacity | Opaque in white (the hardest test and the most-complained-about failure) |
| Palette | Neutral only: ecru, bone, fog grey, navy, black |
| Decoration | Water-based or discharge ink only, so any mark sits in the fabric, not on it (DTG/DTF on top is the AI-merch tell) |
| Finishing | Relabeled, considered packaging |
| Build path (primary) | LA Apparel 1801 blank (6.5 oz / 220 GSM, garment/pigment-dyed, made in LA, from ~$9.46/unit) |
| Build path (alternate) | AS Colour Heavy Faded 5082 (6.5 oz combed, est. ~$7 to $9 blank, not confirmed on a live tier sheet) |
| Target landed cost | ~$14 to $22/unit, small batch, decorated + relabeled + finished |
| Target retail | $48 |

**The complaint it solves:** all three top complaints at once. Sheerness (#1 disqualifier) via opacity at 220 GSM. Length-shrinkage (most under-served) via garment-dye + enzyme-wash + a published after-wash measurement. Pilling/price-betrayal via heavyweight combed cotton. The product is the angle made physical.

**Taste rationale:** Passes the FUTURE UNIFORM filter cleanly. It is Uniqlo's LifeWear bias (simple, useful, quality-feeling, wearable-often, no fake luxury) extracted, not copied, then sharpened with one defensible engineering claim and an ALD-grade campaign world on top. The garment is quiet; the campaign carries the heat. No graphic with no reason to exist. The only mark is a small functional spec stamp (GSM and wash count), which earns its place.

## Name candidates (candidates only, `.com` checked live, handles/trademark NOT checked)

Live-checked against the `.com` registry during this build. Social handles, search collision, and apparel-class trademark are still open and must be cleared by a human before any name is locked.

| # | Name | Domain | Status | Note |
|---|---|---|---|---|
| 1 | SQUARE AFTER | squareafter.com | available, $11.25 | Holds shape + after-wash promise. On-claim, says-aloud clean. |
| 2 | HOLDS LINE | holdsline.com | available, $11.25 | Keeps length and shape. Confident, restrained. |
| 3 | TWENTY WASH | twentywash.com | available, $11.25 | Names the 20-wash proof directly. Literal, a little blunt. |
| 4 | STANDARD ISSUE | standardissue.com taken; wearstandardissue.com available, $11.25 | rides a longer domain | Strong lane fit; common phrase, high trademark-collision risk, check carefully. |
| 5 | THE FIELD TEE | thefieldtee.com | available, $11.25 | Doubles as the product name. Quiet, uniform-coded. |
| 6 | WEAR UNIFORM | wearuniform.co | available, $17.99 (`.co`) | On-lane but `.co` is a compromise; only if no stronger `.com` clears. |
| 7 | BASIS STANDARD | basisstandard.com | available, $11.25 | Reads as a quality benchmark; slightly corporate, test aloud. |
| 8 | NORTH BASIS | northbasis.com | taken | Cut unless an alternate TLD is acceptable. |
| 9 | SQUARE (wordmark) | bare `.com` taken | candidate only | Needs a modified domain that reads well. |
| 10 | TRUE AFTER | trueafter.com | taken | Cut. |
| 11 | PLAIN GOODS | plaingoods.com | taken | Cut. |
| 12 | FIELD STANDARD | not yet checked | gate next | Strong lane fit (uniform + benchmark). Check before use. |

**Shortlist to the human gate** (cleared `.com`, on-taste, say-aloud clean): **SQUARE AFTER, HOLDS LINE, THE FIELD TEE.** All three still need handle + trademark clearance before locking.

## The visual direction

Pulls from the verified FUTURE UNIFORM research (The Row = withhold, ALD = real place beats borrowed heritage, Toteme = palette + casting restraint). Never name the aesthetic out loud.

- **Logo/wordmark feel:** quiet, typographic, no icon doing decorative work. The only motif is a functional spec mark (e.g. "220 / 20" for GSM and wash-count) used sparingly, like a stamp. Borrow The Row's blank-page restraint: wordmark small, lots of negative space. Avoid any mark that reads as streetwear graphic.
- **Palette:** narrow related-tone neutrals only. Ecru, bone, fog grey, deep navy, black. No teal/orange, no statement color. Maps to the locked Adobe Neutral restraint lane. Neutrals layered in related tones (Toteme discipline), not contrasted.
- **Campaign world:** a closed, slightly-withheld world, not a borrowed class. One consistent environment (concrete, daylight, a real city block, a plain room with one window). Status reads as "something precise is happening here," not "I dressed up rich."
- **Casting:** real people who already belong to the world, not aspirational models auditioning to enter it. Candid, minimal styling, natural posture. Reject the staged stealth-wealth pose; that is the tried-too-hard tell that kills the lane.
- **Photography (the R6 moat):** natural/available light, polished without looking staged. The after-wash proof shot is the signature product image: the same tee, day one vs after 20 washes, laid flat with a ruler in frame. That single honest shot does more brand work than any campaign render, because it makes the falsifiable claim visible. Film-grain/halation is associated with this lane but came from photographer/preset sources, not the named brands' own campaigns, so treat grain as an optional finishing technique, not gospel.
- **Product-page assets:** hero (tee on body, daylight), fabric macro (weave + opacity hold-to-light), fit-on-body in 2 to 3 real settings, and the after-wash measurement proof. Adobe MCP for grade/grain/finish.
- **Motion concepts:** (a) hold-to-light opacity test, slow and quiet; (b) the stretch-and-recover pull test in one continuous take; (c) the after-wash reveal, ruler on the day-one tee cut to ruler on the 20-wash tee, same length. All three are product-truth motion, not vibe motion.

Human gate on visuals: the tee, the fabric macro, the fit-on-body, the after-wash proof, and the faces are shot real on the R6. AI (Higgsfield/Seedream/Nano Banana, graded in Adobe) builds only the campaign-world cutaways and landing-page backgrounds. The product page hero is never AI-generated.

## The content engine

Formats chosen from the verified content-format ledger (what already wins for clean basics), mapped to the product:

1. **Fabric/quality test** (the spine, because the differentiator is the cloth and the claim).
2. **The perfect-white-tee hunt** (a real recurring search behavior; be the answer at the end of it).
3. **Fit check / fit-and-movement** (reduces fit uncertainty, the #2 complaint).
4. **One tee, multiple ways** (proves versatility, drives saves).
5. **Founder POV / build-in-public** (trust + belonging; one-product origin).
6. **ASMR fold / pack-an-order** (retention format, quality-control signal).

### First 20 posts (format · hook · shot note)

1. Fabric test · "Stop buying tees you can see through." · hold-to-light opacity test, daylight, R6.
2. Fabric test · "This is what 220 GSM actually feels like." · macro weave + hand, slow pan.
3. After-wash proof · "Watch what happens after 20 washes." · ruler on day-one vs 20-wash, same length.
4. White-tee hunt · "The white tee search is over." · the one tee on body, clean room.
5. White-tee hunt · "I tested 7 white tees so you don't have to." · contenders on table, ours last.
6. Fit check · "I finally found a tee that doesn't go see-through." · fit + movement, street.
7. Fit check · "POV: you stop buying cheap basics." · real body, natural light, no styling.
8. Fabric test · "Watch it hold to the light." · backlit opacity hold, wait-for-it payoff.
9. After-wash proof · "Width fine, length gone? Not this one." · names the complaint, measurement.
10. One tee, multiple ways · "One tee, five outfits." · setup → reveal → full look, neutral palette.
11. One tee, multiple ways · "If you only own one tee, style it like this." · 3 looks, real settings.
12. Founder POV · "Day 1 of building the only basics brand I'd actually wear." · workspace, blanks in hand.
13. Founder POV · "I got tired of tees that turn into crop tops. So I'm fixing it." · founder voice, the problem.
14. Fabric test · "The $12 three-pack vs this. Hold both to the light." · side-by-side opacity.
15. Fit check · "This is how it actually looks day three, no iron." · real-world wear, candid.
16. After-wash proof · "I'll put the measurements in writing. Here they are." · the guarantee on screen.
17. White-tee hunt · "Why this one and not the cheap one." · the spec, plainly.
18. ASMR pack · "Pack a Field Tee order with me." · slow fold, tissue, label, quiet.
19. One tee, multiple ways · "Save this for the next time you say you have nothing to wear." · save-bait, looks.
20. Founder POV · "POV: the first run, financed by your preorders." · the preorder model, honest.

Cross-format rules from the research, enforced: hook in the first 2 to 3 seconds with first-frame text; 15 to 30 seconds; raw mirror trust beats studio polish; problem-named and result-tease hooks over brand-speak. Vendor stats ("authentic ~60% better," "problem/solution ~2x") are directional, not audited, used as signal only. Pre-screen cuts with Higgsfield virality_predictor before posting.

Batch plan: shoot formats 1 to 3 and 8/14 (all fabric/proof) in one R6 session; formats 6/7/15 (fit) in one street session; 10/11/19 (styling) in one session; founder POV native on phone.

## The funnel (actual copy)

Mobile-first. One concept (after-state guarantee), one product (the Field Tee), one CTA. Two-stage: waitlist first (soft signal, low friction), then a preorder page (hard signal, gates the run).

**Stage 1 waitlist page** (Carrd or a Vercel-deployed page, email capture):

- Headline: **The tee that holds its shape after 20 washes.**
- Subhead: Opaque. Square. The exact length you bought. In writing, with the measurements.
- One CTA: **Get the drop + the guarantee →** (email field, single button).
- Proof strip: the day-one vs 20-wash measurement photo.
- One line of world: Made in LA. 220 GSM. Enzyme-washed and pre-shrunk before it ships.
- No catalog, no nav, no second product.

**Stage 2 preorder page** (Shopify + PreOrder Now or Timesact, partial or full payment, ship-by date):

- Same headline and proof, plus the written guarantee stated as a spec: "Measured at purchase and after 20 home washes. If it loses more than [X] in length, we replace it." (Fill X from the blank's tested shrink. Do not publish a number you have not measured.)
- FAQ that kills objections:
  - Will it shrink? No. Here is the measurement.
  - Is the white see-through? No. Here is the hold-to-light.
  - When does it ship? [date].
  - Why preorder? The run is financed by preorders. Honest framing, no scarcity theater.
- Founder/world section: the one-product origin, plain.
- One CTA: **Preorder the Field Tee →**, with a deposit option.

Copy stays in the operator register: plain, declarative, no hype, no em-dashes, no "luxury" said out loud.

## The money path (real numbers, with a clear continue/kill threshold)

**Unit economics (from the verified supply research):**

| Line | Amount |
|---|---|
| Blank (LA Apparel 1801) | ~$9.46/unit small wholesale (AS Colour alt est. ~$7 to $9, not confirmed) |
| Decoration (water-based/discharge, 1 to 2 color) | ~$3 to $7/unit, low end for the spec mark |
| Relabel | ~$1 to $2.50/unit |
| Hem tag / woven label / packaging | ~$1 to $3/unit |
| **Realistic all-in landed cost** | **~$14 to $22/unit** (50 to 300 units), mid case ~$18 |
| **Retail** | **$48** (top of the $35 to $50 band, below ALD's $58 on purpose) |
| Gross margin at $48 / $18 landed | **~$30, ~62%** |
| After ~3% processing + realistic fulfillment | contribution ~$26 to $28/unit |

(Decoration, relabel, and packaging adders are industry ranges, not a single sourced quote. Get a firm number from one LA printer before committing.)

**Thresholds (set before launch, not after):**

| Gate | Threshold | Meaning |
|---|---|---|
| Signups-to-continue | **300 waitlist emails** | Below this, the angle is not pulling. Re-angle before building Shopify. |
| Preorders-to-manufacture | **~40 paid preorders** | Covers a 50-unit run (~$900 at ~$18 landed) at deposit + balance, with buffer. |
| Conversion floor | **waitlist→preorder ≥ ~10%** | Below this, the price or the proof is not landing, not the traffic. Fix the page before buying reach. |

**Continue/kill, stated plainly:**
- **Below 300 signups:** kill or re-angle. Do not build the commerce page.
- **300+ signups but below 10% preorder conversion:** the page is the problem, not the idea. Fix proof/price, retest once. Two misses kills the angle.
- **300+ signups and 40+ preorders at 10%+:** continue. Place the financed run.

**The realistic first profit path:** ~300 signups → ~40+ preorders at $48 = ~$1,920 in preorder revenue funding a ~$900 run → first run ships → roughly $1,000 gross contribution on run one, with the page, the content batch, and the after-wash proof asset already built and reusable. Run two prices the next batch against a warm list and a proven format. This is the Buck Mason/ALD lesson applied small: a real product surface and a community that does the distribution, not paid-CAC dependence.

**The fantasy (named so it stops getting modeled):** ordering a 300+ unit cut-and-sew run before validation (50 to 100 units x ~$25 = $1,250 to $2,500 per style committed before a single sale, plus sampling weeks and cost). Cut-and-sew is the taste ceiling; you earn your way there after preorders prove demand, not before. Also fantasy: assuming organic reach replaces a funnel, or that transparency/sustainability copy converts (the research proved it commoditized and CAC-fatal).

## The human quality gate for this brand

| Must be real (R6 + human + manufacturer) | AI is fine (no quality drop) |
|---|---|
| The tee itself, on camera | Campaign-world environments and cutaways |
| Fabric macro (weave, opacity hold-to-light) | Landing-page hero backgrounds |
| Fit-on-body in real settings | Motion mood plates and transitions |
| The after-wash measurement proof shot | Color grade, grain, finishing (Adobe MCP) |
| Real faces, real people, candid | Identity-consistent faces for world-building only (Higgsfield Soul ID), never the product page |
| Pattern, fit, neck construction, relabel, packaging (real manufacturer at the cut-and-sew step) | Copy drafts, format ideation, research synthesis |

Hard lines specific to this brand:
- The after-wash proof shot is the most important asset in the brand and must be a real, honest measurement, never staged or AI'd. The entire angle is falsifiable; faking the proof kills the moat permanently.
- The product page hero is shot, never generated. The garment hand is the quality signal; AI fabric reads as fake to this exact buyer.
- Any AI output that does not beat its real-shot source is rejected. Honest studio context beats a failed AI cleanup.
- Never name the aesthetic. No "quiet luxury," "old money," "elevated." The restraint shows; it is not announced.

**Open gates before anything ships (handed to the human, not auto-resolved):** social handle availability (IG/TikTok) for the shortlist names; apparel-class trademark search (USPTO TESS or counsel) for SQUARE AFTER / HOLDS LINE / THE FIELD TEE; and one live quote from an LA printer/relabeler to lock the real landed cost and the publishable shrink number for the guarantee. Reddit complaint quotes could not be pulled directly (crawler-blocked in the source research); the complaint ranking rests on editorial test labs that corroborate each other tightly on the top three failures.

---

# PART 3: OS GAPS, WHAT IS MISSING

The machine ran, but it ran on a thin data floor. Several components leaned on industry ranges and a single research pass rather than owned, verified data the OS can reuse across runs. Stated plainly: here is what the OS still lacks to run this machine well, and exactly what to add next, in priority order.

**P0: Supplier and manufacturing data (the biggest hole).** The entire money path rests on decoration, relabel, and packaging numbers that are ranges from blogs, not quotes. There is no owned supplier table in the OS. The guarantee number (max length loss after 20 washes) cannot be published until a real garment is washed and measured. Add next:
- A live quote from 1 to 2 LA printers/relabelers for the 1801 blank at 50/100/150 units, decoration included.
- A vetted-vendor table in the OS: blank source, decorator, relabeler, packaging, each with real per-unit cost, MOQ, lead time, contact.
- A washed-and-measured shrink test on the actual 1801 blank to set the publishable [X] in the guarantee. Without this, the brand's core claim is unbacked.

**P1: POD / Shopify / preorder-app operating knowledge.** The funnel names Shopify + PreOrder Now/Timesact but the OS has no captured how-to: app setup, partial-payment config, per-variant limits, ship-by handling, the deposit-to-balance flow. This is a known-unknown that will cost a day of fumbling at launch. Add next: a short Shopify-preorder runbook (app chosen, settings, deposit mechanics, the exact go-live checklist), captured the first time it is built so run two is fast.

**P2: Customer research that is first-party, not inferred.** The complaint ledger is strong but built from editorial test labs because Reddit was crawler-blocked. The sharpest-complaint quote is synthesized, not a captured real voice. Add next: 10 to 20 real buyer quotes from accessible sources (YouTube tee-review comments, Amazon/retail reviews, any reachable forum), stored verbatim with source, so the angle rests on real language. Also a 5-question pre-launch survey to the first waitlist signups to confirm the after-state claim is the true hook.

**P3: Trend and search-demand data.** The content-format ledger and the "white-tee hunt" behavior are asserted as real but not quantified. There is no search-volume or trend pull in the OS for this category. Add next: a Semrush/keyword pull on "best white t-shirt," "tshirt see through," "tshirt shrinks length," and the format terms, to size the actual demand behind the angle and rank the content formats by real interest, not assertion.

**P4: Fashion brand case-study library.** The run cites Everlane, Buck Mason, ALD, Asket, COS as decided facts, but the OS has no durable case-study file on why each lived or died (CAC, channel, drop cadence, retail surface). Each new run re-derives this. Add next: a one-page-per-brand case file (positioning, channel, what worked, what killed or saved them, the lesson), so brand-angle work in future runs pulls from an owned library instead of re-researching.

**P5: A reusable supply-cost and unit-economics template.** The money path was assembled by hand. Add next: a standing spreadsheet (blank + decoration + relabel + packaging + processing + fulfillment → landed cost → margin → thresholds) the machine fills in every run, so unit economics are a fill-in, not a rebuild.

Priority order to act on: P0 (supplier quote + shrink test) unblocks the guarantee and the real numbers and is the gate on everything downstream. P1 (Shopify runbook) is needed the moment 300 signups hit. P2 to P5 raise quality and speed of future runs but do not block this one.

---

# PART 4: THE SKILL SPEC

Define the machine as a reusable OS skill so it can be invoked, not rebuilt, each time.

**Name:** `brand-validation-machine`

**One-line description:** Test-fire a clothing brand concept from raw idea to a demand-validated go/no-go, before any inventory spend, using data, a real camera, and AI for world-building only.

**Trigger:** Invoke when the founder says "validate a brand idea," "test this clothing concept," "run the validation machine," brings a new apparel category/angle to pressure-test, or wants to know whether a product idea is worth manufacturing. Not for: an already-validated brand needing execution, or non-apparel products (the supply and complaint logic is apparel-specific).

**Inputs (the intake sheet, component 1):** taste anchors + "not this" list; aesthetic lane (≤5 words); silhouettes in/out; price-point intent; customer type by behavior; single category; founder constraints (capital ceiling, hours/week, inventory tolerance, fulfillment method); hard "never do this" constraints. Blanks allowed if marked "resolve in Research."

**Step sequence (idea → data → brand → product → content → page → test → feedback → decision):**
1. **Intake** lock the one-page spec sheet. *(human gate: founder confirms the sheet)*
2. **Data** produce market map, complaint ledger, content-format ledger, supply reality. Every number sourced or flagged.
3. **Brand angle** one sentence no competitor can honestly say + rejection list. *(human gate: founder picks/approves the angle)*
4. **Product** one hero spec that physically solves the sharpest complaint, buildable at target price.
5. **Name gate** 8 to 12 candidates, live `.com` check, flag handle/trademark as open. Output a shortlist.
6. **Visual** real-camera shot list + AI world plan + per-run quality gate sheet.
7. **Content** 5 to 10 winning formats + first 20 posts (format · hook · shot note) + batch plan.
8. **Page** mobile-first waitlist copy, then preorder page copy + capture mechanism.
9. **Money thresholds** unit economics + signups/preorders/conversion thresholds, set before the test. *(human gate: founder commits to the kill numbers)*
10. **Test** run traffic + content live.
11. **Feedback** weekly read, scale the winner, kill the rest, update the learning log.
12. **Decision** thresholds met → manufacture against deposits; missed → kill or re-angle, keep the machine. *(human gate: founder makes the go/no-go and the manufacturing spend)*

The human quality gate (component 11) runs across every step as the anti-slop firewall: garment, fabric, fit, after-wash proof, and faces are always real; AI builds world only.

**Outputs:** locked intake sheet; 4 research artifacts; one brand angle + rejection list; one hero product spec; name shortlist with domain status and open flags; visual direction + shot list + quality gate sheet; 20-post batch; waitlist + preorder page copy; unit economics + pre-committed thresholds; weekly feedback read + learning log; a final go/no-go.

**Human gates (the points where the machine stops and waits):**
- After Intake: founder confirms the spec sheet.
- After Brand angle: founder approves the one sentence.
- After Money thresholds: founder commits to the kill numbers before any traffic.
- Name lock: handle + trademark cleared by a human, never auto-declared.
- Supplier lock: one live quote + a real shrink measurement before publishing the guarantee.
- Final decision: the manufacturing spend is always a human call.

**Tools the skill routes to:** WebSearch/WebFetch (research); Vercel `check_domain_availability_and_price` (name gate); R6 + Adobe MCP (real capture + finishing); Higgsfield generate_image/generate_video/Soul ID/virality_predictor + Seedream + Nano Banana Pro (world-building, pre-post screening); Carrd or Vercel deploy (waitlist); Shopify + PreOrder Now/Timesact (preorder); a unit-economics spreadsheet; TikTok/IG + GA/Shopify analytics (feedback).

**Learning log:** every run appends what won, what died, and the verified numbers (real supplier quotes, real shrink figures, real conversion rates) so the machine compounds across runs and Part 3's gaps close permanently as they are filled.

---

# THE FIRST REAL MOVE

Call one LA printer/relabeler this week and get a live quote on the LA Apparel 1801 blank at 50, 100, and 150 units with a 1 to 2 color water-based or discharge print, relabel included. In the same order, buy one or two 1801 blanks, wash and dry them 20 times on a normal home cycle, and measure the length loss. That single quote plus that single shrink number unblock the real money path and set the publishable [X] in the guarantee, which is the entire moat. Everything else in this run is ready to move the moment those two numbers exist.
