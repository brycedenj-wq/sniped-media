---
name: platform-mastering
description: Turn one approved campaign hero into per-surface platform masters, and decide color vs B&W on evidence. Use AFTER /composite-master-qa passes, when exporting a hero for story/feed/square/deck/proof, when the user asks "which file for story vs feed", "is color failing or is it an export issue", "should this be black and white", "master this for platforms", or when a composite looks weak at small size. Enforces: never resize one flat master, re-compose per platform, clean/no-text default for posting, baked text only for drop cards/deck/ads, numeric skin-drift check, fail export on hue/temp shift, B&W is a prestige sidecar not the default. Subject grade stays LOCKED.
---

# Platform Mastering

A campaign hero is NOT finished when the composite passes QA. It is finished when the platform masters pass. Run this after `/composite-master-qa`. Full standard: `00_COMMAND_CENTER/_standards/PLATFORM_MASTERING.md` (read it first; it is canonical). Mirror copy travels in the project folder.

## Prime rule
Do not export one flat master and crop it everywhere. Re-compose or crop intentionally per platform. Each surface is a different viewing environment. The subject grade stays LOCKED; only output/export and (where rebuilt per aspect) the already-passed environment marriage change. Never re-grade skin.

## Steps
1. For each surface, produce its OWN crop / safe area / contrast / sharpening:
   - Story 9:16: face below top UI (~8%), feet above bottom UI (~12%), more vertical headroom, higher sharpening.
   - Feed 4:5: tighter full-body, distinct from story, mobile sharpening.
   - Square 1:1: full body with side environment.
   - Deck 16:9: cinematic, room for native type, light sharpening.
   - Proof: studio frame beside campaign, equal height.
2. Clean / no-text is the DEFAULT for posting. Baked text ONLY for drop cards, deck slides, intentional ad graphics.
3. When color confidence is in question, MEASURE skin drift numerically: interior body skin (alpha eroded ~25px, warm mask), source vs composite, mean RGB + delta.
   - Uniform delta on R/G/B (brightness only) = PASS.
   - Uneven / hue / temp shift = FAIL the export; reduce marriage strength on the subject, do not ship.
4. If color passes but feels weak, test platform sharpening + contrast BEFORE considering B&W. Do not hide a weak export in B&W.
5. B&W is an editorial / prestige sidecar, not the default drop asset, unless the brand concept specifically calls for B&W. When brand identity is built on color, color leads conversion.
6. Build side-by-side phone proofs (color vs B&W, platform set) so the operator judges on a phone.

## Output per hero
Clean masters (story/feed/square/deck + hi-res), one B&W sidecar, text versions only where allowed, phone proof sheets, the measured skin-drift line. Then update SESSION_STATE + commit the milestone.

## Locked precedent · Alma BH hero
Skin drift +2.8/+2.8/+2.9 RGB (uniform) -> color preserves identity, color leads; B&W is one prestige sidecar. Casual-to-client + posting use the clean color feed/story masters; deck uses the 16:9 color master with native type.


## INVOKE WHEN
- "master this for platforms" / "which file for story vs feed"
- After /composite-master-qa passes and surface exports are needed
- "is this a color issue or an export issue" / "should this be black and white"

## Inputs
- Approved campaign hero file that already passed /composite-master-qa (required)
- Target surfaces: any subset of story 9:16, feed 4:5, square 1:1, deck 16:9, proof (required)
- Brand color identity context (e.g. Alma coral-on-cream anchor) for B&W sidecar decision

## Gates
- Pre-condition: /composite-master-qa must pass before this skill runs; do not skip
- Re-compose gate: never resize one flat master and crop everywhere; each surface is its own re-composition
- Subject grade lock: never re-grade skin during platform mastering; grade stays LOCKED
- Skin drift gate: measure interior body skin (alpha eroded ~25px), mean RGB + delta; hue/temp shift = FAIL the export
- B&W gate: test sharpening + contrast before considering B&W; B&W is sidecar only; clean/no-text default for posting

## Test
- case: Operator approves Alma BH composite (post /composite-master-qa PASS) and requests story, feed, and deck masters. Expected: story 9:16 with face below top UI 8%, feed 4:5 tight full-body, deck 16:9 with room for native type, skin-drift line (e.g. +2.8/+2.8/+2.9 uniform PASS), one B&W sidecar, phone proof sheet, SESSION_STATE updated.
- expected failure: Invoked before /composite-master-qa has been run. Skill halts: 'Platform mastering requires /composite-master-qa to pass first. Run /composite-master-qa on this hero and re-invoke.'
