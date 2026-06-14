export const meta = {
  name: 'alma-her-film-edl',
  description: "Whole-watch Alma's real raw clips + build the frame-accurate 10/10 EDL from HER deadpan-summer brief",
  phases: [
    { title: 'Whole-watch real clips', detail: 'fresh agents whole-watch each must-use raw clip end to end' },
    { title: 'Build EDL', detail: 'synthesize the shot-by-shot 10/10 EDL from her brief + verified moments + AI-fill beats' },
  ],
}
const A = args || {}
const clips = A.clips || []
const briefDir = A.briefDir

const CLIP_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['clip','beat','best_in_out','what_happens','luxury_or_chaos','usable','notes'],
  properties: {
    clip: { type: 'string' },
    beat: { type: 'string', description: 'which brief beat this is (lens-wipe, speaker-gag, towel, trunk-reveal, poster, etc.)' },
    best_in_out: { type: 'string', description: 'the exact in/out seconds of the strongest moment' },
    what_happens: { type: 'string' },
    luxury_or_chaos: { type: 'string', enum: ['LUXURY','CHAOS','either'] },
    usable: { type: 'boolean' },
    notes: { type: 'string', description: 'plate/blur needs, other-person warnings, framing, sound cue' },
  },
}

phase('Whole-watch real clips')
const watched = await parallel(clips.map(c => () =>
  agent(
    `Whole-watch this real footage clip END TO END (do NOT sample, use the /watch skill: run  python3 "/Users/sniper/AI-Brain-Refinery/.claude/skills/watch/scripts/watch.py" "${c.path}"  then Read every frame it prints). This is raw footage for a deadpan-summer luxury swimwear commercial (mannequin-still model, the comedy is the situation, the swimsuit is the hero, "the suit survives the chaos"). The brief + the editor's logged must-use moment for this clip are in ${briefDir} (CREATIVE_BRIEF_FOR_EDITOR.md, MUST_USE_MOMENTS.md). Expected beat: ${c.expected}. Confirm or correct the exact in/out of the STRONGEST moment, describe what happens, classify it LUXURY (clean/held) or CHAOS (fast/aggressive/iphone), note any plate/license-plate that needs blur, any second person entering frame, and the framing. Em-dashes banned. Return ONLY the structured object.`,
    { label: `watch:${c.path.split('/').pop()}`, phase: 'Whole-watch real clips', schema: CLIP_SCHEMA, model: 'sonnet' }
  )
))
const valid = watched.filter(Boolean)

phase('Build EDL')
const packet = valid.map(v => `${v.clip} | beat=${v.beat} | ${v.best_in_out} | ${v.luxury_or_chaos} | usable=${v.usable} | ${v.what_happens} | ${v.notes}`).join('\n')
const edl = await agent(
  `You are the director/editor. Whole-read the client's brief in ${briefDir} (CREATIVE_BRIEF_FOR_EDITOR.md = her concept + her 0:00-0:45 beat structure + two-mode LUXURY/CHAOS cut; MUST_USE_MOMENTS.md; SUGGESTED_EDIT_ARCS.md). Below are fresh whole-watch confirmations of her REAL raw clips. Build the FRAME-ACCURATE 10/10 EDL for the 30-45s HERO cut that delivers HER vision exactly: deadpan awkward-luxury summer, mannequin-still model, the suit is the hero, clean->awkward->clean->awkward->clean rhythm (chaos cut fast 0.3-1s, beauty/product held 2-5s), her beat order (lens-wipe reveal -> low step-in -> speaker gag with the KICK -> handcuff/palm-up detail -> tug POV -> trunk back reveal -> giant towel struggle -> palm beauty -> bikini-top graphic -> car-interior quick cuts -> seated-poster freeze + Alma Love / DEADPAN SUMMER / LOUD SUIT STRANGE DAY lockup).\n\nCRITICAL: her brief lists beats she WANTED but could NOT shoot: dog, smoking/cigarette, gas station, handcuff detail, towel/leash tug-with-camera. We now AI-generate those to COMPLETE her vision. For EACH such beat, write an AI-FILL shot spec (photoreal, matched to her world: same model look, the cherry-print suit, retro Beverly Hills, deadpan, the level-up no-text + photographer-grade rules).\n\nOutput a markdown EDL: a numbered shot table (timecode in/out, source = REAL clip+in/out OR AI-FILL spec, LUXURY/CHAOS, action, why it earns its place, plate-blur/sound cue), then a SOUND plan (natural sound + upbeat 80s, lens-wipe SFX, speaker static->lock, metal clink), then the END CARD spec, then the AI-FILL shot list with full generation prompts. Be precise and production-ready. Em-dashes banned. Output the markdown only.\n\nREAL-CLIP CONFIRMATIONS:\n${packet}`,
  { label: 'build-edl', phase: 'Build EDL', model: 'opus' }
)
return { watchedCount: valid.length, edl }
