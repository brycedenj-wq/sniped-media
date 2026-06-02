#!/usr/bin/env python3
"""
Write BIOGRAPHY_FOUNDER_MEDIA_CHUNKS.jsonl · 22 chunks (20 source + 2 synthesis) across 6 sources.
12-field canonical schema. NO new domain · anchored on existing `founder-psychology` + operator-doctrine/
operator-process/strategy/brand/aesthetics/culture. Forbidden domains (biography/media-business/founder/
media) must NOT appear. Identity-optionality guardrail: founder/media arcs are PATTERN-LIBRARY only, NOT a
directive to manufacture a SNIPED myth; no final SNIPED / SNIPED Media / BASEPLATE direction. Em-dash sweep.
"""

import json
from pathlib import Path

OUT = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "BIOGRAPHY_FOUNDER_MEDIA_CHUNKS.jsonl"

DV = ("D.V.", "dv_vreeland.txt", "Diana Vreeland")
NF = ("No Filter", "no_filter_instagram_frier.txt", "Sarah Frier")
BR = ("Losing My Virginity", "losing_my_virginity_branson.txt", "Richard Branson")
KR = ("Grinding It Out", "grinding_it_out_kroc.txt", "Ray Kroc")
RA = ("That Will Never Work", "that_will_never_work_randolph.txt", "Marc Randolph")
MO = ("Made in Japan", "made_in_japan_morita.txt", "Akio Morita")

DG = "Pattern-library / decision-support only. These founder/media arcs are lenses, NOT a directive to manufacture a SNIPED founder myth; this does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction, and photography remains one option among several. Optionality preserved."

C = []
def add(src, domain, concept, summary, principle, relevance, quotes, tags):
    n = len(C) + 1
    title, sfile, author = src
    C.append({
        "chunk_id": f"BIOGRAPHY_FOUNDER_MEDIA_{n:03d}",
        "batch_id": "BIOGRAPHY_FOUNDER_MEDIA",
        "source_title": title, "source_file": sfile, "author": author,
        "domain": domain, "concept": concept, "summary": summary,
        "usable_principle": principle, "sniped_relevance": relevance,
        "direct_quotes": quotes, "tags": tags,
    })

# ---------------- D.V. (Vreeland · taste-making) · 4 ----------------
add(DV, "aesthetics",
    "Taste as a cultivated discipline: the trained eye",
    "Vreeland treats taste not as opinion but as a trained, deliberate faculty. The editor's job is to see what others miss, to know exactly why a thing works, and to allow a deliberate flaw ('a little bad taste') as the spark that keeps perfection from being dull. Taste is built, exercised, and applied with intent.",
    "Cultivate taste as a discipline: develop a precise eye, know why something works, and use a deliberate imperfection to give polished work life.",
    "Directly relevant to SNIPED's editorial/photography craft: taste is a trainable competitive faculty, not a vibe. " + DG,
    ["A little bad taste is like a nice splash of paprika"],
    ["taste", "the-eye", "editorial", "aesthetics", "vreeland"])

add(DV, "aesthetics",
    "Exaggeration and invention: fashion as fantasy, not reporting",
    "Vreeland insisted the editor's role is to conjure desire and fantasy, not to document what exists. She exaggerated, invented stories and trends, and gave readers something to aspire to rather than a mirror. Imagination and bold overstatement are the tools of the taste-maker.",
    "Lead with invention and aspiration, not documentation; give an audience a fantasy to move toward.",
    "An editorial-stance lens: SNIPED imagery can construct an elevated world rather than merely record one (consistent with the composite/world-building register). " + DG,
    [],
    ["exaggeration", "fantasy", "invention", "aesthetics", "vreeland"])

add(DV, "culture",
    "The editor as myth-maker and cultural authority",
    "As editor at Harper's Bazaar and Vogue, Vreeland did not follow culture, she set it, deciding what was beautiful and making it so by conviction and platform. Authority over taste came from a singular, unwavering point of view, consistently broadcast, that others learned to trust.",
    "Cultural authority is earned by holding and broadcasting a singular point of view with total conviction, until others orient to it.",
    "A myth-making lens connecting to the corpus's status/culture and category-design layers: own a POV and broadcast it consistently. " + DG,
    [],
    ["myth-making", "cultural-authority", "point-of-view", "culture", "vreeland"])

add(DV, "founder-psychology",
    "Self-creation: the operator as their own invention",
    "Vreeland built herself as deliberately as any magazine page, curating her persona, language, and legend so that the self became the masterwork. Personal inevitability, in her telling, is manufactured through relentless self-stylisation and refusal of the ordinary.",
    "Treat the public self as a deliberate creation; identity is built and curated, not merely revealed.",
    "A founder-psychology pattern (self-as-made-object), echoing BATCH_010's self-authorship · held as a lens, NOT a directive to manufacture a SNIPED persona. " + DG,
    [],
    ["self-creation", "persona", "inevitability", "founder-psychology", "vreeland"])

# ---------------- No Filter (Instagram) · 4 ----------------
add(NF, "aesthetics",
    "Aesthetic as the product: simplicity plus filters as the wedge",
    "Instagram won by making everyone's photos look good (filters) inside a ruthlessly simple app focused on one thing. The aesthetic upgrade was the product, and the constraint (square photos, few features) was a feature. Beauty and simplicity, not feature breadth, drove adoption.",
    "Make the aesthetic upgrade the product and ruthlessly constrain scope; beauty and simplicity can be the wedge.",
    "A product-taste lens for SNIPED: the aesthetic result IS the offer, and constraint sharpens it (echoes the locked register/environment-rotation discipline). " + DG,
    [],
    ["aesthetic-product", "simplicity", "constraint", "aesthetics", "instagram"])

add(NF, "strategy",
    "Community-first growth: curate the taste-makers",
    "Early Instagram grew by hand-curating: seeding the right creative early users, a suggested-user list, and personally cultivating a community whose taste set the tone. Growth came from deliberately shaping who was on the platform and what 'good' looked like, not from undifferentiated scale.",
    "Seed and curate the early taste-setting community deliberately; who you let define 'good' shapes everything downstream.",
    "A scene-density lens (depth before breadth): SNIPED can curate the specific cultural circle it serves rather than chase undifferentiated reach. " + DG,
    [],
    ["community", "curation", "seeding", "strategy", "instagram"])

add(NF, "founder-psychology",
    "Founder psychology under acquisition: autonomy vs scale",
    "Systrom and Krieger's arc turns on the tension between creative autonomy and the resources/scale of selling to Facebook. The book shows the founder's bargain: scale and protection in exchange for control, and the slow erosion of the original taste-led vision under growth pressure.",
    "Weigh the real price of scale: capital and reach often cost the autonomy and taste that built the thing.",
    "A cautionary founder-psychology lens for any future scale/partnership decision · kept as analysis, not a directive. " + DG,
    [],
    ["autonomy", "acquisition", "scale-tradeoff", "founder-psychology", "instagram"])

add(NF, "culture",
    "Visual culture and distribution: Instagram reshaped status and taste",
    "Instagram became the distribution layer for visual culture, reshaping how status, taste, aspiration, and the influencer economy work. Owning the surface where images are seen conferred power over what becomes desirable and who becomes visible.",
    "Distribution of images is power over taste and status; controlling the surface shapes what becomes desirable.",
    "A distribution lens tying SNIPED's imagery to the platforms that confer visibility and status (connects to the status/culture layer). " + DG,
    [],
    ["distribution", "visual-culture", "status", "culture", "instagram"])

# ---------------- Losing My Virginity (Branson) · 3 ----------------
add(BR, "brand",
    "Brand-as-attitude: one name across unrelated industries",
    "Virgin works as a brand of attitude (cheeky, customer-siding, adventurous) rather than a product category, which let Branson stretch one name across records, airlines, cola, and more. The brand is a promise of how it feels, not what it sells.",
    "Build a brand around an attitude and a feeling, not a category, so it can stretch across offerings.",
    "A brand-architecture lens: a SNIPED-style brand could be an attitude/standard that travels, rather than a single product · held as an option, not a decision. " + DG,
    [],
    ["brand-as-attitude", "brand-extension", "promise", "brand", "branson"])

add(BR, "brand",
    "Founder-as-brand: the showman is the marketing",
    "Branson made himself the marketing, using stunts, publicity, and visible personal risk to generate attention no ad budget could buy. The founder's persona became the cheapest and most durable distribution channel for the brand.",
    "When you lack budget, the founder's visible persona and bold acts can be the distribution channel.",
    "A founder-as-brand pattern · a lens on owned attention, explicitly NOT a directive to manufacture a SNIPED founder myth (see guardrail). " + DG,
    [],
    ["founder-as-brand", "publicity", "attention", "brand", "branson"])

add(BR, "strategy",
    "Protect the downside, then make it fun",
    "Branson takes bold, adventurous bets but structures them so a failure cannot sink the whole enterprise (protect the downside), and insists the work be fun, which sustains energy and attracts talent. Asymmetric bets plus enjoyment are the operating posture.",
    "Take bold bets only after capping the downside so you survive to play again; build the work to be enjoyable.",
    "Pairs with the corpus's risk/optionality layer (Marks, Housel): adventurous upside with a survivable floor · a posture lens, not a mandate. " + DG,
    ["protect the downside"],
    ["protect-the-downside", "asymmetric-bets", "fun", "strategy", "branson"])

# ---------------- Grinding It Out (Kroc) · 3 ----------------
add(KR, "founder-psychology",
    "The overnight success that took thirty years",
    "Kroc built McDonald's into a giant in his fifties after decades as a milkshake-machine salesman; the breakthrough rode on a long, unglamorous grind of persistence, recognising the right opportunity, and total commitment when it finally appeared. Inevitability was manufactured by showing up for years.",
    "Treat the long grind as the precondition for the breakout; persistence and readiness convert a late opportunity into inevitability.",
    "A founder-psychology / strategic-patience lens for a solo operator early in the arc · the reps precede the breakout. " + DG,
    [],
    ["persistence", "late-bloom", "readiness", "founder-psychology", "kroc"])

add(KR, "operator-process",
    "The system is the product: QSC and replicable standards",
    "McDonald's scaled not on a recipe but on a system: Quality, Service, Cleanliness enforced identically across franchises, with obsessive standardisation (fry timing, bun size) so any location delivered the same experience. The replicable operating system, not the burger, was the asset.",
    "Make the replicable system (standards, consistency) the real product, so quality survives scale and people.",
    "An operating-system lens: SNIPED's repeatable standards (the locked register, environment rotation, delivery SOP) are the scalable asset, not any single shoot. " + DG,
    ["Quality, Service, Cleanliness"],
    ["system-as-product", "qsc", "standardisation", "operator-process", "kroc"])

add(KR, "operator-doctrine",
    "Obsessive standards and details",
    "Kroc's discipline was relentless attention to operational detail and refusal to let standards slip, treating cleanliness and consistency as non-negotiable even at small scale. The standard is held the same on day one as at a thousand stores.",
    "Hold non-negotiable standards from the very first unit; details are the doctrine, not an afterthought.",
    "A standards-doctrine lens reinforcing EDGE_AND_OPERATING_DISCIPLINE: hold the bar from the first deliverable. " + DG,
    [],
    ["standards", "details", "consistency", "operator-doctrine", "kroc"])

# ---------------- That Will Never Work (Randolph · Netflix) · 3 ----------------
add(RA, "operator-process",
    "Nobody knows anything: test, do not predict",
    "Randolph's core lesson is that no one can predict what will work, so the discipline is to ship cheap tests fast and let reality decide, rather than debating ideas in the abstract. Ideas are nearly worthless until tested; the test is the only real information.",
    "Stop predicting and start testing: ship the cheapest experiment that returns real signal, and let it decide.",
    "A validation-discipline lens (pairs with the EDGE ICP/validation worksheets): SNIPED can test offers/directions cheaply rather than over-plan. " + DG,
    ["Nobody Knows Anything"],
    ["test-dont-predict", "experiments", "ideas-are-cheap", "operator-process", "netflix"])

add(RA, "strategy",
    "Focus and the willingness to pivot",
    "Early Netflix survived by dropping what worked-but-distracted (DVD sales) to focus on the rental/subscription model, and by being willing to abandon the original plan when the data demanded. Focus on the one thing that compounds, and pivot without ego.",
    "Cut even profitable distractions to focus on the model that compounds, and pivot without ego when evidence says so.",
    "A focus/pivot lens for the operator's direction decision: concentrate on the compounding line, stay willing to change it · held as a lens. " + DG,
    [],
    ["focus", "pivot", "subscription", "strategy", "netflix"])

add(RA, "founder-psychology",
    "Conviction under universal doubt",
    "The title is what everyone said; the arc is sustaining conviction and emotional resilience through relentless rejection and a near-failure launch. Founder psychology here is the capacity to keep going when credible people say it cannot work.",
    "Expect 'that will never work' and build the emotional resilience to keep testing through rejection.",
    "A resilience lens for an operator at the drawing-board stage facing doubt · pattern, not prescription. " + DG,
    [],
    ["conviction", "resilience", "rejection", "founder-psychology", "netflix"])

# ---------------- Made in Japan (Morita · Sony) · 3 ----------------
add(MO, "strategy",
    "Create demand, do not follow it",
    "Morita built the Walkman (and Sony's posture generally) on leading the public rather than asking it: market research could not have requested a product no one imagined. The job is to create demand by giving people something they did not know they wanted.",
    "Lead the public with what they cannot yet articulate, rather than only building to stated demand.",
    "A demand-creation lens (pairs with Play Bigger's category design): SNIPED can define a new experience rather than serve an existing brief · held as an option. " + DG,
    [],
    ["create-demand", "lead-the-public", "walkman", "strategy", "sony"])

add(MO, "brand",
    "Brand-name discipline: refuse the lucrative private-label deal",
    "Early Sony turned down large, profitable OEM/private-label orders that would have hidden its name, choosing slower growth to build the Sony brand as a global mark of quality. Protecting the name above near-term revenue was the long-game decision.",
    "Protect the brand name over near-term revenue; refuse work that builds someone else's mark instead of yours.",
    "A brand-ownership lens directly on the operator's 'avoid staying a service provider' question: own the name, do not just execute under others'. " + DG,
    [],
    ["brand-name", "long-game", "ownership", "brand", "sony"])

add(MO, "operator-doctrine",
    "Workmanship and the complementary co-founder",
    "Sony combined Morita's commercial and global instincts with Ibuka's engineering obsession, and held workmanship/quality as the non-negotiable foundation. Durable companies pair complementary founders and refuse to compromise on craft.",
    "Pair complementary strengths and treat craft quality as the non-negotiable base of everything you ship.",
    "A craft-and-partnership lens reinforcing SNIPED's craft-depth moat · and a note that complementary collaborators beat solo heroics. " + DG,
    [],
    ["workmanship", "complementary-founders", "craft", "operator-doctrine", "sony"])

# ---------------- Synthesis · 2 ----------------
add(DV, "founder-psychology",
    "SYNTHESIS: the operator-arc pattern library",
    "Read together, the six arcs show how individuals turn skill, narrative, capital, and timing into durable power: cultivate a trained eye and a singular POV (Vreeland), make the aesthetic the product and curate the early community (Instagram), build a brand of attitude and be the marketing (Branson), make the replicable system the asset and hold the long grind (Kroc), test instead of predict and pivot without ego (Randolph), and create demand while protecting the name (Morita). The common thread: durable power compounds from taste + system + narrative held over time.",
    "Combine a trained eye, a replicable system, a clear narrative, and patient timing; durable power compounds from these, not from any single move.",
    "A consolidated pattern library for the operator's arc · it supplies patterns to draw from, NOT a path to copy. " + DG,
    [],
    ["synthesis", "operator-arc", "pattern-library", "founder-psychology", "biography"])

add(RA, "strategy",
    "SYNTHESIS: pattern-library only, optionality preserved",
    "These biographies are inspiration and a pattern library, not a template. Taken literally they could push the operator to manufacture a founder myth, over-index on persona, or copy a specific path. Within the active identity-and-brand-optionality guardrails they are treated strictly as lenses that widen and pressure-test the option set, keeping SNIPED's direction reversible until the operator writes the fresh current brief.",
    "Use founder/media arcs to expand and stress-test options, not to manufacture a persona or copy a path; keep direction reversible.",
    "Explicitly preserves optionality: founder/media arcs are pattern-library only. No final SNIPED, SNIPED Media, or BASEPLATE direction; photography stays one option among several. " + DG,
    [],
    ["optionality", "pattern-library", "guardrail", "strategy", "biography"])

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
for bad in ("biography", "media-business", "founder", "media"):
    assert bad not in dist, f"FORBIDDEN domain used: {bad}"
print("forbidden domains (biography/media-business/founder/media) used: NONE")
print("em-dashes in output:", sum(json.dumps(c, ensure_ascii=False).count(EM) for c in C))
