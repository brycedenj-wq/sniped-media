export const meta = {
  name: 'adversarial-verify',
  description: 'The standing Verify phase: N parallel fresh-context skeptics each try to BREAK a result on one axis, then synthesize a verdict. Rebuilds the Gemini hostile lane as a workflow. Run on any serious artifact before crowning it.',
  whenToUse: 'Before calling any production artifact done/final/client-ready. Pass the artifact path(s) + the claim being made. Each skeptic is scoped to one failure axis and defaults to REFUTE.',
  phases: [
    { title: 'Refute', detail: 'parallel fresh-context skeptics, one per axis' },
    { title: 'Synthesize', detail: 'merge into one verdict' }
  ]
}

// args: { target: "<path or description of the artifact>", claim: "<what is being claimed>", axes: [..optional..] }
const target = (args && args.target) || ''
const claim = (args && args.claim) || 'this artifact is client-ready / final'
const AXES = (args && args.axes) || [
  { key:'identity', lens:'identity/likeness drift across shots or frames (os-face-lock); is it the same subject everywhere, any morph/melt' },
  { key:'grade',    lens:'grade/exposure/skin-tone consistency + composite physics (composite-master-qa, platform-mastering); any shot that jumps, any floating cutout, skin drift' },
  { key:'craft',    lens:'edit craft (Commercial Craft V2): is the hero the longest hold, are cuts motivated, does it read MUTED, is it a stitched-clip feel, pacing contrast' },
  { key:'truth',    lens:'claim-truth: does the artifact actually deliver what the claim says; what is missing, unverified, or overstated; would a hostile client reject it' },
  { key:'slop',     lens:'AI/uncanny + brand-tone (os-vision-reject-gate): hands, skin plasticity, physics, off-brand expression, thirst-vs-expensive tone' }
]

const VERDICT = { type:'object', properties:{
  axis:{type:'string'}, refuted:{type:'boolean'}, severity:{type:'string'},
  evidence:{type:'array', items:{type:'string'}}, fix:{type:'string'}
}, required:['axis','refuted','evidence'] }

phase('Refute')
const votes = (await parallel(AXES.map(a => () => agent(
  `You are a HOSTILE, fresh-context reviewer. Your ONLY job is to REFUTE this claim on ONE axis. Default to refuted=true unless the evidence clearly clears it.
CLAIM: ${claim}
ARTIFACT: ${target}
AXIS: ${a.key} -> ${a.lens}
Inspect the artifact directly (Read frames/files, run ffprobe/ffmpeg to extract and view frames if it is a video, whole-watch do not sample). Cite concrete evidence (timestamps, frame observations, file facts). Then return JSON: refuted (true/false), severity (blocker/major/minor/none), evidence[], fix (the single highest-leverage fix). Be specific, no politeness.`,
  { schema: VERDICT, label: `refute:${a.key}` }
)))).filter(Boolean)

phase('Synthesize')
const syn = await agent(
  `Synthesize these adversarial verdicts into ONE honest call. Verdicts JSON:
${JSON.stringify(votes)}
Rules: ANY blocker on a never-relax axis (identity, slop hard-fail, legal) => verdict=blocked. Count refutes. Give: overall (clear|conditional|blocked), the blockers, the ranked fix list, and an honest score /10 with what blocks 10. Return JSON {overall, blockers:[], fixes:[], score, blocks_10}.`,
  { schema:{ type:'object', properties:{ overall:{type:'string'}, blockers:{type:'array',items:{type:'string'}}, fixes:{type:'array',items:{type:'string'}}, score:{type:'number'}, blocks_10:{type:'string'} }, required:['overall','score'] }, label:'synthesize' }
)
return syn
