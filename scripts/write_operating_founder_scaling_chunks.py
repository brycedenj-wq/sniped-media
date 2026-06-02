#!/usr/bin/env python3
"""Write OPERATING_FOUNDER_SCALING_CHUNKS.jsonl from the 2 curated hypergrowth/intensity books.

Blitzscaling (Hoffman/Yeh) + Amp It Up (Slootman). 12-field canonical schema. Existing
domains only (operator-doctrine / strategy / operator-process / leadership /
commercial-architecture / founder-psychology). NO new domain (startup / entrepreneurship /
founder / business / operations / scaling / product-development NOT created or used).
CURATED representative scaling/operator-tempo pattern extraction, NOT a chapter-by-chapter
summary. Held as a transferable operating tempo + scaling-judgment toolkit for BJ's actual
build-mode stage, NOT a command to hyperscale. Blitzscaling is held as CONDITIONAL and
dangerous (not default advice); Amp It Up's intensity is translated into raised operating
standards, NOT burnout cosplay. Bible held separately and untouched. Every chunk carries
the CURRENT_OPERATOR_REALITY_BRIEF reference + identity-optionality guardrail (GUARD).
Em-dash swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "OPERATING_FOUNDER_SCALING_CHUNKS.jsonl"
BATCH = "OPERATING_FOUNDER_SCALING"

BS = ("Blitzscaling", "Reid Hoffman and Chris Yeh", "blitzscaling_hoffman_yeh.txt")
AU = ("Amp It Up", "Frank Slootman", "amp_it_up_slootman.txt")

GUARD = (" Held as an operating / founder scaling pattern-library lens, read against "
         "CURRENT_OPERATOR_REALITY_BRIEF: a transferable model of operating tempo and scaling "
         "judgment, NOT a directive that BJ become a startup founder, a VC-style operator, a software "
         "CEO, or an agency owner, and NOT a mandate to raise venture capital, hyperscale, or build "
         "software. Blitzscaling is held as a CONDITIONAL and dangerous strategy (rational only when "
         "the prize is large and the competition intense), NOT default advice; Amp It Up's intensity "
         "is translated into raised operating standards, NOT burnout cosplay. The methods are decoupled "
         "from the startup/VC context that produced them and applied to BJ's actual build-mode stage. "
         "The Bible remains held separately and untouched. No final SNIPED, SNIPED Media, or BASEPLATE "
         "direction is set here; photography remains one option among several.")

# (source_tuple, concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
ROWS = [
    # ---------- Blitzscaling · 5 + synthesis ----------
    (BS,
     "Blitzscaling defined: prioritize speed over efficiency under uncertainty",
     "strategy",
     "Hoffman and Yeh define blitzscaling as driving extremely rapid growth by 'prioritizing speed "
     "over efficiency, even in the face of uncertainty.' It deliberately inverts the classic strategy "
     "of acting only when results are reasonably certain; it is, they stress, counterintuitive and "
     "uncomfortable, trading correctness and efficiency for raw speed when speed is the decisive "
     "variable.",
     "When speed is genuinely the decisive variable, deliberately trade efficiency and certainty for "
     "velocity; but recognize this inverts normal prudent strategy and is uncomfortable by design.",
     "A tempo lens for BJ: in the rare situations where being first/fast actually decides the outcome, "
     "accept some inefficiency and uncertainty to move faster; most of the time the classic "
     "efficiency-first approach is correct. Held interpretively.",
     ["speed over efficiency", "in the face of uncertainty"],
     ["speed-vs-efficiency", "velocity", "counterintuitive", "strategy", "blitzscaling", "operating-founder-scaling"]),
    (BS,
     "The conditional gate: blitzscaling is dangerous and rarely the right move",
     "operator-doctrine",
     "Hoffman and Yeh are explicit that blitzscaling is 'fraught with challenges' and risky: "
     "uncontrolled growth, they note, is the business equivalent of cancer. It becomes 'a rational, "
     "even optimal strategy' only under specific conditions, when the prize is large enough and the "
     "competition intense enough to justify the burn and chaos. Absent those conditions, blitzscaling "
     "is reckless, not admirable.",
     "Treat aggressive speed-at-all-costs as a conditional, dangerous bet to be justified case by "
     "case (is the prize large and the competition intense?), never as default advice; uncontrolled "
     "growth can kill the thing it is meant to build.",
     "A discipline lens for BJ: blitzscaling-style all-out speed is the exception, not the rule, and "
     "is dangerous; for a solo build-mode operator the default is controlled, efficient growth, and "
     "speed-at-all-costs needs a specific justification. Read as cautionary. Held interpretively.",
     ["fraught with challenges", "a rational, even optimal strategy"],
     ["conditional", "danger", "growth-discipline", "operator-doctrine", "blitzscaling", "operating-founder-scaling"]),
    (BS,
     "First-scaler advantage: the market logic that can justify the risk",
     "commercial-architecture",
     "The mechanism behind blitzscaling's payoff is 'first-scaler advantage': in markets with strong "
     "network effects, the first company to reach critical scale triggers a feedback loop (more "
     "users attract more users) that lets it dominate a winner-take-most market and lock out later "
     "entrants. The strategy only pays when the business model actually has such growth factors "
     "built in.",
     "Speed-led strategy only pays where the business model has built-in growth factors (network "
     "effects, winner-take-most dynamics); check whether your model actually has them before betting "
     "on being first to scale.",
     "A model-check lens for BJ: before any speed-led push, ask whether the work actually has "
     "winner-take-most or compounding-network dynamics that reward being first; a craft/service model "
     "usually does not, so the speed bet would not pay. Held interpretively.",
     ["first-scaler advantage", "winner-take-most market"],
     ["first-scaler-advantage", "network-effects", "market-logic", "commercial-architecture", "blitzscaling", "operating-founder-scaling"]),
    (BS,
     "Let fires burn: triage ruthlessly when everything is on fire",
     "operator-process",
     "In rapid growth there are always more problems than resources. Hoffman and Yeh's counterintuitive "
     "rule is to 'let fires burn', deliberately leave most problems unaddressed and fight only the few "
     "that would actually destroy the company. As one colleague puts it, what you say no to matters "
     "more than what you say yes to.",
     "Under overload, explicitly choose which problems to ignore and fight only the ones that are "
     "existential; ruthless triage (a deliberate 'no' to most fires) is the survival skill, not "
     "trying to fix everything.",
     "An overload lens for BJ as a solo operator: you cannot fix everything, so consciously decide "
     "which fires to let burn and protect attention for the few that are genuinely existential; "
     "saying no is the leverage. Held interpretively.",
     ["let fires burn", "say 'no' to is more important"],
     ["triage", "prioritization", "saying-no", "operator-process", "blitzscaling", "operating-founder-scaling"]),
    (BS,
     "The stages and transitions: the operator must change as the thing grows",
     "leadership",
     "Hoffman and Yeh frame growth as five stages (by organizational scale) crossed via a set of key "
     "transitions; each stage demands a radically different management approach and forces "
     "counterintuitive moves (hiring 'good enough' people, shipping imperfect products). The leader "
     "who cannot change his own role as the organization scales becomes the bottleneck.",
     "What works at one scale breaks at the next; the operator must consciously change his own role "
     "and methods at each stage rather than running the prior stage's playbook into the ground.",
     "A self-evolution lens for BJ: the way of working that fits a solo build-mode stage will need to "
     "change deliberately if anything scales; plan to re-define your own role at each transition "
     "rather than freezing in the current mode. Held interpretively.",
     ["five key stages", "key transitions"],
     ["growth-stages", "transitions", "self-evolution", "leadership", "blitzscaling", "operating-founder-scaling"]),
    # ---------- Amp It Up · 5 ----------
    (AU,
     "Raise your standards: the default bar is too low",
     "operator-doctrine",
     "Slootman's central move is to 'raise your standards': most organizations quietly accept a "
     "mediocre default bar, and the highest-leverage act of leadership is to ratchet expectations up, "
     "refuse 'good enough,' and insist on a world-class standard. Standards are a choice, and most "
     "people set them too low.",
     "Deliberately raise the standard you accept; the default bar drifts toward mediocre, and simply "
     "demanding markedly better work (of yourself first) is one of the highest-leverage moves "
     "available.",
     "A standards lens for BJ: the quality bar quietly sags toward 'good enough'; consciously raising "
     "your own standard (on the work, the craft, the output) is high-leverage and free. Held "
     "interpretively.",
     ["Raise Your Standards", "sharpen your focus"],
     ["raise-standards", "quality-bar", "anti-mediocrity", "operator-doctrine", "amp-it-up", "operating-founder-scaling"]),
    (AU,
     "Narrow the focus: spread too thin is the default failure",
     "strategy",
     "Slootman finds organizations are routinely 'spread too thinly across too many priorities.' His "
     "fix is to narrow the aperture, force the question 'if you could do just one thing this year, "
     "what would it be?' and ruthlessly concentrate energy there. Focus is created by subtraction, "
     "not by adding more initiatives.",
     "Concentrate energy on the one or two things that matter most and cut the rest; being spread "
     "thin across many priorities is the default failure mode, and focus is achieved by subtraction.",
     "A focus lens for BJ as a solo operator: the constant pull is to do too many things at once; "
     "force the 'one thing' question and subtract the rest, because spread-thin is the predictable "
     "way a solo build stalls. Held interpretively.",
     ["narrowing the aperture on priorities", "the one thing"],
     ["focus", "subtraction", "priorities", "strategy", "amp-it-up", "operating-founder-scaling"]),
    (AU,
     "Pick up the pace: tempo and urgency as a leadership lever",
     "operator-process",
     "Slootman treats organizational tempo as a deliberate lever: a leader's job on day one is to "
     "'pick up the pace,' increasing urgency, energy, and expectations so that decisions and "
     "execution move in days rather than quarters. Pace is set from the top and compounds; a slow "
     "default cadence quietly caps everything downstream.",
     "Set and raise the operating tempo deliberately; urgency is a choice that compounds, and a slow "
     "default cadence silently caps the output of everything downstream.",
     "A cadence lens for BJ: decide and ship on a fast clock (days, not quarters) by choice; the pace "
     "you set as the operator becomes the ceiling on everything, so raise it deliberately. Held "
     "interpretively (pace as standard, not frantic busywork).",
     ["Pick Up the Pace", "increasing urgency"],
     ["tempo", "urgency", "cadence", "operator-process", "amp-it-up", "operating-founder-scaling"]),
    (AU,
     "Declare war on incrementalism: a big mission, not burnout",
     "founder-psychology",
     "Slootman urges leaders to 'declare war on incrementalism' and to set a mission that is big "
     "(though not impossible) and not primarily about money, so that the energy comes from the scale "
     "of the ambition rather than from grinding. The intensity he prizes is a refusal of mediocre, "
     "timid defaults, not a glorification of overwork for its own sake.",
     "Aim at a mission big enough to pull real energy out of you and refuse timid incremental defaults; "
     "the intensity that matters is ambition and standards, not hours-as-virtue or burnout.",
     "A motivation lens for BJ: a mission worth the effort and a refusal of timid, incremental "
     "defaults generate real energy; read the intensity as a raised standard of ambition, NOT a "
     "directive to grind yourself out. Held interpretively.",
     ["war against incrementalism", "a great mission"],
     ["anti-incrementalism", "big-mission", "intensity-not-burnout", "founder-psychology", "amp-it-up", "operating-founder-scaling"]),
    (AU,
     "Hire drivers, not passengers: who is in the seats sets the pace",
     "leadership",
     "Slootman divides people into 'drivers' (who own outcomes and move the work forward) and "
     "'passengers' (who are carried along), and insists on staffing for drivers and getting the wrong "
     "people off the team. Tempo and standards are ultimately a function of who is in the seats; the "
     "wrong people cap both no matter how hard the leader pushes.",
     "Staff deliberately for owners who drive outcomes, and move the wrong people out; the team's "
     "tempo and standard are set by who is in the seats, not by exhortation.",
     "A people lens for BJ: as he adds collaborators, choose owners who drive the work, not passengers "
     "carried along; a single passenger caps the pace and standard regardless of how hard you push. "
     "Held interpretively.",
     ["drivers, not passengers", "the wrong people off"],
     ["drivers-vs-passengers", "ownership", "team-tempo", "leadership", "amp-it-up", "operating-founder-scaling"]),
    # ---------- synthesis · 1 ----------
    (BS,
     "Synthesis: the scaling/tempo toolkit and the optionality guardrail",
     "operator-doctrine",
     "Across both books a scaling/tempo toolkit emerges: treat all-out speed as a conditional, "
     "dangerous bet justified only by first-scaler dynamics (Blitzscaling), and otherwise raise "
     "standards, narrow focus, lift the operating tempo, refuse incrementalism, and staff for drivers "
     "(Amp It Up). It is held as an interpretive operating toolkit, NOT a command to hyperscale: "
     "blitzscaling stays conditional and dangerous, and Amp It Up's intensity is a raised standard, "
     "not burnout.",
     "Combine conditional speed-judgment (blitzscale only when the model and stakes warrant it) with "
     "the always-useful tempo disciplines (raise standards, narrow focus, increase urgency, refuse "
     "incrementalism, staff for drivers), held as decision-support and decoupled from the startup/VC "
     "context that produced it.",
     "This synthesizes the lane for BJ: a portable operating-tempo toolkit (default to controlled "
     "growth with raised standards, narrow focus, and a fast cadence; reserve all-out speed for the "
     "rare cases the model warrants) held as decision-support against CURRENT_OPERATOR_REALITY_BRIEF, "
     "NOT a directive to hyperscale, raise VC, or build software; blitzscaling stays conditional, "
     "intensity stays a standard not burnout; photography remains one option among several; no final "
     "SNIPED / SNIPED Media / BASEPLATE direction is set.",
     ["speed over efficiency", "one option among several"],
     ["synthesis", "scaling-tempo", "optionality", "operator-doctrine", "blitzscaling", "operating-founder-scaling"]),
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
