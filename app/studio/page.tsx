"use client";

import { Player } from "@remotion/player";
import {
  ChronixelScene01,
  CHRONIXEL_DURATION_IN_FRAMES,
  CHRONIXEL_FPS,
  CHRONIXEL_HEIGHT,
  CHRONIXEL_WIDTH,
} from "@/video/ChronixelScene01";

// Previews the Remotion composition inside the Next.js app via @remotion/player.
// The same component is rendered headlessly by the Remotion CLI (see video/Root.tsx).
export default function StudioPage() {
  return (
    <main
      style={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 16,
        padding: 24,
        backgroundColor: "#000",
        color: "#fff",
      }}
    >
      <h1 style={{ fontSize: 24, fontWeight: 600 }}>Remotion preview — ChronixelScene01</h1>
      <Player
        component={ChronixelScene01}
        durationInFrames={CHRONIXEL_DURATION_IN_FRAMES}
        fps={CHRONIXEL_FPS}
        compositionWidth={CHRONIXEL_WIDTH}
        compositionHeight={CHRONIXEL_HEIGHT}
        controls
        loop
        style={{ height: "80vh", maxHeight: 854, aspectRatio: "9 / 16" }}
      />
    </main>
  );
}
