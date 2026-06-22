---
name: sniped-caption-writer
description: Write captions for SNIPED IG posts, LinkedIn POVs, or carousel content in the locked SNIPED voice. Use when user has a post needing caption, asks "what should the caption be," is about to ship a hero composite or carousel, or needs first-comment hashtags. Calibrates voice per platform (IG = mythology / editorial fashion, LinkedIn = trust / structured / case study). Applies v3 LUXURY restraint · short, declarative, atmospheric, no emojis, no process talk on IG, no narrative cinematic theatrics. Refuses generic content marketing voice.
---

# SNIPED Caption Writer Skill

Caption-writing for SNIPED posts in the locked voice. Output target: copy that feels Loewe campaign on IG, founder-trust on LinkedIn, never YouTube-thumbnail-style.

---

## MANDATORY READING ON INVOCATION

Read in this order:

1. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_platform_split.md` · LinkedIn vs IG voice
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_visual_direction_luxury_editorial.md` · the locked aesthetic direction
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_positioning_phrases.md` · phrase bank + 5 failure modes
4. `/Users/sniper/Downloads/    SNIPED_OS/07_CONTENT/linkedin_pov_bank.md` (if exists) · LinkedIn POV templates
5. `/Users/sniper/Downloads/    SNIPED_OS/07_CONTENT/caption_templates.md` (if exists) · existing caption shapes
6. `/Users/sniper/Downloads/    SNIPED_OS/07_CONTENT/hook_library.md` (if exists) · hook patterns

After reading, ask:

> "Three things before I draft:
> 1. Platform · IG hero post / IG carousel / LinkedIn POV / Threads / Story
> 2. The frame · share image OR describe content + context
> 3. Goal · awareness / portfolio update / case study / hiring signal / network warmth?"

---

## PLATFORM VOICE CALIBRATION

### IG hero post (luxury editorial register)
- **Length:** 1-3 lines max. Sometimes one line.
- **Tone:** declarative, atmospheric, observational
- **No process talk** ("how I made it" belongs on LinkedIn, never IG)
- **No emojis** (break the register)
- **First-person rare** · usually third-person or observational
- **Hashtags:** 3-5 in first comment, all editorial-fashion tier
- **Reference moves:** how Loewe / The Row / Saint Laurent caption campaign photography

✅ "Yae · 04 · Brutalist study"
✅ "The fourth in the series. Concrete holds her better than light."
✅ "Quiet rooms make loud subjects."

❌ "Obsessed with how this turned out 🔥"
❌ "Shot this with my Canon R6 II at f/2.8, edited in Lightroom..."
❌ "Tell me what you think in the comments!"

### IG carousel
- **Length:** can be slightly longer to introduce the series (3-5 lines)
- **Same restraint rules** as hero post
- **Often ends with a chapter title or series tag**

### LinkedIn POV
- **Length:** 200-400 words optimal
- **Tone:** structured, observational, teaching not pitching
- **Hook:** specific observation, not general claim
- **Body:** 3-5 short paragraphs, each one a single idea
- **Close:** soft, invitational, no aggressive CTA
- **Per `feedback_platform_split.md`:** LinkedIn audience is in skeptical evaluation mode. Lead with structure, end with offer if relevant. Never lead with pitch.

### Threads
- **Length:** 1-2 sentences max
- **Tone:** punchy observation, often slightly contrarian
- **Atmospheric without explanation**

---

## THE 5 FAILURE MODES TO REFUSE

Per `intel_positioning_phrases.md`:

1. **Generic content marketing voice** · "Here's why I love founder portraits..."
2. **Tutorial energy on IG** · process talk dilutes mythology
3. **Stunner / obsessed / fire emoji register** · cheap signals
4. **Multi-CTA messes** · pick one
5. **Cross-platform copy reuse** · IG and LinkedIn want different things

---

## SNIPED VOICE FINGERPRINTS

Patterns that should appear in SNIPED captions:

- **Single-word frames as titles** · "Yae." "Brutalist." "Series."
- **Em-period transitions** · "Yae. The fourth." (NOTE: em-dashes BANNED. Use period transitions.)
- **Observation over claim** · "Concrete holds her" not "I created a Brutalist composite"
- **Architectural / material language** · concrete, fabric, light, room, surface
- **Editorial restraint** · short sentences. Long pauses. Few adjectives.
- **First-name model references** · "Yae" or "Marcus" not "the model"
- **Series indexing** · "04" / "the fourth" / "chapter 2" implies a body of work

---

## OUTPUT FORMAT

Always output 3 caption options at the chosen length, plus first-comment hashtags:

```
PLATFORM: [IG hero / IG carousel / LinkedIn POV / Threads]
FRAME: [brief description]

OPTION 1 (most restrained):
[caption]

OPTION 2 (slightly more narrative):
[caption]

OPTION 3 (most declarative / strongest):
[caption]

FIRST-COMMENT HASHTAGS (for IG):
#editorialportraiture #fashioncampaign #luxuryeditorial [+ 1-2 more relevant]
```

User picks. If they want a fourth option that splits the difference, write it.

---

## HASHTAG DISCIPLINE

For IG:
- ✅ #editorialportraiture #fashioncampaign #luxuryeditorial #brutalistphotography #studiophotography #editorialfashion #portraitphotography (tier 1)
- ❌ #photography #lightroom #photographer #photooftheday #picoftheday (tier 0 noise)
- 3-5 max, always in first comment for clean grid
- For Brutalist Monument posts specifically: #brutalism #brutalistphotography #brutalistarchitecture work as 2nd-comment supplements

For LinkedIn:
- 2-3 max
- Use professional/business hashtags · #FounderBranding #VisualIdentity #Photography (the audience expects them)
- Don't stack in first comment · put inline at end of post

---

## ABSOLUTE BANS (per `/Users/sniper/.claude/CLAUDE.md`)

- **No em-dashes (—).** Lifetime ban. Use colons, periods, parentheses, or arrows instead.
- **No emojis** unless user explicitly requests
- **No "obsessed," "stunner," "fire," "literally"** · these are amateur signals
- **No process talk on IG** · save for LinkedIn

---

## WHAT TO REFUSE

- Captions that lead with hashtags
- Captions over the platform-appropriate length
- Captions in the "look at me" / "tell me what you think" register
- Cross-platform copy reuse (IG copy reused on LinkedIn or vice versa)
- Captions that explain the technical work (on IG)
- Captions that pitch services in the body (use the bio for services)

---

## FILES

```
sniped-caption-writer/
└── SKILL.md (this file)
```


## Inputs
- Platform target: IG hero post / IG carousel / LinkedIn POV / Threads / Story
- The visual frame: image file OR description of content and context
- Post goal: awareness / portfolio update / case study / hiring signal / network warmth
- Optional: existing phrase bank or caption templates from 07_CONTENT/

## Gates
- No em-dashes anywhere (lifetime ban per ABSOLUTE BANS section)
- No process talk in IG captions and no cross-platform copy reuse between IG and LinkedIn
- No hashtags leading the caption body (first comment on IG, inline at end on LinkedIn)
- No emojis unless operator explicitly requests; no 'obsessed/stunner/fire' amateur signals
- Caption length within platform ceiling: 1-3 lines IG hero, 200-400 words LinkedIn POV, 1-2 sentences Threads

## Test
- case: BJ just finished a brutalist composite of a founder named Marcus. Platform: IG hero post. Goal: portfolio signal. Expected output: 3 options in declarative/atmospheric register ('Marcus. 07. Concrete study.' tier), plus a first-comment hashtag block with #editorialportraiture and 2-4 editorial-fashion tags. No process talk, no emojis.
- expected failure: If no platform is specified and no image or description is provided, the skill must ask the three intake questions (platform / frame / goal) before drafting. Producing a generic caption without those three anchors is a refusal condition.
