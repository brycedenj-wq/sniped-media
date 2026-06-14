# Gridiron Royale · numeric thresholds (fixed before code)

- Frame budget: 60 fps desktop, >=30 fps phone-class; logic step fixed 60 Hz.
- devicePixelRatio cap: 1.5.
- Draw calls worst-case scene: <= 150 (crowd, confetti, pickups instanced; one mesh per defender capped at 12 active).
- Per-frame heap allocations in the loop: 0 (reused vectors, preallocated pools).
- Entities: defenders <= 12, confetti 600 (one InstancedMesh), crowd 1200 (one InstancedMesh).
- Input tolerance: juke untouchable window 0.4s; spin break radius 2.0u; tackle radius 1.3u (player hitbox 0.8x visual).
- Match: 120s clock, 4 downs, TD = 7 pts, golden ball = +3 pts, MVP threshold 21.
- Parameter consistency check: drive 80u at base 10 u/s = 8s per drive uncontested; 120s allows ~10 drives; 21 points (3 TDs) reachable by wave 3 defender speed (10.4 u/s) < player sprint 15 u/s. Reachable.
- Asset budget: zip < 25 MiB; audio total < 4 MiB target.
- Audio mix: music -18 dBFS, SFX -10 to -12 dBFS, true peak <= -3 dBFS (gain-staged in code: music 0.35, SFX 0.8 relative).
