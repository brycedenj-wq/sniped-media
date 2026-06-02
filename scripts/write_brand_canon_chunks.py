#!/usr/bin/env python3
"""Write BRAND_CANON_CHUNKS.jsonl · 15 curated chunks · 5 sources.

batch_id: BRAND_CANON · chunk_id: BRAND_CANON_NNN
Existing domains only (brand anchor). No new domain. `taste` NOT used (routes to
aesthetics/culture/status/brand). No em-dashes. Curated brand-as-perception /
identity-system / naming-craft extraction (NOT chapter summary). Decision-neutral:
NOT a directive and NOT a finalized SNIPED brand or name. Guardrail in every chunk.
"""
import json
import os

OUT = os.path.expanduser(
    "~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/BRAND_CANON_CHUNKS.jsonl")

GAP = ("The Brand Gap", "the_brand_gap_neumeier.txt", "Marty Neumeier")
WHEELER = ("Designing Brand Identity", "designing_brand_identity_wheeler.txt", "Alina Wheeler and Rob Meyerson")
AIREY = ("Identity Designed", "identity_designed_airey.txt", "David Airey")
NAMING = ("Brand Naming", "brand_naming_meyerson.txt", "Rob Meyerson")
WATKINS = ("Hello, My Name Is Awesome", "hello_my_name_is_awesome_watkins.txt", "Alexandra Watkins")

GUARD = (" Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support and "
         "pattern-library only, not doctrine and not a directive: not a directive that "
         "BJ become a fashion brand, luxury influencer, personal-brand guru, lifestyle "
         "creator, agency bro, clout account, or aesthetics-only operator. Brand material "
         "is held as market perception, symbolic capital, category design, proof "
         "architecture, and taste-as-strategy. No final SNIPED, SNIPED Media, or BASEPLATE "
         "direction; photography remains one option among several.")
NAMING_CLAUSE = (" Naming is held as naming-craft, NOT a directive to finalize a SNIPED, "
                 "SNIPED Media, or BASEPLATE name.")

# (source, domain, naming_flag, concept, summary, usable_principle, relevance_lead, quotes, tags)
ROWS = [
    # ---- THE BRAND GAP (Neumeier) · 3 ----
    (GAP, "brand", False,
     "A brand is a person's gut feeling, not what you say it is",
     "Neumeier defines a brand not as a logo, an identity system, or a product, but as a person's gut "
     "feeling about a product, service, or company. Because it lives in other people's minds, a brand "
     "is not what you say it is, it is what they say it is; when enough individuals converge on the "
     "same gut feeling, a brand exists.",
     "Treat the brand as market perception you influence but do not own; manage the gut feeling in the "
     "audience's mind rather than the message you broadcast.",
     "For BJ this reframes any brand question as: what gut feeling forms in the market, not what claim "
     "is made; the work and the proof shape perception more than the assertion.",
     ["a person's gut feeling", "what THEY say it is"],
     ["brand-as-perception", "gut-feeling", "market-perception", "definition", "audience-owned"]),

    (GAP, "aesthetics", False,
     "The brand gap and the charismatic brand: bridging strategy and creativity",
     "Neumeier names the brand gap as the chasm between left-brain strategy (logic) and right-brain "
     "creativity (magic); brands fail at the point of contact when the two are not bridged. Brands that "
     "close the gap become charismatic (a product for which people believe there is no substitute), "
     "and aesthetics is the bridge because it is the language of feeling in an information-rich, "
     "time-poor world.",
     "Bridge logic and magic deliberately; use aesthetics as a strategic asset (the language of "
     "feeling) that resists commoditization, not as decoration.",
     "BJ's visual craft is strategic leverage here: aesthetics done with intent shrinks the psychic "
     "distance to an audience and resists being commoditized, held as a tool not a lifestyle.",
     ["the language of feeling", "logic and magic"],
     ["brand-gap", "charismatic-brand", "aesthetics-as-strategy", "commoditization-resistance", "feeling"]),

    (GAP, "strategy", False,
     "The five disciplines and the three differentiation questions",
     "Neumeier organizes brand-building into five disciplines: differentiate, collaborate, innovate, "
     "validate, and cultivate. Differentiation starts with three blunt questions every brand must "
     "answer cleanly: who are you, what do you do, and why does it matter, with the third being the "
     "hardest and most decisive.",
     "Earn a brand by answering who-you-are, what-you-do, and why-it-matters cleanly, then differentiate, "
     "collaborate, innovate, validate, and cultivate as a repeatable discipline.",
     "BJ can pressure-test any offer or direction against the three questions (especially why it "
     "matters) before committing, as a clarity filter, not a branding mandate.",
     ["Who are you?"],
     ["five-disciplines", "differentiation", "three-questions", "clarity", "why-it-matters"]),

    # ---- DESIGNING BRAND IDENTITY (Wheeler) · 4 ----
    (WHEELER, "brand", False,
     "Brand identity as recognition infrastructure",
     "Wheeler distinguishes brand (the perception) from brand identity (the tangible expression that "
     "appeals to the senses: seen, touched, heard, watched). Brand identity fuels recognition, "
     "amplifies differentiation, and makes big ideas and meaning accessible, turning an abstract brand "
     "into something people can perceive and remember.",
     "Build identity as recognition infrastructure: a tangible, sensory system that makes an abstract "
     "promise recognizable and repeatable, not a one-off logo.",
     "BJ can treat a visual system as recognition infrastructure for whatever he builds, designed for "
     "memory and differentiation, held as craft rather than a finalized identity.",
     ["fuels recognition"],
     ["brand-identity", "recognition", "differentiation", "sensory-system", "memory"]),

    (WHEELER, "commercial-architecture", False,
     "The brand-identity ideals: the criteria for an effective system",
     "Wheeler sets out ideals that an effective brand identity should meet: vision, meaning, "
     "authenticity, coherence, flexibility, commitment, value, differentiation, and durability. These "
     "function as evaluation criteria for whether an identity system will hold up as a strategic asset "
     "over time rather than a passing aesthetic.",
     "Judge any identity or system against durable criteria (vision, meaning, authenticity, coherence, "
     "flexibility, commitment, value, differentiation, durability), not against taste of the moment.",
     "BJ can use these ideals as a checklist for whether any system he builds is coherent and durable "
     "enough to be an asset, a quality bar rather than a brand directive.",
     ["brand ideals"],
     ["brand-ideals", "criteria", "durability", "coherence", "strategic-asset"]),

    (WHEELER, "commercial-architecture", False,
     "The disciplined process and the primacy of touchpoints",
     "Wheeler frames brand identity as a managed process moving through phases (conducting research, "
     "clarifying strategy, designing identity, creating touchpoints, and managing assets) rather than "
     "a one-time creative act. The brand is actually experienced at every touchpoint, so consistency "
     "and governance across touchpoints are where the brand is won or lost.",
     "Run identity as a governed process and manage every touchpoint as the real brand experience; "
     "consistency across touchpoints compounds, inconsistency erodes.",
     "BJ can treat each point of contact (a gallery, a feed, a delivery, a reply) as a touchpoint that "
     "either compounds or erodes perception, managed as a system.",
     ["Creating touchpoints"],
     ["process", "touchpoints", "consistency", "governance", "brand-management"]),

    (WHEELER, "positioning", False,
     "Strategy and positioning as the foundation under the design",
     "Wheeler is emphatic that brand identity must be built on a clear brand strategy and positioning: "
     "the big idea, the differentiated position, and the meaning come before the visual expression. "
     "Design without an agreed strategy is decoration; strategy gives the identity something true to "
     "express.",
     "Settle positioning and the big idea before designing the expression; the visual system should "
     "express a decided position, not substitute for one.",
     "BJ should resolve what a thing actually is and where it sits in the market before investing in "
     "its look, holding positioning as the upstream decision (without finalizing SNIPED's).",
     [],
     ["positioning", "brand-strategy", "big-idea", "foundation", "meaning-first"]),

    # ---- IDENTITY DESIGNED (Airey) · 3 ----
    (AIREY, "aesthetics", False,
     "Visual identity as distinction in saturated markets",
     "Airey frames a visual identity as being to a business what faces are to people: the instrument of "
     "recognition. In saturated worldwide markets the designer's challenge and responsibility is to "
     "craft genuine distinction, which is why design has moved from middle-management meetings into the "
     "boardroom as a driver of business value.",
     "Design for recognition and genuine distinction in a crowded market; visual identity is a "
     "business-value driver, not surface dressing.",
     "BJ's eye for distinction is a business asset: in a saturated field, a recognizable, genuinely "
     "distinct visual identity is leverage, held as craft, not an aesthetics-only identity.",
     ["faces are to people"],
     ["visual-identity", "distinction", "saturated-market", "recognition", "business-value"]),

    (AIREY, "brand", False,
     "Consistency means consistently distinctive, not sameness",
     "Airey argues great brands are consistent, but consistency is wrongly equated with sameness; it "
     "means being consistently distinctive and vibrant. A single typeface used many ways, a distinctive "
     "palette with compelling copy, or a coherent kit of complementary elements can ingrain a brand "
     "experience into memory without becoming monotonous.",
     "Pursue consistency as a coherent, distinctive system that repeats with variation, not rigid "
     "uniformity; coherence is what ingrains a brand into memory.",
     "BJ can keep a recognizable through-line across outputs (a palette, a type voice, a treatment) "
     "that is consistent yet alive, building memory without sameness.",
     ["consistently distinctive"],
     ["consistency", "coherence", "distinctive", "system", "memory"]),

    (AIREY, "operator-doctrine", False,
     "The brief as the structural framework that disciplines the work",
     "Across the studios Airey interviews, the creative brief is the structural framework that keeps a "
     "project honest: agreed up front, it becomes the benchmark every creative route is judged against, "
     "so subjective preference (a CEO who dislikes blue) is overruled by whether the work serves the "
     "agreed objectives. The best studios present two strong routes over six, concentrating effort.",
     "Anchor creative work to an agreed brief and judge against it, not taste; constrain options to a "
     "few strong ones tied tightly to the objectives.",
     "BJ can write a short brief before any build so decisions are judged against stated objectives "
     "rather than mood, and resist proliferating options, a discipline transferable beyond design.",
     ["the structural framework"],
     ["creative-brief", "framework", "benchmark", "discipline", "objectives-over-taste"]),

    # ---- BRAND NAMING (Meyerson) · 2 ----
    (NAMING, "brand", True,
     "The name as the number-one touchpoint and a strategic judgment",
     "Meyerson argues you do not have a brand until you have a name, and the name is the number-one "
     "touchpoint a company or product will ever own: one of the first, longest-lasting, most "
     "consequential identity decisions. A good name is a strategic judgment integrating brand strategy, "
     "marketing, research, linguistics, and IP law, scored against positioning goals, performance "
     "criteria, and legal availability.",
     "Treat a name as a high-leverage, long-lived strategic asset judged against positioning, "
     "performance, and availability, not a casual or contest decision.",
     "If BJ ever names something, this is the bar: a name judged against position, performance, and "
     "availability, held as craft and NOT a cue to finalize a SNIPED name now.",
     ["until you have a name"],
     ["naming", "touchpoint", "strategic-asset", "positioning", "availability"]),

    (NAMING, "operator-doctrine", True,
     "The naming process: brief, generate many, narrow, screen, commit",
     "Meyerson lays out the professional naming process as a repeatable, iterative discipline: write a "
     "naming brief, generate hundreds of candidates, whittle to a finalist set, prescreen for trademark "
     "and run linguistic checks, then build consensus and make the commitment. The volume-then-filter "
     "structure and the fortitude to commit are what separate a strategic name from a lucky one.",
     "Run high-stakes creative choices as generate-many-then-filter against hard criteria, then commit "
     "with fortitude; volume plus disciplined screening beats a single bet.",
     "BJ can apply the generate-broadly-then-screen-hard pattern to any high-stakes naming or "
     "positioning choice, held as process discipline, not a directive to name SNIPED.",
     [],
     ["naming-process", "generate-then-filter", "trademark-screen", "commitment", "iteration"]),

    # ---- HELLO MY NAME IS AWESOME (Watkins) · 2 ----
    (WATKINS, "brand-psychology", True,
     "The SMILE and SCRATCH test for memorable names",
     "Watkins gives a practical evaluation checklist: a sticky name should make you SMILE (the five "
     "qualities of a super-sticky name) and avoid the SCRATCH sins (the seven that make a name "
     "spelling-challenged, hard to pronounce, tame, or annoying). The test turns name choice from "
     "subjective debate into a scorable judgment of memorability.",
     "Score a name for memorability against clear qualities and sins rather than arguing taste; a name "
     "you smile at beats one you scratch your head over.",
     "BJ can evaluate any name, handle, or title against a stickiness checklist before adopting it, a "
     "memorability filter held as craft, not a push to rename anything now.",
     ["SMILE", "SCRATCH"],
     ["naming-test", "memorability", "stickiness", "evaluation", "SMILE-SCRATCH"]),

    (WATKINS, "brand-psychology", True,
     "Names land through familiar concepts and emotional resonance",
     "Watkins, an ex-Ogilvy copywriter, argues the most powerful names connect emotionally because they "
     "are built on familiar words and concepts people already understand and like, not on linguistic "
     "engineering, math, or mangled spellings. People want to feel clever, not clueless, so a name that "
     "people get and like outperforms manufactured words.",
     "Build names and language on familiar, emotionally resonant concepts the audience instantly gets, "
     "not on cleverness that makes them feel clueless.",
     "BJ can favor names and copy that land instantly through familiar concepts over manufactured "
     "cleverness, an audience-comprehension principle, not a brand directive.",
     ["get and like"],
     ["naming", "emotional-resonance", "familiarity", "comprehension", "copywriting"]),

    # ---- SYNTHESIS · 1 ----
    (GAP, "operator-doctrine", False,
     "Synthesis: the brand-as-perception operator toolkit",
     "Across the five sources a single toolkit emerges: a brand is market perception you shape but do "
     "not own (Neumeier); identity is the recognition infrastructure and managed touchpoint system that "
     "makes perception repeatable (Wheeler); distinction and brief-disciplined craft win in saturated "
     "markets (Airey); and a name is a high-leverage strategic asset chosen by generate-then-filter and "
     "scored for memory (Meyerson, Watkins). It is a pattern-library for perception, category, proof, "
     "and taste-as-strategy.",
     "Combine perception management, recognition systems, positioning, and naming craft into brand "
     "literacy, treating brand as leverage over how work is perceived, not as a lifestyle or a finalized "
     "identity.",
     "BJ holds this as a brand-perception toolkit for his build-mode stage: shape perception, build "
     "recognition, and name with craft, WITHOUT finalizing SNIPED's brand or name.",
     [],
     ["synthesis", "brand-literacy", "perception", "category-design", "operator-toolkit"]),
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
    for i, (src, domain, naming, concept, summary, principle, rel, quotes, tags) in enumerate(ROWS, 1):
        title, sfile, author = src
        relevance = rel + GUARD + (NAMING_CLAUSE if naming else "")
        r = {
            "chunk_id": f"BRAND_CANON_{i:03d}",
            "batch_id": "BRAND_CANON",
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": relevance,
            "direct_quotes": quotes,
            "tags": tags,
        }
        rows.append(r)

    for r in rows:
        for q in r["direct_quotes"]:
            assert len(q.split()) <= 6, f"quote too long in {r['chunk_id']}: {q}"

    # forbidden-domain guard (incl taste-not-used)
    forbidden = {"branding", "luxury", "fashion", "identity", "creator", "influencer",
                 "personal-brand", "lifestyle", "hype", "clout", "taste"}
    used = {r["domain"] for r in rows}
    assert not (used & forbidden), used & forbidden

    rows = [sweep(r) for r in rows]
    blob = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    assert chr(0x2014) not in blob, "em-dash found in output"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(blob)
    print(f"wrote {len(rows)} chunks to {OUT}")


if __name__ == "__main__":
    main()
