export const meta = {
  name: 'alma-v5',
  description: 'Alma Love reel V5 through the 7-role harness: orchestrator pins the goal, moment agents verify in/out, grade agent forces one master WB, brand/taste agent protects expensive-deadpan + body ratio, build agent cuts V5, fresh-context skeptics verify, verdict synthesizes. No agent selects+cuts+grades+reviews+crowns its own work.',
  whenToUse: 'Recut Alma V5 against the V4 adversarial fix list (one master grade, honest transitions, expensive-deadpan + brand layer). Serious production -> harness-mandatory.',
  phases: [
    { title: 'Moment-verify', detail: 'one fresh agent per cut entry, whole-watch, tighten in/out, flag transition-real + thirst' },
    { title: 'Grade+brand', detail: 'grade agent measures per-clip WB to one master; brand/taste agent protects deadpan + body ratio + brand layer' },
    { title: 'Synthesize-spec', detail: 'merge into one deterministic BUILD_SPEC' },
    { title: 'Build', detail: 'edit/build agent runs ffmpeg, produces V5 + web' },
    { title: 'Verify', detail: '5 fresh-context skeptics, one per axis, whole-watch V5' },
    { title: 'Verdict', detail: 'synthesize one honest call + score + send/no-send inputs' }
  ]
}

// ---- pinned goal + constraints (defends goal drift: injected into every agent) ----
const GOAL = `GOAL: a 30s vertical (1080x1920) Alma Love brand reel that reads as ONE expensive-deadpan film, not a stitched-clip thirst trap. It must survive a hostile adversarial verify. Target 10/10; 9 is the floor.
HARD CONSTRAINTS (do not relax):
- NO SAMPLING. Whole-watch every clip/segment end to end. 3-frame strips are triage only, never the basis for a claim.
- One LOCKED master grade/WB across all shots: blue-minus-red (B-R) channel mean within +/-5 across every shot after grade. V4 failed here (B-R swung +24 cool to -10 warm = stitched).
- Honest labels only. If a boundary is a hard cut, call it a hard cut. Do NOT claim "lens-wipe" unless an actual whip/garment/hair wipe exists in the footage at that join. V4 was caught overselling hard cuts as lens-wipes.
- Expensive-deadpan tone, body framing under ~30% of shots. No thirst-forward framing. The hero is the LONGEST hold (pacing contrast).
- Alma brand: warm retro-Americana, red signature. A legible brand layer (red wordmark) at open and a lockup at close.
- Identity must hold across every shot (one model throughout; same face). Any morph/melt = blocker.
ROLE BOUNDARY: you do ONLY your assigned role. You do not crown the final result. The orchestrator owns the final decision; a separate adversarial-verify phase judges the cut.`;

const CANON_DIR = '/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/01_RAW_VIDEO';
const IPHONE_DIR = '/Users/sniper/Downloads';
const LUT = '/Users/sniper/alma_lut.cube';
const OUTDIR = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_EDITOR_HANDOFF_001';
const WORK = OUTDIR + '/_v5_work';
const WM_RED = '/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/05_EXPORTS/DELIVERABLES/ALMA_LOVE_BRAND_KIT/logo/ALMA_LOVE_wordmark_red.png';
const WM_LOCKUP = '/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/05_EXPORTS/DELIVERABLES/ALMA_LOVE_BRAND_KIT/logo/ALMA_LOVE_lockup_SWIM_red.png';

function resolve(src, orient) {
  return orient === 'canon' ? `${CANON_DIR}/${src}.MP4` : `${IPHONE_DIR}/${src}.MOV`;
}

// V4 edit map (the spine to verify/tighten, NOT to trust blindly)
const EDIT = [
  { idx:1,  role:'HOOK',       src:'IMG_9509', in:2.9,  len:1.5, orient:'iphone', moment:'tight deadpan MCU at the lens' },
  { idx:2,  role:'wipe-in',    src:'IMG_9510', in:14.0, len:2.2, orient:'iphone', moment:'walks INTO lens, frame blacks (claimed lens-wipe)' },
  { idx:3,  role:'movement',   src:'D94A3320', in:5.6,  len:2.4, orient:'canon',  moment:'emerges from the convertible' },
  { idx:4,  role:'attitude',   src:'D94A3317', in:6.0,  len:1.6, orient:'canon',  moment:'deadpan full-body pose by the car' },
  { idx:5,  role:'hero-pwr',   src:'IMG_9510', in:18.2, len:2.3, orient:'iphone', moment:'hands-on-hips power stance' },
  { idx:6,  role:'product',    src:'IMG_9541', in:0.3,  len:1.8, orient:'iphone', moment:'swimwear dangled out the window' },
  { idx:7,  role:'TRANSITION', src:'D94A3320', in:10.3, len:1.9, orient:'canon',  moment:'tie-dye cover-up swings across lens, blows to red (claimed lens-wipe)' },
  { idx:8,  role:'turn',       src:'IMG_9524', in:2.3,  len:3.2, orient:'iphone', moment:'TUG-OF-WAR on the towel, hair whipping' },
  { idx:9,  role:'transition', src:'IMG_9523', in:9.5,  len:1.1, orient:'iphone', moment:'second model enters + hair sweep (claimed lens-wipe)' },
  { idx:10, role:'group',      src:'IMG_9523', in:10.8, len:1.7, orient:'iphone', moment:'reveal TWO models walking side by side' },
  { idx:11, role:'HERO',       src:'D94A3316', in:26.0, len:4.5, orient:'canon',  moment:'sustained hero in convertible, direct eye contact (longest hold)' },
  { idx:12, role:'deadpan',    src:'IMG_9533', in:13.0, len:2.2, orient:'iphone', moment:'chin-up expensive look' },
  { idx:13, role:'ending',     src:'IMG_9542', in:18.8, len:2.8, orient:'iphone', moment:'car drives away' },
  { idx:14, role:'button',     src:'IMG_9509', in:3.1,  len:1.1, orient:'iphone', moment:'final deadpan' }
].map(e => ({ ...e, path: resolve(e.src, e.orient) }));

// distinct clips for the grade pass
const DISTINCT = Array.from(new Set(EDIT.map(e => e.src))).map(src => {
  const e = EDIT.find(x => x.src === src);
  return { src, orient: e.orient, path: e.path };
});

log(`V5 harness: ${EDIT.length} cut entries, ${DISTINCT.length} distinct clips. Goal pinned. Work dir: ${WORK}`);

// ============ PHASE 1: MOMENT-VERIFY (parallel, one fresh agent per cut entry) ============
phase('Moment-verify');
const MOMENT_SCHEMA = { type:'object', properties:{
  idx:{type:'number'}, verified:{type:'boolean'},
  recommended_in:{type:'number'}, recommended_len:{type:'number'},
  is_the_claimed_moment:{type:'boolean'},
  transition_real:{type:'boolean'}, transition_kind:{type:'string'},
  body_ratio_estimate:{type:'number'}, thirst_risk:{type:'string'},
  identity_ok:{type:'boolean'}, keep:{type:'boolean'},
  notes:{type:'string'}
}, required:['idx','verified','recommended_in','recommended_len','transition_real','keep','notes'] };

const moments = (await parallel(EDIT.map(e => () => agent(
`${GOAL}

ROLE: MOMENT agent for ONE cut entry. Verify and tighten the in/out, and report the truth about it. You select nothing else and crown nothing.

CUT ENTRY #${e.idx} (${e.role}): ${e.moment}
SOURCE: ${e.path}
ORIENT: ${e.orient} (${e.orient==='canon'?'Canon vertical-native, will be transpose=2 then 9:16':'iPhone landscape, will be punch-cropped to 9:16'})
V4 in=${e.in}s len=${e.len}s

DO:
1. Whole-watch the clip around this window. Extract frames across at least [in-2s , in+len+2s] at >=4fps with ffmpeg into a temp dir, then Read EVERY extracted frame (no sampling). For a Canon (.MP4) clip apply transpose=2 when extracting so you see it upright. For iPhone (.MOV) extract as-is (landscape).
   Example: mkdir -p /tmp/mv_${e.idx} && ffmpeg -y -ss <start> -t <dur> -i "${e.path}" -vf "<transpose=2,>fps=6,scale=360:-2" /tmp/mv_${e.idx}/f_%03d.jpg   then Read all f_*.jpg.
2. Decide the TIGHTEST in-point and length that captures the real action/expression cleanly (recommended_in, recommended_len). Keep len roughly 1.0-4.5s.
3. is_the_claimed_moment: does the footage actually show what the entry claims?
4. transition_real: at the OUT boundary, is there an actual in-camera wipe (garment/hair/whip across lens, or a true blur-to-black)? TRUE only if you literally see it; otherwise FALSE (it will be an honest hard cut). transition_kind = what you saw ('hard-cut' if none).
5. body_ratio_estimate (0-1): how body-forward is the framing. thirst_risk: none/low/med/high. Expensive-deadpan favors face/attitude over body.
6. identity_ok: same model, no morph/melt, in-focus.
7. keep: should this beat stay in a 30s expensive-deadpan cut? If it is redundant or thirst-forward, keep=false and say what should replace it.
Cite concrete frame timestamps in notes. Return the JSON.`,
  { schema: MOMENT_SCHEMA, label:`moment:${e.idx}:${e.src}`, phase:'Moment-verify', model:'sonnet' }
).then(r => r ? { ...r, idx:e.idx, src:e.src, role:e.role, orient:e.orient, path:e.path } : null)))).filter(Boolean);

log(`Moment-verify done: ${moments.length}/${EDIT.length} returned. keep=${moments.filter(m=>m.keep).length}, real-transitions=${moments.filter(m=>m.transition_real).length}`);

// ============ PHASE 2: GRADE + BRAND (parallel barrier) ============
phase('Grade+brand');
const GRADE_SCHEMA = { type:'object', properties:{
  master_target:{type:'object', properties:{ b_minus_r:{type:'number'}, note:{type:'string'} }},
  per_clip:{type:'array', items:{type:'object', properties:{
    src:{type:'string'}, measured_b_minus_r:{type:'number'},
    correction_filter:{type:'string'}, note:{type:'string'}
  }, required:['src','correction_filter'] }},
  notes:{type:'string'}
}, required:['master_target','per_clip'] };

const BRAND_SCHEMA = { type:'object', properties:{
  cut_or_replace:{type:'array', items:{type:'number'}},
  hero_is_longest_hold:{type:'boolean'},
  body_forward_flags:{type:'array', items:{type:'number'}},
  transition_policy:{type:'string'},
  brand_layer:{type:'object', properties:{
    open:{type:'object', properties:{ png:{type:'string'}, start:{type:'number'}, end:{type:'number'}, scale_w:{type:'number'}, x:{type:'string'}, y:{type:'string'} }},
    close:{type:'object', properties:{ png:{type:'string'}, start_from_end:{type:'number'}, scale_w:{type:'number'}, x:{type:'string'}, y:{type:'string'} }}
  }},
  notes:{type:'string'}
}, required:['transition_policy','brand_layer','notes'] };

const gradeThunk = () => agent(
`${GOAL}

ROLE: GRADE agent. Force ONE master white balance across all shots. V4 failed because Canon and iPhone shots graded to different WB (B-R swung +24 cool to -10 warm). Fix it with measured numbers.

CLIPS (measure each at its used in-point):
${EDIT.map(e=>`#${e.idx} ${e.src} ${e.orient} in~${e.in}s -> ${e.path}`).join('\n')}
LUT applied last: ${LUT}

DO:
1. For each DISTINCT clip below, extract ONE representative frame at its in-point (Canon: add transpose=2), then measure channel means. Use ffmpeg signalstats or: ffmpeg -ss <in> -i "<path>" -frames:v 1 -vf "<transpose=2,>format=rgb24,scale=200:-2" /tmp/g_<src>.png ; then magick /tmp/g_<src>.png -resize 1x1 txt:- to read R,G,B. Compute B-R.
   DISTINCT: ${DISTINCT.map(d=>`${d.src} (${d.orient}) ${d.path}`).join(' | ')}
2. Pick ONE master_target B-R (warm Alma look, slightly warm so B-R modestly negative, e.g. around -3 to 0).
3. For EACH clip output a concrete ffmpeg correction_filter string (e.g. "colortemperature=temperature=5400:pl=1,eq=gamma_r=1.0:gamma_b=0.96," with a TRAILING COMMA) that, applied BEFORE lut3d, brings that clip's B-R within +/-5 of the master. iPhone clips typically need warming or cooling opposite to Canon; give real per-clip values, not a single shared filter.
4. Keep corrections gentle (no crushed/posterized look). Note any clip that cannot be matched.
Return JSON. correction_filter MUST be a valid ffmpeg -vf fragment ending in a comma so it can be concatenated before lut3d.`,
  { schema: GRADE_SCHEMA, label:'grade:master-wb', phase:'Grade+brand', model:'sonnet' }
);

const brandThunk = () => agent(
`${GOAL}

ROLE: BRAND / TASTE agent. Protect expensive-deadpan tone, body ratio, and the Alma brand layer. You judge tone and brand only; you do not cut.

THE EDIT (V4 spine): ${JSON.stringify(EDIT.map(e=>({idx:e.idx,role:e.role,src:e.src,moment:e.moment})))}
Brand identity: warm retro-Americana (western/beach/soda-shop), RED signature, cards/dice club motif, group/plural energy. Reference the brand kit: /Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/05_EXPORTS/DELIVERABLES/ALMA_LOVE_BRAND_KIT/ (read ALMA_LOVE_BRAND_KIT.md if useful).
Available brand PNGs (transparent): red wordmark = ${WM_RED} ; red SWIM lockup = ${WM_LOCKUP}.

DO:
1. Flag any beat that is body-forward / thirst (idx list = body_forward_flags) and any that should be cut or replaced for a 30s expensive-deadpan reel (cut_or_replace). The point is attitude and face, not body.
2. hero_is_longest_hold: confirm the eye-contact hero (#11) is the longest single hold; if not, say what to change.
3. transition_policy: 'honest_hardcut' (label every join a hard cut, no fake lens-wipe wording) OR 'build_real' (only if real wipes exist per the moment agents). Default to honest_hardcut unless real in-camera wipes are confirmed.
4. brand_layer: place the RED WORDMARK at open (small, lower third, ~0.0-1.4s, scale_w ~ 360-460px on a 1080-wide frame, give x/y as ffmpeg overlay expressions) and the SWIM LOCKUP (or wordmark) at close (last ~1.5s). Keep it tasteful and legible, not a watermark slapped center.
Return JSON with concrete png paths + positions.`,
  { schema: BRAND_SCHEMA, label:'brand:taste', phase:'Grade+brand' }
);

const [grade, brand] = await parallel([gradeThunk, brandThunk]);
log(`Grade: master B-R target=${grade && grade.master_target ? grade.master_target.b_minus_r : '?'}, ${grade ? grade.per_clip.length : 0} clip corrections. Brand: policy=${brand ? brand.transition_policy : '?'}, cut=${brand && brand.cut_or_replace ? JSON.stringify(brand.cut_or_replace) : '[]'}`);

// ============ PHASE 3: SYNTHESIZE BUILD_SPEC ============
phase('Synthesize-spec');
const SPEC_SCHEMA = { type:'object', properties:{
  segments:{type:'array', items:{type:'object', properties:{
    order:{type:'number'}, src:{type:'string'}, path:{type:'string'}, orient:{type:'string'},
    in:{type:'number'}, len:{type:'number'}, grade_filter:{type:'string'},
    boundary:{type:'string'}, role:{type:'string'}
  }, required:['order','src','path','orient','in','len','grade_filter'] }},
  brand_layer:{type:'object'},
  transition_policy:{type:'string'},
  total_target_sec:{type:'number'},
  dropped:{type:'array', items:{type:'string'}},
  notes:{type:'string'}
}, required:['segments','transition_policy','total_target_sec'] };

const spec = await agent(
`${GOAL}

ROLE: SYNTHESIS. Merge the three role outputs into ONE deterministic BUILD_SPEC the build agent will execute literally. Resolve every conflict; the orchestrator owns the goal, you serve it.

MOMENT VERIFICATIONS: ${JSON.stringify(moments)}
GRADE: ${JSON.stringify(grade)}
BRAND/TASTE: ${JSON.stringify(brand)}

RULES:
- Drop any segment where the moment agent set keep=false OR brand flagged it in cut_or_replace. List what you dropped + why in 'dropped'. Keep the spine coherent (hook -> build -> turn/reveal -> hero hold -> close -> button); if dropping breaks a beat, note it.
- Use each moment agent's recommended_in / recommended_len (tightened), not the V4 values.
- Attach each clip's grade correction_filter from the grade agent as grade_filter (must end in a comma; '' if none). Match by src.
- boundary: for each segment, the honest join label ('hard-cut' unless transition_real was true for that segment).
- brand_layer: carry through the brand agent's open/close plan with concrete png paths + positions.
- total_target_sec ~ 28-32s. Order segments and set 'order' 1..N.
Return strict JSON. Every path/in/len/grade_filter must be build-ready.`,
  { schema: SPEC_SCHEMA, label:'synthesize-spec' }
);
log(`BUILD_SPEC: ${spec ? spec.segments.length : 0} segments, target ${spec ? spec.total_target_sec : '?'}s, dropped ${spec && spec.dropped ? spec.dropped.length : 0}.`);

// ============ PHASE 4: BUILD ============
phase('Build');
const BUILD_SCHEMA = { type:'object', properties:{
  ok:{type:'boolean'}, output_path:{type:'string'}, web_path:{type:'string'},
  duration_sec:{type:'number'}, resolution:{type:'string'}, segments_built:{type:'number'},
  brand_layer_applied:{type:'boolean'}, build_log_tail:{type:'string'}, problems:{type:'string'}
}, required:['ok','output_path'] };

const build = await agent(
`${GOAL}

ROLE: EDIT / BUILD agent. Execute the BUILD_SPEC with ffmpeg and produce the V5 file. Do NOT re-judge selection or grade; build exactly what the spec says. You crown nothing.

BUILD_SPEC: ${JSON.stringify(spec)}
LUT (apply LAST in each segment): ${LUT}
WORK DIR: ${WORK}  (mkdir -p it)
FINAL OUTPUT: ${OUTDIR}/ALMA_REEL_INHOUSE_V5_MOMENT_CUT.mp4
WEB OUTPUT: ${OUTDIR}/ALMA_REEL_INHOUSE_V5_web.mp4

METHOD (write a bash script to ${WORK}/build_v5.sh and run it with: bash "${WORK}/build_v5.sh" -- NEVER rely on zsh word-splitting, NEVER put inline # comments after a filter arg):
1. mkdir -p "${WORK}".
2. For EACH segment build a normalized 1080x1920 30fps clip:
   ffmpeg -y -ss <in> -t <len> -i "<path>" -vf "<ROT><GRADE>scale=-2:1920,crop=1080:1920,fps=30,lut3d=${LUT}" -an -c:v libx264 -crf 19 -pix_fmt yuv420p "${WORK}/seg_<order>.mp4"
   where ROT = "transpose=2," for orient==canon else "" ; GRADE = the segment's grade_filter (already ends in a comma, or "" ). Order in the vf chain: rotate -> grade -> scale -> crop -> fps -> lut3d.
3. Concat with the demuxer: write ${WORK}/list.txt with one  file 'seg_<order>.mp4'  line per segment IN ORDER, then:
   ffmpeg -y -f concat -safe 0 -i "${WORK}/list.txt" -c:v libx264 -crf 19 -pix_fmt yuv420p "${WORK}/concat.mp4"
4. Brand layer: overlay the brand_layer PNGs from the spec onto concat.mp4 using -filter_complex with scale + overlay + enable='between(t,start,end)' for open, and enable between (duration-1.5, duration) for close. PNGs are transparent. Produce the FINAL OUTPUT. If brand_layer is missing/empty, copy concat.mp4 to the final path and set brand_layer_applied=false.
5. Web version: ffmpeg -y -i FINAL -vf scale=-2:1280 -c:v libx264 -crf 23 -movflags +faststart WEB.
6. Verify: ffprobe the final for duration + resolution. It MUST be 1080x1920. Report duration_sec, resolution, segments_built, brand_layer_applied, and the last ~15 lines of any error output in build_log_tail. If anything failed, ok=false and explain in problems.
Return JSON.`,
  { schema: BUILD_SCHEMA, label:'build:v5', model:'sonnet' }
);
log(`Build: ok=${build ? build.ok : false} ${build ? build.output_path : ''} dur=${build ? build.duration_sec : '?'}s res=${build ? build.resolution : '?'}`);

// ============ PHASE 5: ADVERSARIAL VERIFY ============
phase('Verify');
const V5_PATH = (build && build.ok && build.output_path) ? build.output_path : `${OUTDIR}/ALMA_REEL_INHOUSE_V5_MOMENT_CUT.mp4`;
const REAL_FOOTAGE_NOTE = 'IMPORTANT: the source is REAL CAMERA FOOTAGE of a real model (iPhone + Canon), NOT AI-generated video. Do NOT label in-camera motion blur, a moving body, or an intentional garment/hair wipe across the lens as "AI melt / generative morph / anatomy melt" - those failure modes do not apply to real footage. A frame that is mostly filled by one in-frame colored object (e.g. a red garment swung across the lens) is a TRANSITION frame, not a grade fault: exclude transition frames from any grade/identity measurement and judge only HELD shots.';
const AXES = [
  { key:'identity', lens:'identity/likeness CONSISTENCY across HELD shots (os-face-lock): is it the same real model everywhere, in focus? (real footage = no generative morph; judge wardrobe/face continuity, not blur)' },
  { key:'grade',    lens:'ONE master grade/WB: measure B-R channel mean on HELD frames only (exclude transition frames dominated by one colored object); does any HELD shot jump outside +/-5 of the others? does it read stitched?' },
  { key:'craft',    lens:'edit craft (Commercial Craft V2): is the hero the longest hold, are cuts motivated, does it read expensive-MUTED or stitched, pacing contrast, clean loop' },
  { key:'truth',    lens:'claim-truth: every boundary labeled honestly (no fake lens-wipe)? does it deliver a 30s ONE-film expensive-deadpan reel? what is missing/overstated? (duration + audio are fair game)' },
  { key:'slop',     lens:'brand-tone + taste (os-vision-reject-gate): thirst-vs-expensive, body ratio under ~30% of shots, brand layer legible + on-brand (warm retro red). On REAL footage, uncanny-AI artifacts do NOT apply - do not invent them' }
];
const VERDICT_AXIS = { type:'object', properties:{
  axis:{type:'string'}, refuted:{type:'boolean'}, severity:{type:'string'},
  evidence:{type:'array', items:{type:'string'}}, fix:{type:'string'}
}, required:['axis','refuted','evidence'] };

const votes = (await parallel(AXES.map(a => () => agent(
`You are a HOSTILE, fresh-context reviewer. Your ONLY job is to REFUTE the claim on ONE axis. Default refuted=true unless the evidence clearly clears it.
${GOAL}
${REAL_FOOTAGE_NOTE}
CLAIM: this V5 cut is a client-ready 30s expensive-deadpan Alma reel with ONE master grade and honest transitions.
ARTIFACT: ${V5_PATH}
AXIS: ${a.key} -> ${a.lens}
Inspect directly: extract frames with ffmpeg across the WHOLE file (>=2fps) and Read them (no sampling); for grade, measure per-shot channel means numerically. Cite timestamps + numbers. Return JSON: refuted, severity (blocker/major/minor/none), evidence[], fix (single highest-leverage fix). No politeness.`,
  { schema: VERDICT_AXIS, label:`verify:${a.key}`, phase:'Verify' }
)))).filter(Boolean);
log(`Verify: ${votes.length}/5 axes returned, refuted=${votes.filter(v=>v.refuted).length}`);

// ============ PHASE 6: VERDICT ============
phase('Verdict');
const verdict = await agent(
`Synthesize these adversarial verdicts on Alma V5 into ONE honest call.
BUILD: ${JSON.stringify(build)}
VERDICTS: ${JSON.stringify(votes)}
Rules: ANY blocker on a never-relax axis (identity, slop hard-fail) => blocked. Count refutes. Compare honestly to V4's 5.5/10: did the master-grade, honest-transition, expensive-deadpan, and brand-layer fixes actually land (measured)?
Return JSON {overall (clear|conditional|blocked), score (0-10), blockers:[], fixes_ranked:[], whats_better_than_v4:[], blocks_10, send_no_send (send|no-send), one_line}.`,
  { schema:{ type:'object', properties:{ overall:{type:'string'}, score:{type:'number'}, blockers:{type:'array',items:{type:'string'}}, fixes_ranked:{type:'array',items:{type:'string'}}, whats_better_than_v4:{type:'array',items:{type:'string'}}, blocks_10:{type:'string'}, send_no_send:{type:'string'}, one_line:{type:'string'} }, required:['overall','score','send_no_send','one_line'] }, label:'verdict' }
);

return { moments, grade, brand, spec, build, votes, verdict };
