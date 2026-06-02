#!/usr/bin/env python3
"""Write POSITIONING_DISRUPTION_CHUNKS.jsonl · 11 curated chunks from the 3 net-new sources.
Existing domains only · positioning anchor · no new domain. Em-dash swept + asserted."""
import json, os

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/POSITIONING_DISRUPTION_CHUNKS.jsonl")
EXTRACT = "01_KNOWLEDGE_BASE/batches/positioning_disruption_extracted"
DASH = chr(0x2014)
BATCH = "POSITIONING_DISRUPTION"

CHASM = ("Crossing the Chasm", "Geoffrey A. Moore", "crossing_the_chasm_moore.txt")
DILEMMA = ("The Innovator's Dilemma", "Clayton M. Christensen", "innovators_dilemma_christensen.txt")
MOM = ("The Mom Test", "Rob Fitzpatrick", "mom_test_fitzpatrick.txt")

GUARD = (
    " Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support / pattern-library only, "
    "NOT doctrine and NOT a directive. NOT a directive that BJ become a salesperson, a copywriter, "
    "an agency owner, a funnel builder, a marketing guru, a SaaS founder, or a disruption-theory consultant. "
    "The positioning, customer-conversation, market-selection, and structural-change methods are translated into "
    "practical patterns for BJ's actual build-mode stage. No final SNIPED, SNIPED Media, or BASEPLATE direction; "
    "photography remains one option among several. The Bible remains held separately and untouched."
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
    # ---- Crossing the Chasm (Moore) · 4 ----
    C(1, CHASM, "positioning",
      "The technology adoption life cycle and the chasm",
      "Moore maps adopters as innovators, early adopters (visionaries), early majority (pragmatists), late majority, and laggards. Between the visionaries and the pragmatists sits a chasm: the early market buys on vision and is forgiving, the mainstream buys on references and proof and is not. Most new things die in that gap because the pitch that won visionaries does not move pragmatists.",
      "Know which side of the chasm a buyer is on; the message and proof that win early believers do not win the cautious mainstream.",
      "Helps BJ see that early enthusiastic interest (from visionaries) does not predict mainstream demand, so he reads validation against which adopter type is actually buying.",
      ["the chasm", "technology adoption life cycle"],
      ["positioning-disruption", "crossing-the-chasm", "moore", "adoption-lifecycle", "chasm", "pragmatists"]),
    C(2, CHASM, "positioning",
      "Target a beachhead niche (the D-Day strategy)",
      "To cross the chasm, Moore says attack one narrow, winnable segment with overwhelming focus rather than spreading thin across many. Dominate that beachhead, become the obvious whole solution for it, and earn the references that pragmatists demand, before expanding.",
      "Win one narrow niche completely before broadening; a dominated small segment beats a thin presence across many.",
      "Points BJ toward picking one specific, winnable segment and becoming undeniable there first, rather than chasing a broad undifferentiated market.",
      ["target a niche", "head pin"],
      ["positioning-disruption", "crossing-the-chasm", "moore", "beachhead", "niche-focus", "segmentation"]),
    C(3, CHASM, "positioning",
      "The whole product: close the gap to what the pragmatist actually needs",
      "The generic product you ship is rarely the whole product the mainstream buyer needs to fully solve their problem (the surrounding services, integrations, guarantees, and proof). Moore argues you must assemble or orchestrate that whole product for the target segment, because pragmatists buy the complete solution, not the core artifact.",
      "Define and complete the whole product for one target segment; the buyer adopts a finished solution, not a raw capability.",
      "Reminds BJ that a strong core skill (e.g. an image, a tool) is not yet a whole product; the surrounding completeness is what a cautious buyer actually pays for.",
      ["whole product"],
      ["positioning-disruption", "crossing-the-chasm", "moore", "whole-product", "completeness", "segment-fit"]),
    C(4, CHASM, "distribution",
      "The bowling alley: expand segment by segment on references",
      "After the beachhead, Moore's bowling-alley image is to topple adjacent segments one at a time, each new segment won partly on the references and whole-product assets built in the last. Mainstream reach compounds through proof and word of mouth among pragmatists who trust peers in their own niche.",
      "Expand to adjacent segments deliberately, carrying references forward; pragmatist reach is earned segment by segment, not broadcast at once.",
      "Suggests BJ grow by moving into adjacent, reference-connected pockets rather than trying to reach everyone at once, letting proof carry across niches.",
      ["the bowling alley"],
      ["positioning-disruption", "crossing-the-chasm", "moore", "bowling-alley", "references", "go-to-market"]),
    # ---- The Innovator's Dilemma (Christensen) · 4 ----
    C(5, DILEMMA, "strategy",
      "Sustaining versus disruptive technologies",
      "Christensen distinguishes sustaining innovations (improve performance on the metrics mainstream customers already value) from disruptive ones (initially worse on those metrics but better on new dimensions like simplicity, price, or convenience). Incumbents reliably win sustaining battles and reliably lose disruptive ones, because the disruptor competes on a dimension the incumbent undervalues.",
      "Watch for offerings that are 'worse' on the established metric but better on a new one; that is where displacement starts, not in head-to-head improvement.",
      "Helps BJ recognize that a simpler/cheaper/more-convenient approach the establishment dismisses can be the real opening, rather than trying to out-perform incumbents on their own terms.",
      ["disruptive technologies", "sustaining technologies"],
      ["positioning-disruption", "innovators-dilemma", "christensen", "disruption", "sustaining-vs-disruptive", "metrics"]),
    C(6, DILEMMA, "systems-thinking",
      "Value networks and resource allocation: why good management misses disruption",
      "Christensen's deepest point is structural, not managerial failure: a firm's value network (its customers, cost structure, and the metrics that earn resources internally) filters what it can rationally pursue. Disruptive bets look small, low-margin, and serve unimportant customers, so well-run resource-allocation processes starve them. Listening closely to current customers actively steers incumbents away from disruption.",
      "Understand that the same processes that make an organization excellent at its current game make it structurally blind to disruptive shifts; the failure is systemic.",
      "Warns BJ that 'listen to your best customers' and 'fund the highest-margin work' are correct locally yet can blind him to a structurally different opportunity; he should watch the system, not just the customer.",
      ["value network", "listening to customers"],
      ["positioning-disruption", "innovators-dilemma", "christensen", "value-networks", "resource-allocation", "systems"]),
    C(7, DILEMMA, "commercial-architecture",
      "Low-end and new-market footholds",
      "Disruptions typically enter either at the low end (serving overserved customers more cheaply) or in a new market (serving non-consumers who lacked access), where incumbents have little incentive to defend. From that foothold the disruptor improves and moves up-market into the incumbent's core.",
      "Enter where the incumbents are happy to cede ground (the overserved low end or the non-consuming new market), then climb; do not attack the fortified center first.",
      "Suggests BJ look at people currently overserved or entirely unserved by existing options as the realistic entry point, rather than competing for the contested premium center.",
      ["low-end", "new market"],
      ["positioning-disruption", "innovators-dilemma", "christensen", "low-end", "new-market", "foothold"]),
    C(8, DILEMMA, "strategy",
      "Performance oversupply: when the basis of competition shifts",
      "When sustaining improvement outruns what mainstream customers can use (performance oversupply / overshoot), the basis of competition shifts from raw performance to convenience, reliability, price, and customization. The trajectory of what customers need is flatter than the trajectory of what producers keep adding, and disruptors meet the customer where they actually are.",
      "When everyone has overshot what customers need, compete on simplicity, reliability, convenience, or price, not on more features.",
      "Tells BJ that in a saturated, over-featured field the winning move is often less (clearer, simpler, more reliable), met at the customer's real need, not more capability.",
      ["overshoot", "trajectory"],
      ["positioning-disruption", "innovators-dilemma", "christensen", "overshoot", "basis-of-competition", "trajectory"]),
    # ---- The Mom Test (Fitzpatrick) · 2 ----
    C(9, MOM, "operator-process",
      "The Mom Test: ask about their life, not your idea",
      "Fitzpatrick's rule is that you can ask anyone (even your mom) about their life and get useful truth, as long as you never mention your idea. Ask about what they actually do, the last time they faced the problem, and what it cost them. Opinions about your idea (and predictions of future behavior) are worthless; concrete past behavior is data.",
      "Interview for facts about their past and present behavior, never for opinions about your idea; their enthusiasm is not evidence.",
      "Gives BJ a discipline for talking to potential buyers without fooling himself: probe real past behavior and cost, not whether people 'like' his concept.",
      ["Talk about their life", "opinions are worthless"],
      ["positioning-disruption", "mom-test", "fitzpatrick", "customer-discovery", "behavior-not-opinion", "validation"]),
    C(10, MOM, "operator-process",
      "Avoid bad data: deflect compliments, anchor fluff, push for commitment",
      "Three sources of false signal: compliments (feel good, mean nothing, deflect them), fluff (generic 'I would always / I usually' claims, anchor them to a specific recent instance), and ideas (capture the underlying problem, not the feature request). Real interest shows as commitment and advancement: giving up time, reputation, or money, and moving to a concrete next step.",
      "Measure interest by what people commit and advance (time, money, reputation, a real next step), not by what they say; treat compliments and fluff as noise.",
      "Keeps BJ from mistaking polite encouragement for demand; he reads commitment and advancement as the only trustworthy signal that an offer is wanted.",
      ["compliments", "commitment", "fluff"],
      ["positioning-disruption", "mom-test", "fitzpatrick", "bad-data", "commitment-and-advancement", "signal"]),
    # ---- Synthesis ----
    C(11, CHASM, "operator-doctrine",
      "Synthesis: the positioning, customer-truth, and disruption toolkit and the optionality guardrail",
      "Across the three sources a single decision-support toolkit emerges: position by targeting and fully serving one beachhead niche, then expand on references (Moore); learn what people truly need by interviewing for past behavior and commitment, not opinions (Fitzpatrick); and find openings where a simpler or new-market offering wins on a dimension incumbents undervalue, watching the system that blinds them (Christensen). Held as decision-support, these are read as patterns for choosing a market, validating it honestly, and spotting structural openings, not as a mandate to build a startup, an agency, or a disruption practice.",
      "Combine the levers: choose a narrow beachhead and complete the whole product, validate with the Mom Test (behavior and commitment, not praise), and look for a low-end or new-market opening on an undervalued dimension; apply only what fits the actual stage.",
      "A single decision-support lens for BJ's market-selection and validation thinking that explicitly preserves optionality: apply the patterns that fit, ignore the rest, finalize nothing.",
      ["cross the chasm", "the Mom Test"],
      ["positioning-disruption", "synthesis", "positioning", "customer-truth", "disruption", "optionality"]),
]

def sweep(o):
    if isinstance(o, str): return o.replace(DASH, " · ")
    if isinstance(o, list): return [sweep(x) for x in o]
    if isinstance(o, dict): return {k: sweep(v) for k, v in o.items()}
    return o

rows = [sweep(r) for r in rows]

assert len(rows) == 11, len(rows)
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
    assert os.path.isfile(os.path.join(ROOT, EXTRACT, r["source_file"])), r["source_file"]
    assert "NOT a directive" in r["sniped_relevance"] and "CURRENT_OPERATOR_REALITY_BRIEF" in r["sniped_relevance"]

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

from collections import Counter
print(f"wrote {len(rows)} chunks -> {OUT}")
print("domains:", dict(Counter(r["domain"] for r in rows)))
print("sources:", dict(Counter(r["source_title"] for r in rows)))
print("longest quote words:", max(len(q.split()) for r in rows for q in r["direct_quotes"]))
