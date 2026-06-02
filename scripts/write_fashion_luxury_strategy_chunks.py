#!/usr/bin/env python3
"""Write FASHION_LUXURY_STRATEGY_CHUNKS.jsonl · 13 curated chunks · 3 sources.

batch_id: FASHION_LUXURY_STRATEGY · chunk_id: FASHION_LUXURY_STRATEGY_NNN
Existing domains only (status anchor). No new domain. `taste` reused (warranted,
not created). No em-dashes. Curated luxury/fashion commercial-strategy extraction
(NOT fashion-history/memoir/lifestyle summary). Decision-neutral: NOT a directive
and NOT a finalized SNIPED brand. Guardrail in every chunk.
"""
import json
import os

OUT = os.path.expanduser(
    "~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/FASHION_LUXURY_STRATEGY_CHUNKS.jsonl")

KAP = ("The Luxury Strategy", "the_luxury_strategy_kapferer.txt", "Jean-Noel Kapferer and Vincent Bastien")
DEL = ("Deluxe", "deluxe_thomas.txt", "Dana Thomas")
AGINS = ("The End of Fashion", "the_end_of_fashion_agins.txt", "Teri Agins")

GUARD = (" Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support and "
         "pattern-library only, not doctrine and not a directive: not a directive that "
         "BJ become a fashion brand, luxury influencer, streetwear founder, lifestyle "
         "creator, designer persona, clout account, or aesthetics-only operator. Fashion "
         "and luxury are held as symbolic value, taste systems, status architecture, "
         "scarcity, cultural signaling, craft, and commercial perception. No final SNIPED, "
         "SNIPED Media, or BASEPLATE direction; photography remains one option among several.")

# (source, domain, concept, summary, usable_principle, relevance_lead, quotes, tags)
ROWS = [
    # ---- THE LUXURY STRATEGY (Kapferer) · 5 + synthesis ----
    (KAP, "status",
     "Luxury is not comparative: superlative, never comparative",
     "Kapferer's foundational inversion is that luxury is not positioned against competitors the way "
     "ordinary or premium goods are; it is superlative rather than comparative. A premium product "
     "argues best-value-for-money against rivals, but a true luxury object stands alone as a symbol of "
     "social rank and self-worth, judged by its own myth and not by a feature comparison.",
     "Distinguish superlative positioning (stand alone as a symbol, refuse comparison) from comparative "
     "positioning (win on value versus rivals); they are different games with different rules.",
     "For BJ this separates a premium offer (compete on value) from a true high-status offer (refuse "
     "comparison, sell the symbol), a positioning choice held as analysis, not a brand directive.",
     ["luxury is not comparative", "Superlative, never comparative"],
     ["luxury-vs-premium", "non-comparative", "symbolic-value", "status", "positioning"]),

    (KAP, "strategy",
     "The anti-laws of luxury marketing: deliberate inversion",
     "Kapferer frames luxury management as a set of anti-laws that deliberately invert ordinary "
     "marketing: do not pander to customers' wishes, dominate the client rather than serve every "
     "demand, communicate to those you are not targeting, and keep non-enthusiasts out. The logic is "
     "that desire is sustained by distance and authority, not by accommodation.",
     "When building desire rather than convenience, inverting the service-everyone reflex (lead taste, "
     "hold authority, do not chase every customer) can be the deliberate strategy.",
     "BJ can recognize when the right move is the anti-law (lead the client, do not pander) versus the "
     "ordinary law (serve the customer), choosing by the kind of value being built.",
     ["anti-laws of marketing", "Dominate the client"],
     ["anti-laws", "inversion", "desire", "authority", "strategy"]),

    (KAP, "commercial-architecture",
     "Scarcity and the price architecture: luxury sets the price",
     "In Kapferer's model luxury runs the price logic backward: make it difficult to buy, do not "
     "respond to rising demand by expanding supply, and raise prices over time to increase rather than "
     "dampen desire. Crucially, luxury sets the price, the price does not set the luxury; price is a "
     "signal of rank, not a clearing mechanism.",
     "Use scarcity and a rising price as desire engines, not friction to remove; in a status economy "
     "price signals rank, so it can lead rather than follow demand.",
     "BJ can read where scarcity and a deliberately high, rising price would build desire (the status "
     "logic) versus where accessibility wins (the volume logic), as a structural choice.",
     ["Luxury sets the price", "Do not sell"],
     ["scarcity", "pricing", "demand", "rank-signal", "commercial-architecture"]),

    (KAP, "brand",
     "Advertising creates the dream, not the sale",
     "Kapferer holds that in luxury the role of advertising is not to sell but to build and sustain the "
     "dream: the imaginative aura that makes the object desirable and the brand non-substitutable. "
     "Communication is aimed partly at people who will never buy, because their admiration is what "
     "gives the owner status.",
     "Separate dream-building communication (sustain the aura, address the non-buyers whose admiration "
     "creates status) from sales activation; the dream is the asset.",
     "BJ can treat some communication as dream-building (the aura others admire) rather than direct "
     "response, recognizing that perceived status is partly conferred by non-buyers.",
     ["advertising is not to sell"],
     ["advertising", "the-dream", "aura", "desire", "non-buyers"]),

    (KAP, "aesthetics",
     "Craft, origin, and time: the work that justifies the myth",
     "For Kapferer the luxury object is grounded in real craft, complexity, and a protected origin (do "
     "not relocate your factories), and it is built to last and even appreciate over time. The "
     "handwork, the country of origin, and the durability are not nostalgia but the substance that "
     "makes the symbolic premium credible.",
     "Anchor a premium claim in real, visible craft and a protected origin that endures; the symbol is "
     "only credible if the underlying work is real.",
     "BJ's actual craft and the durability of his work are the substance that would make any premium "
     "perception credible; the myth must be backed by real making.",
     ["Don't relocate your factories"],
     ["craft", "origin", "durability", "complexity", "authenticity"]),

    # ---- DELUXE (Thomas) · 4 ----
    (DEL, "status",
     "The democratization of luxury into a mass status symbol",
     "Thomas documents how the conglomerates turned luxury into democratic, mass-produced status: the "
     "must-have handbag of the season, entry-level perfume and cosmetics that let aspirational buyers "
     "own a small piece of the brand's dream, and logos as recognizable as fast-food signs. Luxury "
     "broadened far beyond the wealthy into a widely sold status symbol.",
     "Broadening a status symbol to the aspirational middle through entry-level products expands "
     "revenue but converts exclusivity into mass recognition, a tradeoff with long-run cost.",
     "BJ can see the masstige tradeoff clearly: entry-level access grows reach but spends the "
     "exclusivity that made the symbol valuable, a structural tension to weigh, not a path to copy.",
     ["mass-produced luxury", "democratic luxury"],
     ["democratization", "masstige", "status-symbol", "aspiration", "reach-vs-exclusivity"]),

    (DEL, "ethics",
     "Going public erodes craft and the luxury promise",
     "Thomas argues that once luxury houses went public, quarterly profit pressure forced them to cut "
     "corners: outsourcing production, substituting inferior materials, replacing handcraft with "
     "assembly lines, and sometimes falsely implying European making, while raising prices. The "
     "promise of craftsmanship was hollowed even as the price and marketing rose.",
     "Watch for the gap between a premium promise and the eroded substance behind it; short-term "
     "profit pressure can quietly hollow the very quality a brand still charges for.",
     "BJ can hold the integrity line as a deliberate choice: keep the substance real rather than "
     "harvest a reputation, recognizing how easily margin pressure erodes a craft promise.",
     ["transforming creativity into profitability", "lost its luster"],
     ["integrity", "craft-erosion", "profit-pressure", "outsourcing", "promise-gap"]),

    (DEL, "aesthetics",
     "The surviving craft beneath the volume",
     "Even inside the mass-luxury machine, Thomas finds the real craft persisting at the margins: the "
     "Vuitton artisans at Asnieres still building trunks and special-order pieces by hand, one maker "
     "per object, the way they did 150 years ago. The genuine handwork survives as a small, slow, "
     "high-skill remnant beneath the industrialized volume.",
     "Preserve a genuine craft core even when volume is industrialized; the slow, single-maker work is "
     "what keeps the claim of quality honest.",
     "BJ can keep a real craft core (the work done properly, by hand where it matters) as the honest "
     "anchor beneath anything scaled, the part that cannot be faked.",
     ["made by hand"],
     ["craft", "handwork", "quality-core", "slow-making", "authenticity"]),

    (DEL, "status",
     "Manufactured desire: the dream sold at the margins",
     "Thomas shows luxury growth driven by manufactured desire: calculated marketing with fashion-"
     "magazine support creates the season's must-have, and the dream is monetized through high-margin "
     "accessories, perfume, and cosmetics that let almost anyone buy a token of belonging. The "
     "aspiration is engineered, and its shadow includes rampant counterfeiting.",
     "Recognize when desire is manufactured (the engineered must-have, the affordable token of "
     "belonging) so you read the aspiration honestly rather than being moved by it.",
     "BJ can read manufactured aspiration for what it is (an engineered status hunger), useful as "
     "market literacy and as a caution against building on hype rather than substance.",
     ["piece of the brand's dream"],
     ["manufactured-desire", "aspiration", "must-have", "margins", "market-literacy"]),

    # ---- THE END OF FASHION (Agins) · 3 ----
    (AGINS, "culture",
     "The end of trickle-down: fashion off the pedestal",
     "Agins charts the collapse of the old trickle-down system in which Paris couturiers and elite "
     "boutiques dictated how everyone dressed. As good-looking clothes became available at every price "
     "level (Gap, Banana Republic, J. Crew, Target), fashion came off its pedestal and the designer "
     "label began to look like a rip-off, with bargain-hunting a badge of honor even among the "
     "well-to-do.",
     "When access broadens at every price level, an old prestige hierarchy can collapse and the "
     "premium label loses its automatic authority; the gatekeeper economy erodes.",
     "BJ can read when a prestige hierarchy is collapsing under broad access, so he does not bank on "
     "an authority (the label, the gatekeeper) that the market has stopped honoring.",
     ["the end of fashion"],
     ["trickle-down", "democratization", "prestige-collapse", "access", "culture"]),

    (AGINS, "taste",
     "The commoditization of fashion: taste decoupled from price",
     "Agins describes the commoditization of clothing: shoppers discovered (with help from Consumer "
     "Reports tests) that a cheap shirt could match an expensive one in quality, so the truism that "
     "you get what you pay for broke down. Taste and value detached from the designer price, and "
     "Target's tagline that it is fashionable to pay less captured the shift.",
     "When buyers learn that quality and taste are decoupled from price, the price-equals-quality "
     "signal collapses; durable taste must be demonstrated, not asserted by a price tag.",
     "BJ can assume informed buyers no longer equate price with quality or taste, so the work must "
     "demonstrate taste and value directly rather than rely on a premium signal.",
     ["commoditization of fashion"],
     ["commoditization", "taste", "price-quality-decoupling", "value", "perception"]),

    (AGINS, "brand",
     "Image is the form, marketing is the function",
     "Agins's thesis is that fashion's creativity migrated from the clothes to the marketing: the "
     "leading designers became billion-dollar, publicly traded apparel-and-licensing empires that stop "
     "gambling on fashion and instead sell image. As she puts it, image is the form and marketing is "
     "the function; the designer's name became the brand and the real product is perception.",
     "Recognize when the real product has become the image and the brand rather than the artifact; in "
     "a commoditized category, perception and the name carry the margin.",
     "BJ can decide deliberately how much of his value sits in the artifact versus the image and name, "
     "reading clearly that in many categories the brand is the product, not a directive to chase image.",
     ["Image is the form", "selling image"],
     ["image", "designer-as-brand", "marketing", "perception", "licensing"]),

    # ---- SYNTHESIS · 1 ----
    (KAP, "operator-doctrine",
     "Synthesis: the luxury/fashion symbolic-value operator toolkit",
     "Across the three sources a single toolkit emerges: luxury is manufactured non-comparable status "
     "built through the anti-laws (scarcity, rising price, dream-advertising) and grounded in real "
     "craft and origin (Kapferer); democratization and going-public erode that substance into "
     "mass-produced status while a craft remnant survives (Thomas); and once access broadens and "
     "price decouples from quality, the real product becomes image and the brand (Agins). It is a "
     "pattern-library for symbolic value, scarcity, status architecture, taste, and commercial "
     "perception.",
     "Combine symbolic-value literacy (how status, scarcity, and the dream are engineered), the "
     "craft-versus-commoditization tradeoff, and the image-as-product shift into a perception toolkit, "
     "held as analysis rather than a brand to launch.",
     "BJ holds this as symbolic-value and commercial-perception literacy for his build-mode stage, "
     "NOT a directive to become a fashion or luxury brand or to chase image over substance.",
     [],
     ["synthesis", "symbolic-value", "status-architecture", "commercial-perception", "operator-toolkit"]),
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
    for i, (src, domain, concept, summary, principle, rel, quotes, tags) in enumerate(ROWS, 1):
        title, sfile, author = src
        r = {
            "chunk_id": f"FASHION_LUXURY_STRATEGY_{i:03d}",
            "batch_id": "FASHION_LUXURY_STRATEGY",
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": rel + GUARD,
            "direct_quotes": quotes,
            "tags": tags,
        }
        rows.append(r)

    for r in rows:
        for q in r["direct_quotes"]:
            assert len(q.split()) <= 6, f"quote too long in {r['chunk_id']}: {q}"

    forbidden = {"luxury", "fashion", "style", "designer", "apparel", "streetwear",
                 "hype", "clout", "lifestyle", "influencer"}
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
