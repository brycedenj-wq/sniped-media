export const meta = {
  name: 'synergy-hero-v4-reverify',
  description: 'Re-verify the Synergy hero shot v4 (recognition, corrected: welling END keyframe + 5s + early-recognition prompt) against the v3 (7.3, back-loaded, no welling) baseline. Must hit the 9 floor. Fresh-context skeptics, endpoint-diff + welling check.',
  whenToUse: 'After the corrected hero re-roll, before any greenlight. No self-crowning.',
  phases: [ { title: 'Refute', detail: '4 skeptics whole-watch v4' }, { title: 'Verdict', detail: 'does it hit 9?' } ]
}
const DIR = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/_3SHOT_PROOF/clips';
const FILE = `${DIR}/SHOT2_eleanor_recognition_v4.mp4`;
const FRAMES = `${DIR}/frames_SHOT2_v4`;
const BASE = `BASELINE v3 (this hero, prior take): 7.3, borderline. Failures the v4 set out to fix: (1) BACK-LOADED arc - recognition didn't start until ~75% through, the push-in carried most of it; (2) EYE-WELLING ABSENT in every frame; (3) held peak only ~1.2s. v4 fix: a tighter END keyframe with VISIBLE welling (wet lower lids + catch-light), a SHORTER 5s clip so it cannot back-load, and a prompt to begin recognition immediately and hold the welled peak ~2s.`;
const LAWS = `STANDARD: real cinema = SUBJECT performs the change, not the camera. ENDPOINT-DIFF first: name first vs last frame subject state. This is the HERO and must hit the 9 FLOOR: a real, restrained, felt recognition arc (blank->present->welling->faint almost-smile, head turn) that a client could air and be moved by. AI-generated (Kling i2v): hunt slop (morph/melt/waxy/teeth/eye/hand, identity drift, de-aging creep). Anti-gloss documentary, no grin, no melodrama. Whole-watch every frame in order, no sampling. Score strictly: 9 = airs and moves a viewer; <9 = name exactly what is missing.`;
const AXES = [
  { key:'arc_timing', lens:'ARC TIMING + Push-In Law. When does recognition START (which frame) and does it build across the shot, or is it still back-loaded/push-carried? Name first vs last frame state.' },
  { key:'welling_peak', lens:'WELLING + HELD PEAK. Is there visible eye-welling/glassiness/catch-light (the v3 miss)? Does the moved peak HOLD ~2s at the end?' },
  { key:'identity_slop', lens:'IDENTITY + SLOP across all frames: morph/melt/waxy/teeth/eye/hand, identity drift, de-aging creep.' },
  { key:'client_safe', lens:'CLIENT-SAFE at the 9 bar: would Synergy/FMO air this and FEEL it? restrained, dignified, anti-gloss, no AI tell, no melodrama.' }
];
const REFUTE = { type:'object', properties:{ axis:{type:'string'}, pass:{type:'boolean'}, recognition_start_frame:{type:'string'}, welling_present:{type:'boolean'}, first_frame_state:{type:'string'}, last_frame_state:{type:'string'}, severity:{type:'string'}, evidence:{type:'array',items:{type:'string'}}, score_0_10:{type:'number'}, fix:{type:'string'} }, required:['axis','pass','evidence','score_0_10'] };

phase('Refute');
const votes = (await parallel(AXES.map(a => () => agent(
`You are a HOSTILE, fresh-context reviewer at the 9/10 HERO bar. REFUTE on ONE axis. Default pass=false.
${LAWS}
${BASE}
SHOT: Eleanor recognition v4 (HERO). FILE: ${FILE}
WHOLE-WATCH: read EVERY frame in ${FRAMES} in order (fr_001.jpg up, 4fps, 5s). Do not sample.
AXIS: ${a.key} -> ${a.lens}
Return JSON: pass, recognition_start_frame, welling_present, first_frame_state, last_frame_state, severity, evidence[] (cite frames), score_0_10 (strict), fix.`,
  { schema: REFUTE, label:`herov4:${a.key}`, phase:'Refute' }
).then(r => r ? { ...r, axis:a.key } : null)))).filter(Boolean);

phase('Verdict');
const verdict = await agent(
`Does the corrected hero v4 hit the 9 FLOOR? You did not make it.
${BASE}
v4 VERDICTS: ${JSON.stringify(votes)}
Return JSON { hits_9 (true/false), score_0_10, verdict (excellent-9plus|strong-85|borderline|fail), delta_vs_v3, fixed_backloading (true/false), welling_present (true/false), remaining_gap_to_9, one_line }. Be strict: hits_9 only if a real felt recognition arc with welling reads and holds, airable and moving, no blocking slop.`,
  { schema:{ type:'object', properties:{ hits_9:{type:'boolean'}, score_0_10:{type:'number'}, verdict:{type:'string'}, delta_vs_v3:{type:'string'}, fixed_backloading:{type:'boolean'}, welling_present:{type:'boolean'}, remaining_gap_to_9:{type:'string'}, one_line:{type:'string'} }, required:['hits_9','score_0_10','verdict','one_line'] }, label:'herov4-verdict' }
);
return { votes, verdict };
