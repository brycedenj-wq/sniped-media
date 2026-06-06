# VOICE SCRIPT , SOVRA/SOLE manifesto (ElevenLabs V3 tagged)

> Register: The Verdict. Low, dry, measured. A judge reading a finding, not a trailer voice. Pauses are load-bearing. One voice across all tiers. Export stems DRY.
> v3 status: `eleven_v3` is callable via the MCP and accepts inline tags. Tag audibility must be ear-verified on the calibration render; if a tag does not fire, use the v2-safe block with high Stability + punctuation.

## A. V3 TAGGED BLOCK (render on eleven_v3)
```
[measured] Every market begins the same way. Many names. One template. [pause] The same three adjectives. The same borrowed light.

[slightly lower] Then the work got good. [pause] All of it.
Good is now free. Good is now infinite. And good [emphasis] can no longer tell anyone apart.

[cold, deliberate] So we stopped trying to make you better.
[pause] Better is a category. We took you out of it.

[rising, certain] Meridian and Hale is no longer a firm that litigates construction disputes.
It is the only firm that tries a dispute the way the building was engineered. [pause] A structure. Not a story.

[quiet] One claim. One world built to hold it. One mark, struck once.

[whispers] The only one.

[measured] Seventy-two hours. One house at a time. A verdict you will repeat for years.

[final, low] We do not make you better. [pause] We make you the only one.
```

## B. V2-SAFE BLOCK (fallback: eleven_multilingual_v2, Stability 0.7, Style 0.15)
Same words, tags removed, pacing carried by punctuation and line breaks:
```
Every market begins the same way. Many names. One template. The same three adjectives, the same borrowed light.
Then the work got good. All of it. Good is now free. Good is now infinite. And good can no longer tell anyone apart.
So we stopped trying to make you better. Better is a category. We took you out of it.
Meridian and Hale is no longer a firm that litigates construction disputes. It is the only firm that tries a dispute the way the building was engineered. A structure. Not a story.
One claim. One world built to hold it. One mark, struck once.
The only one.
Seventy-two hours. One house at a time. A verdict you will repeat for years.
We do not make you better. We make you the only one.
```

## Voice + render notes
- Pin ONE Verdict voice ID before the final render (this pass uses a resonant premade for the calibration; lock the chosen ID into the registry so every tier renders identical , audio-drift discipline).
- Render beats "the turn" and "the only one" in multiple takes; select by ear.
- Word count ~150 -> ~85-92s at this measured pace. Trim line 1 or the offer line if the cut runs long.
- Stems DRY (no baked reverb); reverb is placed in the mix to seat the voice in the Vault Room.
