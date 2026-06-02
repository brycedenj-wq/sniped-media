# Cold Email Doctrine v1

Last updated: 2026-05-12

The canonical SNIPED cold email playbook. Generalizes beyond any single campaign. When building a new campaign (C2, C3, etc.), this doc is the source of truth. When the doc and a campaign-specific brief conflict, this doc wins until the brief is updated.

Source canon consulted (per "every doc considered" principle):
- `The Cold Email Manifesto` · Berman/Indries
- `Predictable Revenue` · Aaron Ross
- `Gap Selling` · Keenan
- `Combo Prospecting` · Tony Hughes
- `Sniped_Media_Cold_Email_Rewrite_March2026.docx` · BJ's voice
- `Cold_Outreach_Sales_Pipeline_Playbook.docx` · prior playbook
- `cold_email_extraction.docx` · methodology distillation
- `baseplate_cold_outreach.docx` · BASEPLATE-stage cold patterns
- `The_Copywriting_Stack.docx` · Rule of One, Five Stages of Awareness, Halbert
- `The_Outbound_Stack.docx` · infrastructure, ICP Waterfall, three-email architecture
- `Sniped_Media_Cold_Outreach_SOP.docx` · operational pattern
- `Higgsfield_AI_Operator_Playbook.docx` · Loom production workflow
- `intel_hit_mechanics` memory · Hit Makers six mechanics
- `intel_status_psychology` memory · status psychology of premium buyers

---

## Section 1 · The Strategic Thesis

Cold email is a math game layered on top of a trust game.

The math: high volume of targeted sends, measured by reply rate, filtered through qualification, converted on calls.

The trust: every touchpoint must prove relevance in the first 5 seconds or get deleted. You are not trying to close on email 1. You are trying to earn a reply.

The combination produces the SNIPED cold email engine: precision targeting + methodology-anchored offer + low-friction CTA + Loom-audit front-end + Reset back-end.

What it is NOT:
- Not the LinkedIn VIB lane (Tier 0 CRM founders · low volume, high precision)
- Not generic outreach (no "I hope this finds you well")
- Not a brochure-and-quote business (we don't send pricing in email)
- Not a place to invent new strategies · the doctrine is locked, only campaigns vary

---

## Section 2 · The Five Locked Principles

These hold across every campaign. Violate them and outcomes underperform.

### 2.1 The Rule of One (per `The_Copywriting_Stack`)

Every email addresses **one reader, one idea, one offer, one action.**

- **One reader.** Not "operators." A specific person · "James, VP of Engineering at a 200-employee Series B SaaS in LA who posted on LinkedIn last week about hiring."
- **One idea.** A single core promise. "Your photo reads engineer, not VP." Not three problems stacked.
- **One offer.** A single front-end, no tiered options. "5-min Loom audit." Not "audit, sample frame, or consult."
- **One action.** One CTA. "Want me to send it?" Not "reply, book a call, or visit the site."

91 of the top 100 direct-response offers in Agora Publishing history followed this rule. The Rule of One is non-negotiable.

### 2.2 Match the Awareness Stage (per Schwartz)

Cold prospects sit at Problem Aware or Solution Aware. Write to that stage.

- **Don't write to Unaware**: don't start by educating someone on what a "Direction Stack" is. They don't care yet.
- **Don't write to Product Aware**: don't assume they know SNIPED · they don't.
- **Calibrate to Problem Aware**: acknowledge the problem they already half-know they have ("your LinkedIn photo isn't doing the work it should").
- **Move them one stage**: by email 3, they should be Solution Aware (they know the Direction Stack diagnostic exists as a solution category).

### 2.3 Sell Outcomes, Not Deliverables (per `Cold_Outreach_Sales_Pipeline_Playbook` + Five Offers framework)

Nobody buys "photography." They buy "raise status" or "more booked clients" or "press cycle that lands."

The Five Offers (test against each):
1. Save time
2. Make money
3. Save money
4. **Raise status** ← primary for SNIPED (founder portrait business)
5. Improve health / longevity

For SNIPED specifically:
- Don't sell "professional headshots."
- Sell "operator gravity on hiring pages, press cycles, and board surfaces."
- Status is the lever. Status > utility for premium professional services.

### 2.4 Personalization Split (per `The_Outbound_Stack`)

Use AI for the personalization LINE ONLY. Keep the body human-written and tested.

- **Line 1**: AI-generated reference to something specific the prospect did (recent LinkedIn post, hiring announcement, funding event). NOT generic.
- **Lines 2-4**: Static, human-written, A/B tested. Same across every recipient in the segment.

Why: lets you test body copy as a controlled variable while personalization adapts per recipient. If reply rates shift by segment, body works and segmentation is the variable. If reply rates shift by personalization quality, body is constant and personalization is the lever.

The uncanny valley: bad AI personalization is worse than no personalization. Read every AI-generated line aloud. If it sounds like a robot trying to sound human, cut it.

### 2.5 Gap Selling on the Call (per Keenan)

The cold email books the call. The call closes the deal. On the call: Current State → Future State → The Gap.

- **Current State**: where the prospect's photo is now (protocol read)
- **Future State**: where it could be (operator register, specific surfaces)
- **The Gap**: the value · the bigger the gap, the more valuable the Reset

No problem, no sale. If on the call the prospect doesn't have the gap, don't push. Move on.

---

## Section 3 · Infrastructure

### 3.1 Sending Architecture (locked)

- 5 sending domains (NOT the primary `snipedmedia.com`)
- 5 inboxes per domain = 25 total
- 30 emails/inbox/day MAX = 150/day capacity (run at 100-120 to stay safe)
- Continuous warmup on all inboxes via Instantly
- Plain text only · no HTML, no images, no links in body
- Signature: name + website only

### 3.2 Domain performance (locked from March 2026 data)

| Domain | Reply rate | Status |
|---|---|---|
| `trysnipedmedia.com` | 5.1% | KEEP · top performer |
| `snipedstudio.com` | 4.7% | KEEP · top performer |
| `brycedenphoto.com` | 4.5% | KEEP · top performer |
| `snipedproduction.com` | 2.0% | MONITOR · run inbox placement test, re-warm if needed |
| `snipedvisuals.com` | 0.8% | PAUSE + re-warm 14 days · then re-evaluate |
| `admin@snipedmedia.com` | 0% (24 sent) | KILL FROM COLD · primary business email, never use again |

### 3.3 Deliverability targets

| Signal | Healthy | Red Flag |
|---|---|---|
| Open rate | 40-60% | <30% = inbox placement issue |
| Reply rate | 3-5% | <1% = copy/targeting failure |
| Positive reply rate | >1% | <0.5% = offer/ICP mismatch |
| Bounce rate | <3% | >3% = unverified list, stop sending |
| Spam complaint rate | <0.1% | >0.1% = immediate domain damage |

Below floor on any signal: pause, diagnose, do not keep sending.

### 3.4 Spam triggers to AVOID

- Money language: "earn," "make money," "$X"
- Guarantee language: "guaranteed," "risk-free," "100%"
- Urgency language: "act now," "limited time," "expires"
- Excessive caps or punctuation (no more than 1 exclamation point per email)
- HTML formatting beyond paragraph breaks
- Calendly / Loom / PDF links in email 1 (huge spam signal · save for email 2 or post-reply)
- Subject lines that look like marketing ("FREE Audit," "QUICK QUESTION!!!")

---

## Section 4 · The ICP Waterfall

### 4.1 Many small targeted lists, not one big one

Break the addressable market into segmented lists by trigger combination. A 5,000-person list with tailored sequence outperforms a 100,000-person list with generic sequence. Always.

### 4.2 Tier hierarchy

| Tier | Criteria | Treatment |
|---|---|---|
| **Tier 1** | 3+ triggers (role + funding/news + behavior signal) | Highest priority. Most personalization. AI-enriched line 1 referencing specific recent activity. |
| **Tier 2** | 2 triggers | Strong send. Personalized line 1 referencing one trigger. |
| **Tier 3** | 1 trigger (role fit only) | Standard sequence. Moderate personalization. Volume play. |
| **Tier 4** | Role fit, no behavior signal | Low-priority. Defer to inbound or skip. |

### 4.3 Top performing triggers (per outbound stack)

In order of measured performance:

1. **Recent LinkedIn post engagement** · prospect is active, observable, specific topic is the hook
2. **Recent job change** (joined within 60 days) · new mandate, new budget
3. **Recent funding announcement** · cash in bank, investor pressure to scale
4. **Recently founded company** (under 2 years) · services being set up for first time
5. **Active job listings** · growth signal + budget signal
6. **Technology in use** · integration/optimization angle
7. **Industry-specific news** (regulatory, competitive, M&A) · external pressure creates urgency

### 4.4 Tagging on pull (Ren executes)

Every lead pulled gets tagged on receipt:
- Tier (1/2/3/4)
- Primary trigger (if any)
- Demographic confirmation (gender, age range, ethnicity · for VIB reference frame matching)
- Likely protocol read (P01-P10 · based on LinkedIn photo audit before email 1)

The protocol read becomes the `icebreaker` merge variable (per March 2026 rewrite pattern).

---

## Section 5 · The Three-Email Sequence Architecture

### 5.1 Email 1 · The Opener (Day 0)

**Job:** introduce the offer with highest-priority personalization. Earn the reply.

**Structure (4 lines max):**
1. **Why you, why now** · trigger-based opener referencing something specific
2. **Clear offer in one sentence** · what you do, for whom, with what outcome
3. **One proof point** · methodology reference, specific deployment context, or single data point
4. **Single CTA** · low-friction · NEVER "book a call" in email 1

**Constraints:**
- Under 80 words. Under 70 ideal.
- 5th-7th grade reading level.
- Subject line: 2-6 words, lowercase, curiosity-driven. NEVER the offer.
- No links in body. No PDF/Loom/Calendly attached.
- Signature: name + website only.

### 5.2 Email 2 · The Threaded Add (Day 3)

**Job:** add context that was held back from email 1. Same thread (reply, no subject change).

**Structure:**
- Brief bump ("Following up on the note below" or similar)
- Specific NEW info · process detail, secondary proof, data point about the problem
- Same CTA or slightly different angle on the same CTA

**Constraints:**
- Under 50 words.
- Threaded (no subject change).
- Distributes the personalization across the sequence · do NOT front-load everything in email 1.

### 5.3 Email 3 · The Break (Day 7)

**Job:** lower friction. New subject, new thread. Either offer-switch OR breakup-redirect.

**Approach A · Offer Switch:** change the value proposition. "Instead of a call, happy to send the Direction Stack scorecard." Lowers friction. Creates a give-away exit.

**Approach B · Breakup Redirect:** acknowledge non-response, ask for referral. "If you know someone on your team better suited, happy to be introduced. If not, no worries."

**Constraints:**
- New subject line.
- Under 65 words.
- Closes the loop respectfully · keeps door open for re-engage cycle.

### 5.4 After Email 3

- No follow-up. Period.
- Move to suppressed-active list. No more cold sends for 90 days.
- Quarterly TAM refresh (Section 9) re-engages.

---

## Section 6 · The Front-End Offer

### 6.1 What works for SNIPED · Loom Audit

The SNIPED-specific front-end offer is the **5-min Loom audit** built per `/03_OUTREACH/_campaigns/CN_*/05_loom_production_workflow.md` (Higgsfield-anchored static visuals + BJ-recorded master audio per protocol).

**Why it works:**
- Methodology-first selling (per Win Without Pitching) · demonstrates the Direction Stack BEFORE asking for money
- Low friction · "yes send me one" is a $0 ask
- Productized at volume · master audio recorded ONCE, Higgsfield visuals per prospect
- Stays on hybrid-operator side · BJ's voice anchors, AI for world-construction layer only
- High perceived value · 5 min of recorded methodology beats a brochure every time

### 6.2 What does NOT work

- "Want to hop on a call?" · too much friction in email 1
- "Free consultation" · sounds salesy
- "Brochure" or static PDF · static collateral kills trust
- "Sample shot" or "free photo" · sets up a transactional dynamic SNIPED is trying to escape

### 6.3 Workshop Funnel · future option

Per `The_Outbound_Stack`, the Workshop Funnel can outperform direct-to-call funnels in B2B service businesses:
- Math: 5,000 emails → 200 replies (4%) → 50 attendees (25%) → 10 calls (20%) → 3 deals (30%)
- Format: 45-min live "How operator photos actually work" webinar, methodology-led, soft pitch at end
- When to test: month 3+ once C1 baseline is established and Ren has bandwidth

### 6.4 Value-First Boomerang · alternative front-end

Per `The_Outbound_Stack`, an alternative to the Loom audit:
- "Send me your LinkedIn photo, I'll send back 3 specific direction notes"
- Free tangible deliverable creates reciprocity
- Lower production time than Loom (~5 min per vs ~25 min)
- Lower trust signal (text vs video)
- Worth testing as a variant against the Loom in month 2

---

## Section 7 · Reply Handling

### 7.1 The 7 reply types

Templates per campaign live in `/03_OUTREACH/_campaigns/CN_*/04_reply_scripts.md`. The categories:

1. **Positive ("yes send it")** · queue Loom production · 2-hour SLA on the reply
2. **Question ("what do you do?")** · one-paragraph explainer + re-offer
3. **Send-info ("send a brochure")** · refuse brochure, re-offer Loom (no static collateral)
4. **Not-now ("maybe later")** · warm exit, no push
5. **Already-have-someone** · reframe as additive (Loom as briefing for their current photographer)
6. **No-budget** · clarify Loom is free
7. **Hostile** · clean exit, suppress, never email again

### 7.2 Reply SLAs

| Type | Target SLA | Why |
|---|---|---|
| Positive | 2 hours (30 min ideal) | Speed-to-lead studies: 391% sales increase responding within 5 min vs 1 hour |
| Question | 4 hours | Curiosity decays fast |
| Deflection | 24 hours | Lower urgency, OK to batch |
| Negative | 24 hours | Quick clean exit, then drop |

### 7.3 Mom Test on the discovery call (per Rob Fitzpatrick · `The_Outbound_Stack`)

When the reply converts to a booked call:
1. **Talk about their life, not your idea.** Ask about what they actually do, how they spend time, what frustrates them. NEVER ask if your idea is good.
2. **Ask about specifics in the past, not generics about the future.** "When was the last time that happened?" beats "Would you ever use X?"
3. **Talk less, listen more.** If you're talking more than the prospect, you're pitching not learning.

Deflect bad data:
- Compliments → thanks, redirect to their life
- Generics ("I usually...") → "when's the last time?" anchors to specifics
- Hypotheticals ("I would buy that") → "what are you doing about it today?"
- Feature requests → "why do you want that?" digs to motivation

Close every call with a commitment or rejection. No zombie leads.

---

## Section 8 · Performance Benchmarks

### 8.1 Floor / Target / Strong

| Metric | Floor | Target | Strong |
|---|---|---|---|
| Open rate | 30% | 45% | 55%+ |
| Reply rate | 1% | 3% | 5%+ |
| Positive reply rate | 0.5% | 1.5% | 3%+ |
| Booked call rate (of positive) | 20% | 50% | 70%+ |
| Show-up rate (of booked) | 60% | 80% | 90%+ |
| Close rate (of attended) | 10% | 25% | 40%+ |
| Bounce rate | <5% | <3% | <1% |
| Spam complaint rate | <0.3% | <0.1% | <0.05% |

### 8.2 Minimum statistical significance

Don't draw conclusions from small samples:
- 1,000 emails per variant before comparing subject lines / openers / offers
- 5,000 emails before concluding a segment converts or doesn't
- 50 booked calls before concluding a discovery framework works or doesn't

### 8.3 Diagnostic decision tree

- **Open rate < 30%** → deliverability failure · check DNS, rotate domains, rewarm
- **Open rate fine, reply rate < 1%** → copy or offer mismatch · test against Five Offers (especially Raise Status)
- **Reply rate fine, positive reply < 0.5%** → attracting wrong replies · review what positives are saying yes to, amplify that angle
- **Positive replies not converting to booked calls** → CTA friction · test softer asks before calendar links
- **Booked calls but low close rate** → call mechanics issue, not outbound · review Gap Selling + Mom Test discipline

---

## Section 9 · Quarterly TAM Refresh

Per `The_Outbound_Stack`: re-sequence the entire TAM every 90 days.

**Why:** prospects who passed last quarter may be active buyers this quarter. Priorities shift in 90 days. The list doesn't stay converted-or-rejected forever.

**How:**
- Pull fresh enrichment data on the same list (new LinkedIn posts, new funding rounds, new hires)
- Use a different offer angle or value proposition than the prior cycle
- Each cycle gets a different protocol-based icebreaker

**Cadence:**
- Q1 cycle: campaign launches with offer angle A (e.g., "raise status")
- Q2 cycle: same list re-sequenced with offer angle B (e.g., "save time" or specific surface use case)
- Q3 cycle: same list with offer angle C
- Q4 cycle: same list with offer angle D

This prevents list exhaustion. Keeps the pipeline regenerating without needing new list sources.

---

## Section 10 · Common Mistakes (per cold email corpus)

### 10.1 Email-level mistakes

- "I hope you're doing well" / "Hope this email finds you well" · template garbage, cut
- "Just wanted to quickly reach out" · spam language, cut
- ALL CAPS subject lines · marketing tell, cut
- File attachments · trigger spam filters
- Images in email 1 · same
- Pricing in cold email · NEVER. Price goes to discovery call only.
- Pitching the full Reset in email 1 · email's job is to start the conversation, not close
- Following up more than 3 times · harassment + reputation damage
- Sending on weekends · tanks reputation
- Sending from primary domain · one spam complaint kills business email
- Emojis in subject or body · instant spam classification on most clients
- Generic greetings ("Dear Sir/Madam," "Hi there") · delete signal

### 10.2 Strategy-level mistakes

- One big undifferentiated list · hides which segments respond, forces generic copy
- Testing trivial wording changes ("chat" vs "exchange") · waste of cycles
- Testing without statistical significance (changing copy after 50 sends) · noise, not signal
- Blasting all emails at 9 AM sharp · spam pattern (randomize within window)
- No tracking systems · campaigns can't be optimized without data
- Skipping the Gap Selling discovery on calls · zombie leads
- Expecting replies in first 48 hours · most replies come 24-72 hours after send
- Reusing the same sequence quarter after quarter without refreshing offer angle

### 10.3 SNIPED-specific mistakes

- Sending cold email to LA tech founders · they're the LinkedIn VIB lane, do not cross-channel
- Using `admin@snipedmedia.com` for cold · damages primary business email forever
- Sending pricing in reply 2 before audit Loom is delivered · undercuts methodology-first selling
- Letting Ren write copy or make pricing exceptions · escalate every time
- Treating the Loom as a substitute for actual shoot quality · the Loom is the diagnostic, not the deliverable

---

## Section 11 · Campaign Lifecycle

### 11.1 Pre-launch (Week 0)

1. ICP locked (person + niche + geography + company size)
2. Front-end offer locked (default: Loom audit per `05_loom_production_workflow.md`)
3. Super Search filter spec written and validated (returns 5K-25K results)
4. Email 1 + Email 2 + Email 3 drafted with 2-3 variants for email 1 A/B
5. Reply scripts adapted from canonical 7-type templates
6. Ren cadence doc written
7. Master audio for 10 protocols already recorded (one-time prerequisite · see `/03_OUTREACH/_audit_assets/audio_scripts/`)
8. Suppression list checked (no overlap with LinkedIn VIB recipients, prior campaigns)

### 11.2 Launch (Week 1)

1. Lead pull (1,200-1,500 leads via Super Search)
2. Lead clean + tier tag + protocol diagnosis pre-audit
3. Upload to Instantly, map merge variables (firstName, companyName, icebreaker, etc.)
4. A/B variants of email 1 distributed at equal split
5. Sequence cadence set (Day 0, Day 3, Day 7)
6. Sending starts Tue-Thu, 7-9 AM PT
7. Suppression list active (replies pause sequence)

### 11.3 Iteration (Week 2-4)

1. Daily Unibox check (3x/day per Ren cadence)
2. Loom production queue per positive reply
3. Weekly status to BJ: opens, replies, positives, calls booked
4. After 1,000 sends per variant: declare email 1 winner, run winner at 100% in Week 3+
5. After 4 weeks: evaluate vs. benchmarks, decide next iteration

### 11.4 Optimization (Week 5+)

1. Test next variable (NOT trivial wording) · new pain hook, new offer angle, new trigger combination
2. Add second variant of email 1 against the winning angle
3. Consider Workshop Funnel as additional layer if reply rate justifies
4. Consider Value-First Boomerang as alternative front-end if Loom production becomes bottleneck

### 11.5 Quarterly refresh (Month 3+)

Re-sequence the TAM per Section 9. Different offer angle. Fresh enrichment.

---

## Section 12 · The Two-Channel Outbound Architecture

SNIPED runs TWO outbound channels in parallel. Different ICPs, different mechanics.

### 12.1 LinkedIn VIB lane · precision spear

- ICP: LA tech FOUNDERS (Tier 0 CRM, sourced manually by Ren)
- Volume: 4-6 VIBs/week
- Asset: bespoke VIB PNG (LEFT prospect photo / RIGHT matched SNIPED reference)
- Mechanics: personalized DM with VIB attached, 1:1 conversation
- Conversion: VIB → reply → call → Reset
- Doctrine: `/03_OUTREACH/SOP_VIB_production.md`

### 12.2 Cold email lane · volume net

- ICP: LA tech VPs / Directors / non-founder C-Suite (Tier 1-4 by trigger count)
- Volume: ~150 emails/day (~750/week, ~3000/month)
- Asset: 3-email sequence + Loom audit on positive reply
- Mechanics: high-volume automated send with personalized line 1, templated body
- Conversion: email 1 → reply → Loom delivered → call → Reset
- Doctrine: this doc + `/03_OUTREACH/_campaigns/CN_*/00_BRIEF.md` per campaign

### 12.3 Zero cannibalization rule

- Cold email targets NEVER include founders (those go to LinkedIn VIB)
- LinkedIn VIB targets NEVER include random VPs without a referral relationship (those go to cold email)
- Cross-check suppression lists across both channels before any new pull

### 12.4 Combined funnel target

| Stage | Cold email | LinkedIn VIB |
|---|---|---|
| Volume / week | ~2,500 sends | 4-6 VIBs |
| Reply rate | 3-5% | 30-50% (warmer) |
| Positive reply | 1-2% | 50%+ of replies |
| Calls booked / week | 5-10 | 2-3 |
| Reset bookings / week | 1-2 | 0-1 |

Phase 1 target: $3K MRR sustained 2 months = 2 Resets/week from combined channels. The system is designed to hit this from cold email alone, with VIB as upside.

---

## Section 13 · Voice Rules (locked · lifetime)

- **NO EM DASHES.** Period. Use colon, middle dot, comma, parentheses, arrow, or two sentences.
- Plain text only. No HTML, no images, no links in body.
- Signature: name + website only.
- 5th-7th grade reading level. Hemingway / Flesch-Kincaid 70+.
- Under 80 words per email.
- One CTA per email.
- Lowercase casual subject lines. No title case, no caps lock.
- No buzzwords. No corporate tone. No "great post" energy.
- Mid-conversation feel. Slight imperfection is the goal.
- Don't lead with my expertise. Lead with the observation.
- Operator voice (per `The_Direction_Shift`): texture, not clinical perfection. The corpus is full of clean copy that doesn't get read. The slightly broken-on-purpose copy converts.

---

## Section 14 · When to revise this doc

- After 4 weeks of running first campaign · iterate based on data
- After 10K sends total · validate benchmarks
- If a new offer or front-end gets tested and outperforms the Loom audit
- If a new tier of ICP enters (e.g., expansion outside LA)
- If a new tool replaces Instantly (unlikely · infrastructure is sticky)
- Quarterly TAM refresh evaluation

BJ owns the doc. Ren proposes changes via Slack. The doc lives in SNIPED_OS · single source of truth, version-controlled.

---

## Cross-references

- `/00_BRIEF/THE_SPINE.md` · canonical SNIPED positioning
- `/00_BRIEF/CANONICAL_TRUTHS.md` · the 12 truths
- `/03_OUTREACH/linkedin_comment_doctrine_v1.md` · LinkedIn engagement (parallel surface)
- `/03_OUTREACH/SOP_VIB_production.md` · LinkedIn VIB lane (companion channel)
- `/03_OUTREACH/SOP_discovery_call.md` · call mechanics post-cold-email-reply
- `/03_OUTREACH/SOP_discovery_to_close.md` · close mechanics
- `/03_OUTREACH/_campaigns/CN_*/` · per-campaign briefs (C1 live · `C1_tech_operators_LA/`)
- `/03_OUTREACH/_audit_assets/audio_scripts/` · 10 master protocol audio scripts (one-time recording)
