#!/bin/zsh
# ALMA LOVE commercial finishing master. Data-driven WB unify -> real brand LUT -> uniform grain/halation/sharpness-pulldown.
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
V=../02_VIDEO_TESTS; M=../03_REAL_MACROS; A=../05_AUDIO
LUT="/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/05_EXPORTS/DELIVERABLES/ALMA_LOVE_BRAND_KIT/preset/ALMA_LOVE_signature_look_v1.cube"
KIT="/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/05_EXPORTS/DELIVERABLES/ALMA_LOVE_BRAND_KIT/logo"
F() { ffmpeg -nostdin -loglevel error -y "$@"; }
SCALE="scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24"
# LUT blended at 30% (full + 42% pushed magenta on skin); green-recovery added globally in stage 3 to keep skin R>G>B
LUTBLEND="split=2[lo][ll];[ll]lut3d='${LUT}':interp=tetrahedral[lg];[lo][lg]blend=all_mode=normal:all_opacity=0.30"

# Stage 1: per-beat = scale -> WB unify (colorbalance midtones, data-driven) -> real LUT. No grain yet (grain goes on master).
# args: file ss t  rm bm  out   (rm/bm = midtone red/blue balance to neutralize warm/cool spread toward family)
seg() { F -ss "$2" -t "$3" -i "$1" -vf "${SCALE},colorbalance=rm=$4:bm=$5,${LUTBLEND},format=yuv420p" -an -c:v libx264 -crf 16 -r 24 "$6"; }
#                                         rm      bm
seg $V/B01_kling_c94b30be.mp4   0   3.0   0.056  -0.056  m01.mp4   # noon: warm up the cool outlier
seg $V/PROD_hood_ab35eaac.mp4   0.4 2.0   0.010  -0.010  m02.mp4
seg $V/B03_walk_b41fac11.mp4    0.5 2.6   0.020  -0.020  m03.mp4
seg $M/MACRO_cherry_2812.mp4    0   2.0  -0.050   0.050  m04.mp4   # real cherry: rein warm studio toward family, keep red in highlights
seg $V/B06_gas_kling_ba948b6e.mp4 0 3.0  -0.016   0.016  m05.mp4
seg $V/B08_rearview_a75d09fe.mp4 0.4 2.6  0.000   0.000  m06.mp4
seg $V/PROD_mirror_a7638a45.mp4 0.4 2.0  -0.052   0.052  m07.mp4
seg $V/B10_solitaire_f028ce60.mp4 0 2.8  -0.100   0.100  m08.mp4   # solitaire: hottest, cool toward family
seg $M/MACRO_dice_2810.mp4      0   1.8  -0.048   0.048  m09.mp4
# night: cool the orange toward family + lift shadows slightly (separate, keeps it warm-dark)
F -ss 0 -t 4.0 -i $V/B19_night_kling_b0aecae7.mp4 -vf "${SCALE},colorbalance=rm=-0.084:bm=0.084,eq=gamma=1.06:brightness=0.03,${LUTBLEND},format=yuv420p" -an -c:v libx264 -crf 16 -r 24 m10.mp4

# Stage 2: concat the BODY (10 beats + a motivated 4-frame dip-to-black before the night payoff). End card appended AFTER grade.
F -t 0.166 -f lavfi -i color=c=0x070506:s=1920x1080:r=24 -c:v libx264 -crf 16 blk.mp4
printf "file 'm01.mp4'\nfile 'm02.mp4'\nfile 'm03.mp4'\nfile 'm04.mp4'\nfile 'm05.mp4'\nfile 'm06.mp4'\nfile 'm07.mp4'\nfile 'm08.mp4'\nfile 'm09.mp4'\nfile 'blk.mp4'\nfile 'm10.mp4'\n" > mlist.txt
F -f concat -safe 0 -i mlist.txt -c copy _master_body.mp4

# Stage 3: film finish on the body. GREEN-RECOVERY first (kills the LUT magenta: add green, pull blue/red so skin reads R>G>B), then neutral halation, 35mm grain, sharpness pulldown, vignette.
GREENFIX="colorbalance=rm=-0.02:gm=0.10:bm=-0.05:gh=0.07:bh=-0.03:gs=0.04"
HAL="split=2[b][g];[g]curves=all='0/0 0.76/0 1/1',gblur=sigma=14,colorbalance=rm=0.03:gh=0.02[glow];[b][glow]blend=all_mode=screen:all_opacity=0.22,format=yuv420p"
FILMGRAIN="noise=alls=11:allf=t"
SOFTEN="unsharp=lx=5:ly=5:la=-0.45:cx=5:cy=5:ca=0.0"
VIG="vignette=PI/8"
F -i _master_body.mp4 -vf "${GREENFIX},${HAL},${FILMGRAIN},${SOFTEN},${VIG},format=yuv420p" -c:v libx264 -crf 16 -r 24 _body_graded.mp4

# Stage 3b: CLEAN end card from the operator's REAL wordmark (IMG_3366 = ALMA LOVE CLUB bold sans), negated to white-on-black, drop shadow + soft glow + grain. No LUT, no magenta wash.
LOGO="/Users/sniper/.claude/uploads/3d92356b-5ad9-4a03-99f9-fe6e47b3f84d/c240fb49-IMG_3366.png"
F -t 3.0 -f lavfi -i color=c=0x070506:s=1920x1080:r=24 -framerate 24 -loop 1 -t 3.0 -i "$LOGO" \
 -filter_complex "[1:v]negate,scale=900:-1[wm];[wm]split=2[wms][wmg];[wmg]gblur=sigma=9[glow];[0:v][glow]overlay=(W-w)/2:(H-h)/2+3:format=auto[g1];[g1][wms]overlay=(W-w)/2:(H-h)/2:format=auto,noise=alls=7:allf=t,format=yuv420p" \
 -t 3.0 -r 24 -c:v libx264 -crf 16 mEND.mp4

# Stage 3c: concat graded body + clean end card
printf "file '_body_graded.mp4'\nfile 'mEND.mp4'\n" > flist2.txt
F -f concat -safe 0 -i flist2.txt -c copy _master_pic.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 _master_pic.mp4)

# Stage 4: mux owned music (commercial-licensed), fade in/out, bed level, normalize
MUSIC="$A/music__20260612_200235.mp3"
F -i _master_pic.mp4 -i "$MUSIC" -filter_complex "[1:a]atrim=0:${DUR},afade=t=in:st=0:d=0.6,afade=t=out:st=$(echo "$DUR-1.6"|bc -l):d=1.6,loudnorm=I=-15:TP=-1.5,volume=0.9[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 256k -shortest ALMA_LOVE_FULL_CUT_v2_FINISH.mp4

# Web preview (smaller, 1280-wide, faststart, 48kHz audio)
F -i ALMA_LOVE_FULL_CUT_v2_FINISH.mp4 -vf "scale=1280:720" -c:v libx264 -crf 22 -movflags +faststart -ar 48000 -c:a aac -b:a 160k ALMA_LOVE_v2_web_preview.mp4

echo "DUR=$DUR"
ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 ALMA_LOVE_FULL_CUT_v2_FINISH.mp4
du -h ALMA_LOVE_FULL_CUT_v2_FINISH.mp4 ALMA_LOVE_v2_web_preview.mp4 | cut -f1,2
echo "MASTER BUILD DONE"
