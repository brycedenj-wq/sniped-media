"use client";

import { Player } from "@remotion/player";
import {
  HelloWorld,
  HELLO_WORLD_DURATION_IN_FRAMES,
  HELLO_WORLD_FPS,
  HELLO_WORLD_HEIGHT,
  HELLO_WORLD_WIDTH,
} from "@/video/HelloWorld";

// Previews the Remotion composition inside the Next.js app via @remotion/player.
// The same component is rendered headlessly by the Remotion CLI (see video/Root.tsx).
export default function StudioPage() {
  return (
    <main
      style={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        gap: 16,
        padding: 24,
        backgroundColor: "#000",
        color: "#fff",
      }}
    >
      <h1 style={{ fontSize: 24, fontWeight: 600 }}>Remotion preview</h1>
      <Player
        component={HelloWorld}
        durationInFrames={HELLO_WORLD_DURATION_IN_FRAMES}
        fps={HELLO_WORLD_FPS}
        compositionWidth={HELLO_WORLD_WIDTH}
        compositionHeight={HELLO_WORLD_HEIGHT}
        inputProps={{ title: "Sniped Media" }}
        controls
        loop
        style={{ width: "100%", maxWidth: 960, aspectRatio: "16 / 9" }}
      />
    </main>
  );
}
