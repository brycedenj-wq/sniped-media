# FAILURES AND FIXES , MAX_PRODUCTION_PROOF_001
No fake-completion. Everything that broke, and how it was handled.

1. MOTION beat A flagged `nsfw` (FALSE POSITIVE). seedance safety classifier flagged a clothed man in a concrete room. Cost was still charged (~22cr, wasted). FIX: re-prompted (emphasized "fully-clothed man", "no people besides the distant figure", architectural framing) -> passed clean. LESSON: solo-figure i2v can trip the classifier; keep a re-prompt template ready; budget one reroll.
2. POSTER masthead overflow. "THE HOUSE REMEMBERS" clipped both edges (os_adobe_layout poster has no width-fit). FIX: single-word masthead "AXIS" (also stronger editorial register); film title moved to logline. Result: clean, premium.
3. MOTION QA / WORLD gates take a SLUG not a path. Invocation fix.
4. FACEMATCH --out must be an image extension (.png). Invocation fix.
5. POST-PRODUCTION gate reads run_dir/10_logs/EDIT_LOG.csv. Grade+exports were logged elsewhere -> grade_applied FAIL + log WARN. FIX: wrote canonical run-dir EDIT_LOG with the real grade/export/motion ops -> gate SHIP.
6. cand_03 still: off-center without reason -> CUT by vision gate (kept as CUT_hero_cand_03.png).
7. ffmpeg build lacks libwebp encode -> used jpg/png previews. No impact.

All fixes were invocation/logging or creative re-direction. No script code changed except the registry/route work in prior commits.
