export const meta = {
  name: 'synergy-shot2-reverify',
  description: 'Re-verify Synergy Shot 2 v2 (hero recognition, regenerated with END-keyframe method fix) against the v1 animatic-fail baseline. Fresh-context skeptics, endpoint-diff test first.',
  whenToUse: 'After the method-fix regen of the hero shot, before crowning the fix.',
  phases: [ { title: 'Refute', detail: '4 fresh skeptics whole-watch v2' }, { title: 'Verdict', detail: 'did the fix land?' } ]
}

const DIR = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/_3SHOT_PROOF/clips';
const FILE = `${DIR}/SHOT2_eleanor_recognition_v2.mp4`;
const FRAMES = `${DIR}/frames_SHOT2_v2`;
const BASE = `V1 BASELINE (this shot, prior take): adversarial verdict = animatic-fail, 3/10. The reason: fr_001 and fr_028 were emotionally identical (blank, distant, window-ward gaze, neutral mouth) and the ONLY change was the camera tightening = a still + push-in = Push-In Law fail. Identity + skin were clean; the failure was performance-absence. V2 was regenerated with an authored END keyframe (recognition bloomed) + performance-verb prompt + camera held, to FORCE a real arc.`;
const LAWS = `STANDARD: real cinema = the SUBJECT acts and the state CHANGES start->end. A frozen subject under a push-in = FAIL. ENDPOINT-DIFF TEST (run first): compare the FIRST frame to the LAST frame for subject delta in gaze, eyelid/eye-focus, mouth, head angle. If the only delta is framing/scale, it is still an animatic-fail. These are AI-generated (Kling 3.0 i2v) so hunt slop (morph/melt/waxy/teeth/eye/hand). Brief: restrained, real, anti-gloss documentary recognition of an old song; NO grin. Whole-watch every frame, no sampling.`;

const AXES = [
  { key:'endpoint_cinema', lens:'ENDPOINT-DIFF + Push-In Law. Name the first-frame state and last-frame state explicitly. Did the SUBJECT perform a change (turn/eyes/mouth), or did only the camera move? Is v2 cinema or still-an-animatic?' },
  { key:'performance', lens:'PERFORMANCE TRUTH. Does a recognition arc actually read on the face: eyes focus/well, lips part, faint single-corner almost-smile, small head turn? Restrained-real, absent, or overdone grin?' },
  { key:'identity_slop', lens:'IDENTITY + SLOP across all frames: morph/melt/waxy/teeth/eye/hand artifacts; identity drift. v1 was clean here, confirm v2 still is.' },
  { key:'client_safe', lens:'CLIENT-SAFE + ON-BRIEF: would Synergy/FMO accept this as a true, dignified, anti-gloss recognition beat with no AI tells?' }
];

const REFUTE = { type:'object', properties:{
  axis:{type:'string'}, pass:{type:'boolean'}, cinema_or_animatic:{type:'string'},
  first_frame_state:{type:'string'}, last_frame_state:{type:'string'},
  severity:{type:'string'}, evidence:{type:'array',items:{type:'string'}}, score_0_10:{type:'number'}, fix:{type:'string'}
}, required:['axis','pass','evidence','score_0_10'] };

phase('Refute');
const votes = (await parallel(AXES.map(a => () => agent(
`You are a HOSTILE, fresh-context reviewer. REFUTE on ONE axis. Default pass=false unless the frames clear it.
${LAWS}
${BASE}
SHOT: Eleanor recognition v2 (hero). FILE: ${FILE}
WHOLE-WATCH: read EVERY frame in ${FRAMES} in order (fr_001.jpg upward, 4fps across the 7s clip). Do not sample.
AXIS: ${a.key} -> ${a.lens}
Return JSON: pass, cinema_or_animatic ('cinema'|'animatic-still'|'still-with-push'|'n/a'), first_frame_state, last_frame_state, severity, evidence[] (cite frame numbers), score_0_10, fix.`,
  { schema: REFUTE, label:`reverify:${a.key}`, phase:'Refute' }
).then(r => r ? { ...r, axis:a.key } : null)))).filter(Boolean);

phase('Verdict');
const verdict = await agent(
`Did the END-keyframe method fix land on Shot 2 v2? You did not make it.
${BASE}
V2 VERDICTS: ${JSON.stringify(votes)}
Return JSON {
 fixed (true/false): is v2 now real cinema (subject-performed recognition arc, endpoint-diff passes) vs the v1 animatic-fail,
 verdict (cinema-pass|borderline|animatic-fail|slop-fail),
 score_0_10,
 delta_vs_v1,
 method_fix_works (true/false): does END-keyframe + performance-verbs reliably defeat the push-in default,
 remaining_fixes:[],
 one_line }.
Be strict: 'fixed' only if the first vs last frame show a real subject change AND a recognition arc reads, not just a bigger expression than a push.`,
  { schema:{ type:'object', properties:{ fixed:{type:'boolean'}, verdict:{type:'string'}, score_0_10:{type:'number'}, delta_vs_v1:{type:'string'}, method_fix_works:{type:'boolean'}, remaining_fixes:{type:'array',items:{type:'string'}}, one_line:{type:'string'} }, required:['fixed','verdict','score_0_10','method_fix_works','one_line'] }, label:'reverify-verdict' }
);

return { votes, verdict };
