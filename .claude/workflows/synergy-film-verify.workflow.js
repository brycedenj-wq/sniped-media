export const meta = {
  name: 'synergy-film-verify',
  description: 'Hostile verify the full Synergy "The Door" beat set before assembly. Score each beat, pick the hero best-of (v5 vs mouth-closed), read the together connection, and give film-readiness. No self-crowning.',
  whenToUse: 'After all beats are animated, before Premiere assembly.',
  phases: [ { title: 'Score', detail: 'parallel per-beat hostile score' }, { title: 'Synthesize', detail: 'hero pick + film readiness' } ]
}
const DIR = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/_FILM_BUILD/shots';
const LAWS = `STANDARD: Synergy HomeCare brand film, anti-gloss DOCUMENTARY truth, restrained, "makes a room go quiet", client-safe, NO corporate-healthcare gloss, NO melodrama, NO tears needed (frame-readable performance). AI-generated (Kling i2v): hunt slop (morph/melt/waxy/teeth/eye/hand, identity drift). For motion beats apply the Push-In Law (subject must act, not just camera). Whole-watch: extract frames from the mp4 with ffmpeg (fps=3, scale=240) into /tmp and Read ALL of them in order, no sampling. Score strictly 0-10 for use in a deliverable film for a partner review.`;
const BEATS = [
  { key:'phone', file:`${DIR}/SHOT_phone.mp4`, intent:'2am insert: phone glows 2:14 AM in the dark. Mood/time hook. Insert, minimal motion OK.' },
  { key:'daughter_decision', file:`${DIR}/SHOT_daughter.mp4`, intent:'A 30s-40s adult DAUGHTER (not elderly) lies awake at 2am, lowers the phone, exhales, accepts she needs help. Must read as the daughter + a real internal beat.' },
  { key:'door_hinge', file:`${DIR}/SHOT_door.mp4`, intent:'THE HINGE: warm light through the open door, the caregiver walks in, calm and warm. The moment the weight lifts. Real arrival motion.' },
  { key:'coffee', file:`${DIR}/SHOT_coffee.mp4`, intent:'Warm insert: coffee pours, steam rises, record needle lowers. Domestic warmth.' },
  { key:'hero_v5', file:`${DIR}/SHOT_hero_v5.mp4`, intent:'HERO candidate A: Eleanor recognition, blank profile -> turn -> warm almost-smile (eyes-led).' },
  { key:'hero_mc', file:`${DIR}/SHOT_hero_mc.mp4`, intent:'HERO candidate B: same recognition but prompted mouth-CLOSED to kill the mid-turn mouth-gape. Pick the better hero.' },
  { key:'together', file:`${DIR}/SHOT_together.mp4`, intent:'Connection beat: elderly woman + caregiver, hands joined / leaning in, warmth. Is the connection frame-readable? Honest read.' },
  { key:'coast', file:`${DIR}/SHOT_coast.mp4`, intent:'Breath of place: Cape Fear marsh/water, gentle ambient motion. Transition beat.' },
  { key:'exhale', file:`${DIR}/SHOT_exhale.mp4`, intent:'PAYOFF: the daughter (daytime) shoulders drop and she exhales, the weight lifting. Must read as the same younger daughter + real release.' }
];
const SCORE = { type:'object', properties:{ key:{type:'string'}, score_0_10:{type:'number'}, is_cinema:{type:'boolean'}, identity_ok:{type:'boolean'}, slop_free:{type:'boolean'}, on_brief:{type:'boolean'}, what_works:{type:'string'}, problems:{type:'array',items:{type:'string'}}, keep:{type:'boolean'} }, required:['key','score_0_10','keep'] };

phase('Score');
const scores = (await parallel(BEATS.map(b => () => agent(
`HOSTILE fresh-context reviewer. Score ONE film beat for a deliverable Synergy short.
${LAWS}
BEAT: ${b.key}
INTENDED: ${b.intent}
FILE: ${b.file}
Extract frames: mkdir -p /tmp/fv_${b.key} && ffmpeg -y -i "${b.file}" -vf "fps=3,scale=240:-2" /tmp/fv_${b.key}/f_%02d.jpg ; Read ALL frames in order.
Return JSON: key, score_0_10 (strict), is_cinema, identity_ok, slop_free, on_brief, what_works, problems[], keep (use in the film?).`,
  { schema: SCORE, label:`fv:${b.key}`, phase:'Score' }
).then(r => r ? { ...r, key:b.key } : null)))).filter(Boolean);

phase('Synthesize');
const verdict = await agent(
`Synthesize the Synergy film beat scores into a build decision. You did not make these.
SCORES: ${JSON.stringify(scores)}
Decide: (1) hero_pick = 'hero_v5' or 'hero_mc' (whichever scores higher / cleaner mouth), (2) which beats are KEEP vs CUT (cut anything below ~7 that isn't load-bearing; a tighter cut beats a weak beat), (3) the recommended FINAL beat order for a ~32s cut (worry -> decision -> arrival -> warmth -> recognition -> connection -> breath -> release -> title), (4) film_ready (true/false) for assembly, (5) weakest_link + its fix, (6) avg_score of kept beats.
Return JSON {hero_pick, keep:[], cut:[], final_order:[], film_ready, weakest_link, fix, avg_score, one_line}.`,
  { schema:{ type:'object', properties:{ hero_pick:{type:'string'}, keep:{type:'array',items:{type:'string'}}, cut:{type:'array',items:{type:'string'}}, final_order:{type:'array',items:{type:'string'}}, film_ready:{type:'boolean'}, weakest_link:{type:'string'}, fix:{type:'string'}, avg_score:{type:'number'}, one_line:{type:'string'} }, required:['hero_pick','keep','final_order','film_ready','one_line'] }, label:'film-verdict' }
);
return { scores, verdict };
