# 15 FAILURES AND FIXES , live log

Honest log of what broke and how it was routed. No pretending.

## F1 , Premiere AME video render BLOCKED (bridge)
- Symptom: `export_sequence` returns `exported:true` but the mp4 never lands (even with AME 2026 launched + 90s poll). `add_to_render_queue` -> `Illegal Parameter type`. `export_frame` -> `exportFramePNG is not a function`. `create_bars_and_tone` / `create_sequence` -> param errors on 26.2.2.
- Fixes tried: re-export after launching AME; explicit render-queue add; frame export; bars-and-tone leader. All failed with logged errors.
- Route taken: PROVED Premiere at sequence-build + FCPXML interchange export (real artifacts on disk), documented AME render as BLOCKED, routed the actual film render to the proven ffmpeg/aerender hybrid. No local-shortcut-for-convenience (native route fully exercised first). See 06_EDIT/PREMIERE_EXPORT_PROOF.md.

## F2 , AE getLayerInfo needs active comp
- Symptom: `getLayerInfo` -> "No active composition" for a named comp.
- Fix: used project-level `listCompositions` for read-back instead. Authoring proof intact. See 05_MOTION/AE_AUTHORING_PROOF.md.
