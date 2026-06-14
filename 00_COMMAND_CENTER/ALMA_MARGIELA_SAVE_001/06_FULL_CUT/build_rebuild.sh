#!/bin/zsh
# ALMA LOVE CLUB · HOLISTIC REBUILD 4K MASTER. Coherent beat set generated as ONE shoot (locked character + exact true-red product + one world).
# Because every beat shares one look, the grade is ONE unified pass (no per-beat color hacks). Scale-shock day->night, ~30s.
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
R=../07_REGEN/video; A=../05_AUDIO; M=../03_REAL_MACROS
LUT="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT/ALMA_LOVE_signature_look_v1.cube"
LOGO="/Users/sniper/.claude/uploads/3d92356b-5ad9-4a03-99f9-fe6e47b3f84d/c240fb49-IMG_3366.png"
F() { ffmpeg -nostdin -loglevel error -y "$@"; }
SCALE="scale=3840:2160:force_original_aspect_ratio=increase:flags=lanczos,crop=3840:2160,fps=24"
LUTB="split=2[lo][ll];[ll]lut3d='${LUT}':interp=tetrahedral[lg];[lo][lg]blend=all_mode=normal:all_opacity=0.28"
# ONE unified grade for every beat: gentle warm balance + brand LUT + slight contrast. NIGHT beats get a small lift only.
seg() {
  local extra=""
  case "$5" in
    NIGHT) extra=",eq=gamma=1.05:brightness=0.02:saturation=1.03" ;;
    PROD)  extra=",eq=brightness=-0.03:contrast=1.03:saturation=1.02" ;; # REAL macro: gentle integration only, no color push (it IS the exact product)
    *)     extra=",eq=saturation=1.04:contrast=1.02" ;;
  esac
  F -ss "$2" -t "$3" -i "$1" -vf "${SCALE},colorbalance=rm=0.02:bm=-0.02,${LUTB}${extra},format=yuv420p" -an -c:v libx264 -preset medium -crf 18 -r 24 "$4"
}
# beat sources (4K). new coherent beats RB_*; kept-coherent macros + in-car already 4K.
# PRODUCT-DETAIL beats use the REAL studio macros (pixel-exact garment, harness-certified), NOT AI: MACRO_cherry_2812 + MACRO_dice_2810 from BJ's _94A shoot.
DICE=$M/MACRO_dice_2810.mp4; CHERRY=$M/MACRO_cherry_2812.mp4; INCAR=$R/INCAR_drive_4k.mp4
ESTAB=$R/RB_establish_4k.mp4; HERO=$R/RB_hero_4k.mp4; WALK=$R/RB_walk_4k.mp4; GAS=$R/RB_gas_4k.mp4
PLURAL=$R/RB_plural_4k.mp4; SOLIT=$R/RB_solitaire_4k.mp4; NIGHT=$R/RB_night_4k.mp4
# ===== scale-shock order, day -> night, ~30s =====
seg $DICE    1.2 1.4  s01.mp4 PROD    # hook: dice symbol TIGHT
seg $ESTAB   0.4 2.2  s02.mp4 DAY     # world WIDE
seg $CHERRY  1.4 1.4  s03.mp4 PROD    # cherry TIGHT
seg $HERO    0.6 3.0  s04.mp4 DAY     # hero WIDE (reveal)
seg $INCAR   2.4 2.4  s05.mp4 DAY     # in-car MED (real top)
seg $WALK    0.6 2.2  s06.mp4 DAY     # walk WIDE (motion)
seg $GAS     0.8 2.4  s07.mp4 DAY     # gas MED
seg $PLURAL  0.8 2.4  s08.mp4 DAY     # club MED
seg $SOLIT   0.8 2.6  s09.mp4 DAY     # gamble action MED
seg $NIGHT   0.5 4.4  s11.mp4 NIGHT   # night payoff WIDE (earned hold)

# gamble card "LOVE IS A GAMBLE." (with period)
magick -size 3840x2160 xc:'#0A0708' -gravity center -font '/System/Library/Fonts/Supplemental/Didot.ttc' -pointsize 224 -fill '#C23A34' -interline-spacing 54 -annotate +0+0 'LOVE IS A GAMBLE.' card_gamble.png
F -loop 1 -t 1.6 -i card_gamble.png -vf "noise=alls=7:allf=t,fade=t=in:st=0:d=0.3,fade=t=out:st=1.3:d=0.3,format=yuv420p" -r 24 -c:v libx264 -preset medium -crf 18 s10.mp4
F -t 0.18 -f lavfi -i color=c=0x070506:s=3840x2160:r=24 -c:v libx264 -preset medium -crf 18 blk.mp4

printf "file 's01.mp4'\nfile 's02.mp4'\nfile 's03.mp4'\nfile 's04.mp4'\nfile 's05.mp4'\nfile 's06.mp4'\nfile 's07.mp4'\nfile 's08.mp4'\nfile 's09.mp4'\nfile 'blk.mp4'\nfile 's10.mp4'\nfile 's11.mp4'\n" > rb_list.txt
F -f concat -safe 0 -i rb_list.txt -c copy _rb_body.mp4

# Global finish (one pass): green-recovery, halation, fine grain, soften, vignette
GREENFIX="colorbalance=rm=-0.01:gm=0.04:bm=-0.03:gh=0.03:gs=0.02"
HAL="split=2[b][g];[g]curves=all='0/0 0.76/0 1/1',gblur=sigma=28,colorbalance=rm=0.03[glow];[b][glow]blend=all_mode=screen:all_opacity=0.18,format=yuv420p"
F -i _rb_body.mp4 -vf "${GREENFIX},${HAL},noise=alls=8:allf=t,unsharp=lx=7:ly=7:la=-0.35,vignette=PI/11,format=yuv420p" -c:v libx264 -preset medium -crf 19 -r 24 _rb_graded.mp4
rm -f _rb_body.mp4 s01.mp4 s02.mp4 s03.mp4 s04.mp4 s05.mp4 s06.mp4 s07.mp4 s08.mp4 s09.mp4 s10.mp4 s11.mp4 blk.mp4

# End card (real wordmark + CTA, larger)
magick -size 2400x320 xc:none -gravity center -font '/System/Library/Fonts/Optima.ttc' -pointsize 120 -fill '#E8DED9' -annotate +0+0 'TEXT  LOVECLUB  FOR  FIRST  DIBS' cta.png
F -t 2.6 -f lavfi -i color=c=0x070506:s=3840x2160:r=24 -framerate 24 -loop 1 -t 2.6 -i "$LOGO" -framerate 24 -loop 1 -t 2.6 -i cta.png \
 -filter_complex "[1:v]negate,scale=1560:-1[wm];[0:v][wm]overlay=(W-w)/2:820:format=auto[a];[a][2:v]overlay=(W-w)/2:1300:format=auto,noise=alls=7:allf=t,fade=t=in:st=0:d=0.3,format=yuv420p" -t 2.6 -r 24 -c:v libx264 -preset medium -crf 18 s12.mp4
printf "file '_rb_graded.mp4'\nfile 's12.mp4'\n" > rb_list2.txt
F -f concat -safe 0 -i rb_list2.txt -c copy _rb_pic.mp4
rm -f _rb_graded.mp4 s12.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 _rb_pic.mp4)

MUSIC="$A/music__20260612_200235.mp3"
DIPSTART=$(echo "$DUR-6.6"|bc -l); DIPEND=$(echo "$DIPSTART+0.25"|bc -l); FOUT=$(echo "$DUR-1.8"|bc -l)
F -i "$MUSIC" -filter_complex "[0:a]aloop=loop=2:size=2000000,atrim=0:${DUR},afade=t=out:st=${FOUT}:d=1.8,volume=0.28:enable='between(t,${DIPSTART},${DIPEND})'[mus];sine=frequency=52:duration=0.35[s0];[s0]afade=t=out:st=0.05:d=0.3,volume=1.6[thump];[mus][thump]amix=inputs=2:duration=first:normalize=0[mix];[mix]loudnorm=I=-14:TP=-1.5:LRA=9,alimiter=limit=0.891:level=disabled,aresample=48000[a]" -map "[a]" -t ${DUR} -c:a aac -b:a 256k _rb_audio.m4a

F -i _rb_pic.mp4 -i _rb_audio.m4a -map 0:v -map 1:a -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -profile:v high -c:a aac -b:a 256k -shortest -movflags +faststart ALMA_LOVE_REBUILD_4K_MASTER.mp4
F -i ALMA_LOVE_REBUILD_4K_MASTER.mp4 -vf scale=1920:1080:flags=lanczos -c:v libx264 -crf 21 -preset medium -movflags +faststart -c:a aac -b:a 192k ALMA_LOVE_REBUILD_WEB1080.mp4
rm -f _rb_pic.mp4 _rb_audio.m4a
echo "DUR=${DUR}s"; ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 ALMA_LOVE_REBUILD_4K_MASTER.mp4 2>/dev/null | head -1
du -h ALMA_LOVE_REBUILD_4K_MASTER.mp4 ALMA_LOVE_REBUILD_WEB1080.mp4 | cut -f1,2
echo "REBUILD DONE"
