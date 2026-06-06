#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
ST=../../04_STILLS; TE=../../05_MOTION/_teaser; SEAL=$ST/blender_seal/SOLE_seal_FINAL_1x1.png
VO=../tts_Every_20260606_092122.mp3; RT=../sfx_Deep__20260606_083424.mp3; STK=../../07_AUDIO_VOICE/sfx_A_sin_20260606_075110.mp3
ENCV=(-c:v libx264 -preset medium -pix_fmt yuv420p -r 30 -c:a aac -ar 44100 -ac 2 -shortest)

kb(){ # img dur out
 local fr=$(( $2 * 30 ))
 ffmpeg -y -loglevel error -loop 1 -t "$2" -i "$1" -f lavfi -t "$2" -i anullsrc=channel_layout=stereo:sample_rate=44100 \
  -vf "scale=2600:-1,zoompan=z='min(zoom+0.00045,1.12)':d=${fr}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,format=yuv420p" \
  "${ENCV[@]}" "$3"; }
vid(){ # clip out
 local D; D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$1")
 ffmpeg -y -loglevel error -i "$1" -f lavfi -t "$D" -i anullsrc=channel_layout=stereo:sample_rate=44100 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x0A0A0B,format=yuv420p" \
  -map 0:v -map 1:a "${ENCV[@]}" "$2"; }
card(){ # img dur out
 ffmpeg -y -loglevel error -loop 1 -t "$2" -i "$1" -f lavfi -t "$2" -i anullsrc=channel_layout=stereo:sample_rate=44100 \
  -vf "scale=1920:1080,format=yuv420p" "${ENCV[@]}" "$3"; }

kb   "$ST/S01_open_vault.png" 11 s1.mp4
kb   "$ST/S04_plinth_shadow.png" 9 s2.mp4
vid  "$TE/clip2_vaultdoor.mp4" s3.mp4
vid  "$TE/clip1_openvault.mp4" s4.mp4
kb   "$ST/S05_vault_door.jpg" 8 s5.mp4
kb   "$ST/S09_silhouette_owner.png" 8 s6.mp4
kb   "$ST/S11_long_gallery.png" 8 s7.mp4
kb   "$SEAL" 8 s8.mp4
card "$TE/cardD.png" 6 s9.mp4
printf "file '%s.mp4'\n" s1 s2 s3 s4 s5 s6 s7 s8 s9 > list.txt
ffmpeg -y -loglevel error -f concat -safe 0 -i list.txt -c copy picture.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 picture.mp4)
echo "picture dur: $DUR"
ffmpeg -y -loglevel error -stream_loop -1 -i "$RT" -i "$VO" -i "$STK" -i picture.mp4 \
 -filter_complex "[0:a]volume=0.42,atrim=0:${DUR}[bed];[1:a]adelay=4500|4500,volume=1.7[vo];[2:a]adelay=55000|55000,volume=1.1[stk];[bed][vo][stk]amix=inputs=3:duration=first:dropout_transition=0,volume=1.25[a]" \
 -map 3:v -map "[a]" -c:v copy -c:a aac -shortest SOLE_manifesto_FILM_master.mp4
echo "MASTER built: $(ffprobe -v error -show_entries format=duration -of csv=p=0 SOLE_manifesto_FILM_master.mp4)s"
# cutdowns from master
ffmpeg -y -loglevel error -i SOLE_manifesto_FILM_master.mp4 -t 30 -c copy cut_30s.mp4 2>/dev/null || ffmpeg -y -loglevel error -i SOLE_manifesto_FILM_master.mp4 -t 30 SOLE_cut_30s.mp4
ffmpeg -y -loglevel error -ss 54 -i SOLE_manifesto_FILM_master.mp4 -t 14 SOLE_cut_15s.mp4
ffmpeg -y -loglevel error -ss 60 -i SOLE_manifesto_FILM_master.mp4 -t 6 SOLE_cut_6s.mp4
echo "cutdowns done"; ls -la *.mp4 | awk '{print $5,$9}'
