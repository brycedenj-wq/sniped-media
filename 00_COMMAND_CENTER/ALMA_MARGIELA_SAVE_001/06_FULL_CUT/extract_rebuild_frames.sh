#!/bin/zsh
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
MASTER="ALMA_LOVE_REBUILD_4K_MASTER.mp4"
OUT="qa_frames"; rm -rf "$OUT"; mkdir -p "$OUT"
F(){ ffmpeg -nostdin -loglevel error -y "$@"; }
beats=(
 "beat01_dice_REALmacro_HOOK:0.7"
 "beat02_establish:2.5"
 "beat03_cherry_REALmacro:4.3"
 "beat04_hero:6.5"
 "beat05_incar_DRIVING:9.2"
 "beat06_walk:11.5"
 "beat07_gas:13.8"
 "beat08_plural_club:16.2"
 "beat09_solitaire:18.7"
 "beat10_gamble_card:21.0"
 "beat11_night_payoff:24.0"
 "beat12_endcard:27.5"
)
for b in $beats; do
  name=${b%%:*}; tc=${b#*:}
  F -ss "$tc" -i "$MASTER" -frames:v 1 -vf "scale=1280:-1" "$OUT/${name}.png"
done
F -ss 4.3 -i "$MASTER" -frames:v 1 -vf "crop=in_w/2:in_h/2:in_w/4:in_h/4,scale=1000:-1" "$OUT/beat03_cherry_CROP.png"
F -ss 6.5 -i "$MASTER" -frames:v 1 -vf "crop=in_w/1.8:in_h/1.4:in_w/4.5:in_h/5,scale=1000:-1" "$OUT/beat04_hero_CROP.png"
magick montage "$OUT"/beat0*.png "$OUT"/beat1[0-2]*.png -tile 4x3 -geometry 360x203+3+3 -background black "$OUT/_CONTACT_SHEET.png" 2>/dev/null || true
echo "FRAMES: $(ls "$OUT"/*.png | wc -l | tr -d ' ')"