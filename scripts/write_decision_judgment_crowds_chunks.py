#!/usr/bin/env python3
"""Write DECISION_JUDGMENT_CROWDS_CHUNKS.jsonl · 14 curated chunks from the 4 net-new sources.
Existing domains only · decision-making anchor · no new domain. Em-dash swept + asserted.
Sensitive material held descriptively (group-reading / awareness), NOT culture-war posture or manipulation doctrine."""
import json, os

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/DECISION_JUDGMENT_CROWDS_CHUNKS.jsonl")
EXTRACT = "01_KNOWLEDGE_BASE/batches/decision_judgment_crowds_extracted"
DASH = chr(0x2014)
BATCH = "DECISION_JUDGMENT_CROWDS"

RM = ("The Righteous Mind", "Jonathan Haidt", "righteous_mind_haidt.txt")
COD = ("The Coddling of the American Mind", "Greg Lukianoff and Jonathan Haidt", "coddling_lukianoff_haidt.txt")
TB = ("The True Believer", "Eric Hoffer", "true_believer_hoffer.txt")
CR = ("The Crowd", "Gustave Le Bon", "the_crowd_lebon.txt")

GUARD = (
    " Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support / pattern-library only, "
    "NOT doctrine and NOT a directive. NOT a directive that BJ become a political commentator, a culture-war operator, "
    "a manipulator, a propagandist, an activist, a social theorist, an academic, or an ideology brand. The crowd, "
    "moral-psychology, and mass-movement material is translated into practical group-reading, incentive-reading, "
    "moral-language, social-risk, and coalition-awareness patterns for BJ's actual build-mode stage, held descriptively "
    "(to understand and navigate group dynamics) NOT as a manipulation playbook or a culture-war stance. "
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
    # ---- The Righteous Mind (Haidt) · 4 + synthesis ----
    C(1, RM, "decision-making",
      "Intuitions come first, strategic reasoning second (the elephant and the rider)",
      "Haidt's central model: moral and most everyday judgments are made fast and intuitively (the elephant), and conscious reasoning (the rider) mostly arrives afterward to justify the gut call, like a press secretary, not a judge. People rarely reason to a conclusion; they feel it, then build the case. This makes argument-by-evidence weak against a made-up mind.",
      "Expect people (and yourself) to decide intuitively and rationalize after; to move someone, speak to the intuition first, not the logic.",
      "Helps BJ read why a logically airtight pitch fails to move a client whose gut already decided, and why his own 'reasoned' calls may be post-hoc justifications worth re-checking.",
      ["intuitions come first", "the righteous mind"],
      ["decision-judgment-crowds", "righteous-mind", "haidt", "intuition-first", "motivated-reasoning", "elephant-and-rider"]),
    C(2, RM, "ethics",
      "Moral foundations: there is more to morality than harm and fairness",
      "Haidt maps several moral foundations people draw on in different proportions: care/harm, fairness/cheating, loyalty/betrayal, authority/subversion, sanctity/degradation (and liberty/oppression). Groups and individuals weight these differently, so what reads as 'obviously moral' to one person reads as irrelevant or offensive to another.",
      "Read the moral foundation someone is actually using before judging their position; disagreement is often different weightings, not bad faith.",
      "Gives BJ a vocabulary for why audiences/collaborators react differently to the same message, and how to frame in the moral language a given group actually values (loyalty, fairness, sanctity) rather than his own default.",
      ["moral foundations", "Care/harm"],
      ["decision-judgment-crowds", "righteous-mind", "haidt", "moral-foundations", "moral-language", "values"]),
    C(3, RM, "culture",
      "Groupish and the hive switch: we bind into teams and go blind",
      "Humans are, in Haidt's phrase, 90 percent chimp and 10 percent bee: mostly self-interested but able to flip a hive switch that dissolves the self into a group (a rally, a movement, a team). This groupishness builds powerful cooperation and equally powerful blindness to the group's own faults and to outsiders.",
      "Notice when a group (or you) has flipped into hive mode; cohesion rises but self-criticism and outside perception collapse.",
      "Helps BJ read the cohesion-vs-blindness tradeoff in any tribe, scene, or team he builds or joins, and stay aware when belonging starts to override honest judgment.",
      ["Groupish", "the hive switch"],
      ["decision-judgment-crowds", "righteous-mind", "haidt", "groupish", "hive-switch", "coalition"]),
    C(4, RM, "operator-doctrine",
      "Morality binds and blinds: moral capital and its cost",
      "Shared moral order (moral capital) is what lets a group trust, cooperate, and sustain itself without constant policing; it is genuinely valuable. But the same binding blinds members to the group's errors and to legitimate outside views. The operator lesson is to value cohesion while deliberately preserving dissent and outside input.",
      "Build enough shared values to bind a group, but engineer in dissent and outside checks so binding does not become blinding.",
      "For BJ, a caution as he forms any team or scene: cultivate shared standards (moral capital) but keep a channel for the uncomfortable outside view so the group does not lose contact with reality.",
      ["Moral capital", "binds and blinds"],
      ["decision-judgment-crowds", "righteous-mind", "haidt", "moral-capital", "cohesion-vs-dissent", "operator-caution"]),
    # ---- The Coddling of the American Mind (Lukianoff/Haidt) · 4 ----
    C(5, COD, "decision-making",
      "The three Great Untruths to refuse",
      "Lukianoff and Haidt name three falsehoods that wreck judgment: the Untruth of Fragility (what doesn't kill you makes you weaker), the Untruth of Emotional Reasoning (always trust your feelings), and the Untruth of Us Versus Them (life is a battle between good and evil people). Each is psychologically false and reliably makes people worse off when believed.",
      "Reject the three Untruths: treat hardship as potential growth, distrust raw feeling as fact, and resist sorting people into good vs evil camps.",
      "A direct self-check for BJ in a contentious info environment: when a stressor feels like proof of fragility, a feeling feels like a fact, or the world splits into us-vs-them, that is a distortion to override.",
      ["the three Great Untruths", "Emotional reasoning"],
      ["decision-judgment-crowds", "coddling", "lukianoff-haidt", "great-untruths", "fragility", "us-versus-them"]),
    C(6, COD, "systems-thinking",
      "Antifragility: people need stressors to grow",
      "Borrowing from Taleb, the authors argue people are antifragile: like an immune system or a muscle, they require challenge, friction, and exposure to grow strong, and overprotection (safetyism) produces the very fragility it tries to prevent. Shielding a system from all stress weakens it.",
      "Design for productive stressors, not total safety; removing all friction from a person, team, or process makes it weaker, not safer.",
      "Helps BJ treat difficulty (criticism, hard shoots, market pushback) as inputs that strengthen the operation, and avoid over-smoothing his own process into fragility.",
      ["antifragile", "Safetyism"],
      ["decision-judgment-crowds", "coddling", "lukianoff-haidt", "antifragility", "stressors", "safetyism"]),
    C(7, COD, "decision-making",
      "Name the cognitive distortion",
      "The book applies CBT's catalog of distortions to group discourse: catastrophizing, emotional reasoning, dichotomous (all-or-nothing) thinking, labeling, mind reading, and negative filtering. Naming the distortion is the first step to disarming it, individually and in a group's shared talk.",
      "When a thought (yours or a group's) spikes, name the specific distortion (catastrophizing, labeling, all-or-nothing) before acting on it.",
      "A practical hygiene tool for BJ: catch catastrophizing or all-or-nothing framing in his own self-talk and in collaborator dynamics, and re-state the situation accurately before deciding.",
      ["cognitive distortion", "catastrophizing"],
      ["decision-judgment-crowds", "coddling", "lukianoff-haidt", "cognitive-distortions", "cbt", "self-check"]),
    C(8, COD, "culture",
      "How environments manufacture us-versus-them and grievance",
      "The authors trace how institutional incentives and norms (call-out dynamics, identity-as-conflict framing, the reward structure for outrage) can amplify tribalism and fragility in a community, often from good intentions. The pattern is structural: the environment shapes the behavior, not just individuals.",
      "Read the incentive structure of an environment, not just its people; outrage and us-vs-them are often produced by what the system rewards.",
      "Helps BJ evaluate which platforms, scenes, and communities reward grievance and tribal conflict, and choose environments (and design his own) whose incentives reward building over outrage, without taking a political side.",
      ["us versus them", "call-out culture"],
      ["decision-judgment-crowds", "coddling", "lukianoff-haidt", "incentives", "tribalism", "environment-design"]),
    # ---- The True Believer (Hoffer) · 3 ----
    C(9, TB, "culture",
      "Mass movements recruit the frustrated who want to lose the self",
      "Hoffer argues mass movements draw their strength from the frustrated: people who want to escape a spoiled or meaningless self by merging into a collective and a holy cause. The specific doctrine matters less than the hunger for self-renunciation, which is why one movement's converts can switch to another.",
      "Read the underlying hunger (for belonging, meaning, escape from self) beneath a movement's stated cause; the cause is often interchangeable.",
      "Helps BJ understand why people attach intensely to causes/scenes/brands, and to build belonging honestly (real meaning, real contribution) rather than exploiting the hunger for self-loss.",
      ["mass movements", "the true believer", "holy cause"],
      ["decision-judgment-crowds", "true-believer", "hoffer", "frustration", "self-renunciation", "belonging"]),
    C(10, TB, "power",
      "Self-sacrifice and the techniques of unification",
      "Movements demand the individual merge into the collective; Hoffer details the techniques that produce willing self-sacrifice (a present made to seem worthless, a glorious future, a devil to hate, doctrine held as unquestionable, and dramatic ritual). These unify and mobilize, but at the cost of independent judgment.",
      "Recognize the unification techniques (a hated enemy, an unquestionable doctrine, a glorious future, ritual); where you see them, independent judgment is being traded for cohesion.",
      "A defensive-awareness lens for BJ: spot when a community is using these mechanics (a designated enemy, sacred doctrine) and keep his own judgment independent, without deploying them manipulatively himself.",
      ["self-sacrifice", "holy cause"],
      ["decision-judgment-crowds", "true-believer", "hoffer", "self-sacrifice", "unification", "independent-judgment"]),
    C(11, TB, "operator-doctrine",
      "The lifecycle of a movement: men of words, fanatics, practical men",
      "Hoffer describes a sequence: movements are prepared by men of words (who discredit the old order), brought to fire by fanatics (who thrive on action and destruction), and consolidated by practical men of action (who build a stable institution). Different personalities dominate each phase; the founder type rarely fits the consolidation phase.",
      "Match the personality to the phase: the energy that starts something is usually not the temperament that stabilizes it.",
      "For BJ, a pattern for any movement/scene/company arc: the disruptive starter, the zealous accelerant, and the steady builder are different roles, and knowing which phase you are in tells you what the work and the people need.",
      ["men of words"],
      ["decision-judgment-crowds", "true-believer", "hoffer", "movement-lifecycle", "phases", "roles"]),
    # ---- The Crowd (Le Bon) · 2 ----
    C(12, CR, "decision-making",
      "The collective mind: contagion, suggestibility, and thinking in images",
      "Le Bon's 1895 observation (read descriptively, as a period text): in a crowd, individuals can take on a collective mind, governed by sentiment rather than reason, where emotions and beliefs spread by contagion, people become suggestible, and ideas are received as vivid images rather than analyzed. The crowd is more impulsive and less critical than its members alone.",
      "Expect group settings to run on shared sentiment and contagion, not careful reasoning; a crowd judges by feeling and image, not argument.",
      "Helps BJ read why online and in-person crowds amplify emotion and spread belief fast, so he interprets viral sentiment as contagion rather than considered consensus, held as observation not a manipulation method.",
      ["the crowd", "contagion", "by images"],
      ["decision-judgment-crowds", "the-crowd", "le-bon", "collective-mind", "contagion", "sentiment-over-reason"]),
    C(13, CR, "power",
      "Prestige and the leaders of crowds: assertion and repetition over argument",
      "Le Bon observed that crowds follow prestige (an almost hypnotic authority born of success, status, or boldness) and respond to assertion, repetition, and contagion far more than to reasoned proof. This is presented here descriptively, as a caution about how influence actually operates in groups, not as an endorsement or a how-to for manipulation.",
      "Understand that group influence runs on prestige and repeated assertion, not evidence; recognize it to resist being swept, not to exploit it.",
      "A defensive-awareness pattern for BJ: notice when prestige and repetition (not substance) are driving a crowd's belief, so he evaluates on merit and builds genuine credibility rather than borrowed hype, never as a manipulation tactic.",
      ["prestige"],
      ["decision-judgment-crowds", "the-crowd", "le-bon", "prestige", "influence-mechanics", "defensive-awareness"]),
    # ---- Synthesis ----
    C(14, RM, "operator-doctrine",
      "Synthesis: the crowds and social-belief toolkit and the optionality guardrail",
      "Across the four sources a single decision-support toolkit emerges: intuition and feeling precede reason (Haidt), so groups judge by moral language and gut, not proof; shared morality binds and blinds, so cohesion needs engineered dissent; people are antifragile and need stressors, and the three Great Untruths corrupt judgment (Lukianoff/Haidt); mass movements recruit the frustrated with interchangeable holy causes and unification techniques (Hoffer); and crowds run on contagion, prestige, and images rather than argument (Le Bon). Held as decision-support, these are read to understand and navigate group, status, belief, and incentive dynamics, NOT to manipulate, take a culture-war side, or build an ideology brand.",
      "Read groups by their moral language, incentives, and belief-contagion; build belonging on real meaning with dissent preserved; treat stressors as growth; and recognize prestige/repetition influence so you resist it rather than wield it.",
      "A single decision-support lens for BJ's group/coalition/social-risk awareness that explicitly preserves optionality: apply the patterns that help him read and navigate people honestly, ignore the rest, finalize nothing, manipulate no one.",
      ["intuitions come first", "binds and blinds"],
      ["decision-judgment-crowds", "synthesis", "social-belief", "group-reading", "optionality", "operator-doctrine"]),
]

def sweep(o):
    if isinstance(o, str): return o.replace(DASH, " · ")
    if isinstance(o, list): return [sweep(x) for x in o]
    if isinstance(o, dict): return {k: sweep(v) for k, v in o.items()}
    return o

rows = [sweep(r) for r in rows]

assert len(rows) == 14, len(rows)
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
