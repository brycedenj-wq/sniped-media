#!/usr/bin/env python3
"""Author ADVERTISING_RECOVERY chunks (3 recovered advertising/copywriting canon books).

12-field schema. batch_id ADVERTISING_RECOVERY. chunk_id ADVERTISING_RECOVERY_NNN.
Existing domains only (copywriting anchors): copywriting, brand-psychology, brand,
positioning, offer-design, sales-flow, meta-advertising, commercial-architecture,
content-strategy, strategy, operator-process, ethics. NO marketing/persuasion or any new
domain. Per-source attribution. Short illustrative quotes only. Em-dash swept to ' · '.
Every chunk references CURRENT_OPERATOR_REALITY_BRIEF; closing chunk makes the optionality
guardrail explicit (decision-support + execution layer, NOT a directive that BJ become a
copywriter or run an agency).
"""
import json
import os

REPO = os.path.expanduser("~/AI-Brain-Refinery")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/ADVERTISING_RECOVERY_CHUNKS.jsonl")
BID = "ADVERTISING_RECOVERY"

OGILVY = ("Confessions of an Advertising Man", "confessions_of_an_advertising_man_ogilvy.txt", "David Ogilvy")
SUGAR = ("The Adweek Copywriting Handbook", "the_adweek_copywriting_handbook_sugarman.txt", "Joseph Sugarman")
HALBERT = ("The Boron Letters", "the_boron_letters_halbert.txt", "Gary Halbert")
SYN = ("ADVERTISING_RECOVERY: cross-source synthesis", "confessions_of_an_advertising_man_ogilvy.txt", "Ogilvy / Sugarman / Halbert (SNIPED synthesis)")

GUARD = (
    " Held as a decision-support + execution-layer lens read against "
    "CURRENT_OPERATOR_REALITY_BRIEF: craft BJ can apply to copy, positioning, and offers for "
    "whatever he builds, NOT a directive that BJ become a copywriter or run an agency. Does "
    "not finalize SNIPED, SNIPED Media, or BASEPLATE direction; photography remains one option "
    "among several."
)

C = [
    # OGILVY (6)
    (OGILVY, "copywriting", "The headline is the decisive element",
     "Ogilvy holds the headline as the most important element of most ads: about five times as many people read the headline as the body, so a headline that fails to sell has wasted most of the spend. He wrote at least sixteen headlines per ad and tested relentlessly.",
     "Spend most of your effort on the opening line/headline; it does the majority of the selling, so generate many candidates and test rather than settling on the first.",
     "The opening is where attention is won or lost. A lens for how BJ would lead any piece of communication (a page, a pitch, a post) with a headline that earns the next read.",
     ["\"ticket on the meat\""], ["headline", "copywriting", "attention", "testing", "advertising"]),
    (OGILVY, "brand", "Advertising builds the long-term brand image",
     "Ogilvy argued every ad is a long-term investment in the brand image, the complex symbol the product accumulates over time; cheap tricks that sell today can erode the symbol that sustains a premium tomorrow.",
     "Treat each piece of communication as a deposit into a durable brand image, not just a short-term response grab; consistency compounds into a premium symbol.",
     "Brand as a compounding symbol. A lens for BJ to keep every output consistent with the long-term image he wants, not just the immediate reaction.",
     ["\"the brand image\""], ["brand", "brand-image", "long-term", "consistency", "advertising"]),
    (OGILVY, "meta-advertising", "Do your homework: research and test everything",
     "Ogilvy's discipline: study the product and the market before writing, and test promises, media, and headlines rather than trusting opinion. He credited research, not flair, for most of his results.",
     "Ground creative work in homework and measurement: test the promise, the channel, and the hook instead of arguing from taste; let evidence settle disputes.",
     "Evidence over opinion. A lens for how BJ would validate any offer or message with small tests before scaling, fitting the lean-operator posture.",
     ["\"Test your promise\""], ["research", "testing", "evidence", "meta-advertising", "discipline"]),
    (OGILVY, "positioning", "The promise and the big idea sell, or the ad is ignored",
     "Ogilvy insisted an ad must contain a clear promise/benefit and ideally a big idea; without a compelling promise, even beautiful execution fails to sell. The positioning of what is offered matters more than the polish.",
     "Lead with a sharp, specific promise (what the customer gets) and a single big idea; execution serves the promise, it does not replace it.",
     "Promise before polish. A lens for BJ to define the concrete benefit and core idea of any offer before worrying about presentation.",
     ["\"sell or else\""], ["positioning", "promise", "big-idea", "benefit", "advertising"]),
    (OGILVY, "operator-process", "Run the shop: indispensability, standards, and leadership",
     "Confessions opens with how to manage an agency, drawn from Ogilvy's years in a Paris kitchen: make yourself indispensable to clients, inspect every campaign before it ships, set exacting standards, and lead from the front. (Agency-running material, included where it yields an operator principle.)",
     "Operator excellence comes from indispensability, personally inspecting the work before it ships, and holding a visible high standard; leaders earn authority by craft.",
     "Operator-shop discipline. A lens for how BJ would run any small operation: be indispensable to clients, inspect output, and set the standard himself.",
     ["\"make yourself indispensable\""], ["operator-process", "leadership", "standards", "management", "craft"]),
    (OGILVY, "ethics", "Never write an ad you would not want your family to read",
     "Ogilvy's stated rule: never write an advertisement you would not want your own family to read, and do not advertise something you would not let your family use. Honesty is both principle and long-run brand protection.",
     "Hold a personal honesty test for any claim (would I want my family to read/believe this?); deceptive copy wins once and erodes trust thereafter.",
     "An ethics test for any message BJ ships: would he stand behind the claim to people he respects? Integrity and long-run trust align.",
     ["\"Never Write an Advertisement\""], ["ethics", "honesty", "trust", "integrity", "advertising"]),
    # SUGARMAN (5)
    (SUGAR, "copywriting", "The first sentence has one job: get the second read",
     "Sugarman's core mechanic: every element of an ad (headline, image, layout) exists only to get the first sentence read, and the first sentence's only purpose is to get the second sentence read, and so on. Make the first sentence short and almost impossible not to finish.",
     "Engineer each line to pull the reader into the next; the first sentence should be so easy and intriguing it is read almost involuntarily.",
     "Momentum from the first line. A lens for structuring any BJ writing so the opening compels continued reading rather than front-loading information.",
     ["\"get the second sentence read\""], ["copywriting", "first-sentence", "momentum", "openings", "advertising"]),
    (SUGAR, "copywriting", "The slippery slide: make stopping hard",
     "Sugarman's 'slippery slide': great copy is so engaging the reader slides down it unable to stop, every sentence greasing the way to the next. Friction (confusion, a dull line) breaks the slide and loses the reader.",
     "Remove every point of friction and add pull so the reader cannot comfortably stop; flow is engineered sentence by sentence, not assumed.",
     "Engineered flow. A lens for BJ to ruthlessly cut friction and keep momentum in anything meant to be read all the way through.",
     ["\"the slippery slide\""], ["copywriting", "flow", "engagement", "friction", "advertising"]),
    (SUGAR, "content-strategy", "Seeds of curiosity keep the reader moving",
     "Sugarman plants 'seeds of curiosity': short hooks at the end of sections (more on that in a moment) that create an open loop pulling the reader forward through the piece.",
     "Open curiosity loops that the reader needs to close, pacing engagement across a long piece rather than relying on a single hook.",
     "Pacing attention across a piece. A lens for how BJ would structure longer content or a sequence so each section earns the next.",
     ["\"seeds of curiosity\""], ["content-strategy", "curiosity", "open-loops", "engagement", "pacing"]),
    (SUGAR, "brand-psychology", "Sell on emotion, justify with logic",
     "Sugarman frames copy as communicating facts and emotions: people buy on emotion and justify with logic, and every word carries an emotional charge, so word choice is an emotional design decision, not just an informational one.",
     "Lead the buying decision with emotion and supply the logic that lets the buyer justify it; choose words for their emotional charge, not only their meaning.",
     "Emotion drives the decision. A lens for how BJ would frame value (the feeling first, the rationale second) in any offer or message.",
     ["\"facts and emotions\""], ["brand-psychology", "emotion", "word-choice", "buying-decision", "advertising"]),
    (SUGAR, "brand-psychology", "Psychological triggers behind the buy",
     "Sugarman catalogs psychological triggers (consistency, social proof, scarcity, involvement, honesty, storytelling, and more) that move a prospect toward purchase, used deliberately and ethically within the copy.",
     "Know the recurring psychological triggers that move decisions and apply the ones that genuinely fit the offer; triggers are levers, not gimmicks.",
     "A toolkit of decision levers. A lens for BJ to recognize which genuine motivators apply to a real offer, used honestly.",
     ["\"psychological triggers\""], ["brand-psychology", "triggers", "motivation", "influence", "advertising"]),
    # HALBERT (4)
    (HALBERT, "strategy", "The starving crowd: the market beats the copy",
     "Halbert's most famous lesson: asked what advantage he would want selling hamburgers, the answer is not the best meat or location but a starving crowd. The market (who you sell to, and their hunger) matters more than the copy itself.",
     "Choose the market before the message: a hungry, reachable audience with a real need outperforms brilliant copy aimed at an indifferent one.",
     "Demand before craft. A lens for BJ to find a genuinely hungry market for any offer first, rather than perfecting a message no one is waiting for.",
     ["\"a starving crowd\""], ["strategy", "market-first", "demand", "audience", "direct-response"]),
    (HALBERT, "copywriting", "Write like a personal letter to one reader",
     "The Boron Letters (written from prison to his son) model copy as a personal, conversational letter to a single reader, plain and direct, hooking from the first impression because you never get a second chance at one.",
     "Write to one person in plain, personal language and hook them at the first impression; conversational directness outperforms polished corporate voice.",
     "One-to-one voice. A lens for how BJ would write to a single real reader rather than an abstract audience, with a strong opening.",
     ["\"a first impression\""], ["copywriting", "conversational", "voice", "directness", "direct-response"]),
    (HALBERT, "offer-design", "The offer and AIDA: structure the ask",
     "Halbert teaches the direct-response fundamentals: a strong, specific offer carried through AIDA (attention, interest, desire, action) with a clear, low-friction call to action; the offer is the engine, the copy is the vehicle.",
     "Build a specific, compelling offer and walk the reader through attention to action with an explicit, easy ask; a weak offer cannot be rescued by copy.",
     "Offer first, then the ask. A lens for how BJ would construct and present any offer with a clear path to a single action.",
     ["\"AIDA\""], ["offer-design", "aida", "call-to-action", "offer", "direct-response"]),
    (HALBERT, "sales-flow", "The list and the response sequence",
     "Halbert stresses the list/market and the mechanics of direct mail: who receives the message and the response sequence (testing, follow-up, the economics of a campaign) determine results as much as the words.",
     "Treat the audience list and the response sequence as first-class variables: test, follow up, and measure the campaign's economics, not just the creative.",
     "The plumbing behind the message. A lens for BJ to design the sequence and measurement around any offer, not just the pitch itself.",
     ["\"the list\""], ["sales-flow", "list", "direct-mail", "sequence", "testing"]),
    # SYNTHESIS (1)
    (SYN, "commercial-architecture", "Synthesis: the demand-capture execution layer + optionality guardrail",
     "Across Ogilvy, Sugarman, and Halbert a single execution stack emerges: pick a hungry market (Halbert), make a clear promise and a big idea (Ogilvy), win the first line and keep the slippery slide (Sugarman), sell on emotion and justify with logic, carry a specific offer through to an easy action, protect the long-term brand image, test everything, and stay honest. This completes the BATCH_009 advertising canon. This is the closing synthesis chunk.",
     "Demand capture is an engineerable stack: market then promise then opening then emotional pull then offer then action, all measured and kept honest and on-brand.",
     "The integrated demand-capture craft as an execution layer BJ can apply to any offer, explicitly a toolkit and decision-support lens, not a directive to become a copywriter or run an agency." + GUARD,
     ["\"a starving crowd\""], ["synthesis", "demand-capture", "execution-layer", "optionality", "advertising"]),
]


def sweep(s):
    return s.replace(chr(0x2014), " · ").replace(chr(0x2013), "-")


def main():
    if os.path.exists(OUT):
        raise SystemExit(f"REFUSE: {OUT} exists")
    last = len(C) - 1
    lines = []
    for i, (src, domain, concept, summary, principle, relevance, quotes, tags) in enumerate(C, start=1):
        title, sfile, author = src
        sr = relevance if i - 1 == last else relevance + GUARD
        rec = {
            "chunk_id": f"{BID}_{i:03d}",
            "batch_id": BID,
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": sr,
            "direct_quotes": quotes,
            "tags": tags,
        }
        for k, v in rec.items():
            if isinstance(v, str):
                rec[k] = sweep(v)
            elif isinstance(v, list):
                rec[k] = [sweep(x) if isinstance(x, str) else x for x in v]
        lines.append(json.dumps(rec, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {len(lines)} chunks -> {OUT}")


if __name__ == "__main__":
    main()
