#!/usr/bin/env python3
"""
Write MEDIA_BUSINESS_CHUNKS.jsonl · 17 chunks (15 source + 2 synthesis) across 3 oral histories.
12-field canonical schema. ONE new domain `media-business` (anchor · operator-approved). media/
entertainment/programming must NOT appear. Other concepts route to existing culture/strategy/
commercial-architecture/brand/founder-psychology/operator-process/systems-thinking/content-strategy.
Identity-optionality guardrail: media-business patterns are decision-support lenses against
CURRENT_OPERATOR_REALITY_BRIEF, NOT a directive that SNIPED becomes a media company; no final
SNIPED / SNIPED Media / BASEPLATE direction. Em-dash sweep at the end.
"""

import json
from pathlib import Path

OUT = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "MEDIA_BUSINESS_CHUNKS.jsonl"

ESPN = ("Those Guys Have All the Fun", "those_guys_espn.txt", "James Andrew Miller & Tom Shales")
SNL = ("Live From New York", "live_from_new_york_snl.txt", "Tom Shales & James Andrew Miller")
HBO = ("Tinderbox", "tinderbox_hbo.txt", "James Andrew Miller")

DG = "Decision-support / pattern-library lens only, read against CURRENT_OPERATOR_REALITY_BRIEF. Media-empire patterns are lenses, NOT a directive that SNIPED becomes a media company; this does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction, and photography remains one option among several."

C = []
def add(src, domain, concept, summary, principle, relevance, quotes, tags):
    n = len(C) + 1
    title, sfile, author = src
    C.append({
        "chunk_id": f"MEDIA_BUSINESS_{n:03d}",
        "batch_id": "MEDIA_BUSINESS",
        "source_title": title, "source_file": sfile, "author": author,
        "domain": domain, "concept": concept, "summary": summary,
        "usable_principle": principle, "sniped_relevance": relevance,
        "direct_quotes": quotes, "tags": tags,
    })

# ---------------- ESPN · Those Guys Have All the Fun · 5 ----------------
add(ESPN, "media-business",
    "The dual-revenue model: subscriber fees plus advertising",
    "ESPN's structural breakthrough was charging cable operators a per-subscriber carriage fee AND selling advertising, so it was paid twice for the same audience. That dual-revenue base, rising with every subscriber, funded the rights and programming that competitors on a single revenue stream could not match.",
    "Engineer a dual (or recurring) revenue base so the same audience pays more than once and funds a widening lead.",
    "An economics lens: a durable business often rests on a recurring, multi-sided revenue structure, not one-time sales. Held against current reality as a pattern, not a SNIPED directive. " + DG,
    [],
    ["dual-revenue", "carriage-fees", "subscriber-economics", "media-business", "espn"])

add(ESPN, "content-strategy",
    "SportsCenter: the repeatable flagship format",
    "SportsCenter gave ESPN a daily, repeatable, identity-defining program that could run on a cycle, build habit, and showcase a house voice. A signature recurring format (not one-off events) created appointment viewing and a platform for talent and brand.",
    "Build one signature, repeatable format that creates habit and carries the house voice, rather than relying on one-off productions.",
    "A content lens: a repeatable signature format compounds habit and brand · a pattern to consider for any future SNIPED output cadence, not a mandate. " + DG,
    [],
    ["flagship-format", "appointment-viewing", "habit", "content-strategy", "espn"])

add(ESPN, "brand",
    "The Worldwide Leader in Sports: positioning and audience trust",
    "ESPN claimed and then earned the positioning 'the Worldwide Leader in Sports', a confident self-definition that set audience expectations and compounded trust. The brand became shorthand for authority, so being on ESPN conferred legitimacy on events and talent alike.",
    "Claim a clear authority positioning and then earn it; the brand becomes a trust shorthand that confers legitimacy.",
    "A positioning lens (echoes WWP / category design): an authority claim, once earned, compounds trust · held as a pattern, not a SNIPED positioning decision. " + DG,
    ["the worldwide leader in sports"],
    ["positioning", "authority", "audience-trust", "brand", "espn"])

add(ESPN, "commercial-architecture",
    "Long-term rights as the moat",
    "ESPN locked up long-term broadcast rights to leagues and events, which both guaranteed must-watch inventory and denied it to rivals. Controlling the scarce underlying content (the rights) was a structural moat that money alone could not quickly overcome.",
    "Secure long-term control of the scarce underlying asset (rights, access) so competitors cannot easily replicate your inventory.",
    "A moat lens: durable advantage can come from controlling scarce access/inventory · for SNIPED this maps to relationships/archive/access, held as analysis not a directive. " + DG,
    [],
    ["rights", "moat", "scarce-access", "commercial-architecture", "espn"])

add(ESPN, "operator-process",
    "The Bristol talent machine",
    "ESPN built a campus and a system in Bristol that developed on-air and production talent at scale, with a strong (sometimes brutal) internal culture that set standards and produced a deep bench. The institution, not any single anchor, was the engine.",
    "Build a talent-development system and culture so the institution, not any individual star, is the engine of output.",
    "An operating lens: systems and culture that develop talent outlast individuals · a pattern for any future team, not a directive. " + DG,
    [],
    ["talent-development", "culture", "the-institution", "operator-process", "espn"])

# ---------------- SNL · Live From New York · 5 ----------------
add(SNL, "founder-psychology",
    "Lorne Michaels: the founder as the institution",
    "Lorne Michaels is the singular creative authority who built and embodies SNL; his taste, judgment, and stamina across decades are the show's organizing principle. The institution runs on one person's sustained point of view and ability to renew it.",
    "A durable creative institution often rests on one founder's sustained taste and judgment, renewed over decades.",
    "A founder-psychology lens (the operator as the system) · held as a pattern against current reality, not a directive to build a SNIPED institution. " + DG,
    [],
    ["founder-as-institution", "taste", "creative-authority", "founder-psychology", "snl"])

add(SNL, "media-business",
    "The repertory talent pipeline",
    "SNL works as a renewable talent machine: a repertory of cast and writers continuously discovered, developed, churned, and graduated into the wider culture. The pipeline (auditions, seasons, turnover) is the product as much as any single sketch.",
    "Build a renewable talent pipeline (discover, develop, graduate) so the franchise refreshes itself instead of depending on a fixed roster.",
    "A media-business lens: institutions endure by renewing talent, not retaining a fixed cast · a pattern, not a SNIPED staffing directive. " + DG,
    [],
    ["talent-pipeline", "repertory", "renewal", "media-business", "snl"])

add(SNL, "content-strategy",
    "Live as the product: the format is the constraint",
    "The live, weekly, no-net format is SNL's defining product feature: the danger and immediacy of live performance create stakes, urgency, and a reason to watch now. The constraint (live, on a deadline) is the differentiator, not a limitation.",
    "Make a hard constraint (live, deadline, format) the differentiating feature that creates urgency and stakes.",
    "A content lens: a self-imposed constraint can be the product's edge · a pattern for any future SNIPED cadence/format, not a mandate. " + DG,
    [],
    ["live-format", "constraint-as-feature", "urgency", "content-strategy", "snl"])

add(SNL, "systems-thinking",
    "Institutional renewal: the franchise outlasts the stars",
    "SNL has survived repeated cast departures, down seasons, and generational turnover because the format and institution are bigger than any star. Designed renewal (the show reinvents with each new cast) makes the franchise antifragile across decades.",
    "Design the institution so it survives the loss of any star; renewal, not retention, is what makes a franchise last.",
    "A systems lens on durability through renewal · held as analysis against current reality, not a SNIPED structural decision. " + DG,
    [],
    ["renewal", "antifragile", "franchise-over-talent", "systems-thinking", "snl"])

add(SNL, "culture",
    "A cultural institution and launchpad",
    "SNL functions as both a cultural mirror (topical comedy that shapes the national conversation) and a launchpad (a credentialing platform that mints stars and writers). Becoming a cultural institution multiplied its gravity, talent pull, and staying power.",
    "Cultural-institution status compounds gravity: it pulls talent, shapes the conversation, and becomes self-reinforcing.",
    "A culture lens connecting to the status/culture layer · a pattern on institutional gravity, not a SNIPED directive. " + DG,
    [],
    ["cultural-institution", "launchpad", "gravity", "culture", "snl"])

# ---------------- HBO · Tinderbox · 5 ----------------
add(HBO, "media-business",
    "The subscription model: no ads, different incentives",
    "HBO's subscriber-funded, ad-free model meant it answered to viewers paying for quality rather than advertisers chasing the largest audience. That incentive structure justified expensive, risky, prestige programming and a willingness to serve a discerning minority rather than the mass middle.",
    "Subscriber funding changes the incentive: you optimise for the quality your payers value, not the mass audience advertisers want.",
    "An economics lens directly relevant to premium positioning: who pays you determines what you optimise for · held as a pattern, not a SNIPED model decision. " + DG,
    [],
    ["subscription", "ad-free", "incentives", "media-business", "hbo"])

add(HBO, "brand",
    "Not TV: the prestige brand above the category",
    "HBO positioned itself as not-television, a premium brand signaling that its programming was a cut above the medium it technically belonged to. The brand promise (quality, prestige, distinction) set expectations and let it charge a premium and attract top creators.",
    "Position above your category as a premium/quality brand, so the name itself signals distinction and supports a premium.",
    "A premium-positioning lens (pairs with New Luxury / status layer) · a pattern for distinction, not a SNIPED positioning decision. " + DG,
    [],
    ["premium-brand", "prestige", "above-category", "brand", "hbo"])

add(HBO, "culture",
    "Creative autonomy produced the prestige era",
    "HBO's prestige era (The Sopranos and the dramas that followed) came from giving auteur creators unusual room and backing, trusting vision over formula. Creative autonomy, paired with a brand that could absorb risk, produced culture-defining work.",
    "Give trusted creators real autonomy and air cover; vision over formula is what produces culture-defining work.",
    "A creative-leadership lens: autonomy plus backing yields distinctive work · a pattern relevant to SNIPED's craft, not a directive. " + DG,
    [],
    ["creative-autonomy", "auteur", "prestige-programming", "culture", "hbo"])

add(HBO, "operator-process",
    "Creative leadership: betting on the few",
    "Under leaders like Plepler, HBO functioned by cultivating relationships with top creators and making concentrated bets on a small number of high-conviction projects rather than spreading thin. Taste-led curation and creator relationships were the operating method.",
    "Operate by curation and relationships: make concentrated high-conviction bets on the best creators rather than spreading thin.",
    "An operating lens (pairs with the power-law / curation patterns) · concentrated taste-led bets · held as analysis, not a SNIPED mandate. " + DG,
    [],
    ["curation", "creative-leadership", "concentrated-bets", "operator-process", "hbo"])

add(HBO, "strategy",
    "The streaming disruption: scarcity to scale",
    "HBO's premium-channel model (scarcity, exclusivity, a contained slate) came under strain in the streaming era (HBO Max), where the logic shifted to volume, subscribers-at-scale, and library breadth. The very model that created prestige was pressured by the platform shift.",
    "A model optimised for scarcity/prestige can be strained when the platform shifts to scale; durable advantages still face regime change.",
    "A strategy lens on how winning models meet disruption · a caution pattern, not a SNIPED directive · reinforces optionality (no model is permanent). " + DG,
    [],
    ["disruption", "scarcity-vs-scale", "streaming", "strategy", "hbo"])

# ---------------- Synthesis · 2 ----------------
add(ESPN, "media-business",
    "SYNTHESIS: the media-empire pattern",
    "Read together, the three institutions show a common machinery for turning taste, access, talent, and timing into durable power over attention: a recurring/multi-sided revenue base (ESPN dual-revenue, HBO subscription), a signature repeatable format (SportsCenter, the live show), a renewable talent system (the Bristol machine, the SNL repertory, HBO's creator relationships), an authority/prestige brand (Worldwide Leader, not-TV), and control of scarce access or distribution (rights, the channel). Durable media power compounds when these reinforce each other.",
    "Durable attention businesses combine recurring revenue, a signature format, a renewable talent system, an authority brand, and control of scarce distribution, each reinforcing the others.",
    "A consolidated media-empire pattern library · supplies structural patterns the operator can draw from, NOT a path to copy or a directive to build a media company. " + DG,
    [],
    ["synthesis", "media-empire", "pattern-library", "media-business", "media-business-batch"])

add(HBO, "strategy",
    "SYNTHESIS: lenses only, read against current reality",
    "These media-empire patterns are inspiration and a pattern library, not a template. Taken literally they could push the operator toward building a network, a channel, or a content machine. Read against CURRENT_OPERATOR_REALITY_BRIEF (solo operator, ideation/build mode, loading the backend) and the identity-and-brand-optionality guardrails, they are decision-support lenses that widen and pressure-test the option set, keeping SNIPED's direction reversible until the operator decides.",
    "Use media-empire patterns to expand and stress-test options, not to commit to building a media company; keep direction reversible.",
    "Explicitly preserves optionality: media-business patterns are lenses only. No final SNIPED, SNIPED Media, or BASEPLATE direction; SNIPED does not become a media company by default; photography stays one option among several. " + DG,
    [],
    ["optionality", "pattern-library", "guardrail", "strategy", "media-business-batch"])

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
print("media-business count:", dist.get("media-business", 0))
for bad in ("media", "entertainment", "programming"):
    assert bad not in dist, f"FORBIDDEN domain used: {bad}"
print("forbidden domains (media/entertainment/programming) used: NONE")
print("em-dashes in output:", sum(json.dumps(c, ensure_ascii=False).count(EM) for c in C))
