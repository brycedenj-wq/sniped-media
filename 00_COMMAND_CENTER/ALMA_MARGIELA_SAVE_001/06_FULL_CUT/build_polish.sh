#!/bin/zsh
# ALMA LOVE CLUB 16:9 POLISH PASS. Same beats, no new generation, no credits. Fixes: on-body true-red, clean bright product macros, card presence, plural trim, lighter grain.
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
V=../02_VIDEO_TESTS; M=../03_REAL_MACROS; R=../07_REGEN/video; A=../05_AUDIO
LUT="/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/05_EXPORTS/DELIVERABLES/ALMA_LOVE_BRAND_KIT/preset/ALMA_LOVE_signature_look_v1.cube"
LOGO="/Users/sniper/.claude/uploads/3d92356b-5ad9-4a03-99f9-fe6e47b3f84d/c240fb49-IMG_3366.png"
F() { ffmpeg -nostdin -loglevel error -y "$@"; }
SCALE="scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24"
LUTB="split=2[lo][ll];[ll]lut3d='${LUT}':interp=tetrahedral[lg];[lo][lg]blend=all_mode=normal:all_opacity=0.30"
# STD: WB+LUT. GOLD: +anti-coral (on-body true-red). NIGHT: lifted. MAC: CLEAN + BRIGHT product detail (lift, clarity, warm to match EVOTO), and a lighter local finish.
seg() {
  local extra=""
  case "$6" in
    GOLD)  extra=",hue=h=-16,colorbalance=gm=-0.04:gs=-0.02" ;;
    NIGHT) extra=",eq=gamma=1.06:brightness=0.03" ;;
    MAC)   extra=",eq=brightness=0.07:contrast=1.07:saturation=1.06,unsharp=lx=3:ly=3:la=0.6,hue=h=-8" ;;
    *)     extra="" ;;
  esac
  F -ss "$2" -t "$3" -i "$1" -vf "${SCALE},colorbalance=rm=$4:bm=$5,${LUTB}${extra},format=yuv420p" -an -c:v libx264 -crf 16 -r 24 "$7"
}
seg $R/ESTAB_47655342.mp4             0.3  2.5  0.03  -0.03   STD    c01.mp4
seg $V/B01_kling_c94b30be.mp4         0    3.0  0.04  -0.04   STD    c02.mp4
seg $V/PROD_hood_ab35eaac.mp4         0.4  2.0  0.01  -0.01   GOLD   c03.mp4
seg $V/B03_walk_b41fac11.mp4          0.5  2.6  0.02  -0.02   STD    c04.mp4
seg $M/MACRO_cherry_2812.mp4          0    2.0  0.02  -0.02   MAC    c05.mp4   # CLEAN bright cherry product detail
seg $R/PLURAL_8568c446.mp4            0    1.6 -0.05   0.05   GOLD   c06.mp4   # trimmed 2.2 -> 1.6 (was lingering)
seg $V/B06_gas_kling_ba948b6e.mp4     0    3.0 -0.016  0.016  GOLD   c07.mp4
seg $R/INCAR_61763d8d.mp4             0.8  2.5  0.0    0.0    STD    c08.mp4
seg $V/PROD_mirror_a7638a45.mp4       0.4  2.0 -0.052  0.052  GOLD   c09.mp4
seg $V/B10_solitaire_f028ce60.mp4     0    2.6 -0.10   0.10   GOLD   c10.mp4
seg $M/MACRO_dice_2810.mp4            0    1.8  0.02  -0.02   MAC    c11.mp4   # CLEAN bright dice product detail
seg $V/B19_night_kling_b0aecae7.mp4   0    4.0 -0.084  0.084  NIGHT  c13.mp4

# Statement card: BRIGHTER brand red + bigger + longer hold (1.7s) for presence
magick -size 1920x1080 xc:'#0A0708' -gravity center -font '/System/Library/Fonts/Supplemental/Didot.ttc' -pointsize 118 -fill '#D6463A' -interline-spacing 28 -annotate +0+0 'LOVE IS A GAMBLE' card_gamble.png
F -loop 1 -t 1.7 -i card_gamble.png -vf "noise=alls=7:allf=t,fade=t=in:st=0:d=0.3,fade=t=out:st=1.35:d=0.35,format=yuv420p" -r 24 -c:v libx264 -crf 16 c12.mp4
F -t 0.20 -f lavfi -i color=c=0x070506:s=1920x1080:r=24 -c:v libx264 -crf 16 blk.mp4

printf "file 'c01.mp4'\nfile 'c02.mp4'\nfile 'c03.mp4'\nfile 'c04.mp4'\nfile 'c05.mp4'\nfile 'c06.mp4'\nfile 'c07.mp4'\nfile 'c08.mp4'\nfile 'c09.mp4'\nfile 'c10.mp4'\nfile 'c11.mp4'\nfile 'blk.mp4'\nfile 'c12.mp4'\nfile 'c13.mp4'\n" > clist.txt
F -f concat -safe 0 -i clist.txt -c copy _p_body.mp4

# Global finish: LIGHTER grain (alls 9), lighter vignette (cleaner macros), keep halation + soften + green-recovery
GREENFIX="colorbalance=rm=-0.01:gm=0.05:bm=-0.03:gh=0.04:gs=0.02"
HAL="split=2[b][g];[g]curves=all='0/0 0.76/0 1/1',gblur=sigma=14,colorbalance=rm=0.03[glow];[b][glow]blend=all_mode=screen:all_opacity=0.20,format=yuv420p"
F -i _p_body.mp4 -vf "${GREENFIX},${HAL},noise=alls=9:allf=t,unsharp=lx=5:ly=5:la=-0.40,vignette=PI/11,format=yuv420p" -c:v libx264 -crf 18 -r 24 _p_graded.mp4
rm -f _p_body.mp4 c01.mp4 c02.mp4 c03.mp4 c04.mp4 c05.mp4 c06.mp4 c07.mp4 c08.mp4 c09.mp4 c10.mp4 c11.mp4 c12.mp4 c13.mp4 blk.mp4

# Clean end card (real wordmark + CTA)
magick -size 1080x130 xc:none -gravity center -font '/System/Library/Fonts/Optima.ttc' -pointsize 40 -fill '#E8DED9' -annotate +0+0 'TEXT  LOVECLUB  FOR  FIRST  DIBS' cta.png
F -t 2.6 -f lavfi -i color=c=0x070506:s=1920x1080:r=24 -framerate 24 -loop 1 -t 2.6 -i "$LOGO" -framerate 24 -loop 1 -t 2.6 -i cta.png \
 -filter_complex "[1:v]negate,scale=860:-1[wm];[0:v][wm]overlay=(W-w)/2:430:format=auto[a];[a][2:v]overlay=(W-w)/2:640:format=auto,noise=alls=7:allf=t,fade=t=in:st=0:d=0.3,format=yuv420p" -t 2.6 -r 24 -c:v libx264 -crf 16 c14.mp4
printf "file '_p_graded.mp4'\nfile 'c14.mp4'\n" > clist2.txt
F -f concat -safe 0 -i clist2.txt -c copy _p_pic.mp4
rm -f _p_graded.mp4 c14.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 _p_pic.mp4)

# Audio: -14 LUFS, true-peak limited to -1 dBTP (the proven safe master)
MUSIC="$A/music__20260612_200235.mp3"
DIPSTART=$(echo "$DUR-6.6"|bc -l); DIPEND=$(echo "$DIPSTART+0.25"|bc -l); FOUT=$(echo "$DUR-1.8"|bc -l)
F -i "$MUSIC" -filter_complex "[0:a]aloop=loop=2:size=2000000,atrim=0:${DUR},afade=t=out:st=${FOUT}:d=1.8,volume=0.28:enable='between(t,${DIPSTART},${DIPEND})'[mus];sine=frequency=52:duration=0.35[s0];[s0]afade=t=out:st=0.05:d=0.3,volume=1.6[thump];[mus][thump]amix=inputs=2:duration=first:normalize=0[mix];[mix]loudnorm=I=-14:TP=-1.5:LRA=9,alimiter=limit=0.891:level=disabled,aresample=48000[a]" -map "[a]" -t ${DUR} -c:a aac -b:a 256k _p_audio.m4a

F -i _p_pic.mp4 -i _p_audio.m4a -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest -movflags +faststart ALMA_LOVE_FINAL_16x9_MASTER.mp4
F -i ALMA_LOVE_FINAL_16x9_MASTER.mp4 -vf scale=1280:720 -c:v libx264 -crf 23 -preset medium -movflags +faststart -c:a aac -b:a 160k ALMA_LOVE_FINAL_16x9_WEB.mp4
rm -f _p_pic.mp4 _p_audio.m4a
echo "DUR=${DUR}s"; ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 ALMA_LOVE_FINAL_16x9_MASTER.mp4 2>/dev/null | head -1
du -h ALMA_LOVE_FINAL_16x9_MASTER.mp4 ALMA_LOVE_FINAL_16x9_WEB.mp4 | cut -f1,2
echo "POLISH DONE"
