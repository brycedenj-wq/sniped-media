#!/usr/bin/env python3
"""Write NETWORK_DISTRIBUTION_CHUNKS.jsonl · 16 curated chunks from the 5 net-new sources.
Existing domains only · distribution anchor · no new domain. Em-dash swept + asserted."""
import json, os

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/NETWORK_DISTRIBUTION_CHUNKS.jsonl")
EXTRACT = "01_KNOWLEDGE_BASE/batches/network_distribution_extracted"
DASH = chr(0x2014)
BATCH = "NETWORK_DISTRIBUTION"

INEV = ("The Inevitable", "Kevin Kelly", "the_inevitable_kelly.txt")
NEWR = ("New Rules for the New Economy", "Kevin Kelly", "new_rules_kelly.txt")
LONG = ("The Long Tail", "Chris Anderson", "long_tail_anderson.txt")
FREE = ("Free: The Future of a Radical Price", "Chris Anderson", "free_anderson.txt")
GAME = ("The Great Online Game", "Packy McCormick", "great_online_game_mccormick.txt")

GUARD = (
    " Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support / pattern-library only, "
    "NOT doctrine and NOT a directive. NOT a directive that BJ build a platform, a marketplace, a SaaS company, "
    "a media network, an agency, or a growth-hacking business, and NOT a mandate to chase network effects, go viral, "
    "monetize via freemium, or productize attention. Network and platform logic is translated into practical "
    "distribution, access, attention, status, and commercial-architecture patterns for BJ's actual build-mode stage. "
    "No final SNIPED, SNIPED Media, or BASEPLATE direction; photography remains one option among several. "
    "The Bible remains held separately and untouched."
)

def C(n, src, domain, concept, summary, principle, relevance, quotes, tags):
    st, au, sf = src
    return {
        "chunk_id": f"{BATCH}_{n:03d}",
        "batch_id": BATCH,
        "source_title": st,
        "source_file": sf,
        "author": au,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": principle,
        "sniped_relevance": relevance + GUARD,
        "direct_quotes": quotes,
        "tags": tags,
    }

rows = [
    # ---- The Inevitable (Kelly) · 4 + synthesis ----
    C(1, INEV, "systems-thinking",
      "The 12 technological forces are trajectories, not products",
      "Kelly frames the connected economy through twelve ongoing verbs (becoming, cognifying, flowing, screening, accessing, sharing, filtering, remixing, tracking, interacting, questioning, beginning). They are directions of motion, deep currents that persist regardless of which specific company or product wins, so the operator reads the trajectory rather than betting on a single endpoint.",
      "Read the durable direction of a technology current, not the product of the moment; position with the trajectory rather than against it.",
      "Helps BJ read where connected-economy currents are heading (toward sharing, accessing, filtering) so any eventual offer rides a trajectory instead of fighting one.",
      ["forces are trajectories", "this trend will continue"],
      ["network-distribution", "the-inevitable", "kelly", "technological-forces", "trajectory", "systems"]),
    C(2, INEV, "distribution",
      "Flowing: when copies are free, value moves to the un-copyable generatives",
      "As everything becomes a fluid stream, perfect copies cost nothing to make and distribute, so price collapses on the copy itself. Value migrates to qualities that cannot be copied, the generatives: immediacy, personalization, interpretation, authenticity, accessibility, embodiment, patronage, and discoverability.",
      "Stop charging for the copy; charge for the un-copyable layer wrapped around it (access, immediacy, trust, embodiment).",
      "For BJ this reframes where money lives when content is abundant: not the file but the immediacy, authenticity, and embodied experience around it.",
      ["copies flow", "free copies"],
      ["network-distribution", "the-inevitable", "kelly", "generatives", "abundance", "value-migration"]),
    C(3, INEV, "network-effects",
      "Accessing and sharing: access beats ownership and cooperation compounds",
      "Kelly argues the long-term pull is away from ownership toward access (subscription, on-demand, rental) and toward ever-deeper sharing and cooperation. Each act of sharing increases the value of the connected whole, a compounding social/technical dynamic rather than a one-time transaction.",
      "Design for access and repeated sharing, not one-off ownership; value accrues to whatever compounds with each new participant.",
      "Suggests BJ favor access/relationship models that compound over time over one-and-done sales, whatever the eventual offer.",
      ["access over ownership"],
      ["network-distribution", "the-inevitable", "kelly", "access", "sharing", "compounding"]),
    C(4, INEV, "distribution",
      "Filtering: in abundance, attention is the scarce resource",
      "When everything is available, the bottleneck shifts from making or shipping copies to being found. Filtering (curation, recommendation, reputation, trust) becomes the scarce, valuable function, and human attention is the ultimate limited currency that everything else competes for.",
      "Treat attention and being-found as the real scarcity; invest in filtering, curation, and trust signals, not just in making more.",
      "Tells BJ that in a saturated field the constraint is discoverability and trust, so the leverage is in filtering and reputation, not volume.",
      ["attention is the", "scarcity of attention"],
      ["network-distribution", "the-inevitable", "kelly", "filtering", "attention", "discoverability"]),
    # ---- New Rules for the New Economy (Kelly) · 3 ----
    C(5, NEWR, "network-effects",
      "Increasing returns and the law of plenitude: value explodes with membership",
      "In a network economy value grows nonlinearly with the number of connected members (the network's worth rises faster than its size), and plenitude rather than scarcity drives worth, the more abundant and connected a standard becomes, the more valuable membership in it is. This inverts the industrial logic of scarcity.",
      "Pursue increasing-returns dynamics: things that get more valuable the more they are used, shared, or adopted.",
      "Points BJ toward whatever in his work compounds with adoption (a standard, a network, a body of work) rather than depletes with use.",
      ["increasing returns", "the network economy"],
      ["network-distribution", "new-rules", "kelly", "increasing-returns", "plenitude", "network-value"]),
    C(6, NEWR, "distribution",
      "Follow the free: generosity as a distribution engine",
      "Kelly's rule is that in a network economy the most valuable things trend toward free, so the operator should anticipate the free and position upstream and downstream of it, giving away the abundant to sell the scarce, and seeding ubiquity that later converts to relationship and value.",
      "Anticipate what is becoming free and give it away deliberately to build the ubiquity and relationships that monetize elsewhere.",
      "Helps BJ think about strategically giving work away to build reach and trust, while keeping the scarce/relational layer as the value capture.",
      ["Follow the Free"],
      ["network-distribution", "new-rules", "kelly", "follow-the-free", "generosity", "ubiquity"]),
    C(7, NEWR, "strategy",
      "Seek opportunities, not efficiencies; let go at the top",
      "In a fast-moving network economy, optimizing the existing process yields diminishing returns; the larger gains come from chasing new opportunities. Kelly also urges devolving control (letting go at the top) so the system can adapt faster than a command hierarchy allows.",
      "Spend scarce energy finding the next opportunity rather than perfecting the last process; push decisions outward so the system adapts.",
      "Reminds BJ in build-mode to weight exploration of new openings over premature optimization of an unproven offer.",
      ["opportunities, not efficiencies", "Let Go at the Top"],
      ["network-distribution", "new-rules", "kelly", "opportunities", "adaptation", "exploration"]),
    # ---- The Long Tail (Anderson) · 4 ----
    C(8, LONG, "distribution",
      "The Long Tail: selling less of more",
      "When shelves are infinite, demand that was invisible under scarcity becomes reachable; the many niches below the hits, summed together, can rival or exceed the head. The future of business is selling small quantities of an enormous variety, not only blockbusters.",
      "Aggregate niche demand: a wide catalog of small sellers can outweigh a narrow catalog of hits when distribution is unlimited.",
      "Suggests BJ's edge may lie in serving specific niches deeply rather than chasing one mass hit, since aggregated niches are real demand.",
      ["selling less of more", "long tail"],
      ["network-distribution", "long-tail", "anderson", "niches", "aggregate-demand", "infinite-shelf"]),
    C(9, LONG, "commercial-architecture",
      "Three forces: democratized production, democratized distribution, connected supply and demand",
      "Anderson attributes the long tail to three levers: cheaper tools democratize production (more makers), cheap aggregation democratizes distribution (everything available), and filters/search connect supply to demand by lowering the cost of finding. Together they make the tail commercially viable.",
      "Build on the three levers: lower the cost to produce, make everything available, and lower the cost for the right buyer to find you.",
      "Gives BJ a structural checklist for any connected offer: cheap to make, easy to access, easy to be found by the exact fit.",
      ["democratize the tools", "connect supply and demand"],
      ["network-distribution", "long-tail", "anderson", "production", "distribution", "filters"]),
    C(10, LONG, "media-business",
      "From the tyranny of the hit to filters as the new tastemakers",
      "Scarcity of shelf space once forced a hit-driven culture (the tyranny of the hit). With unlimited content, the gatekeeping function moves from pre-selection by distributors to post-hoc filtering (recommendations, reviews, algorithms) that guide attention through the abundance.",
      "When gatekeepers no longer ration access, recommendation and reputation become the tastemakers; earn placement in the filters.",
      "For BJ in a content-saturated visual field, this says the leverage is being surfaced by trusted filters and word of mouth, not winning a single gate.",
      ["the tyranny of", "help me find it"],
      ["network-distribution", "long-tail", "anderson", "hits-vs-niches", "filters", "tastemakers"]),
    C(11, LONG, "strategy",
      "The operating rule: make everything available and help me find it",
      "Anderson compresses long-tail strategy into two moves: provide near-unlimited choice, then provide powerful ways to navigate it. Choice without navigation overwhelms; navigation without choice starves. The pairing is what unlocks niche demand.",
      "Pair abundance with navigation: every expansion of choice must be matched by a better way to guide the right buyer to it.",
      "A concrete operating rule for BJ: whenever offering more, also build the path that leads the right person to the right thing.",
      ["make everything available"],
      ["network-distribution", "long-tail", "anderson", "choice", "navigation", "operating-rule"]),
    # ---- Free (Anderson) · 3 ----
    C(12, FREE, "commercial-architecture",
      "The economics of abundance: marginal cost toward zero and cross-subsidies",
      "When the marginal cost of an extra copy approaches zero, price is dragged toward zero too. Anderson maps the kinds of free (direct cross-subsidy, the three-party/ad model, freemium, and nonmonetary gift) as deliberate architectures where one part is given away to monetize another.",
      "Engineer free deliberately as a cross-subsidy: decide what you give away and exactly what paid value it pulls through.",
      "Helps BJ design any free tier as intentional architecture (what is free, who pays, what it pulls through), not as undercharging.",
      ["cross-subsidies", "marginal cost"],
      ["network-distribution", "free", "anderson", "freemium", "cross-subsidy", "abundance"]),
    C(13, FREE, "distribution",
      "Free as distribution: attention and reputation are the currencies",
      "Anderson argues that giving things away buys the two scarce currencies of an abundant economy, attention and reputation, which can later be converted into money, relationships, or paid demand. The gift economy and the money economy run side by side.",
      "Spend free to earn attention and reputation first; convert those scarce currencies into revenue downstream, not at the point of giving.",
      "Frames how BJ can use generous free work to accumulate attention and reputation that later convert, without expecting immediate payment.",
      ["attention and reputation", "gift economy"],
      ["network-distribution", "free", "anderson", "attention", "reputation", "gift-economy"]),
    C(14, FREE, "strategy",
      "When free works and when it does not: a conditional, not a default",
      "Free is powerful where marginal costs are near zero and a paid layer can be cross-subsidized, but Anderson is explicit that free is not a universal answer: it must be paired with a real revenue path, and in abundance some waste is acceptable because experimenting cheaply beats rationing.",
      "Use free only where marginal cost is near zero and a paying layer exists; otherwise it erodes value rather than building it.",
      "Keeps BJ from cargo-culting free: it is a conditional tool tied to cost structure and a paid layer, not a reflex.",
      ["free is not", "waste is good"],
      ["network-distribution", "free", "anderson", "conditional", "revenue-path", "experimentation"]),
    # ---- The Great Online Game (McCormick) · 1 ----
    C(15, GAME, "status",
      "The Great Online Game: building in public compounds status into opportunity",
      "McCormick frames the internet as one open, persistent game where showing up, sharing work, and building in public earn reputation and status that compound into real-world opportunities (jobs, capital, collaborators). Online points and offline outcomes increasingly converge for anyone who plays consistently.",
      "Play the long open game: consistent public work and reputation compound into opportunities that closed, private effort never reaches.",
      "Encourages BJ to treat consistent public sharing of his work as compounding reputation capital, while keeping it optional and identity-neutral.",
      ["The Great Online Game", "Win the Internet"],
      ["network-distribution", "great-online-game", "mccormick", "status", "build-in-public", "reputation"]),
    # ---- Synthesis (operator-doctrine) ----
    C(16, INEV, "operator-doctrine",
      "Synthesis: the connected-economy distribution toolkit and the optionality guardrail",
      "Across the five sources a single toolkit emerges: in an abundant connected economy, value migrates from copies to the un-copyable and to attention/filtering (Kelly); membership and sharing compound (increasing returns); free is a deliberate, conditional distribution and cross-subsidy strategy (Anderson); niche demand aggregates when you make everything available and help people find it; and consistent public work compounds status into opportunity (McCormick). Held as decision-support, the operator reads these as patterns for how any eventual offer reaches and compounds, not as a mandate to build a platform.",
      "Combine the levers: charge for the un-copyable, give away to earn attention and reputation, design free as cross-subsidy, aggregate niches with navigation, and let consistent public work compound; choose only what fits the actual stage.",
      "A single decision-support lens for BJ's distribution thinking that explicitly preserves optionality: apply the patterns that fit, ignore the rest, finalize nothing.",
      ["selling less of more", "Follow the Free"],
      ["network-distribution", "synthesis", "distribution-toolkit", "optionality", "operator-doctrine"]),
]

def sweep(o):
    if isinstance(o, str): return o.replace(DASH, " · ")
    if isinstance(o, list): return [sweep(x) for x in o]
    if isinstance(o, dict): return {k: sweep(v) for k, v in o.items()}
    return o

rows = [sweep(r) for r in rows]

# integrity asserts
assert len(rows) == 16, len(rows)
ids = [r["chunk_id"] for r in rows]
assert len(ids) == len(set(ids)), "dup chunk_id"
REQ = ["chunk_id","batch_id","source_title","source_file","author","domain","concept","summary","usable_principle","sniped_relevance","direct_quotes","tags"]
for r in rows:
    for k in REQ:
        assert k in r and r[k] not in (None, "", []), (r["chunk_id"], k)
    assert r["batch_id"] == BATCH
    blob = json.dumps(r, ensure_ascii=False)
    assert DASH not in blob, ("em-dash", r["chunk_id"])
    for q in r["direct_quotes"]:
        assert len(q.split()) <= 6, ("quote too long", r["chunk_id"], q)
    # source_file must resolve
    assert os.path.isfile(os.path.join(ROOT, EXTRACT, r["source_file"])), r["source_file"]
    # guardrail present
    assert "NOT a directive" in r["sniped_relevance"] and "CURRENT_OPERATOR_REALITY_BRIEF" in r["sniped_relevance"]

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

from collections import Counter
dd = Counter(r["domain"] for r in rows)
st = Counter(r["source_title"] for r in rows)
print(f"wrote {len(rows)} chunks -> {OUT}")
print("domains:", dict(dd))
print("sources:", dict(st))
print("longest quote words:", max(len(q.split()) for r in rows for q in r["direct_quotes"]))
