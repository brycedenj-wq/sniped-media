#!/bin/zsh
# ALMA LOVE 9:16 vertical direction master. Free post: per-shot reframe of graded beats + gamble card + CTA end card + audio remaster. NO new generation.
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
A=../05_AUDIO
LOGO="/Users/sniper/.claude/uploads/3d92356b-5ad9-4a03-99f9-fe6e47b3f84d/c240fb49-IMG_3366.png"
F() { ffmpeg -nostdin -loglevel error -y "$@"; }
GR="noise=alls=9:allf=t,format=yuv420p"
# per-shot vertical reframe: crop 607x1080 at chosen X from the graded 1920x1080 beat, scale to 1080x1920
# args: seg ss dur cropX out
rf() { F -ss "$2" -t "$3" -i "$1" -vf "crop=607:1080:$4:0,scale=1080:1920:flags=lanczos,${GR}" -an -c:v libx264 -crf 17 -r 24 "$5"; }
#    seg     ss   dur  X
rf m10.mp4   0.2  1.6  656  v01.mp4   # NIGHT headlights = hook open
rf m09.mp4   0.2  1.0  656  v03.mp4   # dice macro
rf m08.mp4   0.3  1.3  520  v04.mp4   # solitaire cards (subject left)
rf m04.mp4   0.2  1.0  656  v05.mp4   # cherry macro
rf m05.mp4   0.3  1.6  820  v06.mp4   # gas station (subject right)
rf m03.mp4   0.4  1.4  656  v07.mp4   # walk
rf m02.mp4   0.3  1.0  656  v08.mp4   # product hood
rf m07.mp4   0.3  1.0  480  v09.mp4   # product mirror (left)
rf m01.mp4   0.2  1.3  656  v10.mp4   # noon establish (now mid)
rf m10.mp4   1.4  2.2  656  v11.mp4   # NIGHT payoff hold

# Gamble card (already 1080x1920) -> 1.2s clip with grain + slow fade
F -loop 1 -t 1.3 -i vert/CARD_gamble_v.png -vf "${GR},fade=t=in:st=0:d=0.2,fade=t=out:st=1.0:d=0.3" -r 24 -c:v libx264 -crf 17 v02.mp4

# Designed vertical END CARD: real wordmark (negated white) centered upper, CTA strip below, near-black + grain
F -t 2.4 -f lavfi -i color=c=0x0A0708:s=1080x1920:r=24 -framerate 24 -loop 1 -t 2.4 -i "$LOGO" -framerate 24 -loop 1 -t 2.4 -i vert/CTA_strip.png \
 -filter_complex "[1:v]negate,scale=760:-1[wm];[0:v][wm]overlay=(W-w)/2:820:format=auto[a];[a][2:v]overlay=(W-w)/2:1040:format=auto,noise=alls=7:allf=t,fade=t=in:st=0:d=0.3,format=yuv420p" \
 -t 2.4 -r 24 -c:v libx264 -crf 17 vEND.mp4

# Concat picture
printf "file 'v01.mp4'\nfile 'v02.mp4'\nfile 'v03.mp4'\nfile 'v04.mp4'\nfile 'v05.mp4'\nfile 'v06.mp4'\nfile 'v07.mp4'\nfile 'v08.mp4'\nfile 'v09.mp4'\nfile 'v10.mp4'\nfile 'v11.mp4'\nfile 'vEND.mp4'\n" > vlist.txt
F -f concat -safe 0 -i vlist.txt -c copy _vert_pic.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 _vert_pic.mp4)

# AUDIO: music remastered to -14 LUFS + a low open transient (sub thump) + a dip before the night payoff (last ~2.6s)
MUSIC="$A/music__20260612_200235.mp3"
DIPSTART=$(echo "$DUR-4.6"|bc -l)   # the v11 night payoff begins ~4.6s before end (2.2 payoff + 2.4 endcard)
F -i "$MUSIC" -filter_complex "\
[0:a]atrim=0:${DUR},afade=t=out:st=$(echo "$DUR-1.8"|bc -l):d=1.8,volume=enable='between(t,${DIPSTART},$(echo "${DIPSTART}+0.25"|bc -l))':volume=0.25[mus];\
sine=frequency=52:duration=0.35[s];[s]afade=t=out:st=0.05:d=0.3,volume=3.0[thump];\
[mus][thump]amix=inputs=2:duration=first:weights='1 0.5':normalize=0,loudnorm=I=-14:TP=-1.0:LRA=9[a]" \
 -t ${DUR} -c:a aac -b:a 256k -vn _vert_audio.m4a

F -i _vert_pic.mp4 -i _vert_audio.m4a -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest -movflags +faststart ALMA_LOVE_VERTICAL_v3.mp4

# 15s vertical hook cut (first ~13.5s, ending on payoff+endcard) for virality
F -i ALMA_LOVE_VERTICAL_v3.mp4 -t 15 -c:v libx264 -crf 20 -c:a aac -b:a 192k -movflags +faststart ALMA_LOVE_VERTICAL_15s_HOOK.mp4

echo "DUR=$DUR"
ffprobe -v error -show_entries format=duration:stream=width,height -of default=noprint_wrappers=1 ALMA_LOVE_VERTICAL_v3.mp4 2>/dev/null | head -4
echo "LUFS check:"; ffmpeg -nostdin -i ALMA_LOVE_VERTICAL_v3.mp4 -af ebur128 -f null - 2>&1 | grep -A1 "Integrated" | tail -2
echo "VERTICAL BUILD DONE"
