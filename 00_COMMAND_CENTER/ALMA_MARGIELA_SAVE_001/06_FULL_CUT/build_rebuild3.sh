#!/bin/zsh
# ALMA LOVE CLUB · REBUILD v3 FINAL GRADE POLISH (free, no generation). Same coherent cut as v2.
# Targeted per-beat grade to make it ONE warm Americana film matched to the REAL coral-on-cream suit:
#  - walk + plural: STRONG green-channel kill (colorchannelmixer) to remove the cool-green cast.
#  - all day beats: deeper de-green toward the warm gas/solitaire reference (G-R near 0).
#  - solitaire: modest coral pull (garment was hue ~29, real coral is 20-25).
#  - skin: NOT pushed red (modest hue, green-channel work not red-boost). Real macros: gentle integration only.
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
R=../07_REGEN/video; A=../05_AUDIO; M=../03_REAL_MACROS
LUT="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT/ALMA_LOVE_signature_look_v1.cube"
LOGO="/Users/sniper/.claude/uploads/3d92356b-5ad9-4a03-99f9-fe6e47b3f84d/c240fb49-IMG_3366.png"
F() { ffmpeg -nostdin -loglevel error -y "$@"; }
SCALE="scale=3840:2160:force_original_aspect_ratio=increase:flags=lanczos,crop=3840:2160,fps=24"
LUTB="split=2[lo][ll];[ll]lut3d='${LUT}':interp=tetrahedral[lg];[lo][lg]blend=all_mode=normal:all_opacity=0.26"
# DAY: warm + deep de-green. WALKG/PLURG: colorchannelmixer green-cut (strong) for the cool-green beats. SOLIT: coral pull. NIGHT: warm de-green. PROD: real macro gentle.
seg() {
  local extra="" precrop=""
  case "$5" in
    DAY)    extra=",hue=h=-4,colorbalance=rm=0.05:gm=-0.13:gh=-0.06:bm=-0.05,eq=saturation=1.05:contrast=1.03" ;;
    WALKG)  extra=",colorchannelmixer=0:0:0:0:0:0.84:0:0:0:0:1:0,hue=h=-4,colorbalance=rm=0.06:gm=-0.07:bm=-0.05,eq=saturation=1.06:contrast=1.03" ;;
    PLURG)  extra=",colorchannelmixer=0:0:0:0:0:0.88:0:0:0:0:1:0,hue=h=-5,colorbalance=rm=0.06:gm=-0.07:bm=-0.05,eq=saturation=1.06:contrast=1.03" ;;
    SOLIT)  extra=",hue=h=-7,colorbalance=rm=0.04:gm=-0.07:bm=-0.04,eq=saturation=1.05:contrast=1.03" ;;
    NIGHT)  extra=",eq=gamma=1.05:brightness=0.02:saturation=1.04,hue=h=-3,colorbalance=rm=0.05:gm=-0.10:bm=-0.04" ;;
    PROD)   extra=",eq=brightness=-0.03:contrast=1.03:saturation=1.02" ;;
    *)      extra="" ;;
  esac
  [ -n "$6" ] && precrop="$6,"
  F -ss "$2" -t "$3" -i "$1" -vf "${precrop}${SCALE},colorbalance=rm=0.02:bm=-0.02,${LUTB}${extra},format=yuv420p" -an -c:v libx264 -preset medium -crf 18 -r 24 "$4"
}
DICE=$M/MACRO_dice_2810.mp4; CHERRY=$M/MACRO_cherry_2812.mp4
ESTAB=$R/RB_establish_4k.mp4; HERO=$R/RB_hero_4k.mp4; WALK=$R/RB_walk_4k.mp4; GAS=$R/RB_gas_4k.mp4
PLURAL=$R/RB_plural_4k.mp4; SOLIT=$R/RB_solitaire_4k.mp4; NIGHT=$R/RB_night_4k.mp4
seg $CHERRY  1.4 1.5  s01.mp4 PROD
seg $ESTAB   0.4 2.4  s02.mp4 DAY  "crop=iw:ih*0.74:0:ih*0.20"
seg $HERO    0.5 3.2  s03.mp4 DAY
seg $WALK    0.6 2.2  s04.mp4 WALKG
seg $GAS     0.8 2.6  s05.mp4 DAY
seg $DICE    1.0 1.5  s06.mp4 PROD
seg $PLURAL  0.8 2.4  s07.mp4 PLURG
seg $SOLIT   0.8 2.6  s08.mp4 SOLIT
seg $NIGHT   0.5 4.6  s10.mp4 NIGHT

magick -size 3840x2160 xc:'#0A0708' -gravity center -font '/System/Library/Fonts/Supplemental/Didot.ttc' -pointsize 224 -fill '#C23A34' -interline-spacing 54 -annotate +0+0 'LOVE IS A GAMBLE.' card_gamble.png
F -loop 1 -t 1.6 -i card_gamble.png -vf "noise=alls=7:allf=t,fade=t=in:st=0:d=0.3,fade=t=out:st=1.3:d=0.3,format=yuv420p" -r 24 -c:v libx264 -preset medium -crf 18 s09.mp4
F -t 0.18 -f lavfi -i color=c=0x070506:s=3840x2160:r=24 -c:v libx264 -preset medium -crf 18 blk.mp4

printf "file 's01.mp4'\nfile 's02.mp4'\nfile 's03.mp4'\nfile 's04.mp4'\nfile 's05.mp4'\nfile 's06.mp4'\nfile 's07.mp4'\nfile 's08.mp4'\nfile 'blk.mp4'\nfile 's09.mp4'\nfile 's10.mp4'\n" > rb3_list.txt
F -f concat -safe 0 -i rb3_list.txt -c copy _rb3_body.mp4

DEGREEN="colorbalance=rm=0.01:gm=-0.03:bm=-0.01"
HAL="split=2[b][g];[g]curves=all='0/0 0.76/0 1/1',gblur=sigma=28,colorbalance=rm=0.03[glow];[b][glow]blend=all_mode=screen:all_opacity=0.18,format=yuv420p"
F -i _rb3_body.mp4 -vf "${DEGREEN},${HAL},noise=alls=8:allf=t,unsharp=lx=7:ly=7:la=-0.35,vignette=PI/11,format=yuv420p" -c:v libx264 -preset medium -crf 19 -r 24 _rb3_graded.mp4
rm -f _rb3_body.mp4 s01.mp4 s02.mp4 s03.mp4 s04.mp4 s05.mp4 s06.mp4 s07.mp4 s08.mp4 s09.mp4 s10.mp4 blk.mp4

magick -size 2400x320 xc:none -gravity center -font '/System/Library/Fonts/Optima.ttc' -pointsize 120 -fill '#E8DED9' -annotate +0+0 'TEXT  LOVECLUB  FOR  FIRST  DIBS' cta.png
F -t 2.6 -f lavfi -i color=c=0x070506:s=3840x2160:r=24 -framerate 24 -loop 1 -t 2.6 -i "$LOGO" -framerate 24 -loop 1 -t 2.6 -i cta.png \
 -filter_complex "[1:v]negate,scale=1560:-1[wm];[0:v][wm]overlay=(W-w)/2:820:format=auto[a];[a][2:v]overlay=(W-w)/2:1300:format=auto,noise=alls=7:allf=t,fade=t=in:st=0:d=0.3,format=yuv420p" -t 2.6 -r 24 -c:v libx264 -preset medium -crf 18 s11.mp4
printf "file '_rb3_graded.mp4'\nfile 's11.mp4'\n" > rb3_list2.txt
F -f concat -safe 0 -i rb3_list2.txt -c copy _rb3_pic.mp4
rm -f _rb3_graded.mp4 s11.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 _rb3_pic.mp4)
MUSIC="$A/music__20260612_200235.mp3"
DIPSTART=$(echo "$DUR-6.6"|bc -l); DIPEND=$(echo "$DIPSTART+0.25"|bc -l); FOUT=$(echo "$DUR-1.8"|bc -l)
F -i "$MUSIC" -filter_complex "[0:a]aloop=loop=2:size=2000000,atrim=0:${DUR},afade=t=out:st=${FOUT}:d=1.8,volume=0.28:enable='between(t,${DIPSTART},${DIPEND})'[mus];sine=frequency=52:duration=0.35[s0];[s0]afade=t=out:st=0.05:d=0.3,volume=1.6[thump];[mus][thump]amix=inputs=2:duration=first:normalize=0[mix];[mix]loudnorm=I=-14:TP=-1.5:LRA=9,alimiter=limit=0.891:level=disabled,aresample=48000[a]" -map "[a]" -t ${DUR} -c:a aac -b:a 256k _rb3_audio.m4a
F -i _rb3_pic.mp4 -i _rb3_audio.m4a -map 0:v -map 1:a -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -profile:v high -c:a aac -b:a 256k -shortest -movflags +faststart ALMA_LOVE_REBUILD_4K_MASTER.mp4
F -i ALMA_LOVE_REBUILD_4K_MASTER.mp4 -vf scale=1920:1080:flags=lanczos -c:v libx264 -crf 21 -preset medium -movflags +faststart -c:a aac -b:a 192k ALMA_LOVE_REBUILD_WEB1080.mp4
rm -f _rb3_pic.mp4 _rb3_audio.m4a
echo "DUR=${DUR}s"; echo "REBUILD v3 POLISH DONE"
