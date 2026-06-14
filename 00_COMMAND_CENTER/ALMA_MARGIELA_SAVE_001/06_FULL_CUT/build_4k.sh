#!/bin/zsh
# ALMA LOVE CLUB · 4K MASTER v2 (3840x2160) · whole-film quality lift to the 9-floor.
# Addresses every harness dimension:
#  GARMENT: in-car interior dropped (moderation wall) -> exterior product-worn beat; cherry stem muted; anti-coral; reframe plural+hood; mirror de-pinked.
#  GRADE:   per-beat warmth rebalance (warm cool hero/plural, tame over-warm solitaire, darken+integrate high-key product macros).
#  EDIT:    re-cut to ~1.7s ASL, scale-shock TIGHT hook (dice), hard wide-to-tight grammar, no wide-to-wide head, no gas-to-incar sag.
#  BRAND:   "LOVE IS A GAMBLE." terminal period, truer card red, larger CTA.
#  STATUS:  in-car now matches the lead, open on a loaded symbol not the empty street, mirror reads brand-red.
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
V=../02_VIDEO_TESTS; R=../07_REGEN/video; A=../05_AUDIO
LUT="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT/ALMA_LOVE_signature_look_v1.cube"
LOGO="/Users/sniper/.claude/uploads/3d92356b-5ad9-4a03-99f9-fe6e47b3f84d/c240fb49-IMG_3366.png"
CHERRY4K="$R/PROD_cherry_v2_4k.mp4"   # v2 cherry product i2v (muted gray-green stem), AI-upscaled 4K
DICE4K="$R/PROD_dice_4k.mp4"          # dice product i2v (passed), AI-upscaled 4K
BYCAR4K="$R/INCAR_drive_4k.mp4"       # NEW in-car DRIVING beat, cherry-print top worn (nano_banana non-pro bypass), AI-upscaled 4K. Standing fallback: BYCAR_product_4k.mp4
F() { ffmpeg -nostdin -loglevel error -y "$@"; }
SCALE="scale=3840:2160:force_original_aspect_ratio=increase:flags=lanczos,crop=3840:2160,fps=24"
LUTB="split=2[lo][ll];[ll]lut3d='${LUT}':interp=tetrahedral[lg];[lo][lg]blend=all_mode=normal:all_opacity=0.30"
# grade roles. colorbalance rm/bm = per-beat white balance (warm/cool). extra = role look.
# $1 src  $2 ss  $3 dur  $4 rm  $5 bm  $6 ROLE  $7 out  [$8 precrop]
seg() {
  local extra="" precrop=""
  case "$6" in
    GOLD)   extra=",hue=h=-16,colorbalance=gm=-0.04:gs=-0.02" ;;
    GOLD2)  extra=",hue=h=-24,eq=saturation=1.06,colorbalance=gm=-0.05:gs=-0.03" ;; # stronger anti-coral (plural beat measured 25.6deg)
    DAYRED) extra=",hue=h=-13,colorbalance=gm=-0.03:gs=-0.02" ;;          # on-body day: garment off the coral ceiling
    MIRROR) extra=",hue=h=-18,eq=saturation=1.12,colorbalance=gm=-0.04" ;; # de-pink the product-in-mirror to brand red
    NIGHT)  extra=",eq=gamma=1.06:brightness=0.03,hue=h=-12,colorbalance=gm=-0.03" ;;
    PROD)   extra=",eq=brightness=-0.06:contrast=1.07:saturation=1.10,unsharp=lx=5:ly=5:la=0.5,hue=h=-6" ;; # darken+integrate macros, push print true-red
    *)      extra="" ;;
  esac
  [ -n "$8" ] && precrop="$8,"
  F -ss "$2" -t "$3" -i "$1" -vf "${precrop}${SCALE},colorbalance=rm=$4:bm=$5,${LUTB}${extra},format=yuv420p" -an -c:v libx264 -preset medium -crf 18 -r 24 "$7"
}
# ===== NEW EDIT ORDER (scale-shock, ~2.0s ASL, day->night, ~30s brief) =====
# 1 HOOK: dice macro TIGHT (loaded gamble symbol, hard punch open)
seg $DICE4K                           1.0  1.3  0.04  -0.04   PROD   s01.mp4
# 2 hero WIDE (reveal character in the world; tight->wide shock) + WARM (was measuring cool). earned hold.
seg $V/B01_kling_c94b30be.mp4         0    3.2  0.10  -0.10   DAYRED s02.mp4
# 3 walk MED (motion)
seg $V/B03_walk_b41fac11.mp4          0.5  1.6  0.06  -0.06   DAYRED s03.mp4
# 4 cherry macro TIGHT (product symbol; wide->tight shock) muted stem
seg $CHERRY4K                         1.4  1.4  0.05  -0.05   PROD   s04.mp4
# 5 in-car DRIVING MED (the lead at the wheel in the real cherry-print top; replaces wrong-garment tank). Later window = closer/clearer push-in.
seg $BYCAR4K                          2.4  2.0  0.07  -0.07   DAYRED s05.mp4
# 6 gas WIDE tableau (earned hold)
seg $V/B06_gas_kling_ba948b6e.mp4     0    3.2  0.02  -0.02   GOLD   s06.mp4
# 7 plural club MED (cards) reframed center off the bottom cherries + strong anti-coral (was 25.6deg)
seg $R/PLURAL_8568c446.mp4            0    1.7  0.06  -0.06   GOLD2  s07.mp4 "crop=iw*0.60:ih*0.66:iw*0.20:ih*0.0"
# 8 mirror product TIGHT, de-pinked to brand red
seg $V/PROD_mirror_a7638a45.mp4       0.4  1.4  0.02  -0.02   MIRROR s08.mp4
# 9 solitaire MED (gamble action) tamed warmth (was +26 over median)
seg $V/B10_solitaire_f028ce60.mp4     0    2.0 -0.12   0.14   GOLD   s09.mp4
# 10 hood product TIGHT, reframed to the top piece (right-cup cherry), drop wrong bottom cherry
seg $V/PROD_hood_ab35eaac.mp4         0.4  1.4  0.01  -0.01   GOLD   s10.mp4 "crop=iw*0.74:ih*0.52:iw*0.13:ih*0.05"
# 11 establishing WIDE (world breath before the payoff)
seg $R/ESTAB_47655342.mp4             0.3  2.0  0.03  -0.03   STD    s11.mp4
# 13 night finale WIDE (earned hold payoff)
seg $V/B19_night_kling_b0aecae7.mp4   0    4.4 -0.084  0.084  NIGHT  s13.mp4

# 12 statement card at 4K: "LOVE IS A GAMBLE." (terminal period) truer brand red, 1.5s
magick -size 3840x2160 xc:'#0A0708' -gravity center -font '/System/Library/Fonts/Supplemental/Didot.ttc' -pointsize 224 -fill '#C23A34' -interline-spacing 54 -annotate +0+0 'LOVE IS A GAMBLE.' card_gamble.png
F -loop 1 -t 1.5 -i card_gamble.png -vf "noise=alls=7:allf=t,fade=t=in:st=0:d=0.3,fade=t=out:st=1.2:d=0.3,format=yuv420p" -r 24 -c:v libx264 -preset medium -crf 18 s12.mp4
F -t 0.18 -f lavfi -i color=c=0x070506:s=3840x2160:r=24 -c:v libx264 -preset medium -crf 18 blk.mp4

printf "file 's01.mp4'\nfile 's02.mp4'\nfile 's03.mp4'\nfile 's04.mp4'\nfile 's05.mp4'\nfile 's06.mp4'\nfile 's07.mp4'\nfile 's08.mp4'\nfile 's09.mp4'\nfile 's10.mp4'\nfile 's11.mp4'\nfile 'blk.mp4'\nfile 's12.mp4'\nfile 's13.mp4'\n" > clist4k.txt
F -f concat -safe 0 -i clist4k.txt -c copy _4k_body.mp4

# Global finish at 4K: green-recovery, halation, fine grain, soften, vignette
GREENFIX="colorbalance=rm=-0.01:gm=0.05:bm=-0.03:gh=0.04:gs=0.02"
HAL="split=2[b][g];[g]curves=all='0/0 0.76/0 1/1',gblur=sigma=28,colorbalance=rm=0.03[glow];[b][glow]blend=all_mode=screen:all_opacity=0.20,format=yuv420p"
F -i _4k_body.mp4 -vf "${GREENFIX},${HAL},noise=alls=9:allf=t,unsharp=lx=7:ly=7:la=-0.40,vignette=PI/11,format=yuv420p" -c:v libx264 -preset medium -crf 19 -r 24 _4k_graded.mp4
rm -f _4k_body.mp4 s01.mp4 s02.mp4 s03.mp4 s04.mp4 s05.mp4 s06.mp4 s07.mp4 s08.mp4 s09.mp4 s10.mp4 s11.mp4 s12.mp4 s13.mp4 blk.mp4

# End card at 4K (real wordmark + larger CTA)
magick -size 2400x320 xc:none -gravity center -font '/System/Library/Fonts/Optima.ttc' -pointsize 120 -fill '#E8DED9' -annotate +0+0 'TEXT  LOVECLUB  FOR  FIRST  DIBS' cta.png
F -t 2.6 -f lavfi -i color=c=0x070506:s=3840x2160:r=24 -framerate 24 -loop 1 -t 2.6 -i "$LOGO" -framerate 24 -loop 1 -t 2.6 -i cta.png \
 -filter_complex "[1:v]negate,scale=1560:-1[wm];[0:v][wm]overlay=(W-w)/2:820:format=auto[a];[a][2:v]overlay=(W-w)/2:1300:format=auto,noise=alls=7:allf=t,fade=t=in:st=0:d=0.3,format=yuv420p" -t 2.6 -r 24 -c:v libx264 -preset medium -crf 18 s14.mp4
printf "file '_4k_graded.mp4'\nfile 's14.mp4'\n" > clist4k2.txt
F -f concat -safe 0 -i clist4k2.txt -c copy _4k_pic.mp4
rm -f _4k_graded.mp4 s14.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 _4k_pic.mp4)

# Audio: -14 LUFS, true-peak limited to -1 dBTP
MUSIC="$A/music__20260612_200235.mp3"
DIPSTART=$(echo "$DUR-6.6"|bc -l); DIPEND=$(echo "$DIPSTART+0.25"|bc -l); FOUT=$(echo "$DUR-1.8"|bc -l)
F -i "$MUSIC" -filter_complex "[0:a]aloop=loop=2:size=2000000,atrim=0:${DUR},afade=t=out:st=${FOUT}:d=1.8,volume=0.28:enable='between(t,${DIPSTART},${DIPEND})'[mus];sine=frequency=52:duration=0.35[s0];[s0]afade=t=out:st=0.05:d=0.3,volume=1.6[thump];[mus][thump]amix=inputs=2:duration=first:normalize=0[mix];[mix]loudnorm=I=-14:TP=-1.5:LRA=9,alimiter=limit=0.891:level=disabled,aresample=48000[a]" -map "[a]" -t ${DUR} -c:a aac -b:a 256k _4k_audio.m4a

# Tuned delivery encode (not the 209Mbps archival weight): CRF 20, high profile, faststart
F -i _4k_pic.mp4 -i _4k_audio.m4a -map 0:v -map 1:a -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -profile:v high -c:a aac -b:a 256k -shortest -movflags +faststart ALMA_LOVE_FINAL_4K_MASTER.mp4
F -i ALMA_LOVE_FINAL_4K_MASTER.mp4 -vf scale=1920:1080:flags=lanczos -c:v libx264 -crf 21 -preset medium -movflags +faststart -c:a aac -b:a 192k ALMA_LOVE_FINAL_4K_WEB1080.mp4
rm -f _4k_pic.mp4 _4k_audio.m4a
echo "DUR=${DUR}s"
ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 ALMA_LOVE_FINAL_4K_MASTER.mp4 2>/dev/null | head -1
du -h ALMA_LOVE_FINAL_4K_MASTER.mp4 ALMA_LOVE_FINAL_4K_WEB1080.mp4 | cut -f1,2
echo "4K BUILD v2 DONE"
