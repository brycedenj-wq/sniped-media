# Gridiron Royale · deploy record

- Play URL: https://joyful-falcon-423.higgsfield.gg/
- game_id (REQUIRED for in-place updates via deploy_game, never invent a new one): `6b78ec4d-cbe1-41fb-8506-bd79b3639931`
- v1 deployed 2026-06-12 (box-character build, 5.7 MiB zip)
- v2 deployed 2026-06-12 same day, IN PLACE (same game_id, same URL): rigged image-to-3D characters, dance emote, sky panorama, announcer VO x7 + crowd walla, status systems, OS-routed design laws. Zip 23.25 MiB (gate < 25 MiB).
- v2 source zip media_id: 8d2085ef-3b10-4782-b918-275a04fe6168
- Thumbnail/favicon: gpt_image_2 generations adc1c3b1 / cd07f806 (CDN URLs reused at v2 deploy)
- Update flow: edit public/, refresh public/design from design/, re-zip from public/ root, media_upload + PUT + media_confirm(type file), deploy_game with the same game_id.
- Live verification note: the public URL wraps the game in an iframe; the actual game document is the frame with `?__raw=1`. Headless CDP probes must target that frame (boot markers on documentElement.dataset.boot; selftest hooks via ?dev=1&selftest=1).
- Receipts: OS_RECEIPT.md (verdict sendable) + PROOF_MANIFEST.json (verify PASS) + design/ADVERSARIAL_VERIFY_V2.json + work/verify/ screenshots.
