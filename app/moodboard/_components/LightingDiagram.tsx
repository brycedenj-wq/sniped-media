type LightingDiagramProps = {
  stroke?: string;
  textColor?: string;
};

export function LightingDiagram({
  stroke = "#F5F3EE",
  textColor = "#F5F3EE",
}: LightingDiagramProps) {
  return (
    <svg
      viewBox="0 0 600 400"
      role="img"
      aria-label="Top-down lighting diagram. Subject center, key light camera left, rim light back right, no fill."
      className="h-auto w-full max-w-2xl"
    >
      {/* Stage / studio bounding outline */}
      <rect
        x="20"
        y="20"
        width="560"
        height="360"
        fill="none"
        stroke={stroke}
        strokeOpacity="0.18"
        strokeWidth="1"
      />

      {/* Camera at the bottom */}
      <g transform="translate(285, 350)">
        <rect width="30" height="22" fill="none" stroke={stroke} strokeWidth="1.2" />
        <polygon
          points="6,0 24,0 30,-10 0,-10"
          fill="none"
          stroke={stroke}
          strokeWidth="1.2"
        />
        <text
          x="15"
          y="38"
          textAnchor="middle"
          fontSize="10"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="600"
          letterSpacing="2"
          fill={textColor}
          opacity="0.7"
        >
          CAMERA
        </text>
      </g>

      {/* Subject (center) */}
      <g transform="translate(300, 200)">
        <circle r="34" fill="none" stroke={stroke} strokeWidth="1.5" />
        <circle r="3" fill={stroke} />
        <text
          y="58"
          textAnchor="middle"
          fontSize="11"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="600"
          letterSpacing="2"
          fill={textColor}
          opacity="0.9"
        >
          SUBJECT
        </text>
      </g>

      {/* Subject facing arrow toward camera */}
      <line
        x1="300"
        y1="234"
        x2="300"
        y2="328"
        stroke={stroke}
        strokeWidth="1"
        strokeDasharray="4 4"
        opacity="0.4"
      />

      {/* Key light — camera left, parallel */}
      <g>
        <rect
          x="80"
          y="170"
          width="60"
          height="60"
          fill="none"
          stroke={stroke}
          strokeWidth="1.2"
        />
        <line
          x1="140"
          y1="200"
          x2="266"
          y2="200"
          stroke={stroke}
          strokeWidth="1"
          strokeDasharray="3 3"
          opacity="0.5"
        />
        <text
          x="110"
          y="160"
          textAnchor="middle"
          fontSize="11"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="700"
          letterSpacing="2"
          fill={textColor}
        >
          KEY
        </text>
        <text
          x="110"
          y="252"
          textAnchor="middle"
          fontSize="9"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="500"
          letterSpacing="1.5"
          fill={textColor}
          opacity="0.6"
        >
          SOFT / PARALLEL
        </text>
      </g>

      {/* Rim light — back right, 45° */}
      <g>
        <rect
          x="450"
          y="80"
          width="40"
          height="40"
          fill="none"
          stroke={stroke}
          strokeWidth="1.2"
        />
        <line
          x1="455"
          y1="120"
          x2="328"
          y2="180"
          stroke={stroke}
          strokeWidth="1"
          strokeDasharray="3 3"
          opacity="0.5"
        />
        <text
          x="470"
          y="70"
          textAnchor="middle"
          fontSize="11"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="700"
          letterSpacing="2"
          fill={textColor}
        >
          RIM
        </text>
        <text
          x="470"
          y="138"
          textAnchor="middle"
          fontSize="9"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="500"
          letterSpacing="1.5"
          fill={textColor}
          opacity="0.6"
        >
          HARD / 45°
        </text>
      </g>

      {/* Negative fill flag — shadow side */}
      <g>
        <line
          x1="380"
          y1="225"
          x2="430"
          y2="225"
          stroke={stroke}
          strokeWidth="2"
          opacity="0.5"
        />
        <text
          x="405"
          y="245"
          textAnchor="middle"
          fontSize="9"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="500"
          letterSpacing="1.5"
          fill={textColor}
          opacity="0.5"
        >
          NEG. FILL (OPT.)
        </text>
      </g>
    </svg>
  );
}
