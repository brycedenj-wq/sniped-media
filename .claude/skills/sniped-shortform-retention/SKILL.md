---
name: sniped-shortform-retention
description: Turn a rough short-form script, caption, launch clip, ad, or talking-head concept into a high-retention sequence. Runs 5 modules: 1-second cadence polish, B-roll/visual splicer, 3 open-loop hooks, audio/SFX pacing, and an infinite-loop ending. Use for reels, TikTok, Threads, short-form video, viral scripts, retention edits, hooks, B-roll/SFX maps, and launch/ad clips. NOT for long-form film story (use creative-levelup) or landing pages (use sniped-web-builder).
---

# SNIPED Short-Form Retention

Make every second earn the next one. Take a rough short-form concept and rebuild it so viewers cannot drop off.

## When to use
A reel / TikTok / Threads / short-form video / viral script / launch or ad clip / talking-head concept needs to hold attention. Trigger words: short-form video, reel, tiktok, retention edit, hook, open loop, b-roll, sfx, infinite loop, cadence, launch clip, ad script, talking head, viral script. NOT long-form film narrative (creative-levelup) or a web page (sniped-web-builder).

## Inputs required
The rough script, caption, or concept (verbatim), the platform (reel / TikTok / Threads / Shorts), the target length, the one thing the viewer should feel or do, and whether there is existing footage or it is generate-from-scratch. Missing the script or the goal triggers the ask-human path.

## The 5 modules (run in order)

### 1. One-second cadence polish
Cut slow setup, intro fluff, and filler. Rewrite into punchy ~1-second chunks. Every line must earn the next second: if a line does not raise a question, land a hit, or move the action, delete it. Front-load the payoff tease; no "hey guys" warm-ups. Apply the copy pack: complete thoughts, one big idea, specific over generic, no hype, no em-dashes.

### 2. B-roll / visual prompt splicer
Map every line or beat to a visual: B-roll, macro insert, product shot, text card, zoom, hard cut, or carousel beat. Every visual must do one of three jobs (clarify, intensify, or pattern-interrupt); cut any visual that is just decoration. Obey the motion pack: intent in every frame, the one-color discipline survives motion, a still + push-in is not a shot.

### 3. Psychological open-loop opener
Generate 3 alternate 3-second hooks. Each must open a loop: curiosity, tension, contradiction, or unfinished business the viewer needs resolved. No generic "here's how / in this video" openers unless a specific strategic reason is named. Lean on the distribution_hook pack (MAYA, a hook in the first beat) and sniped-hit-mechanics.

### 4. Audio pacing / SFX pass
Mark where risers, drops, silence, clicks, bass hits, glitches, whooshes, or beat-cuts belong. Audio supports attention and transitions; it never spams effects. Silence is a tool (use it before a reveal). Owned music in finishing (Suno), diegetic-first in prompts.

### 5. Infinite-loop ending
Make the final line or final shot connect back into the opening so the clip replays seamlessly. Avoid a generic CTA ending; build replay logic when the format allows (the last frame answers, or re-asks, the hook).

## Output format
- Diagnosis of the current script/concept (where it loses retention, in module terms)
- Rewritten hook options (3, each a 3-second open loop)
- 1-second cadence script (line per ~second)
- Visual / B-roll map (beat -> visual -> the job it does)
- Audio / SFX map (timecode -> cue -> why)
- Infinite-loop ending (the loop-back line/shot)
- Final short-form assembly table (sec | line | visual | audio | transition)
- Retention QA checklist (pass/fail)

## Quality gate (pass/fail)
- Hook opens a real loop in <= 3 seconds (no warm-up).
- Every second earns the next (no filler line survives).
- Every visual clarifies, intensifies, or interrupts (no decoration).
- Audio supports attention, not spam.
- Ending loops back or has deliberate replay logic.
- Copy pack clean: complete thoughts, one big idea, no hype, no em-dash.

## Proof / receipt
Log: the original concept, the chosen hook, the assembly table, the retention QA pass/fail, and what needs the human (real footage, brand voice confirmation, music license). On a serious deliverable the conductor RECEIPT (OS_RECEIPT) applies; do not call it final without the QA checklist passing.

## Ask the human when
The script or the one viewer-goal is missing, the platform/length is unconfirmed, or it depends on footage that does not exist yet (route the shot/asset gap to ai-edl).

## Depends on
copy + distribution_hook + motion doctrine packs (os_doctrine.py), sniped-caption-writer (voice), sniped-hit-mechanics (distribution mechanics), OS_AUTOEDIT_DOCTRINE (assembly), ai-edl.workflow.js (if footage must be selected/assembled), os-quality-gates. EXTERNAL-RESOURCE GAP: current per-platform retention norms (hook windows, ideal length) shift; confirm live at publish time.


## Gates
- Hook must open a real loop in 3 seconds or fewer (no warm-up or 'hey guys')
- Every second must earn the next; no filler line survives the cadence pass
- Every visual must clarify, intensify, or pattern-interrupt; decoration = cut
- Audio supports attention and does not spam effects; silence is a tool
- Copy pack clean: complete thoughts, one big idea, no hype, no em-dash; ending loops back or has deliberate replay logic

## Test
- case: Operator hands a rough 30-second Instagram Reel script for a photography offer (verbatim text provided), platform Reel, goal DM inquiries. Expected: all 5 modules run in order; 3 open-loop hooks delivered; second-by-second cadence script with filler removed; B-roll map with each visual's job named; audio/SFX map; infinite-loop ending; final assembly table; QA checklist with all 6 gates marked pass or fail.
- expected failure: Skill produces a generic essay instead of the assembly table, skips labeling each visual's job, returns a generic CTA ending without loop logic, lets an em-dash or filler line survive, or calls output final without the QA checklist passing.
