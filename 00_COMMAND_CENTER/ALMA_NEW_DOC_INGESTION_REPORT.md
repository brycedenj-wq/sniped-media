# ALMA NEW DOC INGESTION REPORT

## A. Exact file path
`/Users/sniper/AI-Brain-Refinery/maybe something here.docx` (182,759 bytes, modified 2026-06-07 14:07). No embedded media in the docx; content is GitBook documentation text + an embedded tutorial-video transcript.

## B. What the document is about
**Chat Video Pro** documentation - an AI-assisted editing EXTENSION (CEP panel) that runs INSIDE Premiere Pro. Core pieces:
- **Story Cutter Assistant** (the headline tool): reads a TRANSCRIPT, finds the best spoken-word soundbites, and assembles a rough cut on the Premiere timeline. Slash commands: `/select pass` (groups best moments by category - hooks/value/CTA/emotional peaks), `/social clip`, `/top 5 soundbites`, `/batch` (multi-deliverable). Models: Claude 4.6 Sonnet, GPT-5.x, Gemini 3.1 Pro (1M context for long transcripts).
- Other assistants mentioned (not detailed in the text): Color Grade Assistant (AI color correction + LUT generation), Video Prompter, Brand Voice, Premiere Pro Guru; Workflows for AI B-roll generation, AI VFX, AI thumbnails, project-folder template, custom export presets.

## C. New principles / rules / workflows
1. **Source -> Selects -> Rough Cut** (their recommended workflow): keep the source timeline untouched; run a selects pass to a dedicated selects timeline with section markers; build the rough cut from there.
2. **Brief like you would brief a human editor**: what it's about, who it's for, what you want them to feel, runtime, platform, type, hook/CTA.
3. **/batch** one transcript -> multiple deliverables (long-form + social + select pass) in one run.
4. **Selects-first automation**: let the AI surface every usable moment; the human makes the creative call.

## D. What CONFLICTS with the current Alma Love workflow
**Nothing that applies.** Story Cutter is **DIALOGUE/TRANSCRIPT-ONLY** and explicitly does NOT handle b-roll/visual-only footage. Alma Love is a **non-dialogue, music-driven, deadpan visual commercial** - there is no transcript to cut from. So the doc's main tool **cannot be used on Alma Love**, and it does not override the visual selects-by-watching method (which is the correct method for non-dialogue footage).

## E. What IMPROVES the current workflow
- **Validation**: the "Source -> Selects -> Rough Cut" philosophy and the `/select pass` category-grouping mirror exactly what we already built for Alma (DIRECTOR_MOMENTS_MAP + EDITOR_SELECTS_MAP_V4 + EDL). The doc confirms the approach; it does not replace it.
- **Operator-side finishing route**: Chat Video Pro's **Color Grade Assistant (AI grade + LUT gen)** and **AI VFX in Premiere** are a MANUAL operator route that could do the rack-focus/grade INSIDE Premiere - exactly where the Premiere MCP failed (QE DOM `apply_effect` returns "Effect not found", `list_available_effects` = []). Worth knowing for the finishing department as a human-in-the-loop path.

## F. What should become PERMANENT OS doctrine
- The "brief the AI like a human editor (what/who/feel/runtime/platform)" principle is already embodied in STORY_PSYCHOLOGY_LAYER (`story_emotional_target`, `story_but_therefore`). No new card needed; cross-reference added.
- "Source -> Selects -> Rough Cut" is already our locked Alma method (selects map -> EDL -> cut). Promote as a named general workflow note.
- Chat Video Pro logged as an **operator-side Premiere finishing tool** in the finishing-department knowledge (NOT an MCP route Claude can drive).

## G. What should become PROJECT-SPECIFIC only
- Nothing Alma-specific changes. Story Cutter would only matter for a FUTURE dialogue project (interview/podcast/vlog/testimonial), not this swimwear commercial.

## H. What current assumptions are now STALE
- None for Alma. One clarification: "use Premiere/AI to fix the hook" now has a candidate MANUAL route (Chat Video Pro AI-VFX/Color-Grade panel) since the Premiere MCP effect-apply is proven broken. That is an operator action, not an automated one.

## I. Exact scripts/gates/cards/docs to update
- `OS_FINISHING_DEPARTMENT.md` (when built): add Chat Video Pro as an operator-side Premiere finishing/grade/VFX route + note it is dialogue-tool for Story Cutter.
- Tool registry: note "Chat Video Pro (Premiere extension)" = operator-driven, not MCP.
- NO change to: EDITOR_SELECTS_MAP, ALMA_COMMERCIAL_STORY_ARC, os_reference_gate.py, COMMERCIAL_CRAFT cards, the hook rule, the product-insert rule. The doc does not touch a non-dialogue commercial's selects/sequence/hook/grade definition.

## J. What should happen next before any render
Resume the FINISHING pass for Alma. The doc does not change the edit. The only new option it surfaces is a MANUAL Chat Video Pro grade/VFX route inside Premiere - optional, operator-run. The automated finishing decision stands: AE-MCP (no import/render) and Premiere-MCP (effect-apply broken) are proven-blocked, so the ffmpeg per-frame animated-blur rack-focus is the working route unless the operator runs Chat Video Pro manually.
