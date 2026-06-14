export const meta = {
  name: 'alma-4k-qa',
  description: 'Role-scoped whole-watch QA harness on the Alma Love 4K master, then adversarial verify',
  phases: [
    { title: 'Whole-watch QA', detail: 'fresh-context role agents each whole-watch + score one dimension' },
    { title: 'Adversarial verify', detail: 'hostile re-measure, break the crown, single highest-leverage fix' },
  ],
}

// args = { master, web, framesDir, docsDir, beats: [{clip, beat, role}] }
const A = args || {}
const master = A.master
const web = A.web
const framesDir = A.framesDir
const docsDir = A.docsDir
const brandDoc = A.brandDoc
const beatList = (A.beats || []).map(b => `${b.clip}=${b.beat}(${b.role})`).join(', ')

const ROLE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['dimension','score_0_10','gate_pass','blockers','strongest_evidence','notes'],
  properties: {
    dimension: { type: 'string' },
    score_0_10: { type: 'number' },
    gate_pass: { type: 'boolean' },
    blockers: { type: 'array', items: { type: 'object', additionalProperties: false,
      required: ['severity','where','issue','evidence'],
      properties: {
        severity: { type: 'string', enum: ['CRITICAL','HIGH','MEDIUM','LOW'] },
        where: { type: 'string', description: 'beat/clip id or timecode' },
        issue: { type: 'string' },
        evidence: { type: 'string', description: 'frame path or measured value backing the claim' },
      } } },
    strongest_evidence: { type: 'string' },
    notes: { type: 'string' },
  },
}

const VERDICT_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['final_verdict','ceiling_score','four_k_confirmed','audio_spec_pass','product_fidelity_pass','confirmed_blockers','overclaims_caught','single_highest_leverage_fix','rationale'],
  properties: {
    final_verdict: { type: 'string', enum: ['SEND','CONDITIONAL','NO_SEND'] },
    ceiling_score: { type: 'number' },
    four_k_confirmed: { type: 'boolean' },
    audio_spec_pass: { type: 'boolean' },
    product_fidelity_pass: { type: 'boolean' },
    confirmed_blockers: { type: 'array', items: { type: 'string' } },
    overclaims_caught: { type: 'array', items: { type: 'string' }, description: 'role-agent claims that did not survive re-measure' },
    single_highest_leverage_fix: { type: 'string' },
    rationale: { type: 'string' },
  },
}

const common = `
You are a fresh-context, hostile QA reviewer for a full-AI 16:9 fashion commercial for the swimwear brand ALMA LOVE CLUB (client: Kennedie). It must be a CLIENT-READY 4K master, not a test.
The deliverable 4K master: ${master}
A 1080 web preview: ${web}
Labeled per-beat frames (read these with the Read tool, they render visually): ${framesDir}
Product-truth garment docs to whole-read (in this dir): ${docsDir} (SWIMSUIT_PRODUCT_ATLAS.md, GARMENT_FIDELITY_RULES.md, SHOT_GARMENT_SOURCE_MAP.md, GARMENT_QA_GATE.md, MASTER_PLAN_16x9.md)
Brand identity doc to whole-read: ${brandDoc}
Beat map (clip = beat(grade-role)): ${beatList}
HARD PRODUCT RULE: the swimsuit must read as HER EXACT product, not a guess. Spec: ivory cherry-print string-triangle halter bikini; TRUE WARM RED print (anchor #B84A40, hue ~3-8deg), NOT coral (hue>18) and NOT pink (Blue>Green); ONE rhinestone cherry pair on the RIGHT cup only; EXACTLY 3 silver (not gold) engraved dice cubes per tie tail; frayed tips; cheeky bottom. A beautiful WRONG bikini is a failed commercial.
Two beats (clip c05 cherry, clip c11 dice) are NEW clean AI product-only macros (no person) that replaced earlier real-photo crops; judge whether they read as the real product and hold at 4K.
Inspect real frames before scoring. Quote frame paths or measured values as evidence. Do NOT rubber-stamp. Refuse to crown if a gate fails. Em-dashes are banned from your output; use commas/periods/colons.
Return ONLY the structured object.`

phase('Whole-watch QA')

const DIMENSIONS = [
  { key: 'garment-fidelity', task: `Dimension: GARMENT / PRODUCT FIDELITY. Whole-read SWIMSUIT_PRODUCT_ATLAS.md + GARMENT_FIDELITY_RULES.md + GARMENT_QA_GATE.md in the docs dir. Inspect EVERY beat frame. For each beat gate the garment: true-warm-red vs coral/pink (eyeball hue), cherry on the RIGHT cup only, silver (not gold) dice beads, print integrity, strap/tie physics. Score hardest on the two on-body day beats and on the two NEW product macros (c05/c11). gate_pass=false if any product-visible beat reads clearly wrong.` },
  { key: 'grade-unification', task: `Dimension: GRADE UNIFICATION + FINISH. Inspect all beats for ONE consistent grade (warm Kodak Americana), skin tone R>G>B where skin is present, no beat off-grade or off-temperature, grain + halation consistent, no banding/crush at 4K. Flag any beat that looks pasted from a different grade.` },
  { key: 'brand-world', task: `Dimension: BRAND / WORLD BIBLE. Whole-read the alma-love brand docs in the docs dir. Does ALMA LOVE CLUB feel EARNED? Is there a plural/CLUB beat? Is the wordmark + "TEXT LOVECLUB" CTA correct and legible at 4K? Is "LOVE IS A GAMBLE" card readable? Check the end card.` },
  { key: 'status-psychology', task: `Dimension: STATUS PSYCHOLOGY. Does the film sell belonging/desire and a coherent signal stack, or just a body? Is the symbol grammar (cards, dice, cherries, gamble) doing status work? Where does it read cheap vs expensive?` },
  { key: 'edit-pacing', task: `Dimension: EDIT / PACING vs the Margiela "Mutiny" reference (measured ASL ~1.6s, hard cuts on action, violent wide-to-tight scale alternation, earned 3-4.7s holds on tableaux, day-to-night arc). Measure this cut's rhythm from the beat map. Is the hook strong in the first 2s? Any beat that lingers or drags? Any dead transition?` },
  { key: 'distribution-spec', task: `Dimension: DISTRIBUTION / TECH SPEC. Use Bash. Confirm the master is true 3840x2160 (ffprobe). Measure audio integrated LUFS + true peak with: ffmpeg -i "${master}" -af loudnorm=print_format=json -f null - 2>&1 | tail -40  AND  ffmpeg -i "${master}" -af ebur128=peak=true -f null - 2>&1 | tail -20. PASS requires <= -1 dBTP true peak and roughly -14 to -16 LUFS. Report exact measured numbers as evidence. Also confirm faststart + 24fps.` },
]

const reviews = await parallel(DIMENSIONS.map(d => () =>
  agent(`${common}\n\n${d.task}`, { label: `review:${d.key}`, phase: 'Whole-watch QA', schema: ROLE_SCHEMA, model: 'sonnet' })
))
const valid = reviews.filter(Boolean)

phase('Adversarial verify')

const packet = valid.map(r => `### ${r.dimension} | score ${r.score_0_10}/10 | gate ${r.gate_pass ? 'PASS' : 'FAIL'}\nstrongest: ${r.strongest_evidence}\nblockers: ${JSON.stringify(r.blockers)}\nnotes: ${r.notes}`).join('\n\n')

const verdict = await agent(
  `${common}\n\nYou are the ADVERSARIAL VERIFIER and final synthesizer. Six role reviewers returned the findings below. Your job: try to BREAK the crown, do not inherit their conclusions. Re-open the master and the frames yourself. Re-measure the two riskiest claims (one product-fidelity claim and the audio/4K spec) with your own Bash + Read calls. Catch any role agent that over-claimed or under-claimed. Then deliver the final verdict for a PAYING CLIENT.\nRules: four_k_confirmed only if you personally ffprobe 3840x2160. audio_spec_pass only if you personally measure <= -1 dBTP. product_fidelity_pass only if no product-visible beat reads clearly wrong to your own eyes. SEND only if every hard gate passes; otherwise CONDITIONAL (sendable with named caveats) or NO_SEND. Give ONE highest-leverage fix. Do not output 10/10 unless the frames truly earn it.\n\nROLE FINDINGS:\n${packet}`,
  { label: 'adversarial-verify', phase: 'Adversarial verify', schema: VERDICT_SCHEMA, model: 'opus' }
)

return { reviews: valid, verdict }
