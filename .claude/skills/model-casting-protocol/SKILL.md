---
name: model-casting-protocol
description: Practical shoot-quality protocol for finding, selecting, communicating with, and locking models without chaos. Use whenever the user wants to cast a model, find talent, book a model, write a casting call/post or casting DM, build a shortlist, vet a model, handle a model who flaked, set rate/usage/release terms, or prep talent before shoot day. Books for the job not just the look; reliability is part of talent. Composes with sniped-direction-stack (intake), os-face-lock (look match to reference), and the photo/composite domain.
---

# Model Casting Protocol

Find, select, communicate with, and lock the right model for the job without chaos. Pretty is not enough; you book for the shoot, not the face.

## Hard laws
1. Pretty is not enough.
2. Reliability is part of talent. A flake is a miscast, however good the look.
3. Book for the job, not just the look.
4. Confirm availability, comfort, usage, pay, and expectations BEFORE shoot day. In writing.
5. No vague "maybe" bookings. A maybe is a no until it is a written yes.
6. Protect the brand before protecting someone's personal IG preferences.
7. If the model's edits/preferences conflict with brand integrity, brand final wins (state this up front).

## Required inputs (ask for any missing, one batch)
shoot concept · brand/product · date/time/location · usage (where it runs, how long) · pay/rate · model requirements (look, body language, register) · wardrobe/beauty requirements · deliverables · reliability risk tolerance · release requirements.

## Step 1 - Define what the shoot needs from the model (not just the look)
From the concept (pull sniped-direction-stack if intake is unclear), write the casting criteria across: look (match to the reference/world via os-face-lock language), body language/register (deadpan, warm, editorial, athletic), confidence on camera, availability for the date, reliability signal, comfort with the wardrobe/usage (e.g. swimwear), and release willingness. Rank which 2-3 are non-negotiable.

## Step 2 - Casting post / call
Write a tight casting post stating: concept (one line), date/time/location (city + general, not exact address publicly), paid (state it is paid + rate or "paid, DM for rate"), usage in plain terms, the look/register, wardrobe note, release requirement, and how to apply (DM + portfolio/IG + availability confirm). Brand-safe, no exact private details in public.

## Step 3 - Shortlist scorecard (score, do not vibe)
For each candidate score 1-5: look-match-to-reference · register/body-language · confidence · availability (hard yes/no for the date) · reliability signal (response speed, past flake risk, professionalism) · usage/comfort agreement · release willingness. Availability and reliability are gates, not points: a no on either disqualifies regardless of look.

## Step 4 - DM / outreach script
Warm, professional, specific: who you are, the concept, date/time/location, paid + rate, usage, wardrobe, deliverables, release requirement, and the explicit asks (confirm availability, confirm comfort with usage/wardrobe, confirm rate). Ask the disqualifying questions early (see red flags).

## Step 5 - Red flags that disqualify
- Vague or slow on availability ("maybe", "probably").
- Dodges usage, rate, or release questions.
- Wants approval/veto over edits in a way that conflicts with brand integrity.
- No-shows a call or reschedules loosely before you have even booked.
- Portfolio does not match the register and they cannot show they can hit it.
- Discomfort with the actual wardrobe/concept (respect it, but it is a miscast for THIS job).

## Step 6 - Lock confirmation (what "booked" means)
A model is LOCKED only when, in writing, you have: confirmed date/time/location, agreed rate + payment terms, agreed usage, agreed wardrobe/beauty, and a signed (or explicitly agreed) model release. Anything less is not booked.

## Step 7 - Pre-shoot send (call sheet info)
Before shoot day send: exact call time + address, parking/access, contact, wardrobe instructions + what to bring, beauty/hair expectations, shot/concept overview, usage reminder, and the release to sign on arrival if not already.

## Step 8 - Backup plan
Always hold a #2 from the shortlist warm. If the lock flakes, you have a named fallback + the casting post ready to re-run. Document the backup so a flake is a swap, not a crisis.

## Proof behavior
For a casting deliverable, the artifact is the LOCKED confirmation: a `PROOF_MANIFEST` (or the casting record) showing date/rate/usage/release all confirmed in writing + a named backup. "Cast locked" cannot be claimed until availability, comfort, usage, pay, expectations, and release are confirmed. A signed release is a never-relax gate.

## Outputs
casting criteria · casting post · shortlist scorecard · DM/script · confirmation message · pre-shoot call-sheet info needed · risk flags · backup plan.


## Inputs
- Shoot concept and brand or product context
- Date, time, and location for the shoot
- Usage terms: where the content runs and for how long
- Pay/rate offered and model requirements (look, body language/register, wardrobe comfort, release willingness)
- Candidate profiles or shortlist (for scoring steps)
- Deliverables and reliability risk tolerance

## Gates
- Availability hard gate: vague or slow availability ('maybe,' 'probably') disqualifies regardless of look score
- Reliability hard gate: a no-show on a pre-booking call, loose rescheduling, or known flake history disqualifies regardless of look score
- Lock definition gate: model is not LOCKED until date/time/location, rate/payment terms, usage, wardrobe/beauty, and release are all confirmed in writing
- Release never-relax gate: a signed or explicitly agreed model release is a never-relax gate; 'cast locked' cannot be claimed without it
- Brand-integrity gate: if model's edit approval preferences conflict with brand integrity, brand decision is final -- must be stated to the model before booking

## Test
- case: User says: 'I need to cast a model for the Alma Love editorial. Shoot is July 5th in Los Angeles. Paid $300 flat. Usage is organic social only for 6 months. I need someone who can hit a deadpan editorial register in swimwear. I have two candidates.' Skill asks (in one batch) for any missing inputs (release requirement, reliability risk tolerance, exact deliverables). Once inputs are in, it writes casting criteria (look-match to Alma world via os-face-lock language, deadpan editorial register non-negotiable, swimwear comfort as a gate), scores both candidates on the 7-axis scorecard with availability and reliability as hard gates, outputs a DM script for each with disqualifying questions surfaced early (availability hard yes/no, swimwear comfort, usage agreement, release willingness), and defines what 'locked' means for this booking. A named backup from the shortlist is designated. Casting record is not issued as confirmed until availability, comfort, usage, pay, and release are all in writing.
- expected failure: Skill declares a model 'booked' or 'locked' before written confirmation of availability + rate + usage + release, OR fails to surface the release requirement before the shoot, OR omits the backup plan, OR scores candidates on look only without running availability and reliability as hard disqualifying gates.


## INVOKE WHEN
- User wants to cast a model, find talent, or book someone for a shoot
- User asks to write a casting call, casting post, or casting DM
- User needs to build a shortlist, score candidates, or vet a model against look and register requirements
- User needs to handle a model who flaked, set rate/usage/release terms, or send a pre-shoot call sheet
