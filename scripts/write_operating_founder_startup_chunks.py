#!/usr/bin/env python3
"""Write OPERATING_FOUNDER_STARTUP_CHUNKS.jsonl from the 3 curated start/founder-reality books.

The Lean Startup (Ries) + The Hard Thing About Hard Things (Horowitz) + The Founder's
Dilemmas (Wasserman). 12-field canonical schema. Existing domains only (operator-doctrine /
operator-process / founder-psychology / strategy / leadership / commercial-architecture /
ethics). NO new domain (startup / entrepreneurship / founder / business / operations /
scaling / product-development NOT created or used). CURATED representative operating-founder
pattern extraction, NOT a chapter-by-chapter book summary. Held as a transferable operating
toolkit for BJ's actual build-mode stage, NOT a directive that BJ become a startup founder,
VC-style operator, software CEO, or agency owner, and NOT a mandate to raise VC, hyperscale,
or build software. Bible held separately and untouched. Every chunk carries the
CURRENT_OPERATOR_REALITY_BRIEF reference + identity-optionality guardrail (GUARD). Em-dash
swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "OPERATING_FOUNDER_STARTUP_CHUNKS.jsonl"
BATCH = "OPERATING_FOUNDER_STARTUP"

LS = ("The Lean Startup", "Eric Ries", "lean_startup_ries.txt")
HT = ("The Hard Thing About Hard Things", "Ben Horowitz", "hard_thing_horowitz.txt")
FD = ("The Founder's Dilemmas", "Noam Wasserman", "founders_dilemmas_wasserman.txt")

GUARD = (" Held as an operating / founder pattern-library lens, read against "
         "CURRENT_OPERATOR_REALITY_BRIEF: a transferable operating toolkit for building under "
         "uncertainty, NOT a directive that BJ become a startup founder, a VC-style operator, a "
         "software CEO, or an agency owner, and NOT a mandate to raise venture capital, hyperscale, "
         "or build software (the methods are decoupled from the startup/VC context that produced them "
         "and applied to BJ's actual build-mode stage). The Bible remains held separately and "
         "untouched. No final SNIPED, SNIPED Media, or BASEPLATE direction is set here; photography "
         "remains one option among several.")

# (source_tuple, concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
ROWS = [
    # ---------- The Lean Startup · 4 + synthesis ----------
    (LS,
     "Validated learning: measure progress in learning, not output",
     "operator-doctrine",
     "Ries argues a startup's real unit of progress is validated learning, demonstrating empirically "
     "what customers actually want, rather than shipped features or hours worked. Effort that does "
     "not produce learning about the real problem is waste, however busy it looks.",
     "Treat learning about what actually works as the unit of progress, not activity or output; "
     "effort that does not test a real assumption is waste dressed up as productivity.",
     "A discipline lens for BJ loading the backend: measure progress by what you have actually "
     "learned works (with real people/clients), not by how much you built; test assumptions cheaply "
     "before scaling them. Held interpretively.",
     ["validated learning"],
     ["validated-learning", "progress", "anti-waste", "operator-doctrine", "lean-startup", "operating-founder"]),
    (LS,
     "The minimum viable product and the build-measure-learn loop",
     "operator-process",
     "The core mechanic: build a minimum viable product (the smallest thing that lets you start "
     "learning), measure real behavior, learn, and iterate, minimizing total time through the "
     "Build-Measure-Learn loop. Track actionable metrics tied to the loop and refuse vanity metrics "
     "and the 'success theater' that flatter without informing a decision.",
     "Ship the smallest real test that produces learning, measure actual behavior on actionable "
     "metrics, and iterate fast; reject vanity metrics that look good but inform no decision.",
     "An operating lens for BJ: build the smallest real version that lets you learn from actual "
     "clients, measure what drives a decision (not flattering totals), and tighten the loop; speed "
     "through the loop beats polish in a vacuum. Held interpretively.",
     ["minimum viable product", "vanity metrics"],
     ["mvp", "build-measure-learn", "actionable-metrics", "operator-process", "lean-startup", "operating-founder"]),
    (LS,
     "Pivot or persevere: the disciplined strategic inflection",
     "strategy",
     "At regular decision points the operator must choose to pivot (a structured change in strategy "
     "while keeping what was learned) or persevere (double down on the current course). Ries frames "
     "this as a disciplined, evidence-based call, not an emotional one; the runway is really the "
     "number of pivots remaining, not the months of cash.",
     "Schedule honest pivot-or-persevere reviews against evidence; a pivot keeps the learning while "
     "changing the bet, and your real runway is how many more pivots you can afford, not just cash.",
     "A strategy lens for BJ: set deliberate checkpoints to decide whether to change the approach "
     "(pivot) or double down (persevere) based on what the evidence shows, rather than drifting on "
     "sunk cost or sentiment. Held interpretively.",
     ["pivot or persevere"],
     ["pivot-or-persevere", "strategic-inflection", "evidence-based", "strategy", "lean-startup", "operating-founder"]),
    (LS,
     "The engine of growth: the model that drives sustainable growth",
     "commercial-architecture",
     "Ries holds that sustainable growth runs on a specific engine of growth (sticky, viral, or "
     "paid), each with its own metrics and feedback loop; new customers come from the actions of "
     "past customers. The operator's job is to identify which engine applies and tune its few "
     "governing variables rather than chasing unrelated tactics.",
     "Identify the one engine that actually drives your growth and tune its governing variables; "
     "growth is a model to be understood and improved, not a grab-bag of disconnected tactics.",
     "A growth-architecture lens for BJ: name the actual engine behind any traction (referrals, "
     "repeat work, paid reach) and improve its few key variables, rather than scattering effort "
     "across unrelated growth tactics. Held interpretively.",
     ["the engine of growth"],
     ["engine-of-growth", "growth-model", "business-model", "commercial-architecture", "lean-startup", "operating-founder"]),
    # ---------- The Hard Thing About Hard Things · 5 ----------
    (HT,
     "The Struggle: leading when there are no good moves",
     "founder-psychology",
     "Horowitz names 'the Struggle', the lonely, frightening reality of building something out of "
     "nothing when every option looks bad. The one skill that matters most, he says, is the ability "
     "to focus and make the best move when there are no good moves, in the moments you most feel "
     "like hiding or quitting.",
     "Expect a Struggle phase where every option is bad; the decisive skill is staying focused and "
     "making the least-bad move rather than freezing, hiding, or quitting.",
     "A resilience lens for BJ in build-mode: the hardest stretches feel like there are no good "
     "moves; the work is to keep deciding and moving rather than freezing, and to know the Struggle "
     "is normal, not a verdict. Held interpretively.",
     ["no good moves"],
     ["the-struggle", "decision-under-pressure", "resilience", "founder-psychology", "hard-thing", "operating-founder"]),
    (HT,
     "Wartime vs peacetime CEO: match your mode to the situation",
     "leadership",
     "Horowitz distinguishes the peacetime operator (who grows the existing advantage, cares about "
     "process and morale, follows the rules) from the wartime operator (who fights for survival, "
     "violates norms when the company's life is at stake, and centralizes the decisive call). The "
     "failure mode is running the wrong mode for the moment.",
     "Read whether the situation is peacetime (expand, cultivate, follow process) or wartime (survive, "
     "concentrate the decision, break norms as needed) and run the matching mode; mismatching the "
     "mode to the moment is the error.",
     "A leadership lens for BJ: know whether the moment calls for patient cultivation or decisive "
     "survival-mode focus, and switch deliberately; do not run a calm-growth playbook in a crisis or "
     "vice versa. Held interpretively.",
     ["wartime CEO"],
     ["wartime-peacetime", "mode-switching", "situational-leadership", "leadership", "hard-thing", "operating-founder"]),
    (HT,
     "Take care of the people, the products, and the profits, in that order",
     "leadership",
     "Horowitz's inherited maxim: 'take care of the people, the products, and the profits, in that "
     "order', because if the company is not a good place to do great work, the products and profits "
     "will not follow. He pairs this with hiring for the right kind of ambition (ambition for the "
     "mission's success, not personal advancement) and for strength rather than lack of weakness.",
     "Put people first (a place where great work is possible), then products, then profits; and "
     "staff for ambition aimed at the mission and for real strengths, not the mere absence of "
     "weaknesses.",
     "A people lens for BJ as he builds a team/collaborators: protect the conditions for great work "
     "first, choose collaborators whose ambition is for the work's success, and select for genuine "
     "strengths over safe mediocrity. Held interpretively.",
     ["people, the products, and the profits", "the right kind of ambition"],
     ["people-first", "right-ambition", "hiring", "leadership", "hard-thing", "operating-founder"]),
    (HT,
     "CEOs should tell it like it is: face the fear and share the hard truth",
     "ethics",
     "Against the overwhelming pressure to be relentlessly positive, Horowitz argues the operator "
     "must tell it like it is, share bad news openly, because a shared, honestly-named problem can "
     "be solved by the whole team, while a hidden one festers and destroys trust. Candor is a "
     "discipline that builds the trust hard times require.",
     "Name problems honestly and early; sharing the hard truth lets the whole team help solve it and "
     "builds the trust that survives crises, whereas forced positivity hides the problem and erodes "
     "trust.",
     "An integrity lens for BJ: tell clients, collaborators, and yourself the truth about what is "
     "wrong rather than performing optimism; honest problem-naming is how problems actually get "
     "solved and trust is kept. Held interpretively.",
     ["tell it like it is"],
     ["candor", "honest-truth", "trust", "ethics", "hard-thing", "operating-founder"]),
    (HT,
     "Lead bullets, not silver bullets: there is no shortcut to a better product",
     "operator-doctrine",
     "Facing a faster competitor, Horowitz's team wanted a silver bullet; his engineer told him "
     "there were 'no silver bullets for this, only lead bullets', they simply had to build a better "
     "product, the hard way, with no escape hatch. They did the grinding work and won. The lesson: "
     "for the core problem there is usually no clever shortcut, only the hard work.",
     "When the core problem is real (your thing is not good enough yet), stop hunting for a clever "
     "shortcut and do the hard, direct work of making it genuinely better; that is the only way "
     "through.",
     "A discipline lens for BJ: when the honest issue is that the work is not yet good enough, the "
     "answer is lead bullets, the hard craft of making it better, not a marketing trick or a "
     "positioning shortcut. Held interpretively.",
     ["only lead bullets", "no silver bullets"],
     ["lead-bullets", "no-shortcut", "do-the-work", "operator-doctrine", "hard-thing", "operating-founder"]),
    # ---------- The Founder's Dilemmas · 5 ----------
    (FD,
     "Rich versus King: the wealth-versus-control trade-off",
     "founder-psychology",
     "Wasserman's central finding: founders repeatedly face a trade-off between wealth and control, "
     "between building maximum financial value (Rich) and keeping a grip on the steering wheel "
     "(King). Most cannot have both; the choices that grow value (raising money, hiring bosses, "
     "ceding equity) usually cost control, and founders who do not decide which they want make "
     "self-defeating choices.",
     "Decide consciously whether you are optimizing for wealth or for control, because most "
     "value-growing moves cost control and most control-keeping moves cap value; refusing to choose "
     "produces incoherent decisions.",
     "A self-knowledge lens for BJ: get explicit about whether you most want maximum value/scale or "
     "maximum control/autonomy, since the two pull apart; the brief's optionality-preserving, "
     "control-leaning posture is a deliberate Rich-vs-King stance, not an accident. Held interpretively.",
     ["Rich versus King", "between wealth and control"],
     ["rich-vs-king", "wealth-vs-control", "founder-motivation", "founder-psychology", "founders-dilemmas", "operating-founder"]),
    (FD,
     "The Three Rs: relationships, roles, and rewards",
     "operator-doctrine",
     "Wasserman frames the core founding-team decisions as 'the Three Rs', relationships (whom you "
     "build with), roles (who does and decides what), and rewards (how equity and pay are split), "
     "and shows they are interlocked: a weak choice on one destabilizes the others and the whole "
     "venture. Most founding-team blowups trace back to unexamined Three-Rs decisions.",
     "Treat relationships, roles, and rewards as one interlocked system to be decided deliberately "
     "and early; a careless choice on any one (who, who-decides, who-gets-what) destabilizes the "
     "rest.",
     "A partnering lens for BJ: before binding to any collaborator or partner, decide relationships, "
     "roles, and rewards explicitly and together, because vague early arrangements predictably blow "
     "up later. Held interpretively.",
     ["relationships, roles, and rewards"],
     ["three-rs", "founding-team", "partnership-design", "operator-doctrine", "founders-dilemmas", "operating-founder"]),
    (FD,
     "Equity splits and the cost of the quick handshake: early structure compounds",
     "operator-process",
     "Wasserman documents that founders who rush to split the equity equally in a quick early "
     "handshake, before roles and contributions are clear, create instability that surfaces later "
     "(the Pandora case: equal split plus deferred salaries heightened tensions and pushed out a "
     "cofounder). Early structural decisions have delayed but large effects.",
     "Slow down on equity and structural splits; provisional, contribution-aware, or vesting-based "
     "arrangements beat a fast equal handshake, because early structure compounds and is painful to "
     "undo.",
     "A structure lens for BJ: do not lock in equity, ownership, or revenue splits with collaborators "
     "in a hasty handshake; design them to reflect real contribution over time, because the early "
     "structure is hard to unwind. Held interpretively.",
     ["split the equity equally"],
     ["equity-splits", "early-structure", "compounding-decisions", "operator-process", "founders-dilemmas", "operating-founder"]),
    (FD,
     "Solo vs team, and when to found: career, market, and personal factors",
     "strategy",
     "Wasserman treats the pre-founding decisions as real strategic forks: whether to go solo or "
     "build a founding team (each with distinct advantages and risks), and when to commit, which is "
     "easy only when career, market, and personal factors are all favorable. Unfavorable factors on "
     "any axis create genuine dilemmas worth weighing, not ignoring.",
     "Treat the solo-vs-team and the timing decision as deliberate strategic choices weighed against "
     "career, market, and personal readiness, rather than defaulting into them on enthusiasm.",
     "A timing/structure lens for BJ: weigh solo vs collaborator-based building and the readiness of "
     "career, market, and personal factors deliberately; the brief's solo build-mode is a defensible "
     "stance, not an unconsidered default. Held interpretively.",
     ["career, market, and personal factors"],
     ["solo-vs-team", "timing", "founding-decision", "strategy", "founders-dilemmas", "operating-founder"]),
    (FD,
     "Founders' biases: passion and optimism breed shortsighted decisions",
     "founder-psychology",
     "Wasserman warns that founders' natural inclinations, 'passion, optimism, and conflict "
     "avoidance', lead to shortsighted decisions: over-trusting people, skipping hard structural "
     "conversations, and assuming the best. The same drive that makes founding possible is also the "
     "predictable source of its avoidable mistakes.",
     "Treat your own passion, optimism, and conflict-avoidance as known bias sources; deliberately "
     "force the hard conversations and structural decisions your enthusiasm wants to skip.",
     "A self-awareness lens for BJ: the optimism and conflict-avoidance that fuel building also "
     "produce predictable blind spots (over-trust, skipped hard talks); name them and force the "
     "uncomfortable decisions early. Held interpretively.",
     ["passion, optimism, and conflict avoidance"],
     ["founder-bias", "optimism", "conflict-avoidance", "founder-psychology", "founders-dilemmas", "operating-founder"]),
    # ---------- synthesis · 1 ----------
    (LS,
     "Synthesis: the operating-founder startup toolkit and the optionality guardrail",
     "operator-doctrine",
     "The three books yield a coherent build-under-uncertainty toolkit: measure progress in validated "
     "learning and tighten the build-measure-learn loop (Ries), decide pivot-or-persevere on "
     "evidence, lead through the Struggle with candor and lead bullets rather than silver ones "
     "(Horowitz), and design relationships/roles/rewards and the Rich-vs-King stance deliberately "
     "while guarding against founder optimism bias (Wasserman). It is held as an interpretive "
     "operating toolkit, NOT a directive to run a venture-backed software startup.",
     "Combine validated learning, disciplined pivot/persevere, candid wartime/peacetime leadership, "
     "and deliberate founding-structure + self-knowledge into one build-under-uncertainty toolkit, "
     "held as decision-support and decoupled from the startup/VC context that produced it.",
     "This synthesizes the lane for BJ: a portable build-mode operating toolkit (learn fast, decide "
     "on evidence, lead with candor and hard work, structure partnerships deliberately, know your "
     "Rich-vs-King stance) held as decision-support against CURRENT_OPERATOR_REALITY_BRIEF, NOT a "
     "directive to become a startup founder, raise VC, hyperscale, or build software; photography "
     "remains one option among several; no final SNIPED / SNIPED Media / BASEPLATE direction is set.",
     ["validated learning", "one option among several"],
     ["synthesis", "operating-toolkit", "optionality", "operator-doctrine", "lean-startup", "operating-founder"]),
]


def sweep(o):
    if isinstance(o, str):
        return o.replace(chr(0x2014), " · ")
    if isinstance(o, list):
        return [sweep(x) for x in o]
    if isinstance(o, dict):
        return {k: sweep(v) for k, v in o.items()}
    return o


def main():
    lines = []
    for i, (src, concept, domain, summary, principle, relevance, quotes, tags) in enumerate(ROWS, 1):
        title, author, sfile = src
        rec = {
            "chunk_id": f"{BATCH}_{i:03d}",
            "batch_id": BATCH,
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": relevance + GUARD,
            "direct_quotes": quotes,
            "tags": tags,
        }
        lines.append(sweep(rec))

    text = "\n".join(json.dumps(r, ensure_ascii=False) for r in lines) + "\n"
    assert chr(0x2014) not in text, "em-dash leaked"
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {len(lines)} chunks -> {OUT}")
    doms, srcs = {}, {}
    for r in lines:
        doms[r["domain"]] = doms.get(r["domain"], 0) + 1
        srcs[r["source_file"]] = srcs.get(r["source_file"], 0) + 1
    print("domains:", json.dumps(doms, ensure_ascii=False))
    print("per-source:", json.dumps(srcs, ensure_ascii=False))
    forb = [d for d in ("startup", "entrepreneurship", "founder", "business",
                        "operations", "scaling", "product-development") if d in doms]
    print("forbidden domains present:", forb or "NONE")
    mx = max(len(q.split()) for r in lines for q in r["direct_quotes"])
    print("longest quote words:", mx)


if __name__ == "__main__":
    main()
