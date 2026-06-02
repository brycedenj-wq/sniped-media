#!/usr/bin/env python3
"""Write HISTORICAL_BIOGRAPHY_CHUNKS.jsonl from the 2 Chernow biographies.

Grant + Washington: A Life (both Chernow). 12-field canonical schema. Existing
domains only (leadership / power / strategy / operator-doctrine / operator-process /
ethics / culture). NO new domain (character/statecraft/governance/politics/military/
biography NOT created). Per-source attribution, roughly equal weight. CURATED
representative leadership/power-pattern extraction, NOT exhaustive biography.
Distinguished from Titan / business-founder histories. Ethics kept honest, not
hagiographic. Every chunk carries the CURRENT_OPERATOR_REALITY_BRIEF reference +
identity-optionality guardrail (GUARD). Em-dash swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "HISTORICAL_BIOGRAPHY_CHUNKS.jsonl"
BATCH = "HISTORICAL_BIOGRAPHY"

GRANT = ("Grant", "Ron Chernow", "grant_chernow.txt")
WASH = ("Washington: A Life", "Ron Chernow", "washington_a_life_chernow.txt")

GUARD = (" Held as a pattern-library / decision-support lens, read against "
         "CURRENT_OPERATOR_REALITY_BRIEF: transferable patterns of leadership, power, and "
         "character under pressure, NOT a directive that BJ become a political, military, or "
         "public-leadership figure, and not hagiography (the flaws are read honestly). No final "
         "SNIPED, SNIPED Media, or BASEPLATE direction is set here; photography remains one "
         "option among several.")

# (source_tuple, concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
CHUNKS = [
    # ---------- Grant (Chernow) · 7 ----------
    (GRANT,
     "Quiet command: earned authority without self-promotion",
     "leadership",
     "Chernow's Grant leads without boasting: a lifelong aversion to self-promotion, content to "
     "let the wartime record speak rather than trumpet it. Plain dress, plain manner, no "
     "grandstanding; sophisticated people underrated him precisely because he refused to "
     "advertise himself, yet his results compounded his authority.",
     "Authority can be earned by results and understatement rather than self-promotion; letting "
     "the work speak can build more durable credibility than broadcasting it.",
     "A counter-pattern for BJ's posture: competence demonstrated quietly can out-build "
     "self-promotion; useful as a leadership lens, held interpretively, not a directive about "
     "any public role.",
     ["a lifelong aversion to boasting", "let the record speak"],
     ["quiet-authority", "understatement", "credibility", "leadership", "grant", "chernow"]),
    (GRANT,
     "Relentless persistence and the repeated comeback",
     "operator-doctrine",
     "Grant's arc is a chain of failures and comebacks: failed farmer, failed in business, "
     "branded a flop, then the general who would not stop pressing, then the ruined ex-president "
     "who wrote a masterwork memoir while dying of cancer. He repeatedly bounced back from "
     "adversity, mastering hard things over the long haul rather than in a single stroke.",
     "Durable success comes from persistence across repeated failure and the willingness to keep "
     "going under pressure; mastery is a long-haul accumulation, not a single win.",
     "A persistence lens for BJ's build-mode: repeated setbacks are compatible with eventual "
     "mastery if you keep pressing; held as a pattern, not a directive.",
     ["bounced back from adversity", "in the long haul"],
     ["persistence", "comeback", "resilience", "operator-doctrine", "grant", "chernow"]),
    (GRANT,
     "Strategic clarity and tenacity: grasp the whole and keep pressing",
     "strategy",
     "Grant's generalship combined a grasp of the entire theatre (coordinating armies toward one "
     "aim) with relentless forward pressure where predecessors had hesitated. His plain orders "
     "and refusal to retreat ('fight it out on this line') turned clarity plus tenacity into a "
     "war-winning strategy.",
     "Strategy is grasping the whole and then applying relentless, clear pressure toward the "
     "decisive aim, rather than cautious half-measures; clarity plus follow-through beats "
     "hesitation.",
     "A strategy lens for BJ: see the whole board, pick the decisive aim, and press it with "
     "clear, sustained action rather than hedging; held interpretively.",
     ["fight it out on this line", "plain orders"],
     ["strategy", "tenacity", "clarity", "grant", "chernow", "decisive-aim"]),
    (GRANT,
     "Magnanimity in victory: generous terms at Appomattox",
     "power",
     "At Appomattox, Grant gave Lee's defeated army strikingly generous terms (officers kept "
     "sidearms, men kept horses for spring planting, no humiliation), embodying 'let us have "
     "peace.' He used the moment of maximum power to reconcile rather than punish, a tolerance "
     "Chernow traces to his borderland upbringing.",
     "How you wield power at the moment of victory shapes what follows; magnanimity toward the "
     "defeated can build durable peace where humiliation would breed resentment.",
     "A power-handling lens for BJ: restraint and generosity at the moment of leverage often "
     "compound better than maximal extraction; held interpretively, not a directive.",
     ["let us have peace", "generous terms"],
     ["magnanimity", "victory", "reconciliation", "power", "grant", "chernow"]),
    (GRANT,
     "Using power for justice: Reconstruction and crushing the Klan",
     "ethics",
     "As president Grant used the power of his office for moral ends: creating the Justice "
     "Department, bringing thousands of anti-Klan indictments, and defending Black citizens' "
     "rights under the Reconstruction amendments when no southern jury would convict the night "
     "riders. His pursuit of justice was imperfect but his resolve to protect never wavered.",
     "Power held in office is a moral instrument; the test is whether it is spent protecting the "
     "vulnerable, even against fierce resistance and imperfect results.",
     "An ethics lens for BJ: whatever leverage one builds is a moral instrument; the honest "
     "question is what it is used to protect. Held interpretively, not a political directive.",
     ["his noble desire to protect them", "crush the Klan"],
     ["justice", "moral-courage", "reconstruction", "ethics", "grant", "chernow"]),
    (GRANT,
     "The honest man undone by misplaced trust",
     "operator-process",
     "Grant, scrupulously honest himself, was 'naive and artless in business' and trusted "
     "Ferdinand Ward, the 'Young Napoleon of Finance,' whose firm turned out to be a colossal "
     "fraud that ruined Grant and friends who had entrusted their savings. Personal integrity "
     "did not protect him in a domain he did not understand and did not vet.",
     "Personal integrity is not a substitute for competence and due diligence in an unfamiliar "
     "domain; trusting the wrong expert without verification is a recurring, ruinous failure mode.",
     "A practical caution for BJ: integrity does not replace vetting partners and understanding "
     "a domain before committing; verify before you trust capital or reputation to someone "
     "else's claimed expertise.",
     ["a colossal fraud", "naive and artless in business"],
     ["due-diligence", "misplaced-trust", "verification", "operator-process", "grant", "chernow"]),
    (GRANT,
     "The honest reckoning: a lifelong struggle with drink",
     "ethics",
     "Chernow treats Grant's alcoholism without moralizing or excusing: a chronic, recurring "
     "binge pattern that shadowed his career, that he openly struggled against (joining a "
     "temperance lodge), and that he largely mastered over the long haul. The biography refuses "
     "both the 'drunkard' caricature and the hagiographic denial.",
     "Honest assessment holds a person's real flaw and real mastery in the same frame, without "
     "caricature or denial; reckoning with a weakness squarely is itself a kind of strength.",
     "An honesty lens for BJ: assess yourself and others without caricature or hagiography; a "
     "flaw faced squarely and managed over time is part of a real record, not a disqualification.",
     ["a forbidden impulse he struggled", "mastery in the long haul"],
     ["honest-assessment", "flaw", "self-mastery", "ethics", "grant", "chernow"]),
    # ---------- Washington (Chernow) · 7 ----------
    (WASH,
     "Cultivated self-control: reserve as an instrument of authority",
     "leadership",
     "Washington was a man of 'granite self-control' and famous reserve, a high-strung temper "
     "mastered by reflection and habit. He deliberately set a dignified distance, learned to "
     "manage his body and face, and exploited his bottled-up intensity to exert his will. The "
     "composure was a constructed, effortful discipline, not a placid nature.",
     "Emotional self-command and a deliberate, dignified distance can be cultivated tools of "
     "authority; composure under pressure is built through discipline, not given.",
     "A leadership lens for BJ: composure and measured distance are trainable instruments, not "
     "innate traits; the discipline of self-command compounds authority. Held interpretively.",
     ["granite self-control", "his fabled reserve"],
     ["self-control", "composure", "reserve", "leadership", "washington", "chernow"]),
    (WASH,
     "The self-invented public figure: the constructed self vs the inner man",
     "culture",
     "Washington deliberately invented himself as the model English country gentleman and then "
     "the dignified republican leader, masking the most interior of the founders behind a public "
     "facade. Chernow distinguishes the constructed public figure from the turbulent private "
     "man, locating Washington's authority partly in that managed self-presentation within his "
     "era's status culture.",
     "Public standing is partly a deliberately constructed self-presentation; distinguishing the "
     "crafted public figure from the private person clarifies how reputation is built, without "
     "mistaking the myth for the man.",
     "A culture/identity lens for BJ (held strictly decision-neutral under the optionality "
     "guardrails): public identity is partly constructed, but this is an observation about how "
     "reputation works, NOT a directive to construct any particular SNIPED persona.",
     ["the self-invented", "self-made Americans"],
     ["self-invention", "public-self", "reputation", "culture", "washington", "chernow"]),
    (WASH,
     "The Fabian war of posts: survive by not losing",
     "strategy",
     "Against a stronger enemy, Washington adopted a 'war of posts': prolong, procrastinate, "
     "avoid a general engagement, and above all keep the Continental Army intact to wear Britain "
     "down. He won by not losing, preserving the force as the strategic asset rather than risking "
     "it on a decisive battle he could not afford.",
     "When weaker, the winning strategy is often to survive and preserve your core asset rather "
     "than seek a decisive confrontation; outlasting a stronger opponent can beat trying to "
     "beat them head-on.",
     "A strategy lens for BJ's build-mode (under-resourced, optionality-preserving): preserve "
     "the core, avoid bet-the-company confrontations, and outlast rather than over-commit. Held "
     "interpretively.",
     ["prolong, procrastinate", "a war of posts"],
     ["fabian-strategy", "preservation", "attrition", "strategy", "washington", "chernow"]),
    (WASH,
     "Cincinnatus: the deliberate relinquishing of power",
     "power",
     "Washington's defining act was giving power up: resigning his military commission rather "
     "than seizing rule, declining anything like a crown, and stepping down after two terms to "
     "set the precedent of voluntary transfer. The willingness to surrender power, more than its "
     "acquisition, founded his and the republic's authority.",
     "The disciplined, voluntary relinquishing of power can be the source of lasting authority "
     "and legitimacy; knowing when and how to let go is a rarer and higher skill than seizing.",
     "A power lens for BJ: holding power loosely and knowing when to step back can build more "
     "trust and legitimacy than accumulation; directly resonant with the brief's "
     "optionality-preserving, non-grasping posture. Held interpretively.",
     ["Cincinnatus", "stepped down"],
     ["relinquishing-power", "restraint", "legitimacy", "power", "washington", "chernow"]),
    (WASH,
     "Coalition command under scarcity: holding a fragile army together",
     "operator-doctrine",
     "For years Washington held together an under-resourced, under-paid, repeatedly-near-"
     "collapsing army through brutal winters, appalled at the lack of civilian support, yet "
     "keeping the coalition intact by sheer persistence, presence, and shared hardship. The "
     "achievement was less battlefield brilliance than not letting the enterprise dissolve.",
     "Leading a fragile, under-resourced effort is mostly the discipline of keeping it from "
     "dissolving: presence, persistence, and shared hardship hold a coalition together when "
     "resources do not.",
     "An operator lens for BJ as a solo/lean builder: much of leadership is simply refusing to "
     "let the thing collapse through scarce stretches; endurance and presence are the load-"
     "bearing skills. Held interpretively.",
     ["appalled by the lack of patriotism", "keep the army intact"],
     ["coalition", "endurance", "scarcity", "operator-doctrine", "washington", "chernow"]),
    (WASH,
     "Setting precedents and the restraint of power",
     "power",
     "Washington was acutely conscious that his every act set a precedent for a new republic, "
     "and he deliberately chose restraint, wary of how 'dangerous to civil liberty the precedent "
     "is of armed soldiers dictating terms.' He built durable norms by constraining his own "
     "power rather than testing its limits.",
     "When you are first, your behavior sets the norm; choosing restraint over the maximal "
     "exercise of power builds durable institutions and trust that precedent-breaking would "
     "erode.",
     "A lens for BJ: early choices set the pattern others inherit; deliberate restraint and "
     "norm-setting can matter more than any single maximal move. Held interpretively, not a "
     "directive about public office.",
     ["dangerous to civil liberty the precedent", "set a precedent"],
     ["precedent", "restraint", "norms", "power", "washington", "chernow"]),
    (WASH,
     "The flagrant contradiction: ideals and slaveholding",
     "ethics",
     "Chernow refuses hagiography: Washington professed liberty while holding hundreds of people "
     "in bondage at Mount Vernon, a 'world of flagrant contradictions' a contemporary called "
     "'cursed hypocrisy.' He freed his slaves only in his will, and the biography holds the "
     "greatness and the moral failure in the same honest frame.",
     "Honest assessment of any admired figure holds their achievement and their moral failure "
     "together; greatness does not erase complicity, and refusing hagiography is the precondition "
     "for learning from a life accurately.",
     "An ethics lens for BJ: read admired figures (and one's own influences) without "
     "hagiography, holding achievement and failure together; the honest record is the useful "
     "one. Held interpretively.",
     ["what cursed hypocrisy", "world of flagrant contradictions"],
     ["contradiction", "slavery", "honest-history", "ethics", "washington", "chernow"]),
    # ---------- Synthesis · 2 ----------
    (WASH,
     "Synthesis: the disciplined handling and relinquishing of power",
     "power",
     "Across both lives the through-line is restraint with power, not its accumulation: "
     "Washington surrendering command and office to found a republic's norms, and Grant offering "
     "magnanimous terms at the moment of total victory. Mature power is marked by what it "
     "declines to do, by self-imposed limits and generosity, more than by what it seizes.",
     "The mark of mature power is restraint: voluntary limits, generosity at the moment of "
     "leverage, and knowing when to let go build more durable authority than maximal extraction.",
     "For BJ, the dominant lesson of this lane is power-restraint and optionality (hold loosely, "
     "wield generously, know when to step back), read against CURRENT_OPERATOR_REALITY_BRIEF and "
     "held interpretively, not as a directive toward any public-leadership role.",
     ["Cincinnatus", "let us have peace"],
     ["restraint", "power", "synthesis", "washington", "chernow", "historical-biography"]),
    (GRANT,
     "Synthesis: the leadership pattern library and the optionality guardrail",
     "operator-doctrine",
     "HISTORICAL_BIOGRAPHY distills transferable patterns from two leaders: quiet earned "
     "authority, relentless persistence, strategic clarity, self-command, coalition endurance, "
     "the moral use and disciplined relinquishing of power, and honest reckoning with flaws. For "
     "SNIPED this is a decision-support pattern library decoupled from its political-military "
     "context, explicitly NOT a directive that BJ pursue political, military, or public-"
     "leadership life, and explicitly non-hagiographic (the drink, the fraud, the slaveholding "
     "are read honestly).",
     "Extract transferable leadership/power/operator patterns from historical lives while "
     "decoupling them from their political-military context and refusing hagiography; the value "
     "is the pattern, not the era or the office.",
     "This synthesizes the lane for BJ: a leadership/power/operator toolkit held as decision-"
     "support against CURRENT_OPERATOR_REALITY_BRIEF, with photography one option among several "
     "and no final SNIPED / SNIPED Media / BASEPLATE direction set.",
     ["letting the record speak", "one option among several"],
     ["synthesis", "leadership-patterns", "optionality", "operator-doctrine", "grant", "historical-biography"]),
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
    for i, (src, concept, domain, summary, principle, relevance, quotes, tags) in enumerate(CHUNKS, 1):
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
    forb = [d for d in ("character", "statecraft", "governance", "politics", "military",
                        "biography") if d in doms]
    print("forbidden domains present:", forb or "NONE")
    mx = max(len(q.split()) for r in lines for q in r["direct_quotes"])
    print("longest quote words:", mx)


if __name__ == "__main__":
    main()
