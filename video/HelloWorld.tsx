import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

// Shared composition metadata so the Remotion CLI (Root.tsx) and the
// in-app <Player> (app/studio) stay in sync.
export const HELLO_WORLD_FPS = 30;
export const HELLO_WORLD_WIDTH = 1920;
export const HELLO_WORLD_HEIGHT = 1080;
export const HELLO_WORLD_DURATION_IN_FRAMES = 150;

export type HelloWorldProps = {
  title: string;
};

export const HelloWorld = ({ title }: HelloWorldProps) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({ frame, fps, config: { damping: 200 } });
  const opacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0a0a0a",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <h1
        style={{
          color: "white",
          fontSize: 120,
          fontWeight: 700,
          fontFamily: "sans-serif",
          letterSpacing: "-0.04em",
          transform: `scale(${scale})`,
          opacity,
        }}
      >
        {title}
      </h1>
    </AbsoluteFill>
  );
};
