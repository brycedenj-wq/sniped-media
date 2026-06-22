---
name: sniped-vib-outreach
description: Draft a VIB (Visual Identity Brief) outreach DM to a target LA founder. Use when user wants to send a cold DM via LinkedIn or IG to a prospect, asks for outreach copy, references the VIB method, or needs to fill the pipeline. Follows the locked VIB SOP · 5-message sequence with the signature "soft offer / proof / specific compliment / hands-off ask" structure. Saves every drafted DM to /03_OUTREACH/_sent_dms/. Refuses generic founder spray. Refuses copy that breaks the WWP positioning rules.
---

# SNIPED VIB Outreach Skill

The cold DM machinery for SNIPED's founder pipeline. Output target: warm specific outreach that opens conversations with LA founders worth $1,500+ Reset spend or higher tiers. NOT generic spray.

---

## MANDATORY READING ON INVOCATION

Read in this order:

1. `/Users/sniper/Downloads/    SNIPED_OS/03_OUTREACH/SOP_VIB_production.md` · the locked VIB outreach SOP
2. `/Users/sniper/Downloads/    SNIPED_OS/03_OUTREACH/VIB_caption_library.md` · the phrase bank
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_wwp_proclamations.md` · Win Without Pitching positioning rules
4. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_positioning_phrases.md` · 5 failure modes to avoid
5. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_platform_split.md` · LinkedIn vs IG voice
6. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_referral_handling.md` · Pearl-network protocol (if referral)

After reading, ask:

> "Five things before I draft:
> 1. Recipient name + handle + role + company
> 2. Platform · LinkedIn or IG
> 3. Cluster · LA-Founder, Series-A, Series-B, LA-Black-Founder, Pearl-network referral, other
> 4. Visual intel · any specific work of theirs, recent post, trigger event, or angle of vulnerability
> 5. Goal · Reset booking ($1,500), Op Kit pitch ($3-8K), Brand System lead ($10K+), or warm intro for later"

---

## THE LOCKED VIB STRUCTURE

Per `/03_OUTREACH/SOP_VIB_production.md`. Every DM has 4 structural elements:

### 1. Specific compliment (not generic)
Reference SOMETHING concrete from their recent work. Generic compliments are noise.

❌ "Love your content!"
✅ "The way you sequenced the Series A announcement carousel · third frame was a sleeper hit"

### 2. Soft offer (no pressure)
Position the offer as something they might find useful · NOT a sales pitch.

❌ "I'd love to shoot you, my packages start at $1,500."
✅ "Working on a series with LA founders building category leaders. If it's interesting, I can send a one-pager."

### 3. Proof (subtle, not braggy)
One credibility signal embedded naturally.

❌ "I've shot hundreds of founders."
✅ "Last shoot was with [name] · she used the frames for the [outcome]."

### 4. Hands-off ask
One specific yes/no question, easy to answer.

❌ "Would you be interested in possibly doing a shoot at some point if you have time?"
✅ "Worth me sending the one-pager?"

---

## PLATFORM CALIBRATION (per `feedback_platform_split.md`)

### LinkedIn voice
- Trust, professional credibility, founder proximity
- Restrained register, "magazine retouch" voice
- Skeptical evaluation mode · receptive to structure, hostile to mythology
- Subject line / opener references their professional context

### IG voice
- Mythology, aesthetic gravity, taste signaling
- Heavier register, "editorial fashion" voice
- Receptive seduction mode · receptive to atmosphere, hostile to explanation
- Opener references their visual world or aesthetic instinct

NEVER cross-post the same DM to both platforms. Different voice, different angle.

---

## THE 5 FAILURE MODES TO REFUSE

Per `intel_positioning_phrases.md`:

1. **Premature pitching** · selling before establishing relevance
2. **Generic compliment opens** · "love your content" / "great work" · trash signals
3. **Volume language** · "I shoot lots of founders" · undermines premium positioning
4. **Begging tone** · "would love the chance to" / "I'd really appreciate" · self-orientation per Trust Equation
5. **Multi-CTA messes** · don't ask 3 questions in one DM

---

## DRAFT OUTPUT FORMAT

Always output as a complete artifact ready to copy/paste:

```
---
DM TO: [Name] · [@handle] · [Platform]
DRAFTED: 2026-MM-DD
ROLE: [Their role / company]
CONTEXT: [Why this person, the angle]
---

[The DM body]

---
TARGET ACTION: [What yes/no question they're answering]
ESCALATION PATH: [What happens if they say yes / no]
```

---

## SAVE-TO-DISK PROTOCOL (load-bearing)

Every DM drafted gets saved to `/03_OUTREACH/_sent_dms/YYYY-MM-DD_recipient-handle.md` using the template in `/03_OUTREACH/_sent_dms/_README.md`. NOT optional.

This ensures:
- Results conversations are possible in future sessions
- Cloud session loss doesn't lose the drafts
- Pattern analysis across multiple DMs over time
- The user can review what was sent before sending

When user is ready to send: ask "send now?" Once confirmed, update the saved file's "Sent" date and "Status" to `sent`.

---

## WHAT TO REFUSE

- **Generic compliment opens** · refuse, ask for specific intel
- **Pure pitch DMs** · refuse, restructure to VIB shape
- **Volume language** · "I'll shoot 10 founders this month" type framing
- **Bait-and-switch openers** · "Quick question" when it's a pitch
- **Multi-CTAs in one DM**
- **Cross-platform copy reuse**
- **DMs to off-positioning prospects** (e.g., volume photography lead, non-LA without Pearl referral, off-cluster)

If the prospect is off-positioning per the locked Reset / Op Kit / Brand System ICP, surface the mismatch and recommend declining the outreach rather than crafting a DM.

---

## FILES

```
sniped-vib-outreach/
└── SKILL.md (this file)
```

The actual VIB SOP, caption library, and positioning intel live elsewhere (read on invocation). This skill is the runbook, those are the material.


## Inputs
- Recipient name + handle + role + company
- Platform: LinkedIn or IG
- Cluster: LA-Founder, Series-A, Series-B, LA-Black-Founder, Pearl-network referral, or other
- Visual intel: specific recent work, post, trigger event, or angle of vulnerability (REQUIRED, no generic opens)
- Goal: Reset booking ($1,500), Op Kit pitch ($3-8K), Brand System lead ($10K+), or warm intro

## Outputs
- Complete DM in the locked VIB format: specific compliment + soft offer + subtle proof + hands-off yes/no ask
- Platform-calibrated voice (LinkedIn: restrained/professional vs IG: editorial/atmospheric)
- Saved file at /03_OUTREACH/_sent_dms/YYYY-MM-DD_recipient-handle.md (load-bearing, not optional)
- Receipt: 'VIB DM drafted for [Name] on [Platform]. Goal: [tier]. Saved to /03_OUTREACH/_sent_dms/[filename].'

## Gates
- Mandatory reads confirmed: SOP_VIB_production.md + VIB_caption_library.md + intel_wwp_proclamations.md + intel_positioning_phrases.md + feedback_platform_split.md
- DM contains all 4 structural elements: specific compliment, soft offer, proof signal, hands-off ask
- None of the 5 failure modes present: no premature pitch, no generic compliment, no volume language, no begging tone, no multi-CTA
- Prospect confirmed on-positioning (Reset/Op Kit/Brand System ICP); off-positioning leads surfaced and declined, not drafted
- Draft saved to disk before user is asked to send

## Test
- case: User says: 'DM @marcusbuild on LinkedIn. He just posted a Series-A announcement carousel where the third frame was a quiet flex about hiring his creative director. Goal: Reset booking.' Expected output: DM opens with specific reference to the third carousel frame, soft-offers the VIB founders series, embeds one named proof signal, closes with a single yes/no ask ('Worth me sending the one-pager?'). Saved to /03_OUTREACH/_sent_dms/2026-06-21_marcusbuild.md.
- expected failure: User asks to draft a DM with no visual intel, only 'I want to reach out to some LA founders this week.' Skill refuses and asks for the 5 required inputs. States that a generic compliment open is failure mode 2 and will not be drafted.
