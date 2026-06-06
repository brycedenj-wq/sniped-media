# OS REFERENCE INGESTION STANDARD , the Commercial Craft layer

> Why: "watch the best ads and get better" must become operating doctrine the OS uses automatically, not inspiration. A reference link/file becomes a structured teardown -> repeatable craft cards -> gates that measure our own edits/campaigns against the best. Internal study only; references are never re-posted.

Stack:
- `scripts/os_reference_ingest.py` , link/file -> reference package (frames, shot map, pacing, transcript/audio, teardown scaffold)
- `OS_COMMERCIAL_CRAFT_CARDS.json` + `scripts/os_commercial_card.py` , the repeatable craft moves (8-field cards)
- `OS_COMMERCIAL_CRAFT_LIBRARY.md` , rendered human-readable card library
- `scripts/os_reference_gate.py` , checks a built edit/campaign against the cards
- `REFERENCE_LIBRARY/<ref_id>/` , per-reference package ; `REFERENCE_LIBRARY_INDEX.md` , the index
- `REFERENCE_INGESTION_DASHBOARD.md` , state

## How a link becomes doctrine (the pipeline)
1. **Ingest:** `os_reference_ingest.py <url|file> [--id NAME] [--seconds N] [--res 360]`. Downloads via yt-dlp (uses `player_client=android,web_safari,tv` to bypass datacenter 403s), ffprobe for specs, ffmpeg scene-cut detection for the shot map, keyframes per shot, captions if present else audio.mp3 for STT, and a TEARDOWN.md scaffold with the computed metrics.
2. **Read (agent):** view `frames/`, read `transcript.txt` (or run ElevenLabs `speech_to_text` on `audio.mp3` if no captions), fill the TEARDOWN sections with SPECIFIC moves (hook, visual grammar, edit rhythm, copy/VO, sound, transitions, believability, do-not-copy).
3. **Card:** `os_commercial_card.py add ...` turns each move into a card: problem / when_to_use / principle / exact_move / timestamp_evidence / tool_route / gate_influenced / do_not_copy.
4. **Gate:** future edits run `os_reference_gate.py check <video> [--ref <ref_id>]` , it computes shots/ASL/pacing-contrast and prints the card-backed 9-point checklist.

## Tool reality (verified 2026-06-06)
- ffmpeg/ffprobe: present. yt-dlp: installed (2025.10.14). YouTube metadata: works. **Video stream 403s on the default web client; `--extractor-args youtube:player_client=android,web_safari,tv` bypasses it (proven: real 90s ingest, 13 shots).** ElevenLabs `speech_to_text`: available for the no-captions fallback.
- Limits (honest): the script does the DETERMINISTIC parts (download, shots, pacing, frames, audio). The QUALITATIVE read (seeing frames, hearing music, writing principles) is the agent's job. Motion-feel and music nuance are inferred, not perceived frame-perfect. **Ingest single spots, not compilations, for clean pacing** (a compilation's ASL mixes title cards + many ads).

## Rules
- Internal study only. Never re-post or redistribute a reference. Cards capture PRINCIPLES; every card has a `do_not_copy` field naming what is the reference's own (its exact staging, music, lockup, scene design).
- No vague notes. "Great energy" is rejected; "open on the spectacle, withhold the product until 0:08, product is the longest hold" is a card.
- Pair with `os_reference_gate` before any edit/campaign is called done.

## Routes wired (os_library)
COMMERCIAL_CRAFT_LIBRARY now loads for: video_campaign, film, ad, social_rollout, photo_post, still_range. Gate `os_reference_gate` feeds: elite_art_direction (hook/typo/variety), premiere/AE edit (pacing/transition), audio_stack_gate (audio_sync), figma_design (typography), max_readiness (pacing). 
