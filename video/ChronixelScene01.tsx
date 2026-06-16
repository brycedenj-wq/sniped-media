import {
  AbsoluteFill,
  interpolate,
  random,
  Sequence,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/Poppins";

// Off-white Poppins ExtraBold (800) per the Chronixel text-style guide.
const { fontFamily } = loadFont("normal", { weights: ["600", "800"] });

// Shared composition metadata (kept in sync with Root.tsx + app/studio).
export const CHRONIXEL_FPS = 30;
export const CHRONIXEL_WIDTH = 1080;
export const CHRONIXEL_HEIGHT = 1920;
export const CHRONIXEL_DURATION_IN_FRAMES = 240; // 8s

// Chronixel palette.
const INK = "#070708"; // dark cinematic base
const OFF_WHITE = "#F4F1EA";
const ORANGE_GRAD = "linear-gradient(135deg, #FFB14E 0%, #FF6A00 55%, #FF3D00 100%)";
const GLASS_BG = "rgba(255,255,255,0.04)";
const GLASS_BORDER = "rgba(255,255,255,0.12)";

const HEADING: React.CSSProperties = {
  fontFamily,
  fontWeight: 800,
  color: OFF_WHITE,
  letterSpacing: "-0.05em", // very tight, letters almost touching
  margin: 0,
  lineHeight: 0.95,
};

// --- Background: dark cinematic base + radial glow + subtle drifting grid ---
const ChronixelBackground = () => {
  const frame = useCurrentFrame();
  const drift = interpolate(frame, [0, CHRONIXEL_DURATION_IN_FRAMES], [0, 40]);
  const cell = 90;
  return (
    <AbsoluteFill style={{ backgroundColor: INK }}>
      {/* warm cinematic glow toward the center */}
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(120% 70% at 50% 38%, rgba(255,106,0,0.18) 0%, rgba(255,61,0,0.05) 35%, rgba(7,7,8,0) 70%)",
        }}
      />
      {/* subtle grid */}
      <AbsoluteFill
        style={{
          backgroundImage: `linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px)`,
          backgroundSize: `${cell}px ${cell}px`,
          backgroundPosition: `0px ${drift}px`,
          maskImage:
            "radial-gradient(100% 75% at 50% 45%, #000 30%, transparent 85%)",
          WebkitMaskImage:
            "radial-gradient(100% 75% at 50% 45%, #000 30%, transparent 85%)",
        }}
      />
      {/* vignette */}
      <AbsoluteFill
        style={{
          boxShadow: "inset 0 0 400px 120px rgba(0,0,0,0.85)",
        }}
      />
    </AbsoluteFill>
  );
};

// --- Reusable glass UI panel ---
const GlassPanel = ({
  children,
  style,
}: {
  children?: React.ReactNode;
  style?: React.CSSProperties;
}) => (
  <div
    style={{
      background: GLASS_BG,
      border: `1px solid ${GLASS_BORDER}`,
      borderRadius: 28,
      backdropFilter: "blur(12px)",
      boxShadow:
        "0 30px 80px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.08)",
      ...style,
    }}
  >
    {children}
  </div>
);

// --- Beat 1: MESSY WORKFLOW — scattered glass cards that settle into a stack ---
const MessyToClean = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // 0 = scattered chaos, 1 = snapped into a clean aligned stack
  const order = spring({ frame, fps, durationInFrames: 55, config: { damping: 200 } });

  const cards = new Array(5).fill(0).map((_, i) => {
    const seed = i + 1;
    const chaosX = (random(`x${seed}`) - 0.5) * 520;
    const chaosY = (random(`y${seed}`) - 0.5) * 360;
    const chaosRot = (random(`r${seed}`) - 0.5) * 38;

    const targetY = (i - 2) * 150;
    const x = interpolate(order, [0, 1], [chaosX, 0]);
    const y = interpolate(order, [0, 1], [chaosY, targetY]);
    const rot = interpolate(order, [0, 1], [chaosRot, 0]);
    const warn = interpolate(order, [0, 0.6], [1, 0], { extrapolateRight: "clamp" });

    return (
      <GlassPanel
        key={i}
        style={{
          position: "absolute",
          width: 560,
          height: 118,
          transform: `translate(${x}px, ${y}px) rotate(${rot}deg)`,
          display: "flex",
          alignItems: "center",
          padding: "0 28px",
          gap: 20,
        }}
      >
        {/* status dot: orange warning while messy → calm while clean */}
        <div
          style={{
            width: 18,
            height: 18,
            borderRadius: 99,
            background: warn > 0.5 ? ORANGE_GRAD : "rgba(255,255,255,0.25)",
            boxShadow: warn > 0.5 ? "0 0 22px rgba(255,106,0,0.8)" : "none",
            flexShrink: 0,
          }}
        />
        {/* skeleton "content" bars — never literal sentences */}
        <div style={{ flex: 1, display: "flex", flexDirection: "column", gap: 12 }}>
          <div style={{ height: 14, width: `${60 + i * 7}%`, borderRadius: 8, background: "rgba(255,255,255,0.16)" }} />
          <div style={{ height: 10, width: `${35 + i * 9}%`, borderRadius: 8, background: "rgba(255,255,255,0.09)" }} />
        </div>
      </GlassPanel>
    );
  });

  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
      {cards}
    </AbsoluteFill>
  );
};

// --- Animated word label (rises + fades in) ---
const Label = ({
  text,
  size,
  accent,
}: {
  text: string;
  size: number;
  accent?: boolean;
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const enter = spring({ frame, fps, config: { damping: 200 } });
  const y = interpolate(enter, [0, 1], [40, 0]);
  const opacity = interpolate(frame, [0, 14], [0, 1], { extrapolateRight: "clamp" });

  const accentStyle: React.CSSProperties = accent
    ? {
        background: ORANGE_GRAD,
        WebkitBackgroundClip: "text",
        backgroundClip: "text",
        WebkitTextFillColor: "transparent",
      }
    : {};

  return (
    <h1
      style={{
        ...HEADING,
        ...accentStyle,
        fontSize: size,
        opacity,
        transform: `translateY(${y}px)`,
        textAlign: "center",
      }}
    >
      {text}
    </h1>
  );
};

// --- Orange progress timeline near the bottom ---
const Timeline = () => {
  const frame = useCurrentFrame();
  const pct = interpolate(frame, [0, CHRONIXEL_DURATION_IN_FRAMES - 20], [0, 1], {
    extrapolateRight: "clamp",
  });
  return (
    <div
      style={{
        position: "absolute",
        bottom: 150,
        left: 90,
        right: 90,
        height: 14,
        borderRadius: 99,
        background: "rgba(255,255,255,0.08)",
        overflow: "hidden",
        border: `1px solid ${GLASS_BORDER}`,
      }}
    >
      <div
        style={{
          height: "100%",
          width: `${pct * 100}%`,
          background: ORANGE_GRAD,
          boxShadow: "0 0 26px rgba(255,106,0,0.7)",
        }}
      />
    </div>
  );
};

export const ChronixelScene01 = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: INK }}>
      <ChronixelBackground />

      {/* Top label — names the problem in 2 words, not a sentence */}
      <Sequence from={0} durationInFrames={120}>
        <AbsoluteFill style={{ alignItems: "center", paddingTop: 210 }}>
          <Label text="MESSY WORKFLOW" size={96} />
        </AbsoluteFill>
      </Sequence>

      {/* The visual idea: chaos resolving into an aligned system */}
      <Sequence from={10}>
        <MessyToClean />
      </Sequence>

      {/* Payoff label — the resolved state, accented in orange */}
      <Sequence from={120} durationInFrames={CHRONIXEL_DURATION_IN_FRAMES - 120}>
        <AbsoluteFill style={{ alignItems: "center", paddingTop: 210 }}>
          <Label text="CLEAN SYSTEM" size={104} accent />
        </AbsoluteFill>
      </Sequence>

      {/* Brand tag */}
      <Sequence from={150}>
        <AbsoluteFill style={{ alignItems: "center", justifyContent: "flex-end", paddingBottom: 230 }}>
          <Label text="CHRONIXEL" size={56} />
        </AbsoluteFill>
      </Sequence>

      <Timeline />
    </AbsoluteFill>
  );
};
