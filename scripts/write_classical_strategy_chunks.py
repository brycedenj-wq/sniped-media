#!/usr/bin/env python3
"""Write CLASSICAL_STRATEGY_CHUNKS.jsonl from the 4 curated classical-strategy texts.

The Prince (Machiavelli) + On War (Clausewitz) + Meditations (Marcus Aurelius) +
Landmark Caesar. 12-field canonical schema. Existing domains only (strategy / power /
leadership / operator-doctrine / mindset / ethics / mental-models / decision-making).
NO new domain (philosophy/statecraft/war/history/politics/military/empire NOT created).
Per-source attribution. CURATED representative strategy/operator-pattern extraction,
NOT exhaustive. Machiavelli/Clausewitz read as pattern libraries NOT directives for
ruthless tactics; Meditations treated as SECULAR operator-discipline, not a faith lane.
Every chunk carries the CURRENT_OPERATOR_REALITY_BRIEF reference + identity-optionality
guardrail (GUARD). Em-dash swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "CLASSICAL_STRATEGY_CHUNKS.jsonl"
BATCH = "CLASSICAL_STRATEGY"

PRINCE = ("The Prince", "Niccolo Machiavelli", "the_prince_machiavelli.txt")
ONWAR = ("On War", "Carl von Clausewitz", "on_war_clausewitz.txt")
MED = ("Meditations", "Marcus Aurelius", "meditations_marcus_aurelius.txt")
CAESAR = ("The Landmark Julius Caesar (Web Essays)", "Robert B. Strassler (ed.)", "landmark_caesar.txt")

GUARD = (" Held as a strategy / power / operator pattern-library lens, read against "
         "CURRENT_OPERATOR_REALITY_BRIEF: a transferable model of judgment under "
         "uncertainty, NOT doctrine and NOT a directive (Machiavelli and Clausewitz are "
         "read as pattern libraries, not a mandate for ruthless power tactics; Meditations "
         "is read as secular operator-discipline, not a faith lane). No final SNIPED, SNIPED "
         "Media, or BASEPLATE direction is set here; photography remains one option among several.")

# (source_tuple, concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
CHUNKS = [
    # ---------- The Prince (Machiavelli) · 4 ----------
    (PRINCE,
     "Feared versus loved: be feared without being hated",
     "power",
     "Machiavelli argues that if a leader cannot be both loved and feared, it is safer to be "
     "feared, because love is held by a bond of obligation that self-interested people break "
     "when it suits them, while fear is sustained by dread of consequences. The crucial caveat: "
     "never become hated, which fear-without-fairness produces.",
     "Reliable influence rests on credible consequences and respect more than on goodwill alone, "
     "but it must never tip into being hated; calibrated, fair firmness outlasts mere likeability.",
     "A power-dynamics lens for BJ: durable standing with clients/partners comes from credible "
     "follow-through and respect, not only being liked, while never crossing into resentment. "
     "Read as a pattern, not a directive to rule by fear.",
     ["safer to be feared than loved", "avoid being hated"],
     ["feared-vs-loved", "authority", "respect", "power", "machiavelli", "the-prince"]),
    (PRINCE,
     "The fox and the lion: combine cunning with force",
     "power",
     "Machiavelli's image of leadership: one must be a fox to recognize traps and a lion to "
     "frighten off wolves; neither alone suffices. Pure force is blind to snares; pure cunning "
     "cannot defend itself. The effective operator holds both perception and the capacity to act "
     "decisively.",
     "Pair shrewd perception (spotting traps, reading incentives) with the capacity to act "
     "forcefully; cleverness without strength is exposed, and strength without cleverness is led "
     "into snares.",
     "A judgment lens for BJ: combine reading the real incentives/risks (the fox) with the "
     "willingness to act decisively when it counts (the lion); neither pattern alone is enough. "
     "Held interpretively, not a directive.",
     ["a fox to recognize snares", "the lion cannot defend himself"],
     ["fox-and-lion", "cunning", "force", "power", "machiavelli", "the-prince"]),
    (PRINCE,
     "Rely on your own arms, not mercenaries",
     "strategy",
     "Machiavelli's recurring warning: a prince who depends on mercenary or borrowed forces is "
     "never secure, because they are loyal to pay, not to him, and fail at the decisive moment. "
     "Lasting power rests on one's own arms, capabilities under one's own control.",
     "Build and control your own core capability rather than depending on rented or borrowed "
     "leverage that is loyal only to its own interest and absent when it matters most.",
     "Directly relevant to BJ loading the backend: own the core capability (skills, systems, "
     "audience) rather than depending on rented platforms or hired-gun leverage that disappears "
     "under pressure. Held interpretively.",
     ["with his own arms", "mercenaries are useless"],
     ["own-arms", "self-reliance", "capability", "strategy", "machiavelli", "the-prince"]),
    (PRINCE,
     "Realpolitik read honestly: effect over intention, timing of hard and soft moves",
     "ethics",
     "Machiavelli's most notorious teaching is descriptive realism: judge actions by their "
     "effects in a world as it is, inflict necessary hard measures all at once so they are soon "
     "over, and spread benefits out over time so they are savored. Chernow-style honest reading "
     "holds this as analysis of how power actually behaves, not an endorsement of cruelty.",
     "Understand how power actually operates (effects matter, hard moves concentrated, benefits "
     "spread out) as analysis, while choosing your own ethics deliberately rather than adopting "
     "ruthlessness as a value.",
     "An honest-realism lens for BJ: see clearly how incentives and power work so you are not "
     "naive, but this is explicitly NOT a directive to act ruthlessly; the realpolitik is read "
     "as description, and BJ's own ethics remain his choice.",
     ["inflicted all at once", "Fortune is a woman"],
     ["realpolitik", "effects-over-intention", "honest-realism", "ethics", "machiavelli", "the-prince"]),
    # ---------- On War (Clausewitz) · 4 ----------
    (ONWAR,
     "War as the continuation of politics by other means",
     "strategy",
     "Clausewitz's central dictum: war is not an end in itself but an instrument of policy, the "
     "continuation of politics by other means. Every military act must serve the political "
     "purpose, and losing sight of the end corrupts the means.",
     "Any aggressive action or campaign must stay subordinate to the actual objective; tactics "
     "divorced from the real purpose become self-defeating. Keep the end in view at all times.",
     "A strategy lens for BJ: every tactic (a launch, a pitch, a build) must serve the actual "
     "objective, not become an end in itself; means subordinate to purpose. Held interpretively.",
     ["continuation of politics by other means", "war is a duel"],
     ["ends-and-means", "purpose", "policy", "strategy", "clausewitz", "on-war"]),
    (ONWAR,
     "Friction: why everything in war is harder than it looks",
     "mental-models",
     "Clausewitz's concept of friction: 'everything in war is simple, but the simplest thing is "
     "difficult.' Countless small frictions (delay, confusion, fatigue, weather, miscommunication) "
     "accumulate to make plans go awry. The competent commander expects friction and builds "
     "tolerance for it rather than assuming the plan executes cleanly.",
     "Plans degrade in execution through accumulated small frictions; build slack, simplicity, "
     "and tolerance for things going wrong rather than assuming flawless execution.",
     "A planning lens for BJ: expect friction (delays, confusion, things breaking) and design "
     "simple, robust plans with slack rather than brittle ones that assume everything goes right. "
     "Held interpretively.",
     ["everything in war is simple", "the simplest thing is difficult"],
     ["friction", "execution-gap", "robustness", "mental-models", "clausewitz", "on-war"]),
    (ONWAR,
     "The center of gravity: concentrate against the decisive point",
     "mental-models",
     "Clausewitz's Schwerpunkt: identify the enemy's center of gravity, the hub of all power and "
     "movement, and concentrate force against it rather than dispersing effort. Strategy is "
     "finding the one decisive point where pressure collapses the whole.",
     "Find the single decisive point (the center of gravity) and concentrate resources there "
     "rather than spreading effort thinly across many fronts.",
     "A focus lens for BJ: identify the one decisive lever in any situation and concentrate "
     "resources on it rather than diffusing across many small efforts. Held interpretively.",
     ["centre of gravity", "the Schwerpunkt"],
     ["center-of-gravity", "concentration", "focus", "mental-models", "clausewitz", "on-war"]),
    (ONWAR,
     "The culminating point and the strength of the defensive",
     "strategy",
     "Clausewitz warns that an attack has a culminating point beyond which it over-extends and "
     "weakens, and that defence is intrinsically the stronger form of fighting. Knowing when an "
     "advance has reached its limit, and when to hold rather than push, is a mark of strategic "
     "judgment under uncertainty.",
     "Aggression has a culminating point past which it over-extends; recognize when to consolidate "
     "rather than push, and respect that holding a strong position can beat over-reaching.",
     "A judgment lens for BJ: know when a push (a launch, a scale-up) has reached its culminating "
     "point and consolidating beats over-extending; over-reach is a common failure mode. Held "
     "interpretively.",
     ["the culminating point", "defence is the stronger form"],
     ["culminating-point", "overreach", "consolidation", "strategy", "clausewitz", "on-war"]),
    # ---------- Meditations (Marcus Aurelius) · 4 ----------
    (MED,
     "The dichotomy of control: govern your judgments, not externals",
     "mindset",
     "Marcus Aurelius's Stoic core: 'all is but opinion,' and 'it is in thy power absolutely to "
     "exclude all manner of conceit.' What disturbs us is our judgments about events, not the "
     "events themselves; the one thing fully in our power is our own response and assent.",
     "Direct energy to what is actually in your control (your judgments, choices, and response) "
     "and release attachment to outcomes and others' opinions that are not.",
     "A composure lens for BJ in build-mode uncertainty: spend energy on the controllable (the "
     "work, the response) and release what is not (market reactions, others' opinions). Read as "
     "secular operator-discipline, not faith.",
     ["all is but opinion", "it is in thy power"],
     ["dichotomy-of-control", "stoicism", "composure", "mindset", "marcus-aurelius", "meditations"]),
    (MED,
     "Duty and the present: do the work in front of you",
     "operator-doctrine",
     "Marcus returns repeatedly to acting according to nature, continuing his course through "
     "right action, and confining attention to the present task rather than being scattered by "
     "past or future. The discipline is to do the work in front of you, well, now.",
     "Concentrate on the present task and do it well, rather than dissipating attention across "
     "what has passed or what might come; sustained right action compounds.",
     "A focus lens for BJ: confine attention to the present task and execute it well rather than "
     "being scattered by anxiety about outcomes; the discipline of the next right action. Held "
     "interpretively, secular.",
     ["I continue my course", "according to nature"],
     ["present-focus", "duty", "discipline", "operator-doctrine", "marcus-aurelius", "meditations"]),
    (MED,
     "Nothing external can hinder the inner citadel",
     "mindset",
     "Marcus holds that 'no man can hinder thee to live as thy nature doth require': obstacles "
     "and others' actions can block external aims but cannot compel your character or your "
     "response. The inner citadel of judgment and will remains yours regardless of circumstance.",
     "Circumstances and other people can obstruct outcomes but cannot force your character or "
     "response; the inner ground of judgment stays under your control.",
     "A resilience lens for BJ: setbacks and others' behavior can block a particular outcome but "
     "not your response, standards, or next move; the inner ground stays yours. Held interpretively.",
     ["no man can hinder thee"],
     ["inner-citadel", "resilience", "agency", "mindset", "marcus-aurelius", "meditations"]),
    (MED,
     "Memento mori: impermanence as a source of clarity and proportion",
     "mindset",
     "Marcus repeatedly contemplates death and the torrent of change ('as through a torrent pass "
     "the things of the world'; generation and death alike are nature's work). Holding "
     "impermanence in view strips away vanity and trivial worry and concentrates attention on "
     "what actually matters now.",
     "Keeping mortality and impermanence in view is a practical tool for proportion: it dissolves "
     "petty concern and vanity and focuses energy on what genuinely matters.",
     "A proportion lens for BJ: holding the long view and impermanence cuts through status-anxiety "
     "and trivial worry, clarifying what is worth doing now. Read as secular Stoic practice, not "
     "a faith claim.",
     ["as through a torrent", "so also death"],
     ["memento-mori", "impermanence", "proportion", "mindset", "marcus-aurelius", "meditations"]),
    # ---------- Landmark Caesar · 4 ----------
    (CAESAR,
     "Command, audacity, and calculated risk",
     "leadership",
     "The Landmark essays show Caesar as a commander willing to take great risks to seize "
     "decisive advantage, trusting his self-confidence and judgment to extract himself from "
     "trouble. His boldness was real and knowing, not reckless; he repeatedly gambled on speed "
     "and decisiveness where rivals hesitated.",
     "Decisive, calculated boldness, acting fast where others hesitate, can seize advantage, "
     "provided it rests on real judgment rather than recklessness.",
     "A leadership lens for BJ: calculated boldness and speed can win position where hesitation "
     "loses it, but it must rest on real judgment; held interpretively, not a directive to gamble.",
     ["willing to take great risks", "self-confident"],
     ["audacity", "calculated-risk", "decisiveness", "leadership", "caesar", "landmark-caesar"]),
    (CAESAR,
     "Clemency as strategy: clementia that made his position credible",
     "strategy",
     "Caesar's famous clemency, pardoning defeated enemies rather than slaughtering them, was not "
     "only character but strategy: it made his position credible, reduced the cost of resistance, "
     "and won over former opponents. Mercy functioned as a tool of consolidation after victory.",
     "Generosity toward the defeated can be strategically powerful: it lowers resistance, builds "
     "credibility, and converts former opponents, often outperforming maximal punishment.",
     "A power-handling lens for BJ (echoing Grant's Appomattox magnanimity): restraint and "
     "generosity at the moment of advantage can consolidate position better than maximal "
     "extraction. Held interpretively.",
     ["his famous clemency", "made his position credible"],
     ["clemency", "consolidation", "magnanimity", "strategy", "caesar", "landmark-caesar"]),
    (CAESAR,
     "Control your own narrative: the Commentaries as self-account",
     "operator-process",
     "Caesar wrote his own campaigns (the Gallic and Civil War Commentaries) in spare third-"
     "person prose, shaping how posterity would see him; the Landmark essays read them frankly as "
     "works of propaganda. He understood that controlling the record of your actions is part of "
     "the strategy, not an afterthought.",
     "Controlling the account of your own work (clear, deliberate self-documentation) shapes how "
     "it is judged; the narrative of what you did is part of the strategy, not separate from it.",
     "A strategic-communications lens for BJ: documenting and framing your own work clearly "
     "(the record, the case study, the narrative) is part of the strategy; controlling the account "
     "shapes the outcome. Read honestly (it was also propaganda), held interpretively.",
     ["a work of propaganda", "third person"],
     ["narrative-control", "self-documentation", "reputation", "operator-process", "caesar", "landmark-caesar"]),
    (CAESAR,
     "The bond with his soldiers: loyalty earned through shared stake",
     "leadership",
     "Caesar's power rested on the fierce loyalty of his veterans, cultivated by sharing hardship, "
     "rewarding them (land for veterans), and binding their fortunes to his. The essays show this "
     "soldier bond as a foundation of his strategic position, not a byproduct of it.",
     "Loyalty is earned by sharing hardship and binding people's real stake to the mission; a "
     "committed core, invested in the outcome, is a foundational strategic asset.",
     "A team/relationship lens for BJ: durable loyalty comes from shared stake and genuine care, "
     "not command alone; a small committed core invested in the outcome is foundational. Held "
     "interpretively.",
     ["land to his veterans", "loyalty of his"],
     ["loyalty", "shared-stake", "team", "leadership", "caesar", "landmark-caesar"]),
    # ---------- Synthesis · 2 ----------
    (ONWAR,
     "Synthesis: the classical-strategy operating pattern",
     "strategy",
     "Across the four texts a single operating pattern emerges: see the world as it actually is "
     "(Machiavelli's realism), expect that execution is harder than the plan (Clausewitz's "
     "friction) and concentrate on the decisive point, govern what is in your control and stay "
     "composed (Aurelius's inner command), and act with decisive but disciplined boldness, "
     "consolidating with restraint (Caesar). Clear sight, focused force, inner steadiness, "
     "decisive-yet-restrained action.",
     "Combine clear-eyed realism, focus on the decisive point, composure over the controllable, "
     "and disciplined decisive action with restraint, the durable spine of classical strategy "
     "and operator judgment.",
     "For BJ this is a portable judgment toolkit (see clearly, concentrate force, govern "
     "yourself, act decisively but with restraint), held as decision-support against the brief, "
     "not a directive about which battle to fight.",
     ["the simplest thing is difficult", "centre of gravity"],
     ["synthesis", "classical-strategy", "judgment", "strategy", "clausewitz", "classical-strategy"]),
    (MED,
     "Synthesis: pattern-library discipline and the optionality guardrail",
     "operator-doctrine",
     "CLASSICAL_STRATEGY is held as an interpretive strategy/operator pattern library, NOT "
     "doctrine: Machiavelli and Clausewitz are read for how power and conflict actually work, "
     "explicitly not as a mandate for ruthless tactics; Meditations is read as secular operator-"
     "discipline, not a faith lane; Caesar is read for command patterns, not conquest. The "
     "material informs BJ's judgment without setting any brand direction.",
     "Mine classical strategy for transferable judgment patterns while holding it as "
     "interpretation, not doctrine or directive; the value is sharpened judgment, decoupled from "
     "the politics, war, and empire that produced it.",
     "This synthesizes the lane for BJ: a sharpened-judgment toolkit held as decision-support "
     "against CURRENT_OPERATOR_REALITY_BRIEF, with Meditations secular not faith, Machiavelli/"
     "Clausewitz not directives, photography one option among several, and no final SNIPED / "
     "SNIPED Media / BASEPLATE direction set.",
     ["it is in thy power", "one option among several"],
     ["synthesis", "interpretive-lens", "optionality", "operator-doctrine", "marcus-aurelius", "classical-strategy"]),
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
    forb = [d for d in ("philosophy", "statecraft", "war", "history", "politics",
                        "military", "empire") if d in doms]
    print("forbidden domains present:", forb or "NONE")
    mx = max(len(q.split()) for r in lines for q in r["direct_quotes"])
    print("longest quote words:", mx)


if __name__ == "__main__":
    main()
