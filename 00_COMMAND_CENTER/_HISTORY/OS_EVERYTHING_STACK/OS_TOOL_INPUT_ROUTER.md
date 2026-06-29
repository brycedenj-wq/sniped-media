# OS TOOL INPUT ROUTER , the input chooses the toolchain
> The OS does not ask "do we need this tool." It reads the INPUT and assembles the maximal chain for THAT input. Every tool is in the OS; the job decides which fire.

## Routing by input
- **"new world / hero"** -> Higgsfield Nano Banana (4K) -> os_adobe_grade -> os_postproduction_gate. (retouch handoff: Photoshop desktop, only for a hero going to a real sale)
- **"social variations / crops"** -> Adobe image_crop_and_resize (subject-aware) + os_adobe_reframe + os_adobe_layout(carousel/thumbnail).
- **"banner / wide / masthead space"** -> Adobe image_generative_expand. (proven: the DEED banner)
- **"cutout / product / drop mockup"** -> Adobe image_remove_background -> os_adobe_layout/composite. (3D drop -> Blender, WIRE_INSTALL)
- **"retouch / recolor a region"** -> Adobe image_select_by_prompt (TEST) ; deep retouch -> Photoshop desktop (HANDOFF).
- **"landing / web hero"** -> local HTML/CSS -> Chrome headless render (proven) ; rich interactive -> /web-artifacts-builder (HANDOFF) ; go-live -> Netlify/Vercel (WIRE, HELD).
- **"client deck / lookbook"** -> local Pillow PDF (proven) ; world-class typeset -> Adobe document_render InDesign (TEST, needs template).
- **"numbered edition / labels"** -> Adobe document_merge (INPUT_SPECIFIC) ; small batch -> Pillow numbering.
- **"motion shot"** -> Higgsfield Seedance -> os_adobe_cut -> os_motion_qa.
- **"trailer (multi-shot)"** -> 3-6 Seedance shots -> ffmpeg edit ; titling/sound -> After Effects (WIRE_INSTALL).
- **"social cutdown from a long clip"** -> Adobe video_create_quick_cut (TEST) ; manual -> ffmpeg.
- **"design system / app UI"** -> Figma (HANDOFF: open app+file) ; static -> os_adobe_layout.
- **"proof loop / lead tracking"** -> os_form_ingest/score (local) + Airtable (read proven; write input-specific) ; live form -> Netlify (HELD).
- **"reach a person"** -> Gmail draft (HANDOFF, you send) ; SMS -> Twilio (INPUT_SPECIFIC, app).
- **"market/SEO research"** -> Semrush (INPUT_SPECIFIC).
- **"3D object / virtual set"** -> Blender/Unreal (WIRE_INSTALL) ; pseudo-3D now -> Higgsfield-generated scene.
- **"automate across apps"** -> Zapier (WIRE via /mcp-builder) ; internal -> os_* scripts.

## Standing rule
Every output passes its gate (os_postproduction_gate / os_motion_qa / os_privacy_gate) and logs to EDIT_LOG/SPEND_LEDGER before it counts. No artifact, no credit.
