#!/usr/bin/env python3
"""
Write FOUNDER_SECOND_TIER_CHUNKS.jsonl · 20 chunks (18 source + 2 synthesis) across 7 founder bios.
12-field canonical schema. NO new domain (10 existing domains · anchored on founder-psychology · ethics
carries the dark-side-of-scale chunks). Identity-optionality guardrail: founder arcs are PATTERN-LIBRARY
only, read against CURRENT_OPERATOR_REALITY_BRIEF; NO directive for BJ to copy any founder or manufacture
a myth; no final SNIPED / SNIPED Media / BASEPLATE direction. Em-dash sweep at the end.
"""

import json
from pathlib import Path

OUT = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "FOUNDER_SECOND_TIER_CHUNKS.jsonl"

WALTON = ("Sam Walton: Made In America", "sam_walton_made_in_america.txt", "Sam Walton")
MUSK = ("Elon Musk", "elon_musk_isaacson.txt", "Walter Isaacson")
UBER = ("Super Pumped", "super_pumped_uber_isaac.txt", "Mike Isaac")
AIRBNB = ("The Airbnb Story", "the_airbnb_story_gallagher.txt", "Leigh Gallagher")
TITAN = ("Titan", "titan_rockefeller_chernow.txt", "Ron Chernow")
BANANA = ("The Fish That Ate the Whale", "the_fish_that_ate_the_whale_cohen.txt", "Rich Cohen")
SCHULTZ = ("Pour Your Heart Into It", "pour_your_heart_into_it_schultz.txt", "Howard Schultz & Dori Jones Yang")

DG = "Pattern-library / decision-support lens only, read against CURRENT_OPERATOR_REALITY_BRIEF (solo operator, ideation/build mode). NOT a directive for BJ to copy this founder or manufacture a myth; this does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction, and photography remains one option among several."

C = []
def add(src, domain, concept, summary, principle, relevance, quotes, tags):
    n = len(C) + 1
    title, sfile, author = src
    C.append({
        "chunk_id": f"FOUNDER_SECOND_TIER_{n:03d}",
        "batch_id": "FOUNDER_SECOND_TIER",
        "source_title": title, "source_file": sfile, "author": author,
        "domain": domain, "concept": concept, "summary": summary,
        "usable_principle": principle, "sniped_relevance": relevance,
        "direct_quotes": quotes, "tags": tags,
    })

# ---------------- Sam Walton · Walmart · 3 ----------------
add(WALTON, "operator-doctrine",
    "Customer obsession and relentless cost discipline",
    "Walton built Walmart on two non-negotiables: the customer is the boss (lowest prices, always), and controlling expenses better than any competitor so the savings could be passed on. The cost discipline was a culture, not a campaign, held from the first store to thousands.",
    "Treat the customer as the boss and out-discipline competitors on cost; pass the savings on as the durable edge.",
    "An operator-doctrine lens: a relentless, culture-deep cost/quality discipline can be the moat. " + DG,
    [],
    ["customer-obsession", "cost-discipline", "walmart", "operator-doctrine", "walton"])

add(WALTON, "commercial-architecture",
    "Distribution and logistics as the real moat",
    "Walmart's hub-and-spoke distribution centers, private trucking fleet, and early investment in inventory IT let it expand profitably into small towns competitors ignored. The logistics system, not the storefront, was the structural advantage that made low prices sustainable at scale.",
    "Build the unglamorous distribution/logistics system that makes the visible offering cheap and defensible at scale.",
    "A structural lens: the back-end system (distribution, logistics, IT) is often the real moat behind a simple front-end. " + DG,
    [],
    ["distribution", "logistics", "moat", "commercial-architecture", "walton"])

add(WALTON, "operator-process",
    "Learn relentlessly and align the associates",
    "Walton copied good ideas from anyone (including competitors), kept a famous Saturday-morning rhythm of review and adjustment, and turned employees into profit-sharing 'associates' to align the whole organization. Humility-to-learn plus shared ownership of outcomes powered the expansion.",
    "Copy what works from anyone, run a relentless review cadence, and give the people doing the work a real stake.",
    "An operating-process lens (pairs with EDGE): learn without ego, run a review rhythm, align the team with ownership. " + DG,
    [],
    ["learning", "review-cadence", "associates", "operator-process", "walton"])

# ---------------- Elon Musk · Tesla/SpaceX · 3 ----------------
add(MUSK, "founder-psychology",
    "Mission-driven extreme risk tolerance",
    "Musk frames his companies around civilizational missions (sustainable energy, multiplanetary life) and repeatedly bets everything (personal capital, company survival) on them. The mission justifies a risk appetite far beyond normal operators, for better and worse.",
    "A galvanizing mission can license extreme risk and effort; it also concentrates danger when the bet is the whole company.",
    "A founder-psychology lens on mission and risk · held as a pattern, NOT a prescription for the operator's risk level. " + DG,
    [],
    ["mission", "risk-tolerance", "all-in", "founder-psychology", "musk"])

add(MUSK, "systems-thinking",
    "First principles and the machine that builds the machine",
    "Musk reasons from physics-level first principles (what does this actually cost / require) rather than analogy, and obsesses over the factory itself, the machine that builds the machine, treating manufacturing/production as the hard problem, not the prototype.",
    "Reason from first principles, not analogy, and treat the production system (not the prototype) as the real engineering problem.",
    "A systems lens: the repeatable production system is the leverage point · relevant to any future SNIPED system, held as a pattern. " + DG,
    ["the machine that builds the machine"],
    ["first-principles", "manufacturing", "production-system", "systems-thinking", "musk"])

add(MUSK, "founder-psychology",
    "Hardcore intensity and leadership contradictions",
    "Isaacson documents the 'surge' and 'demon mode' style: punishing deadlines, hardcore expectations, and abrupt swings that produce extraordinary output at real human cost. The biography presents the contradiction (drive vs. damage) rather than endorsing it.",
    "Extreme intensity can produce extraordinary results and serious collateral cost; weigh both rather than romanticising the drive.",
    "A founder-psychology lens that explicitly includes the costs · a caution pattern, NOT a model to imitate. " + DG,
    [],
    ["intensity", "leadership-contradiction", "human-cost", "founder-psychology", "musk"])

# ---------------- Super Pumped · Uber · 3 ----------------
add(UBER, "strategy",
    "Blitzscale: growth as the only metric",
    "Under Kalanick, Uber pursued hypergrowth above all, raising and burning enormous capital to win market share city by city before competitors or regulators could react. Speed and scale were treated as the strategy, with most other concerns subordinated.",
    "Hypergrowth-at-all-costs can win a market fast, but subordinating everything to growth builds compounding liabilities.",
    "A strategy lens on blitzscale and its trade-offs · held as analysis, NOT a directive to chase growth-at-all-costs. " + DG,
    [],
    ["blitzscale", "hypergrowth", "market-share", "strategy", "uber"])

add(UBER, "commercial-architecture",
    "Operating ahead of the rules",
    "Uber expanded by launching in cities before regulators could respond, mobilising riders and drivers as a political lobby, and treating legal/regulatory friction as an obstacle to route around. The model depended on outrunning the rule-makers.",
    "Some models depend on operating ahead of regulation; that creates speed but also existential legal and reputational risk.",
    "A structural lens on regulatory-arbitrage models and their fragility · a caution pattern, not a recommendation. " + DG,
    [],
    ["regulation", "first-mover", "political-mobilisation", "commercial-architecture", "uber"])

add(UBER, "ethics",
    "The toxic-culture collapse: the dark side of win-at-all-costs",
    "Uber's growth culture (epitomised by values like 'Always Be Hustlin' and 'toe-stepping') curdled into harassment, surveillance, and scandal that ultimately forced Kalanick out. The book is a case study in how an unchecked win-at-all-costs culture becomes an existential liability.",
    "An unchecked win-at-all-costs culture eventually produces the scandals that threaten the company itself; culture is a risk, not a slogan.",
    "An ethics lens that keeps the scale pattern honest · the cost of growth without guardrails · NOT aspirational. " + DG,
    ["Always Be Hustlin"],
    ["toxic-culture", "ethics", "win-at-all-costs", "uber", "dark-side"])

# ---------------- The Airbnb Story · 2 ----------------
add(AIRBNB, "systems-thinking",
    "Manufacturing trust between strangers",
    "Airbnb's core problem was not lodging but trust: getting strangers to host and stay with strangers at scale. Reviews, verified identity, secure payments, and host guarantees were the system that engineered enough trust for the marketplace to exist.",
    "When the real obstacle is trust, build the system (reputation, verification, guarantees) that manufactures it at scale.",
    "A systems lens: trust can be engineered as a product feature · relevant to any future marketplace/relationship-based SNIPED offer, held as a pattern. " + DG,
    [],
    ["trust", "marketplace", "reputation-system", "systems-thinking", "airbnb"])

add(AIRBNB, "brand",
    "Design thinking, the 11-star experience, and belonging",
    "Chesky (a designer) ran Airbnb on design thinking: obsess over the user's emotional experience, imagine an absurd '11-star' version to push past adequate, and frame the brand around 'belong anywhere' rather than cheap rooms. Experience and belonging were the brand, not price.",
    "Design the emotional experience past 'good enough' and frame the brand around belonging/identity, not the commodity.",
    "A brand/experience lens directly relevant to SNIPED's craft: design the felt experience and the meaning, not just the deliverable. " + DG,
    ["belong anywhere"],
    ["design-thinking", "experience", "belonging", "brand", "airbnb"])

# ---------------- Titan · Rockefeller · 3 ----------------
add(TITAN, "capital",
    "Consolidation and capital control: the Standard Oil trust",
    "Rockefeller built Standard Oil by consolidating a chaotic industry, through horizontal and vertical integration and the legal 'trust' structure, into near-total control of refining and distribution. Control of the capital structure and the chokepoints, not just operations, was the source of power.",
    "Durable power can come from consolidating a fragmented industry and controlling the capital structure and chokepoints, not only from operating well.",
    "A capital/ownership lens (pairs with MONEY_OWNERSHIP) on consolidation and control · held as analysis, not a directive. " + DG,
    [],
    ["consolidation", "the-trust", "capital-control", "capital", "rockefeller"])

add(TITAN, "operator-doctrine",
    "Efficiency obsession and leverage over suppliers",
    "Rockefeller was fanatical about efficiency (measuring everything, eliminating waste to the drop) and used scale to extract railroad rebates that competitors could not match. Operational excellence plus structural leverage compounded into an unassailable cost position.",
    "Pair fanatical operational efficiency with structural leverage so your cost position cannot be matched.",
    "An operator-doctrine lens on efficiency-as-weapon · the leverage methods are noted with their ethical cost (next chunk). " + DG,
    [],
    ["efficiency", "rebates", "cost-leverage", "operator-doctrine", "rockefeller"])

add(TITAN, "ethics",
    "Ruthlessness, monopoly, and the philanthropy that followed",
    "Standard Oil's dominance relied on ruthless, often anticompetitive tactics that provoked antitrust breakup; Rockefeller later became one of history's great philanthropists. The arc raises the unresolved ethics of monopoly power and of redemption through giving.",
    "Monopoly power built by ruthless means invites reckoning; later philanthropy complicates but does not erase the means.",
    "An ethics lens keeping the consolidation pattern honest · power and its costs · NOT an endorsement. " + DG,
    [],
    ["monopoly", "antitrust", "philanthropy", "ethics", "rockefeller"])

# ---------------- The Fish That Ate the Whale · Zemurray · 2 ----------------
add(BANANA, "operator-process",
    "On-the-ground operator knowledge beats the head office",
    "Sam Zemurray, a penniless immigrant, out-competed the giant United Fruit by knowing the banana business at ground level (the docks, the ripes, the boats) better than its absentee executives, then eventually took the company over, the fish that ate the whale.",
    "Deep, hands-on operating knowledge of a specific business can outmaneuver larger, distant incumbents who manage from spreadsheets.",
    "An operator-knowledge lens directly relevant to BJ's field-operator edge: on-the-ground knowledge is a real advantage · held as a pattern. " + DG,
    [],
    ["on-the-ground", "operator-edge", "outmaneuver-incumbents", "operator-process", "zemurray"])

add(BANANA, "ethics",
    "United Fruit and the dark geopolitics of power",
    "Zemurray's and United Fruit's dominance extended to backing a coup in Honduras and entangling the company in Central American politics, the dark side of unchecked corporate power abroad. The hustle-to-empire arc includes real human and political costs.",
    "Unchecked corporate power can extend into politics and harm; the inspiring hustle arc carries a serious ethical shadow.",
    "An ethics lens that keeps the immigrant-operator myth honest · power without accountability · NOT aspirational. " + DG,
    [],
    ["united-fruit", "geopolitics", "power-without-accountability", "ethics", "zemurray"])

# ---------------- Pour Your Heart Into It · Schultz · 2 ----------------
add(SCHULTZ, "brand",
    "Brand through experience: the romance and the third place",
    "Schultz built Starbucks not as coffee but as an experience, the 'romance' of Italian espresso bars and the 'third place' between home and work. The brand lived in the felt experience of the store, which justified a premium far above commodity coffee.",
    "Build the brand in the felt, repeatable experience (the third place), so the offering escapes commodity pricing.",
    "A brand/experience lens highly relevant to SNIPED's editorial/photography craft: sell the experience and meaning, not the commodity. " + DG,
    ["Third Place"],
    ["experience", "third-place", "premium", "brand", "schultz"])

add(SCHULTZ, "culture",
    "Scaling culture: partners, values, and the growth tension",
    "Schultz treated employees as 'partners' (with stock and benefits even for part-timers) and tried to scale Starbucks' values and culture as fast as its stores, wrestling openly with the tension between growth and staying true to the original soul.",
    "Scaling a values-led culture is a deliberate, contested project; growth and soul pull against each other and must be managed.",
    "A culture lens on scaling values and the growth-vs-soul tension · relevant to any future SNIPED growth, held as a pattern. " + DG,
    [],
    ["partners", "values", "growth-vs-soul", "culture", "schultz"])

# ---------------- Synthesis · 2 ----------------
add(WALTON, "founder-psychology",
    "SYNTHESIS: the scale-operator pattern",
    "Across the seven arcs, ambitious operators turned small openings into durable institutions through a recurring pattern: a relentless edge (Walton's cost discipline, Rockefeller's efficiency, Musk's first-principles, Zemurray's on-the-ground knowledge, Chesky's design, Schultz's experience), a back-end system or moat (distribution, the trust, the production machine, trust-engineering), control of capital or chokepoints, and culture scaled deliberately, with several arcs (Uber, Standard Oil, United Fruit) showing the recurring dark side when scale outruns guardrails.",
    "Turn a small opening into an institution via a relentless edge, a back-end moat, capital/chokepoint control, and deliberately scaled culture, while watching for the dark side when growth outruns guardrails.",
    "A consolidated scale-operator pattern library · supplies patterns to draw from, NOT a path to copy. " + DG,
    [],
    ["synthesis", "scale-operator", "pattern-library", "founder-psychology", "founder-second-tier"])

add(MUSK, "strategy",
    "SYNTHESIS: pattern-library only, read against current reality",
    "These founder arcs are inspiration and a pattern library, not a template. Taken literally they could push the operator to copy a founder, chase scale, or manufacture a myth. Read against CURRENT_OPERATOR_REALITY_BRIEF (solo operator, ideation/build mode, loading the backend) and the identity-and-brand-optionality guardrails, they are decision-support lenses that widen and pressure-test the option set, keeping SNIPED's direction reversible until the operator decides.",
    "Use founder arcs to expand and stress-test options, not to copy a founder, chase scale, or manufacture a myth; keep direction reversible.",
    "Explicitly preserves optionality: founder arcs are pattern-library only. No directive for BJ to copy any founder or manufacture a myth; no final SNIPED / SNIPED Media / BASEPLATE direction; photography stays one option among several. " + DG,
    [],
    ["optionality", "pattern-library", "guardrail", "strategy", "founder-second-tier"])

# ---------------- write + em-dash sweep ----------------
EM = chr(0x2014)
def sweep(o):
    if isinstance(o, str): return o.replace(EM, " · ")
    if isinstance(o, list): return [sweep(x) for x in o]
    if isinstance(o, dict): return {k: sweep(v) for k, v in o.items()}
    return o

C = [sweep(c) for c in C]
with OUT.open("w", encoding="utf-8") as f:
    for c in C:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")

from collections import Counter
dist = Counter(c["domain"] for c in C)
print(f"wrote {len(C)} chunks to {OUT}")
print("domains:", dict(sorted(dist.items(), key=lambda x: -x[1])))
m = json.load(open(Path.home()/"AI-Brain-Refinery"/"01_KNOWLEDGE_BASE"/"MASTER_CHUNK_MAP.json"))["combined_domain_counts"]
newd = [d for d in dist if d not in m]
print("NEW domains (should be NONE):", newd or "NONE")
print("em-dashes in output:", sum(json.dumps(c, ensure_ascii=False).count(EM) for c in C))
