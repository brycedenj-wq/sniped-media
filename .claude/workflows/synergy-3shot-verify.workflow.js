export const meta = {
  name: 'synergy-3shot-verify',
  description: 'Adversarial verify for the Synergy 3-shot competence proof. Per shot, fresh-context skeptics whole-watch and refute on 4 axes (cinema-vs-animatic / identity+slop / performance-truth / client-safe), synthesize a per-shot verdict, then answer the competence question: are we competent to make Synergy as a real AI film now?',
  whenToUse: 'After generating the Synergy 3-shot proof, before crowning. Defends self-preferential bias: the orchestrator does not score its own shots.',
  phases: [
    { title: 'Refute', detail: '4 fresh skeptics per shot, whole-watch, one axis each' },
    { title: 'Per-shot verdict', detail: 'synthesize each shot' },
    { title: 'Competence verdict', detail: 'one overall call' }
  ]
}

const DIR = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/_3SHOT_PROOF/clips';
const LAWS = `STANDARD (REAL_FILM_PRODUCTION_OS): real cinema = the SUBJECT acts and the state CHANGES from start to end. An animatic still = only the camera moves (push-in/Ken-Burns) on a frozen subject = FAIL the Push-In Law. A slow push-in is allowed ONLY if it supports a real performance that is itself changing. These clips ARE AI-generated (Kling 3.0 i2v), so AI slop (face morph/melt, waxy skin, teeth/eye artifacts, melting/merging hands, identity drift) IS in scope and must be hunted. Brief: Synergy HomeCare, emotional brand film, anti-gloss documentary truth, client-safe, emotionally clear, NO corporate-healthcare sheen. Whole-watch: read EVERY frame in order, no sampling.`;

const SHOTS = [
  { id:1, name:'SHOT1 daughter 2am (scene-opening action)', file:`${DIR}/SHOT1_daughter_2am.mp4`, frames:`${DIR}/frames_SHOT1_daughter_2am`,
    intent:'At 2am the sleepless daughter lowers the glowing phone from her face, her eyes lift, she exhales, she decides not to call again. A decision must play on her face/hand. Real start->end change, not a push.',
    fails:'phone warps; eyes go uncanny/dead; no real decision reads; only the camera moves; any morph.' },
  { id:2, name:'SHOT2 Eleanor recognition (emotional performance / reaction)', file:`${DIR}/SHOT2_eleanor_recognition.mp4`, frames:`${DIR}/frames_SHOT2_eleanor_recognition`,
    intent:'An old song begins; Eleanor (~78) goes from blank/distant to recognition: eyes focus and glisten, lips part, the FAINTEST almost-smile, a few-degree turn toward the music. The hero beat, longest hold, restrained.',
    fails:'over-smiling/grin instead of a restrained almost-smile; stays blank (no recognition arc = animatic); identity drift; waxy skin; the slow push-in does ALL the work while the face stays frozen.' },
  { id:3, name:'SHOT3 together turn (transition / resolution)', file:`${DIR}/SHOT3_together_turn.mp4`, frames:`${DIR}/frames_SHOT3_together_turn`,
    intent:'Eleanor turns from the window to the caregiver, their eyes meet, the faintest warm almost-smile passes between them, the caregiver hand settles over hers. A real human connection forming between TWO consistent people.',
    fails:'either face swaps/morphs; the two people lose consistency or merge; the turn looks robotic; no connection change (just two stills sitting); melting/merging hands.' }
];

const AXES = [
  { key:'cinema',      lens:'CINEMA-vs-ANIMATIC. Apply the Push-In Law. Does the SUBJECT act and the state CHANGE start->end, or is this a frozen subject with only a camera push (Ken-Burns)? Name the start state and the end state from the frames.' },
  { key:'identity_slop', lens:'IDENTITY + AI SLOP. Is the person identity-stable across all frames? Hunt face morph/melt, waxy plastic skin, teeth/eye artifacts, melting/merging hands, warping objects. This is AI video, so slop is fair game.' },
  { key:'performance', lens:'PERFORMANCE TRUTH. Does the intended emotional change actually READ on the face/body (not just camera)? Is it restrained-and-real, absent (frozen), or overdone (fake grin)? The brief wants real, restrained, anti-gloss feeling.' },
  { key:'client_safe', lens:'CLIENT-SAFE + ON-BRIEF. Would Synergy/FMO accept this as emotionally clear, true, documentary, NOT corporate-healthcare gloss or AI flex? Any artifact or tonal miss that embarrasses on a client send?' }
];

const REFUTE = { type:'object', properties:{
  shot_id:{type:'number'}, axis:{type:'string'}, pass:{type:'boolean'},
  cinema_or_animatic:{type:'string'}, severity:{type:'string'},
  start_state:{type:'string'}, end_state:{type:'string'},
  evidence:{type:'array', items:{type:'string'}}, score_0_10:{type:'number'}, fix:{type:'string'}
}, required:['shot_id','axis','pass','evidence','score_0_10'] };

phase('Refute');
// pipeline: each shot fans out to 4 skeptics (stage1), then synthesizes a per-shot verdict (stage2). No barrier between shots.
const SHOT_VERDICT = { type:'object', properties:{
  shot_id:{type:'number'}, verdict:{type:'string'}, score_0_10:{type:'number'},
  is_cinema:{type:'boolean'}, blockers:{type:'array',items:{type:'string'}},
  what_works:{type:'array',items:{type:'string'}}, highest_leverage_fix:{type:'string'}
}, required:['shot_id','verdict','score_0_10','is_cinema'] };

const perShot = await pipeline(SHOTS,
  (s) => parallel(AXES.map(a => () => agent(
`You are a HOSTILE, fresh-context reviewer. REFUTE this shot on ONE axis. Default to pass=false unless the frames clearly clear it.
${LAWS}
SHOT: ${s.name}
INTENDED (what it must deliver): ${s.intent}
KNOWN FAIL MODES: ${s.fails}
AXIS: ${a.key} -> ${a.lens}
WHOLE-WATCH: read EVERY frame in ${s.frames} in order (fr_001.jpg upward; they are 4fps across the whole clip). You may also ffprobe/extract more from ${s.file} if needed. Do NOT sample.
Return JSON: pass, cinema_or_animatic ('cinema'|'animatic-still'|'still-with-push'|'n/a'), severity (blocker/major/minor/none), start_state, end_state, evidence[] (cite frame numbers), score_0_10, fix (single highest-leverage). Be specific, no politeness.`,
    { schema: REFUTE, label:`refute:s${s.id}:${a.key}`, phase:'Refute' }
  ).then(r => r ? { ...r, shot_id:s.id, axis:a.key } : null))),
  (votes, s) => agent(
`Synthesize the 4 adversarial verdicts for ${s.name} into ONE per-shot call.
INTENDED: ${s.intent}
VERDICTS JSON: ${JSON.stringify((votes||[]).filter(Boolean))}
Rules: is_cinema=false if cinema axis says animatic-still OR still-with-push with a frozen subject. Any identity/slop blocker caps the score low. verdict = one of: cinema-pass | borderline | animatic-fail | slop-fail. Give score_0_10, blockers[], what_works[], highest_leverage_fix.`,
    { schema: SHOT_VERDICT, label:`verdict:s${s.id}`, phase:'Per-shot verdict' }
  )
);

phase('Competence verdict');
const overall = await agent(
`You judge whether SNIPED is competent to make the Synergy film as a REAL AI film now (not stills panning). You did not make these shots.
${LAWS}
The 3-shot competence proof targeted the exact three beats The Door v2 FAILED (character performance done as frozen stills). Per-shot verdicts:
${JSON.stringify((perShot||[]).filter(Boolean))}
Answer honestly. Return JSON {
 competent (true/false),
 overall_call (one of: proceed-to-full-film | regenerate-specific-shots | revise-concept | stop-not-competent-yet),
 per_shot:[{shot_id, keep_or_regen, why}],
 method_fixes:[ what to change in the PRODUCTION METHOD before scaling (prompting, end-keyframes, model, push-in discipline) ],
 score_avg,
 one_line }.
Be strict: 'competent' means these read as real cinema with real performance and no slop, at a client-safe bar. A clean-but-too-subtle performance is 'regenerate-specific-shots', not 'proceed'. Frozen subject + push = not competent yet.`,
  { schema:{ type:'object', properties:{ competent:{type:'boolean'}, overall_call:{type:'string'}, per_shot:{type:'array',items:{type:'object'}}, method_fixes:{type:'array',items:{type:'string'}}, score_avg:{type:'number'}, one_line:{type:'string'} }, required:['competent','overall_call','one_line'] }, label:'competence-verdict' }
);

return { perShot:(perShot||[]).filter(Boolean), overall };
