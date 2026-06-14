export const meta = {
  name: 'alma-ai-edl',
  description: "Build the 100% AI 10/10 EDL for Alma's deadpan-summer swimwear film from HER brief",
  phases: [
    { title: 'Design panel', detail: 'three lenses each draft the all-AI EDL from her brief' },
    { title: 'Synthesize EDL', detail: 'merge into the production-ready all-AI shot list with generation prompts' },
  ],
}
const A = args || {}
const briefDir = A.briefDir
const playbook = A.playbook

const common = `This is a HIGH-STAKES client save: a paying swimwear client (Alma Love) rejected the human editor's real-footage cut; this is a 100% AI production that must hit HER vision or it is a refund + reputation hit. Do NOT use any real footage; every shot is AI-generated. Whole-read her brief in ${briefDir} (CREATIVE_BRIEF_FOR_EDITOR.md = her concept + her 0:00-0:45 beat structure + two-mode LUXURY/CHAOS; SWIMWEAR CAMPAIGN EDIT DOCUMENT if present; MUST_USE_MOMENTS.md and SUGGESTED_EDIT_ARCS.md for the intended beats). Whole-read the photoreal craft rules in ${playbook}.
HER VISION (do not drift): "Awkward Luxury / Deadpan Summer". A mannequin-still, almost robotic swimwear model has a strangely difficult day with luxury objects (Mercedes convertible, palm streets, a rolling speaker, a giant striped towel, sunglasses, lipstick, heat). The COMEDY IS THE SITUATION, never her face; she stays serious, composed, robotic; "the suit survives the chaos"; the cherry-print swimsuit is always the clean readable hero. Two modes cut against each other: LUXURY (clean, beautiful skin, suit readable, longer 2-5s holds, composed) vs CHAOS (iPhone 0.5x wide, low aggressive angles, lens wipe, fast 0.3-1s inserts, paparazzi). Rhythm: clean -> awkward -> clean -> awkward -> clean.
HER BEAT ORDER (30-45s): lens-wipe reveal -> low aggressive step-in -> speaker gag (fidget + the KICK + walk-off) -> handcuff/palm-up glossy detail -> tug/pull POV -> trunk back swimsuit reveal (product hero) -> giant towel struggle -> palm beauty breath -> bikini-top graphic -> car-interior quick cuts (lipstick gloss, recline) -> seated-poster FREEZE + "Alma Love / DEADPAN SUMMER / LOUD SUIT. STRANGE DAY." lockup.
AI NOW DELIVERS THE BEATS SHE WANTED BUT COULDN'T SHOOT: dog, smoking/cigarette, gas station, the handcuff detail. Weave them in as CHAOS inserts.
CRAFT (from the playbook): win the still first; hard-negative ALL text/signage/logos (kill the AI tell); prompt like a photographer (named lens + aperture, practical light only, 35mm film grain + halation, real imperfection); never head-on (3/4 angles); the model is the SAME synthetic lead + the SAME cherry-print coral-on-cream suit in every shot; deadpan, no mugging. Em-dashes banned.`

phase('Design panel')
const LENSES = [
  { key: 'vision-fidelity', task: 'LENS 1, HER-VISION FIDELITY. Draft the full all-AI EDL that is maximally faithful to her exact brief: her beat order, the deadpan mannequin performance, the two-mode clean/chaos rhythm, the suit-as-hero, the awkward-luxury comedy. Make sure every beat she named is present and reads as SHE described it.' },
  { key: 'comedy-in-ai', task: 'LENS 2, EXECUTING THE COMEDY IN AI. Draft the EDL focused on HOW to make the gags actually work as AI motion: the lens-wipe reveal (blur->hand wipes lens->sharp suit), the speaker drag + KICK + walk-off, the giant towel streaming across frame, the palm-up handcuff detail, the dog/smoking/gas-station chaos inserts. For each, specify the START keyframe and the Seedance motion prompt (the action verb + camera) so the deadpan comedy lands, not a static pretty shot.' },
  { key: 'cinema-craft', task: 'LENS 3, CINEMA CRAFT + FINISH. Draft the EDL focused on indistinguishable-from-real look + the two-mode visual grammar (LUXURY = clean Canon-style 35-50mm composed; CHAOS = iPhone 0.5x fisheye-ish low handheld), the kill-AI-tells rules per shot, the sound design (natural sound + upbeat 80s, lens-wipe SFX, speaker static->lock, metal clink), the grade, and the cream-script end-card lockup.' },
]
const drafts = await parallel(LENSES.map(l => () =>
  agent(`${common}\n\n${l.task}\n\nReturn a markdown EDL draft: numbered shots with timecode in/out, LUXURY/CHAOS, the action, the START-keyframe generation prompt, the Seedance motion prompt, and why it earns its place.`,
    { label: `draft:${l.key}`, phase: 'Design panel', model: 'sonnet' })
))
const valid = drafts.filter(Boolean)

phase('Synthesize EDL')
const edl = await agent(
  `${common}\n\nThree design drafts are below. Synthesize the SINGLE production-ready 100% AI 10/10 EDL. Output strict markdown:\n1) LOGLINE + the deadpan-summer intent in 2 lines.\n2) SHOT TABLE: # | tc in-out | LUXURY/CHAOS | beat | action | START-KEYFRAME PROMPT (full, photographer-grade, no-text, the cherry-print suit + the lead) | SEEDANCE MOTION PROMPT (action + camera, anti-drift) | why it earns its place. Cover her full beat order + the dog/smoking/gas-station AI-fill inserts. Keep the rhythm clean->awkward->clean, chaos cut fast, product/beauty held.\n3) SOUND PLAN. 4) END CARD spec (cream script Alma Love / DEADPAN SUMMER / LOUD SUIT. STRANGE DAY.). 5) A flat ordered list of every KEYFRAME to generate first (so production can batch them).\nThis is the blueprint a producer will execute beat by beat. Be precise, complete, production-ready. Em-dashes banned. Output the markdown only.\n\nDRAFTS:\n${valid.map((d,i)=>`===== DRAFT ${i+1} =====\n${d}`).join('\n\n')}`,
  { label: 'synthesize-edl', phase: 'Synthesize EDL', model: 'opus' }
)
return { drafts: valid.length, edl }
