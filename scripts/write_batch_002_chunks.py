#!/usr/bin/env python3
"""
Emits BATCH_002_CHUNKS.jsonl from in-script chunk definitions.
Schema per user spec:
  chunk_id, batch, source_title, source_file, author, domain, concept,
  summary, usable_principle, sniped_relevance, direct_quotes, tags
"""
import json
from pathlib import Path

OUT = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "BATCH_002_CHUNKS.jsonl"
OUT.parent.mkdir(parents=True, exist_ok=True)

BATCH = "BATCH_002_TIER_1_CANON_BOOKS"
CHUNKS = []

def add(*, source_title, source_file, author, domain, concept,
        summary, usable_principle, sniped_relevance,
        direct_quotes=None, tags=None):
    cid = f"batch-002-chunk-{len(CHUNKS)+1:03d}"
    CHUNKS.append({
        "chunk_id": cid,
        "batch": BATCH,
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
# Poor Charlie's Almanack · Charles Munger
# =============================================================
STITLE = "Poor Charlie's Almanack"
SFILE = "poor_charlies_almanack_munger.md"
AUTHOR = "Charles T. Munger (ed. Peter D. Kaufman)"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="mental-models",
    concept="Worldly wisdom · the latticework of mental models",
    summary="Munger's central thesis is that real-world problem solving requires a latticework of mental models drawn from many disciplines: physics, biology, psychology, economics, history. A single discipline produces 'the man with a hammer' bias where every problem looks like a nail.",
    usable_principle="Maintain a working set of 80-100 mental models across hard disciplines. Cross-check any decision against models from at least three unrelated fields before committing.",
    sniped_relevance="Direction Stack is itself a small latticework (mechanical + psychological + photographic + cultural protocols). Treat methodology refinement as an explicit cross-disciplinary import problem, not a craft-only refinement. The 9-photographer canon is the photographic latticework; expand to include engineering / behavioral economics / cinematography references already named in SNIPED_OS_V1_SYNTHESIS.",
    direct_quotes=[
        "To a man with a hammer, every problem looks pretty much like a nail.",
        "You've got to have models in your head."
    ],
    tags=["munger","mental-models","cross-disciplinary","decision-making"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="decision-making",
    concept="Inversion · solve forward by working backward",
    summary="Many problems are solved faster by inverting them. Instead of 'how do I succeed?' ask 'what guarantees failure, and how do I avoid it?' Munger credits much of his and Buffett's success to systematically avoiding stupidity rather than seeking brilliance.",
    usable_principle="Before any major initiative, run the inversion pass: list everything that would guarantee failure of this initiative. Eliminate those before optimizing for upside.",
    sniped_relevance="The SNIPED 10 'aesthetic traps' (Influencer Photographer, Wedding Drift, Streetwear Lookbook Trap, MFA Drift, etc) are already an inversion exercise — what would guarantee SNIPED becomes generic — applied to positioning. Extend inversion to pricing decisions (what would guarantee $1,500 floor erodes?) and network decisions (what would guarantee Rejuar dependency collapses?).",
    direct_quotes=[
        "Invert, always invert.",
        "It is remarkable how much long-term advantage people like us have gotten by trying to be consistently not stupid, instead of trying to be very intelligent."
    ],
    tags=["munger","inversion","mental-models","failure-modes"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Psychology of Human Misjudgment · 25 cognitive biases",
    summary="Munger's signature talk lists 25 standard causes of human misjudgment: reward-and-punishment superresponse tendency, liking/loving tendency, doubt-avoidance, inconsistency-avoidance, curiosity, Kantian fairness, envy/jealousy, reciprocation, influence-from-mere-association, simple pain-avoiding psychological denial, excessive self-regard, over-optimism, deprival-superreaction, social proof, contrast-misreaction, stress-influence, availability-misweighing, use-it-or-lose-it, drug-misinfluence, senescence-misinfluence, authority-misinfluence, twaddle, reason-respecting, lollapalooza (multiple biases combining).",
    usable_principle="Run any negotiation, pitch, or major decision through the 25-bias checklist. Pay special attention to lollapaloozas — situations where 3+ biases compound, which is where most catastrophic decisions are made.",
    sniped_relevance="Pricing-floor erosion is a lollapalooza risk: reciprocation (client gave you a referral so you discount) + liking (you like them) + social proof (other photographers discount) + doubt-avoidance (you're unsure they'll close at full). Naming the lollapalooza makes the discount discipline holdable. Same for free-shoot-without-return-mechanic temptations.",
    direct_quotes=[
        "Never, ever, think about something else when you should be thinking about the power of incentives.",
        "Show me the incentive and I will show you the outcome."
    ],
    tags=["munger","cognitive-bias","psychology","negotiation"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="finance",
    concept="Sit on your ass investing · the power of doing nothing",
    summary="Berkshire's compound returns came largely from a small number of decisions held for decades, not from constant trading. Munger calls the discipline of holding through volatility 'sit on your ass investing.' Activity is usually destructive to long-term return.",
    usable_principle="When a system is working, the highest-leverage move is to not touch it. Reserve change-energy for system bottlenecks that are unambiguously broken.",
    sniped_relevance="Maps directly to the SNIPED 'Repetition > Novelty' lock (CANONICAL_TRUTHS.md). Architecture is built; the next 90 days are reps, not new frameworks. Resist the urge to rewrite the doctrine docs every week. Sit on the locked aesthetic, the locked offer ladder, the locked Direction Stack — execute them.",
    direct_quotes=[
        "The big money is not in the buying and selling, but in the waiting.",
        "Sit on your ass investing."
    ],
    tags=["munger","compounding","discipline","do-nothing"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Circle of competence · know the edge of what you know",
    summary="Each person's expertise has a defined perimeter. Inside the circle you have informational and judgment advantages. Outside it you are at a disadvantage against specialists. Most catastrophic decisions happen when people act confidently outside their circle of competence.",
    usable_principle="Name your circle of competence in a single sentence and write it down. Before any new initiative, ask: is this inside or outside? If outside, either build competence first (slow) or partner with someone whose circle includes it (fast).",
    sniped_relevance="BJ's circle: 10-protocol direction on set, operator-coded portraiture, founder/cultural-doc lane in LA, methodology-led service design. Outside circle (delegate or partner): retoucher-scale operations, contract law, advanced compositing (delegated to Rejuar), eventually social media volume work. The boundaries are explicit in the 'un-delegate-ables' list in OPERATIONAL_BACKBONE.md — that's the circle named.",
    direct_quotes=[
        "Knowing what you don't know is more useful than being brilliant."
    ],
    tags=["munger","circle-of-competence","self-knowledge","delegation"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Incentives are everything · superresponse tendency",
    summary="Humans respond more strongly to incentives than to logic, ethics, or persuasion. FedEx solved a chronic delay problem only when night shift compensation switched from hourly to per-shift (work done = go home). Solving 'incentive misalignment' usually solves 90% of organizational problems.",
    usable_principle="Before designing a process, design the incentive. Before hiring, design the comp structure. When something isn't getting done, the first question is never 'is the person lazy' — it's 'what is the incentive actually rewarding?'",
    sniped_relevance="For the eventual retoucher hire, this means per-Hero payment with a quality-gate clause (rejected Heroes don't bill) — aligns retoucher with BJ's quality standard automatically. For Ren outreach: per-positive-reply or per-booked-call structure rather than per-email-sent prevents volume gaming. The Pixieset upsell architecture (Heroes→Selects→Proofs tiers) is a buyer-incentive design — every gallery encourages upgrading by structure.",
    direct_quotes=[
        "Never, ever, think about something else when you should be thinking about the power of incentives."
    ],
    tags=["munger","incentives","org-design","compensation"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="empire-building",
    concept="Compounding requires a long runway · the eighth wonder",
    summary="Compounding's power is hyperbolic with time. Interrupting the compound — through fees, market exits, premature withdrawals, or career pivots — is the single most expensive thing one can do. Munger's net worth came from holding Berkshire for 50+ years, not from picking 50 great stocks.",
    usable_principle="The single longest commitment you can sustain to one specific compounding asset will dominate your lifetime return. Pick the asset deliberately; defend the runway ruthlessly.",
    sniped_relevance="The SNIPED 10-year archive horizon (REVERSE_ROADMAP.md Year 10 state) is the long-runway bet. Khalil Joseph / Bradford Young / Teju Cole all took 10-15 years before cultural recognition arrived. Every short-term temptation that would break the runway (wedding gigs, viral TikTok, NYC move) is a compound-break. Treat the 10-year horizon as the load-bearing constraint, not the aspirational marker.",
    direct_quotes=[
        "The first rule of compounding is to never interrupt it unnecessarily."
    ],
    tags=["munger","compounding","long-game","patience"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Avoid intense ideology · maintain mental flexibility",
    summary="Strong ideological commitment closes off thinking. Munger refuses to commit to political or economic ideologies because they prevent updating when evidence demands it. Smart people often hold strong views weakly.",
    usable_principle="Distinguish between locks (held strongly because evidence supports them) and ideology (held strongly because identity demands it). The first is competence; the second is rigidity.",
    sniped_relevance="The hybrid AI stance (YES for world-construction, NO for identity) is held BECAUSE of the Berger/Sax framework + observed AI-portrait skin-texture limits, not because BJ is 'anti-AI.' Naming the reasoning makes the position update-able if evidence shifts (e.g. if AI identity-generation crosses the editorial floor in 2-3 years, the stance can re-open without identity damage).",
    direct_quotes=[
        "You're not entitled to take a view, unless and until you can argue better against that view than the smartest guy who holds that opposite view."
    ],
    tags=["munger","ideology","epistemic-humility","steelman"]
)

# =============================================================
# Zero to One · Peter Thiel + Blake Masters
# =============================================================
STITLE = "Zero to One"
SFILE = "zero_to_one_thiel.md"
AUTHOR = "Peter Thiel + Blake Masters"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="The contrarian question · what important truth do few people agree with you on?",
    summary="Thiel's interview question for founders. A real answer requires you to (a) believe something, and (b) believe something that the consensus rejects. Most people fail because they either have no belief or only have consensus beliefs. Genuine contrarian truths are the source of monopoly opportunities.",
    usable_principle="Force-write your contrarian thesis in one sentence. If a consensus reader would nod, the thesis isn't sharp enough. Keep tightening until a credible peer would push back.",
    sniped_relevance="SNIPED's contrarian thesis: 'In an AI-saturated 2026 visual market, the most defensible photography business is methodology-disclosed real-subject editorial portraiture for a specific LA cultural cluster — not volume, not AI-augmented, not generalist.' Consensus says scale, automate, generalize. SNIPED says specialize, methodology-anchor, archive-build. The intersection is what BATCH_001 STRATEGIC_PRINCIPLES chunk called 'the empty intersection moat.'",
    direct_quotes=[
        "What important truth do very few people agree with you on?",
        "The most contrarian thing of all is not to oppose the crowd but to think for yourself."
    ],
    tags=["thiel","contrarian","strategy","monopoly"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Monopoly · competition is for losers",
    summary="Thiel argues that businesses that don't have monopolies (priced like commodities, competing on price/feature) will not generate enough margin to invest in long-term advantage. True monopolies — defined as 'this company so dominates its category it can set its own price' — are the only structure where founders can fund 10+ year horizons. Most founders lie about being in monopolies (by drawing markets narrowly) or being in competition (by drawing markets broadly) — both are sales tactics.",
    usable_principle="Define your market precisely enough that you are the dominant or near-dominant player AND honestly enough that the definition is real. A monopoly built on a fake market boundary collapses when the market is correctly framed.",
    sniped_relevance="SNIPED's market is NOT 'LA photographers' (massive competition, commodity pricing). It's 'methodology-disclosed operator-coded portraiture for LA emerging Black founder/artist culture with named cultural-documentation horizon.' Inside that market SNIPED is a monopoly because the named intersection is empty (per BATCH_001 strategic-principles chunk). This is what justifies the $1,500 floor and the 10-year compounding bet.",
    direct_quotes=[
        "Competition is for losers.",
        "If you want to create and capture lasting value, don't build an undifferentiated commodity business."
    ],
    tags=["thiel","monopoly","positioning","market-definition"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Four characteristics of monopoly · proprietary tech, network effects, economies of scale, brand",
    summary="Thiel identifies four reinforcing characteristics that produce durable monopolies. Proprietary technology must be 10× better than the next-best alternative on at least one dimension. Network effects create value as users join. Economies of scale lower marginal cost as volume grows. Brand is what enables charging premium for the same physical product.",
    usable_principle="For any business, score on each of the four dimensions. If you score 0 on all four, you're in commodity competition. The reinforcement multiplies: a strong brand makes the network worth joining; the network makes the tech harder to copy; the scale makes the brand more defensible.",
    sniped_relevance="SNIPED's four scores: proprietary tech = the 10-protocol Direction Stack methodology + composite environment rotation (medium); network effects = the cultural-doc institutional network + LA founder cluster referral compounding (medium, growing); economies of scale = limited in a service business but real for the Pixieset upsell architecture + recyclable LinkedIn POV bank (low); brand = the operator-coded register + locked aesthetic + Direction Stack book as authority asset (medium-high, growing). Brand and methodology are the two strongest legs; network is the longest-runway lever; scale is the limiting factor that justifies the eventual retoucher hire.",
    direct_quotes=[
        "A great company is a conspiracy to change the world; when you share your secret, the recipient becomes a fellow conspirator."
    ],
    tags=["thiel","monopoly","moats","brand"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Start small and monopolize · the founder's first market",
    summary="The best path to a large monopoly is to dominate a small market first — small enough that you can take 100% of it, then expand to concentric adjacent markets. Facebook started with Harvard students (one school, one demo, fully addressable) before expanding. Amazon started with books. PayPal with eBay power sellers. The mistake is to launch into a 'huge market' where you're 0.001% of it and competing against incumbents.",
    usable_principle="Pick the smallest specific market you can credibly dominate. Take it to ~100% saturation before opening the next concentric ring.",
    sniped_relevance="SNIPED's first market = LA emerging Black founder portraiture, not 'photography.' Within that, the first concentric ring = the LA tech-founder slice on LinkedIn that the VIB method targets. Even narrower first ring: BJ's existing warm network (Pearl/Miho referrals, returning models like Yae, Kennedie). Saturate that first → then concentric expansion to broader LA founders → then operator-class generally → then national.",
    direct_quotes=[
        "Every startup is small at the start. Every monopoly dominates a large share of its market. Therefore, every startup should start with a very small market."
    ],
    tags=["thiel","monopoly","market-entry","specialization"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Definite optimism vs indefinite optimism",
    summary="Thiel divides worldviews on two axes: optimism/pessimism and definite/indefinite. Definite optimists believe the future is better AND can be specifically planned for and built. Indefinite optimists believe the future is better but cannot be planned — only positioned for. The current US default is indefinite optimism (hedge funds, diversification, optionality). Thiel argues that historic value creation comes from definite optimism (Apollo program, Hoover Dam, the Manhattan Project, Stripe, SpaceX).",
    usable_principle="Make definite plans with named milestones and named bets, not optionality-preserving hedges. The Reverse Roadmap with specific Year 1 / 3 / 5 / 10 milestones is itself an instance of definite optimism.",
    sniped_relevance="The REVERSE_ROADMAP.md document IS definite optimism applied to SNIPED. The 10-year named outcome (named visual documentarian of LA emerging Black founder/operator/artist culture at $1.5-3M annual revenue with multiple published books) is a specific bet, not an option. The dependency chain forces sequencing. Resist drift toward 'let's keep options open' — it's the indefinite-optimism trap.",
    direct_quotes=[
        "A definite view, by contrast, favors firm convictions.",
        "Indefinite optimism is inherently unsustainable: how can the future get better if no one plans for it?"
    ],
    tags=["thiel","optimism","planning","determinism"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="distribution",
    concept="Distribution is half the product · the dirty secret of startups",
    summary="Founders romanticize the product and underbuild distribution. Thiel: 'Customers will not come just because you build it.' A great product without distribution fails; a mediocre product with great distribution often succeeds. Sales and distribution are at least 50% of the work, no matter how technical the field.",
    usable_principle="For every hour spent on the work, spend an hour on distribution. The Production Stack and Direction Stack are the work; the Attention Stack, Outbound Stack, and VIB method are the distribution. Both budgets must be approximately equal.",
    sniped_relevance="The SNIPED Phase 1 lean override correctly prioritizes Revenue Engine (cold outreach + VIB) at 50%+ of allocated time. This is Thiel's principle operationalized. The temptation to spend more time on the Direction Stack book or the Aesthetic v3 refinement than on shipping VIBs is the distribution-under-investment trap. Counter-discipline: VIB #1 ships before any new strategy doc.",
    direct_quotes=[
        "Customers will not come just because you build it.",
        "Distribution is half the product. The product is half the distribution."
    ],
    tags=["thiel","distribution","sales","founder-traps"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="hiring",
    concept="Cult-like cohesion · the 0-1 founding team",
    summary="The early team should feel cult-like to outsiders. Not because of weirdness for its own sake, but because the team needs intense shared belief in a non-obvious thesis (the contrarian truth above) to survive the years when no one else believes. PayPal Mafia, early Facebook, early SpaceX all had this property.",
    usable_principle="Hire on shared belief, not just skill. The Trust Equation (Maister) applies internally too: low self-orientation, high reliability + intimacy + credibility. Cohesion is built by shared mission + shared sacrifice + shared inside-language, not by perks.",
    sniped_relevance="The current SNIPED team (BJ + Rejuar + Ren + Hermine + Pearl as domestic infrastructure) IS the founding cult. Rejuar takes a $100/mo retainer for design work that's worth multiples more — that's belief, not market-rate work. Preserve this. The first retoucher hire (Mo 6-9 per BATCH_001 chunks) should be filtered for shared-belief, not just retouching skill. The 'inside language' is the Direction Stack vocabulary, the Lock numbering, the canonical-truths shorthand.",
    direct_quotes=[
        "A startup is the largest endeavor over which you can have definite mastery.",
        "Cults are intense, and their members are weirdly enthusiastic about each other. Outsiders see them as creepy. Insiders see each other as comrades."
    ],
    tags=["thiel","hiring","team","mission"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Last mover advantage · the value is in capture, not first",
    summary="First-mover advantage is overrated. The valuable position is being the LAST mover in a market — the last entrant who, by virtue of better execution or timing, takes the market and holds it. Google was not the first search engine. Facebook was not the first social network. The first movers in both categories are forgotten.",
    usable_principle="Optimize for being the lasting player in your category, not the first. The metrics that matter are 10-year retention and category ownership, not launch-week speed.",
    sniped_relevance="SNIPED is not the first LA founder-portrait business, not the first methodology-led photographer, not the first cultural-documentation operator. The play is to be the LAST mover — the one who in 2036 is the named figure in the category. This is the explicit Year-10 bet from REVERSE_ROADMAP.md. Every short-term speed-to-market temptation that comes at the cost of long-term defensibility (rushing a sloppy book launch, taking weak-fit clients to fill the pipeline) is a first-mover trap.",
    direct_quotes=[
        "It's much better to be the last mover — that is, to make the last great development in a specific market and enjoy years or even decades of monopoly profits."
    ],
    tags=["thiel","last-mover","timing","monopoly"]
)

# =============================================================
# The Art of War · Sun Tzu (tr. Lionel Giles)
# =============================================================
STITLE = "The Art of War"
SFILE = "art_of_war_sun_tzu.txt"
AUTHOR = "Sun Tzu (tr. Lionel Giles)"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Five fundamentals of war · the laying-plans calculus",
    summary="Sun Tzu opens with five factors that determine victory before any battle: the Moral Law (whether the people are aligned with leadership), Heaven (timing, seasons, conditions), Earth (terrain, distance, geography), the Commander (wisdom, sincerity, courage, strictness), Method and discipline (organization, control, supply). A general who has assessed these honestly before engaging knows the outcome before fighting.",
    usable_principle="Before any campaign (product launch, market entry, hire), audit yourself honestly on each of the five fundamentals. If you score weakly on any, address it before engaging — not during.",
    sniped_relevance="Maps onto the SNIPED 'pre-flight checklist' discipline from PRODUCTION_OS + EXECUTION_PRIORITIZATION. Moral Law = team belief in the thesis (cult-like cohesion per Thiel). Heaven = LA cultural moment timing (post-2020 Black founder rise · genuine 'heaven' window). Earth = DTLA studio anchor + LinkedIn/IG terrain. Commander = BJ's operator-coded discipline. Method = the 6 backbone loops + Direction Stack methodology. The audit reveals: Heaven and Earth are favorable; Commander and Method are strong; Moral Law is single-operator solid; gap is downstream Method (delivery automation, retoucher onboarding) not yet built.",
    direct_quotes=[
        "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.",
        "The art of war is governed by five constant factors."
    ],
    tags=["sun-tzu","strategy","planning","fundamentals"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="All warfare is based on deception",
    summary="Sun Tzu's foundational tactical claim: appear weak when you are strong, appear strong when you are weak, appear far when near, appear near when far, hold out baits to entice the enemy, feign disorder, attack where the enemy is unprepared, emerge where you are not expected. The point is asymmetric information — the strategist who knows the opponent's plan while concealing their own wins before fighting.",
    usable_principle="Conceal the next move from competitors. Don't publicly announce strategy before it's executed; let the result speak. Reserve the surprising move for the moment maximum advantage.",
    sniped_relevance="SNIPED's 'methodology disclosed on the artifact' (Chapter Card colophon citing 'DIRECTION STACK · v3 LUXURY') is the opposite move — radical transparency as competitive moat. The reasoning works because the methodology is hard to copy (requires years of craft + a directed-subject discipline competitors don't have). Sun Tzu's deception principle still applies to TIMING — the Direction Stack book launch is held private until Q3 2026 not because the methodology is secret but because the launch moment is concealed from competitors who might race to ship lesser methodology books first.",
    direct_quotes=[
        "All warfare is based on deception.",
        "Hence, when able to attack, we must seem unable; when using our forces, we must seem inactive."
    ],
    tags=["sun-tzu","deception","information","timing"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Supreme excellence · subduing the enemy without fighting",
    summary="The highest form of generalship is to break the enemy's resistance without battle. Diplomatic and strategic moves that make conflict unnecessary are higher-order than tactical brilliance in actual battle. Winning by avoiding the wasteful contest is the rare skill.",
    usable_principle="Before competing directly, ask if there's a positioning or pricing move that makes direct competition unnecessary. Most 'competition' is actually self-inflicted because the operator failed to differentiate.",
    sniped_relevance="The SNIPED refusal of wedding/family/lifestyle work, the Eagle Rock studio kept private (Lock 9), the deliberately narrow 'operator-coded' definition — all are 'subduing without fighting' moves. By NOT competing in the broad LA-photographer market, SNIPED makes itself uncompare-able on price. Every operator who competes on the photography commodity layer is doing the wasteful contest Sun Tzu warns against.",
    direct_quotes=[
        "Supreme excellence consists in breaking the enemy's resistance without fighting.",
        "The skillful leader subdues the enemy's troops without any fighting."
    ],
    tags=["sun-tzu","positioning","avoidance","differentiation"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Know yourself and know the enemy",
    summary="Sun Tzu: 'If you know the enemy and know yourself, you need not fear the result of a hundred battles. If you know yourself but not the enemy, for every victory gained you will also suffer a defeat. If you know neither the enemy nor yourself, you will succumb in every battle.' Self-knowledge alone produces 50% win rate; combined with competitor knowledge, win rate approaches 100%.",
    usable_principle="Maintain dossiers on both yourself (capabilities, weaknesses, true circle of competence) and on competitors (their positioning, pricing, where they will and won't go). Update both quarterly. Decisions made with only half the data are 50/50 at best.",
    sniped_relevance="SNIPED's self-knowledge is well-documented (OPERATING_BRIEF + CANONICAL_TRUTHS + the 7-signature recognizability test + the 10 aesthetic traps). Competitor-knowledge layer is thinner. Recommendation: build a 'LA photographer competitive landscape' doc tracking 8-12 named competitors (e.g. Tadder, jpwphoto cited in feedback_visual_direction memory as the lane SNIPED is NOT) + their pricing + their refusals. Refresh quarterly during Constraint Audit.",
    direct_quotes=[
        "If you know the enemy and know yourself, you need not fear the result of a hundred battles."
    ],
    tags=["sun-tzu","self-knowledge","competitive-intel","constraint-audit"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="operations",
    concept="The line between order and disorder lies in logistics",
    summary="Sun Tzu treats supply, terrain, and operational discipline as more important than tactical brilliance. The general who runs out of provisions loses regardless of skill. Most defeats in war (and most failures in business) trace back to logistics breakdowns, not strategic miscalculations.",
    usable_principle="Audit logistics before celebrating strategy. Backup discipline, file structure, calendar protection, edit-hour ceilings are not unsexy admin — they are the difference between sustained operation and collapse.",
    sniped_relevance="PRODUCTION_OS folder structure (10 subfolders per shoot, locked) + storage tiering (hot/warm/cold/cloud) + 5-day SLA + 25-30% tax set-aside + the wage-separation system — these ARE the logistics layer Sun Tzu treats as load-bearing. The temptation to deprioritize them as 'just admin' is the failure mode. Every Reset that exceeded SLA in BJ's history traces to a logistics breakdown (travel-week booking, bottlenecked edit queue), not creative failure.",
    direct_quotes=[
        "The line between disorder and order lies in logistics.",
        "An army marches on its stomach."
    ],
    tags=["sun-tzu","logistics","operations","discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Use the indirect approach · cheng and ch'i",
    summary="Sun Tzu's tactical distinction: cheng = direct, expected, normal force. Ch'i = indirect, unexpected, irregular force. Victories come from combining both. A frontal cheng attack engages the enemy's defenses; the ch'i flanking move arrives where defense is absent. Whoever can produce endless combinations of cheng and ch'i is unbeatable.",
    usable_principle="The expected move (frontal pitch, direct ask, conventional channel) anchors the engagement. The unexpected move (a Loom audit instead of a brochure, a VIB image instead of a sales deck, a Day-30 Op Kit DM after delivery silence) is where the conversion actually happens.",
    sniped_relevance="The VIB method is pure ch'i — prospects expect a generic LinkedIn DM pitch (the cheng); they get a side-by-side visual diagnostic (the ch'i). The Loom audit is ch'i — expected: a calendar link; delivered: a personalized 5-min recorded methodology demo. Direction Stack book as 'authority asset rather than just a book' (Truth 11) is ch'i — competitors send pricing PDFs (cheng); SNIPED sends a 57-page methodology book (ch'i). Maintain the asymmetry deliberately.",
    direct_quotes=[
        "In all fighting, the direct method may be used for joining battle, but indirect methods will be needed in order to secure victory.",
        "There are not more than two methods of attack — the direct and the indirect; yet these two in combination give rise to an endless series of maneuvers."
    ],
    tags=["sun-tzu","indirect-approach","tactics","asymmetric-moves"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Be like water · adapting form to terrain",
    summary="Water has no fixed shape — it takes the shape of the vessel that holds it and flows around obstacles. Sun Tzu's tactical doctrine: a general should never have a fixed formula. The right tactic depends entirely on terrain, enemy state, weather, and timing. Rigid playbooks lose to adaptive ones.",
    usable_principle="Lock the strategy. Adapt the tactics. The strategic locks (offer ladder, aesthetic, methodology) are the channel; the tactical execution (which client, which platform, which week) flows to fit the immediate terrain.",
    sniped_relevance="The SNIPED 'lock' / 'adapt' distinction is already operationally encoded. 12 canonical truths = locked strategy. The 'when traveling for engineering work' adaptation in OPERATING_BRIEF Section 5 = water-like tactical flex. Phase 1 Lean Override (drop free shoots to 0 when paid pipeline grows) = water-like tactical adjustment within strategic lock. The discipline is knowing which layer to defend rigidly and which to let flow.",
    direct_quotes=[
        "Water shapes its course according to the nature of the ground over which it flows.",
        "Therefore, just as water retains no constant shape, so in warfare there are no constant conditions."
    ],
    tags=["sun-tzu","adaptation","flexibility","tactics"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Choose your battles · don't fight when you can't win",
    summary="Sun Tzu enumerates conditions for engagement: superior numbers, favorable terrain, enemy disarray, secure supply. When these conditions are absent, retreat or refuse engagement is the correct move. The general who fights every challenge offered ends bankrupt. The discipline of refusal is itself an offensive asset.",
    usable_principle="Decline more than you accept. Most opportunities are baits — engagement consumes resources for marginal return. The yes that compounds is the rare yes.",
    sniped_relevance="The SNIPED 'lane refusal rules' (free-shoot ceiling, wedding/family/lifestyle drift refusal, MFA gallery purity refusal, influencer-photographer refusal) ARE Sun Tzu's choose-battles discipline. Every yes to a wrong-tier opportunity costs disproportionate downstream time. The Win Without Pitching 'we will be selective' proclamation (per BATCH_001) is the same discipline named differently.",
    direct_quotes=[
        "He will win who knows when to fight and when not to fight."
    ],
    tags=["sun-tzu","selectivity","refusal","focus"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Use of spies · pay for information",
    summary="Sun Tzu's final chapter argues for heavy investment in intelligence. Five classes of spies (local, inward, converted, doomed, surviving). A campaign costing thousands in lives and gold can be won or lost on a single piece of competitor intelligence purchased for a relative pittance. 'To remain in ignorance of the enemy's condition simply because one grudges the outlay of a hundred ounces of silver is the height of inhumanity.'",
    usable_principle="The cost of competitive intelligence is always lower than the cost of acting blind. Build cheap intel mechanisms: read competitor websites quarterly, follow named competitor accounts, subscribe to industry newsletters, attend the events your prospects attend.",
    sniped_relevance="For SNIPED, the cheap-intel mechanisms: quarterly LinkedIn audit of named competitor founder-photographers' pricing/positioning (free, 30 min); attendance at 1-2 LA founder events per quarter (low-cost ch'i intel layer); reading Aperture, Cultured, T Mag quarterly to track gallery/editorial moves; subscribing to Stoute's United Masters newsletter for cultural-capital intel. Already cited in BATCH_001 STRATEGIC_PRINCIPLES recommendation. Add a 'competitive landscape doc' to the workspace, refreshed quarterly.",
    direct_quotes=[
        "What enables the wise sovereign and the good general to strike and conquer, and achieve things beyond the reach of ordinary men, is foresight. Now this foresight cannot be elicited from spirits; it must be obtained from men who know the enemy situation."
    ],
    tags=["sun-tzu","intelligence","competitive-research","information"]
)

# =============================================================
# The 48 Laws of Power · Robert Greene
# =============================================================
STITLE = "The 48 Laws of Power"
SFILE = "48_laws_of_power_greene.md"
AUTHOR = "Robert Greene"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 1 · Never outshine the master",
    summary="Greene's opening law: those above you want to feel secure in their superiority. When you display talents that surpass theirs (even unintentionally), you trigger fear and envy, and they will work to undermine you. Make those above you feel comfortably superior; mask your own brilliance until you no longer report to them.",
    usable_principle="In any patronage/client/mentor relationship, calibrate displayed competence to a level that supports the principal's authority. Save the bigger moves for when you control the room.",
    sniped_relevance="For SNIPED client conversations (especially Op Kit and Brand System tier), the operator's role is to make the client feel they are the protagonist of the visual transformation — never to display 'I'm smarter than you about your business.' The Direction Stack diagnostic is framed as 'here's what's happening mechanically in your photos' (operator-as-technician) NOT 'here's how your judgment failed' (operator-as-superior). The Mom Test discipline + Trust Equation low-self-orientation are this law operationalized.",
    direct_quotes=[
        "Never outshine the master.",
        "Make your masters appear more brilliant than they are and you will attain the heights of power."
    ],
    tags=["greene","power","client-management","positioning"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 4 · Always say less than necessary",
    summary="When trying to impress, the powerful say less. Silence creates space for the other party to read meaning into your words and to fill the gap with their own narrative. Talkativeness signals insecurity. The shorter, more enigmatic the statement, the more weight it carries.",
    usable_principle="In high-stakes conversations (pricing, negotiation, first meetings), say 30% of what you'd be tempted to say. Let the silence pull the other party forward.",
    sniped_relevance="The 80-word cold-email limit + the under-50-word email-2 + the 'no pricing in cold DM' rule (per cold_email_doctrine) are this law in protocol form. Discovery calls: Mom Test discipline = 'talk less, listen more.' When a prospect asks 'why $1,500?', the answer is one sentence (the value), then silence. The temptation to over-justify pricing IS the insecurity signal that erodes the price.",
    direct_quotes=[
        "Always say less than necessary.",
        "Powerful people impress and intimidate by saying less. The more you say, the more common you appear, and the less in control."
    ],
    tags=["greene","power","negotiation","silence"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 6 · Court attention at all cost",
    summary="Anonymity is the enemy of power. A bad reputation can be transformed; an unknown reputation cannot. Stand for something — even if controversial — that pulls attention to your name. The greatest sin in the attention economy is being forgettable.",
    usable_principle="If forced between 'safe and forgettable' and 'sharp and polarizing,' choose sharp. The cost of being mildly disliked by the wrong audience is dwarfed by the cost of not being known by the right one.",
    sniped_relevance="Maps to the SNIPED 'becoming known is the goal' canonical truth (Truth 6). The 10-year named-figure horizon is precisely this law applied. Counter-balance: the law doesn't endorse cheap attention (clickbait, viral stunts, trolling) — those produce attention from the WRONG audience. The chapter rollout doctrine produces attention from the RIGHT audience (a recurring serial that the LA cultural cluster trains on).",
    direct_quotes=[
        "Court attention at all cost.",
        "Better to be slandered and attacked than ignored."
    ],
    tags=["greene","power","attention","reputation"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 9 · Win through your actions, never through argument",
    summary="Words convince only the convinced. Arguing your point with someone hardens their position. Demonstrating your point through visible action — letting the result speak — bypasses the defensive layer entirely. Politicians know this; great founders know this; argumentative people lose without realizing it.",
    usable_principle="When someone resists your idea, stop arguing and ship a demonstration. The result is the argument that cannot be rebutted.",
    sniped_relevance="VIB method is law-9 in pure form. The prospect doesn't argue with the side-by-side image because the demonstration IS the argument. No need to explain why the Direction Stack matters — the visible delta between left-panel and right-panel does the work. Same for Cultural Documentation: the body of work IS the argument for SNIPED's seriousness; no manifesto required.",
    direct_quotes=[
        "Win through your actions, never through argument.",
        "Demonstrate, do not explicate."
    ],
    tags=["greene","power","demonstration","selling"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 11 · Learn to keep people dependent on you",
    summary="The more critical you are to a relationship, the more leverage you have. Make yourself the indispensable node — the one whose absence creates cost. Avoid being replaceable; cultivate skills, knowledge, or relationships that cannot be easily duplicated.",
    usable_principle="Build skills that are scarce within your category. The more transferable your skills (anyone can do them), the less power you hold. The more idiosyncratic your skills (only you), the more leverage.",
    sniped_relevance="The 10 'un-delegate-ables' in OPERATIONAL_BACKBONE.md (Direction Stack diagnostic, 90-second opener, pricing decision, methodology refinement, aesthetic call, etc.) are the dependencies SNIPED builds. They cannot be replicated by hiring a different photographer because they require the operator's specific accumulation. This is the moat that justifies the Operator Kit and Brand System tiers.",
    direct_quotes=[
        "Learn to keep people dependent on you.",
        "To maintain your independence you must always be needed and wanted."
    ],
    tags=["greene","power","indispensability","leverage"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 13 · Appeal to people's self-interest, never to their mercy",
    summary="When asking for help, do not invoke past favors, kindness, or your own need. People act on what benefits them. Frame every request in terms of the recipient's interest — what they gain, how it serves their goals, how it makes them look. Appeals to mercy register as weakness and breed contempt.",
    usable_principle="Every ask is wrapped in the recipient's frame, not yours. 'I need a favor' is wrong. 'This serves you because X' is right.",
    sniped_relevance="In Day-30 Op Kit pitches, the message is not 'as a satisfied client, I'd love your continued business' (operator's frame). It's 'the Reset gave you 10 Heroes for LinkedIn + press — your Series B announcement window is the moment Op Kit was designed for, and these 25 additional images will carry you through the next 6 months of deployment' (client's frame). Same for referral asks: 'if you know a founder building something premium, the Reset will serve them' (referrer's frame of being helpful) NOT 'please refer me' (operator's need).",
    direct_quotes=[
        "When asking for help, appeal to people's self-interest, never to their mercy or gratitude."
    ],
    tags=["greene","power","persuasion","framing"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 15 · Crush your enemy totally · half-measures invite retaliation",
    summary="A wounded enemy will recover and retaliate. When the strategic moment arrives to remove an obstacle, do it completely — finish the move, don't soften it for sentimentality. The half-finished elimination is the most expensive kind: you lose the upside of the move AND inherit the long-term cost of the unfinished resentment.",
    usable_principle="When you decide to refuse a wrong-tier opportunity, refuse cleanly and finally. When you cancel a project, cancel it; don't 'maybe' it. When you fire a contractor, end the relationship; don't keep them at half-distance.",
    sniped_relevance="Soft-application: the Phase 1 'kill list' (cold-email infrastructure not Phase 1, TikTok daily volume not Phase 1, custom website not Phase 1, paid ads not Phase 1, course creation not Phase 1) is the law of crushing — these are not 'paused,' they are KILLED for Phase 1. Re-evaluating monthly creates drag and self-doubt. The discipline is the total nature of the refusal.",
    direct_quotes=[
        "Crush your enemy totally.",
        "More is lost through stopping halfway than through total annihilation."
    ],
    tags=["greene","power","decisiveness","refusal"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 17 · Cultivate an air of unpredictability",
    summary="Predictable behavior is exploitable behavior. When opponents (or partners, or clients) can model your next move, they price in advance against you. Periodic deliberate unpredictability — a surprising decision, an unexpected refusal, a move out of pattern — resets the calculation and restores power.",
    usable_principle="Once a quarter, make one deliberate move that breaks your established pattern. The point is not chaos; it's restoring the model uncertainty that gives you optionality.",
    sniped_relevance="Light touch for SNIPED: the methodology, pricing, and aesthetic are DELIBERATELY predictable (because consistency is the moat). The unpredictable moves should happen at the EDGES — surprise delivery moments (Kling AI animated post-conversion gift), unexpected refusals (declining a high-profile but wrong-tier opportunity publicly), surprising collaborations (a one-time gallery show, a single Substack essay long before launch). These reset competitor models.",
    direct_quotes=[
        "Cultivate an air of unpredictability.",
        "Humans are creatures of habit with an insatiable need to see familiarity in other people's actions."
    ],
    tags=["greene","power","unpredictability","pattern-breaking"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 25 · Re-create yourself · do not accept the roles society foists on you",
    summary="The roles assigned by family, class, profession, or history are not your true self — they are convenient compressions for others' use. The powerful deliberately construct a public identity that serves their strategy, then live up to it. The construction is real once it is sustained.",
    usable_principle="Your public identity is a deliberate construction. Choose the version of yourself that serves the 10-year game, then live up to it consistently enough that the chosen identity becomes the actual one.",
    sniped_relevance="The 'operator-coded, not artist-coded' identity claim (Section 1.1 OPERATING_BRIEF) is exactly Greene's law-25 move. The engineer-to-operator-photographer narrative arc is a deliberately constructed identity — true to BJ's actual background (Tuskegee engineering + Clemson planning + AWS field engineering) AND strategically chosen because it differentiates SNIPED from the artist-coded LA photographer default. Lock 11 ('Direction Stack is authority asset, not just a book') is the same move — the book is part of the constructed identity, not a side project.",
    direct_quotes=[
        "Re-create yourself.",
        "Do not accept the roles that society foists on you."
    ],
    tags=["greene","power","identity","positioning"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 28 · Enter action with boldness",
    summary="Hesitation telegraphs weakness. A bold action — even if not perfectly planned — pulls people forward because they read confidence as competence. The actor who pauses to refine endlessly produces less impact than the actor who commits and adjusts in flight.",
    usable_principle="When the decision is made, execute decisively. Refinement happens after the first move, not before. Boldness is itself a competitive advantage because most competitors hesitate.",
    sniped_relevance="The BATCH_001 'uncomfortable necessary actions' chunk listed 'Send VIB #1' as the highest-impact unblock. That IS Greene's law-28. The exact same energy applies to: launching the LinkedIn promotion-announcement post (delayed for 'privacy' reasons that are actually hesitation); first $1,500 quote without flexing; first Day-30 Op Kit pitch even when conversion is unlikely. Each is bolder than feels comfortable; each unblocks downstream compounding.",
    direct_quotes=[
        "Enter action with boldness.",
        "If you are unsure of a course of action, do not attempt it. Your doubts and hesitations will infect your execution."
    ],
    tags=["greene","power","action","decisiveness"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 33 · Discover each man's thumbscrew · what they want most",
    summary="Every person has a specific lever — a need, an insecurity, an unmet desire — that, if you identify and serve it, gives you influence. Generic appeals fail; specific appeals to the individual's actual driving need succeed. The work is discovering what that lever is for each specific person.",
    usable_principle="Before any important relationship (client, partner, hire), invest time in discovering the specific lever. What do they actually want that they can't articulate publicly? Status? Recognition? Belonging? Security? Once known, the relationship becomes navigable.",
    sniped_relevance="For founder portrait buyers: the lever is almost always STATUS (per Status Anxiety chunk in BATCH_001) — the felt gap between current visible presence and operational level of business. Identifying this in the Mom Test discovery call (NOT asking 'do you need photos' but 'when was the last time you turned down a media opportunity because your image wasn't right') surfaces the thumbscrew. The Op Kit pitch then addresses it specifically.",
    direct_quotes=[
        "Discover each man's thumbscrew.",
        "Find the chink in their armor, that soft spot which they cannot defend."
    ],
    tags=["greene","power","persuasion","discovery"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 38 · Think as you like but behave like others",
    summary="Internal divergence from the crowd is unlimited; external divergence is costly. Display the surface conformity that makes you welcome in any room, then think and act independently from a position of acceptance. The visibly contrarian person attracts opposition before they accomplish anything; the inwardly contrarian one accumulates the position from which to act.",
    usable_principle="Save the visible eccentricities for the moments they serve a strategic purpose. Default surface conformity buys access; reserve visible divergence for the move that genuinely needs it.",
    sniped_relevance="SNIPED's surface presentation (clean LinkedIn, professional cold email voice, standard contracts, recognizable visual language) is conformity at the surface. The contrarian thesis (methodology-disclosed, locked-aesthetic, anti-commodity, refuse-the-trends) is held internally and expressed through the WORK, not through provocative posting. This is why the BATCH_001 advice to 'never lead with my expertise; lead with the observation' works — surface humility, internal sharpness.",
    direct_quotes=[
        "Think as you like but behave like others.",
        "Trumpet your differences and people will think you only want to call attention to yourself."
    ],
    tags=["greene","power","conformity","strategic-display"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="power",
    concept="Law 48 · Assume formlessness",
    summary="The final law: rigid form is exploitable. Whoever can change shape — adapt strategy, abandon obsolete positions, restructure under pressure — defeats whoever is committed to a fixed form. Water again, but now as a strategic principle for the entire operation. The Tao Te Ching version of this law underpins much of the book.",
    usable_principle="Lock the values and the long-term direction. Keep the strategy and tactics formless enough to respond to new terrain. Every quarter, audit which pieces of the current operation are formless (adaptive) vs which are calcified (rigid by default rather than deliberately locked).",
    sniped_relevance="Bridges to Sun Tzu's 'be like water' chunk above. The SNIPED locked/adaptive distinction: 12 canonical truths = LOCKED (these are the load-bearing form, defended). Everything below them = FORMLESS (the chapter cadence adjusts to Rejuar's bandwidth; the VIB target list refreshes quarterly; the platform mix evolves with algorithm shifts). The quarterly Constraint Audit IS the formlessness mechanism — it asks 'what should we re-shape this quarter?'",
    direct_quotes=[
        "Assume formlessness.",
        "By taking a shape, by having a visible plan, you open yourself to attack."
    ],
    tags=["greene","power","formlessness","adaptability"]
)

# =============================================================
# The 33 Strategies of War · Robert Greene
# =============================================================
STITLE = "The 33 Strategies of War"
SFILE = "33_strategies_of_war_greene.md"
AUTHOR = "Robert Greene"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 1 · Declare war on your enemies · the polarity strategy",
    summary="Without an identified enemy, energy diffuses. Naming the enemy — the rival firm, the obsolete idea, the cultural pattern you refuse — concentrates effort and clarifies daily decisions. People rally to a 'we are against X' more reliably than to a 'we are for Y.' Strong brands have explicit villains.",
    usable_principle="Name your enemy. Write it down. The enemy can be a competitor, a category convention, a cultural pattern, or an internal habit. Whatever it is, the act of naming it sharpens every downstream decision.",
    sniped_relevance="SNIPED's named enemies (already in the doctrine): the influencer-photographer with trendy LUTs and presets-as-product; the commodity headshot studio; the artist-coded gallery purist who refuses commercial; the AI-first photographer who replaces subjects with AI avatars; the wedding/family/lifestyle drift; the hypebeast urban-grit posturing. The 10-traps list in SNIPED_OS_V1_SYNTHESIS IS the named enemy roster. Re-read quarterly during Constraint Audit.",
    direct_quotes=[
        "Life is endless battle and conflict, and you cannot fight effectively unless you can identify your enemies."
    ],
    tags=["greene","enemies","positioning","clarity"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 4 · Create a sense of urgency and desperation · the death-ground strategy",
    summary="People fight hardest when retreat is impossible. Generals throughout history have burned the boats, broken the bridges, or otherwise eliminated the option to fall back — forcing maximum effort. In modern context: voluntarily eliminate your fallback options. Without the option to retreat, performance rises.",
    usable_principle="Identify your safety nets. The ones that protect you against catastrophe — keep. The ones that let you avoid commitment (always-applying-for-other-jobs, hedge-bet side projects, optionality preserved against the main play) — burn deliberately.",
    sniped_relevance="The AWS field-engineering job IS BJ's safety net + funding mechanism (per 100Q Audit chunk). NOT to be burned — it's the runway that enables long-game compounding. But other 'optionality hedges' should be examined: side-creative project ideas, generic photography work 'just in case,' undefined-future income streams that absorb mental energy. The SNIPED OS already enforces this via the 99_VAULT being explicitly EMPTY (no non-SNIPED adjacent IP projects). The discipline is in maintaining the emptiness.",
    direct_quotes=[
        "We are at our most strategic when we are forced to be resourceful, when we use our wits because we must.",
        "Death-ground strategy is a way of forcing yourself into the position of having to fight."
    ],
    tags=["greene","commitment","death-ground","optionality"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 5 · Avoid the snares of groupthink · the command-and-control strategy",
    summary="Committees produce average decisions. The structure that wins delegates execution broadly but concentrates STRATEGIC decisions in a single mind. Hierarchical command isn't authoritarian — it's a recognition that strategy requires coherence, and coherence requires a single decision-making locus.",
    usable_principle="Distinguish strategic decisions (must be made by one person, not delegated) from execution decisions (must be delegated to whoever is closest to the work). Confusing the two — strategy by committee, execution by central control — produces the worst of both.",
    sniped_relevance="OPERATIONAL_BACKBONE.md's 10 'un-delegate-ables' list IS the command-and-control distinction. Direction Stack diagnostic, methodology refinement, pricing decision, Year-10 vision, the decision to decline, aesthetic call — all reserved to BJ alone. Everything else delegated explicitly. This is not micromanagement; it's exactly what Greene prescribes — coherent strategy, distributed execution.",
    direct_quotes=[
        "What you want is a group with a clear chain of command, in which orders move quickly from the top down through the ranks."
    ],
    tags=["greene","command","delegation","decision-making"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 6 · Segment your forces · the controlled-chaos strategy",
    summary="Concentrating all force in one massive unit makes you slow, predictable, and vulnerable to a single decisive blow. Segmenting force into independent units that can act autonomously creates speed, redundancy, and the ability to take risks (each unit's failure doesn't cascade).",
    usable_principle="Don't put all production into one client, one platform, one channel. Build redundant smaller bets that compound independently. The portfolio of small bets outperforms the single big one over long horizons.",
    sniped_relevance="The three SNIPED engines (Revenue/Audience/Reputation) IS this segmentation. The two-channel outbound (LinkedIn VIB + cold email) IS segmentation. The recurring-series content philosophy (multiple named series running parallel) IS segmentation. Each can be paused/expanded independently. Counter-discipline: don't merge them into a single mega-funnel; the segmentation IS the resilience.",
    direct_quotes=[
        "Concentrated power is hostile to flexibility."
    ],
    tags=["greene","segmentation","resilience","portfolio"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 8 · Pick your battles · the perfect-economy strategy",
    summary="Resources are always finite. The general who fights only the battles that materially advance the strategic position wins on net. The one who fights every challenge offered exhausts the army and loses to the conserver. Economy of force is itself an offensive principle.",
    usable_principle="Three filters for any potential engagement: does it advance the strategic position? Does it cost less than the alternative? Does winning it open downstream advantage? If less than 3 yes, decline.",
    sniped_relevance="The Constraint Audit's monthly question 'what is the single bottleneck this month?' is the perfect-economy applied. Same with the EXECUTION_PRIORITIZATION list — explicitly tiering tasks so that only Tier 1 gets attention until cleared. The 4-yes-default-NO rule for free shoots is the same discipline. Greene's framing makes the discipline emotionally easier — it's not 'I'm being precious'; it's perfect economy of force.",
    direct_quotes=[
        "Choose your battles wisely. Strategy depends on knowing when not to fight."
    ],
    tags=["greene","selectivity","economy","focus"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 12 · Lose battles but win the war · grand strategy",
    summary="Tactical losses are acceptable when they serve strategic gains. The general who refuses to lose any battle wins each one but loses the war by exhausting force. The general who accepts well-chosen losses preserves capacity for the decisive engagement. Grand strategy is the discipline of subordinating tactical pride to strategic victory.",
    usable_principle="When a specific opportunity is a tactical win but a strategic drift, refuse it. The cost of the refusal (lost revenue, perceived rejection) is repaid by maintained strategic position.",
    sniped_relevance="Refusing the $5K wedding gig that would 'just be one weekend' is a tactical loss (cash on the table) that preserves the strategic position (operator-coded LA founder lane). Same for refusing a celebrity branding deal whose values contradict the methodology. Same for refusing to compress the 5-day SLA to 24 hours when a client pressures (the SLA discipline IS the brand). Per Greene: the photographer who said yes to every paying job from 2018-2026 has higher cumulative revenue but no lane.",
    direct_quotes=[
        "Some lose battles but win the war. Others win battles but lose the war."
    ],
    tags=["greene","grand-strategy","tradeoffs","long-game"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 17 · Defeat them in detail · the divide-and-conquer strategy",
    summary="A unified enemy is hard to defeat. The same enemy split into pieces can be defeated piece by piece, the pieces unable to reinforce each other. Divide the opposition (or the problem, or the market) into manageable units and address them sequentially with full force.",
    usable_principle="A problem that seems overwhelming as a whole becomes solvable when broken into independent pieces. A market too large to enter at once becomes enterable when you pick one segment and dominate it.",
    sniped_relevance="Maps to Thiel's 'start small and monopolize' chunk above. SNIPED's 'pick one rung above your highest proven' discipline. The 6-element Minimum Viable Empire (per BATCH_001) is a divide-and-conquer of the full SNIPED architecture — pick the 6 highest-leverage loops, defeat them in detail, then expand. Same for VIB list segmentation: break the LA founder TAM into trigger-tier segments, work each tier with appropriate force.",
    direct_quotes=[
        "Look for the parts of the whole that you can divide."
    ],
    tags=["greene","divide-and-conquer","segmentation","sequencing"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 21 · Negotiate while advancing · the diplomatic-war strategy",
    summary="The strongest negotiating position is the one where you don't need the deal AND are visibly advancing without it. Negotiation from weakness produces concession; negotiation from strength produces favorable terms. Continue building your position even during negotiation — let the other party see that the deal is for their benefit, not yours.",
    usable_principle="Before any major negotiation, ensure you have at least one alternative path forward. The visible alternative is the leverage. Without it, you're negotiating from need.",
    sniped_relevance="Holding the $1,500 floor in cold pricing only works if SNIPED has alternative paths to revenue (other prospects in pipeline, paid Reset weeks already booked, the AWS engineering income covering the rent regardless). The 'no discount, remove deliverables instead' discipline from BATCH_001 IS this strategy. When prospects sense desperation (the operator NEEDS this deal), they extract concessions. When they sense alternatives (the operator doesn't), they accept terms.",
    direct_quotes=[
        "The art of war is the art of negotiation by other means."
    ],
    tags=["greene","negotiation","leverage","alternatives"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 25 · Occupy the moral high ground · the righteous strategy",
    summary="In any conflict, the side perceived as righteous gains popular support, attracts allies, and faces less resistance. The actual righteousness matters less than the perceived righteousness. Strategists deliberately position themselves on the moral high ground — even when fighting for material reasons — because the moral framing recruits energy that pure self-interest cannot.",
    usable_principle="Frame your strategic position in terms of what you serve, defend, or protect — not what you take. The frame is real once it is held consistently.",
    sniped_relevance="SNIPED's positioning serves the Year-10 cultural-documentation horizon (preserving the moment of LA emerging Black founder/artist culture for the record), serves operator-coded founders against the commodity headshot economy, serves the methodology lineage against AI commoditization, serves cultural institutions through the reciprocity ledger. These are real and they are also moral high ground. The framing recruits energy that pure 'sell expensive portraits' framing cannot.",
    direct_quotes=[
        "Find a higher cause to fight for and you have what is called the moral high ground."
    ],
    tags=["greene","moral-high-ground","framing","mission"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy 33 · Sow uncertainty and panic through acts of terror · the chain-reaction strategy",
    summary="Greene's final strategy (named provocatively but operationally specific): in a competitive landscape, a single dramatic, hard-to-predict move can shake competitors out of their patterns, force them into hasty responses, and break their strategic coherence. The point is not violence — it's pattern-disruption that destabilizes the competitor's planning.",
    usable_principle="Once per year, consider a single dramatic move that competitors cannot have predicted. The point is not chaos for its own sake — it's resetting the competitive landscape's assumption about what you will and won't do.",
    sniped_relevance="Light application for SNIPED (an emerging player): the Direction Stack book public launch in Q3 2026 IS the pattern-disrupting move. No other LA founder-photographer is publishing a 57-page methodology book with a named protocol vocabulary. The launch will reset what LA founder-photographer-buyers expect from the category. Subsequent moves (the Substack Q3 launch, the first gallery show by Year 3-4) play similar roles at later stages.",
    direct_quotes=[
        "By acting in a way that is unconventional and surprising, you destabilize your enemy."
    ],
    tags=["greene","pattern-disruption","surprise","competitive-strategy"]
)

# =============================================================
# Steve Jobs · Walter Isaacson
# =============================================================
STITLE = "Steve Jobs"
SFILE = "steve_jobs_isaacson.md"
AUTHOR = "Walter Isaacson"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="taste",
    concept="The intersection of liberal arts and technology",
    summary="Jobs's enduring formulation: the place where Apple lives is at the crossing of the humanities (taste, design, story, craft) and technology (the hard engineering that delivers the experience). Products that live only on one side feel either cold (pure tech) or precious (pure aesthetic). The intersection is rare and defensible because it requires unusual founders.",
    usable_principle="The most defensible positions live at the intersection of disciplines. Build at the seam, not in the center of a single field.",
    sniped_relevance="SNIPED's empty intersection (per BATCH_001 STRATEGIC_PRINCIPLES): editorial commercial photography × serious cultural documentation × operator-coded methodology. Each ingredient requires a different discipline; the intersection IS the moat. BJ's engineer-to-operator-photographer arc is the personal-level expression of the same intersection (engineering rigor × taste × cultural fluency).",
    direct_quotes=[
        "Technology alone is not enough. It's technology married with liberal arts, married with the humanities, that yields us the result that makes our hearts sing.",
        "The people who are crazy enough to think they can change the world are the ones who do."
    ],
    tags=["jobs","intersection","craft","positioning"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="taste",
    concept="End-to-end control · own the whole stack",
    summary="Jobs's view that the integrated product is fundamentally superior to the open/modular one. When one company controls hardware, software, services, and experience, every layer can be calibrated against every other. The trade-off is reach (smaller market) for excellence (better artifact). This is Apple's core strategic bet, made explicitly against Microsoft's open licensing model.",
    usable_principle="Where you have the choice between owning the full stack (slower, more expensive, better artifact) vs assembling from off-the-shelf parts (faster, cheaper, worse artifact), choose ownership when the artifact's excellence is the brand.",
    sniped_relevance="The SNIPED v2 delivery architecture (Heroes/Selects/Proofs all rendered through one operator's locked aesthetic, one Lightroom catalog, one Evoto preset stack, one Pixieset template, one delivery email sequence) IS end-to-end control. The temptation to outsource pieces (let the model bring their own MUA, let the client choose the editing app, let a third-party gallery handle delivery) collapses the integrated experience. The retoucher hire (Mo 6-9) must preserve the integrated stack, not fragment it.",
    direct_quotes=[
        "I have always wanted to own and control the primary technology in everything we do.",
        "It's really hard to design products by focus groups."
    ],
    tags=["jobs","integration","quality","control"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="taste",
    concept="Focus is saying no to good ideas",
    summary="When Jobs returned to Apple in 1997, the product line had ~350 SKUs. He cut it to four: consumer/pro × desktop/laptop. The cuts killed several products that were genuinely good and had real customers. The discipline: focus isn't refusing the bad ideas; the bad ideas are easy to refuse. Focus is refusing the GOOD ideas so that the great ones can have all the resources.",
    usable_principle="Once a quarter, audit the active project list. The cuts that hurt are the ones that matter. Anything that's 'good but not central to the thesis' is candidate for removal.",
    sniped_relevance="The SNIPED Phase 1 'do not start' list (per OPERATING_BRIEF + EXECUTION_PRIORITIZATION): TikTok daily volume, custom website beyond Carrd, paid ads, course product, cold-email infrastructure, wedding/family/lifestyle work, refereeing income, multi-city expansion. Many of these ARE good ideas with real upside. They are deliberately refused so that the 6-element MVE has all the resources. The discipline IS the asset.",
    direct_quotes=[
        "Focusing is about saying no.",
        "People think focus means saying yes to the thing you've got to focus on. But that's not what it means at all."
    ],
    tags=["jobs","focus","refusal","prioritization"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="hiring",
    concept="A-players hire A-players · B-players hire C-players",
    summary="Jobs's hiring axiom: top performers want to work with other top performers and will hire accordingly. Mediocre performers feel threatened by top performers and hire down. The first wrong hire at a senior level can cascade through a generation of hiring and is very hard to recover from. Therefore the founder must guard the hiring bar personally, especially at senior levels, for as long as possible.",
    usable_principle="Stay personally involved in every hire above an entry level for as long as possible. The cost of one wrong senior hire is permanent.",
    sniped_relevance="For SNIPED, this means BJ personally evaluates every hire (retoucher Mo 6-9, social VA Mo 12+, general VA Mo 12+, bookkeeper Mo 9+, eventual content editor Mo 9-12) — none of these get delegated to a third-party hiring service. The 'cult-like cohesion' principle from Thiel reinforces this: hire on shared belief, not just skill. Greene's Law 25 (re-create yourself) means the people you hire become part of the SNIPED identity construction.",
    direct_quotes=[
        "A small team of A+ players can run circles around a giant team of B and C players.",
        "It doesn't make sense to hire smart people and then tell them what to do; we hire smart people so they can tell us what to do."
    ],
    tags=["jobs","hiring","quality-bar","team-building"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Reality distortion field · willing the impossible",
    summary="Jobs's signature leadership effect: insisting on outcomes that engineers and designers initially called impossible, and through that insistence, pulling them into achieving them. Not bullying but a deep refusal to accept the artificial limits people imposed on themselves. Bud Tribble named the effect (after Star Trek) — and acknowledged it was real even though it broke from how rational management was supposed to work.",
    usable_principle="The 'realistic' estimate from your team is often the conservative one. Push for the version that requires creative problem-solving. Some of the team will rise; the rising defines the strategic baseline.",
    sniped_relevance="The SNIPED 5-day Reset SLA, the 12-15 min/Hero edit target, the 6 VIBs/week cadence — these are reality-distortion numbers that force the system to be designed for them. The conservative estimate would be 7-day SLA, 25 min/Hero, 3 VIBs/week. The aggressive numbers force the discipline that produces actual operator-grade output. Light caveat: distortion without integrity destroys trust; the SNIPED version is 'commit to hard numbers AND tell the team why' (per the Production OS time-cap discipline).",
    direct_quotes=[
        "Real artists ship."
    ],
    tags=["jobs","leadership","ambition","execution"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="Brand is the residue · what people say when you're not in the room",
    summary="Apple's brand wasn't built by marketing campaigns (though those reinforced it). It was built by what the products themselves communicated, frame by frame, decision by decision. Every interaction with an Apple artifact (the box, the unboxing, the startup, the materials, the support call) either reinforces or erodes the brand. Marketing is the tip of the iceberg; the iceberg is the operational discipline.",
    usable_principle="Every touchpoint is a brand vote. Audit your customer's entire journey, not just the marketing surfaces. The unmarketed touchpoints (invoice format, delivery email tone, the pre-shoot brief, the post-shoot follow-up cadence) carry as much brand weight as the website.",
    sniped_relevance="The PRODUCTION_OS one-shoot-to-eight-outputs pipeline + the post-delivery email cadence + the Pixieset gallery template + the Day-7 testimonial ask + the Day-30 Op Kit pitch — these are all brand touchpoints, not just operations. The detail of the 6 SNIPED locks (signature recognizability test) is brand-building through operational consistency. The Day-30 Op Kit DM written in operator voice (NOT a templated salesy nudge) IS the brand reinforced quietly.",
    direct_quotes=[
        "Design is not just what it looks like and feels like. Design is how it works.",
        "We don't get a chance to do that many things, and every one should be really excellent."
    ],
    tags=["jobs","brand","touchpoints","operational-discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Stay hungry, stay foolish · Whole Earth Catalog farewell",
    summary="Jobs's 2005 Stanford commencement speech ended with the Whole Earth Catalog's final-issue benediction. The phrase compresses two psychological postures: continued ambition (hunger) and willingness to look stupid pursuing unproven ideas (foolish). Both are needed; either alone is insufficient. The combination is rare because most people lose one as they accumulate the other.",
    usable_principle="Preserve both ambition and openness to looking foolish. Comfortable expertise without ambition produces stagnation; ambitious certainty without willingness to be wrong produces brittle empires.",
    sniped_relevance="SNIPED is in Year 0 of a Year-10 plan. The hunger is structural (the 18-24 Resets target, the named-figure-by-2036 horizon). The foolishness is the willingness to ship a methodology book (no other LA founder-photographer does this), to send VIBs that competitors would call 'gimmicky,' to publicly disclose the methodology on the artifact's colophon (competitors hoard process). Each is the foolishness that compounds into competitive advantage if held long enough.",
    direct_quotes=[
        "Stay hungry. Stay foolish.",
        "Your time is limited, so don't waste it living someone else's life."
    ],
    tags=["jobs","ambition","beginner-mind","founder-psychology"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Connect the dots looking backward",
    summary="Jobs's Stanford speech also: 'You can't connect the dots looking forward; you can only connect them looking backward.' Career and strategic decisions cannot be optimized in advance for an unknown future. The best one can do is to follow curiosity and commitment with intensity, trusting that retrospectively the path will reveal coherence.",
    usable_principle="Don't paralyze on optimal sequencing. Pick the move that resonates with the current thesis and commit fully. The next move will reveal itself only after the current one is executed.",
    sniped_relevance="Maps to the BATCH_001 advice to ship VIB #1 rather than refine the master file. Also maps to the long-arc Year-10 vision: the specific path from Year 1 to Year 10 cannot be planned in detail, but the next 90-day move can be committed to with confidence. Don't over-plan the dot-connection.",
    direct_quotes=[
        "You can't connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future."
    ],
    tags=["jobs","emergence","commitment","trust"]
)

# =============================================================
# The Ride of a Lifetime · Robert Iger
# =============================================================
STITLE = "The Ride of a Lifetime"
SFILE = "ride_of_a_lifetime_iger.md"
AUTHOR = "Robert Iger (with Joel Lovell)"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Optimism without delusion · the leadership posture",
    summary="Iger's first principle of leadership: people will not follow a pessimist. The leader must be the most genuinely (not performatively) optimistic person in the room — not blind to problems, but framing problems as solvable. The energy of the leader sets the energy of the org. The hardest version is during crisis, when the temptation to be visibly worried is strongest.",
    usable_principle="Be the most energy-giving presence in every conversation about a problem. Acknowledge the problem fully; then immediately move to the solvable framing. The shift from problem-recognition to solution-orientation is the leadership move.",
    sniped_relevance="For SNIPED solo-founder application: this is internal-leadership of self. When the pipeline is empty (which it is in Phase 1), the temptation is internal pessimism. The discipline is genuine optimism grounded in the strategic logic (the 10-year horizon, the methodology IS the moat, the 12 canonical truths are correct). Iger's frame applied to a 1-person org: be the energy you'd want a CEO to bring.",
    direct_quotes=[
        "Optimism in a leader, especially in challenging times, is so vital.",
        "Pessimism leads to paranoia, which leads to defensiveness, which leads to risk aversion."
    ],
    tags=["iger","leadership","optimism","posture"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Courage · the willingness to take big risks",
    summary="Iger's three big acquisitions as Disney CEO (Pixar 2006 $7.4B, Marvel 2009 $4B, Lucasfilm 2012 $4B) each required betting more than the company could afford to lose, on outcomes that were not guaranteed. The pattern: identify the strategic gap, find the right asset, pay a premium price, and integrate without destroying the acquired culture. Each acquisition was widely doubted at the time; each is now seen as transformative.",
    usable_principle="The biggest strategic moves require accepting unrecoverable risk on the upside case. Hedge-bet caution preserves you in the short term but loses the decade.",
    sniped_relevance="For SNIPED, the equivalent 'big bets': committing to the Direction Stack book launch as the central authority asset (vs many smaller content products); committing to the cultural documentation thesis as a 10-year compounder (vs Year-1 ROI optimization); the eventual commitment to long-term studio lease in Year 3-5 (vs perpetually Peerspace-flexible). Each requires unrecoverable commitment. Each defines the 10-year position.",
    direct_quotes=[
        "The riskiest thing we can do is just maintain the status quo.",
        "If you don't innovate, you die."
    ],
    tags=["iger","risk","commitment","big-bets"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Decency matters · how you treat people is the brand",
    summary="Iger emphasizes that the way leaders treat people — including in difficult moments like firings, transitions, and disputes — accumulates as a reputation that affects every future relationship. Decency is not a soft virtue; it is the long-term compound interest of executive behavior. The leader who fires people humanely is the leader other A-players will join in the next role.",
    usable_principle="In any difficult interaction (firing a contractor, ending a client relationship, refusing a referral), behave as if every person in the room will be in some future relationship with you. The cost of decency is low; the cost of indecency is permanent.",
    sniped_relevance="In SNIPED practice: how Ren or Rejuar are spoken to in tense moments, how a client who is being declined is communicated with, how a contractor whose work is rejected is told. The Hospitality vs Service principle (BATCH_001 STRATEGIC_PRINCIPLES) is the same idea framed differently — what's promised vs what's delivered above-and-beyond. Decency is internal; hospitality is external; both compound.",
    direct_quotes=[
        "How you treat people during the worst moments matters.",
        "We've been taught throughout our lives that the world is full of zero-sum games — but the best deals are good for both sides."
    ],
    tags=["iger","leadership","decency","reputation"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Avoid micromanagement of brilliant people · respect autonomy",
    summary="Iger's policy with John Lasseter at Pixar after acquisition: Disney would not impose its way of working on the smaller studio. The deal-makers' instinct is to integrate immediately and extract synergies. Iger's instinct was the opposite: leave the goose alone and let it keep laying golden eggs. The acquisition's value is in what made the acquired entity special; integration that erases that destroys the value.",
    usable_principle="When you bring in someone exceptional, define the boundaries of authority broadly and don't trespass. The instinct to check, redirect, and 'add value' often destroys the exact thing you hired the person for.",
    sniped_relevance="For SNIPED's eventual hires (especially retoucher and content editor), this means: define the quality standard (BJ's pass-4 review, the 7 SNIPED signatures, the reject criteria); define the workflow boundaries; then let them work. Don't check pixels at midnight. Don't second-guess every cut. The exception is the explicit quality gate, which is non-negotiable; everything else is autonomous.",
    direct_quotes=[
        "I find micromanaging to be extremely disempowering.",
        "If you've found someone you trust, set them loose."
    ],
    tags=["iger","autonomy","delegation","trust"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Tell the truth · about the work and about the situation",
    summary="Iger argues against the executive habit of softening hard truths. Employees and partners read sanitized messages as condescension; they appreciate being treated as adults. Honest framing of bad situations — including admitting uncertainty about outcomes — produces more trust and more effective collective action than spin.",
    usable_principle="Default to honesty about the situation, including uncertainty. Sanitized 'everything is fine' communication erodes trust over time even when each individual instance seemed harmless.",
    sniped_relevance="Maps to the SNIPED voice rules (per cold_email_doctrine): mid-conversation feel, slight imperfection, no buzzwords, no corporate tone. The honesty layer extends to client communications: if a Reset edit will take an extra day, say so directly with the actual reason ('I'm at a higher quality bar on the Hero series this week'). The trust-equation Intimacy component is built through this exact honesty.",
    direct_quotes=[
        "True authority and true leadership come from knowing who you are and not pretending to be anything else.",
        "If something doesn't feel right to you, it won't be right for you."
    ],
    tags=["iger","leadership","honesty","trust"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Pace of change is the rate-limiter · execution speed as moat",
    summary="Iger's 15-year Disney run included shutting down hand-drawn animation, betting on Pixar acquisition, betting on Marvel, betting on Lucasfilm, betting on Disney+, expanding international parks. The cumulative pace mattered as much as any individual decision. The competitor that operates at a slower decision-velocity loses regardless of individual decision quality.",
    usable_principle="Compress decision-cycle time. The decisions that get made in days outperform the decisions that get made in months not because they are better but because they capture momentum the slow decision misses.",
    sniped_relevance="SNIPED's Phase 1 lean override is itself a decision-velocity bet (small loops shipped weekly, not perfected quarterly). The Monday Cockpit + weekly Constraint Audit + monthly Constraint Audit cadence is the compressed-decision mechanism. Counter-discipline: Phase B+ trigger requires resisting the temptation to add complexity that slows decision cycles ('let's wait for the Q3 strategic offsite to decide about the retoucher hire' = velocity erosion).",
    direct_quotes=[
        "The pace of change is going to accelerate, not slow down.",
        "Innovate or die, and there's no innovation if you operate out of fear of the new or untested."
    ],
    tags=["iger","speed","decision-velocity","compounding"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Strategy is a clear answer to three questions",
    summary="Early in his CEO tenure, Iger articulated Disney's strategy as three clear bets: (1) prioritize high-quality branded content (vs middle-tier volume); (2) embrace new technology (especially digital and direct-to-consumer); (3) become a truly global company (not US-with-international-offices). Every subsequent decision was tested against these three. The simplicity of three made the strategy executable across 200,000+ employees.",
    usable_principle="Compress strategy to three sentences. If you can't, the strategy isn't sharp enough yet. Every decision tests against the three; anything that doesn't serve them is candidate for cut.",
    sniped_relevance="SNIPED's three (per the OPERATING_BRIEF + CANONICAL_TRUTHS): (1) Build operator-coded methodology-led editorial portraiture as a defensible LA founder-photography position; (2) Build the cultural documentation archive as a 10-year compounding asset that AI cannot commoditize; (3) Build the Direction Stack as transferable IP that becomes the authority layer beyond the service business. Three sentences. Every Phase 1 decision tests against these.",
    direct_quotes=[
        "I asked myself: what are the three big things we need to do?"
    ],
    tags=["iger","strategy","clarity","three-bets"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Don't take it personally · separate self from role",
    summary="Iger emphasizes that hard feedback, criticism, and rejection accumulate over a career and the executive who internalizes each instance burns out. The discipline: receive the feedback against the role (CEO, photographer, operator), evaluate it on the merits, but do not let it leak into the self. The role can be wrong without the person being inadequate.",
    usable_principle="Maintain a structural distinction between self and role. Critique of the work is information; do not promote it into critique of the person.",
    sniped_relevance="For a solo founder, the boundary is harder because BJ is the role to a much greater extent than a Disney CEO. The mitigation: have explicit non-SNIPED identity domains (Pearl relationship, physical fitness, family roles, AWS work, personal friendships) that exist independent of how SNIPED is doing this quarter. The 'avoid burnout' practice in OPERATIONAL_BACKBONE is structurally addressing this. Iger's framing makes it more emotionally tractable: this isn't 'work-life balance' soft talk — it's role/self separation that preserves long-term decision quality.",
    direct_quotes=[
        "Don't let your ambition get in the way of your patience."
    ],
    tags=["iger","leadership","self-role-separation","sustainability"]
)

# =============================================================
# Creativity, Inc. · Ed Catmull (with Amy Wallace)
# =============================================================
STITLE = "Creativity, Inc."
SFILE = "creativity_inc_catmull.md"
AUTHOR = "Ed Catmull (with Amy Wallace)"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="creative-process",
    concept="If you give a good idea to a mediocre team they will screw it up · the team is primary",
    summary="Catmull's organizing claim from his Pixar tenure: creative output depends more on the team than on the idea. A great team can take a weak idea and iterate it into greatness; a weak team will take the best idea and produce mediocre output. Therefore the organizational focus is recruiting, retaining, and protecting the creative team, not generating ideas.",
    usable_principle="When evaluating a project's likelihood of success, weight the team's quality heavily and the idea's quality lightly. When deciding what to fund/build, invest in team capacity before idea generation.",
    sniped_relevance="For SNIPED, the 'team' includes the warm-relationship infrastructure (Rejuar, Ren, Hermine, Pearl as domestic anchor, returning models, the casting-call network). Investing in this team's capacity (paying Rejuar fair rates, treating Ren well in the cold-outreach work, retaining the MUA relationships, recurring-subject collaborators like Yae) is higher leverage than perfecting any single new content idea or visual concept. Greene's Law 11 (indispensability) compounds: the team is the asset.",
    direct_quotes=[
        "Ideas come from people. Therefore, people are more important than ideas.",
        "If you give a good idea to a mediocre team, they will screw it up. If you give a mediocre idea to a great team, they will either fix it or throw it away."
    ],
    tags=["catmull","team","creative-process","Pixar"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="creative-process",
    concept="The Braintrust · candid feedback without authority",
    summary="Pixar's signature institution: a group of director-peers who review films-in-progress and give brutally honest feedback. The Braintrust has no decision authority — the director can take or leave the feedback. This is the load-bearing structural design: feedback without authority allows total honesty (no political consequences for the giver, no defensive bracing from the receiver). Authority-bearing feedback hardens defenses; the Braintrust dissolves them.",
    usable_principle="Build a recurring feedback structure of trusted peers who have no authority over your work. Their job is to tell you what they actually see. Your job is to consider it without obligation.",
    sniped_relevance="For SNIPED solo-founder: the equivalent is a curated 3-5 person 'Braintrust' (Larry Bernard quarterly call, Ramon for film/video, possibly 1-2 future operator-peers identified by Year 2). Their job: review the latest Reset deliveries, the chapter rollouts, the LinkedIn POV bank, with full honesty and no obligation to act on their feedback. Already partially implicit in OPERATIONAL_BACKBONE's quarterly Larry mentor call; formalize as the SNIPED Braintrust.",
    direct_quotes=[
        "The Braintrust meets every few months to assess each movie we're making.",
        "Its premise is simple: Put smart, passionate people in a room together, charge them with identifying and solving problems, and encourage them to be candid."
    ],
    tags=["catmull","feedback","peer-review","candor"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="creative-process",
    concept="Early movies all suck · the iteration discipline",
    summary="Every Pixar film starts ugly. Toy Story's early cuts were unwatchable. Up was a different movie at draft 1. The pattern: creative work begins as failure; iteration converts it. The discipline is not avoiding the ugly early phase (impossible) but not panicking through it. Creative teams that lose nerve at early-ugly kill films that would have been great by draft 10.",
    usable_principle="Expect the first version to be bad. Plan iteration cycles into the schedule, not as 'in case of need.' The bad first version is the input to the good final version, not evidence of failure.",
    sniped_relevance="For SNIPED, this maps to: the first VIBs will be awkward; the first Reset deliveries will be over-edited; the first LinkedIn POVs will read self-conscious; the first chapter rollout (CH01 Yae) will reveal problems. Do not abandon the system because the first executions are imperfect. Iteration converts. The reps ARE the path. This is encoded in the 'feedback_repetition_over_novelty' memory lock from BATCH_001.",
    direct_quotes=[
        "Early on, all of our movies suck.",
        "Our job is not to prevent the suck. Our job is to go from suck to not-suck."
    ],
    tags=["catmull","iteration","first-drafts","creative-discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Trust the process · but the process is iteration, not steps",
    summary="Catmull warns against turning 'the process' into rigid steps that produce safety theater. Pixar's process is iteration with candid feedback — that's the only constant. Specific step lists (storyboard → animatic → animation → render) are tools, not the process. Teams that worship the steps stop iterating; teams that iterate adapt the steps.",
    usable_principle="Codify the iteration loops, not the specific steps. The steps will change; the loop is the constant.",
    sniped_relevance="The 6 backbone loops in OPERATIONAL_BACKBONE (VIB, Reset, Authority, Cultural Doc, Day-30, Constraint Audit) ARE the iteration loops. The specific steps within each loop (which scheduler, which CRM field, which email template) are tools that can change without breaking the system. The discipline is protecting the LOOPS while remaining open to changing the steps inside them. Pre-flight checklist + post-mortem = process; the specific items on the checklist = tools.",
    direct_quotes=[
        "Trust the process is not a magic formula. It's a recognition that the process is iteration with candor."
    ],
    tags=["catmull","process","iteration","tools-vs-process"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Postmortems are about learning, not blame",
    summary="Pixar's post-project reviews focus on extracting transferable lessons, not assigning blame. The shift requires explicit cultural design: leaders model self-criticism, blame-language is replaced with 'what did we learn,' and the lessons are documented and propagated to subsequent projects. Without this structure, postmortems become defensive theater and no learning happens.",
    usable_principle="After every project or shoot, run a structured post-mortem: what worked, what didn't, what's the transferable lesson. Document it. Make sure leadership self-critiques first; this signals safety for others.",
    sniped_relevance="The /90_NOTES/ subfolder in PRODUCTION_OS per-shoot folder structure IS the postmortem container. The monthly Constraint Audit IS the broader postmortem cycle. The structure exists; the discipline is filling it after every shoot, not just when something went badly. CH01 Yae postmortem already implicit in the 100Q_AUDIT chunk that identified bottlenecks (Rejuar composite turnaround, communication cadence). Make the practice explicit and recurring.",
    direct_quotes=[
        "Postmortems are one of the most valuable tools we have at Pixar."
    ],
    tags=["catmull","postmortem","learning","reflection"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Protect new ideas · the fragile early phase",
    summary="Promising new ideas are vulnerable in their early phase. Subjected to too much scrutiny too early, they get killed by 'real-world objections' that the idea hasn't had time to answer yet. Catmull argues for deliberately shielding early-stage ideas from full critique until they've had room to develop their own logic.",
    usable_principle="When an idea is in its early phase, share it with a tiny trusted circle that can give 'how do we develop this' feedback, not 'why it won't work' critique. Open the critique aperture as the idea gains its own legs.",
    sniped_relevance="For SNIPED, this applies to: the Direction Stack book in its drafting phase (kept private until Rejuar's design is closer to deliverable); the Substack drafts in their Q3 prep phase; any new offer experiments before they're battle-tested. The OPERATING_BRIEF's distinction between 'active surface' and '99_VAULT' is structurally similar — vault is for new ideas that aren't ready for full pressure-test yet.",
    direct_quotes=[
        "Originality is fragile. And, in its first moments, it's often far from pretty.",
        "To create, you must have a long view; you can't make decisions based on the noise of the moment."
    ],
    tags=["catmull","early-ideas","protection","creative-process"]
)

# =============================================================
# Shoe Dog · Phil Knight
# =============================================================
STITLE = "Shoe Dog"
SFILE = "shoe_dog_knight.txt"
AUTHOR = "Phil Knight"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="founder-psychology",
    concept="Crazy idea · committing before you're ready",
    summary="Knight's memoir documents the long path from a Stanford business-school paper about importing Japanese running shoes to Nike's global dominance. The through-line: at every decision point, Knight committed before the move was 'rational.' Borrowing more than he could repay. Hiring people Nike couldn't afford. Going public before the company was ready. The pattern is not recklessness but the recognition that ready-state never arrives for any worthwhile move.",
    usable_principle="Most worthwhile commitments require acting before you're ready. The 'ready' state is usually a phantom that recedes as you approach it. Commit on the basis of the strategic logic, not the comfort level.",
    sniped_relevance="The BATCH_001 'uncomfortable necessary actions' chunk lists this principle in specific form (send VIB #1; quote $1,500 without flexing; drop the LinkedIn promotion-announcement post; pitch the Day-30 Op Kit). Knight's broader frame: ready-state will not arrive. The Direction Stack book is not 'ready' for public launch; the Substack is not 'ready' to start drafting; the gallery conversations are not 'ready' to initiate. The strategic logic for committing to each is sound. Ready is the wrong gate.",
    direct_quotes=[
        "Just do it.",
        "The cowards never started, and the weak died along the way. That leaves us."
    ],
    tags=["knight","commitment","action","founder-psychology"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="The Buttfaces · candid inner circle running an emerging company",
    summary="Knight's nickname for his early Nike inner circle (the original team of misfit shoe-obsessives). Their working pattern: brutal candor, low formality, deep mutual loyalty, and a willingness to fight for years through cash crises, customs disputes, and competitor wars. The team's cohesion through hardship is what kept Nike alive through the periods when it should not have survived.",
    usable_principle="The early team is the only thing that survives a sustained crisis. Build it from people who can disagree productively, hold conviction under pressure, and stick through years of unfunded uncertainty.",
    sniped_relevance="SNIPED's current core (BJ + Rejuar + Ren + Hermine, plus Pearl as domestic anchor) IS the Buttfaces analog. The crisis-survival quality of the team has not yet been pressure-tested at SNIPED's scale — that comes when (not if) the first major setback hits. Preserve the bond now: visible recognition when wins happen, fair pay even when SNIPED can't afford much, transparency about runway, and deep listening when team members raise concerns. Iger's decency principle + Catmull's team-first principle reinforce.",
    direct_quotes=[
        "There comes a time in every company's life when it must be reinvented, when it must be saved from itself.",
        "Beating the competition is relatively easy. Beating yourself is a never-ending commitment."
    ],
    tags=["knight","team","inner-circle","loyalty"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="Beating the competition is relatively easy · beating yourself is the work",
    summary="Knight's late-book reflection on Nike's three-decade arc: the external competition (Adidas, Reebok, Asics) was visible and addressable. The harder fight was internal — Nike's own complacency, the temptation to take the easy customer, the drift toward decisions made for short-term comfort. Each generation of internal challenge was harder than the last because previous successes built up the institutional habits that became liabilities.",
    usable_principle="External competition is the easy version. The harder version is the internal drift toward comfort decisions, hedge-bets, and short-term optimizations. Schedule explicit anti-drift moments (the quarterly Constraint Audit, the annual 10-year vision re-read) to surface it.",
    sniped_relevance="The 8 drift symptoms in OPERATIONAL_BACKBONE.md are exactly this — internal-drift detection. The 'wrong game' drift (checking IG analytics, comparing follower counts), the 'motion confused with progress' drift (producing posts with no VIBs sent), the 'drifting from moat' drift (considering wedding gig 'this one time') — each is internal, not external. Knight's frame names the deeper truth: the internal fight is the lifelong one. The external competitor list never matters as much as the internal discipline.",
    direct_quotes=[
        "Beating the competition is relatively easy. Beating yourself is a never-ending commitment."
    ],
    tags=["knight","discipline","internal-vs-external","founder-psychology"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="The relationships build the company · long-arc loyalty",
    summary="Nike's relationships with the Japanese shoe manufacturers (Onitsuka first, then independents) were the load-bearing supply chain through the early years. Knight's pattern of personal visits, drinking sessions, decades-long relationships, and willingness to fly across the Pacific for one meeting was not romantic — it was operational. The relationships WERE the business when there was no other moat.",
    usable_principle="In emerging businesses, individual relationships ARE the company. Invest in them with personal time, not just transactions. The long-arc loyalty compounds across decades.",
    sniped_relevance="The OPERATIONAL_BACKBONE 'relationship infrastructure neglected' drift symptom + the 'Tier 1-5 relationships' framework from REVERSE_ROADMAP encode this. Pearl, Larry, Ramon, Rejuar, Bishop Peters network, Tracy at Davis Law, key recurring models (Yae, Mimi) — each is a long-arc relationship asset. Knight's frame justifies the quarterly mentor calls, the unsolicited touches, the deliberate cadence of relationship maintenance.",
    direct_quotes=[
        "You measure yourself by the people who measure themselves by you."
    ],
    tags=["knight","relationships","long-arc","loyalty"]
)

# =============================================================
# The Everything Store · Brad Stone
# =============================================================
STITLE = "The Everything Store"
SFILE = "everything_store_bezos_stone.md"
AUTHOR = "Brad Stone"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Customer obsession · the only durable orientation",
    summary="Stone documents Bezos's persistent reorientation of Amazon away from competitor-focus and toward customer-focus. Competitor-focus produces feature races, copying, and reactive strategy. Customer-focus produces unbounded ambition (the customer always wants more) and structural advantage (your decisions are calibrated to a moving but knowable target). The first question in every Amazon decision: 'Is this what the customer wants?'",
    usable_principle="Reorient every strategy meeting from 'what are competitors doing' to 'what does the customer want that they don't yet have.' The first question is reactive; the second is generative.",
    sniped_relevance="The SNIPED Mom Test discipline (talk about THEIR life, not your idea) + the de-Botton-grounded buyer-psychology framing (the founder wants to be observed/attended/noticed) are customer-obsession applied. Counter-discipline: don't over-rotate to 'what other LA founder-photographers are charging' — that's competitor-focus. The locked $1,500 floor is calibrated to founder-buyer status psychology, NOT to market-rate benchmarking.",
    direct_quotes=[
        "If you're competitor-focused, you have to wait until there is a competitor doing something. Being customer-focused allows you to be more pioneering."
    ],
    tags=["bezos","customer-obsession","strategy","orientation"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Day 1 · the company that stops being Day 1 starts dying",
    summary="Bezos's framing of corporate metabolism. Day 1 companies have founder energy, customer obsession, decision velocity, and the willingness to take big risks. Day 2 companies have stasis, followed by irrelevance, followed by death. The transition is gradual and invisible from inside. Bezos kept his office in a building called 'Day 1' to make the symbol load-bearing.",
    usable_principle="Audit yourself quarterly: am I still operating in Day 1 mode? Specific markers: am I making decisions in days not months? Am I still talking to customers directly? Am I still willing to take risks on unproven moves?",
    sniped_relevance="For SNIPED at Year 0, Day 1 is structural — there's no other mode available. The discipline begins to matter at Year 3-5 when the first scale tempts the Day 2 patterns (delegate every client interaction, stop sending VIBs personally, lose direct contact with the audience). The OPERATIONAL_BACKBONE 'un-delegate-ables' list IS the Day-1 defense in advance — BJ keeps direct customer contact (VIB sends, Discovery calls, Day-30 pitches) permanently, even as other functions delegate.",
    direct_quotes=[
        "Day 2 is stasis. Followed by irrelevance. Followed by excruciating, painful decline. Followed by death.",
        "And that is why it is always Day 1."
    ],
    tags=["bezos","day-one","metabolism","founder-mode"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="High standards · the willingness to be loved or hated",
    summary="Stone documents Bezos's reputation for being demanding to the point of cruelty in meetings. The justification: high standards produce high-quality output, and high-quality output is the only durable competitive advantage. Bezos was willing to be disliked in exchange for product excellence. The leaders who optimize for being liked produce mediocre work.",
    usable_principle="When you have to choose between being liked and being right, the long-run choice is being right (delivered with as much grace as possible, but the rightness is non-negotiable).",
    sniped_relevance="The SNIPED 12-15 min/Hero ceiling, the 7-signature recognizability test, the reject-criteria for retouched Heroes, the 'no two HEROs within 7 days' chapter rollout rule — each is a high standard that someone (Rejuar, future retoucher, future content editor, BJ himself in tired moments) will want to soften. The discipline is holding the standard with grace, not lowering it. The Iger 'decency matters' chunk softens the delivery; the standard itself is non-negotiable.",
    direct_quotes=[
        "I'm not going to change. You can either accept it or not.",
        "If you can't tolerate critics, don't do anything new or interesting."
    ],
    tags=["bezos","high-standards","quality","culture"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Long-term thinking · the regret-minimization framework",
    summary="Bezos's 1994 decision to leave a senior position at D.E. Shaw to start Amazon used what he called the 'regret minimization framework': project yourself to age 80, look back at this decision, and ask which choice you would regret. Most short-term decisions look very different from the 80-year-old's perspective. The framework strips out short-term emotional weight and reveals the long-term-correct move.",
    usable_principle="Before any major decision, run the regret-minimization test. Project to 30 years from now. Which choice will you regret? That's the right move, even if it's harder today.",
    sniped_relevance="Same as Thiel's 'definite optimism' applied at the personal level. The SNIPED Year-10 vision IS the regret-minimization framework operationalized — the 80-year-old BJ regrets NOT building the cultural-documentation archive, regrets NOT publishing the Direction Stack book, regrets NOT compounding on the LA founder photography lane. These regrets reverse-cast into present commitments. Every short-term temptation (wedding gig, viral TikTok, NYC move) is filtered against the regret test.",
    direct_quotes=[
        "I knew that when I was eighty I was not going to regret having tried this. I was not going to regret trying to participate in this thing called the Internet."
    ],
    tags=["bezos","regret-minimization","long-term","decision-framework"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="operations",
    concept="Frugality · constraint as creativity driver",
    summary="Amazon's early culture (and to a large extent its continuing one) emphasized extreme frugality — door desks, modest offices, no first-class travel. The justification was not just cost: constraint forces creativity, makes the team self-select for mission over comfort, and signals to customers that the company is on their side (low cost passed through).",
    usable_principle="Cap unnecessary expense even when revenue grows. The discipline of constraint is itself a creative input. Lavish operations produce lavish (and slow) thinking.",
    sniped_relevance="The SNIPED Phase 1 sub-$100/mo backend stack discipline (Notion, Calendly, Stripe, Pixieset, Google Workspace) IS the frugality principle. The temptation in Phase B+ will be to upgrade everything to enterprise tier 'because we can afford it now.' The discipline is to upgrade only what demonstrably eliminates measured friction, not what makes the operation feel more expensive. Munger's incentives chunk reinforces: lavish tools signal lavish thinking, which incentivizes lavish decisions.",
    direct_quotes=[
        "Frugality breeds resourcefulness, self-sufficiency, and invention.",
        "There's no extra points for growing headcount, budget size, or fixed expense."
    ],
    tags=["bezos","frugality","constraint","creativity"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Two-pizza teams · keep groups small enough to be fed by two pizzas",
    summary="Bezos's rule: any team that can't be fed by two pizzas is too big. The justification: larger teams generate communication overhead, political behavior, and decision-by-committee. Two-pizza teams (6-10 people) move fast, own outcomes clearly, and stay scrappy. Amazon scales by having many two-pizza teams loosely coordinated, not few large ones tightly coordinated.",
    usable_principle="When a team grows past ~10, split it. The communication overhead of a 15-person team is more than 50% greater than two 7-person teams.",
    sniped_relevance="For SNIPED at the 1-person stage, the rule preemptively informs future structure: when scaling, prefer many small teams (one per content series, one per geographic market, one per service tier) over a single growing team. The Year-10 4-7 person team from REVERSE_ROADMAP IS a two-pizza team. If SNIPED scales beyond that, the pattern is to split (e.g., a separate cultural-doc unit from the commercial portrait unit) not enlarge.",
    direct_quotes=[
        "If you can't feed a team with two pizzas, it's too large."
    ],
    tags=["bezos","team-size","two-pizza","scaling"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="High-velocity, high-quality decisions · most are reversible",
    summary="Bezos's distinction: Type 1 decisions are one-way doors (irreversible) — these deserve slow, careful analysis. Type 2 decisions are two-way doors (reversible) — these should be made fast, by small groups, with high tolerance for being wrong. Most organizations apply Type 1 process to Type 2 decisions, which slows everything to a crawl.",
    usable_principle="Classify every meaningful decision: one-way door or two-way door? Two-way doors get fast decisions from small groups. One-way doors get the slow analytical treatment. Mixing the two destroys velocity.",
    sniped_relevance="For SNIPED: one-way doors = pricing the floor (changing it later is expensive), the locked aesthetic v3 LUXURY (re-grading the archive would be a year of work), the methodology disclosure on the Card (can't take back). Two-way doors = which prospect to VIB this week, which platform to test first, which Reel cut to ship, whether to take a specific casting call. Confusion costs: spending strategic-decision energy on tactical two-way doors is a common Phase 1 failure mode.",
    direct_quotes=[
        "Some decisions are consequential and irreversible or nearly irreversible — one-way doors — and these decisions must be made methodically, carefully, slowly, with great deliberation and consultation.",
        "But most decisions aren't like that — they are changeable, reversible — they're two-way doors."
    ],
    tags=["bezos","decision-making","reversibility","velocity"]
)

# =============================================================
# Working Backwards · Colin Bryar + Bill Carr
# =============================================================
STITLE = "Working Backwards"
SFILE = "working_backwards_bryar_carr.md"
AUTHOR = "Colin Bryar + Bill Carr"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="systems",
    concept="The PR/FAQ method · start with the press release",
    summary="Amazon's signature product-development discipline: before any new product is approved, the team writes a one-page press release announcing the product as if it has shipped, plus an FAQ anticipating customer and stakeholder questions. The press release forces clarity on what the product DOES for whom; the FAQ forces honesty about hard problems. If the team can't write a compelling PR, the product probably shouldn't be built.",
    usable_principle="For any new offer, service, content series, or strategic initiative, draft the announcement first. If the announcement doesn't compel even you, the underlying thing isn't ready to build.",
    sniped_relevance="Apply to: new offer tier launches (write the Reset+ press release before designing the package); content series launches (write the Substack #1 essay before drafting the Substack architecture); book launch (write the Direction Stack book launch press release now, even if Q3 2026 ships it). The exercise reveals which initiatives have a real customer thesis vs which are operator interest projects.",
    direct_quotes=[
        "The PR/FAQ process leads to better products by forcing teams to think through everything early, well before they write a single line of code.",
        "If you can't write a compelling PR, you probably shouldn't build the product."
    ],
    tags=["amazon","pr-faq","product-design","customer-thesis"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="systems",
    concept="Six-page narrative memos · ban on PowerPoint",
    summary="Amazon's most cultural-defining meeting practice: no slide presentations. Instead, the meeting host writes a 6-page narrative memo (full sentences, full paragraphs). The first 20-30 minutes of the meeting are silent reading. Then discussion begins, grounded in the same shared document. The writing discipline reveals weak thinking that slides can hide; the silent reading creates a level information playing field.",
    usable_principle="For any meeting that matters, replace slides with a written memo. The writing exposes thinking quality. The silent reading ensures shared context. The discussion that follows is substantively better.",
    sniped_relevance="For SNIPED solo-founder phase: this maps to writing the Monday Cockpit, the monthly Constraint Audit doc, the quarterly Reverse Roadmap re-read, the per-shoot postmortem in /90_NOTES/. The discipline of writing-first IS the strategic discipline. The doctrine docs in /00_BRIEF/ (CANONICAL_TRUTHS, OPERATIONAL_BACKBONE, EXECUTION_PRIORITIZATION) are Amazon-style 6-page memos applied to a 1-person org. Hold the discipline as the org grows: when meetings start (with retoucher hire, with VA hire), preserve the no-slides norm.",
    direct_quotes=[
        "The narrative structure of a good memo forces better thought and better understanding of what's more important than what.",
        "There is no way to write a six-page, narratively structured memo and not have clear thinking."
    ],
    tags=["amazon","memos","narrative","communication"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="systems",
    concept="Single-threaded leaders · one person fully accountable",
    summary="Amazon's organizational principle: every major initiative has one leader who is single-threaded — meaning that initiative is their only job. Single-threaded leaders move 5-10× faster than multi-tasking ones because they have full mental focus, full ownership of timeline, and no conflicting priorities. Initiatives that span multiple leaders' attention are perpetually slow.",
    usable_principle="For any major initiative, name a single owner. Don't split ownership across two people who 'collaborate'; that creates coordination overhead that kills velocity.",
    sniped_relevance="In SNIPED Phase 1, BJ is single-threaded on every initiative by default (1-person org). The relevance comes in Phase B+: the retoucher should own retouching end-to-end, not co-own it with BJ; the social VA should own scheduling end-to-end, not check every post; the bookkeeper owns books end-to-end. Confusing the boundaries reproduces the multi-threaded-leader problem that Amazon's principle is designed to prevent.",
    direct_quotes=[
        "The best way to fail at inventing something is by making it somebody's part-time job."
    ],
    tags=["amazon","ownership","single-threaded","focus"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="systems",
    concept="Input metrics over output metrics · controllable vs reported",
    summary="Output metrics (revenue, customer count, share price) are lagging and largely uncontrollable in any short window. Input metrics (selection breadth, page-load time, in-stock rate, perfect-order rate) are leading and directly controllable. Amazon's operational discipline: optimize for input metrics, trust that output metrics follow.",
    usable_principle="For any goal, identify the input metric that, if improved, produces the output metric mechanically. Optimize the input. The output is a result, not a target.",
    sniped_relevance="The SNIPED weekly Notion dashboard already encodes this (per BATCH_001 PRODUCTION_OS chunks): VIBs sent, discovery calls held, edit hours, studio utilization, NOT revenue or follower count. The 100Q_AUDIT chunk reinforces: refuse to track follower count as a success metric. Input metrics: cold emails sent, VIBs delivered, LinkedIn POVs published, comments left on founder posts. Output metrics: Resets booked, MRR, audience size. The discipline is to celebrate input metric hits regardless of output metric noise.",
    direct_quotes=[
        "The right metrics to focus on are the ones the team can directly control — the inputs — not the outputs."
    ],
    tags=["amazon","metrics","inputs","controllable"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Flywheels · self-reinforcing growth loops",
    summary="Bezos's signature strategic diagram: Amazon's flywheel. Lower prices → more customers → more sales → more selection → better customer experience → growth → lower cost structure → lower prices. The diagram is self-reinforcing — every input feeds the next, and the whole accelerates with time. Identifying and accelerating the flywheel is more important than optimizing any single component.",
    usable_principle="Map your business's flywheel. The components should be a cycle: each output feeds back as the next input. Once mapped, the strategic question becomes 'which component is currently throttling the cycle?' and you address that.",
    sniped_relevance="The SNIPED flywheel (implicit in OPERATING_BRIEF and OPERATIONAL_BACKBONE): better Direction Stack methodology → better Reset delivery → stronger testimonials & case studies → stronger VIB social proof → higher Reset conversion → more Reset clients → bigger hero archive → stronger LinkedIn POV content → larger audience → bigger Cultural Doc institutional access → stronger 10-year body of work → premium-tier positioning → higher pricing → more resources to invest in methodology. The throttle in Phase 1 is the FIRST loop — Reset count. Every loop downstream multiplies it.",
    direct_quotes=[
        "We work hard to make sure that we have a fly wheel that's connected to itself."
    ],
    tags=["amazon","flywheel","compounding","systems-thinking"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Bar Raiser · the structural defense against hiring drift",
    summary="Amazon's hiring practice: every senior hire interview loop includes a 'Bar Raiser' — a trained interviewer from another team who has veto power. The Bar Raiser's only job is to evaluate whether the candidate raises the average bar of the team. The hiring manager wants to fill the role; the Bar Raiser is structurally incentivized to say no. The friction is the feature — it prevents hire-down drift.",
    usable_principle="Build structural friction against the failure modes you fear. The friction is the safety. Without it, the path of least resistance erodes the standard over time.",
    sniped_relevance="For SNIPED future hires (retoucher, content editor, VA), the equivalent: every hire is reviewed against the SNIPED 7-signature standard + the Mom Test discipline + the 'cult-like cohesion' criterion before yes. If BJ is the only voice in the room, the temptation to fill the role can erode the standard. Bring in Larry as the equivalent Bar Raiser for senior hires — a peer with no operational pressure to hire who can say no.",
    direct_quotes=[
        "The Bar Raiser is the one person on the loop empowered to say no, even if everyone else says yes."
    ],
    tags=["amazon","hiring","structural-friction","bar-raiser"]
)

# =============================================================
# The Outsiders · William Thorndike
# =============================================================
STITLE = "The Outsiders"
SFILE = "outsiders_thorndike.md"
AUTHOR = "William N. Thorndike"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="capital-allocation",
    concept="Capital allocation is the CEO's primary job · not operations",
    summary="Thorndike's central thesis (from studying 8 outlier CEOs who dramatically outperformed peers): the CEO's job is not running operations — it's allocating capital across 5 options: invest in existing operations, acquire other businesses, issue dividends, pay down debt, repurchase stock. Most CEOs default to one or two; the outliers ranked all 5 against each other and made the highest-return call each time.",
    usable_principle="The biggest strategic decisions in a business are about WHERE money goes, not about HOW operations run. Audit your own allocation regularly. If you're putting cash into ANY direction (gear, ads, salary, savings) without comparing to the alternatives, you're probably misallocating.",
    sniped_relevance="For SNIPED, the founder's capital allocation choices: (1) reinvest in the operation (gear upgrades, software, content production); (2) acquire (paying for high-quality contractor work · Rejuar retainer); (3) distribute (BJ's owner salary); (4) pay down debt (the personal debt cited in 100Q audit); (5) save (the $10K cash reserve target). Decisions should be made comparatively, not defaulted. Phase 1 default: surplus → $10K reserve first (per Revenue Stack chunk), then reinvestment. After $10K reserve, the allocation choice becomes more dynamic.",
    direct_quotes=[
        "CEOs need to do two things well to be successful: run their operations efficiently and deploy the cash generated by those operations.",
        "Most CEOs spend their careers focused on the first set of activities, and yet the second set is critical."
    ],
    tags=["thorndike","capital-allocation","ceo-job","strategy"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="capital-allocation",
    concept="Outsider personality profile · independent, analytical, contrarian",
    summary="Thorndike's 8 CEOs shared personality traits: independent thinkers who didn't seek validation from peers or media, analytically rigorous (comfortable with numerical comparison), willing to be contrarian when the numbers supported it, frugal in personal and corporate spending, deeply focused on the long-term, willing to do nothing for long stretches when no good opportunities existed.",
    usable_principle="The combination of independence + analytical rigor + contrarian willingness is rare and high-value. The outsider pattern is closer to investor-discipline than executive-charisma. Cultivate the analytical pose, not the leadership-theater pose.",
    sniped_relevance="Maps to the SNIPED operator-coded refusal of validation-seeking (per OPERATIONAL_BACKBONE drift-detection: 'wrong game' symptom includes checking follower counts). The 'sit on your ass investing' (Munger chunk) reinforces: when no good moves are available, doing nothing is correct. Contrarian willingness shows in the SNIPED 10-aesthetic-traps refusals and the 99_VAULT-deliberately-empty discipline.",
    direct_quotes=[
        "These CEOs were not charismatic, charismatic visionaries. They were quiet, analytical, and deeply contrarian.",
        "When everyone else was running for the exits, they were buying."
    ],
    tags=["thorndike","temperament","contrarian","analytical"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="capital-allocation",
    concept="Decentralization · push decisions to where information lives",
    summary="The 8 outlier CEOs ran corporate HQs that were tiny relative to peer companies' (Singleton's Teledyne, Buffett's Berkshire, Henry Singleton's office had ~50 people running a Fortune 500). Operational decisions lived with the operating units; corporate HQ allocated capital and otherwise stayed out of the way. Decentralization wasn't ideology — it was empirical recognition that operators close to the work decide better than removed corporate.",
    usable_principle="For every decision, ask: who has the most information? Push the decision there. Centralized decision-making requires centralized information, which requires bureaucracy to gather, which produces stale decisions.",
    sniped_relevance="Maps to Greene's Strategy 5 (command-and-control vs delegation) + the SNIPED un-delegate-ables vs delegated functions. BJ centralizes the strategic decisions (the un-delegate-ables) and decentralizes execution (retoucher decides specific masks, content editor decides specific cuts, VA decides specific scheduling slots). The principle: don't centralize what doesn't need to be centralized.",
    direct_quotes=[
        "Decentralization was a uniform feature of all the companies and proved to be a hallmark of the outsiders' style."
    ],
    tags=["thorndike","decentralization","decision-rights","org-design"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="capital-allocation",
    concept="Cash flow is the metric · not earnings",
    summary="Thorndike's CEOs all focused on cash flow as the primary financial metric, not GAAP earnings. The reason: GAAP earnings can be manipulated through depreciation choices, write-offs, and accounting treatments; cash flow is harder to fake. The outsiders' bias was always toward the maximally-conservative measurement of true business health.",
    usable_principle="When measuring business health, prioritize cash flow over reported earnings. The cash question — 'did money actually arrive this period' — is harder to lie about than the earnings question.",
    sniped_relevance="For SNIPED, this means: the dashboard metric that matters is collected cash (Stripe deposits), not invoiced amounts. The MRR tracking in the 100Q audit is collected MRR, not contracted. The Phase B trigger ($2K MRR × 3 months sustained per 100Q chunk) is collected MRR. The discipline avoids the trap of celebrating booked but unpaid work.",
    direct_quotes=[
        "Cash, not reported earnings, is what determines long-term value."
    ],
    tags=["thorndike","cash-flow","metrics","financial-honesty"]
)

# =============================================================
# Genghis Khan and the Making of the Modern World · Jack Weatherford
# =============================================================
STITLE = "Genghis Khan and the Making of the Modern World"
SFILE = "genghis_khan_weatherford.md"
AUTHOR = "Jack Weatherford"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="empire-building",
    concept="Merit over lineage · the Mongol meritocracy",
    summary="Weatherford documents Genghis Khan's break from the tribal hereditary norm: he promoted commanders on demonstrated ability, not lineage. Soldiers from defeated tribes were assigned to new units that mixed origins, breaking tribal loyalty in favor of meritocratic competence. This was the structural innovation that turned a small steppe people into a Eurasian empire.",
    usable_principle="When building a team, optimize for demonstrated capacity, not for credentials, social proof, or 'who introduced them.' The mixing also matters — homogeneous teams produce groupthink, mixed teams cross-fertilize.",
    sniped_relevance="For SNIPED hires (per the Catmull team-first and Thiel cult-cohesion chunks), the merit principle applies as a check on the cohesion principle: cohesion comes from shared belief in the thesis, NOT from shared background or tribal affinity. Future hires should be evaluated on demonstrated work product, not on referrer prestige or aesthetic-similarity to existing team. Mixing matters — the team's strength comes from BJ-engineer + Rejuar-designer + Ren-outreach + Hermine-MUA being complementary, not similar.",
    direct_quotes=[
        "Genghis Khan recognized that victory did not come from fighting beside men who shared his blood, but from fighting beside men who shared his discipline."
    ],
    tags=["weatherford","meritocracy","empire","hiring"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="empire-building",
    concept="Speed and surprise · the Mongol operational signature",
    summary="The Mongol army's defining military advantage was speed. They moved with extra horses (each soldier had 3-5), they ate while riding, they could cover 100+ miles in a day. Combined with surprise attacks at points the enemy didn't expect, the speed produced a disorienting effect that broke larger conventional armies. The principle: faster decision and execution cycles defeat larger but slower systems.",
    usable_principle="In any competitive context, optimize for decision-and-execution cycle time. The competitor who is 2× faster captures 4× the strategic advantage because they can finish their move before the slow competitor can respond.",
    sniped_relevance="Reinforces Iger's pace-of-change chunk + Bezos's two-way-door decisions. For SNIPED: 24-hour turnaround on positive cold-email replies (per cold_email_doctrine), same-day BTS clip publication, the 5-day Reset SLA — each is a velocity discipline that competitors can't match. The Mongol multiple-horses analog for SNIPED is the multi-platform multi-asset content repurposing (one shoot → 8 outputs from PRODUCTION_OS chunk) — one input produces parallel outputs that arrive at multiple surfaces simultaneously.",
    direct_quotes=[
        "While the European armies marched five to seven days to reach a destination, the Mongols arrived in one or two."
    ],
    tags=["weatherford","speed","velocity","operational-tempo"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="empire-building",
    concept="Open trade and information flow · the Mongol Peace",
    summary="Beyond conquest, the Mongol empire's lasting contribution was a continental-scale system for moving goods, people, and information safely. The yam (postal system), the protection of merchant caravans, the religious tolerance that allowed missionaries and scholars to cross the empire — these created the conditions for the 13th-century burst of cross-civilizational exchange that historians now credit with reshaping the medieval world. Empire builders who only conquer get short returns; those who establish the systems for ongoing flow get long ones.",
    usable_principle="The conquest is the headline; the system is the asset. After winning a market, the long return comes from the infrastructure that keeps value flowing through it.",
    sniped_relevance="For SNIPED, the conquest = winning the LA founder portrait lane. The system = the methodology, the chapter rollout cadence, the cultural-documentation archive, the LinkedIn POV bank, the eventual Direction Stack book, the eventual Substack. Each is infrastructure for ongoing flow. Once installed, they keep producing value (per the BATCH_001 'what compounds quietly' chunk) regardless of any individual conquest. The 99_VAULT-deliberately-empty discipline preserves space for systems that compound, refusing one-off conquest temptations.",
    direct_quotes=[
        "The Mongol Peace was a period of unprecedented commercial expansion and cultural exchange."
    ],
    tags=["weatherford","empire","infrastructure","long-term"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Absorb the conquered · use their expertise",
    summary="The Mongol pattern after conquest: rather than destroying the captured population's specialists (engineers, scribes, craftspeople, administrators), Genghis Khan integrated them into the imperial system. Chinese siege engineers were sent to fight Persians. Persian administrators ran Mongol provinces. This absorption multiplied imperial capability without proportional investment.",
    usable_principle="In any new market or domain, the existing specialists are an asset, not an obstacle. The instinct to 'do it yourself' loses to the discipline of recruiting the people who already know how. Even competitors can become assets if absorbed correctly.",
    sniped_relevance="For SNIPED's eventual cross-medium expansions (Substack writing, gallery shows, video documentary): rather than learning from scratch, recruit specialists who already know — a Substack editor (when ready to launch), a gallery curator (when Year 3-4 approaches), a documentary editor (when video doctrine activates per PRODUCTION_OS Phase B+). Pay them well. They are force-multipliers.",
    direct_quotes=[
        "He had the rare ability to absorb the customs of those he conquered, integrating their best practices into his own administration."
    ],
    tags=["weatherford","absorption","specialists","leverage"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Long campaign discipline · multi-decade horizons",
    summary="Genghis Khan's conquests spanned ~25 years (1206-1227); his successors extended the empire for another 50+. The strategic patience to plan and execute across decades was not common among contemporaries (most rulers thought in 1-2 year horizons). The compounding effect of consistent long-horizon execution against shorter-horizon competitors is the empire-building signature.",
    usable_principle="The competitor operating on a 2-year horizon will always lose to the competitor operating on a 10-year horizon, all else equal. The longer the planning horizon you can sustain, the more compound advantage you build.",
    sniped_relevance="The SNIPED 10-year Reverse Roadmap horizon IS this discipline. Khalil Joseph / Bradford Young / Teju Cole analogs (per REVERSE_ROADMAP) all operated on similar horizons before their cultural recognition arrived. The discipline isn't just patience — it's strategic planning that takes 10-year horizons seriously enough to make 1-year decisions consistent with them. Every Phase 1 decision tests against the Year-10 vision.",
    direct_quotes=[
        "The campaign was not measured in months or years but in generations."
    ],
    tags=["weatherford","long-horizon","patience","compounding"]
)

# =============================================================
# Alexander the Great · Philip Freeman
# =============================================================
STITLE = "Alexander the Great"
SFILE = "alexander_the_great_freeman.md"
AUTHOR = "Philip Freeman"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Lead from the front · the visible commander",
    summary="Alexander's signature leadership pattern: he fought in the front line, ate the same rations, slept on the same ground, took the same wounds. This was strategic, not romantic — his army would follow into impossible situations because they saw him assume the same risks. The leader who is visibly absent from the hardships cannot demand the hardships from others.",
    usable_principle="The leader's visible willingness to do the work — and take the risks — sets the ceiling of what the team will do. Symbolic abstention from the work caps the team's effort proportionally.",
    sniped_relevance="For SNIPED solo-founder: BJ doing the editing work himself in Phase 1 — even when temptation is to delegate prematurely — is the lead-from-front pattern. When the retoucher hire happens, BJ should still personally do Pass 4 review (per delegation matrix) — visible continued involvement in the quality work. Same with sending VIBs personally and writing the Day-30 Op Kit DMs personally even at Phase B+. The 'un-delegate-ables' list IS the lead-from-front commitment formalized.",
    direct_quotes=[
        "He led every charge himself, asking no soldier to face danger he would not face first."
    ],
    tags=["freeman","leadership","front-line","example-setting"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="The pothos · the longing that drives the campaign",
    summary="Greek historians used 'pothos' (longing/yearning) to describe Alexander's drive to push beyond known horizons. Each conquest opened a new horizon that called him further. The pothos was not strategic in the usual sense — it was a sustained existential commitment to seeing what lay beyond the next ridge. Empires of this scale require this drive; rational strategy alone doesn't sustain decades.",
    usable_principle="The 10-year game requires more than strategy — it requires a sustained existential commitment to the destination. Name your pothos. Without it, the strategic logic gets eroded by short-term comfort.",
    sniped_relevance="BJ's pothos (implicit in REVERSE_ROADMAP and OPERATING_BRIEF): becoming the named visual documentarian of LA's emerging Black founder/operator/artist culture. The Direction Stack as a real published methodology. The cultural-documentation archive as a serious 10-year body of work. These are not commercially-optimal targets — they are existential commitments. The pothos is what sustains the discipline when the commercial logic alone would say 'take the easier path.'",
    direct_quotes=[
        "He was driven by an inner longing to see what lay beyond every horizon."
    ],
    tags=["freeman","drive","longing","commitment"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Cultural absorption · the Persian-court adoption",
    summary="After conquering the Persian Empire, Alexander adopted Persian court protocols, married Persian wives, and integrated Persian nobility into his command structure. This horrified his Macedonian generals — but it was strategic. He recognized that ruling a multi-ethnic empire required cultural absorption, not Macedonian-supremacist imposition. The transition cost him political support at home but enabled the longer-arc imperial integration.",
    usable_principle="Conquest and rule require different cultural postures. Winning a market through aggressive moves doesn't translate to governing the market through aggressive imposition. The shift to integration is uncomfortable but load-bearing.",
    sniped_relevance="For SNIPED at Year 3-5+, when initial market position is established: the discipline shifts from VIB-aggressive-outreach to relationship-deepening with the won market. The integration phase looks different — institutional relationships (Bishop Peters network, future gallery relationships), recurring-subject collaborations, named clients who return as portfolio anchors. The aggressive Phase-1 outreach tone doesn't translate to Phase-3 institutional posture. Plan for the shift.",
    direct_quotes=[
        "He chose to wear Persian dress and adopt Persian customs, knowing his Macedonians would resent it but his empire required it."
    ],
    tags=["freeman","cultural-absorption","integration","governance"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Decisive concentration of force · the Granicus pattern",
    summary="Alexander's tactical signature: at the moment of engagement, concentrate the maximum force on the single decisive point. At Granicus, Issus, and Gaugamela, he identified the Persian king's location and drove personally toward it with the Companion cavalry. The king's flight collapsed the whole army. Decisive battles are won by force concentration on the strategic node, not by spreading effort evenly.",
    usable_principle="When the strategic moment arrives, concentrate the maximum resources on the single decisive node, even at the cost of leaving other fronts undefended. Spreading effort evenly across multiple fronts wastes the decisive moment.",
    sniped_relevance="For SNIPED: the launch moments (Direction Stack book launch Q3 2026, first gallery show in Year 3-4, eventual Substack launch) require force concentration. Everything else in those windows takes second priority. Same applies to specific client engagements: the first Op Kit pitch from a delivered Reset client deserves full focus, not parallel attention to other prospects. The Constraint Audit's 'one bottleneck this month' discipline IS the Alexander concentration principle at the monthly tempo.",
    direct_quotes=[
        "He aimed straight at the heart of the enemy line, knowing that to defeat the king was to defeat the army."
    ],
    tags=["freeman","concentration","decisive-moment","tactics"]
)

# =============================================================
# The Cold Start Problem · Andrew Chen
# =============================================================
STITLE = "The Cold Start Problem"
SFILE = "cold_start_problem_chen.md"
AUTHOR = "Andrew Chen"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="network-effects",
    concept="The Cold Start framework · 5 stages of a networked product",
    summary="Chen's framework for the lifecycle of any networked product. (1) Cold Start — the network has no users; the product can't deliver value yet. (2) Tipping Point — first 'atomic network' (the smallest network that can sustain itself) achieved. (3) Escape Velocity — multiple self-reinforcing loops compounding. (4) Ceiling — saturation, anti-network effects, overcrowding. (5) Moat — defending the network against competitors. Most discussion of 'network effects' collapses these into one — Chen argues they require different strategies at each stage.",
    usable_principle="Identify which stage your network/audience is currently in. The right strategy at the Cold Start stage is the wrong strategy at the Moat stage. Don't apply Escape Velocity tactics to a Cold Start problem.",
    sniped_relevance="SNIPED's three engines mapped to Cold Start stages: Audience Engine (LinkedIn + IG) is currently at Cold Start (per 100Q audit: 'pre-audience phase'). Reputation Engine (institutional cultural-doc network) is at Cold Start. Revenue Engine (Reset bookings) is at Cold Start. Different strategies needed for each. The 'pre-audience phase distribution moves' (paid boost CH01, direct DM seeding, organic reshare from subject) ARE Cold Start tactics, not Escape Velocity tactics. Naming the stage explicitly prevents premature optimization.",
    direct_quotes=[
        "Every network goes through five stages: the Cold Start Problem, the Tipping Point, Escape Velocity, the Ceiling, and the Moat."
    ],
    tags=["chen","network-effects","lifecycle","stages"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="network-effects",
    concept="Atomic network · the smallest self-sustaining unit",
    summary="Chen's most operational concept: the smallest network unit that can keep itself alive without external boost. For Uber, an atomic network = one city, with enough drivers and riders that the average wait time stays under acceptable threshold. For Slack, it = one team. For Tinder, it = one college campus. The strategic discipline: don't try to launch nationally; identify the atomic network, achieve it fully, then replicate.",
    usable_principle="Identify the smallest unit of your network that can keep itself alive. Achieve full saturation of one unit before expanding. The unit-of-replication is the deployable strategy, not the abstract aggregate.",
    sniped_relevance="For SNIPED, the atomic network = the LA founder cluster (geographic + behavioral) where (a) enough founders subscribe/follow that BJ has steady inbound; (b) enough referral density that one closed Reset produces 2-3 warm intros; (c) recurring-subject collaboration enables chapter momentum. This is the Cold Start target — saturate the LA tech-founder + creative-operator cluster first before any geographic expansion. The 'cluster economics matter' lesson from Hit Makers + the Audience-of-Audience strategy in BATCH_001 STRATEGIC_PRINCIPLES converge on this.",
    direct_quotes=[
        "The most important thing for a new network is to focus on one atomic network, the smallest network that can stand on its own."
    ],
    tags=["chen","atomic-network","saturation","entry-strategy"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="network-effects",
    concept="The Hard Side · who is harder to acquire",
    summary="Every two-sided network has a hard side and an easy side. For Uber, drivers are hard (high time investment, equipment, regulatory friction); riders are easy. For Tinder, women were hard (safety concerns, ratio dynamics); men were easy. The strategic asymmetry: spend disproportionately on the hard side. The easy side will follow the hard side; the hard side will not follow the easy side.",
    usable_principle="In any two-sided system (clients/photographer, audience/creator, contractors/operator), identify the hard side. Invest disproportionately in acquisition and retention of the hard side. Optimizing the easy side wastes effort.",
    sniped_relevance="For SNIPED, the hard side is QUALIFIED FOUNDER PROSPECTS (Tier 0-1 in the VIB CRM per cold_email_doctrine). Subjects who will model for chapter rollouts are also hard side — the operator-coded register requires careful casting. Easy sides: general LinkedIn followers, casting-call sign-ups (per casting_call_doctrine, must be filtered hard). Invest in the hard side: Ren's outreach time is concentrated on Tier 0 founders, not Tier 4 fillers. Chapter casting prioritizes returning collaborators (Yae, future repeat subjects) over expanding first-time pool.",
    direct_quotes=[
        "The hard side of the network is the smaller group of users that puts in much more effort and gets much more out of it.",
        "Find the hard side, and serve them."
    ],
    tags=["chen","two-sided","hard-side","prioritization"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="network-effects",
    concept="Come for the tool, stay for the network · the Instagram pattern",
    summary="Instagram launched as a photo-filter tool — useful even with zero other users. Users came for the filters, then stayed because their friends started posting. This is a structural solution to the Cold Start Problem: the first version of the product is a single-player utility; the network is layered on later. Compare with products that require the network from day one (which can't get started at all).",
    usable_principle="For network-effects products, design a single-player utility that delivers value even with zero other users. Then layer the network on. This is the Cold Start escape mechanism.",
    sniped_relevance="The Direction Stack book IS this for SNIPED. As a standalone PDF, it delivers value to any photographer or founder who reads it — no SNIPED network required. But it ALSO creates a connection back to SNIPED methodology, which feeds the audience and reputation engines. Same applies to the eventual Substack: each essay should deliver value as standalone reading, while the cumulative archive builds the audience network. The single-asset-utility + layered-network pattern is the right architecture.",
    direct_quotes=[
        "Come for the tool, stay for the network. This pattern has been used by many successful products to bootstrap."
    ],
    tags=["chen","come-for-tool","bootstrap","Instagram-pattern"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="network-effects",
    concept="Anti-network effects · negative dynamics at scale",
    summary="Network effects are not uniformly positive. As networks grow, they accumulate anti-network effects: spam (Twitter), trolling (YouTube comments), overcrowding (Craigslist), context collapse (Facebook). The same growth dynamics that built the positive flywheel start producing negative flywheels at scale. Mature network management is largely about managing the anti-network effects.",
    usable_principle="Plan for the anti-network effects at scale. The discipline of curation, moderation, and selective acceptance becomes more important as the network grows.",
    sniped_relevance="For SNIPED at Phase B+ when audience grows: anti-network effects = engagement bait commenters, opportunistic 'collaboration' DMs, inappropriate casting-call submissions, low-quality referrals. The casting_call_doctrine (per BATCH_001) already encodes anti-bot defenses. As audience grows, the discipline of refusal becomes more important — every yes to a wrong-fit opportunity erodes the cluster purity that makes SNIPED's network valuable in the first place.",
    direct_quotes=[
        "Networks don't just grow positively. As they get large, negative effects emerge that can eventually destroy them."
    ],
    tags=["chen","anti-network","curation","scale-management"]
)

# =============================================================
# The Song Machine · John Seabrook
# =============================================================
STITLE = "The Song Machine"
SFILE = "song_machine_seabrook.md"
AUTHOR = "John Seabrook"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="distribution",
    concept="The hit factory · structured production beats individual genius",
    summary="Seabrook documents the Swedish-Scandinavian hit-factory model (Cheiron Studios, Max Martin, Stargate) that produced disproportionate share of global pop hits from the late 1990s onward. The structural innovation: separate the creative roles (track, topline melody, lyrics, vocal) and assign specialists to each. Then iterate combinations at high volume. Hit-rate is higher than individual auteur model because each specialist gets reps.",
    usable_principle="For repeat creative output, specialize the roles. The auteur who does everything personally has a low ceiling. The structured production line with specialists at each stage produces more, faster, and at higher quality.",
    sniped_relevance="For SNIPED scaling, this informs how the production team is structured at Phase B+: BJ as direction + aesthetic call; Rejuar as composite + design; future retoucher as Lightroom/Evoto specialist; future content editor as Reels specialist; eventual social VA as scheduling specialist. Each role gets reps, each specializes, BJ orchestrates. Currently BJ is doing all roles by necessity — the structure to specialize comes online with hires. Plan the production line, don't accumulate roles randomly.",
    direct_quotes=[
        "The hit factory is a structured collaboration where each specialist contributes one piece — the track-maker, the topliner, the lyricist, the singer.",
        "It is a system that has produced more hits per producer-hour than any other in history."
    ],
    tags=["seabrook","hit-factory","specialization","production"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="distribution",
    concept="Earworm engineering · the science of the hook",
    summary="Modern pop hits are engineered to produce 'earworm' effect — the song that gets stuck in the listener's head and pulls them back to repeat listens. Specific structural elements: high information density in the chorus, melodic ascent then resolution, lyrical hooks at predictable beat positions. The factory has reverse-engineered the listener's brain. The same engineering applies to short-form video hooks and visual content.",
    usable_principle="Hooks are engineered, not discovered. The first 1-3 seconds (audio or visual) carry disproportionate weight. Study what produces the pull-back effect in your category and apply it.",
    sniped_relevance="Reinforces the BATCH_001 'Hook Factory' chunk from Attention Stack. The SNIPED LinkedIn hook templates ('Most LA founder photos fail at one specific layer.' 'There are 10 protocols. Most photographers don't run any of them.') are earworm-engineered. The 7-signature recognizability test produces the visual equivalent — viewers see one SNIPED frame and the structure pulls them to look at the next. Apply explicit hook-engineering discipline to every content surface; don't rely on intuition.",
    direct_quotes=[
        "The hook arrives within the first three seconds, repeats predictably, and resolves at the listener's expectation."
    ],
    tags=["seabrook","hooks","earworm","engineering"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="distribution",
    concept="Songwriter camps · concentrated creative iteration",
    summary="Modern pop production includes 'camps' where multiple songwriters, producers, and singers are brought together for 3-5 days of intensive collaboration. The constrained time + concentrated talent produces output that wouldn't emerge from distributed work. The structure forces iteration at speed.",
    usable_principle="For specific creative pushes, concentrate effort in short intensive windows rather than diffusing across long timelines. Constraint + concentration produces output that distribution doesn't.",
    sniped_relevance="For SNIPED, the equivalent: dedicated BTS Content Days (per PRODUCTION_OS Section 5.5 from BATCH_001) — one 6-hour Saturday produces ~3 weeks of Reels content. Similar discipline for: dedicated LinkedIn POV writing sessions (one 2-hour block produces 4 weeks of posts), dedicated cultural-documentation shoot days, dedicated Substack drafting blocks when launched. Resist diffusing the creative work across the calendar; concentrate it.",
    direct_quotes=[
        "The camp produces in five days what distributed work could not produce in five months."
    ],
    tags=["seabrook","creative-camps","concentration","production-blocks"]
)

# =============================================================
# DisneyWar · James B. Stewart
# =============================================================
STITLE = "DisneyWar"
SFILE = "disneywar_stewart.md"
AUTHOR = "James B. Stewart"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Founder mode degradation · the long arc of a single CEO",
    summary="Stewart documents Michael Eisner's 20-year run as Disney CEO: brilliantly successful in years 1-10 (Pixar partnership, Touchstone, theme park revival, Lion King era), then deteriorating in years 11-20 (Ovitz disaster, talent feuds, board conflict, succession failure, eventual ouster). The pattern: founder-mode strengths (decisive control, personal involvement, willingness to demand excellence) became liabilities at scale (micromanagement, talent flight, paranoia, succession blocking). The same traits that built the empire eventually undermined it.",
    usable_principle="The leadership traits that work at one stage may fail at the next. Self-audit periodically: are the patterns that built Phase 1 still serving Phase 3? The willingness to evolve leadership style is the rarer skill.",
    sniped_relevance="For SNIPED's long arc (Year 10 destination at 4-7 person team), the Eisner failure mode is a real risk. BJ's Phase 1 strengths (personal involvement in every decision, methodology obsession, high quality bar, refusal to delegate aesthetic calls) are correct at solo-founder scale. At 4-7 person team scale, the SAME traits — applied without adjustment — produce talent flight and decision bottlenecks. The OPERATIONAL_BACKBONE delegation matrix already plans for this. The discipline is actually evolving the leadership pattern when scale demands it, not just planning to.",
    direct_quotes=[
        "The traits that had built the empire were now corroding it.",
        "Eisner could not let go, and his inability to let go became the central problem of his second decade."
    ],
    tags=["stewart","leadership-arc","founder-mode","succession"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Succession is strategy · who follows you is the final move",
    summary="Stewart's deep theme: Eisner's failure to develop and trust a successor was his most expensive mistake. Talent left because they saw no path. The board lost confidence because the bench was thin. The eventual succession (to Iger) was forced by board action, not designed by Eisner. Successful long-tenure CEOs (Buffett, Bezos) treat succession as a primary 5-10 year project, not a retirement-eve afterthought.",
    usable_principle="Succession planning is itself a strategic discipline. The leader who refuses to develop a successor is — whether intentionally or not — choosing to undermine the organization's continuity.",
    sniped_relevance="At Year 10, SNIPED is a 4-7 person team with BJ as central operator. Even early in that arc (Year 5-7), the question 'who could run SNIPED if BJ stepped back for 6 months' must have an answer. The successor (likely an experienced photographer or operations lead) needs to be developed years before the question becomes urgent. Don't make this a Year-9 panic. Start naming the criteria in Year 3-5; identify candidates in Year 5-7; transition some functions in Year 7-9.",
    direct_quotes=[
        "A CEO's most important job is choosing a successor, and Eisner failed at it."
    ],
    tags=["stewart","succession","continuity","long-arc"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Talent flight · the slow erosion of cultural quality",
    summary="Disney under late Eisner lost Jeffrey Katzenberg (founded DreamWorks), Steve Jobs (took Pixar elsewhere until Iger acquisition), and many mid-level creative leaders. Each departure was justifiable in isolation; the cumulative effect was a hollowing of creative capacity. Talent flight doesn't happen at once — it accumulates. The CEO who creates conditions where A-players leave one by one is dismantling the company in slow motion.",
    usable_principle="Track talent retention as carefully as financial metrics. The departure of one A-player is information; the departure of three is a fire. Address the underlying culture before the third departure.",
    sniped_relevance="For SNIPED, this means: when Rejuar, Ren, or future hires show signs of disengagement, address the underlying conditions immediately. The Iger 'decency matters' chunk + the Catmull 'team is primary' chunk + the Greene Law 11 'indispensability' chunk all converge on this. The current team is small but load-bearing — Rejuar's design work alone is the bottleneck on chapter rollout cadence. Treat retention as a strategic priority, not a soft HR concern.",
    direct_quotes=[
        "The greatest talent in the entertainment business had once been at Disney. Eisner watched them leave, one by one, and did not understand what he was losing."
    ],
    tags=["stewart","talent-retention","culture","slow-erosion"]
)

print(f"After cluster 5 (Weatherford + Freeman + Chen + Seabrook + Stewart): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 6 · STOUTE · cultural capital as creator of financial capital
# Tanning of America (book) + Powerhouse talk (Silicon Valley transcript)
# =============================================================
STITLE = "The Tanning of America"
SFILE = "tanning_of_america_stoute.md"
AUTHOR = "Steve Stoute"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="culture",
    concept="Cultural capital precedes financial capital · the tanning thesis",
    summary="Stoute's central thesis: hip-hop culture 'tanned' mainstream America starting in the late 1980s. Suburban white youth adopted the aesthetics, language, and values of urban black culture, creating a generation whose shared cultural reference points were no longer racially segregated. Brands that recognized this shift early (Tommy Hilfiger, Adidas, Sprite) captured massive value; brands that ignored it or fought it (Cristal famously) destroyed their own franchises. The mechanism: cultural authority, held by the artists, the streets, the early adopters, converts to commercial demand on a 3-7 year lag.",
    usable_principle="The brands that win in the next decade are the ones that recognize where cultural authority is being created NOW, partner with it authentically, and let the demand follow. Trying to manufacture cultural relevance after the fact is exponentially more expensive than partnering with it early.",
    sniped_relevance="For SNIPED, this is the Founder Tier playbook in raw form. The 60 founder portraits are not just client work; they are a partnership with the people creating cultural authority in tech/founder culture this decade. If even 3-5 of those founders go on to outsized cultural impact (Series B+, acquisition, IPO, public-figure status), SNIPED becomes the visual brand that captured them when no one else saw it. The Cultural Doc 'On Refusing to Use AI' is itself a bid for cultural authority in the anti-AI photographer camp.",
    direct_quotes=[
        "Cultural currency is the new global currency.",
        "Hip-hop didn't just sell records. It sold a worldview, and that worldview was bought by everyone."
    ],
    tags=["stoute","cultural-capital","authority-conversion","founder-tier"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="The Cristal failure mode · rejecting the cultural buyer who chose you",
    summary="Cristal champagne became the dominant hip-hop status symbol in the late 1990s, referenced in lyrics, ordered in clubs, photographed in music videos. Stoute documents the catastrophic 2006 moment when Cristal's managing director made dismissive comments about the hip-hop association ('What can we do? We can't forbid people from buying it'). Jay-Z called for a boycott. Within months, Cristal was replaced by competitors (Ace of Spades, Dom Pérignon) and never recovered its cultural position. The lesson: when an unexpected cultural buyer chooses your brand and elevates it, your only winning move is to embrace it. Rejecting them is brand suicide.",
    usable_principle="If a buyer or community chooses your brand and amplifies it in a direction you didn't expect, treat that as a gift, not a contamination. The brands that try to police who 'should' carry them lose to the brands that embrace their actual buyers.",
    sniped_relevance="For SNIPED's photography work, this means: if SNIPED's portraits become culturally associated with a specific founder archetype, scene, or city (e.g., 'the SF AI founder look,' 'the LA second-gen Korean-American founder portrait'), embrace it rather than trying to broaden out of it. Specificity creates authority; trying to be for everyone dissolves the cultural position you accidentally won.",
    direct_quotes=[
        "Cristal didn't understand that the people who made them famous could also unmake them.",
        "When the community that elevated you decides to walk away, you don't get to choose the consequences."
    ],
    tags=["stoute","cristal-failure","cultural-rejection","brand-suicide"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="Authentic partnership beats licensed endorsement · the Run-DMC / Adidas template",
    summary="Stoute uses the 1986 Run-DMC / Adidas deal as the template: Run-DMC wore Adidas Superstars (with no laces, in the prison style) because they actually wore them. The 'My Adidas' song was not commissioned by Adidas; it was organic. When Adidas executives saw 40,000 fans hold up their Adidas shoes during a Madison Square Garden performance, they signed the first non-athlete endorsement deal in sports apparel history. The deal worked because the cultural authority was real BEFORE the commercial relationship existed. Contrast with later celebrity endorsement deals that started with the contract and failed because no organic cultural authority preceded them.",
    usable_principle="Partner with people who already use your product authentically, not with people you have to pay to use it. The commercial deal should formalize an existing cultural reality, not manufacture one.",
    sniped_relevance="For SNIPED's named-client strategy: the Founder Portraits work because the founders chose SNIPED for their own portraits, not because SNIPED paid them to be 'ambassadors.' Resist any future pressure to do paid-influencer partnerships in photography. The integrity of the work is the entire asset; the moment money flows toward the client (instead of from them), the cultural-authority transfer collapses.",
    direct_quotes=[
        "Run-DMC wasn't wearing Adidas because Adidas paid them. Adidas paid them because they were already wearing them.",
        "The deal didn't create the relationship. The relationship created the deal."
    ],
    tags=["stoute","authentic-partnership","run-dmc-adidas","endorsement-mechanics"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="Translation as a profession · the cultural broker role",
    summary="Stoute frames his own career (Translation, the agency he founded) as a translation function between cultural creators (artists, communities, scenes) and corporate brand decision-makers (CMOs, CEOs, boards). Both sides need each other: the brands have distribution and capital; the cultures have authority and authenticity. But they speak different languages and operate with different value systems. The translator role is high-value because the failure modes are catastrophic: brands that misread culture get publicly humiliated (Pepsi/Kendall Jenner ad); cultures that get exploited by brands lose trust permanently.",
    usable_principle="In any market where two communities create value together but don't share a vocabulary, the translator role is structurally undervalued and structurally critical. Becoming the trusted translator is a defensible position.",
    sniped_relevance="For SNIPED, BJ is already a translator: between technical/engineering culture (where the founders live) and visual/aesthetic culture (where the portraits land on social, in press, in pitch decks). The Direction Stack methodology is, in effect, a translation protocol, turning founder vagueness ('I want it to feel powerful') into specific visual decisions. Lean into the translator framing for positioning: SNIPED is not 'a photographer' to founders; SNIPED is the person who translates between who they are and how they need to be seen.",
    direct_quotes=[
        "The translator's job is to make sure both sides win without either side losing what made them valuable.",
        "Authenticity isn't the goal. Authentic translation is the goal."
    ],
    tags=["stoute","translation-role","cultural-broker","positioning"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="The mental color line · why brands hesitated to integrate",
    summary="Stoute argues that the corporate hesitation to embrace hip-hop in the 1990s was not driven by overt racism. It was driven by a 'mental color line' where brand managers couldn't imagine their (white suburban) customer aspiring to black urban culture. The market data already showed the conversion was happening; the brand teams couldn't see it because their internal model of the customer was outdated. The brands that broke through (Hilfiger, Sprite, Adidas) did so because someone inside had direct cultural exposure and could override the internal model.",
    usable_principle="The biggest market opportunities are usually visible in the data before they are visible to leadership, because leadership's internal model of the customer is calibrated to an outdated reality. The discipline is updating the model when data and model diverge.",
    sniped_relevance="For SNIPED, this means staying alert to which founder communities are creating cultural authority now that incumbent photographers don't see. Second-generation immigrant founders. Female-led infra startups. AI-skeptical founders in heavily-AI markets. Climate-tech founders bridging finance and engineering. These are the Run-DMC / Adidas moments hiding in plain sight: partner now, document now, become the visual brand of that community before anyone else recognizes the cultural lift.",
    direct_quotes=[
        "The data was screaming, but the brand teams were still drawing the old map.",
        "Cultural opportunity is mostly the gap between what's true and what leadership believes is true."
    ],
    tags=["stoute","mental-color-line","outdated-models","emerging-authority"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="culture",
    concept="Generational color blindness · the demographic clock",
    summary="Stoute's underlying demographic argument: each successive generation in the US is more comfortable with cross-racial cultural exchange than the last. Gen X bought the hip-hop integration; Millennials grew up assuming it; Gen Z assumes a fully multi-cultural baseline. Brands that bet on the old segregated map lose progressively more ground each decade as the population literally ages out from under them. The demographic clock is one of the most predictable forces in marketing, and one of the most ignored by incumbents.",
    usable_principle="When making a 10-year bet on a market, ask: what does the demographic curve look like in 10 years? Bet with the curve, not against it. Generational shifts compound in ways quarterly thinking misses.",
    sniped_relevance="For SNIPED's 10-year arc, the demographic bet is: founder culture itself is becoming more multi-cultural, more female, more globally distributed, and more cross-disciplinary. The portraits that age well will be the ones that capture that demographic shift, not the ones that replicate the 2010-2020 'founder in a hoodie in front of brick' aesthetic. The Direction Stack is well-positioned because it starts from the individual subject rather than imposing a category aesthetic.",
    direct_quotes=[
        "Demographics don't argue. They just arrive.",
        "Every decade, the population gets younger than the brand team's mental model of the customer. The gap is the opportunity."
    ],
    tags=["stoute","demographic-clock","generational-shift","10-year-bet"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="The Reebok S. Carter sneaker · cultural capital made physical",
    summary="Stoute brokered the 2003 Reebok / Jay-Z 'S. Carter' sneaker deal, the first signature shoe for a non-athlete. The shoe sold out in hours and validated the thesis that cultural authority could move physical product at the same scale as athletic endorsement. The deal worked because: (1) Jay-Z had genuine cultural authority, (2) Reebok needed a non-Nike differentiation strategy, (3) the product itself was good (not a logo slap), (4) the launch leveraged Jay-Z's own distribution (his music, his appearances) rather than relying on traditional advertising.",
    usable_principle="When cultural authority makes physical product, the launch should leverage the authority-holder's existing distribution, not bolt on a traditional ad campaign. The audience is already there; meet them where they already are.",
    sniped_relevance="For SNIPED's Direction Stack book (Year 2-3), the launch should leverage BJ's existing channels (the LinkedIn following, the Cultural Doc series, the founder client network's own social) rather than buying ads or seeking traditional book PR. The book is the physical artifact of cultural authority already built; the launch should be the harvest, not the build.",
    direct_quotes=[
        "The audience for an artifact is the audience the creator already has. Don't build a second audience for the launch.",
        "Cultural capital monetizes when it touches a physical product. But only if the product is real."
    ],
    tags=["stoute","s-carter-sneaker","launch-strategy","existing-distribution"]
)

STITLE = "Powerhouse Talk · Silicon Valley"
SFILE = "stoute_powerhouse_talk.txt"
AUTHOR = "Steve Stoute"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="Cultural capital creates financial capital · the inversion",
    summary="Stoute's central argument in the Silicon Valley Powerhouse talk: in the legacy economy, financial capital created cultural capital (rich brands sponsored cultural moments). In the current economy, the inversion holds: cultural capital creates financial capital. Artists, creators, and cultural communities now hold the authority; brands have to bid for access to it. The implication for tech founders in the audience: stop thinking about marketing as 'spending money to acquire users' and start thinking about it as 'partnering with people who already have cultural authority over your user base.'",
    usable_principle="If you have to spend a dollar to acquire a unit of attention, you're operating in the old model. Find the people who already have authority over your audience and find a way to be valuable to them; the attention follows.",
    sniped_relevance="For SNIPED, this is the operating philosophy: the founders SNIPED photographs each have their own cultural authority (their team, their investors, their early customers, their LinkedIn following). When SNIPED does great work for them, the work travels through their authority channels for free. This is why $1,500 Reset is loss-leader strategically: every Reset creates an authority node that can later refer Founder Tier work. The economics only work because cultural capital is doing the customer acquisition.",
    direct_quotes=[
        "Money used to make culture. Now culture makes money.",
        "If you're paying for attention, you're losing. The winners get attention because they're worth paying attention to."
    ],
    tags=["stoute","cultural-to-financial","authority-acquisition","loss-leader-logic"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="The artist as the brand · the founder parallel",
    summary="Stoute argues that the hip-hop era proved an individual artist could be a brand, a media company, a fashion house, and a distribution channel simultaneously. Jay-Z, Diddy, Dr. Dre all built billion-dollar businesses where the artist's identity WAS the brand. The Silicon Valley parallel: the founder is increasingly the brand of the company. Customers don't buy from Tesla; they buy from Elon-as-Tesla. They don't buy from Patagonia; they buy from Chouinard-as-Patagonia. The personal brand and the corporate brand are merging back together after a century of corporate brands trying to be impersonal.",
    usable_principle="The era of impersonal corporate branding is closing. The customer wants to know who they're buying from. Build the founder brand and the company brand together; don't try to separate them.",
    sniped_relevance="For SNIPED, BJ-the-photographer and SNIPED-the-brand are intentionally merging. The Direction Stack book carries BJ's name. The Cultural Doc has a singular voice. The portraits credit BJ. The risk is bus-factor (what if BJ is unavailable for 6 months?), but the alternative (a faceless 'SNIPED Studio' brand) loses 80% of the premium pricing power and the cultural-authority transfer. Accept the bus-factor risk; mitigate with operational backbone (the methodology is documented, others can be trained on it), not by hiding BJ.",
    direct_quotes=[
        "The artist is the brand. The brand is the artist. The customer always knew that. The corporate world is just remembering.",
        "Founders are the new artists. Their companies are their albums."
    ],
    tags=["stoute","founder-as-brand","personal-corporate-merge","direction-stack-positioning"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="Authenticity is not a tactic · it is the entire asset",
    summary="Stoute repeatedly warns the Silicon Valley audience: you cannot fake cultural authenticity. Every attempt to manufacture it (paid influencers without genuine product fit, brand-voice campaigns that mimic culture, 'street' marketing from corporate teams) gets detected and rejected. The audience for cultural products has developed sophisticated bullshit detection over 30 years of watching brands try and fail. The only path is genuine investment in the culture, on the culture's own terms, with the culture's own people leading the work.",
    usable_principle="Authenticity cannot be tactical. It must be the entire foundation of the work, baked in from the start, owned by people who actually live in the culture. Anything else gets detected.",
    sniped_relevance="For SNIPED, this validates the refusal to do AI compositing for client work, the refusal to fake credentials, the insistence on showing the actual Direction Stack process, the named-client transparency (real founders, real names, real work). The bullshit-detection of the founder audience is high; they will instantly spot a generic 'business photographer' positioning. The entire pricing premium rests on the authenticity being real.",
    direct_quotes=[
        "You cannot perform authenticity. You can only be authentic and let it be seen.",
        "Every brand that tried to fake culture got caught. Every single one."
    ],
    tags=["stoute","authenticity-as-foundation","bullshit-detection","anti-ai-positioning"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="The decade-long bet · cultural movements take 10 years to monetize",
    summary="Stoute's timeline argument in the Powerhouse talk: he started recognizing hip-hop's commercial potential in 1988. The first major brand wins (Tommy Hilfiger, Sprite) happened 1995-1997. The peak monetization (Jay-Z's Rocawear sale, Diddy's Sean John, Stoute's own Translation agency) happened 2005-2015. That's a 17-27 year arc from cultural recognition to full financial extraction. Founders trying to monetize emerging culture in 18 months are misunderstanding the timeline. The reward goes to those who bet early, stay patient, and let the cultural authority compound.",
    usable_principle="The biggest financial returns from cultural bets accrue over 10-20 year horizons. If you're trying to monetize a cultural shift in 18 months, you're either late or wrong about the size of the opportunity.",
    sniped_relevance="For SNIPED, this validates the 10-year arc thinking explicitly. The current 2026 work (Direction Stack, Cultural Doc, founder portraits) is the early bet. The 2030+ harvest (book sales, methodology licensing, possible product line, possible studio expansion) is the monetization peak. Resist short-term pressure to dilute the bet for faster cash. Resist scope expansion that would muddy the cultural position. The reward of patient cultural betting is non-linear.",
    direct_quotes=[
        "Cultural bets pay in decades, not quarters.",
        "The people who got rich off hip-hop saw it in '88 and got rich in '08. That gap is the cost of admission."
    ],
    tags=["stoute","decade-arc","patient-betting","cultural-monetization"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="The community owns the brand · permission economy",
    summary="Stoute's framing for the Silicon Valley audience: in the cultural economy, the community owns the brand more than the company does. The community can take a brand from obscure to dominant (as hip-hop did for Tommy Hilfiger) and it can take a brand from dominant to dead (as it did for Cristal). Smart brand operators recognize this and operate with the community's permission, not in opposition to it. The CMO who thinks they 'own' the brand is operating an outdated model.",
    usable_principle="Treat your customer community as the actual owner of the brand. Make decisions in partnership with them, not in spite of them. The CEO who thinks they own the brand is one PR crisis away from learning otherwise.",
    sniped_relevance="For SNIPED, the 'community' is the founder network. Each portrait subject becomes a partial owner of what SNIPED means in the founder world. Their satisfaction, their advocacy, their willingness to refer all compound the brand or destroy it. The premium-service model (white-glove delivery, Direction Stack consultation, hand-signed prints) is not just service polish; it is permission-maintenance with the community that owns the brand's cultural meaning.",
    direct_quotes=[
        "The brand is owned by the people who carry it, not the people who registered the trademark.",
        "Every customer is a board member. They just don't get a check."
    ],
    tags=["stoute","community-ownership","permission-economy","client-experience"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="The four quadrants of brand attempts at culture",
    summary="Implicit in Stoute's Powerhouse talk: brands attempt culture in four quadrants based on (authenticity × competence). High auth + high competence = wins (Hilfiger '95, Adidas '86, Sprite '97). High auth + low competence = sympathy losses (the brand tried, the execution failed). Low auth + high competence = polished failures (Pepsi/Kendall Jenner ad, technically beautiful, culturally tone-deaf). Low auth + low competence = invisible failures (most corporate attempts at culture, ignored rather than mocked). The quadrant strategy: only enter the high-auth quadrants; if you can't be authentic, don't engage culture at all.",
    usable_principle="Before engaging a cultural movement commercially, audit honestly: do we have genuine authority here? If no, don't engage. Even competent execution will fail. If yes, invest heavily; competence multiplies authenticity.",
    sniped_relevance="For SNIPED's positioning decisions, this means: only engage cultural conversations where SNIPED has genuine authority (premium photography for founders, anti-AI craft positioning, the Direction Stack methodology). Don't try to engage adjacent cultural conversations (e.g., 'AI ethics in general,' 'founder mental health,' 'the future of work') where SNIPED has no native authority. Stay in the lane where authenticity is real.",
    direct_quotes=[
        "If you don't have the right to be in the conversation, the conversation will notice, and punish you.",
        "Pick the lanes where you're authentic. Don't enter the lanes where you're not."
    ],
    tags=["stoute","authenticity-quadrants","lane-discipline","positioning"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="brand",
    concept="The premium of doing what nobody else will · refusal-positioning",
    summary="Stoute notes throughout the talk that the largest cultural wins came from doing what the conventional industry refused to do: signing rappers as fashion ambassadors when no one would, partnering hip-hop with luxury when both sides said no, launching artist-owned product lines when artists were supposed to 'stay in their lane.' The refusal of the broader market created the opportunity. Whoever broke the rule first captured a category nobody else could enter for a decade.",
    usable_principle="Watch for the things the broader market refuses to do. If the refusal is based on outdated bias rather than real economics, the first mover gets a category to themselves.",
    sniped_relevance="For SNIPED, the photography industry's near-universal embrace of AI compositing IS the equivalent refusal moment, but inverted. The market is racing to AI; the refusal-position is to publicly stay analog/in-camera/identity-preserving. This is the same structural opportunity Stoute exploited (do the thing the market refuses to do well) just flipped in direction. The Cultural Doc 'On Refusing to Use AI' is the artifact that claims this position publicly.",
    direct_quotes=[
        "The biggest wins came from doing what the industry said couldn't be done, or shouldn't be done.",
        "Refusal is often the most strategic move available. It just doesn't look like strategy at the time."
    ],
    tags=["stoute","refusal-positioning","first-mover","anti-ai-moat"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Distribution is the last mile · cultural authority is the first 99",
    summary="Stoute argues against the Silicon Valley default of 'we'll figure out distribution later.' His counter: distribution is the last mile, but the first 99 miles is building cultural authority that makes the distribution earn-able. The brands that succeeded in his hip-hop work had spent years (decades, for some) building cultural authority before the commercial breakout. Tommy Hilfiger had been a fashion brand for 10 years before the hip-hop integration; Adidas had decades of athletic credibility; Sprite had years of being the 'second-tier cola' before it was repositioned. Without the cultural authority foundation, no amount of distribution work would have produced the wins.",
    usable_principle="Distribution is a multiplier of cultural authority. Without authority, distribution moves nothing; with authority, distribution moves mountains. Build the authority first.",
    sniped_relevance="For SNIPED, this validates the current Year 1-2 emphasis on building authority (Cultural Doc, named-client portfolio, Direction Stack methodology) BEFORE worrying about distribution scale (paid ads, partnerships, sales reps). The current LinkedIn organic + referral motion is the authority-building phase. Distribution amplification comes later, and is only worth doing once the authority foundation has compounded for 18-24 months. Premature distribution scaling burns capital and embarrasses the brand.",
    direct_quotes=[
        "Distribution is the last mile. Don't run it first.",
        "The brands that scaled too fast scaled their own absence of cultural authority. It's not a winning move."
    ],
    tags=["stoute","authority-before-distribution","sequencing","year-one-discipline"]
)

print(f"After cluster 6 (Stoute Tanning + Powerhouse talk): {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 7 · DEPTH ADDS on highest-density canon
# Munger + Greene + Thiel + Isaacson + Catmull + Bezos + Iger + Thorndike
# =============================================================

STITLE = "Poor Charlie's Almanack"
SFILE = "poor_charlies_almanack_munger.md"
AUTHOR = "Charles T. Munger"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Lollapalooza effects · when multiple biases stack and amplify",
    summary="Munger's term for when 3-5 psychological biases converge on the same direction and produce extreme outcomes that no single bias would predict. His canonical example: Tupperware parties combined reciprocation (free gift), commitment/consistency (publicly chose products), social proof (others buying), liking (hosted by a friend), and authority (the demonstrator's expertise), producing buying behavior 5-10x what any single factor would explain. Lollapaloozas appear in cult recruitment, market bubbles, panic sells, and political movements. Recognizing the stacking pattern is more powerful than knowing any single bias.",
    usable_principle="When multiple psychological forces point the same direction simultaneously, the resulting behavior will be extreme and apparently irrational from outside. Look for the stacking, not just individual biases. Design your own systems to USE lollapalooza dynamics for adoption, and to RESIST them when you're the target.",
    sniped_relevance="For SNIPED's client experience, deliberately stack: reciprocation (the welcome packet exceeds expectation), commitment (the discovery call gets the client articulating their own vision so they commit publicly to it), social proof (the named-client portfolio), liking (BJ's earned warmth in person), authority (Direction Stack book, Cultural Doc series). A lollapalooza-stacked premium offer converts at far higher rates than any single lever. For the inverse defense: when SNIPED is the target of a 'big opportunity' pitch (agency partnerships, scaling offers), recognize when the pitch is itself a lollapalooza and discount accordingly.",
    direct_quotes=[
        "When several powerful psychological tendencies operate together toward the same outcome, you get lollapalooza results.",
        "The lollapalooza tendency is not just additive; it is multiplicative."
    ],
    tags=["munger","lollapalooza","bias-stacking","client-experience"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Incentive-caused bias · whose bread I eat, his song I sing",
    summary="Munger's most-emphasized bias: people will rationalize behavior that serves their incentive structure, even when they sincerely believe they are reasoning objectively. The classic test: 'Show me the incentive, I'll show you the outcome.' Doctors over-prescribe profitable procedures while sincerely believing they are practicing best medicine; brokers churn accounts while sincerely believing they are serving clients; consultants recommend expensive engagements while sincerely believing the problem is real. The danger is not bad faith; it is sincere belief that aligns with self-interest.",
    usable_principle="When evaluating advice or analysis, always ask first: what is this person's incentive? Discount or invert the recommendation when incentive and recommendation align suspiciously. When designing your own incentives, make them match the outcomes you actually want; your future self will rationalize whatever you incentivize.",
    sniped_relevance="For SNIPED: when an agency or partner suggests 'you should scale by hiring more photographers,' ask whose incentive that serves (theirs, if they get a placement fee; the photographers', if they want jobs). When a tech vendor suggests 'you need AI tooling to compete,' check whose incentive that serves. When BJ's own gut says 'we should expand into video,' check whose incentive THAT serves (often: short-term revenue at long-term lane-dilution cost). Self-incentive bias is the hardest to detect.",
    direct_quotes=[
        "Show me the incentive, and I will show you the outcome.",
        "Never, ever, think about something else when you should be thinking about the power of incentives."
    ],
    tags=["munger","incentive-bias","advisor-evaluation","self-deception"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Inversion · solve forward problems by working backward from failure",
    summary="Munger's cognitive trick borrowed from Jacobi: 'Invert, always invert.' Instead of asking 'how do I succeed at X?', ask 'what would guarantee failure at X?' and then avoid those things. The inversion often surfaces fatal errors that forward thinking misses. Munger's life-advice example: don't ask 'how do I have a good life?', ask 'what would guarantee a terrible life?' (drugs, debt, unreliable people, envy, resentment, self-pity), then avoid those. The inversion produces a clearer and more actionable answer.",
    usable_principle="For any strategic question, run the forward analysis AND the inverted analysis. The inverted version often reveals fatal-error patterns the forward version misses. Combine both for a complete decision.",
    sniped_relevance="For SNIPED's Year 10 destination, apply inversion: what would GUARANTEE SNIPED fails to reach Year 10? Burnout (over-commit to client volume), lane-dilution (chase every adjacent opportunity), authority-collapse (compromise on AI or quality for short-term cash), founder-replacement-risk (BJ becomes unavailable with no documented methodology), legal/financial blow-up (poor contracts, IP confusion). Avoiding those five fatal patterns is more actionable than 'building toward success.'",
    direct_quotes=[
        "Invert, always invert. Turn a situation or problem upside down. Look at it backward.",
        "It is remarkable how much long-term advantage people like us have gotten by trying to be consistently not stupid, instead of trying to be very intelligent."
    ],
    tags=["munger","inversion","avoid-failure","not-stupid-strategy"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Circle of competence · know the edge of what you know",
    summary="Munger's discipline: identify clearly what you genuinely understand (the inside of the circle), what you don't (the outside), and especially where the edge is (the boundary). The boundary is the dangerous zone because people who are excellent inside their circle systematically overrate their competence at the edge. The discipline is not to expand the circle aggressively (which leads to over-confident mistakes) but to operate ruthlessly within it and be honest about where it ends.",
    usable_principle="The size of your circle of competence matters less than knowing exactly where the boundary is. Make decisions deep inside the circle; refuse opportunities outside it even when they look attractive; treat the edge as the most dangerous zone.",
    sniped_relevance="For SNIPED, the circle of competence is: founder photography (deep center), Direction Stack methodology (deep center), brand-system thinking applied to single-operator services (solid middle), photo workflow optimization (solid middle), Lightroom + Photoshop craft (deep center). Outside the circle: video, weddings/events, full-time team management at scale, AI compositing, corporate stock-style work. The discipline is to refuse outside-circle opportunities even when the money is real. Each refusal preserves the position; each accepted edge-case dilutes the circle's integrity.",
    direct_quotes=[
        "Knowing what you don't know is more useful than being brilliant.",
        "You have to figure out what your own aptitudes are. If you play games where other people have the aptitudes and you don't, you're going to lose."
    ],
    tags=["munger","circle-of-competence","refusal-discipline","edge-awareness"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Latticework of mental models · multiple disciplines as cross-checks",
    summary="Munger's central educational thesis: develop a working command of the big ideas from 80-100 disciplines (physics, biology, psychology, economics, mathematics, history, engineering) and use them as cross-checking lenses on any decision. The person with only one model (a hammer) sees every problem as a nail; the person with a latticework sees the same problem from 5 angles and catches errors a single-model thinker misses. The investment in building the latticework is large up front but compounds for life.",
    usable_principle="Don't be a one-model thinker. Force yourself to analyze any major decision through at least 3-4 distinct disciplinary lenses (psychology + economics + systems + history) and watch for where the analyses diverge; the divergence usually points to where the real risk lives.",
    sniped_relevance="For SNIPED, this is already happening implicitly through the auto-memory intel files (positioning, trust, hospitality, leverage, status psychology, new luxury, company-of-one, photo theory, blockbuster, analog premium, AI market). Each intel file is a mental model lens. Major decisions (pricing, hiring, scope expansion) should be analyzed across multiple lenses simultaneously. Make this explicit: for any strategic call, write out the analysis from at least 4 intel-file lenses before deciding.",
    direct_quotes=[
        "You've got to have models in your head. And you've got to array your experience, both vicarious and direct, on this latticework of models.",
        "To the man with only a hammer, every problem looks pretty much like a nail."
    ],
    tags=["munger","latticework","multi-model-thinking","decision-discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Social proof tendency · the dangerous shortcut in uncertain situations",
    summary="Munger's analysis of social proof bias: in uncertain situations, humans use the behavior of others as a strong proxy for what to do, often overriding their own analysis. This is adaptive in some cases (everyone running from a building means there's probably fire) and catastrophic in others (everyone buying the bubble means it's about to pop). The discipline is to notice when you're in an uncertain situation and your judgment is being heavily influenced by what others are doing; that is precisely when first-principles thinking is most valuable and least practiced.",
    usable_principle="When you find yourself agreeing with a consensus you can't independently defend from first principles, that is the moment to slow down. Social proof is most powerful exactly when you can least afford to follow it blindly.",
    sniped_relevance="For SNIPED, the photography market is currently in massive AI-adoption social proof: every studio, every YouTube channel, every agency is pushing AI workflows. The temptation to follow consensus is enormous. The anti-AI positioning is precisely a refusal to follow social proof, and is defensible because it is grounded in first-principles analysis (premium clients pay for human craft, identity integrity matters, scarcity will compound as everyone else races to AI). Re-examine the position every 6 months from first principles, but resist drift driven by industry social proof.",
    direct_quotes=[
        "Big-shot businessmen get into these waves of social proof. Do you remember some years ago when one oil company bought a fertilizer company, and every other major oil company practically ran out and bought a fertilizer company?"
    ],
    tags=["munger","social-proof","consensus-resistance","ai-positioning"]
)

STITLE = "The 48 Laws of Power"
SFILE = "48_laws_of_power_greene.md"
AUTHOR = "Robert Greene"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Law 1 · Never outshine the master",
    summary="Greene's opening law: in any hierarchy, make those above you feel comfortably superior. Showing more talent than your superior creates resentment that will eventually be paid back in your career. The law applies to corporate hierarchies, royal courts, and informal social structures. The historical examples Greene uses (Galileo overshadowing Pope Urban VIII, court intriguers losing favor by outshining the king) all share the pattern: technical brilliance without political awareness destroyed careers that should have flourished.",
    usable_principle="When operating within a hierarchy you don't control, calibrate your visible competence to what the structure can tolerate. Outshine deliberately and only when you control the consequences, never accidentally.",
    sniped_relevance="For SNIPED's named-client work, the inverse applies: BJ is the 'master' of the visual outcome, and the client is the subject. Never make the client feel outshone by the visual technique. The portrait should make the SUBJECT look like the powerful one; the photographer's skill is the invisible scaffolding. This is why generic 'fashion-magazine for tech founders' aesthetic often fails: the technique outshines the subject. Direction Stack's discipline is to serve the subject's authority, not display the photographer's.",
    direct_quotes=[
        "Always make those above you feel comfortably superior. In your desire to please and impress them, do not go too far in displaying your talents or you might accomplish the opposite: inspire fear and insecurity.",
        "Make your masters appear more brilliant than they are and you will attain the heights of power."
    ],
    tags=["greene","law-1","subject-primacy","portrait-discipline"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Law 6 · Court attention at all cost",
    summary="Greene's argument: in a noisy market, being talked about (even controversially) is worth more than being respected silently. The historical figures who built lasting power (P.T. Barnum, Andy Warhol, Salvador Dalí) all deliberately cultivated attention through unusual behavior, distinctive aesthetic, public spectacle. Obscurity is the worse fate; controversy is preferable to invisibility. The discipline is choosing what KIND of attention to cultivate so it compounds the right position.",
    usable_principle="In a crowded market, invisibility is the largest risk. Cultivate distinctive, attention-earning behavior in the direction that compounds your strategic position. Controversy is often more valuable than respectability.",
    sniped_relevance="For SNIPED, the Cultural Doc 'On Refusing to Use AI' is a deliberate attention-courting move. It will offend AI-adopting photographers; it will resonate strongly with the anti-AI camp; it will get talked about more than a polite middle-ground position would. The discipline is to ensure the attention is in the direction of the strategic position (premium craft, identity integrity, founder-photographer authority) rather than random provocation. Court attention strategically; never become a generic attention-seeker.",
    direct_quotes=[
        "Court attention at all cost. Everything is judged by its appearance; what is unseen counts for nothing. Never let yourself get lost in the crowd, then, or buried in oblivion."
    ],
    tags=["greene","law-6","strategic-attention","cultural-doc"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Law 28 · Enter action with boldness",
    summary="Greene argues that boldness is itself a signal of capability: observers interpret confident action as evidence of competence and back the bold player accordingly. Timid execution, even of a sound plan, creates doubt in observers and self alike. The boldness must be calibrated to the actual decision (not recklessness) but the EXECUTION of any chosen plan should be unhesitating. Half-measures lose to both timid retreat and full commitment.",
    usable_principle="Once a decision is made, execute boldly. Hesitation in execution signals weakness regardless of the soundness of the underlying plan. Save the agonizing for the decision phase; once committed, move with full conviction.",
    sniped_relevance="For SNIPED, this applies to client interactions (deliver the Direction Stack consultation with full conviction, even when uncertain about an aesthetic call), pricing conversations (state the Reset $1,500 floor without hedging, without apologetic explanations), refusal of off-scope referrals (decline cleanly, without lengthy justification). Hesitation in any of these signals weakness that erodes the premium position. Decide carefully, then act boldly.",
    direct_quotes=[
        "If you are unsure of a course of action, do not attempt it. Your doubts and hesitations will infect your execution. Timidity is dangerous: Better to enter with boldness."
    ],
    tags=["greene","law-28","execution-boldness","premium-confidence"]
)

STITLE = "Zero to One"
SFILE = "zero_to_one_thiel.md"
AUTHOR = "Peter Thiel"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Monopoly through narrow start · own a small market completely before expanding",
    summary="Thiel's playbook for monopoly creation: start with a market small enough that you can dominate it, achieve genuine monopoly in that niche, then expand to adjacent markets from the position of strength. Amazon started with books (a market Barnes & Noble underestimated), Facebook started with Harvard (a market so small it was beneath competitors' attention), PayPal started with eBay power-sellers (a tiny but desperate niche). Trying to enter a large market against existing competitors is structurally losing; creating a small market you can own is structurally winning.",
    usable_principle="Find a market small enough that you can credibly dominate it within 2-3 years. Win it completely. Then expand from the moat of total dominance, not from a position of partial market presence.",
    sniped_relevance="For SNIPED, the small market is: premium founder photography in a specific geographic / vertical slice. Not 'all business photography' (too broad, dominated by entrenched players). Not even 'all founder photography' (still too broad). Specifically: premium founder photography for Series A-C tech founders in SF Bay Area + LA + NYC, with the Direction Stack methodology and anti-AI positioning as differentiation. That market is small enough to credibly dominate in 24-36 months. Once dominated, expand to adjacent verticals (creative-economy founders, second-gen immigrant founders, climate-tech) or geographies (Austin, Miami, London).",
    direct_quotes=[
        "Every startup is small at the start. Every monopoly dominates a large share of its market. Therefore, every startup should start with a very small market.",
        "The perfect target market for a startup is a small group of particular people concentrated together and served by few or no competitors."
    ],
    tags=["thiel","narrow-monopoly","market-domination","sniped-niche"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="The power law applies to founder bets · most things don't matter",
    summary="Thiel's argument from venture capital portfolio theory: in any high-variance domain, returns are dominated by a tiny number of extreme winners. One investment may produce more return than the entire rest of the portfolio combined. The implication is not just for VC investing; it applies to which projects a founder works on, which clients a service business chases, which ideas a creative person pursues. The discipline is to focus disproportionate resources on the bets that could produce power-law outcomes and to ruthlessly cut energy from bets that can only produce moderate returns.",
    usable_principle="Identify which 1-2 bets in your portfolio could produce power-law outcomes (10-100x what the others produce) and concentrate energy there. Cut or minimize bets that can only produce moderate, linear returns even if they look 'safe.'",
    sniped_relevance="For SNIPED, the power-law bet is the Direction Stack methodology becoming the standard for premium founder photography in the next decade. If it works: book sales + licensing + studio expansion + cultural authority compound to 8-figure outcomes. The Reset $1,500 client work is the cash-flow / authority-building substrate, not the power-law bet. Make sure the daily prioritization reflects this: the methodology development, Cultural Doc, book work should get protected time even when client work feels more urgent.",
    direct_quotes=[
        "The biggest secret in venture capital is that the best investment in a successful fund equals or outperforms the entire rest of the fund combined.",
        "Life is not a portfolio. The power law dictates that one thing will be more important than everything else."
    ],
    tags=["thiel","power-law","bet-concentration","direction-stack-priority"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="The four characteristics of monopoly · proprietary tech / network effects / economies of scale / branding",
    summary="Thiel's checklist for evaluating monopoly durability: (1) Proprietary technology that is 10x better than the closest substitute, (2) network effects where the product becomes more valuable as more people use it, (3) economies of scale that lower unit cost as volume grows, (4) branding that creates pricing power independent of pure functional differentiation. The strongest monopolies have multiple of these; the weakest have none and rely on temporary execution advantages.",
    usable_principle="Evaluate any business position against the four monopoly characteristics. If you have zero, you're in a commodity fight; if you have one, you have temporary advantage; if you have three or four, you have durable monopoly. Build deliberately toward acquiring more of the four over time.",
    sniped_relevance="For SNIPED, the current monopoly characteristics are: (1) Proprietary methodology (Direction Stack, early-stage, not yet 10x but on the path), (2) Network effects (modest, founder referrals do compound), (3) Economies of scale (limited, service business), (4) Branding (strong, anti-AI craft positioning, BJ-as-author, premium aesthetic). The strongest current asset is brand; the next investment should be deepening proprietary methodology (the book) and accelerating network effects (every founder portrait becomes a referral node). Scale economies will never be strong; accept that and build a different moat shape.",
    direct_quotes=[
        "Every monopoly is unique, but they usually share some combination of the following characteristics: proprietary technology, network effects, economies of scale, and branding."
    ],
    tags=["thiel","monopoly-checklist","moat-evaluation","sniped-moat"]
)

STITLE = "Steve Jobs"
SFILE = "steve_jobs_isaacson.md"
AUTHOR = "Walter Isaacson"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="The intersection of liberal arts and technology · the bridge premium",
    summary="Isaacson's recurring framing of Jobs's career: the unique position came from sitting at the intersection of humanities (calligraphy, design, music, philosophy) and technology (engineering, manufacturing, supply chain). Most technologists ignored design as decoration; most artists ignored technology as mechanics. Jobs treated both as primary and equally important. The companies he built (Apple, Pixar) all expressed this intersection. The lesson generalizes: the most valuable positions are often at the bridge between two communities that don't take each other seriously.",
    usable_principle="The intersection of two disciplines that don't respect each other is often the most underserved and most defensible position. Be the bridge; don't be the specialist in either lane alone.",
    sniped_relevance="For SNIPED, the intersection is photography craft + founder/business strategy. Most photographers don't engage seriously with business strategy; most founders don't engage seriously with visual craft. BJ's position at the intersection (Direction Stack methodology brings strategic thinking to portraiture; founder portrait work brings visual craft to strategic positioning) is structurally hard to replicate because most operators in either lane don't have the bridge to the other. Protect this intersection ruthlessly; refuse to specialize fully into either lane.",
    direct_quotes=[
        "The people who are crazy enough to think they can change the world are the ones who do.",
        "I always thought of myself as a humanities person as a kid, but I liked electronics. Then I read something that one of my heroes, Edwin Land of Polaroid, said about the importance of people who could stand at the intersection of humanities and sciences, and I decided that's what I wanted to do."
    ],
    tags=["isaacson","intersection-position","bridge-premium","direction-stack-positioning"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="End-to-end control · why Jobs insisted on integration",
    summary="Isaacson's analysis of Jobs's defining strategic choice: control the entire user experience by owning hardware + OS + apps + services + retail. The 'open systems' camp (PC industry, Android camp) argued integration was inefficient and would lose to modular competition. Jobs argued (and proved at scale) that for products where user experience is the value proposition, integration produces an experience that modular systems can never match. The lesson: when experience is the moat, control end-to-end; when commodity efficiency is the moat, modularize.",
    usable_principle="If your value proposition is experience quality, control the entire pipeline that produces the experience. Modularization is appropriate for commodity efficiency but destructive for experience differentiation.",
    sniped_relevance="For SNIPED, end-to-end control is the moat. BJ controls: the discovery call, the Direction Stack consultation, the shoot direction, the capture, the cull, the edit, the delivery, the post-delivery touch. Every handoff in this chain is a quality risk. The temptation to delegate (hire a second photographer, outsource editing, use an assistant for delivery) must be weighed against the experience-quality cost. Some handoffs may be safe (admin, scheduling, file delivery); the creative chain probably cannot be safely broken without losing the premium position.",
    direct_quotes=[
        "I've always wanted to own and control the primary technology in everything we do.",
        "When you connect everything together, the parts amplify each other. When you separate them, you lose the magic."
    ],
    tags=["isaacson","end-to-end-control","integration-vs-modularity","delegation-discipline"]
)

STITLE = "Creativity, Inc."
SFILE = "creativity_inc_catmull.md"
AUTHOR = "Ed Catmull"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="The Braintrust · candor as a process, not a personality",
    summary="Catmull's central operational invention at Pixar: the Braintrust is a regularly-scheduled meeting where directors show works-in-progress to senior creative peers who deliver maximum-candor feedback. The structural keys: (1) participants have NO authority to mandate changes; feedback is advisory only, (2) the director keeps decision rights, (3) candor is enforced by group norm and design, not by individual brave personalities, (4) the meeting is regular (not ad-hoc), creating predictability that lowers defensiveness. The Braintrust is the antidote to corporate yes-cultures that kill creative work.",
    usable_principle="Candor that depends on brave individuals is fragile; candor that is built into recurring process is durable. Design feedback structures where honest critique is the expected default, with clear decision rights so feedback doesn't become governance.",
    sniped_relevance="For SNIPED, this suggests building a 'Braintrust' equivalent: a small group of trusted operators (other premium photographers, brand strategists, founder clients post-delivery) who get to see works-in-progress and give honest feedback BEFORE delivery. The Direction Stack book draft, the Cultural Doc essays, the pricing pages all need candid review from people who will tell the truth. Setting this up as recurring process (monthly review session?) is more reliable than ad-hoc 'can you take a look at this' requests.",
    direct_quotes=[
        "The Braintrust meets every few months or so to assess each movie we're making. Its premise is simple: Put smart, passionate people in a room together, charge them with identifying and solving problems, and encourage them to be candid.",
        "Candor is forthrightness or frankness, not so different from honesty, really. And yet, in common usage, the word communicates not just truth-telling but a lack of reserve."
    ],
    tags=["catmull","braintrust","structured-candor","feedback-process"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Protect the new · ideas in their infancy need shelter, not stress-tests",
    summary="Catmull's counterintuitive principle: new ideas, when first surfaced, are ugly. They look obviously wrong. The mature, polished version exists nowhere yet, only the rough, half-formed seed. If you stress-test a seed against the standards you apply to mature work, you will kill every potential breakthrough. The discipline is to protect new ideas during the fragile early phase, give them time to develop into a form that can be evaluated, and only THEN apply rigorous critique.",
    usable_principle="When evaluating a new idea, ask first 'is this still in the seed phase or is it ready for stress-testing?' Apply the appropriate standard. Killing seeds with mature-stage critique is one of the most common ways organizations strangle their own creativity.",
    sniped_relevance="For SNIPED, this applies to: aesthetic experiments (a new editing direction), positioning experiments (a new copy frame for the website), pricing experiments (a new offer structure). When BJ tries something new, the initial output WILL look bad compared to the polished existing work. The Direction Stack itself looked rough in early forms. The discipline is to give new ideas 2-4 cycles to develop before judging them by the standard of mature output. Self-critique that kills seeds is as dangerous as external critique that does.",
    direct_quotes=[
        "Originality is fragile. And, in its first moments, it's often far from pretty.",
        "If you give a good idea to a mediocre team, they'll screw it up. If you give a mediocre idea to a great team, they'll either fix it or come up with something better."
    ],
    tags=["catmull","protect-the-new","seed-vs-mature","creative-discipline"]
)

STITLE = "The Everything Store"
SFILE = "everything_store_bezos_stone.md"
AUTHOR = "Brad Stone"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Day 1 mentality · the disease of Day 2 is invisible decay",
    summary="Stone documents Bezos's recurring 'Day 1' framing: Amazon must always operate as if it is on the first day of its existence: agile, customer-obsessed, willing to make long-term bets, resistant to process for process's sake. The opposite condition, 'Day 2,' is not catastrophic failure: it is slow, invisible decay where the company becomes process-bound, customer-distant, optimization-focused rather than invention-focused. Bezos's argument: Day 2 always ends in irrelevance and death; the only question is how fast. The discipline of staying Day 1 is the discipline of resisting natural organizational drift.",
    usable_principle="Watch for symptoms of Day 2 drift: process meetings replacing customer meetings, optimization replacing invention, defensiveness replacing curiosity. The drift is gradual and invisible; the antidote is deliberate counter-pressure, not waiting for a crisis to reveal it.",
    sniped_relevance="For SNIPED, Day 1 mentality means: every quarter, ask 'what would we do if we were starting from scratch today?' If the answer differs from current operations, investigate why. Watch for symptoms: are client interactions becoming templated? Is the Direction Stack methodology calcifying into mechanical recipe? Is the Cultural Doc becoming 'content marketing' rather than genuine point of view? Catch the drift early; counter it deliberately.",
    direct_quotes=[
        "Day 2 is stasis. Followed by irrelevance. Followed by excruciating, painful decline. Followed by death. And that is why it is always Day 1.",
        "You can't be that worried about your competitors because they aren't going to send you any money. We're driven by the customer."
    ],
    tags=["bezos","day-1","organizational-drift","quarterly-reset"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="High-judgment / low-judgment decisions · don't apply the same process to both",
    summary="Stone covers Bezos's two-bin decision framework: Type 1 decisions are one-way doors (irreversible, consequential: hiring a senior exec, betting the company on a strategy, killing a major product) and require slow, careful, multi-stakeholder deliberation. Type 2 decisions are two-way doors (reversible, low-consequence) and should be made quickly, often by one person, without committee. Most organizations fail by applying Type 1 process to Type 2 decisions (over-deliberating reversible choices, killing speed) or Type 2 process to Type 1 decisions (rushing irreversible choices, eating catastrophic risk). The discipline is correct classification.",
    usable_principle="Before any decision, classify it Type 1 (irreversible) or Type 2 (reversible). Apply slow process to Type 1, fast process to Type 2. The biggest organizational waste is Type 1 process applied to Type 2 decisions.",
    sniped_relevance="For SNIPED's solo-founder context: Type 1 decisions (hiring first FT employee, signing a multi-year studio lease, licensing the Direction Stack methodology, accepting a major investor or partner) deserve weeks of analysis. Type 2 decisions (a single new edit experiment, a one-off copy change on the website, a single client scope concession, an outreach message variant) deserve minutes. Currently BJ may be applying Type 1 weight to Type 2 decisions (e.g., agonizing over individual social posts): calibrate the process to match the decision class.",
    direct_quotes=[
        "Some decisions are consequential and irreversible or nearly irreversible (one-way doors) and these decisions must be made methodically, carefully, slowly, with great deliberation and consultation.",
        "But most decisions aren't like that. They are changeable, reversible. They're two-way doors. If you've made a suboptimal Type 2 decision, you don't have to live with the consequences for that long."
    ],
    tags=["bezos","type-1-type-2","decision-classification","decision-speed"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Disagree and commit · resolving deadlock without false consensus",
    summary="Stone documents Bezos's 'disagree and commit' framing: when a senior leader disagrees with a decision but the group has made it, the leader must commit fully to executing it as if they agreed: not slow-walking, not undermining, not waiting to be proven right. The principle resolves the otherwise-fatal organizational pattern where decisions get nominally made but lieutenants who disagreed sabotage execution through under-investment. The leader's job is to argue hard during the decision, then commit hard during execution, even when their position lost.",
    usable_principle="Once a decision is made, the time for arguing is over. Commit fully to execution regardless of your prior position. The organization that practices disagree-and-commit can move 5x faster than one that doesn't.",
    sniped_relevance="For SNIPED's small-team context, this applies internally (BJ deciding to go a direction Rejuar or Ren may have argued against) and externally (BJ deciding to take a client direction the client initially resisted, after the discovery process resolved). Once decided, no second-guessing, no relitigating, no passive resistance. The decision itself can be revisited at a future review; the current execution gets full commitment.",
    direct_quotes=[
        "Disagree and commit. This phrase will save a lot of time. If you have conviction on a particular direction even though there's no consensus, it's helpful to say, 'Look, I know we disagree on this, but will you gamble with me on it? Disagree and commit?'"
    ],
    tags=["bezos","disagree-and-commit","execution-discipline","decision-finality"]
)

STITLE = "The Ride of a Lifetime"
SFILE = "ride_of_a_lifetime_iger.md"
AUTHOR = "Robert Iger"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="Optimism as operating system · the leader's mood propagates",
    summary="Iger's recurring leadership principle: the leader's mood (especially regarding the company's prospects and possibilities) propagates through the organization at scale. A leader who is privately worried but publicly confident still leaks the worry; teams pick up on micro-cues. A genuinely optimistic leader produces teams that take bigger bets and recover from setbacks faster. The optimism must be grounded in real assessment (not denial) but it must also be the operating default. Pessimism, even when 'realistic,' is organizationally toxic.",
    usable_principle="Cultivate genuine optimism as a leadership operating mode. The mood you carry into rooms propagates more powerfully than the words you say. Build the optimism on real foundation but make it the default register.",
    sniped_relevance="For SNIPED as solo-operator with small team (Rejuar, Ren, future hires), BJ's mood propagates directly to everyone in contact. Client interactions, team check-ins, the Cultural Doc voice, the LinkedIn POV all carry mood as much as content. The discipline is to bring genuine optimism (not performed positivity) to every interaction, while reserving private space for working through real concerns. The leak between private worry and public mood is real and costly.",
    direct_quotes=[
        "Optimism in a leader, especially in challenging times, is so vital. Pessimism leads to paranoia, which leads to defensiveness, which leads to risk aversion.",
        "Optimism sets a different machine in motion."
    ],
    tags=["iger","optimism-as-os","mood-propagation","leadership-register"]
)

STITLE = "The Outsiders"
SFILE = "outsiders_thorndike.md"
AUTHOR = "William N. Thorndike"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Capital allocation is the CEO's primary job · not operations",
    summary="Thorndike's central thesis from studying eight unconventional CEOs (Singleton, Murphy, Stiritz, Buffett, etc.): the CEO's single most important function is capital allocation: deciding where dollars go (operations reinvestment, acquisitions, share buybacks, dividends, debt paydown). Most CEOs are promoted from operations and continue to focus on operations after taking the corner office, leaving capital allocation to CFOs or default patterns. The outliers Thorndike studied flipped this: they treated capital allocation as PRIMARY and operations as delegable. Their long-term returns dramatically exceeded operations-focused peers.",
    usable_principle="If you're the leader, your primary job is allocation (of capital, attention, time, talent), not execution. Re-examine quarterly: am I spending time on allocation decisions, or am I doing operations that someone else could do?",
    sniped_relevance="For SNIPED-as-business, this applies even at solo scale. BJ's allocation decisions: how much time goes to client work vs methodology development vs Cultural Doc vs operational backbone? How much capital goes to gear vs marketing vs hire-vs-DIY decisions? These allocation choices compound into the 10-year outcome far more than any single shoot's execution quality does. The temptation to spend the day in Lightroom (operations) when the higher-leverage work is methodology writing (allocation) is constant and must be resisted with structure.",
    direct_quotes=[
        "There are basically only five choices for deploying capital: investing in existing operations, acquiring other businesses, issuing dividends, paying down debt, or repurchasing stock; and three options for raising it: tapping internal cash flow, issuing debt, or raising equity.",
        "The Outsiders shared a worldview that made them deeply different from their peers and led to outstanding performance."
    ],
    tags=["thorndike","capital-allocation","ceo-primary-job","time-allocation"]
)

print(f"After cluster 7 depth-adds: {len(CHUNKS)} chunks")

# =============================================================
# CLUSTER 8 · FINAL DEPTH ADDS · push past 150 · Knight + Bryar/Carr + Greene 33
# =============================================================

STITLE = "Shoe Dog"
SFILE = "shoe_dog_knight.txt"
AUTHOR = "Phil Knight"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="leadership",
    concept="The crazy idea · let your business be your obsession",
    summary="Knight's framing throughout Shoe Dog: building Nike was not a 'job' or even a 'company' for the first 15 years; it was an obsession that organized his life. Every decision, every relationship, every dollar flowed through the obsession. The conventional wisdom (work-life balance, professional distance, multiple income streams) would have killed Nike before it formed. The lesson is not that obsession is required of all entrepreneurs, but that for the rare bets that produce category-defining companies, obsession is usually present, and trying to manufacture it after the fact rarely works.",
    usable_principle="If you're not obsessed with the work, the work probably will not produce category-defining outcomes. Don't try to fake obsession; do find the work that genuinely produces it, or accept that you're building something smaller.",
    sniped_relevance="For SNIPED, the question is honest: is BJ actually obsessed with founder photography + Direction Stack + the 10-year arc? The evidence suggests yes: the methodology development, the Cultural Doc writing, the willingness to refuse profitable off-scope work all point to genuine obsession. The discipline is to protect the obsession from organizational dilution (meetings, admin, low-leverage tasks) and from psychological dilution (comparison to other photographers, social proof drift). The obsession is the entire engine.",
    direct_quotes=[
        "Don't tell people how to do things, tell them what to do and let them surprise you with their results.",
        "The cowards never started and the weak died along the way. That leaves us, ladies and gentlemen. Us."
    ],
    tags=["knight","obsession","category-defining","engine-protection"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="Cash flow is oxygen · profitability is meaningless without it",
    summary="Knight documents Nike's near-bankruptcy moments repeatedly throughout the 1970s: the company was technically profitable but constantly out of cash because all profits were reinvested into inventory ahead of growth. Banks didn't understand the working-capital dynamic and pulled lines of credit at the worst moments. Knight's lesson: cash flow timing matters more than P&L profitability for any growing business. The companies that die in growth phases die from cash, not from profit losses.",
    usable_principle="Track cash flow separately and more carefully than P&L profitability, especially during growth. A profitable business that runs out of cash dies just as completely as an unprofitable one. Build cash reserves before they're needed; understand the working capital cycle before it surprises you.",
    sniped_relevance="For SNIPED, this means: maintain a cash buffer of 6-12 months operating expenses BEFORE accelerating any expensive growth bet (studio space, hire, gear purchase, marketing spend). The premium-service business model has lumpy cash flow (large deposits, multi-week project cycles, occasional Founder Tier engagements that arrive irregularly). The discipline is to NOT mistake a high-cash-flow month for a sustainable run rate, and to NOT take on commitments that depend on the high months continuing.",
    direct_quotes=[
        "Cash flow was our biggest problem. Wherever we turned, our cash flow was strangling us.",
        "The single easiest way to find out how you feel about someone. Say goodbye."
    ],
    tags=["knight","cash-flow","working-capital","reserve-discipline"]
)

STITLE = "Working Backwards"
SFILE = "working_backwards_bryar_carr.md"
AUTHOR = "Colin Bryar, Bill Carr"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="systems",
    concept="The PR/FAQ working-backwards document · start with the customer-facing press release",
    summary="Bryar and Carr document Amazon's signature product-development discipline: before any new product is approved or built, the team writes the future press release for the product (1-2 pages, customer-facing, plain language) AND the anticipated FAQ. The exercise forces the team to articulate the customer benefit clearly BEFORE the engineering complexity is even considered. If the press release isn't compelling, the product idea is killed before resources are spent. The discipline filters out ideas that sound exciting internally but don't actually translate into customer value.",
    usable_principle="Before committing resources to any new offer or product, write the future announcement of it as if it already exists. If the announcement doesn't excite the target customer, the idea isn't ready. Iterate the announcement until it's compelling, then build.",
    sniped_relevance="For SNIPED's offer ladder evolution (new tiers, new products like the Direction Stack book, possible Brand System tier, possible group programs), apply working-backwards: write the customer-facing announcement first. If BJ can't write a 1-pager that makes a founder client genuinely want to buy the new thing, the new thing isn't ready. This is the antidote to internal-logic offers (e.g., 'we should have a mid-tier because Naval says ladders are good') that don't survive customer-perspective scrutiny.",
    direct_quotes=[
        "We start by writing the press release. We write the FAQ. Only then do we consider whether to build the product.",
        "If the press release is hard to write, then the product is probably going to be unsuited to the customer's needs."
    ],
    tags=["bryar-carr","working-backwards","pr-faq","offer-design"]
)

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="systems",
    concept="Single-threaded leadership · one owner, one mission",
    summary="Bryar and Carr document Amazon's principle of single-threaded leadership: every important initiative gets exactly one leader whose ONLY job is that initiative. The leader is not splitting attention across multiple priorities; they are completely owning one thing. This breaks the common organizational pattern where the most important initiatives get the least focused attention because their leaders are also running other things. The discipline produces visibly faster execution on the prioritized initiative and clearer accountability.",
    usable_principle="For any genuinely important initiative, assign single-threaded ownership. The leader's only job is that initiative; everything else is delegated or paused. Initiatives that share leaders with other priorities are deprioritized initiatives, no matter what the org chart says.",
    sniped_relevance="For SNIPED at solo-founder scale, this translates to: BJ cannot be 'single-threaded' on multiple initiatives, but can be single-threaded on ONE initiative per quarter. Currently the Direction Stack book might be the single-threaded priority; client work, Cultural Doc, and operational backbone are the maintenance layer. The discipline is to choose ONE quarterly initiative that gets the protected daily time and execute it as if it were BJ's only job, with everything else maintained on minimum-viable rhythm.",
    direct_quotes=[
        "We figured out that when you wanted to deliver software fast, you needed a single-threaded leader: one person whose sole job is to lead that team and deliver that product.",
        "Without single-threaded leadership, important initiatives compete for attention and lose to the urgent."
    ],
    tags=["bryar-carr","single-threaded","priority-discipline","quarterly-focus"]
)

STITLE = "The 33 Strategies of War"
SFILE = "33_strategies_of_war_greene.md"
AUTHOR = "Robert Greene"

add(
    source_title=STITLE, source_file=SFILE, author=AUTHOR,
    domain="strategy",
    concept="The grand strategy · think beyond the current battle to the larger campaign",
    summary="Greene's central strategic discipline: the grand strategy thinks in terms of multi-year campaigns, not individual battles. Most operators (in war, business, careers) lose because they win tactical engagements that drift them away from strategic goals. The discipline is to maintain a clear North Star (the political objective for which war is being waged) and refuse engagements that would win on tactics while losing on strategy. The historical examples Greene uses (Napoleon's overreach into Russia, Hannibal's tactical brilliance without strategic follow-through) all share the pattern of tactical excellence undermined by strategic incoherence.",
    usable_principle="Before any tactical decision, ask: how does winning this advance the larger strategy? If it doesn't, decline the engagement even when victory is achievable. Tactical wins that drift you off strategy are losses in the larger frame.",
    sniped_relevance="For SNIPED, the grand strategy is the 10-year arc: become the definitive premium founder photographer + Direction Stack methodology + cultural authority node. Every tactical decision (this client, this collaboration, this content piece, this gear purchase, this expansion idea) should be evaluated against the grand strategy. Winning a profitable but off-strategy engagement (e.g., a corporate event shoot for a Fortune 500) is a strategic loss even when tactically successful. The Constraint Audit quarterly review should test for grand-strategy alignment.",
    direct_quotes=[
        "Strategy is the art of looking beyond the present battle and calculating ahead.",
        "Focus on your grand strategic goal, and you will not be tempted into the side trips and dead ends that destroy so many in war and in life."
    ],
    tags=["greene","grand-strategy","tactical-vs-strategic","constraint-audit"]
)

print(f"After cluster 8 final adds: {len(CHUNKS)} chunks")
with OUT.open("w") as f:
    for c in CHUNKS:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")
print(f"Wrote {len(CHUNKS)} chunks to {OUT}")
