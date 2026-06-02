#!/usr/bin/env python3
"""
Write MONEY_OWNERSHIP_CHUNKS.jsonl · 21 chunks (19 source + 2 synthesis) across 6 sources.
12-field canonical schema. ONE new domain `capital` (operator-approved). investing/wealth/ownership/
economics NOT used. Other concepts route to existing strategy/commercial-architecture/operator-doctrine/
systems-thinking/finance. Identity-optionality guardrail: capital thinking is a decision-support lens,
NOT a pivot; no final SNIPED / SNIPED Media / BASEPLATE direction. Em-dash sweep at the end.
"""

import json
from pathlib import Path

OUT = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "MONEY_OWNERSHIP_CHUNKS.jsonl"

HOUSEL = ("The Psychology of Money", "psychology_of_money_housel.txt", "Morgan Housel")
BUFFETT = ("The Essays of Warren Buffett", "essays_of_warren_buffett.txt", "Warren E. Buffett & Lawrence A. Cunningham")
MARKS = ("The Most Important Thing", "the_most_important_thing_marks.txt", "Howard Marks")
KOC = ("King of Capital", "king_of_capital_blackstone.txt", "David Carey & John E. Morris")
POWER = ("The Power Law", "the_power_law_mallaby.txt", "Sebastian Mallaby")
MW = ("Money, Wealth & Getting Ahead", "money_wealth_getting_ahead.txt", "SNIPED (synthesis)")

DG = "Decision-support lens only. Capital / ownership thinking is a lens, NOT a pivot decision; this does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction, and photography remains one option among several. Optionality preserved."

C = []
def add(src, domain, concept, summary, principle, relevance, quotes, tags):
    n = len(C) + 1
    title, sfile, author = src
    C.append({
        "chunk_id": f"MONEY_OWNERSHIP_{n:03d}",
        "batch_id": "MONEY_OWNERSHIP",
        "source_title": title, "source_file": sfile, "author": author,
        "domain": domain, "concept": concept, "summary": summary,
        "usable_principle": principle, "sniped_relevance": relevance,
        "direct_quotes": quotes, "tags": tags,
    })

# ---------------- The Psychology of Money (Housel) · 3 ----------------
add(HOUSEL, "capital",
    "Getting wealthy vs staying wealthy: survival and compounding",
    "Housel separates the skill of getting money (optimism, risk-taking) from the skill of keeping it (frugality, paranoia, survival). Compounding only works if you do not interrupt it, so staying in the game for decades matters more than any single high return. The biggest gains come from time, not heroics.",
    "Prioritise survival and never interrupting compounding; longevity in the game beats chasing the highest return.",
    "Frames any future capital the operator builds: protect the downside and let time compound, rather than swinging for fast wins. " + DG,
    [],
    ["compounding", "survival", "staying-wealthy", "capital", "housel"])

add(HOUSEL, "operator-doctrine",
    "Enough: wealth is what you do not see",
    "True wealth is the assets and freedom you do NOT spend, the income converted to options rather than visible consumption. Without a sense of 'enough', rising income just moves the goalpost and invites ruinous risk. The highest dividend money pays is control over your own time.",
    "Define 'enough' early and treat unspent income as freedom; the goal is control of your time, not visible consumption.",
    "A temperament lens for the operator: build optionality and time-control rather than lifestyle, whatever direction is chosen. " + DG,
    ["Wealth is the nice cars not purchased."],
    ["enough", "freedom", "temperament", "operator-doctrine", "housel"])

add(HOUSEL, "capital",
    "Room for error: margin of safety in personal finance",
    "Because the future is uncertain and tails drive outcomes, build room for error (cash reserves, conservative assumptions, low fixed costs) so a bad surprise never forces a bad decision. The margin is not pessimism; it is what lets you survive long enough for the upside to arrive.",
    "Hold a margin of safety in cash and fixed costs so no single setback can knock you out of the game.",
    "Directly supports the operator's stability: financial breathing room removes desperation pricing and survival-mode decisions. " + DG,
    [],
    ["room-for-error", "margin-of-safety", "reserves", "capital", "housel"])

# ---------------- The Essays of Warren Buffett · 4 ----------------
add(BUFFETT, "capital",
    "Intrinsic value and owner earnings",
    "Buffett values a business by its intrinsic value, the discounted cash it will produce over its life, and judges performance by 'owner earnings' (reported earnings plus non-cash charges minus the real capital needed to sustain the business), not headline accounting profit. Think like an owner of the whole enterprise.",
    "Value a business by the cash it actually throws off to an owner over time, not by accounting earnings or price.",
    "An owner's-eye lens for evaluating any business or asset the operator might build or buy. " + DG,
    [],
    ["intrinsic-value", "owner-earnings", "cash-flow", "capital", "buffett"])

add(BUFFETT, "finance",
    "Mr. Market and the margin of safety",
    "Mr. Market offers a price every day driven by emotion; the investor is free to ignore him and act only when price is far below value. That gap is the margin of safety, the discipline of buying with a buffer so that errors and bad luck do not become permanent losses.",
    "Treat market prices as optional quotes from an emotional partner; act only with a margin of safety between price and value.",
    "An emotional-discipline lens for any capital decision: separate price noise from value and demand a buffer. " + DG,
    [],
    ["mr-market", "margin-of-safety", "discipline", "finance", "buffett"])

add(BUFFETT, "capital",
    "Capital allocation is the core job",
    "Over time, how retained earnings are reinvested determines a company's fate, so capital allocation is the most important job of the person at the top. Buffett's test: every dollar retained should create at least a dollar of market value; otherwise return it to owners.",
    "Judge every retained dollar by whether it creates at least a dollar of value; allocation, not operations, compounds wealth.",
    "The central owner skill the operator would need to grow beyond service income: deciding where each dollar goes. " + DG,
    [],
    ["capital-allocation", "retained-earnings", "reinvestment", "capital", "buffett"])

add(BUFFETT, "commercial-architecture",
    "Economic moats and durable advantage",
    "Buffett favours businesses with a durable competitive advantage, an economic moat (brand, switching costs, low-cost production, network effects) that protects returns from competition. Float and pricing power are forms of moat that let capital compound at high rates for long periods.",
    "Prefer assets with a durable moat that protects pricing power and returns, so capital compounds without erosion.",
    "A structural lens: any durable SNIPED asset should be evaluated for what protects it from imitation (craft depth, archive, relationships). " + DG,
    [],
    ["moat", "durable-advantage", "pricing-power", "commercial-architecture", "buffett"])

# ---------------- The Most Important Thing (Marks) · 3 ----------------
add(MARKS, "strategy",
    "Second-level thinking",
    "Marks distinguishes first-level thinking (obvious, consensus) from second-level thinking (deeper, contrarian, accounting for what others believe and how that is priced). Above-average returns require thinking that is both different from and better than the crowd, which depends on others being wrong.",
    "To beat the consensus you must think differently and more correctly than it; mere effort at the obvious is already priced in.",
    "A judgment lens for any contested decision: ask what the crowd believes, why it might be wrong, and whether you are actually better-informed. " + DG,
    ["second-level thinkers depend on inefficiency"],
    ["second-level-thinking", "contrarian", "edge", "strategy", "marks"])

add(MARKS, "systems-thinking",
    "Risk is more things can happen than will happen",
    "Marks defines risk not as volatility but as the probability of permanent loss, rooted in the fact that the future is a distribution of possibilities, not a single line. Because many outcomes were possible, a good result can come from a bad decision and vice versa; judge process, not just outcome.",
    "Treat risk as the range of things that could happen, not past volatility; judge decisions by process under uncertainty.",
    "A risk lens for the operator's bets: size them for the bad branches that did not happen, not just the one that did. " + DG,
    ["Risk means more things can happen than will happen."],
    ["risk", "uncertainty", "process-vs-outcome", "systems-thinking", "marks"])

add(MARKS, "systems-thinking",
    "Market cycles and contrarian positioning",
    "Markets move in cycles driven by a pendulum of greed and fear that always overshoots; knowing roughly where you stand in the cycle is the most important input. The disciplined move is contrarian and counter-cyclical: more aggressive when others are fearful, defensive when others are euphoric.",
    "Read where the cycle stands and lean against the crowd's emotion; be defensive in euphoria and aggressive in fear.",
    "A timing-and-temperament lens applicable to markets, attention, and category cycles the operator may face. " + DG,
    [],
    ["market-cycles", "contrarian", "mean-reversion", "systems-thinking", "marks"])

# ---------------- King of Capital (Blackstone) · 3 ----------------
add(KOC, "capital",
    "The leveraged buyout: amplifying equity returns with debt",
    "The private-equity buyout buys a company largely with borrowed money, improves it, and sells it; because debt is repaid from the company's cash flow, a modest gain in enterprise value produces an outsized return on the small equity slice. Leverage magnifies both returns and risk.",
    "Understand that debt-financed ownership amplifies equity returns when cash flow services the debt, and amplifies losses when it does not.",
    "An ownership-mechanics lens: shows how owners (not service providers) capture amplified upside, with the matching risk made explicit. " + DG,
    [],
    ["leveraged-buyout", "leverage", "enterprise-value", "capital", "blackstone"])

add(KOC, "finance",
    "Private-equity economics: GP/LP, carry, and fund structure",
    "Blackstone's rise shows the PE fee model: a general partner raises a fund from limited partners, charges a management fee (around 2 percent), and keeps carried interest (around 20 percent of the profits). The GP compounds wealth on other people's capital by allocating it well and aligning through carry.",
    "Capital-light ownership of returns is possible by managing other people's money for a fee plus a share of the upside.",
    "A structural lens on how operators turn judgment into ownership economics without supplying all the capital themselves. " + DG,
    [],
    ["private-equity", "carried-interest", "gp-lp", "fund-economics", "finance", "blackstone"])

add(KOC, "commercial-architecture",
    "Operational value creation and resilience through cycles",
    "Blackstone created value by actively owning portfolio companies (operational improvement, not just financial engineering) and survived near-death moments by diversifying beyond buyouts into a broad alternative-asset manager. Owning and improving assets, then surviving the cycle, built enduring enterprise value.",
    "Build value by actively improving what you own and by diversifying enough to survive the cycle that kills single-bet firms.",
    "A build-and-survive lens for the operator's own enterprise: improve the asset, do not over-concentrate, outlast downturns. " + DG,
    [],
    ["value-creation", "diversification", "resilience", "commercial-architecture", "blackstone"])

# ---------------- The Power Law (Mallaby) · 3 ----------------
add(POWER, "capital",
    "The power law: a few winners drive everything",
    "Venture returns are not normally distributed; a tiny number of grand-slam investments return more than the entire rest of the fund combined. Because outcomes follow a power law, the cost of missing one huge winner dwarfs the cost of many failures, which inverts ordinary risk intuition.",
    "When outcomes follow a power law, optimise for access to the rare huge winner, not for avoiding small losses.",
    "A returns-shape lens: in power-law domains (which may include attention and culture), one outlier outcome can dominate everything else. " + DG,
    ["the power law was inexorable"],
    ["power-law", "outliers", "returns-distribution", "capital", "mallaby"])

add(POWER, "strategy",
    "Bet on outliers and the founders who make them",
    "Venture capitalists win by backing the rare founder and idea capable of a power-law outcome, tolerating a high failure rate as the price of access to the few that matter. The mindset is upside-seeking: ask how big this could be if it works, not how likely it is to fail.",
    "Select for maximum upside and exceptional founders, accepting many misses as the cost of catching the few outliers.",
    "An upside-orientation lens for the operator's project selection: weight the size of the win, not just the odds. " + DG,
    [],
    ["outliers", "founders", "upside", "strategy", "mallaby"])

add(POWER, "capital",
    "The venture ownership model: minority stakes, staged capital",
    "VCs take minority equity stakes, finance in stages tied to milestones, and construct a portfolio so that the power-law winners more than cover the losers. Ownership of equity in the future (not fees for present labor) is the engine of venture wealth.",
    "Own staged equity in many shots-on-goal rather than selling labor once; portfolio ownership captures the power-law upside.",
    "The clearest contrast to service-provider economics: equity ownership of future value vs one-time payment for work done. " + DG,
    [],
    ["equity", "staged-financing", "portfolio", "capital", "mallaby"])

# ---------------- Money, Wealth & Getting Ahead (SNIPED synthesis) · 3 ----------------
add(MW, "strategy",
    "Constraint elimination and correct-contrarian bets",
    "The operator's own synthesis: getting ahead is a systems problem, not a motivation problem. Eliminate the single binding constraint instead of optimising around many; and win through a small number of correct contrarian bets (where you were right and the crowd was wrong) rather than many safe ones.",
    "Find and kill the one binding constraint, and concentrate on the few contrarian bets that produce most of the outcome.",
    "Operator-authored · directly applies the finance-canon lessons (Marks contrarianism, power-law concentration) to the operator's own situation. " + DG,
    ["Constraint elimination beats optimization."],
    ["constraint-elimination", "contrarian-bets", "leverage", "strategy", "sniped-synthesis"])

add(MW, "operator-doctrine",
    "The Protected Hour, 60% beats zero, and compounding systems",
    "One uninterrupted hour per day on a 12-month compounding asset (skill, business, content, research) changes the trajectory more than any hack; on low-energy days do 60 percent of the plan but never zero, because two missed days in a row kills momentum. Build systems that compound while you sleep.",
    "Protect one daily hour for a compounding asset and never drop to zero; momentum and compounding beat intensity.",
    "Operator-authored execution discipline that pairs with EDGE_AND_OPERATING_DISCIPLINE; the capital it compounds is the point. " + DG,
    ["60% beats zero."],
    ["protected-hour", "compounding", "momentum", "operator-doctrine", "sniped-synthesis"])

add(MW, "capital",
    "Wealth is passive income above burn rate, not a better-branded job",
    "The synthesis's definition of financial freedom: money arriving without your labor, exceeding your burn rate. Until then, even a great creative practice is 'a job with better branding'. Passion follows competence, and surface area of luck (publishing, putting work out) beats internal perfection.",
    "Aim for income that exceeds burn rate without your labor; treat ownership and assets, not just billable work, as the goal.",
    "The crux of the operator's 'avoid staying only a talented service provider' question · held as a decision-support lens, not a directive to abandon the craft. " + DG,
    ["Wealth = passive income > burn rate."],
    ["passive-income", "ownership", "service-provider-trap", "capital", "sniped-synthesis"])

# ---------------- Synthesis · 2 ----------------
add(MW, "capital",
    "SYNTHESIS: the capital-thinking stack (own, do not only serve)",
    "Read together: think like an owner and value cash flow (Buffett); demand a margin of safety and judge risk as the range of outcomes (Marks, Housel); concentrate on the few power-law winners (Mallaby); use leverage and active ownership to amplify and protect value (Blackstone); and convert labor income into compounding assets above burn rate (the operator's synthesis). The throughline is moving from selling labor once to owning compounding value.",
    "Convert the service practice's cash flow into owned, compounding assets evaluated like an owner, so wealth is not bound to billable hours.",
    "A consolidated capital-thinking stack for the operator's economic future. It generates and evaluates ownership options; it does NOT decide the direction. " + DG,
    [],
    ["synthesis", "ownership", "capital-stack", "capital", "money-ownership"])

add(MARKS, "systems-thinking",
    "SYNTHESIS: capital thinking is a lens, optionality preserved",
    "These ownership and capital frameworks are powerful but commitment-shaped; taken literally they could push the operator to pivot toward investing or to subordinate the craft to returns. Within the active identity-and-brand-optionality guardrails they are treated strictly as decision-support lenses that widen and pressure-test the economic option set, keeping direction reversible until the operator writes the fresh current brief.",
    "Use capital frameworks to expand and stress-test economic options, not to prematurely pivot identity, niche, or business model.",
    "Explicitly preserves optionality: capital thinking is a lens. No final SNIPED, SNIPED Media, or BASEPLATE direction; photography stays one option among several. " + DG,
    [],
    ["optionality", "decision-support", "guardrail", "systems-thinking", "money-ownership"])

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
print("NEW domain 'capital' count:", dist.get("capital", 0))
for bad in ("investing", "wealth", "ownership", "economics"):
    assert bad not in dist, f"FORBIDDEN domain used: {bad}"
print("forbidden domains (investing/wealth/ownership/economics) used: NONE")
print("em-dashes in output:", sum(json.dumps(c, ensure_ascii=False).count(EM) for c in C))
