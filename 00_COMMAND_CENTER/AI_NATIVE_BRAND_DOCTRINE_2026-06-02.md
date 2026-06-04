# AI-NATIVE BRAND DOCTRINE
**Distilled from 16 complete-read segments of a ~400,000-word corpus. One reference doc, built to load at decision time.**

Coverage note up front: segments 1-12 carry the AI / ecommerce / brand / content / image-gen signal. Segments 13-16 are a single cinematography channel (Wandering DP) that the corpus swept in by accident. Its craft signal is real and is folded into the relevant sections, but it is not AI-native business material. Full per-segment confirmation is in the Coverage Manifest at the end.

A note on what this corpus actually is: a stack of YouTube tutorials, founder podcasts, and Reddit threads. The numbers ($54k/30 days, $67k/8 days, $8k MRR) are creator marketing claims, not audited. Treat them as direction and proof-of-possibility, not as guarantees. The *methods* are the signal. The *amounts* are bait.

---

## 1. AI AGENTS + AUTOMATION SYSTEMS

**The core shift: SaaS to "service as a software."** Old definition: software as a service. New definition (Opus Clip's Young, echoed across segments): you take a service that humans/agencies/freelancers currently perform and deliver it as software. The opportunity sits wherever there is an "imperfect hacky solution" or a human doing tedious work. TAM is no longer seats x $20/mo; it is the combined salary of everyone currently paid to do the job (Jake Heller / CaseText: "a thousand-x bigger").

**What to build (ranked by proven traction in the corpus):**

- **Free-website-to-local-business + marketing upsell** (the $8k MRR winner, Brandon Doyle / OpenClaw). Agent scrapes Google Business Profiles, builds hundreds of sites for cents each (Chinese models keep token cost low), then offline outreach via postcards + QR (Lob). 350 sent, ~20% scanned, ~20% of scanners closed, ~$400/mo average client, biggest at $1,200/mo. The differentiator was *offline* (postcard), not another inbox email. Repeated by Reddit poster: ~2 deals/week at $350 + $50/mo, tools lovable.dev / webild.io / leadburnr.com / stripe / hunter.io.
- **AI voice agents for SMBs** (ElevenLabs, Synthflow). Dentists, doctors, mechanics miss appointments because no one answers the phone. Setup $1k-$5k, monthly $200-$1k+. ElevenLabs platform abstracts speech+LLM+TTS latency and your knowledge base; Twilio for telephony. Synthflow starter $29/mo. "Worth thousands to tens of thousands per month if you land a few."
- **Custom personalized newsletter as a product** (Dreamtales, ~$300+ MRR). Anti-app: "people don't want another app." Delivered into email/SMS where people already live. $9/mo single, $19-24 multi.
- **AI ad agency** (Cedley/Chris Branch, Coca-Cola). Spec ads to build portfolio, then $1k for a short piece up to $50k-$100k for a full social/TV campaign that one person now fulfills.
- **AI content studio on retainer** ($1k-$3k/mo), **website flipping** ($300-$2k), **AI tools audit** ("selling clarity, not tech," easiest entry), **AI workshops/training** ($500-$5k/session).

**Agent platforms named:** OpenClaw (the heavyweight; connect to any model incl. DeepSeek/Qwen/Kimi for cost, give it a card, put it in iMessage/Slack/WhatsApp), Manus (autonomous research/agent, Chinese, caution with data), HyperAgent (Airtable, per-agent prompt/tools/skills/budget). Multi-agent "director" model: Agent Opus runs 8-9 sub-agents (script writer, voiceover, avatar, asset sourcing) under one director agent.

**Interface placement is the tactic, not the tech.** Put the agent where the user already lives (iMessage, Slack, email, WhatsApp). Voice-prompt it. "Frictionless." Anti-app doctrine throughout: solve the problem in the channel, do not ship app #51.

**The four interaction modes** (Alli Miller): microtasker → real-time companion (voice/video) → delegate (20-min task returns a full deliverable) → teammate (whole team gets a helper; auto Friday status reports from Drive+Gmail). Most people are stuck at microtasker.

**Hire one "AI automation person"** (Dan Martell, formerly "RevOps"). Audits every workflow, unbottlenecks, automates, teaches the team to prompt. "A must to be competitive."

**Zapier/Make stack for solo ops** (Cassidy Warren's 7-step): blog → RSS → ChatGPT rewrite → post to 4 platforms; lead in Google Sheet → wait 5 min (don't look robotic) → personalized Gmail send → mark sent; Stripe payment → create Drive folder + questionnaire + welcome email + Trello card + Slack ping in <60s.

---

## 2. AI SKILLS + PROMPTING METHODS

**The thesis that justifies this whole section** (the "7 Claude Skills" video, appears 3x in corpus): *"In a world where everyone has access to the exact same AI models, skills determine who gets the most out of those models."* Knowing how/when to use and how to *build* skills is itself the moat.

**The reusable-skill pattern.** A skill = a folder of markdown files defining an intake/flow the model follows. Invoke with `/skillname`. Install: Settings → Capabilities → Customize skills → Upload a skill (zip) → toggle on → new chat auto-loads it. Internal structure example (Infographic Builder): intake → confirm → pick type from `types.md` → pick aesthetic from `aesthetics.md` → lock dimensions → set interactivity → build → review.

**The 7 named skills worth stealing:**
1. **Infographic Builder**, builds an editable interactive HTML page (not a static image), screenshot for social.
2. **Excalidraw Diagram Generator**, hand-drawn flowcharts, fully editable after export.
3. **Expand and Contract**, explode an idea into ~25 features, then contract to core / nice-to-have / explicitly-out / maybe-later-with-a-trigger ("add manual food search after 1,000 paid subs"). Renders as concentric circles.
4. **Steelman**, argues both sides per angle (case for / case against / who's winning), verdict at bottom. Pressure-tests assumptions.
5. **Promptizer**, writes a better prompt for any task; asks clarifying questions if vague.
6. **Swarm Consensus**, queries many models (Grok/Gemini/ChatGPT/Claude) via OpenRouter (one API key, set a credit cap ~$8) and synthesizes; ~$15 for 30 frontier sessions, 8 cheap models = 40 responses for 3 cents. Use for high-stakes/legal where you want many brains to agree.
7. **Find Skills**, points the agent at skills.sh (90,000+ community skills) so you don't build from scratch.

**The single most valuable prompting habit (add to Claude/system instructions):**
> "While working, note opportunities for automation, improvement, repeatability, and if a task is a good candidate for a skill, tell me so I can turn it into a skill and reuse the workflow later."
Plus: *"Before diving into complex work, ask 3-4 clarifying questions to understand context, goal, and constraints."* (Clarify-before-acting raises first-try quality dramatically.)

**Prompting methods that recur across every segment:**
- **Reverse prompting / prompt-to-build-a-prompt.** Don't hand-write the long prompt. Tell the model: "Create a prompt I can use to build [X]." It interviews you, returns a robust prompt, you run *that*. Used for Claude Design tools, Midjourney prompts, image/video gen.
- **Use ChatGPT to write prompts for *other* models** (image/video). "Hidden hack."
- **Web search ON = research engine, not just a writer.** "Search Reddit/articles/social for what [audience] struggles with most; give pain points *in their own words*, not clinical terms" (the $54k PDF method).
- **Be hyper-specific and explicitly say "avoid generic."** (Eric Johnson's entire brand-build pipeline.)
- **Ask it to interview you.** "Go full Mel Robbins / Barbara Walters, ask me 20 questions," then dictate and ramble. "Whisper to it for 20 minutes, get 4 hours of work done." Treats AI as a "prosthesis for reinvention," not a faster Google.
- **20+ rounds of back-and-forth with full context** for hard decisions (Young). Throw in everything; do not ask one-liners.
- **Rank-and-score.** For complex problems, ask for "tons of options," then "rank and score them." Then "give me 3 ways this might go wrong."
- **The cheat code** (Dan Martell): when you get an output you love, ask *"Write me the system prompt that would have generated this output."*
- **Memory/decision journaling** (Young, citing Mustafa Suleyman): tell the AI daily what you decided and how you felt; monthly ask "What's the biggest mistake I made in the last 6 months?" / "What would you have told me 3 months ago?"
- **Treat the agent as a powerful but distractible intern** (Amjad/Replit). Overcommunicate. Precision = "programming without the syntax." When it errors, copy the log and hand it back: "When I deploy I get this error but NOT in preview."

**Models routinely named:** Claude (Code, Design, Opus/Sonnet/Haiku), ChatGPT (o3, GPT-5 thinking), Gemini 3 Pro, Grok, Perplexity (research). Tool-routing intuition matters more than tool worship.

---

## 3. ECOMMERCE + PRODUCT LAUNCH (validation → first sale → pricing)

**Validate by engineering the result, not building the product.** Opus Clip's whole origin: manually used AI to make the final videos, emailed them to prospects, got >60% positive replies, *then* built a Discord bot (no UI). PMF signal = people complaining about the queue/quota. ElevenLabs: built a lightweight dubbing prototype first, customers said "actually fix just my voice," pivoted to the real (smaller, earlier) problem. The test for a real business: can you state the value in ~10 words? Are people asking for pricing / handing over a card, or just saying "amazing"?

**The painful-job-to-be-done test.** If it's a real painful job, alternatives already exist (humans, internal tools, manual hacks) where people spend painful hours. Find the problem *rationally* (deep industry/workflow knowledge), not emotionally. Avoid: (1) building a feature an incumbent can bundle (don't build the meeting note-taker, Zoom adds it); (2) being a thin wrapper ("AGI-pilled", if a model does the job 80% today, the next release does it 99% and erases your prompts). Own the workflow *end to end*; AI is part of the workflow, not all of it.

**Reliability is the bridge from demo to business** (Jake Heller, the highest-signal source). Most ship 60-70% accuracy, enough to raise and sign pilots, but "doesn't work in practice." Method:
1. Learn exactly how the best human does the task (be the expert or hire one, 30-40% of CaseText were lawyers).
2. Ask "how would they do it with unlimited time / 1,000 AIs?" Work backward into discrete steps.
3. Turn each step into code; most become prompts. Avoid a prompt wherever deterministic logic works (prompts are slow/expensive).
4. Workflow (fixed steps) vs agentic (depends on circumstances). Prefer deterministic workflows.
5. **Evals are the part everyone skips.** Make outputs objectively gradable (true/false, 0-7). Use promptfoo. Write ~12 test cases → perfect them → scale to 100. Keep a hold-out set. Grind a single prompt from ~60% to ~97% over two sleepless weeks. Customer complaints become new tests. "There should be a new pull request on your prompts every day."

**Pilot Recurring Revenue ("PRR") is the coming mass-extinction.** Reported "$10M ARR" is often 6-month pilots that never convert. The sale doesn't end at the check, ensure use, training, onboarding. "Your product isn't just the pixels on the screen" (support, success, forward-deployed engineers sitting beside the customer).

**Pricing (a real science):**
- Anchor to **value creation**: what would the user do without you (their time, a vendor, a pro)? Editing a viral clip = 30-60 min, market price $25-$50, that's your benchmark.
- Watch **unit economics**: inference + *storage* (the video "elephant," 5% of COGS early → 50% over 3-5 years).
- **Experiment heavily** (thousands of surveys, 20-30 customer interviews per critical decision, representative mix). Price on **usage not seats** for solopreneurs.
- **You don't need a price everyone likes.** Say no to ~70% of early users; serve only the ICP.
- Customers often *want* predictable pricing (CaseText: customers asked for flat $6,000/seat over per-usage). Listen to how they want to pay.
- For previously-impossible tasks, price from value delivered (save them $100M → take 10-20%). Then expect commoditization (good for society, "bad for your business").
- POD/physical margins: target 20-30% min, never more than 7 color variants, clothing + wall art have best perceived-value headroom.

**First-sale escape maps:**
- **$10k/mo = 4 clients × $2,500** (Liam Ottley). Niche AI automation agency. The 4 starter systems any local business needs: speed-to-lead, SMS/WhatsApp booking, social DM bot, AI receptionist. Sell to the "AI-clueless" (HVAC, roofers, plumbers, "easiest to sell to people who know less than you"). Cold email via Apollo lists; test 4 offers x N niches, double down on the winning combo.
- **Etsy as testbed, Shopify as endgame.** Etsy = built-in traffic + public sales data, ~$0.20/listing, Printify integration = $0 upfront (pay after sale). Volume game: post 50-100 (Greg) to 1,000 (Mark) listings, let the algorithm pick winners, "saturation doesn't matter." $10k/mo math: 100 listings × 15 sales/mo × $7 profit. Then duplicate winners to your own Shopify (where you can *legally collect emails*, worth ~$1/customer/mo).
- **The "export button" thesis** (Greg Eisenberg): every export button is a $1M-$100M AI business, people export to do analysis a human currently does.

---

## 4. CONTENT + SOCIAL GROWTH (hooks, formats, what travels)

**Distribution is the moat now that building is trivial.** Repeated by Higgsfield's Alex, Nicole (4 apps), Greg, and the Reddit threads. "It's not about the features. It's about distribution."

**Permanent-inventory math** (the $54k PDF + reels method). Every reel is a permanent asset. 1 reel = ~10k views, ~0.5% click = 50 visits, ~2 buy a $27 product = $54 from a video you never touch again. Stack 4/week → 100 in 6 months, all running 24/7. ~1 in 20-50 hits 100k-1M views. "Laying brick after brick."

**Model, don't copy.** Search any buyer keyword, find videos with millions of views, steal the *structure* (hook pattern, pacing, format), make your own version. "If a format is getting millions of views, the algorithm already did your testing."

**Formats are the secret to audience** (Greg's ACP: Audience → Community → Product, reverse of old order). Pick ONE format per business day and systematize it. Look for formats *outside* your niche and bring them in. The "creative faucet routine": feed yourself inputs, capture in a notes app, schedule.

**Hooks / what travels:**
- First 3 seconds decide everything. Test many hooks (Heres brand).
- Pain in the buyer's own words > clinical/generic. Title does 3 jobs: name the pain, promise a fix, signal a "system."
- "Overstimulated" one-word tee = ~$40k from one listing. Sarcastic/witty text travels on TikTok Shop + Etsy.
- "FYP" comment hack (Dan Martell): search a topic, comment "FYP" on ~10 videos, your feed retrains in days. Train your feed deliberately.

**Day-trading attention** (Gary Vaynerchuk): post 3-12 pieces across the 7 platforms *today*, watch organic algorithmic reach, then make another decision later today. Old job of media dollars = hide bad creative; new job = *amplify* proven creative (post organic first, only put money behind what overindexes). "Overindex vs viral": an 8,000-view post when you usually get 80 is the signal, bet on it. Facebook proper (not IG) is underused and great for 45-80 y/o with money.

**The UGC system that scales** (Nicole, ~400-500M views/mo): be your own creator first ("understand your content deeper than your creators do") → source (talkers for talking-head, expressive faces for reactions) → onboard (interview + a tailored creator *course* with a quiz; >50% who complete it go viral in 2 weeks) → manage (Discord, promote top creators to managers) → systemize (referral + dashboards). "You can always maximize the surface area of your luck."

**Platform split & creator-business ops:**
- Try each distribution strategy 2-3 weeks, "milk it," iterate until one hits.
- B2B = LinkedIn; B2C = the rest. LinkedIn "on the rise" for AI launches; X still where AI products originate (small communities → AI news pages → IG → Telegram). "Breaking/just in" in the top slug.
- Streamers/creators: "you cannot grow solely on streaming", clips/short-form for discovery, long-form for monetization (PlaqueBoyMax). Look at P&Ls monthly. The #1 brand-deal mistake everyone names: not giving the creator creative control.
- Pinterest is a *search engine*, not social, best free traffic for POD/products with zero followers.

**Cold-outreach-as-content** (Greg's 175-journalist play): 30-second selfie videos, ask isn't "cover me", it's "can we chat, I'll give you value." DM creators (50% have open DMs). "Shoot your shot, be different, use video, add value."

---

## 5. AI IMAGE / VIDEO GENERATION WORKFLOWS WORTH STEALING

**The general pipeline (clothing/product, but generalizes):**
1. ChatGPT writes the image prompt (specific; "avoid generic"). Generate model with **arms relaxed at sides** for clean torso = clothing-swap-ready.
2. Image gen: Imagen 4 (via Whisk), Nano Banana Pro (best for character/reference/brand consistency), Seedream 5.0/4.5 (SNIPED's locked tool), Higgsfield Soul.
3. Clothing/product swap: Fashion AI, or **Higgsfield Canvas** ("prompt by painting", mask the region, drop the product image, generate; no text prompt). Soul for aesthetic.
4. **Upscale to 4K before animating** (iLoveIMG), realism.
5. Video: Kling (2.1 Master / 3.0 for emotion), Seedance (best for action, follows prompts if detailed), Veo, LTX 2. ChatGPT writes the Kling prompt.
6. Audio: ElevenLabs sound effects (prompt influence ~90%), voiceover.
7. Assemble: CapCut / Premiere.

**Key craft lessons:**
- **Use synthetic characters, not celebrities/yourself, for video.** Video models guess on unseen angles → likeness drift. "No one knows what he looks like, so when he turns his head, who's to say it's wrong." 1 min of video ≈ 60,000 words of information; the starting frame only gives one angle.
- **Consistent characters:** Higgsfield Character needs ~20 images (up to 70 = better); Soul ID needs 10+ photos. Reuse via `@element` references (LTX Elements: objects, characters, locations).
- **Patterns/seamless textures:** Midjourney prompt + `--tile`.
- **Claude Design as a tool-*builder*:** reverse-prompt it to build bulk generators (text-design generator, pattern-press generator, résumé generator, budget-tracker). Uncheck "high fidelity" to save credits. Export HTML standalone or "Send to Canva." This is the sharpest image-adjacent play in the corpus, you build a custom mini-app per product type, then mass-produce.
- **Mockups make or break a listing.** Buy the exact mockups top-selling listings use (~$2-3 on Etsy); default Printify/PlaceIt mockups underperform. Listing View / Higgsfield generate them in bulk (mask region, multiply/invert blend rules, multi-region for color charts).

**The "AI ad agency" production stack** (Cedley/Higgsfield): storyboard → create a character + a character sheet/angle prompt (reuse across every frame) → route by tool (Nano Banana for image, Kling for emotion, Seedance for action, Cinema Studio for start/end-frame control) → editor + SFX. Spec ads for Nike/IKEA/League-of-Legends to build the book.

**Disclosure/legal:** AI fashion models without disclosure = "deceptive" (The Iconic case). Add small-print: "visuals enhanced with AI for style; actual garment specs unchanged." Fit is the real risk.

**The cinematography craft layer (segments 13-16, Wandering DP)**, transferable even if you never touch AI video, because it teaches what *good* looks like so you can direct/judge generated footage:
- Shoot **into the shadow**, **backlight everything** (more 3D, more control), keep the **sun/source out of frame** ("the interest is in the edges").
- **Sun wrap (good)**, bounce from the *same* side as the sun so light wraps the face, neg on the far side. **Sun sandwich (bad)**, bounce from the opposite side, flattens. This "one trick gets you 80% of the way there."
- **Depth = layers + light-to-dark-to-light variance** ("salt and pepper"), shoot into the corner/"L" of a room, get the subject off the wall.
- **Light the room, not the person**, the more advanced look makes the person feel like they belong in the space rather than perfectly keyed.
- Set the **uncontrollable element first** (the sky/window level via ND), then build the controllable subject to it; hold the sky, never clip it; favor a fat toe / underexposure.
- The "last 7 minutes" of a setup is where the look is won, give yourself time to sit and judge the monitor.

---

## 6. BRAND BUILDING FOR A SMALL AI-NATIVE BRAND

**The 30-minute brand build** (Eric Johnson's full ChatGPT pipeline, the most complete single artifact in the corpus). Run these prompts in order, each saying "avoid generic":
1. 5 brand identity/energy words → 2. Pinterest photo references → 3. movie references → 4. character references (Miles Morales, Vegeta = the mindset) → 5. environment/location references → 6. detailed ICP (age/gender split/cities/lifestyle/mindset/fashion/social behavior) → 7. 20 brand names → 8. logo concepts (for a designer) → 9. IG bio (tease the drop) → 10. Shopify password-page button copy → 11. 10 trending product ideas → 12. find manufacturer → 13. design concepts → 14. manufacturer outreach message → 15. 2-4 week marketing rollout → 16. growth-rescue tactics → 17. drop-day SMS/email series → 18. unboxing experience (10 ways, with a #UGC tag prompt).

**Brand principles that recur:**
- **"Take boring products and imagine the best possible outcome"** (Heres). Position Doran Rose as a *beauty* brand, not bedding. Sell the design + emotion; the product is the canvas.
- **Differentiate by doing the opposite** of the category; make every touchpoint one-of-a-kind.
- **Momentum > perfection.** No early decision is permanent (Amazon was "Cadabra," Google was "BackRub"). $20 AI subscription → 100 designs in a weekend.
- **Pitch the problem, not the AI.** "Nobody wakes up wanting to buy AI." Pitch market size, team, pain, traction; AI is table stakes (Dan Martell, Greg). Sam Altman: build the tool that gets *better* as the model gets better; don't bolt a use-case onto AI.
- **Brand identity is what survives past the first drop.** Retention > acquisition: "how do I give existing customers more value" before chasing new ones.
- **Trust-build for AI buyers:** head-to-head pilots/studies, predictable pricing, forward-deployed help (CaseText).

**The anti-AI-slop / analog pendulum hedge** (Gary Vee, Grace Wells, The Dogist, ElevenLabs deepfake model, SNIPED's own doctrine): as AI content floods, *genuine connection, authenticity, analog, and IP* become the differentiators. "The only safe business in the next decade is intellectual property" (Gary Vee / VeeFriends). Stop-motion and print are seeing resurgences. Blockchain/watermarking as a deepfake counter. IRL community is the named next creator frontier for 2026-27 (Dogist meetups, Grace Wells alumni brunch people flew in for, experiential/festivals). **This directly validates SNIPED's locked anti-identity-AI + analog-premium + physical-IP stance.**

**B2B is the quiet revenue cheat code** (Heres): easier to forecast, much higher profit %, smaller revenue share. Corporate gifting + omnichannel (every channel feeds the others; don't split B2B/B2C teams).

---

## 7. OTHER MAJOR RECURRING THEMES

**The Doer → Director shift.** Entry-level "doing" is gone (AI codes better than a junior). The skill is creativity + directing + taste. To make $1M/yr, "disconnect from the doing, build the machine that runs the machine" (Martell, echoing Elon's "the factory is harder than the prototype"). The 92% rule: get 92% of work done by AI, the 8% is "your magic, your fingerprint." What stays human: vision (see the future that should exist), taste (pick the 2 of 25 ads to bet on), and the emotional/people layer.

**Leverage = labor / capital / code+content** (Naval, cited by Liam, Martell). AI now spans all four and is the new "code." "AI is the only programming language programmed in English." System prompts are your new IP. SNIPED note: this is `leverage-logic`, default to code+media leverage.

**Niche ruthlessly, pick boring.** Drill down until you can't segment further; boring niches are 10x-100x less competitive. "Riches are in the niches" (Higgsfield rents apartments via AI ads; Peec AI does GEO). Pick something you have domain knowledge / a personal relationship with.

**Be relentlessly resourceful + have grit** (Amjad/Replit, Paul Graham). Most people quit after 6 hours; the win is the next day or two. Overcommunicate. "Launch launch launch, iterate iterate iterate", Replit's Hacker News hit came from a title change.

**GEO is the new SEO** (Peec AI / "Peak"). Structure content for AI readability (exact answers, FAQ pairs, no "between lunch and late afternoon"). Middle/bottom-of-funnel beats top-of-funnel (a model answers the lasagna question directly, no click). Off-page presence + social signals (Quora, Reddit already matter) decide how AI thinks of your brand. SNIPED note: this is exactly what `sniped-article` (GEO/AEO) is built for.

**Benchmarks worth holding** (creator claims, treat as direction): first dollar by day 30, $1M ARR (~$80k/mo) by day 90; target ACV $2,000/mo; 8-20 interviews to find the wedge, not thousands; stay cash-flow positive, question whether you need VC; track DAU + ACV, not vanity MAU.

---

## THE 15 SHARPEST, MOST NON-OBVIOUS PLAYS (ranked)

1. **Build a reusable skill/tool per workflow, then add "tell me when something should become a skill" to your system instructions.** The compounding moat. Skills > raw model access. Reverse-prompt the model to build the skill.
2. **Engineer the result before building the product.** Manually deliver the AI output, email it, measure if people ask for pricing. PMF before a single line of UI (Opus Clip's >60% reply, ElevenLabs' fake-prototype pivot).
3. **The free-website-to-local + offline postcard play.** Build hundreds of sites for cents, then reach them *offline* (Lob postcard + QR) because the inbox is dead and offline signals you're real. $8k MRR proof.
4. **Sell to the AI-clueless.** HVAC/roofers/plumbers/dentists. "Easiest money is selling to people who know less than you." Voice agents and speed-to-lead feel like magic to them.
5. **Reverse-prompt the model to write the long prompt for you.** Then run that prompt. Applies to brand builds, image/video gen, design tools. Also: "write the system prompt that would have generated this output I liked."
6. **The "export button" = a $1M-$100M business.** Audit your own/clients' tedious workflows; every export precedes human analysis AI can now do.
7. **Own the workflow end-to-end; never be the wrapper.** Be "AGI-pilled", assume the next model release erases anything that's just prompts. AI is *part* of the workflow.
8. **Claude Design as a custom mini-app factory.** Build a bulk generator per product type (résumés, budget trackers, pattern-press designs), mass-produce listings. Highest-leverage image play here.
9. **Buy the exact mockups winners use; mockups make/break the listing.** Default tool mockups underperform. ~$2-3 each.
10. **The 92% rule + the 8% that stays human.** Set an explicit AI-completion target per role; reserve vision/taste/emotion for yourself. Get the GitHub repo of leading app-builders' system prompts to level up your prompting.
11. **Amplify proven creative, don't hide bad creative.** Post organic across all platforms first; only put ad dollars behind what *overindexes* (8,000 views when you normally get 80).
12. **Turn virality into a system** (sourcing → course-with-quiz → management → referral). ">50% of trained creators go viral in 2 weeks." Maximize the surface area of luck.
13. **GEO: structure for AI answers, win the off-page/social layer.** FAQ pairs, exact answers, middle/bottom-funnel content, Reddit/Quora presence. The new SEO, mostly unworked.
14. **The analog/IP hedge.** As AI floods content, bet on authenticity, IRL community, physical IP. "The only safe business in the next decade is IP." Validates SNIPED's anti-AI moat directly.
15. **Compounding hard things.** 1 hard thing ≈ 1 close; 3 hard things (cold call + postcard + built site) ≈ 17 closes. Short-term-easy = long-term-hard; standing out is the whole game.

---

## A BETTER WAY TO HANDLE KNOWLEDGE AND AI SKILLS

Yes, the corpus describes a method better than chunking, and it describes it repeatedly. The founder's suspicion is correct. The better pattern is **skills + agents + distillation + eval**, not a chunk graveyard.

**1. Skills over chunks.** A "chunk" is dead text you hope retrieval surfaces. A **skill** is a small, invokable, *executable* package (markdown flow files + a trigger) that encodes *how* to do a thing, loads only when relevant, and is reusable across sessions. skills.sh holds 90,000+ of them. The corpus's explicit advice, "if a workflow is repeatable, turn it into a skill so you can reuse it later", is exactly the alternative to re-chunking the same knowledge. Knowledge you'll act on should be a skill, not a passage.

**2. Distill, don't dump.** Jake Heller's eval method *is* a knowledge-distillation pattern: figure out how the best human does the task → break into discrete steps → each step becomes a prompt or deterministic code → grade each step objectively → keep a hold-out set → customer complaints become new tests. A skill built this way is a distilled, *tested* unit of knowledge that improves over time ("a new pull request on your prompts every day"). That beats embedding raw transcripts and retrieving fuzzy neighbors.

**3. Agents + budgets + retrieval, governed.** HyperAgent's frame ("every agent gets its own prompt, tools, skills, and budget") and Agent Opus's director-of-sub-agents model are the deployment shape: a router/director assigns scoped tasks to skill-equipped sub-agents. Swarm Consensus shows the *cross-model* distillation move, query several models, synthesize, surface disagreement, better than trusting one retrieval pass. SNIPED already has this: `sniped-command-router` + `sniped-os-execution-governor` are precisely "classify the input, pull only the relevant spine, retrieve corpus chunks *only when policy says so*, output a receipt." That is retrieval-as-policy, not retrieval-as-default, the anti-chunk-graveyard design.

**4. Memory as decision journal, not document pile.** The Suleyman/Young practice (tell the AI daily what you decided and felt; monthly ask "biggest mistake in 6 months") turns memory into a queryable decision record, not a stack of notes. Distill the *decisions*, not the raw material.

**Concretely for SNIPED:** convert recurring corpus tactics into named skills (you already do this); keep this doctrine as the *single distilled reference* it is; route through the command-router so chunks are pulled only on policy; and add the "flag anything repeatable as a skill candidate" instruction to the OS. The corpus's own answer to "what's better than chunking" is: **distill into tested, invokable skills; let governed agents call them; retrieve only when policy demands; journal the decisions.**

---

## COVERAGE MANIFEST (16/16 confirmed read)

| # | File | Primary content | Confirmation line |
|---|------|-----------------|-------------------|
| 1 | seg_000.txt | 7 Claude Skills + Opus Clip (Young) AI startup playbook | "read lines 1 to 4201" |
| 2 | seg_001.txt | OpenClaw/Brandon Doyle agent businesses + $54k PDF method + Mel Robbins x Alli Miller | "read lines 1 to 4201" |
| 3 | seg_002.txt | 5 ways to make money w/ AI (Higgsfield) + Replit/Amjad Masad + ElevenLabs/Mati (start) | "read lines 1 to 4201" |
| 4 | seg_003.txt | ElevenLabs founder + Dan Martell live Q&A (leverage, 92% rule) | "read lines 1 to 4201" |
| 5 | seg_004.txt | Martell tail + Cassidy 7-step + Jake Heller/CaseText $650M + Liam Ottley + Greg Eisenberg | "read lines 1 to 4201" |
| 6 | seg_005.txt | Greg Eisenberg framework + 5 AI income streams + Bailey Vann agency + POD masterclass | "read lines 1 to 4201" |
| 7 | seg_006.txt | POD tutorials (Greg Gottfried, Mark Tilbury x2, Mac) | "read lines 1 to 4200" |
| 8 | seg_007.txt | Money With Mac POD/branding + Reddit "make money with AI" scrapes | "read lines 1 to 4201" |
| 9 | seg_008.txt | POD + AI-design ecommerce (Printify, KD, Etsy/Shopify) | "read lines 1 to 4201" |
| 10 | seg_009.txt | Claude Design bulk t-shirt/digital products + 7 Claude Skills (repeat) | "read lines 1 to 4201" |
| 11 | seg_010.txt | Bulk mockups + Gary Vee attention/IP + PlaqueBoyMax + Dogist + Grace Wells + SheMed + Heres | "read lines 1 to 4201" |
| 12 | seg_011.txt | Peec AI/GEO + AI clothing-brand tutorials + Eric Johnson brand pipeline + LTX + Higgsfield Canvas | "read lines 1 to 4201" |
| 13 | seg_012.txt | Higgsfield ecommerce mockups + Nicole app distribution + Higgsfield/Alex + cinematography critiques | "read lines 1 to 4201" |
| 14 | seg_013.txt | Wandering DP cinematography (lighting framework), AI-content outlier | "read lines 1 to 4201" |
| 15 | seg_014.txt | Wandering DP cinematography (sun wrap, grading, natural light), outlier | "read lines 1 to 4201" |
| 16 | seg_015.txt | Wandering DP cinematography (12-node grade, framework, reel tactics), outlier | "read lines 1 to 3581" |

All 16 segments confirmed read end-to-end. Segments 13-16 are a single cinematography channel the corpus ingested by accident; their craft signal (lighting/framing/grading + spec-work/reel tactics) is folded into Sections 5 and 4 above. Segments 1-12 carry the full AI/ecommerce/brand/content/image-gen doctrine.
