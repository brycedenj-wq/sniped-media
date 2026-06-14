export const meta = {
  name: 'synergy-3shot-verify-v3',
  description: 'Hostile verify of the Synergy 3-shot EXCELLENCE polish pass (v3). Per shot, fresh-context skeptics whole-watch + endpoint-diff, score against the 9-floor. Pass condition: all 3 >= 8.5 AND hero (shot 2) >= 9. Answers: full-film greenlight or still blocked.',
  whenToUse: 'After the v3 excellence polish, before greenlighting the full film. No self-crowning.',
  phases: [ { title: 'Refute', detail: '4 skeptics per shot, whole-watch + endpoint-diff' }, { title: 'Per-shot verdict', detail: 'score each vs 9-floor' }, { title: 'Greenlight verdict', detail: 'pass condition check' } ]
}

const DIR = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/_3SHOT_PROOF/clips';
const LAWS = `STANDARD (REAL_FILM_PRODUCTION_OS): real cinema = SUBJECT acts and state CHANGES start->end. Frozen subject under a push-in = FAIL the Push-In Law. ENDPOINT-DIFF TEST FIRST: name first-frame vs last-frame subject state (gaze/eyelid/mouth/head/hands); if the only delta is framing/scale (a push/zoom), it FAILS regardless of how nice it looks. AI-generated (Kling 3.0 i2v) so hunt slop (morph/melt/waxy/teeth/eye/hand, identity drift). Brief: Synergy HomeCare, restrained anti-gloss documentary truth, client-safe, emotionally clear, NO corporate-healthcare gloss, NO melodrama. Whole-watch EVERY frame in order, no sampling. This is an EXCELLENCE pass: the 9/10 floor is the bar, not cinema-pass. Score strictly: 9 = a real client could air it and feel it; 8 = strong but one nit; 7 = competent but the beat is soft or push-carried.`;

const SHOTS = [
  { id:1, name:'SHOT1 daughter 2am v3 (scene-opening action)', file:`${DIR}/SHOT1_daughter_2am_v3.mp4`, frames:`${DIR}/frames_SHOT1_daughter_2am_v3`,
    intent:'POLISH TARGET: a legible internal DECISION, not just "awake with phone." She almost calls (thumb hovers over the glowing screen), stops herself, lowers the phone, closes her eyes, exhales, accepts she needs help. The decision must read as an action on hand+face. v1 was 8.0 but read as fatigue not decision.' },
  { id:2, name:'SHOT2 Eleanor recognition v3 (HERO)', file:`${DIR}/SHOT2_eleanor_recognition_v3.mp4`, frames:`${DIR}/frames_SHOT2_eleanor_recognition_v3`,
    intent:'POLISH TARGET (must hit 9): blank/listening -> recognition -> eyes present and welling -> faint single-corner almost-smile/softened mouth -> head turns a few degrees to the music -> HOLD the recognized peak ~2s. Restrained, dignified, no grin, no melodrama. v2 was 7.5; this v3 used a stronger peak END keyframe + 8s to hold.' },
  { id:3, name:'SHOT3 together turn v3 (transition/resolution)', file:`${DIR}/SHOT3_together_turn_v3.mp4`, frames:`${DIR}/frames_SHOT3_together_turn_v3`,
    intent:'POLISH TARGET: a genuine RELATIONSHIP beat. Eleanor starts looking out the window, then TURNS to the caregiver, eye contact lands, faint almost-smile, the caregiver hand settles over hers, the room feels safe. Must be subject-performed connection, NOT a slow push-in on a two-shot. v1 skipped the turn (faced caregiver from frame 1).' }
];

const AXES = [
  { key:'endpoint_cinema', lens:'ENDPOINT-DIFF + Push-In Law. Name first-frame vs last-frame subject state. Did the SUBJECT perform the intended change, or did the camera (push/zoom) do the work? Is the named polish action actually staged on camera?' },
  { key:'performance', lens:'PERFORMANCE TRUTH at the 9 bar. Does the intended emotional/decision arc read clearly and land, restrained-real (not absent, not overdone)? Is the peak held long enough to feel?' },
  { key:'identity_slop', lens:'IDENTITY + SLOP across all frames: morph/melt/waxy/teeth/eye/hand artifacts, identity drift, two-person consistency (shot 3).' },
  { key:'client_safe', lens:'CLIENT-SAFE at the 9 bar: would Synergy/FMO air this and FEEL it? Anti-gloss documentary truth, no corporate sheen, no AI tell, no melodrama.' }
];

const REFUTE = { type:'object', properties:{
  shot_id:{type:'number'}, axis:{type:'string'}, pass:{type:'boolean'},
  cinema_or_animatic:{type:'string'}, first_frame_state:{type:'string'}, last_frame_state:{type:'string'},
  severity:{type:'string'}, evidence:{type:'array',items:{type:'string'}}, score_0_10:{type:'number'}, fix:{type:'string'}
}, required:['shot_id','axis','pass','evidence','score_0_10'] };

const SHOT_VERDICT = { type:'object', properties:{
  shot_id:{type:'number'}, verdict:{type:'string'}, score_0_10:{type:'number'},
  is_cinema:{type:'boolean'}, meets_85:{type:'boolean'}, blockers:{type:'array',items:{type:'string'}},
  what_works:{type:'array',items:{type:'string'}}, highest_leverage_fix:{type:'string'} }, required:['shot_id','score_0_10','is_cinema','meets_85'] };

phase('Refute');
const perShot = await pipeline(SHOTS,
  (s) => parallel(AXES.map(a => () => agent(
`You are a HOSTILE, fresh-context reviewer at the 9/10 EXCELLENCE bar. REFUTE this shot on ONE axis. Default pass=false.
${LAWS}
SHOT: ${s.name}
INTENDED: ${s.intent}
AXIS: ${a.key} -> ${a.lens}
WHOLE-WATCH: read EVERY frame in ${s.frames} in order (fr_001.jpg up, 4fps). Do not sample.
Return JSON: pass, cinema_or_animatic, first_frame_state, last_frame_state, severity, evidence[] (cite frames), score_0_10 (strict), fix.`,
    { schema: REFUTE, label:`v3:s${s.id}:${a.key}`, phase:'Refute' }
  ).then(r => r ? { ...r, shot_id:s.id, axis:a.key } : null))),
  (votes, s) => agent(
`Synthesize the 4 verdicts for ${s.name} at the 9-floor bar.
INTENDED: ${s.intent}
VERDICTS: ${JSON.stringify((votes||[]).filter(Boolean))}
is_cinema=false if endpoint_cinema says still-with-push/animatic. meets_85 = score>=8.5. Give verdict (excellent-9|strong-85|cinema-pass|borderline|fail), score_0_10 (strict, average-aware but a blocker caps it), blockers[], what_works[], highest_leverage_fix.`,
    { schema: SHOT_VERDICT, label:`v3:verdict:s${s.id}`, phase:'Per-shot verdict' }
  )
);

phase('Greenlight verdict');
const overall = await agent(
`Decide the full-film greenlight for Synergy. You did not make these shots.
PASS CONDITION (operator-set): ALL three shots >= 8.5 AND the hero (shot 2) >= 9. If the hero does not hit 9, DO NOT greenlight.
Per-shot v3 verdicts: ${JSON.stringify((perShot||[]).filter(Boolean))}
Return JSON {
 pass_condition_met (true/false),
 greenlight (full-film-greenlight | still-blocked),
 hero_hits_9 (true/false),
 per_shot:[{shot_id, score, meets_bar, keep_or_regen, why}],
 blockers:[],
 remaining_fixes:[],
 avg_score,
 one_line }.
Be strict and literal about the pass condition.`,
  { schema:{ type:'object', properties:{ pass_condition_met:{type:'boolean'}, greenlight:{type:'string'}, hero_hits_9:{type:'boolean'}, per_shot:{type:'array',items:{type:'object'}}, blockers:{type:'array',items:{type:'string'}}, remaining_fixes:{type:'array',items:{type:'string'}}, avg_score:{type:'number'}, one_line:{type:'string'} }, required:['pass_condition_met','greenlight','hero_hits_9','one_line'] }, label:'greenlight-verdict' }
);

return { perShot:(perShot||[]).filter(Boolean), overall };
