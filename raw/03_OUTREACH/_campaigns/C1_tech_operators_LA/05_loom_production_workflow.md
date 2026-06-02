# Higgsfield-Anchored Loom Production · Workflow

Last updated: 2026-05-12

Production system for the "5-min Loom audit" front-end offer. Designed for volume: BJ-voiced master audio (record once) + Higgsfield-generated prospect-specific visuals (per prospect) = a Loom that looks personal at scale.

Stays on the hybrid-operator side: BJ's voice = methodology anchor (no AI avatar). Higgsfield = world-construction layer only.

---

## The two-layer architecture

```
LAYER 1: MASTER AUDIO (record once, reuse forever)
    ├─ 10 protocol-specific audio scripts
    ├─ Each ~3-5 min
    ├─ BJ records once on a Saturday
    └─ Output: 10 MP3s, named protocol_01.mp3 ... protocol_10.mp3

LAYER 2: PROSPECT-SPECIFIC VISUALS (Ren produces per prospect)
    ├─ Prospect's LinkedIn photo (the "before")
    ├─ Higgsfield-generated reference treatment (the "after")
    ├─ SNIPED reference frame matched to demographic (from VIB pool)
    └─ Output: 30-60 sec of visual content per prospect

ASSEMBLY: Descript (or similar)
    ├─ Master audio of matched protocol
    ├─ Visual layer overlaid
    ├─ Light text overlay (protocol header, observation, implication)
    └─ Export: MP4 / Loom-share link
```

---

## Layer 1 · The 10 master audio scripts

Record once. Saved at `/03_OUTREACH/_audit_assets/audio_masters/`. Each protocol gets its own audio template that follows the same structure:

### Master script structure (each protocol)

```
[INTRO · 30 sec · universal]
"Hey, this is BJ from SNIPED. I'm going to walk you through what
I see on your LinkedIn photo using a framework I built called the
Direction Stack · 10 protocols that describe specifically where
a photo is working or falling short. This is a free read, no pitch.
The protocol I'm seeing on your photo is [PROTOCOL NAME]."

[OBSERVATION · 60-90 sec · protocol-specific]
[Walk through what the protocol means · what's mechanically present
or absent in their photo · why this register specifically reads the
way it does]

[IMPLICATION · 60-90 sec · protocol-specific]
[Where the gap shows up · hiring posts, press cycle, sales decks,
conference thumbnails · what the photo IS doing vs what it COULD be
doing on each surface]

[THE FIX · 60 sec · protocol-specific]
[Describe what the same person could look like with the protocol
corrected · reference SNIPED's methodology · don't get into pricing]

[OUTRO · 30 sec · universal]
"If this read is useful and you want to talk about closing the gap,
my Calendly is in the email I sent. The Reset at $1,500 is the
typical path · 1 look, 20 finals, 5-day turn. But the Loom is the
diagnostic, take or leave the conversation."
```

Total: ~3.5-4.5 min per audio file. Sum across 10 protocols: ~40 min of total master audio that you record ONCE.

### Production budget for Layer 1

- Block one Saturday morning: 9 AM-1 PM
- Write the 10 scripts (or refine from `08_BOOK/The_Direction_Stack_v_final_2026-05-12.pdf`): 1.5 hrs
- Record + light edit in Descript: 2 hrs
- Output: 10 master MP3s saved permanently

**This is a one-time cost.** Once recorded, the master audio scales infinitely.

---

## Layer 2 · Higgsfield prospect-specific visuals

For each prospect (Ren executes):

### Step 1 · Diagnose the protocol (5 min · Ren reads, escalates if unclear)

Ren looks at the prospect's LinkedIn photo and assigns ONE primary protocol from the 10. Decision tree:

- Smiling, casual environment → 07 or 09
- Posture stiff, smile forced → 07
- Good mechanics, no presence → 09
- Dated, retreated, dead-eyed → 10
- Stock-corporate, no asymmetry → 03 (Squared)
- Hands clutching anything → 01 (Claw Hands)
- Caught mid-motion → 08 (Transition Freeze)

If Ren can't decide between two protocols, BJ adjudicates in Slack (30-sec ask).

### Step 2 · Generate the "after" visual via Higgsfield (10-15 min · Ren)

In Higgsfield Soul (or equivalent):

**Prompt template (Ren fills in protocol + demographic):**

```
[Subject demographic: male/female, age band, build, ethnicity]
Editorial portrait, [SNIPED visual direction reference], cream
or oatmeal wardrobe, contained intensity, slight 3/4 turn,
black backdrop, single key light from camera right, soft shadow
fall, dignified posture, no smile or contained slight smile,
hands held considered, Mamiya 7 + Kodak Portra 400 grain,
quiet luxury editorial restraint, Roversi / Meisel lane.
NOT cinematic, NOT teal/orange, NOT dramatic.
```

Generate 4-6 candidates. Pick the strongest 2-3 that match the prospect's demographic and feel like a SNIPED reference frame.

### Step 3 · Pair with prospect's LinkedIn photo + SNIPED reference frame (5 min · Ren)

In Descript / Premiere / similar:
- Open the master audio for the assigned protocol
- Layer the visual track:
  - **0:00-0:30** (intro) · prospect's LinkedIn photo full-frame, slight zoom
  - **0:30-2:00** (observation) · prospect's photo with annotation overlays · arrows pointing to protocol indicators (smile, shoulders, hand position, etc.)
  - **2:00-3:30** (implication) · split-screen · LinkedIn photo on LEFT · Higgsfield-generated "after" treatment on RIGHT
  - **3:30-4:00** (the fix) · zoom into the Higgsfield-generated treatment · slow pan
  - **4:00-4:30** (outro) · static frame · SNIPED logo + Calendly URL text overlay

### Step 4 · Export + send (5 min · Ren)

- Export MP4 (small file, ~30-50 MB) OR upload to Loom and grab share link
- Reply to the prospect's "yes send it" email with the Loom link
- Copy:

```
Here's the read. ~4 min. The Calendly's at the end if you want
to talk about closing the gap.

· BJ
```

Total per prospect: ~25-30 min Ren-led.

---

## Higgsfield codex consultation

Workflow patterns to reference from `/Users/sniper/Downloads/    SNIPED_OS/The_Higgsfield_Codex.docx` + `Higgsfield_AI_Operator_Playbook.docx`:

- Identity preservation: prospect's actual face is NEVER generated · only the "reference register" is generated using anonymous demographic-matched subjects
- Composite environment rotation: use Brutalist Monument or Monochromatic Void as backdrop options for the generated reference (per `composite_environment_rotation_v1.md`)
- Plate generation export rules: PNG at 2048px long edge, sRGB, no sharpening between Higgsfield and editor

**Do NOT:**
- Use Higgsfield to generate the prospect's face
- Use AI avatar tools (Synthesia, HeyGen) for the audio · those cross the identity-AI line
- Generate "fantasy" portraits that don't match SNIPED's actual deliverable register · the Higgsfield output must look like what a SNIPED shoot would actually produce

---

## Volume math

Assumptions:
- 500 emails/day × 5% reply rate = 25 replies/day
- Of those 25: ~50% positive (audit requested) = ~12-13 audit requests/day
- 5 work days/week: ~60-65 audit requests/week

Ren's production capacity:
- 30 min per Loom
- 65 Looms/week = 32-33 hrs/week

That's nearly full-time. Two options:

**Option A: Throttle email volume.** Send 200/day instead of 500/day. ~5 audit requests/day, ~25/week, ~12 hrs/week of Loom production. Sustainable for Ren part-time.

**Option B: Tiered Loom production.** Tier 1 prospects (highest trigger relevance) get the full 30-min produced Loom. Tier 2 get a templated 5-min screen-record-and-go version. Mix the workflow.

**Option C: Scale Ren.** If reply volume is strong enough that Looms are the bottleneck, the Loom production is a paid role · this is when SNIPED hires production support.

My recommendation: **Start with Option A.** Throttle to 200/day for the first 4 weeks. Validate reply rate, audit-conversion rate, and Reset close rate at low volume. If the math works (1-2 Resets/week from cold email), THEN scale to 500/day with Option B or C.

---

## Quality check before sending each Loom

Ren verifies before sending:
- [ ] Audio is the right protocol for the diagnosed photo
- [ ] Prospect's photo is shown clearly in the first 30 sec
- [ ] Higgsfield-generated reference matches the prospect's demographic (not a different gender, not a different ethnicity · this is the identity-respect line)
- [ ] No AI artifacts visible in the generated reference (extra fingers, weird eyes, etc.)
- [ ] Calendly link in the outro is current
- [ ] File size under 100 MB
- [ ] Loom share link works in incognito browser (no auth required to view)

If any fail → re-export. Quality is the trust signal.

---

## Saving the Loom artifact

Each Loom saves to:
```
/03_OUTREACH/_campaigns/C1_tech_operators_LA/_looms_sent/
   2026-05-XX_firstname_lastname_company_protocol-NN.mp4
```

The naming convention makes later analysis possible (which protocols converted, which didn't).

---

## After 1 month of data

Review the Loom workflow:
- Which protocols are most common in the inbound replies?
- Which protocols convert audit → call best?
- Are there scripts that need rewriting?
- Is Higgsfield producing usable visuals at the rate we need?
- Has the prospect ever pushed back on the AI-generated visuals?

Iterate the workflow monthly. Don't over-optimize before week 4.
