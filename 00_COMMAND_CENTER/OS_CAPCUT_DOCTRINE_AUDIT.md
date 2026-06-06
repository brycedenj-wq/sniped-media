# OS CapCut Doctrine Audit

Audited 2026-06-05. Question: can the OS automate CapCut, and if not, what is salvageable?

## Automation reality
| Check | Result |
| --- | --- |
| CapCut desktop app installed | NO (`/Applications/CapCut*` not present) |
| CapCut CLI | NONE (CapCut has no official CLI) |
| Draft-file lib (pyJianYingDraft) | NOT installed |
| CapCut draft dir | NONE (`~/Movies/CapCut*`, `~/Library/Application Support/CapCut` absent) |

Verdict: **CAPCUT_AUTOMATION_BLOCKED** , the app/CLI/draft-lib route does not exist on this machine. Do NOT route the AXIS edit through CapCut.

## Doctrine IS available (apply it inside the callable route)
The Start Here cards carry CapCut/short-form editing DOCTRINE even though the app is not callable. Status: CAPCUT_DOCS_AVAILABLE_BUT_AUTOMATION_BLOCKED. The 7 relevant cards:
- `social_social_media_3_0_m_the_3_part_hook_vi_0` , 3-Part Hook (Visual Stop + Context + Contrast).
- `copy_social_media_3_0_m_the_4_step_addicti_1` , 4-Step Addiction Loop (Stakes -> Big Question -> Head Fake -> Rehook).
- `brand_apple_signature_font_caption_system` , two-tier caption/font system.
- `brand_apple_signature_animation_sound_kit` , locked signature animation + sound kit.
- `higssfield_og_production-pipeline-tactics` , one-operator AI film pipeline (anchor + framing + editor-driven finish).
- `social_garyvee_gameplan_t_the_7x7_ai_repurpo_0` , 7x7 repurposing into platform-native cuts.
- `money_branding_x_clothes_pod_design_to_stor_2` , (POD pipeline; tangential, not edit doctrine).

## How it is used
The HYBRID route (HyperFrames + ffmpeg) executes the edit; the CapCut/short-form doctrine above DRIVES the creative decisions inside it: hook in the first 1-2s, caption styling, transition/pacing feel, the 6s/15s/30s + 9:16/16:9/1:1 deliverable set. CapCut the tool is blocked; CapCut the playbook is live.

## If CapCut automation is wanted later
Install CapCut + `pyJianYingDraft` (community draft-JSON lib) and add a CAPCUT_AUTOMATED route to os_video_edit_router.py. Low priority: the HYBRID route already delivers end-to-end.
