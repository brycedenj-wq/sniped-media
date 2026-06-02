#!/usr/bin/env python3
"""
CULTURE_AND_STATUS chunk writer · status / culture / symbolic-value theory (2 CORE books).
Schema: chunk_id, batch_id, source_title, source_file, author, domain, concept, summary,
        usable_principle, sniped_relevance, direct_quotes, tags. ID pattern CULTURE_AND_STATUS_NNN.
Domains reused (all pre-existing · operator-approved · NO new domain): status, culture, systems-thinking,
brand-psychology, aesthetics, strategy, lineage (light · 1). Copyright-safe SHORT quotes only. Em-dash swept.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "CULTURE_AND_STATUS_CHUNKS.jsonl"

C = []


def add(src, title, author, domain, concept, summary, usable, relevance, quotes, tags):
    C.append({"source_title": title, "source_file": src, "author": author, "domain": domain,
              "concept": concept, "summary": summary, "usable_principle": usable,
              "sniped_relevance": relevance, "direct_quotes": quotes, "tags": tags})


# ===================== The Status Game · Will Storr (7) =====================
S = "the_status_game_storr.txt"; T = "The Status Game (2021)"; A = "Will Storr"
add(S, T, A, "status", "Status is a fundamental human drive, the hidden game beneath behavior",
    "Storr argues that the pursuit of status (social position relative to others) is a core, evolved human drive that quietly structures behavior, belief, and culture. Most of what looks like other motives is a status game in disguise.",
    "Read a market, a client, or an audience as players in a status game first; the status payoff usually explains behavior better than the stated reason.",
    "Gives SNIPED the master lens for premium-buyer psychology: founders buy photography partly to win a status game, not just to get images.",
    "the hidden structure of human life",
    ["status-drive", "hidden-game", "human-motivation", "status"])
add(S, T, A, "status", "Three status games: dominance, virtue, success",
    "Storr distinguishes three ways humans compete for status: dominance (force/fear), virtue (being seen as good/correct), and success (skill/competence/usefulness). Healthy cultures and people lean on virtue and success, not dominance.",
    "Choose which status game you play and reward in others: compete on success (demonstrated skill) and virtue (genuine standards), never dominance.",
    "Frames SNIPED's positioning: win status through demonstrated craft (success) and held standards (virtue), not through dominance posturing.",
    "the dominance game, the virtue game and the success game",
    ["three-games", "dominance-virtue-success", "status-strategy", "status"])
add(S, T, A, "brand-psychology", "Status is detected automatically, from subtle signals",
    "Storr shows the brain reads status from voice, posture, eye contact, and micro-symbols in milliseconds, mostly unconsciously and with surprising accuracy. Status is communicated and judged before a word is consciously processed.",
    "Engineer the subtle status signals (composure, restraint, the quality of the work) because the audience reads them instantly and unconsciously.",
    "Explains why SNIPED's quiet-luxury restraint reads as high status: the signals register pre-consciously, before any claim is made.",
    "the status detection system continually reads symbolic information",
    ["status-detection", "signals", "unconscious", "brand-psychology"])
add(S, T, A, "status", "Prestige status is granted by others, never declared",
    "Storr stresses that prestige-based status must be conferred by others; self-promotion and boasting reliably backfire because status is something an audience grants, not something a player can seize. People are inept at self-status-boosting.",
    "Earn status by being granted it (proof, results, others' words), never by claiming it; let the work and the audience confer the rank.",
    "Underwrites SNIPED's show-don't-claim posture and the social-proof / named-client strategy: status comes from others' recognition.",
    "prestige-based status is granted by others, not declared by a victor",
    ["prestige", "granted-not-seized", "anti-boasting", "status"])
add(S, T, A, "systems-thinking", "When status games go bad: humiliation, tyranny, extremism",
    "Storr's darker thesis: blocked or threatened status (humiliation) drives the worst human behavior, from mobs to extremism to violence. Status games turn destructive when dominance takes over and players are denied a path to earn rank.",
    "Never humiliate a player you want to keep; design interactions so people can save face and earn status, because status threat triggers the worst responses.",
    "A guardrail for SNIPED's client and audience relationships: protect dignity, give people a way to rise, avoid the status-threat that breeds resentment.",
    "what happens when status games go bad",
    ["humiliation", "status-threat", "destructive-dynamics", "systems-thinking"])
add(S, T, A, "systems-thinking", "Positive-sum games beat zero-sum dominance",
    "Storr contrasts zero-sum dominance games (one rises only as another falls) with success and virtue games that can be positive-sum (everyone can earn status by contributing value). The games that build fairer, wealthier worlds are the positive-sum ones.",
    "Build status systems where participants earn rank by adding value, so the game is positive-sum and compounds rather than cannibalizes.",
    "Shapes SNIPED's scene-density strategy: a community where members gain status by elevating the scene is positive-sum and self-reinforcing.",
    "",
    ["positive-sum", "zero-sum", "value-creation", "systems-thinking"])
add(S, T, A, "strategy", "Play a good game: earn status by being genuinely useful and skilled",
    "Storr's practical counsel is to consciously choose status games worth playing, where rank is earned through real skill, contribution, and connection rather than dominance or hollow virtue-signaling. The game you play shapes who you become.",
    "Deliberately pick the success-and-virtue game (real skill, real standards) as your status arena; the chosen game forms the operator.",
    "Aligns with SNIPED's craft-first, repetition-over-novelty identity: status earned through demonstrated mastery is the durable game.",
    "",
    ["play-a-good-game", "earned-status", "self-formation", "strategy"])

# ===================== Status and Culture · W. David Marx (7) =====================
S = "status_and_culture_marx.txt"; T = "Status and Culture (2022)"; A = "W. David Marx"
add(S, T, A, "culture", "The desire for status drives taste",
    "Marx's central thesis: our desire for social rank is the hidden engine that creates taste, identity, art, fashion, and constant cultural change. We adopt tastes and conventions largely to signal and secure status.",
    "Treat taste choices as status signals; to shift what an audience values, change what confers status within their group.",
    "Reframes SNIPED's aesthetic positioning: the quiet-luxury taste is a status signal to a specific tier, not a neutral style preference.",
    "how our desire for social rank creates taste, identity, art, fashion, and constant change",
    ["status-drives-taste", "cultural-engine", "signaling", "culture"])
add(S, T, A, "brand-psychology", "Conventions and signals: how taste communicates rank",
    "Marx shows status symbols work through shared conventions: a choice signals rank only because a group reads it as such. Signaling requires a code the audience already understands, and the signal's meaning is conventional, not intrinsic.",
    "Use the audience's existing status conventions to signal, rather than inventing private symbols they cannot read; meaning is conventional.",
    "Tells SNIPED to deploy the recognized high-status visual conventions of the LA founder/creative tier so the signal lands.",
    "All status symbols rely on objects and behaviors with practical or aesthetic value",
    ["conventions", "signaling", "status-symbols", "brand-psychology"])
add(S, T, A, "systems-thinking", "Status is the engine of fashion cycles and constant change",
    "Marx explains why styles change: as a status signal diffuses to lower tiers, elites abandon it for a new one to re-mark distinction, driving perpetual fashion cycles. Cultural change is the mechanical output of status competition.",
    "Anticipate that any status signal you adopt will diffuse and lose distinction; plan for the cycle rather than being surprised by it.",
    "Explains the churn SNIPED operates against and argues for owning a durable, lineage-rooted signal rather than chasing diffusing trends.",
    "humans hop en masse from one set of arbitrary practices to another",
    ["fashion-cycles", "diffusion", "constant-change", "systems-thinking"])
add(S, T, A, "culture", "Subcultures are alternative status hierarchies",
    "Marx frames subcultures as groups that invent their own status criteria, letting members who rank low in the mainstream win status by their own rules. Authenticity is the prized signal inside these alternative hierarchies, and subcultures historically fed innovation back to the mainstream.",
    "Build or enter a subculture with its own status criteria where your strengths rank high, rather than competing on the mainstream's terms.",
    "Maps to SNIPED's scene-density doctrine: cultivate a specific LA cultural circle with its own status criteria the operator can lead.",
    "",
    ["subcultures", "alternative-hierarchy", "authenticity", "culture"])
add(S, T, A, "lineage", "Cultural capital: taste as learned and inherited status",
    "Drawing on Bourdieu, Marx treats cultural capital (the taste, references, and codes absorbed from one's milieu) as a form of inherited status that the mainstream record reads as natural refinement. Taste is taught and inherited, not innate.",
    "Recognize that fluent taste reads as inherited refinement; build and document the cultural capital deliberately rather than assuming it is innate.",
    "Connects status theory to the SNIPED Lineage Doctrine: cultural capital is inherited status, and documenting from inside a lineage builds it credibly.",
    "",
    ["cultural-capital", "bourdieu", "inherited-status", "lineage"])
add(S, T, A, "culture", "The internet flattened status signaling into ephemeral fads",
    "Marx argues the internet broke the old status-signaling order: exclusive symbols became universally available, taste fragmented into the long tail, and fashion cycles accelerated into ephemeral fads rather than era-defining trends. Distinction got harder to hold.",
    "Do not rely on access-based exclusivity for status in an internet-flattened world; durable distinction now comes from depth, craft, and lineage, not secrecy.",
    "Explains why SNIPED competes on craft-depth and lineage rather than gatekept exclusivity, and why a durable signal beats chasing fads.",
    "fashion cycles pump out ephemeral fads rather than era-defining trends",
    ["internet-age", "flattening", "ephemeral-fads", "culture"])
add(S, T, A, "aesthetics", "Costly, hard-to-fake signals carry the most status",
    "Marx (echoing signaling theory) shows the most reliable status signals are those that are expensive or difficult to fake (deep knowledge, evident craft, time-intensive taste), because the cost is the proof. Cheap-to-copy signals quickly lose their distinguishing power.",
    "Invest in status signals that are genuinely costly to fake (craft, depth, restraint); the difficulty of imitation is what preserves the distinction.",
    "Backs SNIPED's high-production, deep-craft investment as the durable status signal that commoditized AI output cannot cheaply imitate.",
    "",
    ["costly-signals", "hard-to-fake", "distinction", "aesthetics"])

# ===================== synthesis (2 · cite a representative real file) =====================
add("status_and_culture_marx.txt", "CULTURE_AND_STATUS cross-source synthesis", "SNIPED synthesis", "strategy",
    "Sell status, not features: status systems shape brand and positioning",
    "Storr and Marx together establish that status is the hidden engine of behavior and culture, so brands and positioning succeed by offering a credible status payoff within a specific group's hierarchy. The premium buyer is buying rank, recognition, and belonging as much as the deliverable.",
    "Position the offer as a status payoff within the client's specific hierarchy (recognition, belonging, distinction), not as a feature list; price to the status, not the cost.",
    "The core commercial conclusion CULTURE_AND_STATUS hands SNIPED: the premium photography offer sells status and recognition, which is why it commands the floor price.",
    "",
    ["synthesis", "sell-status", "positioning", "strategy"])
add("the_status_game_storr.txt", "CULTURE_AND_STATUS cross-source synthesis", "SNIPED synthesis", "status",
    "Status is the operator's lever, played as a good game with low self-orientation",
    "The two books reframe status as a lever SNIPED can wield, but Storr's warning (dominance and humiliation breed resentment; prestige is granted, not seized) sets the ethical guardrail: win status by being genuinely useful and by conferring status on others, never by extracting or boasting.",
    "Wield status deliberately but play the success-and-virtue game: earn it through craft, grant it generously to clients and the scene, and never seize it through dominance or boasting.",
    "Ties status theory to SNIPED's trust-equation (low self-orientation) and hospitality doctrine: the operator raises others' status, which is the durable way to earn their own.",
    "",
    ["synthesis", "status-as-lever", "ethical-guardrail", "status"])

# ---- emit ----
em = chr(0x2014)
lines = []
for i, ch in enumerate(C, start=1):
    lines.append({
        "chunk_id": f"CULTURE_AND_STATUS_{i:03d}",
        "batch_id": "CULTURE_AND_STATUS",
        "source_title": ch["source_title"],
        "source_file": ch["source_file"],
        "author": ch["author"],
        "domain": ch["domain"],
        "concept": ch["concept"],
        "summary": ch["summary"],
        "usable_principle": ch["usable_principle"],
        "sniped_relevance": ch["sniped_relevance"],
        "direct_quotes": ch["direct_quotes"],
        "tags": ch["tags"],
    })

swept = 0
for rec in lines:
    for k, v in rec.items():
        if isinstance(v, str) and em in v:
            rec[k] = v.replace(em, " · "); swept += 1
        elif isinstance(v, list):
            nl = []
            for item in v:
                if isinstance(item, str) and em in item:
                    nl.append(item.replace(em, " · ")); swept += 1
                else:
                    nl.append(item)
            rec[k] = nl

OUT.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in lines) + "\n", encoding="utf-8")
print(f"Wrote {len(lines)} chunks to {OUT.name}")
print(f"Em-dashes swept: {swept}")
from collections import Counter
print("Domain distribution:", dict(sorted(Counter(r["domain"] for r in lines).items())))
print("Source distribution:")
for k, v in sorted(Counter(r["source_file"] for r in lines).items()):
    print(f"  {v:3d}  {k}")
