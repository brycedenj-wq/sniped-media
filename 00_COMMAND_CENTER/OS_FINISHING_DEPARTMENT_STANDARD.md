# OS FINISHING DEPARTMENT · STANDARD

The permanent SNIPED standard for turning real footage into a finished, client-ready deliverable. This is the doctrine; the dashboard (`OS_FINISHING_DEPARTMENT_DASHBOARD.md`) is the live board; the scripts in `00_COMMAND_CENTER/scripts/` are the engines.

Last locked: 2026-06-07.

---

## 0. The one law

> **PASS is not excellent. A craft-gate PASS clears the floor; CLIENT-READY requires the checklist.**

Finishing is the stage where a good selects pass becomes a deliverable a client would pay for and post without edits. We do not ship "a render came out." We ship the best available route, proven, with no convenience downgrade. See [[premium-stack-maximization-law]].

---

## 1. Two modes (route every job into one)

The headline tool in the ingested Chat Video Pro doc (Story Cutter) is **dialogue/transcript-only**. That is one mode, not the whole department. Every finishing job routes into exactly one of these:

### MODE A · DIALOGUE / TRANSCRIPT
Interview, podcast, vlog, testimonial, talking-head, UGC with a voice. The edit is driven by **spoken word**.
- **Selects engine:** transcript. Surface the best soundbites, group by category (hook / value / proof / CTA / emotional peak).
- **Tooling:** Chat Video Pro Story Cutter (operator-side, inside Premiere); silence-removal / auto-editor passes; `/select pass`, `/top 5 soundbites`, `/batch` for multi-deliverable.
- **Rough cut:** assembled from the transcript timeline.
- **Captions:** transcript-driven, burned or programmatic (Remotion-style overlay) for social.

### MODE B · VISUAL / NO-DIALOGUE
Fashion, swimwear, commercial, product, music-driven, deadpan. There is **no transcript**. The edit is driven by **frames**: action peaks, freezes, motivated cuts, beat-snap.
- **Selects engine:** `os_visual_selects_engine.py` — dense timestamp-burned filmstrips, watch every clip, mark action-peak + freeze + verdict per clip. The visual equivalent of Story Cutter: it watches frames instead of reading words.
- **Tooling:** the selects engine + EDL + the finishing stack (Premiere/AE/Adobe/ffmpeg) per the routing table below.
- **Rough cut:** assembled from the EDL.
- **Captions:** restrained, motivated, 1-2 beats max.

> **The mode is chosen FIRST. Wrong mode = wrong selects engine = wasted pass.** A dialogue tool cannot select a non-dialogue commercial, and a frame-watcher is the wrong tool for a 40-minute interview.

---

## 2. The pipeline (both modes share this spine)

```
SOURCE  ->  SELECTS  ->  ROUGH CUT  ->  FINISHING  ->  REVIEW
(never     (Mode A:     (EDL /        (grade,        (excellence
 edited     transcript;  transcript    plate/privacy,  gate +
 in place)  Mode B:      timeline)     hook, motion,   client-ready
            filmstrips)                audio, export)  checklist)
```

Validated by the Chat Video Pro doc's own "Source -> Selects -> Rough Cut" recommendation. Rules:
1. **Never edit the source timeline in place.** Selects go to a dedicated selects pass; the rough cut is built from selects.
2. **Brief the engine like a human editor:** what it is, who it's for, what they should feel, runtime, platform, type, hook, CTA. (Already embodied in STORY_PSYCHOLOGY_LAYER.)
3. **Selects-first automation:** let the engine surface every usable moment; the human makes the creative call. Director labels are truth until disproven by **timestamped visual evidence** — never sparse-sample and declare a moment missing.
4. **Status-tracking / resumability:** every pass writes its state (selects CSV, EDL, handoff package) so a later session resumes without re-deriving. No silent caps — if a pass bounds coverage, log what was dropped.

---

## 3. Finishing tool routing (per task, best tool first)

Finishing is not one tool. Route each PART to the best available route and PROVE any skip with an exact blocker (skip-ledger format below).

| Finishing task | Primary route | Fallback | Notes |
|---|---|---|---|
| Timeline / editorial | **Premiere** (premiere-pro MCP) | FCPXML handoff | `create_sequence_from_clips`, `add_to_timeline`, `set_clip_rotation` (270 for Canon) |
| Color grade / LUT | **Premiere `apply_lut` / `color_correct`** (re-test) → Adobe Lightroom/ACR | ffmpeg `lut3d` | brand LUT `ALMA_LOVE_signature_look_v1.cube`. apply_lut now exists in the premiere-pro MCP. |
| Rack-focus hook / motion gfx / logo sting | **After Effects** | ffmpeg per-frame animated blur | AE-MCP currently has no import/render tool; prove before falling back |
| Plate / privacy / tracked blur | **AE tracked mask** → **Premiere effect** (re-test) | ffmpeg `gblur`+`overlay` enable-window | required before publish; re-verify unreadable on a proof board |
| Cutouts / remove-bg / select-subject / product cleanup | **Adobe Cloud** (`image_remove_background`, `image_select_subject`) | — | proven via block-upload handshake; never local-mask when this is available |
| World backplate / set extension | **Higgsfield** (`nano_banana_2`, Seedream, Soul) | — | only where it truly elevates, not AI decoration |
| SFX / sound design / VO | **ElevenLabs** (`text_to_sound_effects` works) | synth bed (numpy) | `compose_music` is paid-gated; synth or licensed bed otherwise |
| Auto scene-detect selects | **Premiere `scene_edit_detection`** | filmstrip engine | new capability; useful first-pass cut points for long footage |
| Review board / client deck | **Figma** | contact-sheet montage | proof crops + scores, never "looks good" |
| Assembly / export spine | **Premiere `export_sequence` / `add_to_render_queue`** (re-test) | **ffmpeg** | ffmpeg only when Premiere export is blocked or it is objectively the right low-level renderer |
| Operator-side Premiere finishing (grade/VFX/B-roll) | **Chat Video Pro** (CEP panel) | — | human-in-the-loop, NOT MCP-drivable by Claude |

**Premiere MCP source:** `~/Adobe_Premiere_Pro_MCP` (hetpatel-11). Security-audited 2026-06-07: clean (no postinstall, stdio + local file bridge, `validateScript` denylist, no phone-home). This is the server behind the ~300 premiere-pro tools. Bridge fix: see [[premiere-mcp-bridge-fix]].

**Skip-ledger format (required whenever a premium tool is not used):**
`TOOL / WHY RELEVANT / STATUS / EXACT BLOCKER OR REASON NOT USED / NEXT FIX`

---

## 4. The finishing excellence gate

`os_finish_gate.py` scores a finished edit against 11 axes (0-3 each, >=2 to clear, 3 = excellent) plus a 7-item client-ready checklist (ALL must be YES).

**11 axes:** hook_clarity · story_arc · best_moment_usage · product_visibility · continuity · transition_motivation · premium_grade · audio_sync · plate_privacy_cleanup · rewatch_value · client_readiness.

**Client-ready checklist (all YES):** plate blur done (unreadable, proof board) · wrong people / BTS removed · product inserts don't break the world (real/clean, no AI anatomy) · hook reads within 1.5s · audio synced + legal (-14 LUFS) · final review board exists · revision/handoff package exists.

No "client-ready" claim without the checklist, regardless of a craft-gate PASS.

---

## 5. Engines (in `00_COMMAND_CENTER/scripts/`)

- **`os_visual_selects_engine.py`** — MODE B selects. `strips <dir> <out>` (dense filmstrips), `fine <clip> <a> <b> <out>` (pin the peak), `scaffold <dir> <csv>` (selects template; all MAYBE until watched).
- **`os_finish_plan.py`** — `handoff <edl.csv> <footage> <out>` emits CUT_LIST, ASSET_LIST, TIMESTAMP_MAP, handoff.fcpxml, AE_FINISHING_SPEC, REVISION_NOTES. Hands off to Premiere/AE/Chat-Video-Pro; never concludes "Premiere is useless."
- **`os_finish_gate.py`** — `score <video>` (facts + 11-axis scorecard + checklist), `checklist`, `axes`.

---

## 6. Hard rules (do not relax)

- No client delivery / posting / hosting / sending / invoicing / identity exposure without explicit operator approval.
- No synthetic model likeness without a signed AI-likeness release; if no release, identity-safe composite/world only.
- Plate/privacy blur required before any publish; re-verify unreadable.
- Do not alter originals. Stage exact files only (no `git add -A`).
- No paid-tool purchase without authorization.
- No em-dashes in any copy, ever.
- Maximize the premium stack: prove any skip with an exact blocker. Do not use ffmpeg as a convenience replacement for AE/Premiere finishing.
