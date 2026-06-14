# AUDIO LOUDNESS NOTES · Alma Love Club 16:9 final master
Asset: ALMA_LOVE_FINAL_16x9_MASTER.mp4 (34.4s).

## Measured (final, ebur128 peak=true)
- Integrated loudness: -15.2 LUFS
- True peak: -2.5 dBFS (no inter-sample clipping)
- Loudness range: ~5.2 LU (real structure, not flat-limited)
- Codec: AAC 256k, 48 kHz

## Targets and compliance
- Social/web target: -14 LUFS, ceiling -1 dBTP. Result -15.2 LUFS / -2.5 dBTP = compliant (1.2 LU under target loudness, safely under the peak ceiling).

## History (the one fixed blocker)
- First mux measured TRUE PEAK +1.7 dBFS (max sample 0.0 dB) = inter-sample clipping. The final QA judge flagged this as the single send-blocker (do not ship to a paying client at >0 dBTP).
- Re-mastered: music + open transient + a level dip before the night payoff -> loudnorm I=-14 TP=-1.5 -> alimiter limit=0.891 (a hard true-peak ceiling near -1 dBTP) -> 48 kHz resample. Result: -2.5 dBTP, clean.

## Music
- Owned, ElevenLabs, commercial license (instrumental). Backup: Higgsfield sonilo track.
- A 52 Hz sub-transient sits on the opening cut (rewards an un-mute). A volume dip precedes the night payoff. The film reads with the music muted (deadpan grammar), per doctrine.

## If re-exporting for broadcast/other surface
- Keep the true-peak ceiling at -1 dBTP. For broadcast (-23 / -24 LUFS) re-run loudnorm to that target and re-limit. For IG/TikTok the current -15.2 LUFS is in band.
