#!/usr/bin/env python3
"""Author DEEP_FINANCE_EXPANSION chunks (8 CORE deep finance/capital sources).

12-field schema. batch_id DEEP_FINANCE_EXPANSION. chunk_id DEEP_FINANCE_EXPANSION_NNN.
Existing domains only (capital anchors): capital, finance, systems-thinking, strategy,
commercial-architecture, operator-doctrine, ethics. NO economics/investing/wealth/ownership
or any new domain. Short illustrative quotes only. Em-dash swept to ' · '. Every chunk
references CURRENT_OPERATOR_REALITY_BRIEF; closing chunk makes the optionality guardrail
explicit (capital/finance is a decision-support lens, NOT a directive that BJ become an
investor or finance brand).
"""
import json
import os

REPO = os.path.expanduser("~/AI-Brain-Refinery")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/DEEP_FINANCE_EXPANSION_CHUNKS.jsonl")
BID = "DEEP_FINANCE_EXPANSION"

SA = ("Security Analysis: Sixth Edition", "security_analysis_graham_dodd.txt", "Benjamin Graham, David Dodd")
SNOW = ("The Snowball: Warren Buffett and the Business of Life", "the_snowball_schroeder.txt", "Alice Schroeder")
II = ("The Intelligent Investor", "the_intelligent_investor_graham.txt", "Benjamin Graham")
MARKS = ("Mastering the Market Cycle: Getting the Odds on Your Side", "mastering_the_market_cycle_marks.txt", "Howard Marks")
KLAR = ("Margin of Safety: Risk-Averse Value Investing Strategies for the Thoughtful Investor", "margin_of_safety_klarman.txt", "Seth A. Klarman")
SOV = ("The Sovereign Individual", "the_sovereign_individual_davidson.txt", "James Dale Davidson, William Rees-Mogg")
LORDS = ("The Lords of Easy Money: How the Federal Reserve Broke the American Economy", "the_lords_of_easy_money_leonard.txt", "Christopher Leonard")
TYC = ("The New Tycoons: Inside the Trillion Dollar Private Equity Industry", "the_new_tycoons_kelly.txt", "Jason Kelly")

GUARD = (
    " Held as a decision-support / pattern-library lens read against "
    "CURRENT_OPERATOR_REALITY_BRIEF: a mental model for understanding ownership beyond "
    "service income, NOT a directive that BJ become an investor or a finance/investing "
    "brand. Does not finalize SNIPED, SNIPED Media, or BASEPLATE direction; photography "
    "remains one option among several."
)

# (source_tuple, domain, concept, summary, usable_principle, sniped_relevance, [quotes], [tags])
C = [
    (SA, "finance", "Intrinsic value and the analyst's job",
     "Security Analysis grounds investing in estimating a security's intrinsic value from facts (assets, earnings, dividends, prospects) rather than from price or crowd opinion. The analyst's job is disciplined appraisal of the business behind the security, separating durable value from market noise.",
     "Value any asset from its underlying fundamentals, not from its quoted price or sentiment; price is what you pay, value is what the business is actually worth.",
     "The operator's habit of appraising a thing on fundamentals, not hype. A lens for judging any opportunity (offer, asset, venture) on what it actually produces, not on its market buzz.",
     ["\"intrinsic value\""], ["valuation", "intrinsic-value", "fundamentals", "analysis", "value-investing"]),
    (SA, "finance", "Margin of safety as the analytic buffer",
     "Graham and Dodd's central safeguard: buy at a large enough discount to intrinsic value that error, bad luck, or imprecision still leaves you whole. The margin of safety is room for the unexpected, the famous dollar bought for fifty cents.",
     "Build a buffer between price paid and estimated value so that being wrong is survivable; protection comes from the discount, not from forecasting accuracy.",
     "Decision buffers under uncertainty: never commit at full estimated value. A lens for sizing any irreversible commitment so a wrong estimate is not fatal.",
     ["\"margin of safety\""], ["margin-of-safety", "risk-buffer", "discount", "downside", "discipline"]),
    (SA, "finance", "Investment versus speculation",
     "A foundational distinction: an investment operation promises safety of principal and an adequate return on thorough analysis; anything else is speculation. Most market participants speculate while believing they invest.",
     "Define explicitly whether an action rests on analysis and a protected downside (investment) or on price-movement hope (speculation), and know which you are doing.",
     "Name the bet honestly. A lens for distinguishing analyzed, downside-protected moves from hope-driven gambles in any allocation of time or money.",
     ["\"safety of principal\""], ["investment", "speculation", "discipline", "analysis", "risk"]),
    (SA, "capital", "Reading the business: balance sheet, book value, earning power",
     "Security Analysis teaches reading the balance sheet and income statement to gauge book value, asset quality, and sustainable earning power, the engine that produces owner returns over time. The numbers describe the capital base and what it can earn.",
     "Judge an enterprise by its capital base and durable earning power, not a single year's headline; the balance sheet shows what is owned and owed, earning power shows what it can compound.",
     "Owner-level literacy: read what a business owns, owes, and can durably earn. A lens for evaluating the real economics of any venture BJ might build or back.",
     ["\"earning power\""], ["balance-sheet", "book-value", "earning-power", "owner-economics", "capital"]),
    (SNOW, "capital", "The snowball: compounding over a long runway",
     "Schroeder's title metaphor: Buffett's wealth is a snowball rolled down a very long hill, small advantages compounding for decades. What matters is wet snow (good returns) and a long hill (time), with patience as the multiplier.",
     "Compounding rewards length of runway more than bursts of intensity; protect the runway, reinvest steadily, and let time do the heavy lifting.",
     "Compounding applies to skill, reputation, and a corpus of work, not only money. A lens for why BJ's backend-loading and patient reps compound, given a long enough hill.",
     ["\"snow on snow\""], ["compounding", "patience", "long-term", "snowball", "time-horizon"]),
    (SNOW, "operator-doctrine", "Circle of competence",
     "Buffett operated strictly within a self-drawn circle of competence, declining what he could not understand regardless of how attractive it looked. The size of the circle matters less than knowing exactly where its edge is.",
     "Define the boundary of what you genuinely understand and stay inside it; refusing out-of-circle bets is a discipline, not a limitation.",
     "Operator focus: know the edge of your competence and decline past it. A lens for BJ choosing where his field/AI/taste edge is real versus borrowed.",
     ["\"Circle of Competence\""], ["circle-of-competence", "focus", "self-knowledge", "discipline", "edge"]),
    (SNOW, "operator-doctrine", "The inner scorecard, temperament, and reputation",
     "Buffett's recurring frame: live by an Inner Scorecard (your own standard) rather than an Outer Scorecard (others' applause), and guard reputation as the compounding asset that takes decades to build and moments to lose. Temperament beats IQ.",
     "Anchor judgment to an internal standard and treat reputation and temperament as long-compounding assets; emotional control under pressure outperforms raw cleverness.",
     "Self-defined standards over external validation. A lens for BJ building on his own scorecard while loading the backend, not chasing applause or premature signaling.",
     ["\"Inner Scorecard\""], ["temperament", "reputation", "inner-scorecard", "judgment", "character"]),
    (II, "finance", "Mr. Market: price is a servant, not a guide",
     "Graham's allegory: imagine a manic-depressive partner, Mr. Market, who daily offers to buy or sell at wildly varying prices. His mood is your opportunity, not your instruction; you transact only when his price suits you and ignore him otherwise.",
     "Treat volatile market prices as offers to accept or decline on your own terms, never as a verdict on value; let others' emotion create your opportunities.",
     "Emotional independence from the crowd's pricing. A lens for not letting external valuation swings (of a market, a trend, a competitor) dictate BJ's own assessment.",
     ["\"Mr. Market\""], ["mr-market", "price-vs-value", "emotion", "contrarian", "temperament"]),
    (II, "strategy", "Defensive versus enterprising investor",
     "Graham splits investors into the defensive (passive, seeking safety and freedom from effort) and the enterprising (willing to devote real work for higher return). The error is choosing the enterprising path without doing the enterprising work.",
     "Match your strategy honestly to the effort and temperament you will actually supply; half-committed active effort underperforms an honest passive posture.",
     "Right-size ambition to real capacity. A lens for BJ choosing lanes that match the hours and effort he can truly commit, given the lean-operator constraint.",
     ["\"enterprising investor\""], ["strategy", "effort-matching", "defensive", "enterprising", "honesty"]),
    (II, "finance", "Margin of safety as the individual investor's motto",
     "In the closing chapter Graham elevates margin of safety to the central concept for the lay investor: never overpay no matter how exciting the prospect, because the discount, not the forecast, is what protects you. (This staged copy is partial/abridged; core principle captured.)",
     "For non-experts especially, the entire defense reduces to never overpaying and keeping a built-in cushion; excitement is the enemy of the cushion.",
     "Restraint as protection for the non-specialist. A lens for BJ resisting overpaying (in money, time, or commitment) for exciting-looking options.",
     ["\"never overpaying\""], ["margin-of-safety", "restraint", "central-concept", "downside", "discipline"]),
    (MARKS, "systems-thinking", "The nature and regularity of cycles",
     "Marks frames markets, economies, credit, and psychology as cycles that recur (not on a clock, but reliably) because human behavior and leverage push things to excess and then back. Things that seem to move in straight lines are usually arcs.",
     "Expect mean-reversion and excess: when conditions and sentiment look extreme in one direction, the cycle is more likely to turn than to continue forever.",
     "Cyclical, not linear, thinking. A lens for BJ reading any market, platform, or trend (including AI hype) as a cycle prone to overshoot and reversal.",
     ["\"the nature of cycles\""], ["cycles", "mean-reversion", "excess", "systems", "macro"]),
    (MARKS, "systems-thinking", "The pendulum of psychology and the risk-attitude cycle",
     "Investor psychology swings like a pendulum between greed and fear, complacency and panic, and the cycle in attitudes toward risk is the most dangerous: risk feels lowest exactly when prices and complacency are highest.",
     "Read collective emotion as a contrarian signal: rising complacency and risk-appetite mark danger, while widespread fear marks opportunity.",
     "Sentiment is a gauge, read inversely. A lens for BJ sensing when a field is euphoric (be cautious) versus fearful (be opportunistic).",
     ["\"the pendulum of investor psychology\""], ["pendulum", "psychology", "risk-attitude", "greed-fear", "contrarian"]),
    (MARKS, "strategy", "You cannot predict, but you can prepare and position",
     "Marks's practical core: forecasting the future is futile, but calibrating where we stand in the cycle (via observable evidence and sentiment) lets you tilt the odds, becoming more aggressive when the cycle favors you and more defensive when it does not.",
     "Stop predicting and start positioning: assess where you stand in the cycle and adjust aggression versus caution to put the odds on your side.",
     "Position by present evidence, not prophecy. A lens for BJ calibrating how aggressive to be based on current conditions rather than forecasts.",
     ["\"getting the odds on your side\""], ["positioning", "calibration", "odds", "preparation", "cycle-awareness"]),
    (KLAR, "capital", "Risk-aversion first: avoid loss before chasing return",
     "Klarman's organizing principle: value investors are first risk-averse, focused on not losing money, because avoiding permanent loss preserves the capital base that compounding needs. Return is what remains after risk has been controlled.",
     "Make loss-avoidance the first objective; protecting downside preserves the capital and confidence that future returns depend on.",
     "Downside-first thinking. A lens for BJ structuring bets so a bad outcome is survivable, protecting the runway he is building.",
     ["\"risk-averse\""], ["risk-aversion", "loss-avoidance", "capital-preservation", "downside", "discipline"]),
    (KLAR, "ethics", "Wall Street's incentives are not the investor's",
     "Klarman dissects how Wall Street's short-term, fee-driven, upward-biased incentives and institutional performance pressure conflict with the end investor's interest, pushing players toward fads and relative-performance derbies rather than sound long-term decisions.",
     "Map the incentives of everyone advising or transacting with you; misaligned, short-term, fee-driven incentives reliably distort the advice you receive.",
     "Follow the incentives. A lens for BJ reading whose interests a platform, vendor, or advisor actually serves before trusting their guidance.",
     ["\"short-term relative-performance derby\""], ["incentives", "conflicts-of-interest", "short-termism", "institutions", "ethics"]),
    (KLAR, "capital", "Value investing as discipline and long horizon",
     "Klarman frames value investing not as a formula but as a temperament: bottom-up analysis, strict discipline, a long horizon, and the patience to hold cash and do nothing until a genuine bargain appears. He calls it a book about thinking about investing.",
     "Treat sound capital allocation as a disciplined practice, not a formula: analyze bottom-up, wait for real mispricing, and tolerate inactivity.",
     "Patience and the willingness to do nothing. A lens for BJ resisting forced action and waiting for genuinely high-leverage moves while the backend loads.",
     ["\"thinking about investing\""], ["discipline", "patience", "bottom-up", "long-horizon", "capital-allocation"]),
    (SOV, "systems-thinking", "Technology changes the logic of power",
     "Davidson and Rees-Mogg argue that each shift in the dominant technology of production and violence reshapes who holds power; the microprocessor and information age, they claim, undercut the industrial nation-state much as gunpowder undid feudal lords.",
     "When the underlying technology of value and force changes, institutional power structures eventually reorganize around it; watch the substrate, not just the headlines.",
     "Structural, substrate-level reading of change. A lens for BJ seeing how AI and information tools may reshape who holds leverage in his domains.",
     ["\"the logic of violence\""], ["technology", "power", "information-age", "institutions", "macro"]),
    (SOV, "strategy", "Falling returns to violence and optional jurisdiction",
     "The book's thesis that information technology lowers the payoff to large-scale coercion and lets value and people move across borders, making jurisdiction increasingly something one chooses rather than merely inherits. (A provocative 1997 macro thesis, held as a lens, not a prophecy.)",
     "As mobility and digital value rise, location and jurisdiction become strategic choices rather than fixed constraints; optionality of place is a lever.",
     "Geographic and jurisdictional optionality as strategy. A lens for BJ weighing where and how to operate, not a prediction to act on literally.",
     ["\"transcend locality\""], ["jurisdiction", "mobility", "optionality", "macro-thesis", "strategy"]),
    (SOV, "capital", "The sovereign individual as an autonomy lens",
     "The titular figure is a highly skilled, mobile individual who, freed by technology from dependence on a single employer or state, captures more of the value they create. Read here strictly as a lens on self-reliant value capture, not as an ideology to adopt.",
     "Rising individual leverage means a skilled operator can own more of the value they produce; build skills and assets that are portable and self-owned.",
     "Owning the value you create rather than renting it out. A lens connecting to MONEY_OWNERSHIP's avoid-permanent-service-provider thread for BJ.",
     ["\"Sovereign Individual\""], ["autonomy", "value-capture", "self-reliance", "ownership-lens", "capital"]),
    (LORDS, "systems-thinking", "The Fed's superpower: money from thin air",
     "Leonard explains the Federal Reserve as the one institution that can create dollars at will, depositing new money into a small set of large banks. After 2008 it printed roughly a century's worth of base money in about a year via quantitative easing.",
     "Understand that the money supply is actively managed and can be expanded enormously by policy; the value and quantity of money are decisions, not constants.",
     "Money itself is a managed system, not a fixed backdrop. A lens for BJ reading how monetary conditions (cheap vs tight money) shape the environment any venture operates in.",
     ["\"money appear out of thin air\""], ["federal-reserve", "money-supply", "quantitative-easing", "monetary-system", "macro"]),
    (LORDS, "ethics", "Easy money inflates assets and concentrates gains",
     "Leonard's through-line: years of near-zero rates and QE inflated asset prices, disproportionately benefiting those who already owned assets while wage earners lagged, widening wealth concentration, an unintended distributional consequence of the policy.",
     "Cheap money does not benefit everyone equally; it tends to reward asset owners over earners, so macro policy has distributional ethics, not just efficiency effects.",
     "Who benefits from the system matters. A lens for BJ understanding why owning assets (vs only earning income) matters in an easy-money era, held ethically and critically.",
     ["\"asset price\""], ["asset-inflation", "wealth-concentration", "distribution", "monetary-policy", "ethics"]),
    (LORDS, "operator-doctrine", "Hoenig's dissent: principled independence under pressure",
     "The book centers on Thomas Hoenig, the lone FOMC member who voted no repeatedly against quantitative easing, accepting career and reputational cost to act on his convictions about long-term consequences against overwhelming institutional momentum.",
     "Principled dissent sometimes means being the lone no against powerful consensus, accepting near-term cost for a long-term conviction you can defend.",
     "The courage to hold a defensible minority view. A lens for BJ trusting his own analysis when it diverges from loud consensus, if the reasoning is sound.",
     ["\"he was going to vote no\""], ["dissent", "independence", "conviction", "institutions", "courage"]),
    (TYC, "commercial-architecture", "The leveraged buyout model",
     "Kelly explains private equity's core machine: buy a company largely with borrowed money, improve or restructure it, and sell it later at a profit, with debt amplifying returns on a relatively thin slice of equity. Leverage is the engine and the risk.",
     "Leverage magnifies both returns and fragility; the LBO model shows how ownership structure and debt, not just operations, drive financial outcomes.",
     "Capital structure as a lever, understood with its risk. A lens for BJ grasping how financing structure (not just the offer) shapes a business's economics and fragility.",
     ["\"leveraged buyout\""], ["private-equity", "leverage", "lbo", "capital-structure", "commercial-architecture"]),
    (TYC, "commercial-architecture", "Fees, carry, and the LP/GP alignment",
     "Kelly demystifies PE economics: general partners (GPs) raise funds from limited partners (LPs), charge a management fee plus carried interest (carry, a share of profits), and align (or misalign) incentives accordingly. The fee structure shapes behavior.",
     "Understand who earns what and when in any pooled-capital arrangement; the fee-and-carry structure dictates the incentives and therefore the behavior of the managers.",
     "Read the economics of any arrangement that manages others' resources. A lens for BJ structuring or evaluating any deal where incentives are set by how parties get paid.",
     ["\"carried interest\""], ["fees", "carry", "lp-gp", "incentives", "fund-economics"]),
    (TYC, "capital", "Private equity owns more than you think",
     "The book's framing claim: PE-backed firms touch an enormous share of the economy, so a few large funds effectively own (or influence) companies most people interact with daily, ownership concentrated and largely out of public view.",
     "Ownership of productive assets, not headline brands, is where durable economic power sits; much of it is concentrated and invisible to the public.",
     "Ownership is the quiet locus of power. A lens reinforcing (with MONEY_OWNERSHIP) why BJ should think in terms of owning assets, not only selling services.",
     ["\"that owns everything\""], ["ownership", "private-equity", "concentration", "economic-power", "capital"]),
    (SA, "capital", "Synthesis: the deep-finance ownership stack",
     "Across these eight books a single stack emerges: appraise value on fundamentals (Graham/Dodd), demand a margin of safety and avoid loss first (Klarman), stay emotionally independent of price (Graham's Mr. Market), let compounding run on a long runway with the right temperament (Buffett/Schroeder), read cycles rather than predict them (Marks), understand money and macro forces as managed systems (Leonard, Davidson), and recognize that durable power sits in concentrated ownership (Kelly). Ownership beyond service income is the throughline. This is the closing synthesis chunk.",
     "Durable capital outcomes come from fundamental valuation + downside-first discipline + emotional independence + long-runway compounding + cycle awareness + macro literacy + a bias toward owning rather than only earning.",
     "The integrated capital lens that extends MONEY_OWNERSHIP: how an operator could think about ownership, risk, and compounding beyond trading time for income. Decision-support scaffolding, not a plan to become an investor." + GUARD,
     ["\"margin of safety\""], ["synthesis", "ownership", "capital-stack", "compounding", "decision-support"]),
    (KLAR, "operator-doctrine", "Synthesis: the optionality guardrail",
     "The deep-finance models are mental models for understanding capital, risk, cycles, and ownership, NOT a directive that BJ become an investor, trader, or finance brand. They sharpen how he evaluates any option (including non-finance ones) and reinforce the avoid-permanent-service-provider thread from MONEY_OWNERSHIP, while photography and every other path remain open. This is the closing optionality chunk.",
     "Absorb finance as a thinking toolkit (valuation, risk, compounding, incentives, cycles) applicable to any decision, while keeping identity and direction fully open.",
     "Finance literacy as portable judgment, not a new identity. Explicitly preserves optionality: no lane finalizes SNIPED / SNIPED Media / BASEPLATE, and this is not a cue to pivot into investing." + GUARD,
     ["\"thinking about investing\""], ["optionality", "decision-support", "guardrail", "mental-models", "doctrine"]),
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
        sr = relevance if i - 1 in (25, 26) else relevance + GUARD
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
