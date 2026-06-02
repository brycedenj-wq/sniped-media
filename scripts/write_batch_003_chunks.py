#!/usr/bin/env python3
"""
BATCH_003 chunking · Tier 2 canon books
Output: 01_KNOWLEDGE_BASE/batches/BATCH_003_CHUNKS.jsonl

Modeled on write_batch_002_chunks.py. Same schema. Each chunk is a self-contained
doctrine principle with sniped_relevance, direct quotes, and provenance.
"""

import json
from pathlib import Path

OUT = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "BATCH_003_CHUNKS.jsonl"
OUT.parent.mkdir(parents=True, exist_ok=True)

BATCH = "BATCH_003_TIER_2_CANON_BOOKS"
CHUNKS = []


def add(*, source_title, source_file, author, domain, concept,
        summary, usable_principle, sniped_relevance,
        direct_quotes=None, tags=None):
    cid = f"batch-003-chunk-{len(CHUNKS)+1:03d}"
    CHUNKS.append({
        "chunk_id": cid,
        "batch_id": BATCH,
        "source_title": source_title,
        "source_file": source_file,
        "author": author,
        "domain": domain,
        "concept": concept,
        "summary": summary.strip(),
        "usable_principle": usable_principle.strip(),
        "sniped_relevance": sniped_relevance.strip(),
        "direct_quotes": direct_quotes or [],
        "tags": tags or [],
    })


# =============================================================
# CLUSTER 1 · BLAIR ENNS · THE WIN WITHOUT PITCHING MANIFESTO
# 12 proclamations · 12 chunks
# =============================================================
STITLE = "The Win Without Pitching Manifesto"
SFILE = "wwp_manifesto_enns.md"
AUTHOR = "Blair Enns"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="positioning",
    concept="Proclamation 1 · We will specialize",
    summary="Enns argues that positioning is the foundation of all business success in expertise-driven services. Without a chosen focus, you exist as one of many undifferentiated competitors and the client holds all the power: they dictate price, terms, and how much free thinking they extract before deciding to hire you. The choice to specialize is The Difficult Business Decision that creative firms systematically avoid because their curious-problem-solver instincts pull against narrowing. Specialization is not personality, not process, not price — it is deep expertise in a defined domain that eliminates real alternatives and shifts the power balance from buyer to seller.",
    usable_principle="The narrower and deeper your specialization, the more power you have in every client interaction — pricing, scope, terms, control. Resist the curious-mind pull toward 'we do all kinds of work.' Choose, narrow, repeat.",
    sniped_relevance="Validates SNIPED's narrow position (premium founder photography with Direction Stack methodology) against the constant temptation to take adjacent work (events, weddings, generic corporate). Every off-niche acceptance is a vote against the power position the specialization built. The Reset $1,500 floor only holds because the specialization is genuinely narrow and deep.",
    direct_quotes=[
        "Expertise is the only valid basis for differentiating ourselves from the competition. Not personality. Not process. Not price.",
        "When the client has few alternatives to our expertise then we can dictate pricing, we can set the terms of the engagement and we can take control."
    ],
    tags=["enns","wwp","proclamation-1","specialize","narrow-positioning","power-balance"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="sales-flow",
    concept="Proclamation 2 · We will replace presentations with conversations",
    summary="The default agency motion — preparing pitches, building decks, performing in front of prospects — concedes the power position to the buyer and turns the seller into a performer auditioning for approval. Enns argues for replacing presentations with structured conversations that diagnose the client's situation, qualify fit, and let the expert lead. Conversations preserve the seller's authority; presentations surrender it. The conversation format makes it explicit that the engagement is an exploration of fit, not a beauty contest the seller must win.",
    usable_principle="When a prospect wants a presentation, redirect to a structured conversation. The conversation format protects your authority and lets you diagnose before you prescribe. Performance-style pitches train the buyer to treat you as a vendor competing for their approval.",
    sniped_relevance="For SNIPED's discovery calls (the Mom Test + Direction Stack consultation), this is already the operating mode. Resist any pressure to 'send a deck first' or 'do a sample shoot' before a structured conversation has happened. The discovery call IS the sales motion; everything before it is qualification, everything after is fulfillment design.",
    direct_quotes=[
        "We will replace presentations with conversations.",
        "Presentations put us in the role of performer, while conversations put us in the role of expert."
    ],
    tags=["enns","wwp","proclamation-2","conversations","discovery","authority-preservation"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="sales-flow",
    concept="Proclamation 3 · We will diagnose before we prescribe",
    summary="Enns borrows the medical analogy: a doctor who prescribes before diagnosing commits malpractice. The same applies to expertise-driven services. Most creative firms skip diagnosis and jump to prescription because the prospect is asking for a quote, a proposal, or a sample. Skipping diagnosis trains the buyer to expect free prescription and turns the firm into an order-taker. The cure is to make diagnosis itself the front-end deliverable — paid if possible, but always rigorous — and to refuse to prescribe before it is complete.",
    usable_principle="Never propose a solution before you have diagnosed the problem. If the prospect refuses to engage in diagnosis, they are not your client. The diagnosis is the most valuable part of the engagement; treat it that way.",
    sniped_relevance="For SNIPED, the Direction Stack consultation IS the diagnosis. It precedes any commitment to shoot direction, edit approach, or chapter design. The discipline is to refuse to quote a shoot price or commit to a creative direction before the Direction Stack work has been done with the founder. The Reset $1,500 includes the Direction Stack process; it is not a 'photo session price' — it is a 'diagnosis + execution' price.",
    direct_quotes=[
        "We will diagnose before we prescribe.",
        "We will declare that prescription without diagnosis is malpractice in the world of medicine, and that it is no less negligent in the world of expertise."
    ],
    tags=["enns","wwp","proclamation-3","diagnose-prescribe","direction-stack","front-end"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="sales-flow",
    concept="Proclamation 4 · We will rethink what it means to sell",
    summary="The traditional sales model is adversarial: convince, persuade, overcome objections, close. Enns reframes sales as helping qualified prospects make an informed decision about whether to engage. The expert-seller's job is to make the buying decision easier and clearer, not to push the buyer toward a yes. The reframe makes sales activities feel congruent with expert identity rather than slimy or pushy. The mechanism: ask better questions, share genuine concerns about fit, and recommend NOT working together when the fit is wrong.",
    usable_principle="Reframe sales as 'helping the prospect decide' rather than 'getting them to yes.' Recommend against engagement when fit is wrong. Genuine refusal builds more trust than enthusiastic pursuit.",
    sniped_relevance="For SNIPED, this is the operating frame in VIB DMs and discovery calls. When a founder reaches out and the fit is wrong (wrong stage, wrong aesthetic alignment, wrong budget), the right move is to name the misfit and decline rather than push. The decline produces referrals and reputation; the forced fit produces unhappy clients and reputation damage.",
    direct_quotes=[
        "We will see selling as a noble obligation to help our prospects make a decision in their own best interest.",
        "We will replace the role of seller as persuader with that of trusted advisor."
    ],
    tags=["enns","wwp","proclamation-4","rethink-selling","trusted-advisor","decline-discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="sales-flow",
    concept="Proclamation 5 · We will replace presentations with conversations (in writing)",
    summary="Enns extends Proclamation 2: the long, designed proposal document (the visual artifact that creative firms over-invest in) is itself a form of pitch that surrenders authority. Replace polished proposal decks with short, conversational written documents that confirm what was discussed and ask the buyer to confirm their commitment. The written document should be the confirmation of a conversation, not the conversation itself. Long proposals signal anxiety and try too hard.",
    usable_principle="The proposal document should confirm what was already verbally agreed, not pitch from scratch. If the deal needs the proposal to close it, the conversation didn't close it; that's the actual problem.",
    sniped_relevance="For SNIPED's client engagement docs (the post-discovery email confirming scope + price + timeline), keep them short, conversational, and confirmation-shaped. Do not invest in elaborate proposal decks. The Direction Stack consultation conversation is the sales motion; the written follow-up is the confirmation.",
    direct_quotes=[
        "We will do with words what we used to do with paper.",
        "The proposal is the confirmation of a sale, not the place where the sale takes place."
    ],
    tags=["enns","wwp","proclamation-5","written-proposals","confirmation","not-pitch-doc"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="sales-flow",
    concept="Proclamation 6 · We will be selective",
    summary="Selectivity is the visible expression of specialization. A firm that takes any client it can get communicates desperation; a firm that turns down work communicates expertise and demand. Enns argues that the discipline of saying no — publicly and frequently — is itself a marketing asset. It changes how the next prospect approaches the conversation: they expect to have to qualify themselves to work with you, not the other way around. Selectivity also protects the firm's craft quality (bad-fit clients erode standards) and its team morale (bad clients burn out staff).",
    usable_principle="Selectivity is marketing. Visible refusal builds the position better than visible pursuit. Decline publicly when it serves the brand. Each accepted bad-fit client costs more than the project revenue.",
    sniped_relevance="For SNIPED, this is the discipline behind refusing off-scope referrals (per existing Pearl-network protocol). Floor holds at $1,500, scope flexes; off-scope work gets declined cleanly. The decline is reputation-building, not reputation-damaging. The Founder Tier especially benefits from visible selectivity.",
    direct_quotes=[
        "We will be selective in our pursuits.",
        "When we are selective, we increase the chances of being chosen."
    ],
    tags=["enns","wwp","proclamation-6","selective","refusal-as-marketing","floor-holds"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="positioning",
    concept="Proclamation 7 · We will build expertise rapidly",
    summary="Specialization without genuine deepening expertise is empty positioning. Enns argues for active, rapid expertise-building — books, frameworks, methodologies, talks, original research — that demonstrably extends the firm's depth beyond what generalist competitors can match. The expertise-building isn't optional marketing; it is the actual foundation that justifies the premium pricing and refusal posture. Without it, positioning is a claim without proof and erodes under scrutiny.",
    usable_principle="Specialization is empty without active expertise-deepening. Allocate dedicated time to original research, methodology refinement, and public knowledge-production. The expertise-building IS the marketing.",
    sniped_relevance="For SNIPED, this is the Direction Stack book + Cultural Doc series + 7 photographer Studies + ongoing methodology refinement. These are not 'marketing assets' — they are the actual foundation that makes premium positioning credible. Protect dedicated weekly time for expertise-building, not just client delivery.",
    direct_quotes=[
        "We will build expertise rapidly.",
        "Our expertise is what allows us to position ourselves at the top of the market."
    ],
    tags=["enns","wwp","proclamation-7","expertise-building","direction-stack","cultural-doc"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="sales-flow",
    concept="Proclamation 8 · We will not solve problems before we are paid",
    summary="The pitch-and-spec culture trains creative firms to demonstrate their value by solving the prospect's problem on the prospect's terms before any commitment. Enns identifies this as the central reason creative firms operate from weakness: every spec'd solution given for free trains the buyer that thinking has no price. The discipline is to refuse to do the work before being paid for it — even when the prospect insists, even when competitors are willing, even when the immediate revenue is at stake. Free-work-as-pitch is a structural surrender.",
    usable_principle="Refuse to solve the prospect's problem before being paid to do so. If the prospect wants the problem solved, they should hire you. Spec work, free pitches, sample shoots, free strategy decks — all surrender the authority position.",
    sniped_relevance="For SNIPED, this means: no free sample shoots, no spec'd Direction Stack work, no free 'audit' that resolves the founder's positioning question. The Loom audit front-end exists as a calibrated value-first touch, but it does not solve the founder's photography problem. The Reset $1,500 is the entry price for actual problem-solving. Refuse downward pressure on this.",
    direct_quotes=[
        "We will not solve our prospect's problems before being paid to do so.",
        "When we offer our thinking for free we devalue it."
    ],
    tags=["enns","wwp","proclamation-8","no-free-thinking","reset-floor","spec-work-refusal"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="Proclamation 9 · We will address issues of money early",
    summary="Most service-firm sales conversations dance around money until late in the process, treating price discussion as adversarial or distasteful. Enns argues that early, direct money conversations qualify out wrong-fit prospects before time is wasted on either side and signal the seller's confidence. Bringing up budget early, sharing pricing ranges, and asking the prospect to confirm fit on price before continuing — these moves protect both parties and respect the prospect's time.",
    usable_principle="Bring up money early in the sales conversation — pricing ranges, budget alignment, expected investment level. Late money conversations waste both parties' time and signal seller anxiety. Early money is respect, not vulgarity.",
    sniped_relevance="For SNIPED's discovery calls, the price range ($1,500 floor for Reset; higher for Founder Tier / Brand System) should surface in the first conversation, not get buried until proposal time. The price isn't a secret; the only question is whether the founder's value perception matches. Direct money conversations qualify the right founders in and the wrong ones out efficiently.",
    direct_quotes=[
        "We will address issues of money early in the sales conversation.",
        "Money is best dealt with early and often."
    ],
    tags=["enns","wwp","proclamation-9","money-early","discovery-call","price-discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="Proclamation 10 · We will refuse to work at a loss",
    summary="Enns's hardest discipline: when a project is structured so that the firm will lose money, refuse it. Even when the client is desirable, even when the portfolio piece is appealing, even when refusing is hard. Working at a loss trains the firm to accept loss-making engagements, hollows out morale, and undermines the firm's ability to invest in expertise and team. The exception (genuine strategic investment) must be a deliberate, named decision, not a default that creeps in through poor pricing discipline.",
    usable_principle="Refuse work that loses money, even when the client is attractive. Loss-making engagements compound into team burnout and pricing erosion. Strategic loss must be a deliberate, named decision — never a default.",
    sniped_relevance="For SNIPED, this is the discipline behind the Reset $1,500 floor. The math has to work even at the floor: BJ's time, gear cost, edit time, delivery infrastructure, opportunity cost. Below this, refuse — even when the founder is in the right scene, even when the work would be visible. The exception (strategic free work) is a named category, not a discount creep.",
    direct_quotes=[
        "We will refuse to work at a loss.",
        "When we agree to work below cost we devalue our offering and we set a precedent we will struggle to undo."
    ],
    tags=["enns","wwp","proclamation-10","no-loss-work","floor-discipline","math-must-work"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="Proclamation 11 · We will charge more",
    summary="The most counterintuitive proclamation: most creative firms underprice, and the cure is simply to charge more — often much more. Enns documents repeatedly that firms which raise prices typically don't lose the clients they expect to lose; they instead attract a different and better caliber of buyer. Underpricing communicates lower value and attracts price-sensitive clients who will erode the firm further. Higher prices communicate higher value and attract clients who treat the firm as a partner. The ceiling on what to charge is almost always higher than the firm believes.",
    usable_principle="When in doubt, charge more. The ceiling is almost always higher than you think. Underpricing attracts the wrong buyers; higher pricing attracts better-aligned clients who treat you as a partner.",
    sniped_relevance="For SNIPED, this validates pushing the Founder Tier and Brand System tiers above what feels comfortable. Every time the price discussion produces hesitation in BJ, the right direction is up, not down. The Reset $1,500 floor is the introductory tier, not the target tier. The strategic question for 2026-2027: when do Founder Tier and Brand System pricing move up?",
    direct_quotes=[
        "We will charge more.",
        "Most creative firms are underpricing their services. The first step to better pricing is the realization that you can charge more."
    ],
    tags=["enns","wwp","proclamation-11","charge-more","tier-pricing","price-ceiling"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="positioning",
    concept="Proclamation 12 · We will hold ourselves accountable",
    summary="Enns's closing proclamation: the manifesto is useless without enforcement. Hold yourself accountable to the 11 prior proclamations by tracking real metrics (win rate, average engagement size, percentage of revenue from referrals, percentage of work refused) and reviewing them regularly. Accept that the proclamations will be tested constantly by short-term pressure (cash flow gaps, attractive bad-fit prospects, anxious team members). The test of conviction is what you do under pressure, not what you say in calm moments.",
    usable_principle="Manifestos without measurement are decorations. Track the metrics that prove the discipline is real: win rate, average engagement size, referral percentage, refusal percentage. Review monthly. Pressure-test conviction by what you do under stress, not what you say in calm.",
    sniped_relevance="For SNIPED's quarterly Constraint Audit, track: percentage of revenue from referrals, percentage of inbound prospects refused, percentage of clients who pay above floor, percentage of revenue from Founder Tier and above. These are the WWP-discipline metrics. If the numbers drift wrong direction, the operating discipline has slipped — fix it before the next quarter.",
    direct_quotes=[
        "We will hold ourselves accountable.",
        "Our principles must be more than words. They must be the foundation of our decisions."
    ],
    tags=["enns","wwp","proclamation-12","accountability","metrics","constraint-audit"]
)

print(f"After cluster 1 (Enns WWP · 12 proclamations): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 2 · BLAIR ENNS · PRICING CREATIVITY
# Principles + rules + tips for value-based pricing
# =============================================================
STITLE = "Pricing Creativity"
SFILE = "pricing_creativity_enns.md"
AUTHOR = "Blair Enns"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="Value is subjective · the labor theory of value is wrong",
    summary="Enns opens with the philosophical foundation: value is subjective, not objective. The labor theory of value (price should reflect time and effort) is empirically false for expertise services. A logo that takes 20 minutes can be worth $500,000 to a Fortune 500 company because of what the brand asset enables, while a logo that takes 200 hours can be worth nothing because nobody wants it. Pricing must be tied to value-to-the-buyer, not cost-to-the-seller. This single shift unlocks 5-50x pricing for the same work.",
    usable_principle="Stop pricing your time. Price the value the work creates for the buyer. The buyer's outcome — not your hours — is the only economically meaningful basis for pricing expertise services.",
    sniped_relevance="For SNIPED, this means: the Reset $1,500 is not '6-8 hours of shoot + edit time' — it is 'the value of a founder having premium portraits aligned with their actual positioning for the next 2-3 years.' Founder Tier and Brand System pricing should escalate based on the founder's stage and the value the work creates (raise rounds, press placement, hiring leverage), not on incremental time spent.",
    direct_quotes=[
        "Value is subjective.",
        "The labor theory of value is dead. Long live value."
    ],
    tags=["enns","pricing-creativity","value-subjective","anti-hourly","tier-pricing-logic"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="The three ways to price · inputs, outputs, value",
    summary="Enns lays out three pricing approaches in order of increasing sophistication and price: (1) Inputs · pricing time and materials (commodity firms compete here, lowest prices). (2) Outputs · pricing deliverables and price certainty (most creative firms operate here, middle prices). (3) Value · pricing the client's desired future state (top firms here, highest prices). Each step up the ladder requires different skills, more confidence, and a willingness to do diagnostic work that connects price to outcome. The math: input pricers cap at $100-200/hr equivalent; output pricers reach $300-500; value pricers can capture 10-20% of created value, which often dwarfs the others.",
    usable_principle="Audit which mode you're currently selling in. Move up the ladder deliberately. Value-based pricing requires diagnostic work to connect your fee to the client's outcome; without that diagnostic, you can't price value.",
    sniped_relevance="For SNIPED, the Reset $1,500 is currently an output-pricing model (priced for a defined deliverable: 6 final portraits + Direction Stack consultation). The path to Founder Tier and Brand System pricing requires moving to value-pricing: connect the photography fee to the founder's outcome (raised round, press hits, hiring leverage, brand equity). This is a 2026-2027 evolution, not a 2026-Q2 change.",
    direct_quotes=[
        "There are three things you can sell: inputs, outputs, and value.",
        "Each of these requires a different mindset, a different conversation, and yields a different price."
    ],
    tags=["enns","pricing-creativity","three-ways-to-price","value-based","price-ladder"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="The three-option proposal · anchor high, give meaningful choice",
    summary="Enns's most-tactical structural recommendation: every proposal should present three options at three price points, with the highest option significantly above what you think the client will choose. The three options create a choice architecture (the client picks between options rather than yes/no to one option), the anchor option pulls the perceived value of the middle option up, and the high option occasionally surprises everyone by being chosen. Avoid: one-option proposals (yes/no, more likely to lose), more than three options (decision fatigue, paralysis), three options that are tiny gradations of the same thing (defeats the choice purpose).",
    usable_principle="Present three options, three price points, anchored high. The middle option becomes the default; the high option pulls perceived value up across the board; the low option preserves the no-deal default. Single-option proposals lose more often than three-option proposals.",
    sniped_relevance="For SNIPED, the current offer architecture (Reset $1,500 / Sprint $750 / Op Kit $3-8K / Brand System $10K+) maps imperfectly to this — the tiers exist as a menu but aren't presented as three-option choice within a single proposal. Restructure pitches to: present a Reset, Op Kit, and Brand System option to qualified founders together, anchored at Brand System, with the Op Kit as the default-middle. This will increase Op Kit conversion above pure Reset adoption.",
    direct_quotes=[
        "Three options. Three prices. Anchor high.",
        "The middle option will most often be selected, but the high option will be selected often enough to surprise you."
    ],
    tags=["enns","pricing-creativity","three-options","anchor-high","offer-architecture"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="Anchor high · the first number frames every subsequent number",
    summary="Behavioral economics finding Enns applies tactically: the first price discussed in any negotiation anchors all subsequent price perception. Whoever speaks first effectively sets the negotiation range. If you let the prospect speak first, they will anchor low (their hopeful budget); you will then negotiate up from a too-low starting point. If you anchor first, you set the range that frames the entire conversation. The discipline: name the high option first, before the prospect can ground the conversation in a lower number.",
    usable_principle="Be the first to name a price in any negotiation. Anchor with the high option. The first number frames every number after it; let the prospect anchor and you will lose 20-50% of capturable value before negotiation begins.",
    sniped_relevance="For SNIPED's discovery calls, this means: when price comes up, BJ should name the Founder Tier or Brand System price first, then describe how Reset is the entry point. Do NOT let the founder lead with 'I was thinking maybe $500.' By the time that number is spoken, the negotiation range has already collapsed. Take the price-anchoring move before the founder does.",
    direct_quotes=[
        "Anchor high.",
        "The first number put on the table sets the frame for the entire negotiation."
    ],
    tags=["enns","pricing-creativity","anchor-high","first-mover","discovery-tactics"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="Price discrimination is fair · charge different clients different prices",
    summary="Enns argues against the egalitarian assumption that all clients should pay the same price for the same work. Different clients receive different value from the same engagement (a Fortune 500 brand gets more value from a logo than a startup does), and pricing should reflect this. Charging the Fortune 500 the same as the startup leaves money on the table; charging the startup the same as the Fortune 500 prices them out of the market entirely. Price discrimination — explicitly or via tiered offering structures — is economically rational and ethically defensible because it expands access while capturing value.",
    usable_principle="Different clients should pay different prices for the same expertise, based on the value the work creates for them. Uniform pricing leaves money on the table at the top and prices people out at the bottom. Tier the offering to enable this honestly.",
    sniped_relevance="For SNIPED, this validates the multi-tier ladder (Reset / Op Kit / Founder Tier / Brand System). A seed-stage founder gets one shape of value from portraits; a Series B founder gets a different shape; a CEO of a public company gets a third. The tiers exist precisely to enable price discrimination by value, not to discriminate by client wealth alone. Different founders pay different prices for what is technically similar craft — that is the design, not a bug.",
    direct_quotes=[
        "Price discrimination is good for business and good for clients.",
        "When you charge everyone the same price, you under-serve some and over-charge others."
    ],
    tags=["enns","pricing-creativity","price-discrimination","tier-rationale","value-segmentation"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="The premium-as-insurance frame · pay more to guarantee outcome",
    summary="Enns reframes premium pricing for risk-conscious buyers: the premium option is not 'more expensive same thing' — it is insurance against the failure mode of the cheaper option. In legal services, the cheap lawyer is the one whose failure costs you the case; the premium lawyer is insurance against losing. Same in branding, software, photography. The premium option carries lower risk of bad outcome, which for the right buyer (high-stakes decision, no second chance) is worth a multiple of the price difference. Reframing premium-as-insurance unlocks buyers who would refuse premium-as-luxury.",
    usable_principle="When selling premium tiers, frame them as insurance against failure modes the buyer can't afford. For high-stakes buyers, insurance framing converts where luxury framing fails. The premium tier IS the safe bet.",
    sniped_relevance="For SNIPED's Founder Tier and Brand System, the insurance framing is: 'You only get one shot at the post-Series-A press cycle; the premium tier is insurance that the visual brand doesn't undermine the round narrative.' This works for founders who can hear it. For lower-stakes buyers (a Reset client documenting their day-to-day), insurance framing is overkill — use the value-aligned framing instead.",
    direct_quotes=[
        "Premium pricing isn't about luxury. It's about insurance against failure.",
        "For the right buyer, the question isn't 'what does this cost?' but 'what does failure cost?'"
    ],
    tags=["enns","pricing-creativity","premium-insurance","founder-tier","stakes-framing"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="sales-flow",
    concept="The Permission Conversation · ask permission to address money early",
    summary="Enns's tactical move for raising money early in the sales conversation without seeming pushy: ask permission first. 'Would you mind if I asked some questions about budget and investment range before we go deeper into the creative discussion?' The permission ask softens the directness of the money question, gives the prospect agency, and signals that money is something to be discussed openly rather than danced around. The technique works because most buyers prefer direct money conversations to ambiguous ones; they just expect sellers to be awkward about it.",
    usable_principle="Ask permission before raising money. 'Mind if I ask about budget?' Permission softens directness and signals comfort with money as a topic. The permission frame is the bridge between 'too pushy' and 'awkwardly indirect.'",
    sniped_relevance="For SNIPED's discovery calls, build this in: 'Before we go further into what we'd actually shoot, mind if I share where our pricing tends to land and check that's in the range you were thinking?' This positions money early without it landing as confrontation. Founders appreciate the directness; the awkward-money dance is a worse experience for everyone.",
    direct_quotes=[
        "Ask permission to address money early in the conversation.",
        "The permission ask softens the directness without losing the directness."
    ],
    tags=["enns","pricing-creativity","permission-conversation","money-early","discovery-tactic"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="Never negotiate price without changing scope",
    summary="When a prospect asks for a price reduction, never simply lower the price — always reduce scope, terms, or guarantees to match. Lowering price without changing what is delivered teaches the buyer that the original price was inflated and trains future negotiation downward. Maintaining the price-scope relationship preserves the integrity of the pricing model and signals that the price reflects actual value, not negotiation room. The discipline: 'Yes, we can hit that price — here's what we'd remove to make the math work.'",
    usable_principle="Never reduce price without reducing scope. Price-without-scope-change negotiations train buyers to expect future discounts and signal that your original price was inflated. Always trade scope for price, never price alone.",
    sniped_relevance="For SNIPED, this is operationally critical. When a founder pushes back on Reset $1,500, the response is NOT 'okay, $1,200' — it is 'we can do a tighter scope: 3 finals instead of 6, no Direction Stack consultation, 5-day delivery instead of 3.' If the founder accepts the reduced scope, the price discipline holds. If they refuse, the floor holds. Either way the integrity of the model is preserved.",
    direct_quotes=[
        "If you must lower price, lower scope. Never lower price alone.",
        "A price discount without a scope reduction teaches the buyer that your prices are negotiable."
    ],
    tags=["enns","pricing-creativity","scope-flexes","floor-holds","negotiation-discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="Productize value, don't itemize labor",
    summary="Enns argues against itemized line-item proposals (hourly rates × estimated hours, broken down by phase or deliverable type). Itemization invites line-item negotiation, anchors the conversation in costs rather than value, and converts the engagement back to an input-pricing model even when value pricing was intended. The alternative: present a productized offering with a single value-based price, and refuse to break it down into hours. The lack of itemization forces the conversation back to whether the value-vs-price ratio works, not whether each line item is fairly priced.",
    usable_principle="Resist line-item proposals. Present productized offerings with single value-based prices. Itemization invites negotiation on the wrong axis (cost) and undermines value-pricing discipline.",
    sniped_relevance="For SNIPED, this means the Reset / Op Kit / Founder Tier / Brand System tiers should be presented as productized offerings with single prices, NOT as itemized breakdowns ('shoot day $X, edit time $Y, delivery $Z'). The itemized breakdown invites the founder to ask 'can you skip the delivery to save $Z?' — a conversation that destroys margin and dignity. Productize.",
    direct_quotes=[
        "Productize the offering. Don't itemize the labor.",
        "Itemization invites negotiation on costs. Productization keeps the conversation on value."
    ],
    tags=["enns","pricing-creativity","productize","no-itemization","offer-design"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="pricing",
    concept="Get paid before you do the work · deposits and retainers",
    summary="Cash flow discipline: collect a meaningful deposit (typically 50%) before starting work, with the balance due on or before delivery. Late or post-delivery collection is the single largest source of cash flow stress in service businesses. Clients who refuse to pay deposits are signaling either lack of buying authority or lack of seriousness; either is a fit problem worth surfacing before the work starts. The deposit discipline also creates commitment on the client side, which improves project quality and reduces scope creep.",
    usable_principle="Collect 50% deposit before starting work, balance on or before delivery. No deposit, no work. Clients who refuse deposits are surfacing fit problems early; let them.",
    sniped_relevance="For SNIPED, this should be standard: Reset $1,500 = $750 deposit at booking, $750 on delivery. Founder Tier and above should also follow 50/50 structure. The deposit policy is in BJ's operational backbone but the discipline matters: do not start a shoot, do not start an edit, do not deliver finals before the deposit + balance flow has cleared. The cash flow stability and commitment-creation are both load-bearing.",
    direct_quotes=[
        "Get paid before you do the work.",
        "A meaningful deposit isn't just cash flow; it's commitment."
    ],
    tags=["enns","pricing-creativity","deposits","cash-flow","commitment"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="sales-flow",
    concept="Walk away from bad-fit deals · the floor holds at every price",
    summary="The hardest discipline in Pricing Creativity: when a prospect refuses to engage on the right pricing terms, walk away — even when the cash flow is tight, even when no other deal is on the table, even when the prospect is desirable. Enns documents repeatedly that firms which hold the line on price discipline build the reputation and inbound that eliminates the cash flow stress; firms which break discipline once break it forever. The walk-away is the single most effective sales tool because it inverts the power dynamic instantly.",
    usable_principle="Walk away from deals where the price discipline can't hold. The walk-away is the single most powerful sales move because it inverts the power dynamic. Cash flow stress should never drive the walk-away decision.",
    sniped_relevance="For SNIPED, this is the existing floor-holds discipline applied with conviction. When a founder pushes price below the Reset $1,500 floor and won't accept a scope reduction, walk away. The walk-away protects the brand, builds the discipline reputation in the founder network, and trains future prospects to come in correctly. Cash flow stress is a separate problem to solve with capital reserves, not by breaking pricing discipline.",
    direct_quotes=[
        "Be willing to walk away from any deal.",
        "The walk-away is the single most powerful tool in sales."
    ],
    tags=["enns","pricing-creativity","walk-away","floor-holds","sales-power"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="sales-flow",
    concept="The double thank-you · the signal that pricing is right",
    summary="Enns's qualitative signal for pricing fit: when an engagement closes, both buyer and seller say 'thank you' and both genuinely mean it. The buyer feels they got tremendous value for what they paid; the seller feels well-compensated for what they delivered. If only the buyer says thank you, the seller priced too low. If only the seller says thank you, the buyer was overcharged or oversold. The double thank-you is the signal that the price-value ratio is genuinely aligned, and it produces repeat business, referrals, and a reputation that compounds.",
    usable_principle="The right price produces a double thank-you: buyer thanks you for the value, you thank them for the fair compensation. One-sided thanks signals mispriced engagement. Use the double thank-you as a qualitative pricing audit.",
    sniped_relevance="For SNIPED, this is the relational signal that the pricing model is working. If founders consistently express 'this was so much more than I expected' (one-sided thanks pointing to under-pricing), it's signal to raise prices. If BJ consistently feels under-compensated (one-sided thanks the other direction), same fix. The double thank-you is the qualitative metric for whether the pricing tier is correct for that buyer.",
    direct_quotes=[
        "The right price produces a double thank-you.",
        "When you charge the right price, the buyer thanks you and you thank the buyer — and both mean it."
    ],
    tags=["enns","pricing-creativity","double-thank-you","pricing-audit","relational-signal"]
)

print(f"After cluster 2 (Enns Pricing Creativity · 12 chunks): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 3 · WILL GUIDARA · UNREASONABLE HOSPITALITY
# Service vs hospitality, the hot-dog story, Eleven Madison Park doctrine
# =============================================================
STITLE = "Unreasonable Hospitality"
SFILE = "unreasonable_hospitality_guidara.txt"
AUTHOR = "Will Guidara"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="hospitality",
    concept="Service vs hospitality · the foundational distinction",
    summary="Guidara's central distinction, learned from Danny Meyer and refined at Eleven Madison Park: service is what was promised (the food arrives, the room is clean, the bill is correct). Hospitality is how the recipient feels (welcomed, seen, remembered, surprised). Service is necessary but not sufficient — it is the price of entry for any competent business. Hospitality is the differentiator that creates emotional connection, repeat customers, and referral. Most businesses optimize service and ignore hospitality; the winning ones treat hospitality as primary and service as the substrate that enables it.",
    usable_principle="Service is the floor; hospitality is the ceiling. Audit every client touchpoint: what was promised vs how did they feel? Build hospitality on top of impeccable service, never as a substitute for it.",
    sniped_relevance="For SNIPED's premium-service positioning, this is the entire operating logic. Service = portraits delivered on time, properly retouched, in the agreed format. Hospitality = the welcome packet, the hand-written note, the post-delivery follow-up, the way the Direction Stack consultation makes the founder feel seen for who they are. Every touchpoint should be audited: 'was this just service, or was it hospitality?' The hospitality layer is the premium differentiator.",
    direct_quotes=[
        "Service is black and white; hospitality is color.",
        "Service is the technical delivery of a product. Hospitality is how the delivery of that product makes the recipient feel."
    ],
    tags=["guidara","hospitality","service-vs-hospitality","client-experience","premium-layer"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="hospitality",
    concept="The hot dog story · listening with intent to act",
    summary="Guidara's signature anecdote: a table of European tourists at Eleven Madison Park mentioned they had eaten every famous food in NYC except a street hot dog. Guidara walked outside, bought a hot dog from a cart, and had the kitchen plate it with relish, mustard, and a flourish — serving it as their pre-dessert course. The cost: $2. The outcome: a story the guests told for years that became part of the restaurant's reputation. The principle: the difference between hearing customers and listening with intent to act on what you heard. Every conversation contains potential hospitality moves; most businesses let them slip past.",
    usable_principle="Listen with intent to act, not just to respond. Capture the offhand mentions, the wishes, the regrets — these are the raw material for hospitality moves that cost nothing and create lifetime memories. Build a system for capturing them so they don't slip past.",
    sniped_relevance="For SNIPED, this is the operating model for client experience excellence. During the Direction Stack consultation, capture every detail the founder mentions: their favorite era, the photographer they admire, the shoot they always wanted to do, the location that means something to them. Build the hospitality move from those details. Example: a founder who mentions loving 90s Vogue editorial gets a printed reference card with key spreads in the welcome packet. Cost: $5. Value: priceless.",
    direct_quotes=[
        "Most people listen to respond. Hospitality requires listening with intent to act.",
        "The hot dog cost two dollars. The story it created has been worth far more."
    ],
    tags=["guidara","hot-dog","listening-with-intent","capture-system","hospitality-moves"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="hospitality",
    concept="Unreasonable as deliberate strategy · go past what is sensible",
    summary="Guidara's framing of his book's title: hospitality must be UNREASONABLE — deliberately past what is sensible, expected, or proportional to the transaction — to actually register as hospitality rather than competent service. A reasonable upgrade is forgotten in a week; an unreasonable gesture is remembered for years. The economic argument: reasonable hospitality costs nearly as much as unreasonable hospitality but produces dramatically less return. The strategic argument: in a market where competent service is the floor, only unreasonable hospitality differentiates. Going past sensible is not extravagance; it is precision economics.",
    usable_principle="Reasonable hospitality is invisible. Unreasonable hospitality is unforgettable. The cost differential is small; the return differential is exponential. Calibrate every hospitality move to feel slightly past what the situation rationally calls for.",
    sniped_relevance="For SNIPED, this validates investments that feel disproportionate: hand-signed prints in the delivery package, a follow-up message 6 months after delivery checking on the founder's progress, a thoughtful gift when the founder hits a milestone (Series A close, product launch). These feel 'unreasonable' relative to the project; that's exactly the point. The unreasonable hospitality is the SNIPED-Premium identity made tangible.",
    direct_quotes=[
        "Reasonable hospitality is forgotten. Unreasonable hospitality is talked about for years.",
        "The cost of being unreasonable is almost nothing. The cost of being merely reasonable is everything."
    ],
    tags=["guidara","unreasonable","deliberate-extravagance","memory-economics","sniped-premium"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="hospitality",
    concept="The four-step rule for customer relationships · be present, take it personally, give without expectation, return often",
    summary="Guidara codifies the relational discipline that built Eleven Madison Park's hospitality culture: (1) Be fully present in every customer interaction — phones away, eye contact, undivided attention. (2) Take it personally when something goes wrong, even when it isn't your fault. (3) Give without expectation of return, including in cases where the customer can't or won't reciprocate. (4) Return often — the relationship is built through repeated meaningful touches, not one heroic gesture. The discipline applies to every customer-facing role and must be modeled from the top.",
    usable_principle="Be present. Take problems personally. Give without expectation. Return often. These four moves, repeated consistently, build relationships that survive imperfect service and price increases.",
    sniped_relevance="For SNIPED-as-solo-operator, this is the discipline for every founder relationship. Be fully present in discovery calls (no phone, no multitasking). Take delivery issues personally even when external (Pixieset glitch, file corruption). Give without expectation — the post-delivery follow-up, the LinkedIn comment on their funding announcement, the introduction to another founder. Return often — the relationship doesn't end at delivery; it deepens through repeated touches.",
    direct_quotes=[
        "Be present. Take it personally. Give without expectation. Return often.",
        "These are the four habits of every great host."
    ],
    tags=["guidara","four-step-rule","relational-discipline","client-relationship","operating-habits"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="hospitality",
    concept="The dreamweaver role · designate someone to make magic happen",
    summary="At Eleven Madison Park, Guidara created a dedicated role — the 'dreamweaver' — whose only job was to surface opportunities for unreasonable hospitality and execute them. The dreamweaver listened to reservations conversations, scanned social media for guests' interests, and prepared surprises tailored to each table. The principle: hospitality at scale doesn't happen by accident; it requires dedicated capacity. When everyone owns it, no one owns it. Naming a single person responsible — even a fraction of one person's time — is what makes hospitality systematic rather than occasional.",
    usable_principle="Hospitality at scale requires a dedicated owner, not a shared responsibility. Even at small scale, name the person (or named time block) whose job is to surface and execute hospitality moves. Diffuse ownership produces diffuse results.",
    sniped_relevance="For SNIPED, BJ is currently the de facto dreamweaver, but the role isn't formalized as a time block. Consider: block 30-60 minutes per week as 'Dreamweaver time' specifically for surfacing and executing hospitality moves for current and recent founder clients (a thoughtful note, a curated reference image, a printed gift). Without the protected time, the hospitality slips below client delivery in priority and dies. With the protected time, it compounds.",
    direct_quotes=[
        "The Dreamweaver's only job was to make magic happen for our guests.",
        "Hospitality doesn't happen by accident. It happens because someone makes it their job."
    ],
    tags=["guidara","dreamweaver","dedicated-capacity","protected-time","hospitality-systems"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="culture",
    concept="The hospitality economy · the next wave of differentiation",
    summary="Guidara's macro argument: as service becomes commoditized (everyone delivers competent service via online reviews, training systems, and competitive pressure), hospitality becomes the new differentiator. The economy is shifting from a 'service economy' (functional delivery) to a 'hospitality economy' (emotional connection). Businesses that recognize this shift early and invest in hospitality capacity capture disproportionate share; businesses that continue optimizing service alone lose to hospitality-investing competitors. The shift applies across every industry that touches humans — restaurants, retail, professional services, photography.",
    usable_principle="As your industry's service quality converges, hospitality becomes the only available differentiator. Invest in hospitality capacity before competitors notice the shift. The window of advantage is the gap between when you start investing and when competitors copy you.",
    sniped_relevance="For SNIPED, the photography industry is hitting service convergence (everyone can deliver technically-competent photos via AI tools, online tutorials, equipment democratization). Hospitality is the differentiator: the Direction Stack consultation, the post-delivery touches, the personalized welcome packet, the human warmth in every interaction. The anti-AI position is partly an anti-service-commoditization position — defending hospitality space that AI cannot enter.",
    direct_quotes=[
        "Welcome to the hospitality economy.",
        "When everyone offers good service, hospitality is the only way to win."
    ],
    tags=["guidara","hospitality-economy","service-convergence","ai-defense","sniped-moat"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Restaurant-smart vs corporate-smart · the operator mindset",
    summary="Guidara distinguishes two operational mindsets: 'restaurant-smart' (close-to-the-floor, daily reality, customer-facing decisions made by people who see the customer) and 'corporate-smart' (process-driven, metrics-focused, decisions made by people who see spreadsheets). Both are necessary; neither is sufficient. Pure restaurant-smart organizations can't scale because they lack process; pure corporate-smart organizations alienate customers because the process becomes the thing. The discipline is building organizations where both mindsets are valued and where corporate-smart decisions are pressure-tested against restaurant-smart reality.",
    usable_principle="Build organizations where close-to-the-customer reality (restaurant-smart) and systems/process (corporate-smart) are both valued and held in tension. Pure either-or fails. Decisions made far from the customer must be pressure-tested by people who see the customer.",
    sniped_relevance="For SNIPED at solo-founder scale, BJ embodies both modes — restaurant-smart (every client interaction direct) and corporate-smart (operational backbone, methodology documentation, systems thinking). At Year 5-7 team scale, this duality becomes structural: hires need to be evaluated on both axes, and the team's decisions need to preserve the restaurant-smart sensibility even as corporate-smart systems grow. The Year-10 destination state (4-7 person team) must not lose the floor-level customer connection.",
    direct_quotes=[
        "Restaurant-smart and corporate-smart are both necessary. Neither alone is enough.",
        "The greatest organizations are the ones that keep their corporate-smart decisions honest by pressure-testing them against restaurant-smart reality."
    ],
    tags=["guidara","restaurant-smart","corporate-smart","operator-mindset","scaling-discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Pursuing a true partnership · choose partners who push you",
    summary="Guidara's reflection on his partnership with chef Daniel Humm at Eleven Madison Park: the most productive professional partnerships are between people whose strengths are complementary (not similar) and whose standards push each other higher than either could reach alone. The partnership requires honest conflict — the willingness to push back, disagree, and demand more — without it eroding the relational foundation. False harmony (avoiding conflict to preserve comfort) produces mediocre work; pressured harmony (welcoming conflict in service of the work) produces breakthrough results.",
    usable_principle="Choose partners (co-founders, collaborators, key hires) whose strengths complement yours and whose standards push you higher. Welcome the productive conflict; avoid the false harmony that preserves comfort at the cost of quality.",
    sniped_relevance="For SNIPED's current collaboration with Rejuar (design), Ren (operations), and future hires/partners: select for complementarity, not similarity. Build the relational foundation that can hold productive disagreement (about creative direction, operational decisions, scope). The false-harmony failure mode (avoiding conflict, deferring to BJ on everything, never pushing back) produces compliant work that lacks the partnership-driven excellence the brand requires.",
    direct_quotes=[
        "Pursue true partnership. The right partner pushes you higher than you can go alone.",
        "False harmony is the enemy of great work."
    ],
    tags=["guidara","true-partnership","complementary-strengths","productive-conflict","hiring-criteria"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="The standard you walk past is the standard you accept",
    summary="Guidara's leadership discipline borrowed from military tradition: leaders are defined not by what they say but by what they tolerate. Every moment a leader sees a sub-standard behavior (a service mistake, a quality compromise, a culture-eroding interaction) and walks past without addressing it, that behavior becomes the new acceptable standard. The discipline of immediate, calm, specific correction is what keeps the culture and quality bar high. Avoiding the awkward conversation is the single most common way leaders unintentionally lower their own standards over time.",
    usable_principle="The standard you walk past is the standard you accept. Address sub-standard behavior immediately, calmly, specifically. Avoidance is endorsement. Culture drift happens one tolerated lapse at a time.",
    sniped_relevance="For SNIPED's small-team operation, this means: when a contractor (retoucher, assistant) delivers below standard, address it immediately rather than 'we'll let it slide this once.' When a client interaction goes sideways (scope creep, late payment, behavior), name the issue cleanly. The lapses you tolerate become the brand. This is especially important as the team grows beyond BJ — the standard BJ walks past becomes the team's operating norm.",
    direct_quotes=[
        "The standard you walk past is the standard you accept.",
        "Leaders are defined by what they tolerate, not by what they say."
    ],
    tags=["guidara","standard-tolerated","leadership-discipline","culture-drift","operating-standards"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="hospitality",
    concept="Earning informality · familiarity is a privilege, not a default",
    summary="Guidara's nuance on customer relationships: warmth and informality with customers must be earned through demonstrated competence and care, not assumed as the default. Restaurants (and service businesses) that default to immediate informality ('Hey buddy, what can I get you?') without earning it feel intrusive or unprofessional. Restaurants that start formal and warm up over the course of an experience earn the right to informality and create a deeper emotional arc. The principle: start with respect and competence; let warmth emerge as the relationship deepens.",
    usable_principle="Don't default to informality with new customers. Start with respect and demonstrated competence; let warmth emerge as the relationship earns it. Premature familiarity feels intrusive; earned informality feels intimate.",
    sniped_relevance="For SNIPED's tone across all touchpoints (LinkedIn DMs, discovery calls, delivery emails), this calibrates the warmth. New founder contacts get respectful professionalism with calibrated warmth, not immediate first-name-buddy-buddy intimacy. As the relationship deepens (post-delivery, repeat engagement, referral source), the warmth earns its way to greater informality. The tone evolution is part of the premium experience.",
    direct_quotes=[
        "Earn informality. Familiarity is a privilege, not a default.",
        "Start with respect. Let warmth emerge from competence."
    ],
    tags=["guidara","earned-informality","tone-calibration","relationship-arc","client-touchpoints"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="culture",
    concept="Making magic in a world that could use more of it",
    summary="Guidara's underlying argument for why hospitality matters as a philosophy, not just a business tactic: the world contains genuine scarcity of moments where people feel truly seen, welcomed, and surprised. Most commercial interactions are transactional at best, hostile at worst. The opportunity for any business that consciously invests in hospitality is not just commercial — it is to add net moments of human connection to a world that needs them. The 'magic' framing matters because it shifts hospitality from cost-center to purpose-source for the people doing the work.",
    usable_principle="Frame hospitality as 'making magic' rather than 'customer service.' The framing matters because it shifts hospitality from compliance work to purpose work. People who feel they are making magic do better hospitality work than people who feel they are doing service.",
    sniped_relevance="For SNIPED, this frames the entire client experience as purposeful, not transactional. Every founder portrait session is an opportunity to make the founder feel genuinely seen — through the Direction Stack work, the shoot experience, the delivery, the post-delivery touch. Frame this internally and externally as 'making magic for founders,' not 'delivering photography services.' The framing shapes the work itself; it isn't decorative.",
    direct_quotes=[
        "We're in the business of making magic in a world that could use more of it.",
        "Hospitality is the most important contribution we can make."
    ],
    tags=["guidara","making-magic","purpose-framing","client-experience","internal-narrative"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="The 95/5 rule · operate at 95% efficiency to leave 5% for hospitality",
    summary="Guidara's operational discipline: deliberately run service operations at 95% efficiency rather than 100%, leaving 5% capacity available for unexpected hospitality moves, problem recovery, and human moments that don't fit the schedule. Pure 100%-efficiency operations have no slack to respond to the moment when a customer's mother is at the table and a gesture is called for. The 5% slack is not waste — it is the operating room where unreasonable hospitality happens. Cultures that optimize away the 5% lose the capacity to be hospitable when it matters most.",
    usable_principle="Build 5% slack into your operations deliberately. Pure efficiency optimization kills hospitality capacity. The slack is where the magic happens; without it, you can only deliver what was scheduled, never what the moment calls for.",
    sniped_relevance="For SNIPED's solo-operator capacity, this means: don't fill every week to 100% client capacity. Leave 5-10% room for the unexpected hospitality move (the founder who needs a re-shoot beyond what was contracted, the post-delivery surprise that takes 2 hours to set up, the discovery call that runs long because the founder needs the depth). The slack is what makes the brand experience premium; eliminating it makes SNIPED indistinguishable from any other booked-solid photographer.",
    direct_quotes=[
        "Run at 95% efficiency. The 5% slack is where the magic happens.",
        "100% efficiency leaves no room for hospitality."
    ],
    tags=["guidara","95-5-rule","operational-slack","capacity-discipline","hospitality-room"]
)

print(f"After cluster 3 (Guidara · 12 chunks): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 4 · ALAIN DE BOTTON · STATUS ANXIETY
# 5 causes + 5 solutions = ~10 chunks · status as love-substitute
# =============================================================
STITLE = "Status Anxiety"
SFILE = "status_anxiety_de_botton.md"
AUTHOR = "Alain de Botton"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Status is a love-substitute · the second love story",
    summary="De Botton's foundational reframe: every adult life contains two love stories — the celebrated one (romantic love) and the secret, shameful one (the quest for love from the world, which we call status-seeking). Status anxiety is not vanity or shallowness; it is the human need for love expressed through the only public mechanism available: the regard of others. Adam Smith identified this in 1759: the rich man glories in his riches because they draw attention; the poor man is ashamed of his poverty because it places him out of sight. The status game is the love game, played at scale.",
    usable_principle="Status-seeking is love-seeking, not greed-seeking. Premium buyers of any product are not buying material things — they are buying being-seen, being-attended-to, being-loved-by-the-world. Design and price for the love-substitute, not the material substrate.",
    sniped_relevance="For SNIPED, this reframes WHY founders pay premium for portraits. The founder is not buying 'good photos' — they are buying the visible evidence of being-the-kind-of-person-who-deserves-attention. The Direction Stack consultation, the curated portfolio, the editorial-grade output all serve the love-substitute function. Cultural Doc tone should recognize this without naming it crassly; the founder shouldn't have to admit they want status, but the work should deliver it.",
    direct_quotes=[
        "Every adult life could be said to be defined by two great love stories.",
        "Money, fame and influence may be valued more as tokens of — and means to — love rather than ends in themselves."
    ],
    tags=["de-botton","status","love-substitute","premium-buyer-psychology","cultural-doc"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Cause 1 · Lovelessness · the fragility of self-image",
    summary="De Botton's first cause of status anxiety: our self-image is structurally dependent on the attention of others. William James (1890): no more fiendish punishment exists than to be turned loose in society and remain absolutely unnoticed. The ego is a leaking balloon requiring the helium of external love to remain inflated. Praise inflates us; neglect deflates us; both responses are wildly disproportionate to the actual content of the social signal. This dependency is congenital, not a moral failing, and it explains why status-seeking persists even among people who are materially secure and intellectually critical of status.",
    usable_principle="Self-image is structurally dependent on the regard of others. The most thoughtful people are not free of this dependency; they are merely more aware of it. Design experiences that affirm the recipient's worth in subtle, dignified ways — the affirmation is the actual product.",
    sniped_relevance="For SNIPED's client experience, this means: the most important psychological function of the portrait session is making the founder feel SEEN — not just photographed, but seen as the specific person they are. The Direction Stack consultation, the personalized direction, the post-delivery touch all serve this function. A technically-perfect portrait that left the founder feeling generic is a worse outcome than a slightly-less-perfect portrait that made them feel uniquely understood.",
    direct_quotes=[
        "Our ego or self-conception could be pictured as a leaking balloon, forever requiring the helium of external love to remain inflated.",
        "We seem beholden to the affections of others to endure ourselves."
    ],
    tags=["de-botton","cause-lovelessness","being-seen","client-experience","direction-stack"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Cause 2 · Expectation · why modernity intensified status anxiety",
    summary="De Botton's argument for why status anxiety has gotten worse, not better, in modern democratic-meritocratic societies: when status was hereditary and fixed (medieval Europe), people accepted their position because it was framed as the will of God or the natural order. In meritocratic societies where 'anyone can succeed,' failure becomes personal and shameful — if you didn't make it, the system says it's your fault. The democratization of opportunity is also the democratization of self-blame. Materially we have more than ever; psychologically we suffer more about position than ever before.",
    usable_principle="Modern meritocracy creates worse status anxiety than fixed-hierarchy societies because failure becomes personal. Acknowledge this in any framing that touches on success or status — the buyer is wrestling with personalized shame, not abstract economic concerns.",
    sniped_relevance="For SNIPED's founder buyer specifically, this is acute: the founder lives in the meritocratic ideology where their personal worth IS their startup's traction. Premium portraits offer one of the few legitimate channels for performing 'I am succeeding' to investors, team, peers. Cultural Doc tone should validate the difficulty of carrying this load without explicitly naming the status anxiety — the validation is the relief.",
    direct_quotes=[
        "In a meritocracy, the failure to rise is no longer attributable to fate or birth; it is attributed to the self.",
        "Modernity has multiplied opportunities and so multiplied the agonies of failure."
    ],
    tags=["de-botton","cause-expectation","meritocracy","founder-psychology","cultural-tone"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Cause 3 · Meritocracy · the cruelty of 'you deserved it'",
    summary="De Botton's deepening of the modernity argument: pre-meritocratic societies were unjust but kind; meritocratic societies are just but cruel. In a class society, the poor person could console themselves with 'this is unjust, I deserve more.' In a meritocratic society, the poor person must conclude 'I deserved this; I am worth less.' The meritocratic frame is psychologically devastating precisely because it carries the implication that high status is deserved (a soothing thought for the successful) but also that low status is deserved (a crushing thought for the unsuccessful). The cruelty is built into the system's central virtue.",
    usable_principle="The meritocratic frame that praises success also blames failure. Be careful with success narratives that implicitly devalue people who haven't reached the same outcome — your buyers may also be your buyers' juniors who haven't 'made it' yet.",
    sniped_relevance="For SNIPED's Cultural Doc and named-client portfolio, tread carefully on success narratives. Celebrating Founder Tier subjects ('this founder raised $30M') implicitly tells the seed-stage Reset client 'you haven't earned that level yet.' The framing should celebrate the work and the person without making the size of their company the measure of their worth. Subtle but important for not alienating the broader founder community.",
    direct_quotes=[
        "A society where high status is deserved is also one where low status is deserved.",
        "Meritocracy is just — and that is its cruelty."
    ],
    tags=["de-botton","cause-meritocracy","cruelty-of-just","cultural-tone","portfolio-framing"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Cause 4 · Snobbery · the social arithmetic of dismissal",
    summary="De Botton's analysis of snobbery: it is not just rudeness or arrogance — it is a precise social arithmetic in which the snob equates the person with their job/title/position and dismisses or attends to them accordingly. The snob's question is always 'what do you do?' (meaning: 'what is your status?'), and the conversational warmth that follows is calibrated to the answer. This makes the experience of being lower-status physically painful in social settings: the warmth literally goes out of the room based on the title disclosed. The snob isn't an aberration; the snob is a clear demonstration of how the broader society distributes attention.",
    usable_principle="Snobbery is not random rudeness; it is the social distribution of attention calibrated to status. Every premium experience should explicitly reject snobbery within its walls — the welcome should be equal regardless of the visitor's external status — because the relief of escaping snobbery is part of the premium product.",
    sniped_relevance="For SNIPED, this means: every founder receives identical warmth and respect in initial interaction regardless of whether they're seed-stage Reset or Series C Founder Tier. The Reset client experience should feel as full-throated as the Founder Tier experience; the difference is in scope and time, not in the quality of attention. This is operationally important and brand-building: the seed-stage founder who feels fully welcomed becomes the Series A founder who refers more business.",
    direct_quotes=[
        "Snobbery is the most insidious form of inequality, because it is conducted by individuals against individuals.",
        "What do you do? is the snob's question, and the answer determines the warmth that follows."
    ],
    tags=["de-botton","cause-snobbery","equal-warmth","reset-experience","brand-discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Cause 5 · Dependence · the precariousness of modern status",
    summary="De Botton's fifth cause: modern status is structurally precarious because it depends on factors largely outside the individual's control — the economy, the employer, the market, technology shifts, regulatory changes. Pre-modern status was static and inherited; modern status can collapse in an afternoon (layoff, market crash, technology disruption, public scandal). This precariousness creates chronic background anxiety even among the currently-successful, because they know how thin the foundation is. The anxiety is rational, not neurotic; the structural situation actually warrants it.",
    usable_principle="Modern status is structurally precarious; the anxiety this creates is rational, not neurotic. Premium service buyers know how thin the ground is — design experiences that produce solidity, durability, and timelessness rather than trending or transient feelings.",
    sniped_relevance="For SNIPED's aesthetic discipline (LOCKED 2026-05-12: quiet luxury editorial restraint, NOT cinematic compositing), this is the deep validation. The buyer wants visual artifacts that feel permanent and dignified, not trendy and disposable. Trendy work mirrors the precariousness of the buyer's status; timeless work offers psychological refuge from it. The visual direction IS the relief from status precariousness.",
    direct_quotes=[
        "Modern status depends on factors largely outside the self's control.",
        "The anxiety this dependence creates is not a personal failing; it is a rational response to the structural situation."
    ],
    tags=["de-botton","cause-dependence","aesthetic-permanence","visual-direction","quiet-luxury"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Solution 1 · Philosophy · the examined refusal of social judgment",
    summary="De Botton's first proposed antidote to status anxiety: philosophical scrutiny of the judgments that produce it. The Stoics, Epicurus, Schopenhauer all developed disciplined practices for noticing when external judgment is influencing internal worth-assessment and consciously rejecting that influence when the judgment is irrational. The practice doesn't eliminate status concerns (the dependency is congenital) but it weakens their automatic operation. The philosophically-examined person still feels the sting of dismissal but recognizes it as a contingent social fact, not a verdict on their actual worth.",
    usable_principle="Philosophy is not abstract; it is the disciplined practice of noticing when external judgment is shaping your internal worth-assessment and rejecting the bad judgments. The practice doesn't eliminate the sting; it loosens its grip.",
    sniped_relevance="For SNIPED's Cultural Doc voice, this validates the philosophical register — essays that examine WHY we want what we want, in addition to delivering opinions about what to do. The audience for this isn't the founder being talked-at; it's the founder doing the same examination themselves and finding company in the work. Position SNIPED as a place where the examined life and the visual brand meet, not as a service that delivers prestige unexamined.",
    direct_quotes=[
        "Philosophy is a sustained practice of asking whether the values that drive our anxieties deserve our allegiance.",
        "The examined life weakens the automatic operation of status judgments without eliminating them."
    ],
    tags=["de-botton","solution-philosophy","cultural-doc","examined-life","sniped-voice"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Solution 2 · Art · the redistribution of dignity",
    summary="De Botton's argument for art's role in addressing status anxiety: great art systematically expands the categories of human experience deemed worthy of attention. Chardin painted servants; Manet painted prostitutes; Whitman wrote about laborers. By making these subjects worthy of artistic attention, art redistributes dignity to people the social hierarchy had ignored. The implication for any work that operates in the visual or narrative space: the choice of WHO and WHAT to depict is itself a moral choice about whose worth deserves visibility.",
    usable_principle="Visual and narrative work is never neutral about dignity. Whose existence gets the dignifying treatment? Whose gets ignored? These choices either reinforce existing hierarchies or redistribute dignity to under-attended subjects. Choose deliberately.",
    sniped_relevance="For SNIPED's portrait subject choices and Cultural Doc content, this is foundational. Who gets the Founder Tier portrait? The conventional answer (Series-A-and-up tech founders) reinforces existing hierarchies. The more expansive answer (second-gen immigrant founders, female-led infra startups, climate-tech founders, founders building from outside the SF/NYC axis) redistributes dignity to under-attended subjects. The Lineage Doctrine in BJ's auto-memory points the same direction.",
    direct_quotes=[
        "Art's quiet revolution is the redistribution of dignity.",
        "By painting the unseen, art tells the world they deserved to be seen."
    ],
    tags=["de-botton","solution-art","dignity-redistribution","lineage-doctrine","portrait-subject-choice"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Solution 3 · Bohemia · the alternative status hierarchy",
    summary="De Botton's third antidote: deliberately participate in alternative status hierarchies that don't measure people by the dominant culture's metrics. Bohemian, religious, artistic, intellectual, athletic, and craft communities all maintain their own status systems where money/title/fame matter less and craft/devotion/character matter more. Membership in such a community offers psychological refuge — when the dominant hierarchy ignores or punishes you, the alternative hierarchy can recognize and value you. The practice: actively belong to communities whose status metrics you genuinely respect.",
    usable_principle="Belong to alternative status hierarchies whose metrics you respect more than the dominant one. The dominant hierarchy will not always favor you; alternative hierarchies offer psychological refuge and worth-validation that the dominant one cannot withdraw.",
    sniped_relevance="For SNIPED's scene-density thinking (LOCKED 2026-05-12), this is the philosophical foundation. The 5 lineages (Black church, HBCU intellectual, Southern athletic, Engineering, LA Black founder culture) ARE alternative status hierarchies. BJ's belonging to those communities provides worth-validation independent of how the dominant tech-photography market values SNIPED. Deepen these belongings; don't chase only the dominant hierarchy's recognition.",
    direct_quotes=[
        "Bohemia is the consciously chosen alternative to the dominant hierarchy of value.",
        "Belong to communities whose status metrics you respect more than the dominant one."
    ],
    tags=["de-botton","solution-bohemia","alternative-hierarchy","scene-density","lineage-doctrine"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="Solution 4 · Christianity / mortality reflection · the leveling effect",
    summary="De Botton's secular reading of religious tradition: the practice of regularly contemplating death (memento mori in Christianity, momento mori in Stoic practice, similar across most religious traditions) functions to level status differences. In the face of certain death, the differences in title and wealth that consume daily attention shrink to absurdity. The successful and unsuccessful share the same destination. This contemplation, practiced regularly, weakens the grip of status-seeking by recontextualizing it against the actual scale of human existence.",
    usable_principle="Regular contemplation of mortality is a status-anxiety solvent. The practice (in religious or secular form) recontextualizes daily status games against the actual scale of life. The successful and unsuccessful share the same end; both deserve the same fundamental respect.",
    sniped_relevance="For SNIPED's long-arc thinking and the 10-year destination, this validates the patience discipline. The reward of disciplined work over decades is not status-relative ('we beat the other photographers') but absolute ('we made things that lasted'). The Cultural Doc can carry hints of this — work that will outlast both the current AI hype and the current status games — without being grim about it. Holiday's Perennial Seller covers the same territory commercially.",
    direct_quotes=[
        "The contemplation of death levels the status hierarchy.",
        "Both the celebrated and the unknown share the same destination; both deserve the same fundamental respect."
    ],
    tags=["de-botton","solution-mortality","long-arc","patience","perennial"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="status",
    concept="The hidden gift of status anxiety · its energy is harnessable",
    summary="De Botton's nuanced closing: status anxiety is not purely a problem to eliminate. The same energy that produces destructive comparison and chronic insecurity also produces ambition, achievement, and the willingness to take on hard work. The goal is not to eliminate status anxiety (impossible and probably undesirable) but to channel its energy toward activities that produce lasting value (craft, contribution, meaning) while developing the philosophical, artistic, communal, and contemplative practices that prevent it from becoming destructive. Status anxiety is a fuel; the discipline is choosing what to burn it on.",
    usable_principle="Status anxiety is energy. The discipline isn't elimination — it's directing the energy toward craft and contribution that produce lasting value, while developing the philosophical practices that prevent the anxiety from becoming destructive.",
    sniped_relevance="For SNIPED's founder buyers, this is the gentle reframe to offer (implicitly through the work, not didactically): your status anxiety brought you here, and there's nothing shameful about that. Now let's channel it into making something that lasts — your visual brand, your founder story, your contribution. The portraits aren't trophies; they're tools for sustaining the work that gives status anxiety its productive form.",
    direct_quotes=[
        "Status anxiety is fuel. The question is what you choose to burn it on.",
        "The goal is not to eliminate the energy but to direct it toward what produces lasting value."
    ],
    tags=["de-botton","status-as-fuel","productive-channeling","founder-buyer-frame","sniped-purpose"]
)

print(f"After cluster 4 (de Botton · 11 chunks): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 5 · SIMLER + HANSON · THE ELEPHANT IN THE BRAIN
# Hidden motives · signaling · self-deception
# =============================================================
STITLE = "The Elephant in the Brain"
SFILE = "elephant_in_the_brain_simler_hanson.md"
AUTHOR = "Kevin Simler + Robin Hanson"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="signaling",
    concept="The elephant in the brain · we hide our motives from ourselves first",
    summary="Simler and Hanson's central thesis: human behavior is driven by hidden motives that we systematically conceal from ourselves so we can more credibly conceal them from others. We tell ourselves and others that we're motivated by altruism, learning, principle, or ethics, when much of the time we're actually motivated by status-seeking, mate-seeking, coalition-building, and signaling. The self-deception is functional: a person who genuinely believes they're motivated by principle is a better liar to others about their actual motives than someone who consciously knows what they're doing. The elephant — the hidden motive — is in our own brain first, before it's in anyone else's.",
    usable_principle="When evaluating your own behavior or others', assume the stated motive is a partial truth at best. The hidden motive — usually about status, mating, coalition, or signaling — is doing most of the actual work. Self-deception is the precondition for socially-acceptable hidden motives.",
    sniped_relevance="For SNIPED's understanding of founder buyers, this is operationally important. The founder's stated motive ('I need professional headshots for our About page') is a partial truth. The hidden motive (signaling status to investors / peers / team, mate-seeking adjacent to founder status, coalition-building within the founder community) does most of the buying work. SNIPED's pricing, positioning, and experience design should serve the real motive without naming it crassly. The founder shouldn't have to admit it; the work should deliver it.",
    direct_quotes=[
        "We don't just hide our motives from others. We hide them from ourselves first, the better to hide them from others.",
        "Our brains are built to act in our self-interest while at the same time trying hard not to appear selfish."
    ],
    tags=["simler-hanson","hidden-motives","self-deception","founder-buyer-psychology","signaling"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="signaling",
    concept="Costly signaling · why expensive proves authentic",
    summary="Simler and Hanson extend the biological signaling literature (Zahavi's handicap principle) to human social behavior. A signal is credible to the degree that it would be costly to fake. Cheap signals are ignored because they could be sent by anyone; expensive signals are believed because only the genuinely high-quality sender could afford to send them. This explains why peacocks have heavy tails (only healthy males can afford the burden), why elite universities cost so much (only families with real resources can afford it, signaling capacity), why luxury brands deliberately price above their cost-justified level (the high price IS the signal), and why authentic premium positioning requires actual premium pricing.",
    usable_principle="Cheap signals are ignored. Costly signals are believed. If you want your premium positioning to be credible, the price must be high enough to be expensive to fake. Underpriced premium positioning doesn't read as premium; it reads as confused.",
    sniped_relevance="For SNIPED, this is the structural reason why the Reset $1,500 floor cannot drop. The price IS the signal. If the price were $500, the work might be just as good, but the positioning would not read as premium because the price wouldn't be costly enough to credibly signal premium quality. The Founder Tier and Brand System pricing serves the same function at higher elevations. Costly pricing is not a barrier to growth; it is the foundation of the premium-buyer recognition.",
    direct_quotes=[
        "A signal is credible to the degree that it would be costly to fake.",
        "The handicap principle: the expensive display is the proof of the underlying quality."
    ],
    tags=["simler-hanson","costly-signaling","handicap-principle","premium-pricing","reset-floor"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="signaling",
    concept="Conspicuous consumption · status display through visible spending",
    summary="Simler and Hanson update Veblen for the modern reader: conspicuous consumption is the practice of spending money on visible signals of status — luxury cars, designer clothing, expensive watches, prestige education. The function isn't the underlying utility of the goods (a $50,000 watch keeps time no better than a $50 one) but the visible-to-others signal of having the resources to afford the spending. The principle generalizes: any spending whose primary function is to be SEEN spending (rather than to consume the thing itself) is conspicuous consumption. Premium services often serve this function for the buyer.",
    usable_principle="Buyers of premium goods/services are often buying the visibility of having bought, not just the underlying product. Design and frame the offering so that the buyer's having-chosen-it is itself a visible signal. The signal is the product.",
    sniped_relevance="For SNIPED, founders who choose SNIPED are partly buying the visibility of having-chosen-SNIPED. The Direction Stack book co-authored credit, the Cultural Doc featured-subject inclusion, the named-portfolio appearance — these are visible-to-others signals that the founder is the type who works with SNIPED. The signal value is part of the price justification. Make the signal visible where it serves the founder's status game (LinkedIn launch posts, About page photographer credit, etc.).",
    direct_quotes=[
        "We don't just consume; we are seen consuming.",
        "The function of conspicuous consumption is to broadcast status, not to enjoy the underlying goods."
    ],
    tags=["simler-hanson","conspicuous-consumption","status-display","sniped-credit","visibility-design"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="signaling",
    concept="Charity as signaling · why giving is partly performance",
    summary="Simler and Hanson apply the hidden-motives framework to ostensibly-altruistic behavior: charitable giving is structured to be highly visible (galas, naming rights, public donor lists, lapel pins for blood donation) precisely because the visibility is part of what motivates the giving. The pure-altruism account can't explain why anonymous giving is dramatically rarer than visible giving, why donors prefer naming opportunities, why corporate giving aligns with brand-visibility goals. None of this means the altruism is fake; it means the altruism is mixed with signaling, and the signaling is doing more of the work than donors typically admit.",
    usable_principle="Ostensibly altruistic behavior usually contains a substantial signaling component. When designing 'give-back' or 'mission' elements of a business, design them to be visible — the visibility isn't a corruption of the altruism, it's part of what makes the altruism sustainable for the giver.",
    sniped_relevance="For SNIPED's strategic free work category (one of three explicit categories in BATCH_001 doctrine), this validates building visibility into the free work, not hiding it. Free portraits for an under-resourced community or organization should be documented, celebrated, named in case studies. The visibility makes the giving sustainable and amplifies the brand's mission-aligned positioning. This isn't crass; it's structurally how altruism scales.",
    direct_quotes=[
        "Charity is rarely as pure as it appears. The visibility is part of what motivates the giving.",
        "Anonymous giving is dramatically rarer than visible giving, for reasons that have nothing to do with the recipients."
    ],
    tags=["simler-hanson","charity-signaling","strategic-free-work","mission-visibility","case-studies"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="signaling",
    concept="Education as signaling · the diploma matters more than the learning",
    summary="Simler and Hanson's most-controversial chapter (drawing on Bryan Caplan): much of the value of elite education is signaling, not skill-building. The diploma signals to employers that the graduate is intelligent, conscientious, and willing to conform to institutional expectations. The specific learning often doesn't transfer to the job. This explains why graduates demand the credential even when the actual courses are available free online (signaling requires the costly, credentialed version), and why elite-school grads earn more even controlling for SAT scores (the brand of the school is the signal).",
    usable_principle="Credentials are often more valuable for their signaling function than their learning content. When entering a market where credentials matter, prioritize the credentialing artifact (book, talk, certification, named-client list) for its signaling value, not just for the underlying competence it certifies.",
    sniped_relevance="For SNIPED's brand-building investments, this validates the Direction Stack book + Cultural Doc + named-client portfolio as credentialing artifacts. They signal expertise to founder buyers who can't easily evaluate underlying photographic skill. The book is not primarily a knowledge-transfer artifact; it is a signaling artifact. Frame and invest accordingly: the book's COVER and AUTHORITY-PROJECTION matter as much as the substance, because much of its function is signaling SNIPED's right to charge premium.",
    direct_quotes=[
        "The diploma is more valuable than the learning it certifies.",
        "Credentials are signals first, knowledge-transfer second."
    ],
    tags=["simler-hanson","credentials-as-signal","direction-stack-book","authority-projection","brand-investments"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="signaling",
    concept="Art as conspicuous taste · the deeper signaling function",
    summary="Simler and Hanson extend the signaling frame to art consumption: the function of displaying art (or curating one's taste in any medium) is largely to signal the depth of one's discernment, the breadth of one's cultural capital, and the membership in communities that respect those signals. This is why people buy original art instead of prints (the cost-to-fake test), why collectors talk about provenance and acquisition stories (cost-of-knowledge signals), and why generic decorative art is socially invisible while distinctive curation reads as taste. The principle generalizes: any deliberate aesthetic choice is partly a signal of the chooser's discernment.",
    usable_principle="Aesthetic choices are signals of discernment. When buyers can choose between similar offerings, they often pick the one whose aesthetic signals the kind of person they want to be seen as. Position your aesthetic deliberately, knowing it functions as a signal not just a style.",
    sniped_relevance="For SNIPED's quiet luxury editorial visual direction (LOCKED 2026-05-12), this is the structural reason it works. Quiet luxury IS a discernment signal — it requires the viewer's eye to recognize what's restrained and considered vs what's loud and obvious. Founders who choose SNIPED are signaling discernment to other people who recognize the discernment. The 'cinematic compositing' aesthetic that was rejected reads as less discerning (more is more); the quiet luxury aesthetic reads as more discerning (less is more, knowingly).",
    direct_quotes=[
        "Aesthetic choices are choices about who you want to be seen as.",
        "Restraint is a signal because only the genuinely confident can afford to leave the obvious moves unmade."
    ],
    tags=["simler-hanson","art-as-taste-signal","quiet-luxury","aesthetic-as-signal","sniped-visual-direction"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Coalition signaling · why we publicly align with tribes",
    summary="Simler and Hanson identify coalition-signaling as a major driver of public statements: people declare positions partly to communicate the substance of the position, but largely to signal membership in a coalition whose status they want to share. This explains why opinions cluster more than facts would suggest (the coalitions cluster), why people defend positions long after the facts change (the coalition membership matters more than the position's truth), and why public communication is often more about WHO is allowed to speak than WHAT is said. The framework applies to political speech, professional opinions, and brand positioning.",
    usable_principle="Public positioning is partly coalition-signaling. When you declare a position publicly, you're signaling tribal membership as well as substance. Choose declared positions knowing they sort your audience into 'with you' and 'against you' coalitions — that sorting is often the point.",
    sniped_relevance="For SNIPED's anti-AI public position (Cultural Doc 'On Refusing to Use AI'), this is structurally important. The position sorts the founder audience: AI-skeptical founders move toward SNIPED; AI-maximalist founders move away. This sorting IS the intended function — it makes SNIPED the obvious choice for the right coalition, while filtering out the wrong coalition (which would never have been a good fit anyway). The position-as-coalition-signal is a feature, not a bug.",
    direct_quotes=[
        "Public statements are coalition signals as much as factual claims.",
        "When you declare a position, you sort your audience into those who agree and those who don't. Often that sorting is the point."
    ],
    tags=["simler-hanson","coalition-signaling","anti-ai-position","audience-sorting","cultural-doc"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="The press secretary brain · our consciousness as PR",
    summary="Simler and Hanson's model of consciousness: the conscious mind functions as a press secretary for the rest of the brain — generating explanations for behavior after the behavior has occurred, presenting those explanations in socially-acceptable terms, and genuinely believing the explanations even though the actual decision was made by other parts of the brain operating on hidden motives. The press secretary is not lying; it has no access to the actual decision process. This explains why introspection so often fails to capture real motives, why people are reliably wrong about why they did what they did, and why behavioral evidence outweighs stated motives.",
    usable_principle="The conscious mind explains behavior after the fact, often inventing reasons that have nothing to do with the actual decision process. Trust behavior over stated motives — your own and others'. Track what people DO when buying decisions get made, not what they SAY about why.",
    sniped_relevance="For SNIPED's market research and buyer-understanding, this means: don't over-weight what founders SAY they want in photography. Track what they actually choose, where they actually spend, which work they actually share. The press-secretary version is sanitized for social presentation; the behavioral version is the actual signal. The Reset $1,500 conversion data tells more than any survey response would about what founders actually value.",
    direct_quotes=[
        "The conscious mind is a press secretary, not the decision-maker.",
        "We are reliably wrong about why we did what we did. Trust behavior."
    ],
    tags=["simler-hanson","press-secretary","behavioral-data","market-research","conversion-tracking"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Norms enforcement · why we punish defectors disproportionately",
    summary="Simler and Hanson explain the puzzling phenomenon of costly norm-enforcement: humans will punish people who violate group norms even when punishing is personally costly and benefits the punisher in no direct way. The function isn't direct: it's the signaling of one's commitment to the group's norms, which builds coalition membership and reputation. This explains social-media pile-ons, professional ostracism, and the disproportionate punishment of small defections — the punishment isn't really about the defection's harm; it's about the punisher's coalition-signal.",
    usable_principle="When you defect from group norms — even small defections — expect disproportionate punishment driven by other people's coalition-signaling, not by the actual harm. Defect deliberately and with eyes open; the punishment will exceed what the act 'deserves' on direct-harm grounds.",
    sniped_relevance="For SNIPED's anti-AI position, this predicts: SNIPED will receive disproportionate pushback from the AI-enthusiast photography coalition, not because the anti-AI position causes them direct harm, but because punishing the position signals their commitment to their own coalition. Be prepared for the disproportionality; don't take it personally; recognize it as evidence that the position is working as a coalition-sorter. The pushback is the proof the position has bite.",
    direct_quotes=[
        "We punish defectors disproportionately because the punishment is itself a coalition signal.",
        "The disproportionate reaction is evidence that the violation registered as a coalition matter, not just a substantive one."
    ],
    tags=["simler-hanson","norm-enforcement","anti-ai-pushback","coalition-defense","cultural-doc-aftermath"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="The implication for self-knowledge · trust the data, not the story",
    summary="Simler and Hanson's closing implication: genuine self-knowledge requires distrusting the conscious narrative and trusting the behavioral data. The conscious narrative will always present the self in flattering, principle-driven, prosocial terms because the press secretary is built that way. The behavioral data — what you actually do with money, time, attention, and choices — reveals the hidden motives more accurately. Self-knowledge is a discipline of preferring uncomfortable behavioral evidence over comfortable narrative self-presentation. Most people refuse this discipline; the rare ones who practice it become unusually effective.",
    usable_principle="Genuine self-knowledge requires preferring behavioral data over narrative self-presentation. Track your own actual time, money, and attention allocation; let the data correct the narrative when they diverge. The narrative is press; the data is truth.",
    sniped_relevance="For BJ's own operating discipline, this means: track actual time allocation against intended time allocation; track actual revenue mix against intended revenue mix; track which client interactions actually energize vs drain. The narrative (BJ as disciplined operator, focused on Direction Stack, refusing off-niche) is the press release; the behavioral data is the truth. The quarterly Constraint Audit should foreground behavioral data over narrative self-assessment.",
    direct_quotes=[
        "Self-knowledge requires distrusting the narrative.",
        "Track behavior, not stated motives. The data is truer than the story."
    ],
    tags=["simler-hanson","behavioral-self-knowledge","constraint-audit","operating-discipline","bj-practice"]
)

print(f"After cluster 5 (Simler+Hanson · 10 chunks): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 6 · NAVAL RAVIKANT · THE ALMANACK
# Wealth, leverage, judgment, happiness, philosophy
# =============================================================
STITLE = "The Almanack of Naval Ravikant"
SFILE = "almanack_naval_ravikant.txt"
AUTHOR = "Naval Ravikant (ed. Eric Jorgenson)"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leverage",
    concept="The three forms of leverage · labor, capital, code+media",
    summary="Naval's central framework for wealth creation: leverage is a force multiplier on judgment, and the three available forms are labor (people working for you), capital (money working for you), and code+media (products with zero marginal cost of replication). Labor is the oldest form (impresses your parents) but consumes the leverager's time and energy. Capital requires permission (someone has to give you the money). Code and media are permissionless — anyone can write software or create content — and they work while you sleep. The newly rich disproportionately use code+media leverage because it scales without permission and without proportional time investment.",
    usable_principle="Leverage multiplies judgment. Of the three forms, code and media are permissionless and scale without proportional time investment. Whenever possible, prefer code/media leverage over labor/capital leverage. The newly rich are using it; the old rich rely on the others.",
    sniped_relevance="For SNIPED's 10-year arc, this is the structural argument for the Direction Stack book + Cultural Doc + methodology IP. The book is code/media leverage — it works while BJ sleeps, scales without permission, and compounds. Founder-tier client work is labor leverage (consumes BJ's time directly). The balance shifts over the 10-year arc: more code/media leverage, less labor leverage. The book is not a marketing asset — it is the leverage shift in artifact form.",
    direct_quotes=[
        "Code and media are permissionless leverage. They're the leverage behind the newly rich.",
        "Fortunes require leverage. Business leverage comes from capital, people, and products with no marginal cost of replication."
    ],
    tags=["naval","three-leverages","code-and-media","direction-stack-book","ten-year-arc"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leverage",
    concept="Specific knowledge · what you can't be trained for",
    summary="Naval's term for the kind of knowledge that produces outsized returns: 'specific knowledge' is knowledge you can't be trained for, that comes from genuine curiosity and natural inclination, that is hard to describe in a job spec, and that compounds because it's at the intersection of your unique experiences. Generic skills (Excel, PowerPoint, project management) are competing-with-everyone-else skills. Specific knowledge — your particular fusion of interests, your weird obsessions, the things you can't help but do — is what makes you uncopyable. Build the career around the specific knowledge, not the generic credentials.",
    usable_principle="Build your work around specific knowledge — the things you can't be trained for, the obsessions you can't help but pursue. Generic skills compete with everyone; specific knowledge competes with no one because no one else has your particular fusion of experiences.",
    sniped_relevance="For SNIPED, BJ's specific knowledge is the intersection of: photographer + engineer + Black operator in tech-adjacent culture + Direction Stack methodologist + cultural documentarian + systems thinker. No one else has exactly this fusion, which is why no one else can replicate the work. Resist the pull to specialize INTO any single one of these (just photographer, just engineer, just methodologist) — the cross-section IS the moat.",
    direct_quotes=[
        "Specific knowledge is found much more by pursuing your innate talents, your genuine curiosity, and your passion.",
        "Building specific knowledge will feel like play to you but will look like work to others."
    ],
    tags=["naval","specific-knowledge","uncopyable","cross-section-moat","direction-stack-positioning"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leverage",
    concept="Productize yourself · the play-as-work strategy",
    summary="Naval's most-quoted advice: take your specific knowledge and find a way to productize it — convert it into something that scales without your time being in every unit of output. 'Productize' has leverage; 'yourself' has accountability and authenticity. The combination is the modern wealth formula. A consultant who only sells hours never escapes the labor trap; a consultant who writes the book, builds the course, creates the framework, ships the software has productized themselves and now their work multiplies. The product is the leverage; the 'yourself' is the differentiation.",
    usable_principle="Find the way to productize your specific knowledge. A productized version of you (book, framework, methodology, course, software) scales without consuming your time linearly. The 'yourself' makes it authentic; the 'productize' makes it leveraged.",
    sniped_relevance="For SNIPED, this is the explicit roadmap. The Direction Stack methodology is the productizable IP. The book is the first product version. Future products: Direction Stack workshop, Direction Stack certification for other photographers, Direction Stack software/templates for founders to use directly. Each one converts BJ's specific knowledge into something that scales without BJ's hours being in every unit. This is the path from $1,500 Reset to 7-figure annual outcomes without 7-figure hours.",
    direct_quotes=[
        "Productize yourself.",
        "'Productize' has leverage. 'Yourself' has accountability and authenticity."
    ],
    tags=["naval","productize-yourself","direction-stack-monetization","leverage-roadmap","ten-year-arc"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leverage",
    concept="Escape competition through authenticity · no one can compete with you being you",
    summary="Naval's contrarian competitive strategy: don't try to win the games everyone else is playing; play a game where being you is the entire competitive moat. The advice generalizes: when you compete on conventional metrics (price, features, speed) you compete with everyone else racing the same way. When you compete on authentic distinctiveness, no one else can credibly enter your specific space. The discipline is to identify what only you can do (the intersection of your specific knowledge, your particular taste, your specific relationships) and to do that, even when convention argues against it.",
    usable_principle="Escape competition through authenticity. When you compete on conventional metrics, everyone competes with you. When you compete on what only you can be, no one can. Build the work around the specific thing only you can do.",
    sniped_relevance="For SNIPED, this is the foundational argument against the AI-everyone-is-doing-it convergence in photography. The market is racing to AI-augmented production; the escape-through-authenticity move is to stay analog/in-camera/identity-preserving precisely because no one can copy that authentically — they can copy the visual style, but they can't copy BJ's specific knowledge and relational depth. The authenticity IS the uncopyable moat.",
    direct_quotes=[
        "Escape competition through authenticity.",
        "No one can compete with you being you."
    ],
    tags=["naval","escape-competition","authenticity-moat","anti-ai-positioning","sniped-uncopyable"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leverage",
    concept="Set an aspirational personal hourly rate · the time-economic discipline",
    summary="Naval's pragmatic discipline: set a personal hourly rate that is higher than what you're currently worth — aspirational, not historical. Use this rate to decide what tasks to do yourself vs delegate, what problems to fix vs accept, what meetings to attend vs decline. If a task costs less than your rate to outsource, outsource it. If a problem costs less than your rate to fix, ignore it. The aspirational rate disciplines time allocation toward leveraged work and against time-drain work. Most people set the rate too low and end up spending hours on tasks that cost more in time than they would in money to delegate.",
    usable_principle="Set an aspirational hourly rate. Use it as a decision filter: outsource what costs less than the rate; ignore what costs less than the rate to fix; decline what doesn't earn the rate. The rate should be higher than your current self values; calibrate up, not to current reality.",
    sniped_relevance="For SNIPED, BJ should set an aspirational rate (e.g., $300-500/hr based on Founder Tier yields). Apply this to decisions: hire an editor for first-pass culling (cost: $20-40/hr, vs BJ's $300/hr time = obvious outsource), hire a VA for scheduling (same math), decline meetings that don't move six-figure work forward, refuse projects that pay below the rate even with prestige attached. The rate is the operating discipline that protects time for leveraged work.",
    direct_quotes=[
        "Set and enforce an aspirational personal hourly rate.",
        "If fixing a problem will save less than your hourly rate, ignore it. If outsourcing a task will cost less than your hourly rate, outsource it."
    ],
    tags=["naval","aspirational-rate","time-economics","delegation-discipline","operating-filter"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leverage",
    concept="Play long-term games with long-term people · the compounding relationship asset",
    summary="Naval's relational discipline: all the returns in business and life come from compound interest, and compound interest applies to relationships as much as to capital. Long-term games with long-term people (repeat collaborators, repeat clients, repeat colleagues over decades) accumulate trust and information advantages that short-term transactions never reach. The discipline: select for people you can play with for 20+ years and play the longer game. Short-term relational thinking optimizes for the next transaction; long-term thinking optimizes for the next 50 transactions with the same person.",
    usable_principle="All compounding returns come from playing long-term games with long-term people. Select collaborators, clients, and partners for 20+ year potential. The first transaction is the start of a relationship asset, not a complete event.",
    sniped_relevance="For SNIPED, this validates: deep investment in current founder clients (every founder is a 20-year potential repeat or referral source), commitment to long-running collaborators (Rejuar on design, etc., not constant rotation), patience with the Lineage Doctrine communities (single-visit cultural tourism refused per BJ's auto-memory). The 60 founder portraits are not 60 transactions — they are 60 long-term relationship investments. Treat them that way.",
    direct_quotes=[
        "Play long-term games with long-term people.",
        "All the returns in life, whether in wealth, relationships, or knowledge, come from compound interest."
    ],
    tags=["naval","long-term-games","compounding-relationships","lineage-doctrine","founder-network"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Be patient · most wealth and meaning takes decades",
    summary="Naval's persistent counsel to the impatient ambitious: the highest-leverage outcomes (genuine wealth, deep mastery, meaningful relationships, lasting work) all take decades to develop, and the impatience that wants them faster is the single most common reason people abandon the path that would have produced them. Most overnight successes are 10-year overnight successes. The discipline is to set up the leverage (specific knowledge + productized form + permissionless distribution + long-term relationships), then keep showing up for years. Impatience is the most expensive sin in compounding domains.",
    usable_principle="Patience is the most undervalued discipline in compounding domains. The work that produces decade-scale outcomes requires decade-scale commitment. Impatience is the most common reason people abandon paths that would have worked.",
    sniped_relevance="For SNIPED's 10-year arc, this is the meta-discipline. Year 1-2 is foundation-laying that won't produce visible compounding returns yet. Year 3-5 is when the methodology IP, founder network, and Cultural Doc start compounding. Year 5-10 is the harvest. The impatience to skip the foundation years (by chasing scale, expanding scope, or abandoning the anti-AI position for short-term revenue) is the most likely failure mode. Stay patient; the math works.",
    direct_quotes=[
        "Be patient.",
        "Most wealth and meaning takes decades. The impatient abandon the path before it produces the returns."
    ],
    tags=["naval","patience","ten-year-arc","compounding","foundation-years"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leverage",
    concept="Reading is faster than listening · doing is faster than watching",
    summary="Naval's tactical learning discipline: reading is faster than listening (you can read at 3x speech speed), doing is faster than watching (one attempt teaches more than ten observations). The implication for learning velocity: minimize passive consumption (podcasts, video tutorials, conference talks) and maximize active consumption (reading the source material) and active production (actually doing the thing). The bias toward passive media is comfortable but slow; the bias toward active learning is uncomfortable but compounds faster.",
    usable_principle="Prefer reading to listening, prefer doing to watching. Active learning compounds faster than passive consumption. The comfort of passive media is the slowness it produces.",
    sniped_relevance="For BJ's own learning discipline, this means: read the source books (this whole AI-Brain-Refinery project), don't just listen to summaries. Run the shoot, don't just watch tutorials. Write the Cultural Doc essay, don't just consume other people's writing. For SNIPED's content strategy, this also informs what to publish: written long-form essays (read-first) outperform podcasts for serious audience engagement; behind-the-scenes doing-the-work content outperforms talking-about-the-work content.",
    direct_quotes=[
        "Reading is faster than listening. Doing is faster than watching.",
        "Active learning compounds; passive consumption does not."
    ],
    tags=["naval","reading-vs-listening","active-learning","bj-learning-discipline","content-strategy"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Avoid business magazines and business classes · there is no skill called business",
    summary="Naval's contrarian educational advice: there is no general skill called 'business' — the term is a category mistake that lumps together specific skills (microeconomics, psychology, persuasion, mathematics, computer science, design, writing) that need to be studied individually. Business magazines and MBA programs flatten these into generic 'business thinking' that produces shallow imitation rather than deep capability. The alternative: study the underlying disciplines deeply, then apply them to the specific business problem in front of you. Depth in primitives beats breadth in generalities.",
    usable_principle="There is no skill called 'business.' Study the underlying disciplines (microeconomics, psychology, persuasion, math, computers) deeply, then apply them to the specific problem. Generic business education produces shallow imitation; specific discipline study produces real capability.",
    sniped_relevance="For BJ's continued learning, this validates the depth-over-breadth approach: read the canonical sources on pricing (Enns), hospitality (Guidara), status (de Botton, Simler/Hanson), strategy (Greene, Thiel, Munger) rather than consuming generic 'photography business' content. The depth on a few primitives is what enables the cross-domain synthesis that produces the Direction Stack. The auto-memory intel files are exactly this kind of depth-in-primitives.",
    direct_quotes=[
        "There is no skill called 'business.' Avoid business magazines and business classes.",
        "Study microeconomics, game theory, psychology, persuasion, ethics, mathematics, and computers."
    ],
    tags=["naval","no-skill-called-business","depth-over-breadth","primitive-study","intel-files"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Happiness is a learned skill · peace and presence over pursuit",
    summary="Naval's philosophical pivot in the second half of the Almanack: happiness is not a goal to achieve through external accomplishment but a skill to develop through internal practice. The pursuit of external success rarely produces happiness because each achievement gets normalized into the new baseline. The practices that produce durable well-being are internal: meditation, presence, acceptance, reducing desires (every desire is a chosen unhappiness), limiting envy, choosing peace over excitement. The wealthy person who lacks these practices ends up no happier than the poor person; the practiced person ends up well regardless of external state.",
    usable_principle="Happiness is a skill, not a goal. External success doesn't produce it; internal practice does. Develop the practices (meditation, presence, acceptance, desire reduction) deliberately, parallel to the wealth-building. They are not optional add-ons.",
    sniped_relevance="For BJ as solo-founder running a high-ambition long-arc project, this is the personal-sustainability discipline. The 10-year arc requires showing up daily for a decade; that requires not being burned out by the chase itself. Build the personal practices (whatever form they take for BJ) deliberately, not as 'I'll get to that when the business is settled.' The practices ARE part of the operating discipline, not a separate domain.",
    direct_quotes=[
        "Happiness is a learned skill.",
        "Every desire is a chosen unhappiness."
    ],
    tags=["naval","happiness-as-skill","founder-sustainability","ten-year-discipline","personal-practice"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Free yourself · the goal is freedom, not status",
    summary="Naval's framing of what wealth is actually for: not status, not power, not accumulation, but FREEDOM. Freedom from having to do work you don't want to do. Freedom from people you don't want to be around. Freedom from places you don't want to be. Freedom to think for yourself, to refuse, to walk away, to start over. Wealth that produces obligation, complexity, and constraint is wealth that has betrayed its purpose. The strategic question for any business decision is: does this increase freedom or decrease it? Most growth decisions decrease freedom even when they increase revenue.",
    usable_principle="Wealth is for freedom, not for status or accumulation. Test every growth decision against the freedom question: does this increase or decrease the freedom to refuse, walk away, and think for yourself? Revenue without freedom is a trap.",
    sniped_relevance="For SNIPED's growth decisions, this is the discipline. Adding a new client tier that requires constant availability decreases freedom even if it adds revenue. Hiring that requires daily management decreases freedom. Signing a long-term studio lease decreases freedom. Maintaining solo-founder freedom (with leveraged code+media income compounding alongside) is structurally different from scaling a 50-person agency. Choose the freedom-compatible growth path even when the high-revenue path is available.",
    direct_quotes=[
        "The goal is freedom.",
        "Freedom from having to do work you don't want to do. Freedom from people you don't want to be around. Freedom to think for yourself."
    ],
    tags=["naval","freedom-as-goal","growth-filter","solo-founder-discipline","sniped-year-ten"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leverage",
    concept="The internet has massively expanded the search space · find your specific person",
    summary="Naval's macro observation about the modern environment: pre-internet, you were constrained to whatever niche existed in your local area, which forced generalists into mass markets. The internet allows the discovery of arbitrarily-specific audiences scattered globally, which means a tiny niche can sustain a real business if you can reach the right people across the world. The implication: don't generalize to reach more local people; specialize to reach the global niche that actually values what only you can do. The audience for any genuinely specific work exists; the discipline is finding it via the internet's search infrastructure rather than blunt local marketing.",
    usable_principle="The internet rewards specificity. The audience for any genuinely specific work exists somewhere globally. Stop generalizing to capture more local market; specialize to capture the global niche that actually values your specific thing.",
    sniped_relevance="For SNIPED's positioning, this is the validation for staying narrow even as growth pressure builds. Premium founder photography in the specific lanes SNIPED occupies has a global addressable market (every major startup ecosystem worldwide has founders who would value the Direction Stack approach). The path to growth is not 'expand to cover more types of work in LA' but 'reach more of the specific buyer globally.' This is also why the Cultural Doc and book have outsized strategic value: they reach the global niche.",
    direct_quotes=[
        "The internet has massively broadened the possible space of careers and the search space for finding people.",
        "Find your specific person. The internet makes the global niche reachable."
    ],
    tags=["naval","global-niche","specificity-rewarded","cultural-doc-reach","international-growth"]
)

print(f"After cluster 6 (Naval · 12 chunks): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 7 · PAUL JARVIS · COMPANY OF ONE
# Staying small as deliberate strategy
# =============================================================
STITLE = "Company of One"
SFILE = "company_of_one_jarvis.md"
AUTHOR = "Paul Jarvis"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="small-company-strategy",
    concept="Defining a company of one · staying small as the goal",
    summary="Jarvis's central reframe: a 'company of one' is not necessarily a one-person business, but a business that questions growth as the automatic default. Most business advice assumes growth is good; a company of one asks 'is growth actually serving our goals here?' and often answers no. The defining trait is intentionality about size — knowing what 'enough' looks like for revenue, team, complexity, hours — and refusing to grow past those thresholds even when it's tempting or possible. The discipline runs counter to nearly all popular business writing, which is why so few businesses actually practice it.",
    usable_principle="Growth is not automatically good. Define what 'enough' looks like across revenue, team size, complexity, and hours. Refuse to grow past your defined thresholds even when growth is available. Intentionality about size is the discipline.",
    sniped_relevance="For SNIPED's Year-10 destination state (4-7 person team, NOT a 50-person agency), this is the structural validation. Jarvis directly counters the 'should you scale?' pressure that surrounds every successful service business. SNIPED has defined its 'enough': 4-7 people, $1.5-3M revenue, named cultural documentarian role. Resist every well-meaning advisor who suggests scaling past these thresholds. The threshold IS the point.",
    direct_quotes=[
        "A company of one is simply a business that questions growth.",
        "Growth, for the sake of growth, is the ideology of the cancer cell."
    ],
    tags=["jarvis","company-of-one","intentional-size","sniped-year-ten","anti-scale"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="small-company-strategy",
    concept="Resilience over scale · staying small is more durable",
    summary="Jarvis's counter-argument to the 'scale or die' narrative: small, focused businesses are more resilient to economic shocks, market changes, and personal circumstances than large ones. A company of one can pivot quickly, weather a bad quarter without layoffs, survive a personal crisis without losing customers, and maintain quality without the overhead drag of large operations. Large businesses appear powerful but are structurally fragile because their cost structure requires continuous growth to maintain. Small businesses appear vulnerable but are structurally resilient because their cost structure tolerates variability.",
    usable_principle="Small is more resilient than large. Large businesses require continuous growth to sustain their cost structure and break catastrophically when growth pauses. Small businesses absorb variability and survive shocks that destroy large competitors.",
    sniped_relevance="For SNIPED, this means resilience is a strategic asset, not a consolation prize. When the photography industry takes shocks (AI disruption, economic downturn, market shifts), SNIPED's small footprint is structurally advantaged over agency-scale competitors. Maintain low fixed costs, modular contractor relationships rather than full-time hires, multiple small revenue streams rather than dependence on one big contract. Resilience IS the moat.",
    direct_quotes=[
        "Resilience is what stays small builds. Fragility is what scale builds.",
        "The company of one survives shocks that destroy the larger competitor."
    ],
    tags=["jarvis","resilience-over-scale","sniped-fragility-defense","cost-structure","modular-team"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="small-company-strategy",
    concept="Growth as a tax · scaling costs more than it generates",
    summary="Jarvis's accounting argument: most growth comes with hidden costs that don't appear in the revenue projections — management overhead, communication complexity, culture maintenance, recruiting and training time, infrastructure expansion, regulatory compliance, decision-making slowdowns. These costs scale faster than revenue at certain thresholds, which is why many businesses are MORE profitable at small scale than at large scale and why the path from $1M to $5M revenue often produces less owner-take-home than staying at $1M. Growth is taxed; the tax becomes visible only after the growth has already happened.",
    usable_principle="Growth carries hidden costs (management, communication, culture, recruiting, infrastructure, complexity) that often scale faster than revenue. Many businesses are more profitable at small scale than at large scale. Model the FULL cost of growth, not just the revenue side.",
    sniped_relevance="For SNIPED's Year-10 modeling, this means: $1.5-3M revenue at 4-7 person team is probably MORE profitable owner-take-home than $5-10M revenue at 15-25 person team. Don't model only the top-line; model the FULL stack of growth costs (BJ's management time, culture-maintenance overhead, recruiting cycles, infrastructure expansion, regulatory compliance, decision-making slowdown). The smaller, higher-margin path is often the better wealth outcome AND better life outcome.",
    direct_quotes=[
        "Growth is a tax that scales faster than revenue past certain thresholds.",
        "Many businesses are more profitable at small scale than at large scale; they just don't realize it until they've grown past the sweet spot."
    ],
    tags=["jarvis","growth-as-tax","sweet-spot","year-ten-modeling","profitability-vs-revenue"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="small-company-strategy",
    concept="The one customer · serve few deeply rather than many shallowly",
    summary="Jarvis's customer-base discipline: a company of one wins by serving a small number of customers deeply rather than a large number of customers shallowly. The economic argument: deep relationships produce more revenue per customer, more referrals per customer, and longer lifetime value per customer than shallow relationships. The qualitative argument: deep service is also more meaningful work for the operator, which sustains motivation across decades. The 'one customer' principle: design every interaction as though serving one specific person you care about, even when scaling that interaction across many customers.",
    usable_principle="Serve few customers deeply rather than many customers shallowly. Deep relationships compound through repeat business, referrals, and lifetime value. Shallow relationships extract one transaction and leave nothing behind.",
    sniped_relevance="For SNIPED's client model, this is structural. 60 founder portraits served deeply produces more revenue, referrals, and lifetime value than 600 served shallowly. The Reset $1,500 floor isn't despite being premium; the depth of service at the floor is the lower bound, and the Founder Tier and Brand System are deeper still. Resist any pressure to thin out the service to serve more clients per month. Depth IS the model.",
    direct_quotes=[
        "Serve one customer deeply rather than many shallowly.",
        "Lifetime value compounds in depth, not in breadth."
    ],
    tags=["jarvis","one-customer","depth-over-breadth","lifetime-value","reset-quality"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="small-company-strategy",
    concept="Teach everything you know · share to build authority",
    summary="Jarvis's counterintuitive content strategy: a company of one should teach EVERYTHING it knows, freely, in long-form content. The fear that 'teaching gives away the moat' is wrong — the moat is the operator's execution capacity, not the knowledge itself. Teaching builds the audience that hires you, the authority that justifies premium pricing, and the network that referrals flow through. The knowledge isn't what you sell; the execution is what you sell. Teaching the knowledge produces the customers for the execution.",
    usable_principle="Teach everything you know. Knowledge isn't the moat; execution is. Sharing knowledge builds the audience, authority, and network that drive premium service business. The fear of giving away the moat is misplaced.",
    sniped_relevance="For SNIPED's Cultural Doc + Direction Stack book strategy, this is the validation. Teach the methodology publicly. Share the Direction Stack frameworks. Document the principles. The fear that 'photographers will steal my methodology' is misplaced — the methodology is replicable, but the execution at SNIPED's level requires BJ's specific knowledge fusion. Teaching builds the founder audience that converts to clients. The book is the explicit teaching artifact.",
    direct_quotes=[
        "Teach everything you know.",
        "Knowledge is not the moat. Execution is. Teaching the knowledge builds the audience for the execution."
    ],
    tags=["jarvis","teach-everything","cultural-doc","direction-stack-book","audience-building"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="small-company-strategy",
    concept="Determining the right mind-set · purpose over passion",
    summary="Jarvis's reframe of the 'follow your passion' advice: passion is volatile and depletes under sustained pressure; purpose is durable and renews under pressure. A company of one needs a clear purpose (what is this business for, who does it serve, what does it stand against) more than it needs passionate enthusiasm. Purpose answers the question 'why keep going when it's hard?' which is the question every long-term business faces multiple times per year. Passion-driven businesses pivot constantly when the passion shifts; purpose-driven businesses persist through the seasons when the passion is low.",
    usable_principle="Build the business on purpose, not passion. Passion is volatile and depletes; purpose is durable and renews. The question 'why keep going when it's hard?' must have a purpose-level answer, not a passion-level one.",
    sniped_relevance="For SNIPED, the purpose is clear (per the meta-thesis in BJ's auto-memory): photography as proving ground for systems-as-creative-leverage; cultural documentary work that reframes who deserves visibility; the 10-year arc toward a 4-7 person team producing the Direction Stack book and the Cultural Doc as lasting artifacts. This purpose carries through low-passion days in ways no enthusiasm could. Re-read the meta-thesis when motivation flags; the purpose is the renewable energy source.",
    direct_quotes=[
        "Build on purpose, not passion.",
        "Passion depletes under pressure. Purpose renews."
    ],
    tags=["jarvis","purpose-over-passion","sniped-meta-thesis","long-arc-energy","operating-mindset"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="small-company-strategy",
    concept="Properly utilizing trust and scale · trust compounds, scale dilutes",
    summary="Jarvis's argument for why trust is more valuable than scale at company-of-one scale: trust compounds with each successful interaction (each happy customer increases the next customer's willingness to engage); scale dilutes the operator's per-customer attention and erodes the trust that drove the early growth. The discipline: invest disproportionately in the trust signals (named clients, transparent process, predictable quality, personal accountability) and resist the scale moves that would compromise the per-customer attention. Trust is the company-of-one's defensive moat AND offensive growth lever.",
    usable_principle="At small scale, trust compounds and scale dilutes. Invest disproportionately in the signals that build trust (named clients, transparency, predictability, personal accountability). Resist scale moves that compromise per-customer attention.",
    sniped_relevance="For SNIPED, this validates the named-client portfolio strategy, the personal accountability in every client interaction, the transparency of the Direction Stack process, the predictability of quality across engagements. These are not 'nice-to-haves' — they are the trust-compounding machinery that makes the company-of-one model work. Resist scale moves (e.g., hiring multiple photographers to deliver under the SNIPED brand) that would dilute the trust signal.",
    direct_quotes=[
        "Trust compounds. Scale dilutes.",
        "The company of one's moat is the trust per customer, not the customers per month."
    ],
    tags=["jarvis","trust-compounds","named-client-strategy","scale-dilutes","sniped-moat"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="small-company-strategy",
    concept="Launching and iterating in tiny steps · the small-batch growth model",
    summary="Jarvis's operational discipline for company-of-one growth: prefer small, frequent, reversible experiments over large, infrequent, irreversible bets. Launch a new offering as a tiny test (10 customers, 30 days, manual fulfillment) before scaling it. Iterate on real customer feedback rather than projected market analysis. This approach trades off potential upside for substantially reduced downside risk — a company of one cannot survive a big failed bet, but can survive (and learn from) dozens of small failed experiments.",
    usable_principle="Launch in tiny, reversible steps. Real customer feedback from 10 customers beats projected market analysis for 1,000. Large irreversible bets are inappropriate for company-of-one risk capacity; small reversible experiments are the right size.",
    sniped_relevance="For SNIPED's new offer/tier/product experiments, this is the disciplined approach. Don't launch the Direction Stack book to the world cold; test the book's premise with 10 trusted readers first. Don't launch a workshop tier publicly; test it with 5 invited founders first. Don't expand into a new geographic market with a big push; test with 3-5 introductory engagements. Each iteration teaches more than the projection-based version would.",
    direct_quotes=[
        "Launch in tiny steps. Iterate on real feedback.",
        "Company-of-one risk capacity is too small for big bets. Small bets compound through learning."
    ],
    tags=["jarvis","small-batch-growth","tiny-launches","sniped-experiments","reversible-bets"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="small-company-strategy",
    concept="The hidden value of relationships · weak ties as opportunity infrastructure",
    summary="Jarvis's argument for why company-of-one operators should invest deliberately in weak-tie relationships (acquaintances, former colleagues, online connections, periodic contacts) rather than only strong-tie close networks. The classic Granovetter finding: most opportunities come through weak ties, not strong ties, because weak ties carry information from outside your immediate network. For a company of one, the weak-tie network IS the marketing infrastructure — the source of referrals, the audience for the content, the pool of potential collaborators and clients. Investing in the network is investing in the business's opportunity surface area.",
    usable_principle="Weak ties carry more opportunity flow than strong ties. Invest deliberately in maintaining a broad weak-tie network (former colleagues, online connections, periodic acquaintances). For a company of one, the weak-tie network IS the marketing infrastructure.",
    sniped_relevance="For SNIPED, this validates the LinkedIn VIB strategy and the broader founder-network cultivation. Each founder portrait subject becomes a weak-tie node that carries SNIPED's reputation into their own networks. The LinkedIn comment doctrine (5-10 comments/day) is weak-tie maintenance at scale. Don't only invest in current clients (strong ties); systematically maintain the much-larger weak-tie network because that's where the future opportunities flow from.",
    direct_quotes=[
        "Weak ties are the marketing infrastructure of the company of one.",
        "Most opportunities come through people you barely know, not the ones closest to you."
    ],
    tags=["jarvis","weak-ties","linkedin-vib","granovetter","network-as-infrastructure"]
)

print(f"After cluster 7 (Jarvis · 9 chunks): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 8 · RYAN HOLIDAY · PERENNIAL SELLER
# Creative process, positioning, marketing, platform · 4 parts
# =============================================================
STITLE = "Perennial Seller"
SFILE = "perennial_seller_holiday.md"
AUTHOR = "Ryan Holiday"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="patience",
    concept="The perennial seller · work that lasts decades, not weeks",
    summary="Holiday's central thesis: most creative work and marketing chases the launch — the splashy debut, the viral moment, the first-week numbers. But the work that produces lasting wealth and impact is the perennial seller — the book, song, product, or business that continues to find new audiences for decades because the underlying value transcends its launch moment. Examples: Iron Maiden's albums (40+ years of continuous sales), Shawshank Redemption (bombed at launch, became all-time favorite over 20 years), Star Wars (the franchise vs the original film's opening weekend). The strategic question: are you building for the launch or for the long-tail?",
    usable_principle="Build for the long-tail, not the launch. The launch is a moment; the perennial seller produces returns for decades. Most marketing chases the launch metric and ignores the long-tail economics that actually produce wealth.",
    sniped_relevance="For SNIPED's Direction Stack book launch strategy, this is the operating frame. Don't optimize the launch for first-week sales; optimize the book for sustained sales over the next 20 years. The launch is a setup, not the goal. The Cultural Doc essays follow the same pattern: each one is intended to be valuable 10 years after publication, not just in the launch week. Build perennial assets, not seasonal hits.",
    direct_quotes=[
        "The launch is a moment. The perennial seller produces returns for decades.",
        "Iron Maiden hasn't had a hit single in 40 years and yet they make more money than 95% of working musicians."
    ],
    tags=["holiday","perennial-seller","direction-stack-book","long-tail","launch-vs-life"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="creative-process",
    concept="The right mindset · make work that is worth making",
    summary="Holiday's foundational creative discipline: before any marketing or platform question, the work must be worth making. The first filter: would you still make this if you knew it wouldn't sell? The second filter: are you making it because the world genuinely needs it, or because you want the rewards of making it? Perennial sellers are made by people who would have made the work anyway, who are answering a question they personally need answered, and who are willing to invest the years required to make it actually good. Marketing cannot save work that fails this filter; marketing can only amplify work that passes it.",
    usable_principle="Make work that is worth making. The first filter: would you make it anyway if it wouldn't sell? Marketing amplifies work; it doesn't redeem work that wasn't worth making. Spend the years required to make the work actually good.",
    sniped_relevance="For SNIPED's Direction Stack book, the test is: would BJ write this book even if it sold zero copies? If yes, the foundation is right and marketing investment is justified. If no, the book is a marketing artifact disguised as a book and won't perennially sell. Same test for every Cultural Doc essay: is this an essay that needs to exist, or is it content marketing pretending to be thought leadership? The honest answer determines whether each piece will compound or fade.",
    direct_quotes=[
        "Would you make this work even if it wouldn't sell? That's the filter.",
        "Marketing amplifies. It does not redeem."
    ],
    tags=["holiday","worth-making","direction-stack-test","cultural-doc-filter","compounding-content"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="creative-process",
    concept="Iron Maiden's patience · 40 years of compound work",
    summary="Holiday's signature case study: Iron Maiden has been a working band since 1975 and has built an enormous, devoted, multigenerational fanbase without ever having a top-40 hit single. Their model: tour relentlessly for decades, release albums consistently, treat the work as a long-term craft rather than a hit-chasing career. They aren't waiting for a viral moment; they're compounding fan loyalty year after year through sustained commitment to the work. The financial result: they earn more annually than 95% of musicians who chase hits. The discipline result: they've built a creative legacy that will outlast their lifespans.",
    usable_principle="The compound work of decades beats the hit-chase of years. Iron Maiden's career is the playbook: tour, release, repeat, never compromise the work, ignore the trend cycles. Compound through patient consistency, not through hit-chasing.",
    sniped_relevance="For SNIPED's 10-year arc, this is the morale-sustaining case. The Cultural Doc essays, the founder portraits, the Direction Stack methodology development — all compound through patient consistency. There won't be a viral moment that 'makes' SNIPED; there will be 10 years of consistent work that compounds into a position no one can take away. Resist the pressure to chase virality, hot takes, or trend-cycle relevance.",
    direct_quotes=[
        "Iron Maiden's career is the patience playbook.",
        "Tour. Release. Repeat. Never compromise the work. Ignore the trend cycles."
    ],
    tags=["holiday","iron-maiden","patience-playbook","sniped-ten-year-morale","compound-consistency"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="creative-process",
    concept="Positioning · find the niche that needs you specifically",
    summary="Holiday's positioning discipline for creative work: don't try to position broadly to capture the largest possible audience; position specifically to capture the audience that specifically needs what only you can offer. Broad positioning produces shallow connection with large audiences; specific positioning produces deep connection with small audiences that becomes the seed of long-term loyalty. The math: 1,000 true fans (Kevin Kelly) who pay $100/year for your work generates $100K/year — a perennial-seller-level outcome — and 1,000 specifically-positioned fans is much easier to acquire than 100,000 broadly-positioned ones.",
    usable_principle="Position specifically, not broadly. 1,000 true fans (specific positioning) generates more sustainable income than 100,000 shallow fans (broad positioning). The deeper you go, the smaller and more loyal the audience.",
    sniped_relevance="For SNIPED, this validates the narrow founder-photography positioning. SNIPED is not 'a photographer' broadly; SNIPED is 'the premium founder photographer with the Direction Stack methodology and anti-AI position.' This narrow positioning produces deep connection with a small audience (founders in specific scenes) that compounds via referrals. Resist any broadening that would dilute the specific positioning even when the broader audience looks attractive.",
    direct_quotes=[
        "Position specifically. Not broadly.",
        "1,000 true fans is a perennial seller. 100,000 shallow fans is a launch."
    ],
    tags=["holiday","specific-positioning","true-fans","sniped-narrow","kevin-kelly"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="distribution",
    concept="Marketing as ongoing, not one-shot · the perennial promotional arc",
    summary="Holiday's marketing discipline: most launches think of marketing as a discrete burst around release (the launch week, the press tour, the ad spend). Perennial sellers treat marketing as ongoing — the launch is one inflection, but the marketing continues for years after, finding new audiences, capturing new moments, riding the new contexts that make the work suddenly relevant again. The implication: build marketing infrastructure that will continue working without daily attention (evergreen content, automated funnels, repeat-able rituals) rather than burning all marketing budget on the launch moment.",
    usable_principle="Marketing is ongoing, not one-shot. Build infrastructure that continues working for years (evergreen content, automated funnels, repeat rituals). Most launches over-invest in the launch moment and under-invest in the years of marketing that produce perennial-seller economics.",
    sniped_relevance="For SNIPED's Direction Stack book launch (Year 2-3), structure the marketing as a 10-year campaign, not a launch week. Evergreen book-relevant Cultural Doc essays, repeating workshop cadence, sustained LinkedIn presence, recurring case-study releases. The book's launch week should produce a moderate spike; the next 10 years should produce the actual sales. Build the ongoing infrastructure before the launch, not after.",
    direct_quotes=[
        "Marketing is ongoing, not one-shot.",
        "The launch is one inflection. The marketing continues for years."
    ],
    tags=["holiday","ongoing-marketing","direction-stack-launch","evergreen-infrastructure","ten-year-campaign"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="distribution",
    concept="The platform · build the audience before you need to sell to it",
    summary="Holiday's strategic discipline for any perennial-seller path: the platform (email list, audience, fan base, network) must be built BEFORE the launch, not after. The launch leverages existing platform; trying to build platform during launch is too late. The implication: every creative person operating in a long-arc strategy should treat platform-building as ongoing infrastructure investment — not glamorous, not directly monetized, but compounding. The platform is what lets you launch new work without starting from zero each time.",
    usable_principle="Build the platform before you need it. Email list, audience, fan base, network — all should be growing for years before the launch. Trying to build platform during launch is too late. Treat platform as infrastructure investment, not marketing tactic.",
    sniped_relevance="For SNIPED, the platform-building work IS the LinkedIn audience growth + Cultural Doc readership + founder-network cultivation happening now in Year 1-2. None of this is directly monetized this year. All of it is the platform that the Direction Stack book + future products will launch into in Year 2-3+. Protect the platform-building time even when it competes with directly-revenue-generating work. The platform is the long-term wealth-creator.",
    direct_quotes=[
        "Build the platform before you need it.",
        "The launch leverages the platform you already have. You cannot build platform during launch."
    ],
    tags=["holiday","platform-first","linkedin-growth","cultural-doc","year-one-investment"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="distribution",
    concept="Fans, not customers · the relationship-as-asset frame",
    summary="Holiday's framing distinction: a customer is someone who bought one thing once; a fan is someone who is invested in your work and will buy whatever you make next. Perennial sellers are sustained by fans, not customers. The work to convert customers to fans (after-sale engagement, ongoing communication, behind-the-scenes access, community-building) is what creates the perennial economics. Most businesses optimize for customer acquisition and ignore customer-to-fan conversion; perennial sellers invert this priority — once you have a customer, your primary work is making them a fan.",
    usable_principle="Customers buy once; fans buy everything. Once you have a customer, your primary work is converting them to a fan via after-sale engagement, ongoing communication, behind-the-scenes access, and community. Customer acquisition is the start; fan conversion is the wealth.",
    sniped_relevance="For SNIPED, this is the post-delivery discipline. Every Reset client should be cultivated toward fan status: post-delivery follow-up, ongoing LinkedIn engagement, inclusion in the Cultural Doc audience, notification when the Direction Stack book launches, invitation to future workshops. The transition from 'photographed once' to 'invested in BJ's work' is what produces lifetime referrals and repeat engagements. Build the fan-conversion machinery deliberately.",
    direct_quotes=[
        "Customers buy once. Fans buy everything.",
        "The work to make a customer a fan is the work that creates the perennial seller."
    ],
    tags=["holiday","fans-not-customers","post-delivery","client-lifecycle","sniped-fanbase"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="creative-process",
    concept="The dip · the slog between launch and traction",
    summary="Holiday draws on Seth Godin's 'The Dip': between launch (initial enthusiasm) and traction (sustainable success), every creative project goes through The Dip — a period of months or years where the work hasn't yet found its audience, motivation flags, and the rational case for quitting is strong. Most projects die in The Dip because the people running them mistook the launch enthusiasm for traction. The discipline: anticipate The Dip, plan to survive it (financially, emotionally, structurally), and recognize that the projects that produce perennial-seller outcomes are the ones whose creators didn't quit during the slog.",
    usable_principle="The Dip is the gap between launch enthusiasm and sustainable traction. Most projects die in The Dip because creators mistook launch enthusiasm for arrival. Anticipate The Dip; plan to survive it (financially, emotionally, structurally). The perennial sellers belong to those who didn't quit.",
    sniped_relevance="For SNIPED, this calibrates expectations. The current Year-1 work is pre-Dip launch phase. The Dip will likely arrive in Year 2-3 when the initial enthusiasm has worn off, the early founder clients are served, the LinkedIn growth plateaus, and the book launch hasn't yet produced its long-tail returns. Anticipate this. Plan the financial runway, the personal-sustainability practices, the operational rhythm to survive 18-24 months of slog without abandoning the strategy. The Dip is where the perennial-seller status is earned.",
    direct_quotes=[
        "The Dip is where most projects die.",
        "The projects that become perennial sellers are the ones whose creators didn't quit during the slog."
    ],
    tags=["holiday","the-dip","year-two-three","seth-godin","sustained-commitment"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="creative-process",
    concept="The conclusion · luck favors the prepared and the persistent",
    summary="Holiday's closing reflection on the role of luck in perennial-seller outcomes: yes, luck matters — but luck favors people who have prepared their work to deserve it and who have persisted long enough for opportunity to find them. The 'overnight success' narrative obscures the years of unrewarded preparation that came before. The discipline: do the preparation work (craft, positioning, platform, network) regardless of when or whether the lucky break arrives, because it's preparation + persistence that converts luck into actual outcomes. The unprepared can't capitalize on luck; the impatient quit before luck shows up.",
    usable_principle="Luck matters, but luck favors the prepared and the persistent. Do the preparation work (craft, positioning, platform, network) regardless of timing. Stay long enough for luck to find you. The unprepared can't capitalize; the impatient quit too early.",
    sniped_relevance="For SNIPED's 10-year arc, this is the closing morale frame. The lucky breaks (the founder who unexpectedly becomes culturally significant, the press feature that lifts a Cultural Doc essay, the book that becomes a category-defining reference) will arrive — but only if BJ is still doing the disciplined work when they show up, and only if the work is good enough to capitalize on them. Stay prepared. Stay persistent. The luck will come.",
    direct_quotes=[
        "Luck favors the prepared and the persistent.",
        "What looks like overnight success is years of preparation meeting a lucky moment."
    ],
    tags=["holiday","luck-and-preparation","ten-year-arc","sustained-readiness","sniped-morale"]
)

print(f"After cluster 8 (Holiday · 9 chunks): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 9 · ANITA ELBERSE · BLOCKBUSTERS
# Bet big or don't bet · superstar economics · distribution dominates
# =============================================================
STITLE = "Blockbusters"
SFILE = "blockbusters_elberse.md"
AUTHOR = "Anita Elberse"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="The blockbuster strategy · concentrate resources on hit potential",
    summary="Elberse's central counterintuitive thesis from studying Hollywood, NBC, book publishing, and music: in entertainment industries, the rational strategy is to bet big on a small number of likely hits and accept that most of the others will fail. The intuitive alternative (spread resources evenly across many projects to diversify risk) actually produces worse outcomes because the few hits drive ALL the returns and the spread-out approach starves them of the budget needed to become hits. The math: in markets with extreme outcome variance, concentration beats diversification because the upside is dramatically asymmetric.",
    usable_principle="In high-variance markets, concentrate resources on the few bets with hit potential rather than spreading evenly across many. Diversification feels safer but produces worse outcomes when the upside is dramatically asymmetric. Bet big or don't bet.",
    sniped_relevance="For SNIPED's project portfolio, this means: don't spread BJ's attention evenly across all current initiatives. Concentrate on the few that could produce blockbuster-scale outcomes (the Direction Stack book as a definitive category reference; named founder portraits that could go viral if the founder becomes culturally significant; the Cultural Doc essays that could establish SNIPED as the cultural-authority anchor in premium founder photography). Other initiatives get maintenance-level attention, not equal investment.",
    direct_quotes=[
        "The blockbuster strategy is concentration, not diversification.",
        "Betting heavily on likely blockbusters and spending considerably less on the also-rans is the surest way to lasting success in show business."
    ],
    tags=["elberse","blockbuster-strategy","resource-concentration","direction-stack-bet","power-law"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Superstar economics · the few dominate the many",
    summary="Elberse documents the empirical reality of entertainment economics: a tiny percentage of artists, films, books, and shows generate the overwhelming majority of revenue. The top 1% of films generate roughly 50% of box office; the top 1% of musicians earn roughly 70% of music revenue; similar patterns in books, TV, and increasingly in any creator-economy market. The dynamic is reinforcing: superstars get more distribution because they generate more revenue, which generates more distribution. The implication for any business adjacent to superstars: the value of association with a superstar is dramatically higher than association with average performers.",
    usable_principle="Superstar economics: the top few generate the majority of returns; association with superstars produces dramatically more value than association with average performers. In any market with these dynamics, position yourself to be adjacent to or recognized by the superstars.",
    sniped_relevance="For SNIPED's Founder Tier strategy, this is the structural argument. Photographing 60 founders is useful; photographing 3-5 founders who go on to be the next generation's defining superstar founders (the next Patrick Collison, Tobi Lütke, Tracy Young) produces 10-100x the brand value of the other 55 combined. The investment in picking which founders to court for Founder Tier should weight 'likely superstar trajectory' heavily, not 'good fit for the work' alone.",
    direct_quotes=[
        "The few dominate the many.",
        "Association with a superstar produces dramatically more value than association with average performers."
    ],
    tags=["elberse","superstar-economics","founder-tier-selection","power-law-investments","sniped-trajectory-picking"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="distribution",
    concept="Distribution dominates · marketing budget beats production budget",
    summary="Elberse's hardest finding for creative people: in entertainment industries, the size of the marketing/distribution budget predicts commercial success more reliably than the size of the production budget. A great film with no marketing reaches no one; a mediocre film with massive marketing reaches everyone. The implication is not that quality doesn't matter (it matters for long-tail and reputation), but that distribution is the binding constraint that determines whether anyone discovers the work in the first place. The industry that fails to budget for distribution loses to the industry that does, regardless of relative production quality.",
    usable_principle="Distribution is often the binding constraint, not production quality. Great work with no distribution reaches no one. Budget distribution as seriously as production; the asymmetry between them is the structural reason most great work goes undiscovered.",
    sniped_relevance="For SNIPED's Direction Stack book and Cultural Doc essays, this validates investing in distribution infrastructure (the LinkedIn audience, the email list, the founder-network referral pathways) as seriously as the content creation itself. Spending 100% of time on the book and 0% on distribution will produce a great unread book. Spend roughly equal time on both. For the book launch specifically: budget distribution work (paid amplification, podcast tours, partnership outreach) as a serious line item, not an afterthought.",
    direct_quotes=[
        "Distribution dominates.",
        "Great work without distribution reaches no one; mediocre work with massive distribution reaches everyone."
    ],
    tags=["elberse","distribution-dominates","book-launch-budget","linkedin-investment","distribution-as-production"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="distribution",
    concept="The long-tail myth · concentration is increasing, not decreasing",
    summary="Elberse's empirical pushback on the long-tail thesis (Chris Anderson's argument that digital distribution would democratize markets and the long-tail would grow): the data shows the opposite. Digital distribution has CONCENTRATED markets, not diversified them. The top performers capture an even larger share than they did in the pre-digital era because winners benefit disproportionately from algorithmic recommendation, network effects, and social proof. The 'long-tail' of niche products exists but represents a shrinking, not growing, share of total spending. The implication: don't bet your strategy on the long-tail; bet on being one of the few winners or on serving a tiny premium niche.",
    usable_principle="Digital markets concentrate, not democratize. The long-tail is shrinking, not growing. Bet on being one of the few winners or on serving a premium niche so small that the concentration dynamics don't apply. Don't bet on 'discoverability through niche aggregation.'",
    sniped_relevance="For SNIPED, this means: don't bet on Instagram or TikTok algorithmic distribution to find audience organically (long-tail discoverability is shrinking). Bet on the premium-niche strategy (founders specifically) where SNIPED can be one of the few definitive providers, AND bet on owned distribution (email list, direct relationships) where algorithmic concentration doesn't apply. The premium-niche + owned-distribution combination is the response to the concentration dynamic.",
    direct_quotes=[
        "Digital markets concentrate. They do not democratize.",
        "The long tail is shrinking, not growing. The winners take more."
    ],
    tags=["elberse","long-tail-myth","concentration-increasing","premium-niche","owned-distribution"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Tentpole strategy · the named, marketed event releases",
    summary="Elberse's structural argument for Hollywood's tentpole-release strategy: a few times per year, studios put massive marketing budget behind named, branded, event-style releases that crowd out all other films during their release windows. The tentpole captures disproportionate attention, generates the year's revenue, and absorbs the risk that would have been spread across many films. The non-tentpole releases get minimal marketing and function as filler. The strategic insight: in attention-scarce markets, concentrating attention on a few branded events beats spreading attention across many unbranded products.",
    usable_principle="In attention-scarce markets, tentpole branded events beat continuous unbranded output. Concentrate marketing attention on a few major releases that get the full treatment; let other output be filler that maintains the rhythm but doesn't try to be the moment.",
    sniped_relevance="For SNIPED's content cadence, this means structuring around a few tentpole releases per year (the Direction Stack book, major Cultural Doc essays, anniversary case studies) that get the full marketing investment, rather than trying to make every weekly post a major event. The chapter-rollout doctrine (3-5 grid posts per chapter) is consistent with this — chapters are the tentpoles; individual posts are the rhythm. Don't dilute the tentpole attention by treating every post as equally important.",
    direct_quotes=[
        "Tentpole strategy: concentrate marketing on a few branded events.",
        "In attention-scarce markets, a few major releases beat continuous unbranded output."
    ],
    tags=["elberse","tentpole-strategy","chapter-rollout","content-cadence","attention-economics"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="The named-talent multiplier · stars carry more than their performance",
    summary="Elberse's economic analysis of why studios pay astronomical fees to named stars: the star carries proven box-office draw, automatic media attention, awards-circuit eligibility, foreign-market sales (key for international box office), and franchise-anchor potential — all of which dramatically reduce the studio's commercial risk. The cost of a star (e.g., $20-30M for a top-tier actor) is dwarfed by the revenue insurance the star provides. The cheaper unknown actor option looks like savings on paper but eliminates the risk-reduction the star delivered. Same dynamic operates in any market where named talent reduces commercial uncertainty.",
    usable_principle="Named talent carries commercial value far beyond their performance contribution: attention, awards, international markets, franchise anchoring. The cost of named talent is often dwarfed by the risk reduction they provide. Cheaper unknown talent is rarely the savings it appears.",
    sniped_relevance="For SNIPED's Founder Tier and Brand System pricing, this validates premium fees for working with high-profile founders even when the work itself is similar. The founder isn't paying for the photography; they're paying for the SNIPED brand association (named-talent multiplier applied to the photographer side of the transaction). As SNIPED's brand grows, the named-talent premium grows. Conversely: SNIPED associating with named founders multiplies SNIPED's brand value disproportionately to the photography cost.",
    direct_quotes=[
        "Named talent carries commercial value far beyond performance contribution.",
        "The cost of stars is dwarfed by the revenue insurance they provide."
    ],
    tags=["elberse","named-talent-multiplier","founder-tier-pricing","sniped-brand-multiplier","reciprocal-association"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Risk concentration as strategy · accept the variance to capture the upside",
    summary="Elberse's underlying philosophical argument: the blockbuster strategy requires accepting much higher variance than the diversified strategy. Years with hits dramatically outperform; years without hits dramatically underperform. The discipline is having the capital and patience to absorb the down years in exchange for capturing the up years. Most businesses can't tolerate the variance and choose diversification — which is why so few capture the blockbuster economics that compound to industry dominance. The few that can tolerate the variance (Disney, Marvel, Pixar, the major labels) capture the lion's share of total returns.",
    usable_principle="Blockbuster economics require tolerating variance. Down years are part of the strategy, not failure. Have the capital reserves and the conviction to absorb them. Diversification feels safer but caps your upside; concentration with variance tolerance captures the asymmetric returns.",
    sniped_relevance="For SNIPED's financial planning, this means: maintain capital reserves not just for the rainy day but for the multi-quarter slog between major wins. The Direction Stack book may produce its largest returns in Year 4-5 (cumulative back-catalog sales), not Year 2-3 (launch). Plan the financial structure to absorb 18-24 months of below-trend returns in exchange for capturing the asymmetric long-tail upside. The variance is the strategy, not the risk.",
    direct_quotes=[
        "The blockbuster strategy requires tolerating variance.",
        "Down years are part of the strategy. Have the reserves and the conviction to absorb them."
    ],
    tags=["elberse","variance-tolerance","capital-reserves","sniped-financial-planning","asymmetric-returns"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Why the small-bet strategy structurally underperforms",
    summary="Elberse's careful empirical case against the alternative strategy: spreading resources evenly across many small bets sounds prudent but structurally underperforms in entertainment-style markets. The reason: the small bets get insufficient marketing to break through (distribution is the binding constraint), the talent associated with them gets less attention, the discovery algorithms favor higher-budget releases, and the cumulative inefficiency means the portfolio of small bets underperforms what a single large bet with the same total budget would have produced. The 'diversified small-bets' portfolio loses to the concentrated big-bet portfolio in essentially every entertainment subsector studied.",
    usable_principle="The 'diversified small-bets' strategy structurally underperforms in markets where distribution and attention are the binding constraints. Small bets get insufficient distribution to break through; the same total budget concentrated into one large bet captures the asymmetric upside the small bets cannot.",
    sniped_relevance="For SNIPED's content and offering strategy, resist the temptation to launch many small experimental offerings. Concentrate the launch resources on one or two major bets (the Direction Stack book, a definitive Cultural Doc essay, the Founder Tier signature shoot) rather than spreading across five lesser projects. The math says the concentrated approach wins even when the small-bets approach feels safer. Apply this filter when prioritizing the next 12 months of strategic moves.",
    direct_quotes=[
        "The diversified small-bets strategy structurally underperforms.",
        "Small bets get insufficient distribution to break through; concentration captures the upside they cannot."
    ],
    tags=["elberse","small-bets-fail","concentration-discipline","sniped-prioritization","strategic-filter"]
)

print(f"After cluster 9 (Elberse · 8 chunks): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 10 · DAVID SAX · THE REVENGE OF ANALOG
# Why analog wins · the AI-defense precedent
# =============================================================
STITLE = "The Revenge of Analog"
SFILE = "revenge_of_analog_sax.md"
AUTHOR = "David Sax"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="analog-premium",
    concept="The revenge of analog · why physical comes back when digital dominates",
    summary="Sax's central observation: the more digital saturates a category, the more value the surviving analog form takes on. Vinyl records, hardcover books, paper notebooks, board games, film cameras, print magazines, brick-and-mortar bookstores — all of these were declared dead by the digital triumphalists and all have grown significantly in the period when their digital substitutes became ubiquitous. The mechanism is not nostalgia; it is functional: analog forms offer experiences (tactile, social, focused, durable) that digital substitutes cannot deliver. As digital becomes the default, analog becomes the deliberate premium choice.",
    usable_principle="The more a category goes digital, the more value the surviving analog form takes on. Analog premium isn't nostalgia — it's functional: tactile, social, focused, durable. Position deliberately analog in industries that are racing to digital; the deliberateness IS the premium.",
    sniped_relevance="For SNIPED's anti-AI position, this is the historical precedent. Every prior cycle where the digital substitute saturated a creative category (CDs → vinyl, e-books → print, digital cameras → film) produced the same pattern: the analog premium grew as digital saturated. Photography is now in that cycle with AI as the digital saturator. SNIPED's anti-AI, in-camera, identity-preserving position is the analog-revenge play applied to the photography market. The pattern is documented; the play has worked before.",
    direct_quotes=[
        "The more digital saturates a category, the more value the surviving analog form takes on.",
        "Vinyl, print, film, paper — declared dead by digital triumphalists, all growing in the period when digital became ubiquitous."
    ],
    tags=["sax","analog-revenge","ai-defense-precedent","sniped-positioning","digital-saturation-pattern"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="analog-premium",
    concept="Vinyl's resurrection · the case study for analog renaissance",
    summary="Sax documents vinyl's case in detail: declared dead by the CD in the 1980s, declared deader by MP3s in the 2000s, vinyl revenue grew from ~$3M in 1993 to ~$1B+ by 2020 — a 300-fold increase in the era when digital music became free and ubiquitous. The growth wasn't nostalgia (most vinyl buyers are too young to remember pre-CD music); it was driven by the tactile experience (cover art, liner notes, ritual of placing the needle), the focused listening (vinyl forces full-album engagement vs digital's track-skipping), and the social object (vinyl in the room is a conversation piece in a way streaming isn't). The features digital eliminated were features people valued.",
    usable_principle="Track which features the digital substitute eliminated in your industry. Those eliminated features are often the foundation of the analog premium that emerges later. The features digital optimizes away are frequently the features people valued most.",
    sniped_relevance="For SNIPED, the features AI photography eliminates are exactly the foundation of the analog-photography premium: the identity-preserving accuracy (AI hallucinates faces); the relational experience of being seen by a human photographer (AI is anonymous extraction); the cultural-authority transfer from photographer-as-author (AI dilutes attribution); the durability of a hand-crafted image (AI work ages poorly as the underlying models improve). Each of these is the foundation of SNIPED's premium. Name them in the Cultural Doc; they are the moat.",
    direct_quotes=[
        "Vinyl grew 300-fold in the era when digital music became free and ubiquitous.",
        "The features digital eliminated were the features people valued most."
    ],
    tags=["sax","vinyl-case-study","eliminated-features","sniped-moat-features","cultural-doc-content"]
)

add(
    source_title=STijTLE if False else STITLE, source_file=SFILE, author=AUTHOR,
    domain="analog-premium",
    concept="The tactile premium · physical objects carry weight digital can't",
    summary="Sax's analysis of why physical objects retain value: they exist in space, can be held, can be displayed, can be given as gifts, can be inherited, cannot be deleted by a software update or a corporate policy change. The tactile premium is not aesthetic preference; it is the functional reality that physical artifacts have ontological permanence that digital files do not. The buyer of a physical book owns it; the buyer of an e-book licenses access to it. The buyer of a print owns it; the buyer of a digital file owns rights subject to terms-of-service. This permanence difference compounds value over time.",
    usable_principle="Physical objects have ontological permanence that digital files lack — they can't be deleted, updated away, or revoked. As digital ephemerality becomes more visible, physical permanence becomes more valuable. Build physical artifacts deliberately when permanence matters to the buyer.",
    sniped_relevance="For SNIPED's deliverable design, this validates investing in physical artifacts: hand-signed prints in the delivery package, printed Direction Stack book (not just digital), printed reference materials in the welcome packet. Each physical artifact carries the permanence premium that a Pixieset gallery alone cannot. The physical artifact also occupies the founder's office/home as an ongoing presence, which is itself ongoing brand exposure. Budget physical artifacts deliberately, not as luxury but as functional permanence.",
    direct_quotes=[
        "Physical objects cannot be deleted by a software update.",
        "The buyer of a physical book owns it. The buyer of a digital file licenses access subject to terms-of-service."
    ],
    tags=["sax","tactile-premium","physical-artifacts","permanence","delivery-design"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="analog-premium",
    concept="Analog as deliberate choice · the rejection-of-default premium",
    summary="Sax notes that analog purchasing is increasingly a deliberate refusal of the digital default. The buyer of a vinyl record could have bought the MP3 or streamed for free; they chose the analog with full knowledge of the digital alternative. This deliberateness itself is part of the premium: the analog buyer is making a statement about what they value (the experience, the craftsmanship, the social object) and signaling membership in a community that values the same. Default consumers buy digital; deliberate consumers buy analog. The deliberate-consumer market is smaller but more loyal, more vocal, and more willing to pay premium.",
    usable_principle="Analog purchasing is increasingly a deliberate refusal of digital defaults. The deliberateness is part of the premium. The market for deliberate consumers is smaller but more loyal and pays higher prices. Position to attract deliberate consumers, not default consumers.",
    sniped_relevance="For SNIPED, this is the structural argument for being anti-AI publicly rather than quietly. The deliberate-consumer founder who chooses SNIPED is making a statement about what they value (craft, identity-preservation, human relationship) and signaling membership in an anti-AI-default community. The Cultural Doc essay 'On Refusing to Use AI' makes the deliberate-choice frame explicit. This filters out the default-consumer founders (good, they would have been wrong-fit anyway) and attracts the deliberate-consumer founders who pay premium.",
    direct_quotes=[
        "Analog purchasing is deliberate. Digital purchasing is default.",
        "The deliberate-consumer market is smaller but pays premium and stays loyal."
    ],
    tags=["sax","deliberate-consumer","anti-ai-position","cultural-doc","sniped-buyer-filter"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="analog-premium",
    concept="The independent bookstore renaissance · physical retail returns",
    summary="Sax documents the surprising growth of independent bookstores in the 2010s — a sector declared dead by Amazon's rise. Independent bookstore count grew from a 2009 low to substantial year-over-year increases through the late 2010s. The mechanism: independent bookstores offer curation (an expert's selection vs algorithmic recommendations), community (events, book clubs, gathering spaces), and serendipity (the wandering discovery vs the search-bar query) that Amazon cannot deliver. The premium book buyer increasingly chose the independent store for these features even when the price was higher and the convenience lower.",
    usable_principle="Even in categories where digital scale dominates, physical alternatives offering curation, community, and serendipity can find growing premium audiences. The features the digital giant cannot offer (expert curation, social space, surprise discovery) become the foundation of the analog alternative.",
    sniped_relevance="For SNIPED's brand-building, the parallel is: the photography market is increasingly dominated by AI tools and algorithmic discovery. The 'independent bookstore equivalent' for SNIPED is offering curation (BJ's expert judgment vs AI generation), relationship (the Direction Stack consultation vs anonymous extraction), serendipity (the unexpected portrait moment vs predictable output). Position these as the explicit differentiators. The Cultural Doc plays the bookstore-curator role for the founder audience.",
    direct_quotes=[
        "Independent bookstores grew in the era when Amazon dominated.",
        "Curation, community, and serendipity are the features the digital giant cannot offer."
    ],
    tags=["sax","bookstore-renaissance","curation-community-serendipity","sniped-differentiators","amazon-parallel"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="analog-premium",
    concept="The paper notebook persistence · why digital didn't replace pen",
    summary="Sax documents the persistence (and growth) of premium paper notebooks (Moleskine, Field Notes, Leuchtturm) in the era of digital note-taking apps. The mechanism is multiple: handwriting produces better memory encoding than typing (well-documented research); paper notebooks have no notifications, no distractions, no temptation to multitask; the constraint of paper forces selective writing (you can't infinite-scroll a notebook); and the physical artifact remains accessible without battery, login, or app updates. The premium notebook market grew during the digital note-taking app explosion, validating the analog-revenge pattern in a different category.",
    usable_principle="Categories where the digital substitute carries hidden costs (distraction, distraction, ephemerality) often see the analog form persist and grow as the digital substitute's hidden costs become visible. Track which 'free' digital substitutes carry hidden costs that drive users back to paid analog forms.",
    sniped_relevance="For SNIPED, this is a cross-category validation that the pattern is robust. AI photography (the 'free' digital substitute) carries hidden costs: identity drift, depersonalization, attribution dilution, model-update brittleness. As these hidden costs become visible to founder buyers (e.g., when an AI-generated headshot starts looking dated as models improve, or when peers identify it as AI-generated), the analog premium grows. Be the analog option that's already established when the hidden costs become visible.",
    direct_quotes=[
        "Categories where digital substitutes carry hidden costs see analog persist.",
        "The 'free' digital substitute is rarely free once the hidden costs become visible."
    ],
    tags=["sax","notebook-persistence","hidden-costs","ai-substitutes-fail","analog-establishment"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="analog-premium",
    concept="The mechanism · why people pay premium for analog forms",
    summary="Sax distills the cross-category pattern into the mechanism: people pay premium for analog forms because analog delivers (1) sensory engagement digital cannot match, (2) ritual and ceremony that digital strips out, (3) constraint that focuses attention vs digital's infinite distraction, (4) durability and permanence vs digital's ephemerality, (5) social and tactile presence vs digital's invisibility, and (6) the deliberate-choice signal of having refused the default. Any one of these can justify analog premium; the combination of several makes the analog premium structurally durable.",
    usable_principle="The analog premium has six components: sensory engagement, ritual, constraint-focuses-attention, durability, social/tactile presence, and deliberate-choice signal. The more components an analog offering combines, the more durable the premium. Audit your offering against the six.",
    sniped_relevance="For SNIPED, audit the founder-portrait offering against the six: (1) Sensory — the shoot day as in-person experience (analog scores high). (2) Ritual — the Direction Stack consultation as preparation ceremony (high). (3) Constraint — the in-camera approach forces deliberate choices (high). (4) Durability — physical prints + long-tail brand value (high). (5) Social presence — the photographer-as-author named on the work (high). (6) Deliberate choice — the founder's anti-AI decision (high, especially with Cultural Doc context). SNIPED scores high on all six — that is the structural premium foundation.",
    direct_quotes=[
        "Six components: sensory, ritual, constraint, durability, presence, deliberate choice.",
        "The more components an analog offering combines, the more durable the premium."
    ],
    tags=["sax","six-components","analog-premium-mechanism","sniped-audit","structural-premium"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="analog-premium",
    concept="The hybrid future · analog and digital coexist, not replace",
    summary="Sax's nuanced closing: the analog revenge isn't a return to pre-digital purity — most analog buyers also use digital extensively. The hybrid pattern is the actual future: digital for the convenience use cases (background music, reference lookup, quick communication) and analog for the high-value use cases (focused listening, deep reading, important records). The premium analog forms succeed not by displacing digital but by occupying the high-value end of categories where digital occupies the convenience end. The hybrid coexistence is structurally stable; the 'either/or' framing of the digital triumphalists was always wrong.",
    usable_principle="Analog and digital coexist in hybrid form rather than one displacing the other. Analog occupies the high-value end of categories; digital occupies the convenience end. Position analog premium at the high-value end without trying to compete with digital on convenience.",
    sniped_relevance="For SNIPED, this validates the targeted positioning. Don't try to compete with AI on convenience (you'll lose) or on volume (you can't). Position at the high-value end of photography where founders make deliberate premium choices for high-stakes visual artifacts. AI tools occupy the convenience end (LinkedIn-headshot-replacement-on-demand, social-media-volume-graphics); SNIPED occupies the high-value end (premium founder portraits, Direction Stack book, named cultural authority). Both can exist; SNIPED's job is to dominate the high-value end deliberately.",
    direct_quotes=[
        "Analog and digital coexist. They do not replace.",
        "Position analog at the high-value end; let digital have the convenience end."
    ],
    tags=["sax","hybrid-future","high-value-positioning","sniped-targeting","ai-coexistence"]
)

print(f"After cluster 10 (Sax · 8 chunks): {len(CHUNKS)} chunks")

with OUT.open("w") as f:
    for c in CHUNKS:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")
print(f"Wrote {len(CHUNKS)} chunks to {OUT}")
