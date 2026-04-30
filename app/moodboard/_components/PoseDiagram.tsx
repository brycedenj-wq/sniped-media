type PoseDiagramProps = {
  stroke?: string;
  textColor?: string;
};

export function PoseDiagram({
  stroke = "#F5F3EE",
  textColor = "#F5F3EE",
}: PoseDiagramProps) {
  return (
    <svg
      viewBox="0 0 400 600"
      role="img"
      aria-label="Body silhouette with three crop lines marked at mid-thigh, mid-bicep, and mid-forearm."
      className="h-auto w-full max-w-md"
    >
      {/* Body silhouette: abstract form, no face detail */}
      <g
        fill="none"
        stroke={stroke}
        strokeWidth="1.5"
        strokeLinecap="square"
        strokeLinejoin="miter"
      >
        {/* Head */}
        <ellipse cx="200" cy="68" rx="34" ry="42" />
        {/* Neck */}
        <line x1="186" y1="108" x2="186" y2="125" />
        <line x1="214" y1="108" x2="214" y2="125" />
        {/* Shoulders + torso (A-frame) */}
        <path d="M 130 130 L 270 130 L 290 280 L 240 430 L 200 440 L 160 430 L 110 280 Z" />
        {/* Left arm */}
        <path d="M 130 130 L 90 200 L 70 280 L 80 360" />
        {/* Right arm */}
        <path d="M 270 130 L 310 200 L 330 280 L 320 360" />
        {/* Left leg */}
        <path d="M 175 440 L 165 540 L 160 590" />
        {/* Right leg */}
        <path d="M 225 440 L 235 540 L 240 590" />
      </g>

      {/* Crop line 1: mid-thigh */}
      <g>
        <line
          x1="20"
          y1="500"
          x2="380"
          y2="500"
          stroke={stroke}
          strokeWidth="1"
          strokeDasharray="6 6"
          opacity="0.5"
        />
        <text
          x="380"
          y="494"
          textAnchor="end"
          fontSize="11"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="700"
          letterSpacing="2.5"
          fill={textColor}
        >
          CROP.
        </text>
      </g>

      {/* Crop line 2: mid-bicep */}
      <g>
        <line
          x1="20"
          y1="180"
          x2="380"
          y2="180"
          stroke={stroke}
          strokeWidth="1"
          strokeDasharray="6 6"
          opacity="0.5"
        />
        <text
          x="380"
          y="174"
          textAnchor="end"
          fontSize="11"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="700"
          letterSpacing="2.5"
          fill={textColor}
        >
          CROP.
        </text>
      </g>

      {/* Crop line 3: mid-forearm */}
      <g>
        <line
          x1="20"
          y1="320"
          x2="380"
          y2="320"
          stroke={stroke}
          strokeWidth="1"
          strokeDasharray="6 6"
          opacity="0.5"
        />
        <text
          x="380"
          y="314"
          textAnchor="end"
          fontSize="11"
          fontFamily="'Space Grotesk', system-ui, sans-serif"
          fontWeight="700"
          letterSpacing="2.5"
          fill={textColor}
        >
          CROP.
        </text>
      </g>
    </svg>
  );
}
