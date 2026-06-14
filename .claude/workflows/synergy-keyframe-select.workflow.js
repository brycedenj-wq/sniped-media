export const meta = {
  name: 'synergy-keyframe-select',
  description: 'Brute-force keyframe selection for the Synergy proof. 5 role-scoped agents: existing-shot audit, per-group emotional-performance scoring of 24 candidates, keyframe-strategy, motion-reroll plan, hostile QA. Every claim tied to a file path + numeric score. No self-crowning.',
  whenToUse: 'After generating candidate keyframes, before spending video credits, to pick the strongest start/end pairs.',
  phases: [
    { title: 'Audit+Score', detail: 'existing best-of audit + per-group candidate scoring (parallel)' },
    { title: 'Strategy', detail: 'do we have a 9-capable keyframe per beat or need more' },
    { title: 'Plan', detail: 'exact i2v start/end pairs + params' },
    { title: 'QA', detail: 'hostile verify the picks' }
  ]
}

const ROOT = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/_3SHOT_PROOF';
const CAND = `${ROOT}/candidates`;
const REF = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/SYNERGY_HOMECARE_TEST_001/_assets_bank';
const BRIEF = `Synergy HomeCare brand film. Anti-gloss DOCUMENTARY truth, restrained, client-safe, emotionally clear, NO corporate-healthcare gloss, NO melodrama. Target: a deliverable-grade proof for a partner/company review tomorrow, 8+ with no AI slop, no identity drift, no fake stock-healthcare sheen. These are END/START keyframes that will drive Kling 3.0 i2v, so what matters is: (1) frame-readable PERFORMANCE/emotion (eye contact, mouth soften, head turn, hand connection, breath/posture - NOT dependent on tears), (2) IDENTITY match to the reference person(s), (3) NO AI slop (waxy skin, melt, bad hands/teeth/eyes), (4) anti-gloss documentary look, (5) usable framing. Whole-look every image, cite the exact filename for every score.`;

const SCORE = { type:'object', properties:{
  group:{type:'string'},
  picks:{type:'array', items:{type:'object', properties:{
    file:{type:'string'}, performance:{type:'number'}, identity:{type:'number'}, slop_free:{type:'number'}, antigloss:{type:'number'}, framing:{type:'number'}, total:{type:'number'}, note:{type:'string'}
  }, required:['file','total','note'] }},
  best_file:{type:'string'}, best_total:{type:'number'}
}, required:['group','picks','best_file'] };

const GROUPS = [
  { key:'ELE_smile', mech:'Eleanor recognition via faint almost-smile + warm present eyes', ref:`${REF}/SB_V07_song_recognition.png`, files:[1,2,3,4].map(n=>`${CAND}/ELE_smile_${n}.png`) },
  { key:'ELE_turn',  mech:'Eleanor recognition via head-turn-to-music + lips parted mouthing the word', ref:`${REF}/SB_V07_song_recognition.png`, files:[1,2,3,4].map(n=>`${CAND}/ELE_turn_${n}.png`) },
  { key:'ELE_hand',  mech:'Eleanor recognition via hand rising to collarbone (gesture of being moved)', ref:`${REF}/SB_V07_song_recognition.png`, files:[1,2,3,4].map(n=>`${CAND}/ELE_hand_${n}.png`) },
  { key:'TOG_start', mech:'Together START: Eleanor disconnected/looking down, caregiver near, no contact (closer framing)', ref:`${REF}/SB_V11_together.png`, files:[1,2,3,4].map(n=>`${CAND}/TOG_start_${n}.png`) },
  { key:'TOG_eye',   mech:'Together END: Eleanor turned, real eye contact + faint smiles (closer framing)', ref:`${REF}/SB_V11_together.png`, files:[1,2,3,4].map(n=>`${CAND}/TOG_eye_${n}.png`) },
  { key:'TOG_hand',  mech:'Together END: caregiver hand clasped over Eleanor hands, both warm (closer framing)', ref:`${REF}/SB_V11_together.png`, files:[1,2,3,4].map(n=>`${CAND}/TOG_hand_${n}.png`) }
];

phase('Audit+Score');
const auditThunk = () => agent(
`ROLE: EXISTING-SHOT AUDIT. ${BRIEF}
Whole-watch the current best-of clips and report the honest baseline per beat, with file paths + the known adversarial scores, and what each LACKS that the new keyframes must fix.
- Daughter decision: ${ROOT}/clips/SHOT1_daughter_2am.mp4 (v1, scored 8.0) and frames ${ROOT}/clips/frames_SHOT1_daughter_2am
- Eleanor recognition: ${ROOT}/clips/SHOT2_eleanor_recognition_v2.mp4 (7.5) frames ${ROOT}/clips/frames_SHOT2_v2 ; also v4 ${ROOT}/clips/frames_SHOT2_v4 (6.5)
- Together turn: ${ROOT}/clips/SHOT3_together_turn.mp4 (v1, 7.5) frames ${ROOT}/clips/frames_SHOT3_together_turn
Return JSON {beats:[{beat, best_clip_path, score, what_works, what_lacks}], overall_floor}.`,
  { schema:{ type:'object', properties:{ beats:{type:'array',items:{type:'object'}}, overall_floor:{type:'string'} }, required:['beats'] }, label:'audit:existing', phase:'Audit+Score' }
);
const scoreThunks = GROUPS.map(g => () => agent(
`ROLE: EMOTIONAL-PERFORMANCE SCORING for one candidate group. ${BRIEF}
GROUP: ${g.key} -> ${g.mech}
REFERENCE (identity to match): ${g.ref}
CANDIDATES (Read EVERY one): ${g.files.join('  ')}
Read the reference, then read each candidate. Score each file 0-10 on: performance (frame-readable emotion landing), identity (same person as ref), slop_free (10 = zero AI artifacts), antigloss (10 = documentary, 0 = stock-healthcare gloss), framing (usable for the beat). total = your overall 0-10 for using this as the keyframe. Cite the exact filename. Name best_file + best_total.
Return JSON per the schema.`,
  { schema: SCORE, label:`score:${g.key}`, phase:'Audit+Score' }
));
const ascResults = await parallel([auditThunk, ...scoreThunks]);
const audit = ascResults[0];
const scores = ascResults.slice(1).filter(Boolean);
log(`Audit + ${scores.length} group scores done. Bests: ${scores.map(s=>s && `${s.group}:${s.best_file ? s.best_file.split('/').pop() : '?'}(${s.best_total})`).join(' | ')}`);

phase('Strategy');
const strategy = await agent(
`ROLE: KEYFRAME GENERATION STRATEGY. ${BRIEF}
Group scores: ${JSON.stringify(scores)}
Existing audit: ${JSON.stringify(audit)}
For each blocking beat (Eleanor recognition, Together connection), decide: do we already have a 9-capable END keyframe (and for Together, a START with a real pose delta to the END)? If YES, name the exact files. If NO, say exactly what mechanism/prompt to generate next (specific, so the orchestrator can fire it). Also pick the single best Together START file and whether it has enough disconnect-to-connect delta vs the chosen END.
Return JSON {per_beat:[{beat, have_9_capable_keyframe (bool), chosen_files:[], gap, next_gen_prompt_if_needed}], notes}.`,
  { schema:{ type:'object', properties:{ per_beat:{type:'array',items:{type:'object'}}, notes:{type:'string'} }, required:['per_beat'] }, label:'strategy' }
);

phase('Plan');
const plan = await agent(
`ROLE: MOTION REROLL PLAN. ${BRIEF}
Scores: ${JSON.stringify(scores)}
Strategy: ${JSON.stringify(strategy)}
Existing best-of (use the best PROVEN shot when a new path is not clearly better): daughter ${ROOT}/clips/SHOT1_daughter_2am.mp4 (8.0).
Produce the EXACT video reroll plan to assemble a best-of proof. For each shot give: keep_existing (bool, with path) OR animate (start_image file path, end_image file path, model=kling3_0, mode=pro, sound=off, duration_sec, the verb-first motion prompt). Keep it to the MINIMUM video rerolls (protect video credits): only re-roll the blocking beats. Rank the top 2 keyframe pairs per blocking beat in case the first take fails.
Return JSON {shots:[{beat, action, existing_path, start_image, end_image, duration_sec, prompt, backup_pair}], total_video_rerolls, rationale}.`,
  { schema:{ type:'object', properties:{ shots:{type:'array',items:{type:'object'}}, total_video_rerolls:{type:'number'}, rationale:{type:'string'} }, required:['shots'] }, label:'plan' }
);

phase('QA');
const QA_AXES = ['identity-truth (same person as the reference, no drift)','slop (waxy/melt/hands/teeth/eyes)','performance-readability (does the emotion read at frame level without tears)','anti-gloss + client-safe (documentary, not stock-healthcare)'];
const qa = (await parallel(QA_AXES.map(ax => () => agent(
`ROLE: HOSTILE QA. ${BRIEF} You did not pick these. Try to REFUTE that the chosen keyframes are deliverable-grade, on ONE axis: ${ax}.
CHOSEN PLAN: ${JSON.stringify(plan)}
Read the chosen start_image/end_image files in the plan directly. Cite filenames + exact observations. Return JSON {axis, approved (bool), problems:[], must_fix:[]}.`,
  { schema:{ type:'object', properties:{ axis:{type:'string'}, approved:{type:'boolean'}, problems:{type:'array',items:{type:'string'}}, must_fix:{type:'array',items:{type:'string'}} }, required:['axis','approved'] }, label:`qa:${ax.split(' ')[0]}` }
)))).filter(Boolean);

return { audit, scores, strategy, plan, qa };
