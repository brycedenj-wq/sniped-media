#!/usr/bin/env python3
"""Write TIER_2_GREENE_STRATEGY_CHUNKS.jsonl · 16 curated chunks · 3 sources.

batch_id: TIER_2_GREENE_STRATEGY · chunk_id: TIER_2_GREENE_STRATEGY_NNN
Existing domains only (power anchor). No new domain. No em-dashes.
Curated power / human-behavior / mastery pattern extraction (NOT chapter summary).
Greene held as pattern recognition / defensive awareness / operator judgment,
NOT an endorsement of predatory tactics. Identity-optionality guardrail in every chunk.
"""
import json
import os

OUT = os.path.expanduser(
    "~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/TIER_2_GREENE_STRATEGY_CHUNKS.jsonl")

LOHN = ("The Laws of Human Nature", "laws_of_human_nature_greene.txt", "Robert Greene")
MAST = ("Mastery", "mastery_greene.txt", "Robert Greene")
FIFTY = ("The 50th Law", "the_50th_law_50cent_greene.txt", "50 Cent and Robert Greene")

GUARD = (" Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support and "
         "pattern-library only, not doctrine and not a directive: not a directive that "
         "BJ become a manipulator, guru, pickup-artist, dark-psychology brand, political "
         "operator, masculine-influence account, or power-cosplay persona. No final SNIPED, "
         "SNIPED Media, or BASEPLATE direction; photography remains one option among several.")
GREENE = (" Held as pattern recognition, defensive awareness, and operator judgment "
          "(recognize the move so you are not the mark; develop real skill; see reality "
          "clearly), NOT an endorsement of predatory tactics.")

# (source, domain, concept, summary, usable_principle, relevance_lead, quotes, tags)
ROWS = [
    # ---- THE LAWS OF HUMAN NATURE (7) ----
    (LOHN, "decision-making",
     "The Law of Irrationality: emotion governs thought beneath awareness",
     "Greene argues our deepest blind spot is believing we are rational while emotion quietly "
     "drives our thoughts and decisions, via a pleasure principle that makes us embrace soothing "
     "ideas and recoil from painful ones. This breeds confirmation bias (seeking evidence for what "
     "we already want) and conviction bias (defending an idea loudly to convince ourselves), and "
     "when things go wrong we externalize blame.",
     "Treat your own certainty as suspect; hunt for the evidence that disconfirms a cherished belief "
     "and watch where the pleasure principle is steering you.",
     "BJ can run his own decisions through this filter (what do I want to be true here?) and read "
     "others' confident claims for the bias beneath them.",
     ["the pleasure principle", "confirmation bias"],
     ["irrationality", "cognitive-bias", "self-awareness", "judgment", "emotion"]),

    (LOHN, "culture",
     "The Law of Narcissism: turn self-love into empathy to read people",
     "Greene frames human attention as defaulting inward toward self-absorption; the operator skill "
     "is converting that energy into deliberate empathy, reading others by attending to their moods "
     "and perspective rather than projecting your own. Deep listening and attention to nonverbal "
     "cues turn empathy from a feeling into a trainable instrument.",
     "Build empathy as a skill, not a sentiment: shift attention off yourself and onto the other "
     "person's actual signals to read them accurately.",
     "For BJ, reading a client or collaborator well starts with muting self-focus and attending to "
     "their real cues, a directing and relationship asset.",
     ["self-love into empathy"],
     ["narcissism", "empathy", "social-reading", "attention", "relationships"]),

    (LOHN, "power",
     "The Law of Role-playing: read people past the mask",
     "Greene observes that people are consummate actors who present a controlled front, so the surface "
     "they show is managed and often misleading. The leverage is learning to read the involuntary "
     "signals (micro-expressions, tone, body language) that leak past the mask, and to manage your own "
     "front deliberately rather than unconsciously.",
     "Weight involuntary cues over stated words when reading someone, and treat your own presentation "
     "as a deliberate signal, held defensively to avoid being misled, not to deceive.",
     "BJ can read the room past the polished front and present himself intentionally, recognizing "
     "performance so he is not taken in by it.",
     ["consummate actors"],
     ["role-playing", "reading-people", "nonverbal", "impression-management", "defensive-awareness"]),

    (LOHN, "ethics",
     "The Law of Envy: watch for the fragile ego",
     "Greene describes envy as a covert, often disguised force: people compare and resent, and the "
     "fragile ego lashes out indirectly when it feels diminished. The defensive move is to detect the "
     "early signs of envy in others, avoid needlessly triggering it by flaunting advantage, and to "
     "catch and redirect the envious impulse in oneself.",
     "Read covert envy as a real social hazard, dampen the signals that provoke it, and convert your "
     "own comparison reflex into self-directed effort rather than resentment.",
     "BJ can manage how much advantage he displays and watch for envy-driven undercutting in his "
     "circle, a relationship and reputation safeguard.",
     ["the fragile ego"],
     ["envy", "ego", "social-risk", "comparison", "reputation"]),

    (LOHN, "culture",
     "The Law of Conformity: resist the downward pull of the group",
     "Greene argues groups exert a powerful pull that can lower individuals to a shared emotional "
     "denominator, rewarding conformity and punishing independent thought. People play roles inside a "
     "group court and absorb its moods; the operator skill is participating without surrendering "
     "independent judgment.",
     "Stay aware of the group's emotional gravity and protect a zone of independent judgment instead "
     "of being absorbed into the consensus.",
     "BJ can read scene and group dynamics and keep his own standards intact rather than drifting with "
     "a crowd's mood, while still moving inside it.",
     ["the downward pull"],
     ["conformity", "group-dynamics", "independent-judgment", "social-pressure", "scene"]),

    (LOHN, "decision-making",
     "The Law of Shortsightedness: elevate your perspective",
     "Greene contrasts the reactive mind, gripped by the emotion and noise of the immediate moment, "
     "with the strategic mind that elevates its perspective to longer time horizons and deeper causes. "
     "Most error comes from overweighting the urgent and the dramatic; clarity comes from stepping back "
     "to see trends and second-order effects.",
     "Lengthen your time horizon before deciding: discount the dramatic immediate signal and weight the "
     "longer trend and downstream consequences.",
     "BJ, loading a backend before committing, benefits from the long view: resist reacting to the loud "
     "near-term and judge by where the trend leads.",
     ["elevate your perspective"],
     ["shortsightedness", "long-view", "perspective", "strategy", "second-order"]),

    (LOHN, "founder-psychology",
     "The Law of Death Denial: mortality awareness as a motive force",
     "Greene closes by arguing that suppressing awareness of mortality drains life of urgency, while "
     "consciously confronting it sharpens focus, gratitude, and the will to do meaningful work now. "
     "The brevity of time becomes a source of aliveness and a filter for what actually matters.",
     "Let a sober awareness of limited time set priorities and urgency, converting it into focus on the "
     "work that matters rather than anxiety.",
     "For BJ this is a focusing lens: use the finiteness of time to prioritize the build that matters "
     "and act with urgency, without morbidity.",
     ["meditate on our mortality"],
     ["mortality", "urgency", "priorities", "aliveness", "focus"]),

    # ---- MASTERY (5) ----
    (MAST, "founder-psychology",
     "Life's Task: return to your primal inclination",
     "Greene argues each person has a unique primal inclination, visible early as a pull toward certain "
     "subjects or activities, and that finding and aligning with this Life's Task is the foundation of "
     "mastery. Drifting into work disconnected from it produces mediocrity and restlessness; "
     "reconnecting to it supplies the energy and focus mastery requires.",
     "Align effort with a genuine, self-rooted inclination rather than external prestige; the energy for "
     "deep work comes from that connection.",
     "BJ's optionality search is exactly this: find the wedge that connects to his real inclinations and "
     "skills rather than chasing a generic or prestige path.",
     ["return to your origins"],
     ["lifes-task", "calling", "primal-inclination", "alignment", "vocation"]),

    (MAST, "operator-doctrine",
     "The apprenticeship: transformation over money or title",
     "Greene names three phases (Apprenticeship, Creative-Active, Mastery) and insists the true goal of "
     "the apprenticeship is the transformation of mind and character, not pay, position, or a title. The "
     "practical consequence is choosing roles for their learning value and feedback, moving toward "
     "challenges that toughen you rather than comfortable, lucrative dead ends.",
     "Optimize early-stage choices for learning and honest feedback over money or status; practical "
     "knowledge compounds for decades.",
     "In build-mode, BJ should weight projects by how much real skill and feedback they build, not by "
     "immediate pay or prestige.",
     ["transformation of your mind"],
     ["apprenticeship", "skill-building", "learning-over-pay", "feedback", "development"]),

    (MAST, "operator-process",
     "Deep observation, skills, experimentation, and tacit knowledge",
     "Greene maps the apprenticeship as three overlapping modes: deep observation (the passive mode, "
     "absorbing the rules and reality before trying to impress), skills acquisition (the practice mode, "
     "reducing a craft to a core skill and drilling it toward the roughly ten-thousand-hour threshold), "
     "and experimentation (the active mode). Sustained practice builds tacit knowledge, a feel that is "
     "hard to verbalize but obvious in action.",
     "Sequence learning as observe, then drill a core skill to fluency, then experiment; concentrated "
     "practice converts into tacit, intuitive competence.",
     "BJ can structure his AI, systems, and visual skill-building as deliberate practice of a few core "
     "skills toward real tacit fluency, not scattered dabbling.",
     ["tacit knowledge"],
     ["deliberate-practice", "skill-acquisition", "10000-hours", "tacit-knowledge", "process"]),

    (MAST, "power",
     "Social intelligence: see people realistically, shed the naive perspective",
     "Greene argues many talented people stall because they lack social intelligence: they cling to a "
     "naive perspective (projecting their own assumptions onto others) instead of seeing people as they "
     "actually are. Mastery includes reading individuals accurately, decoding unwritten group and "
     "political codes, and working with people without being derailed by them.",
     "Trade the naive perspective for realistic people-reading: see others on their own terms and learn "
     "the unwritten codes, held defensively rather than to manipulate.",
     "BJ's collaborations and client work depend on this realistic read of people and group codes, an "
     "operator skill as load-bearing as technical skill.",
     ["social intelligence"],
     ["social-intelligence", "people-reading", "politics", "realism", "collaboration"]),

    (MAST, "mental-models",
     "The Creative-Active phase and the dimensional, intuitive mind",
     "After deep apprenticeship, Greene describes the Creative-Active phase, where accumulated knowledge "
     "lets you experiment and connect ideas, culminating in the dimensional mind: a fluid, intuitive "
     "grasp of the whole that fuses rigorous knowledge with pattern-level intuition. This high-end "
     "intuition is earned by the prior years of practice, not a shortcut around them.",
     "Earn intuition through depth: only after deep skill does the mind see the whole and make creative, "
     "fast connections; protect openness to keep refreshing it.",
     "BJ's edge compounds when deep practice in a domain turns into intuitive, cross-connecting judgment, "
     "the dimensional read that beginners cannot fake.",
     ["the dimensional mind"],
     ["creative-active", "intuition", "synthesis", "expertise", "mental-models"]),

    # ---- THE 50TH LAW (3) ----
    (FIFTY, "power",
     "Fearlessness: fear is the real enemy",
     "Greene and 50 Cent argue that fear, useful as a momentary survival signal, becomes corrosive when "
     "it hardens into a fearful attitude toward life, shrinking perception to risk and triggering "
     "retreat exactly when action is needed. The fearless type (forged by adversity) refuses that "
     "downward pull and converts hard circumstances into a source of strength.",
     "Notice when fear has become a standing attitude that narrows your options, and choose action and "
     "wider perception instead of reflexive retreat.",
     "For BJ in an uncertain build, the discipline is to keep fear as a signal, not a worldview, and "
     "keep moving and perceiving widely under pressure.",
     ["fear itself"],
     ["fearlessness", "fear-management", "resilience", "action", "attitude"]),

    (FIFTY, "founder-psychology",
     "Intense realism and self-reliance: see things as they are, own everything",
     "The first law is intense realism: see circumstances for what they are, not as you wish or fear them "
     "to be, stripping away illusion. Paired with it is self-reliance: make everything your own, take full "
     "ownership rather than depending on others or outside forces, which builds both capability and a "
     "durable confidence grounded in reality.",
     "Face reality without flinching and take ownership of your situation; confidence built on clear "
     "sight and self-reliance outlasts confidence built on hope.",
     "BJ's operator stance, seeing real pain and real constraints clearly and owning the build himself, "
     "is exactly this realism plus self-reliance.",
     ["intense realism"],
     ["realism", "self-reliance", "ownership", "confidence", "reality-contact"]),

    (FIFTY, "strategy",
     "Opportunism: turn adversity into opportunity (amor fati)",
     "Greene and 50 Cent frame opportunism as a high art: in every difficulty there is an opening, and "
     "the operator who accepts events rather than railing against them (the Stoic amor fati, love of "
     "fate, Marcus Aurelius's fire that converts everything in its path) can transform setbacks into "
     "advances. Rigidity that misses openings is the failure mode.",
     "Accept the situation you are handed and convert it into an opening; adaptability and amor fati turn "
     "adversity into material rather than defeat.",
     "BJ can treat constraints and setbacks in the build as raw material for the next move rather than "
     "reasons to stall, the opportunist's adaptive stance.",
     ["amor fati"],
     ["opportunism", "amor-fati", "adaptability", "adversity", "stoicism"]),

    # ---- SYNTHESIS (1) ----
    (LOHN, "operator-doctrine",
     "Synthesis: the Greene operator-psychology toolkit",
     "Across the three books a single operator toolkit emerges: read human nature and your own "
     "irrationality clearly (Laws of Human Nature), develop real skill through a deliberate apprenticeship "
     "toward mastery (Mastery), and act with reality-contact, self-reliance, and less fear (The 50th Law). "
     "It is a pattern-library for power literacy, emotional discipline, status-reading, and earned "
     "competence, held defensively rather than as a manipulation program.",
     "Combine clear-eyed people-reading, deep skill development, and fearless realism into operator "
     "judgment, using power literacy to protect and build, not to prey.",
     "BJ holds this as a defensive-awareness and self-development toolkit for his build-mode stage, NOT a "
     "license to manipulate or a power-cosplay identity.",
     ["make everything your own"],
     ["synthesis", "power-literacy", "operator-judgment", "self-development", "defensive-awareness"]),
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
    for i, (src, domain, concept, summary, principle, rel_lead, quotes, tags) in enumerate(ROWS, 1):
        title, sfile, author = src
        r = {
            "chunk_id": f"TIER_2_GREENE_STRATEGY_{i:03d}",
            "batch_id": "TIER_2_GREENE_STRATEGY",
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": rel_lead + GUARD + GREENE,
            "direct_quotes": quotes,
            "tags": tags,
        }
        rows.append(r)

    for r in rows:
        for q in r["direct_quotes"]:
            assert len(q.split()) <= 6, f"quote too long in {r['chunk_id']}: {q}"

    rows = [sweep(r) for r in rows]
    blob = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    assert chr(0x2014) not in blob, "em-dash found in output"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(blob)
    print(f"wrote {len(rows)} chunks to {OUT}")


if __name__ == "__main__":
    main()
