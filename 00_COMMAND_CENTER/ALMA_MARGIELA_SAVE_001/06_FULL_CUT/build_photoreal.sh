#!/bin/zsh
# ALMA LOVE CLUB · PHOTOREAL MASTER (level-up method). Seedance 2.0 photoreal beats (Topaz 4K) + real product macros.
# LIGHT grade only: the Seedance footage already carries grain/halation/film look. Just unify (low LUT + slight warm + vignette + faint grain so the macros match).
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
P=../HIGGS_LEVELUP/photoreal/topaz; A=../05_AUDIO; M=../03_REAL_MACROS
LUT="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT/ALMA_LOVE_signature_look_v1.cube"
LOGO="/Users/sniper/.claude/uploads/3d92356b-5ad9-4a03-99f9-fe6e47b3f84d/c240fb49-IMG_3366.png"
F() { ffmpeg -nostdin -loglevel error -y "$@"; }
SCALE="scale=3840:2160:force_original_aspect_ratio=increase:flags=lanczos,crop=3840:2160,setsar=1,fps=24"
LUTB="split=2[lo][ll];[ll]lut3d='${LUT}':interp=tetrahedral[lg];[lo][lg]blend=all_mode=normal:all_opacity=0.16"
# SEED: light unify (the clip is already photoreal). MAC: real macro + a touch of grain to match the Seedance grain.
seg() {
  local extra=""
  case "$5" in
    MAC)  extra=",eq=brightness=-0.02:contrast=1.03:saturation=1.02,noise=alls=5:allf=t" ;;
    NIGHT) extra=",hue=h=-9,eq=saturation=1.05:contrast=1.02" ;;   # night 30 -> ~21 (real on-body band)
    *)    extra=",hue=h=-7,eq=saturation=1.04:contrast=1.02" ;;     # on-body 26 -> ~19 = MATCH the real on-body product (measured 18-22); mild, skin-safe
  esac
  F -ss "$2" -t "$3" -i "$1" -vf "${SCALE},colorbalance=rm=0.02:bm=-0.02,${LUTB}${extra},vignette=PI/12,format=yuv420p" -an -c:v libx264 -preset medium -crf 18 -r 24 "$4"
}
DICE=$M/MACRO_dice_2810.mp4; CHERRY=$M/MACRO_cherry_2812.mp4
# CORRECTED ORDER: world -> character -> motion -> product macros woven in (no cold product-macro open)
seg $P/PR_establish.mp4 0.2 2.6  s01.mp4 SEED               # 1 establish WIDE (the world)
seg $P/PR_hero.mp4      0.3 2.8  s02.mp4 SEED               # 2 hero (character reveal)
seg $P/PR_walk.mp4      0.3 2.2  s03.mp4 SEED               # 3 walk (motion)
seg $DICE              1.0 1.3  s04.mp4 MAC                 # 4 dice macro (product insert, now contextualized)
seg $P/PR_gas.mp4       0.4 2.4  s05.mp4 SEED               # 5 gas
seg $CHERRY            1.2 1.3  s06.mp4 MAC                 # 6 cherry macro (product insert)
seg $P/PR_plural.mp4    0.4 2.4  s07.mp4 SEED               # 7 club
seg $P/PR_solit.mp4     0.4 2.6  s08.mp4 SEED               # 8 gamble action
seg $P/PR_night.mp4     0.3 4.2  s10.mp4 NIGHT              # 9 night payoff

magick -size 3840x2160 xc:'#0A0708' -gravity center -font '/System/Library/Fonts/Supplemental/Didot.ttc' -pointsize 224 -fill '#C23A34' -interline-spacing 54 -annotate +0+0 'LOVE IS A GAMBLE.' card_gamble.png
F -loop 1 -t 1.6 -i card_gamble.png -vf "noise=alls=6:allf=t,fade=t=in:st=0:d=0.3,fade=t=out:st=1.3:d=0.3,format=yuv420p" -r 24 -c:v libx264 -preset medium -crf 18 s09.mp4
F -t 0.18 -f lavfi -i color=c=0x070506:s=3840x2160:r=24 -c:v libx264 -preset medium -crf 18 blk.mp4

printf "file 's01.mp4'\nfile 's02.mp4'\nfile 's03.mp4'\nfile 's04.mp4'\nfile 's05.mp4'\nfile 's06.mp4'\nfile 's07.mp4'\nfile 's08.mp4'\nfile 'blk.mp4'\nfile 's09.mp4'\nfile 's10.mp4'\n" > pr_list.txt
F -f concat -safe 0 -i pr_list.txt -c copy _pr_pic_body.mp4
rm -f s01.mp4 s02.mp4 s03.mp4 s04.mp4 s05.mp4 s06.mp4 s07.mp4 s08.mp4 s09.mp4 s10.mp4 blk.mp4

magick -size 2600x320 xc:none -gravity center -font '/System/Library/Fonts/Optima.ttc' -pointsize 116 -fill '#E8DED9' -annotate +0+0 'TEXT  LOVECLUB  TO  (850) 636-1785' cta.png
F -t 2.6 -f lavfi -i color=c=0x070506:s=3840x2160:r=24 -framerate 24 -loop 1 -t 2.6 -i "$LOGO" -framerate 24 -loop 1 -t 2.6 -i cta.png \
 -filter_complex "[1:v]negate,scale=1560:-1[wm];[0:v][wm]overlay=(W-w)/2:820:format=auto[a];[a][2:v]overlay=(W-w)/2:1300:format=auto,noise=alls=6:allf=t,fade=t=in:st=0:d=0.3,format=yuv420p" -t 2.6 -r 24 -c:v libx264 -preset medium -crf 18 s11.mp4
printf "file '_pr_pic_body.mp4'\nfile 's11.mp4'\n" > pr_list2.txt
F -f concat -safe 0 -i pr_list2.txt -c copy _pr_pic.mp4
rm -f _pr_pic_body.mp4 s11.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 _pr_pic.mp4)
MUSIC="$A/music__20260612_200235.mp3"
DIPSTART=$(echo "$DUR-6.6"|bc -l); DIPEND=$(echo "$DIPSTART+0.25"|bc -l); FOUT=$(echo "$DUR-1.8"|bc -l)
F -i "$MUSIC" -filter_complex "[0:a]aloop=loop=2:size=2000000,atrim=0:${DUR},afade=t=out:st=${FOUT}:d=1.8,volume=0.28:enable='between(t,${DIPSTART},${DIPEND})'[mus];sine=frequency=52:duration=0.35[s0];[s0]afade=t=out:st=0.05:d=0.3,volume=1.6[thump];[mus][thump]amix=inputs=2:duration=first:normalize=0[mix];[mix]loudnorm=I=-14:TP=-1.5:LRA=9,alimiter=limit=0.891:level=disabled,aresample=48000[a]" -map "[a]" -t ${DUR} -c:a aac -b:a 256k _pr_audio.m4a
F -i _pr_pic.mp4 -i _pr_audio.m4a -map 0:v -map 1:a -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -profile:v high -c:a aac -b:a 256k -shortest -movflags +faststart ALMA_LOVE_PHOTOREAL_4K_MASTER.mp4
F -i ALMA_LOVE_PHOTOREAL_4K_MASTER.mp4 -vf scale=1920:1080:flags=lanczos -c:v libx264 -crf 21 -preset medium -movflags +faststart -c:a aac -b:a 192k ALMA_LOVE_PHOTOREAL_WEB1080.mp4
rm -f _pr_pic.mp4 _pr_audio.m4a
echo "DUR=${DUR}s"; ffprobe -v error -show_entries stream=width,height -of csv=p=0 ALMA_LOVE_PHOTOREAL_4K_MASTER.mp4 2>/dev/null | head -1
echo "PHOTOREAL MASTER DONE"
