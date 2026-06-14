export const meta = {
  name: 'synergy-bestof-verify',
  description: 'Final hostile verify of the Synergy BEST-OF proof set (daughter v1, Eleanor recognition v5, together v2) for the tomorrow partner review. Per shot: fresh-context skeptics whole-watch + endpoint-diff, score vs the deliverable bar. Answers: is the best-of proof deliverable (8+ overall, no slop/drift/gloss)?',
  whenToUse: 'Before assembling/sending the best-of proof. No self-crowning.',
  phases: [ { title: 'Refute', detail: '4 skeptics per shot' }, { title: 'Per-shot', detail: 'score each' }, { title: 'Deliverable verdict', detail: 'is the proof shippable to the partner' } ]
}
const DIR = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/_3SHOT_PROOF/clips';
const LAWS = `STANDARD (REAL_FILM_PRODUCTION_OS): real cinema = SUBJECT acts + state CHANGES start->end; a frozen subject under a push-in FAILS. ENDPOINT-DIFF first (name first vs last subject state). AI-generated (Kling i2v): hunt slop (morph/melt/waxy/teeth/eye/hand, identity drift, two-person consistency). Brief: Synergy HomeCare, restrained ANTI-GLOSS documentary truth, client-safe, emotionally clear, NO corporate-healthcare gloss, NO melodrama, NO tears required (frame-readable performance via eye/mouth/head/hand/breath). This is a DELIVERABLE proof for a partner/company review tomorrow: bar = 8+ overall, zero AI slop, zero identity drift, zero stock-healthcare sheen, clear emotional story. Whole-watch EVERY frame, no sampling. Score strictly.`;
const SHOTS = [
  { id:1, name:'SHOT1 daughter 2am (v1, prior best 8.0)', file:`${DIR}/SHOT1_daughter_2am.mp4`, frames:`${DIR}/frames_SHOT1_daughter_2am`,
    intent:'Sleepless adult daughter at 2am, phone glow, exhausted; a real internal beat reads in the eyes (decision/exhaustion->settle). Anti-gloss isolation. Re-confirm it holds at 8.' },
  { id:2, name:'SHOT2 Eleanor recognition (v5, NEW: blank profile -> turn -> warm almost-smile)', file:`${DIR}/SHOT2_eleanor_recognition_v5.mp4`, frames:`${DIR}/frames_SHOT2_eleanor_recognition_v5`,
    intent:'The hero. Full arc: blank distant profile -> turns toward the room as the song lands -> eyes lift/warm -> faint genuine almost-smile arrives and settles. Restrained, no tears, no grin. Prior versions failed for being too internal/back-loaded; this used start=blank-profile, end=frontal-warm-smile keyframe.' },
  { id:3, name:'SHOT3 together connection (v2, NEW: closer framing, continuity-locked caregiver)', file:`${DIR}/SHOT3_together_turn_v2.mp4`, frames:`${DIR}/frames_SHOT3_together_turn_v2`,
    intent:'Connection beat: elderly woman disconnected/heads-down -> turns to caregiver, mutual eye contact + faint smiles, caregiver hand settles over hers. Closer framing so faces read. Caregiver identity/wardrobe must stay consistent (prior wide v1 was 7.5; tan-vs-blue drift was fixed by deriving END from START).' }
];
const AXES = [
  { key:'endpoint_cinema', lens:'ENDPOINT-DIFF + Push-In Law. Name first vs last subject state. Did the SUBJECT perform the change or did the camera? Is the intended beat staged on camera?' },
  { key:'performance', lens:'PERFORMANCE TRUTH at the 8+ bar. Does the emotion read clearly + restrained-real (not absent, not melodrama)?' },
  { key:'identity_slop', lens:'IDENTITY + SLOP across all frames: morph/melt/waxy/teeth/eye/hand, identity drift, two-person consistency (shot 3 caregiver wardrobe/age must not change).' },
  { key:'client_safe', lens:'CLIENT-SAFE/ON-BRIEF: would a partner/company accept this as a serious proof? anti-gloss documentary, no AI tell, no stock-healthcare sheen.' }
];
const REFUTE = { type:'object', properties:{ shot_id:{type:'number'}, axis:{type:'string'}, pass:{type:'boolean'}, cinema_or_animatic:{type:'string'}, first_frame_state:{type:'string'}, last_frame_state:{type:'string'}, severity:{type:'string'}, evidence:{type:'array',items:{type:'string'}}, score_0_10:{type:'number'}, fix:{type:'string'} }, required:['shot_id','axis','pass','evidence','score_0_10'] };
const SHOT_VERDICT = { type:'object', properties:{ shot_id:{type:'number'}, score_0_10:{type:'number'}, is_cinema:{type:'boolean'}, meets_8:{type:'boolean'}, blockers:{type:'array',items:{type:'string'}}, what_works:{type:'array',items:{type:'string'}}, fix:{type:'string'} }, required:['shot_id','score_0_10','is_cinema','meets_8'] };

phase('Refute');
const perShot = await pipeline(SHOTS,
  (s) => parallel(AXES.map(a => () => agent(
`HOSTILE fresh-context reviewer at the 8+ deliverable bar. REFUTE this shot on ONE axis. Default pass=false.
${LAWS}
SHOT: ${s.name}
INTENDED: ${s.intent}
AXIS: ${a.key} -> ${a.lens}
WHOLE-WATCH every frame in ${s.frames} in order (fr_001.jpg up, 4fps). Do not sample.
Return JSON: pass, cinema_or_animatic, first_frame_state, last_frame_state, severity, evidence[] (cite frames), score_0_10 (strict), fix.`,
    { schema: REFUTE, label:`bo:s${s.id}:${a.key}`, phase:'Refute' }
  ).then(r => r ? { ...r, shot_id:s.id, axis:a.key } : null))),
  (votes, s) => agent(
`Synthesize the 4 verdicts for ${s.name} at the 8+ bar. INTENDED: ${s.intent}
VERDICTS: ${JSON.stringify((votes||[]).filter(Boolean))}
is_cinema=false if endpoint says still-with-push. meets_8 = score>=8.0. Give score_0_10 (strict; a blocker caps it), blockers[], what_works[], fix.`,
    { schema: SHOT_VERDICT, label:`bo:verdict:s${s.id}`, phase:'Per-shot' }
  )
);

phase('Deliverable verdict');
const overall = await agent(
`Decide if the Synergy BEST-OF 3-shot proof is DELIVERABLE for a partner/company review tomorrow. You did not make these.
Bar: 8+ overall, zero AI slop, zero identity drift, zero stock-healthcare gloss, clear emotional story across the 3 beats (daughter worry -> caregiver/recognition warmth -> connection).
Per-shot: ${JSON.stringify((perShot||[]).filter(Boolean))}
Return JSON { deliverable (true/false), overall_score, per_shot:[{shot_id,score,meets_bar}], story_reads (true/false), blockers:[], remaining_fixes:[], one_line, music_note:'owned music (Suno) not connected - proof is silent + needs a music handoff, scratch is not final' }.`,
  { schema:{ type:'object', properties:{ deliverable:{type:'boolean'}, overall_score:{type:'number'}, per_shot:{type:'array',items:{type:'object'}}, story_reads:{type:'boolean'}, blockers:{type:'array',items:{type:'string'}}, remaining_fixes:{type:'array',items:{type:'string'}}, one_line:{type:'string'}, music_note:{type:'string'} }, required:['deliverable','overall_score','one_line'] }, label:'deliverable-verdict' }
);
return { perShot:(perShot||[]).filter(Boolean), overall };
