#!/usr/bin/env python3
"""Write CONSULTING_SERVICE_CHUNKS.jsonl · 15 curated chunks · 7 sources.

batch_id: CONSULTING_SERVICE · chunk_id: CONSULTING_SERVICE_NNN
The professional-services / consulting / client-craft register · the FIRST of the
four ADJACENT_TIER_2_CLUSTERS sub-lanes. Existing domains only (operator-doctrine
anchor). No new domain. `systems` NOT used/grown (route to systems-thinking, which
is also not needed here); `creativity` NOT created. No em-dashes. Curated
consulting/service-craft extraction (NOT a consulting-book chapter summary or guru
playbook). Decision-neutral: NOT a directive and NOT a SNIPED brand. Guardrail in
every chunk.
"""
import json
import os

OUT = os.path.expanduser(
    "~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/CONSULTING_SERVICE_CHUNKS.jsonl")

VBF = ("Value-Based Fees", "value_based_fees_weiss.txt", "Alan Weiss")
MDC = ("Million Dollar Consulting", "million_dollar_consulting_weiss.txt", "Alan Weiss")
MCK = ("The McKinsey Way", "the_mckinsey_way_rasiel.txt", "Ethan M. Rasiel")
MAI = ("Managing the Professional Service Firm", "managing_the_professional_service_firm_maister.txt", "David H. Maister")
GN = ("Getting Naked", "getting_naked_lencioni.txt", "Patrick Lencioni")
ADV = ("The Advantage", "the_advantage_lencioni.txt", "Patrick Lencioni")
FC = ("Flawless Consulting", "flawless_consulting_block.txt", "Peter Block")

GUARD = (" Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support and "
         "pattern-library only, not doctrine and not a directive: not a directive that BJ "
         "become a consultant, agency bro, management guru, productivity influencer, "
         "expert-brand persona, corporate thought-leader, or service-business cosplay "
         "operator. Consulting and service material is held as operator tooling, diagnostic "
         "models, service craft, pricing logic, trust mechanics, and delivery discipline. No "
         "final SNIPED, SNIPED Media, or BASEPLATE direction; photography remains one option "
         "among several.")

# (source, domain, concept, summary, usable_principle, relevance_lead, quotes, tags)
ROWS = [
    # ---- VALUE-BASED FEES (Weiss) · 2 ----
    (VBF, "commercial-architecture",
     "Value-based fees: price the perceived value, not the time",
     "Weiss's core argument is that advisory work should be priced against the value it creates for the "
     "client, not the hours it consumes. Charging by time caps the upside, rewards inefficiency, and "
     "forces the buyer to weigh cost instead of results; perceived value is the real basis of a fee, so "
     "the price should track the outcome and the buyer's perception of it.",
     "Price expertise against the value or outcome delivered, not the time spent; time-based billing "
     "anchors the buyer on cost and penalizes you for being fast and good.",
     "For BJ this separates pricing a deliverable by hours from pricing it by the value it creates, a "
     "pricing-logic distinction held as analysis, not a directive to sell consulting.",
     ["perceived value is the basis"],
     ["value-pricing", "fees", "perceived-value", "outcome-pricing", "commercial-architecture"]),

    (VBF, "operator-doctrine",
     "Conceptual agreement first: align on value with the buyer before the proposal",
     "Before any fee or proposal, Weiss insists on reaching conceptual agreement with the economic buyer "
     "on three things: the objectives, the measures of success, and the value to the client. Once both "
     "sides agree on what the work is worth and how success will be judged, the fee and the proposal "
     "follow naturally; skipping this step is the root cause of fee disputes and scope confusion.",
     "Establish agreed objectives, measures, and value with the real decision-maker before quoting or "
     "proposing; the agreement on worth must precede the price.",
     "BJ can apply align-on-value-before-price to any engagement (agree what good looks like and what it "
     "is worth first), a transferable discipline, not a mandate to become an advisor.",
     ["conceptual agreement", "objectives, measures, and value"],
     ["conceptual-agreement", "economic-buyer", "objectives", "scoping", "value-first"]),

    # ---- MILLION DOLLAR CONSULTING (Weiss) · 2 (incl synthesis attribution at 015) ----
    (MDC, "strategy",
     "Market gravity: be pulled toward, not chasing",
     "Weiss frames sustainable practice growth as building market gravity: a field of attraction "
     "(writing, speaking, reputation, referrals) that pulls prospects toward you so they call seeking to "
     "become clients, rather than you chasing them with cold pursuit. The work is to build the gravity "
     "well, not to hunt each sale.",
     "Build a field of attraction (visible expertise, reputation, referrals) so demand comes to you; "
     "pull beats chase for high-trust, high-value work.",
     "BJ can weigh building attraction (so the right work finds him) against chasing leads, a "
     "demand-architecture pattern held as analysis, not a directive to become a personal-brand marketer.",
     ["Market Gravity"],
     ["market-gravity", "attraction", "demand", "reputation", "strategy"]),

    (MDC, "operator-doctrine",
     "Improve the client's condition; the trust relationship is the asset",
     "Weiss's practice model rests on a single premise: the work exists to improve the client's "
     "condition, and the durable asset is a trusting relationship with the buyer, not a transaction. "
     "Distinctive results plus a collaborative, candid, long-term relationship are what make the "
     "practice resilient through dry spells and generate repeat and referral business.",
     "Anchor service work on measurably improving the client's condition and on a candid, durable "
     "relationship; the relationship, not the single deal, is the real asset.",
     "BJ can hold improve-the-client's-condition and relationship-as-asset as a service-craft lens for "
     "any value-delivery work, not a directive to build a consulting practice.",
     ["improve the client", "trusting relationship with the buyer"],
     ["client-condition", "trust", "relationship-as-asset", "repeat-business", "service-craft"]),

    # ---- THE McKINSEY WAY (Rasiel) · 2 ----
    (MCK, "mental-models",
     "MECE: structure problems mutually exclusive, collectively exhaustive",
     "Rasiel describes MECE (mutually exclusive, collectively exhaustive) as the structuring discipline "
     "pounded into every McKinsey associate: break a problem into buckets that do not overlap (mutually "
     "exclusive) and together cover the whole (collectively exhaustive). It forces clean, complete "
     "decomposition and prevents both double-counting and gaps.",
     "Decompose any problem into non-overlapping, gap-free buckets (MECE) before analyzing; clean "
     "structure precedes good analysis.",
     "BJ can apply MECE structuring to any diagnosis or proposal (clean buckets, no overlap, no gaps), a "
     "directly transferable thinking tool.",
     ["mutually exclusive, collectively exhaustive"],
     ["MECE", "problem-structuring", "decomposition", "diagnosis", "mental-models"]),

    (MCK, "operator-process",
     "Hypothesis-driven and fact-based: don't boil the ocean",
     "The McKinsey method is hypothesis-driven and fact-based: start with an initial hypothesis about "
     "the answer, then gather only the facts needed to prove or disprove it rather than analyzing "
     "everything. Don't boil the ocean (work smarter, use the 80/20), and make sure you are solving the "
     "right problem before you start.",
     "Lead with a falsifiable hypothesis and gather only the facts that test it; ignore most available "
     "data, and confirm you are solving the right problem first.",
     "BJ can run hypothesis-first, fact-bounded analysis (test a clear guess, don't over-collect) on any "
     "problem, an efficiency discipline held as method.",
     ["boil the ocean"],
     ["hypothesis-driven", "fact-based", "80-20", "focus", "operator-process"]),

    # ---- MANAGING THE PROFESSIONAL SERVICE FIRM (Maister) · 2 ----
    (MAI, "commercial-architecture",
     "Leverage: the finders, minders, grinders ratio is the engine",
     "Maister shows that a professional-service firm's economics turn on leverage, the ratio of senior "
     "to junior staff (the finders who win work, the minders who manage it, the grinders who do it). The "
     "mix the work requires determines the firm's profitability, its growth rate, and the career paths "
     "it can offer; get the leverage wrong and the economics break.",
     "Match the senior/junior leverage ratio to the actual work mix; the leverage structure, not effort, "
     "sets the economics of a service practice.",
     "BJ can read leverage (who finds, who minds, who grinds) as the structural lever of any "
     "service-delivery economics, a model held as analysis, not a directive to staff a firm.",
     ["the finders", "grinders"],
     ["leverage", "finders-minders-grinders", "firm-economics", "staffing", "commercial-architecture"]),

    (MAI, "leadership",
     "The asset is people: goodwill, skill, and reputation",
     "In Maister's view the professional firm's real equity is not financial but the accumulated "
     "goodwill, skill, and reputation carried by its people, assets that depreciate quickly without "
     "investment. Managing the firm means continuously balancing three goals (service to clients, "
     "satisfaction for the people, and financial success) by developing the professionals themselves.",
     "Treat skill, reputation, and people as the depreciating core asset to be reinvested in; managing a "
     "knowledge practice is managing and developing its people.",
     "BJ can hold people/skill/reputation as the real, perishable asset to invest in, a people-centered "
     "operating lens applicable beyond firms, not a directive to lead an organization.",
     ["goodwill, skill, and reputation"],
     ["people-as-asset", "skill", "reputation", "three-goals", "leadership"]),

    # ---- GETTING NAKED (Lencioni) · 2 ----
    (GN, "ethics",
     "Vulnerability-based service: shed the three fears, put the client first",
     "Lencioni's fable argues that the most loyal client relationships come from vulnerability: being "
     "willing to look uncertain or wrong in service of the client's interest. The path is shedding the "
     "three fears that sabotage loyalty, so the advisor consults honestly, says the hard thing, and "
     "sometimes risks the deal to serve the client well.",
     "Lead with vulnerability and the client's interest over self-protection; honesty that risks the "
     "engagement builds more loyalty than guarded competence.",
     "BJ can hold client-interest-over-self-protection and candid vulnerability as a trust-building "
     "ethic for any service relationship, not a directive to become a consultant.",
     ["shedding the three fears"],
     ["vulnerability", "client-first", "trust", "candor", "ethics"]),

    (GN, "founder-psychology",
     "The three fears that sabotage: losing the business, embarrassment, inferiority",
     "Lencioni names the three fears that quietly sabotage service relationships: the fear of losing the "
     "business (so you withhold and please), the fear of being embarrassed (so you stay silent), and the "
     "fear of feeling inferior to the client (so you posture). Naming them is what lets an operator act "
     "against them.",
     "Watch for the fear of losing the deal, of looking foolish, and of feeling inferior; these private "
     "fears, unnamed, distort how you show up with clients.",
     "BJ can use the three-fears frame as self-awareness about how his own fear might distort client "
     "interactions, a psychological diagnostic, not a directive.",
     ["fear of losing the business", "fear of feeling inferior"],
     ["fear", "self-sabotage", "self-awareness", "client-relationship", "founder-psychology"]),

    # ---- THE ADVANTAGE (Lencioni) · 2 ----
    (ADV, "culture",
     "Organizational health beats smart: minimal politics and confusion",
     "Lencioni argues organizational health, not raw smarts, is the single greatest factor in success: "
     "the signs are minimal politics, minimal confusion, high morale and productivity, and low turnover "
     "among good people. A healthy organization out-executes a smarter but unhealthy one because its "
     "energy is not lost to friction.",
     "Treat health (low politics, low confusion, aligned people) as a bigger lever than additional "
     "cleverness; friction, not lack of intelligence, is what usually wastes capacity.",
     "BJ can read organizational/relational health as a force multiplier in any group he works with, a "
     "diagnostic lens, not a directive to run a company.",
     ["organizational health", "minimal politics", "single greatest factor"],
     ["organizational-health", "politics", "clarity", "alignment", "culture"]),

    (ADV, "operator-doctrine",
     "The four disciplines: build a cohesive team, create, overcommunicate, reinforce clarity",
     "Lencioni's model for health is four disciplines: build a cohesive leadership team, create clarity "
     "(answer the few critical questions the same way), overcommunicate that clarity relentlessly, and "
     "reinforce it through systems and especially great meetings. Clarity is worthless until it is "
     "repeated far past the point of comfort.",
     "Get a few people genuinely aligned, decide the critical questions, then overcommunicate and "
     "reinforce that clarity well past the point you think is necessary.",
     "BJ can apply create-clarity-then-overcommunicate-it to any team or collaboration, a directly "
     "usable operating discipline.",
     ["Cohesive Leadership Team", "Overcommunicate Clarity"],
     ["clarity", "alignment", "overcommunication", "meetings", "operator-doctrine"]),

    # ---- FLAWLESS CONSULTING (Block) · 2 ----
    (FC, "operator-process",
     "Contracting and the collaborative role: not expert, not pair of hands",
     "Block frames service work in phases (contracting, discovery, feedback, decision) and three "
     "possible roles: the expert who takes over, the pair of hands who just executes, and the "
     "collaborative partner who shares responsibility fifty-fifty. The collaborative role, set up in an "
     "explicit contract about wants and offers, is where expertise actually gets used.",
     "Contract explicitly at the start (mutual wants and offers) and aim for a collaborative, shared-"
     "responsibility role rather than taking over or just executing orders.",
     "BJ can use explicit contracting and the collaborative-partner stance for any advisory or "
     "delivery relationship, a process model held as method.",
     ["pair of hands"],
     ["contracting", "collaborative-role", "phases", "partnership", "operator-process"]),

    (FC, "ethics",
     "Authenticity and resistance: say what you are experiencing",
     "Block's central skill is authenticity: putting into words what you are experiencing with the "
     "client in the moment, rather than being clever or compliant. He treats client resistance not as an "
     "obstacle to overcome but as a signal of an underlying concern (the fear and the wish) to be named "
     "directly; naming it honestly is what moves the work forward.",
     "Name what is actually happening in the room, and treat resistance as information about an "
     "underlying concern rather than something to argue past.",
     "BJ can hold authentic naming and read-the-resistance as a relational discipline for any "
     "high-stakes collaboration, not a directive to perform a consultant role.",
     ["Being Authentic", "put into words what you"],
     ["authenticity", "resistance", "candor", "presence", "ethics"]),

    # ---- SYNTHESIS · 1 (attributed to Million Dollar Consulting) ----
    (MDC, "operator-doctrine",
     "Synthesis: the consulting/service operator toolkit",
     "Across the seven sources a service-craft toolkit emerges: price the value not the time and agree "
     "on worth before the proposal (Weiss); structure problems MECE and work hypothesis-first without "
     "boiling the ocean (Rasiel); run the economics on leverage and treat people/skill/reputation as the "
     "asset (Maister); serve from vulnerability and shed the three fears (Lencioni, Getting Naked); build "
     "health through cohesion and overcommunicated clarity (Lencioni, The Advantage); and contract "
     "explicitly while staying authentic and reading resistance (Block). It is a pattern-library for "
     "pricing, diagnosis, trust, and delivery discipline.",
     "Combine value-pricing, MECE diagnosis, leverage economics, vulnerability-based trust, clarity, and "
     "authentic delivery into a service-craft toolkit, held as analysis rather than a practice to launch.",
     "BJ holds this as operator tooling and service-craft literacy for his build-mode stage, NOT a "
     "directive to become a consultant or expert-brand persona.",
     [],
     ["synthesis", "service-craft", "pricing", "diagnosis", "operator-toolkit"]),
]


def sweep(obj):
    em = chr(0x2014)
    if isinstance(obj, str):
        return obj.replace(em, " · ")
    if isinstance(obj, list):
        return [sweep(x) for x in obj]
    if isinstance(obj, dict):
        return {k: sweep(v) for k, v in obj.items()}
    return obj


def main():
    rows = []
    for i, (src, domain, concept, summary, principle, rel, quotes, tags) in enumerate(ROWS, 1):
        title, sfile, author = src
        r = {
            "chunk_id": f"CONSULTING_SERVICE_{i:03d}",
            "batch_id": "CONSULTING_SERVICE",
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": rel + GUARD,
            "direct_quotes": quotes,
            "tags": tags,
        }
        rows.append(r)

    for r in rows:
        for q in r["direct_quotes"]:
            assert len(q.split()) <= 6, f"quote too long in {r['chunk_id']}: {q}"

    forbidden = {"consulting", "service", "management", "business", "productivity",
                 "expertise", "innovation", "self-help", "systems", "creativity"}
    used = {r["domain"] for r in rows}
    assert not (used & forbidden), used & forbidden

    rows = [sweep(r) for r in rows]
    blob = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    assert chr(0x2014) not in blob, "em-dash found in output"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(blob)
    print(f"wrote {len(rows)} chunks to {OUT}")


if __name__ == "__main__":
    main()
