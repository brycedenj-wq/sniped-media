export type PaletteSwatch = {
  name: string;
  hex: string;
};

export type PaletteData = {
  slug: string;
  hero: string; // the wash word ("WHITE.", "RUST.", "GOLD.")
  washColor: string; // hex for Section 1 wash background
  washTextColor: string; // hex for hero word color
  textureSrc: string; // path to AI texture image
  textureCaption: string;
  // Section 2 / Concept
  concept: string;
  shootLabel: string; // "SHOOT 01"
  shootDate: string;
  callTime: string;
  location: string;
  // Section 3 / Palette
  paletteIntro: string[]; // multi-line operator text above the columns
  swatches: PaletteSwatch[]; // 5 columns
  // Section 5 / Lighting
  lighting: {
    key: string;
    rim: string;
    fill?: string;
    rimNote?: string;
    trailingLines: string[];
  };
  // Section 6 / Direction (Direction Stack-cited stanzas)
  direction: string[][];
  // Section 7 / Wardrobe (block of operator copy)
  wardrobe: {
    paletteCopy: string[];
    garments: string[];
    alsoAcceptable?: string[];
    restrictions: string[];
    jewelry: string[];
    footwear?: string[];
    makeupNote?: string[];
    bringPolicy: string;
  };
  // Section 8 / Team Direction
  teamDirection: {
    hair: string[];
    makeup: string[];
    attitude: string[];
  };
};

export const palettes: Record<string, PaletteData> = {
  white: {
    slug: "white",
    hero: "WHITE.",
    washColor: "#F2EFE7",
    washTextColor: "#1A1A1A",
    textureSrc: "/images/moodboard/white-texture.jpg",
    textureCaption:
      "Studio light on cream silk. The material carries.",
    concept:
      "Polished commercial editorial. Monochromatic color blocking. Skin as the contrast point.",
    shootLabel: "SHOOT 01",
    shootDate: "FRIDAY MAY 1",
    callTime: "CALL 10:00 AM",
    location: "2715 S MAIN ST, LOS ANGELES",
    paletteIntro: [
      "The tonal range. Subject can live anywhere inside it.",
      "Wardrobe reads inside the family or the frame breaks.",
    ],
    swatches: [
      { name: "Pearl", hex: "#F4EFE3" },
      { name: "Cream", hex: "#EDE3CB" },
      { name: "Ivory", hex: "#F0EBE0" },
      { name: "Bone", hex: "#E5E1D6" },
      { name: "Chalk", hex: "#DDD8CB" },
    ],
    lighting: {
      key: "Soft, parallel, camera left",
      rim: "Hard, back-right, 45° behind subject",
      fill: "None. Negative fill on shadow side if needed.",
      trailingLines: [
        "The subject is metered for the face.",
        "The shoulders drop on the exhale.",
        "The frame waits for the breath reset.",
      ],
    },
    direction: [
      [
        "The body does not start squared to the lens.",
        "Protocol 03 runs first. Full rotation vocabulary.",
        "Five body geometries per look.",
      ],
      [
        "The hands are tasked, never neutral.",
        "Protocol 01. Negative space through the forearms.",
        "The frame opens at the silhouette.",
      ],
      [
        "The chin comes forward and down.",
        "Protocol 05. Jawline separation from the neck line.",
        "Spine pulled tall first.",
      ],
      [
        "The operator does not correct without affirming.",
        "The operator does not transmit pressure.",
        "The subject leaves the set respected.",
      ],
    ],
    wardrobe: {
      paletteCopy: [
        "Pearl, cream, ivory, bone, chalk. Stay inside the family.",
        "Warm undertones preferred. No cool whites that fight the warm key.",
        "No optical-bright whites. No black, no navy, no color accent.",
      ],
      garments: [
        "Tailored white blouse, cotton or silk, full sleeve",
        "Cream slip dress or knit top, fitted, not loose",
        "Ivory tailored trouser or skirt, structured",
        "Off-white knit, fine gauge, not chunky",
        "Cream silk camisole, layered or solo",
      ],
      restrictions: [
        "No logos, no patterns, no hardware",
        "No sheer unless layered",
        "No slogans, no prints",
      ],
      jewelry: [
        "Gold, warm metals. Single statement piece per look.",
        "No silver, no cool-tone metal.",
      ],
      footwear: ["Off-frame in most shots. Bring whatever fits the look."],
      bringPolicy: "Bring two looks. Hangers provided.",
    },
    teamDirection: {
      hair: [
        "Clean. Blown out or strongest natural texture.",
        "No half-styling. No loose-trying-to-look-styled.",
      ],
      makeup: [
        "Editorial clean. Skin reads as skin.",
        "Groomed brow. Neutral lip (mauve, nude, soft pink).",
        "Minimal eye. No drama on the face, the wardrobe is the volume.",
      ],
      attitude: [
        "Severe but not angry. Confident but not performing.",
        "Chin forward and down. Eyes either to the lens or through it.",
      ],
    },
  },
  orange: {
    slug: "orange",
    hero: "RUST.",
    washColor: "#7A3A1F",
    washTextColor: "#F5EAD8",
    textureSrc: "/images/moodboard/orange-texture.jpg",
    textureCaption:
      "Rust paper installed. Rim light at the floor line.",
    concept:
      "Rust on rust. Tonal saturation. Skin glow against the warm block.",
    shootLabel: "SHOOT 01",
    shootDate: "FRIDAY MAY 1",
    callTime: "CALL 10:00 AM",
    location: "2715 S MAIN ST, LOS ANGELES",
    paletteIntro: [
      "The tonal range. Subject can live anywhere inside it.",
      "Wardrobe reads inside the family or the frame breaks.",
    ],
    swatches: [
      { name: "Terracotta", hex: "#B25434" },
      { name: "Rust", hex: "#8E3D1E" },
      { name: "Burnt Orange", hex: "#A8442A" },
      { name: "Ochre", hex: "#B97A33" },
      { name: "Sienna", hex: "#7E3814" },
    ],
    lighting: {
      key: "Soft, parallel, camera left",
      rim: "Hard, back-right, 45° behind subject",
      rimNote: "Rim carries the separation on orange-on-orange.",
      trailingLines: [
        "The subject is metered for the face.",
        "The shoulders drop on the exhale.",
        "The frame waits for the breath reset.",
      ],
    },
    direction: [
      [
        "The body does not start squared to the lens.",
        "Protocol 03 runs first. Full rotation vocabulary.",
        "Five body geometries per look.",
      ],
      [
        "The hands are tasked, never neutral.",
        "Protocol 01. Negative space through the forearms.",
        "The frame opens at the silhouette.",
      ],
      [
        "The chin comes forward and down.",
        "Protocol 05. Jawline separation from the neck line.",
        "Spine pulled tall first.",
      ],
      [
        "The palette is dense. The presence matches it.",
        "Protocol 09. No softness. No performed face.",
        "Monumental anchor to the bottom edge.",
      ],
      [
        "The operator does not correct without affirming.",
        "The operator does not transmit pressure.",
        "The subject leaves the set respected.",
      ],
    ],
    wardrobe: {
      paletteCopy: [
        "Rust, terracotta, burnt orange, ochre, sienna. Saturated warm tones.",
        "Stay inside the family. No corals (too pink). No mustards (too yellow).",
        "No browns (collapses the block). No cool accent, no black, no white.",
      ],
      garments: [
        "Rust silk slip dress, fitted, knee or longer",
        "Terracotta knit top, fine gauge",
        "Burnt orange tailored blouse, full sleeve",
        "Ochre suede or leather piece (skirt, jacket)",
        "Sienna trouser or wide-leg pant",
      ],
      restrictions: [
        "No logos, no patterns, no hardware",
        "No black piping or accent trim",
        "Solid tonal blocks only",
      ],
      jewelry: [
        "Gold, brass, warm metals. Single piece per look.",
        "No silver, no cool-tone metal.",
      ],
      makeupNote: [
        "Warm-tone palette throughout. Brick or terracotta lip.",
        "The face has to live in the palette.",
      ],
      bringPolicy: "Bring two looks. Hangers provided.",
    },
    teamDirection: {
      hair: [
        "Clean. Strongest natural texture preferred.",
        "Warm tones in the styling, no cool products.",
      ],
      makeup: [
        "Editorial clean, warm-tone palette throughout.",
        "Groomed brow. Warm lip (terracotta, brick, rust).",
        "Minimal eye, but warmth in the lid if any.",
        "The face lives inside the palette block.",
      ],
      attitude: [
        "Monumental. Grounded. Density of color requires density of presence.",
        "No softness, no flirt.",
      ],
    },
  },
  gold: {
    slug: "gold",
    hero: "GOLD.",
    washColor: "#C9A560",
    washTextColor: "#1A1A1A",
    textureSrc: "/images/moodboard/gold-texture.jpg",
    textureCaption:
      "Champagne satin draped. Gold-toned light spilling camera left.",
    concept:
      "Press-grade portraiture. Cream and gold tonal weight. Promo-elevated, editorial-restrained.",
    shootLabel: "SHOOT 02",
    shootDate: "SUNDAY MAY 3",
    callTime: "CALL 10:00 AM",
    location: "2715 S MAIN ST, LOS ANGELES",
    paletteIntro: [
      "The tonal range. Subject can live anywhere inside it.",
      "Wardrobe reads inside the family or the frame breaks.",
    ],
    swatches: [
      { name: "Champagne", hex: "#E5D2A3" },
      { name: "Cream", hex: "#EDE0C2" },
      { name: "Gold Leaf", hex: "#C9A560" },
      { name: "Warm Tan", hex: "#B5915A" },
      { name: "Honey", hex: "#A87C3D" },
    ],
    lighting: {
      key: "Soft, parallel, camera left",
      rim: "Hard, back-right, 45° behind subject",
      fill: "None. Warmth rides in the key.",
      trailingLines: [
        "The subject is metered for the face.",
        "Press-grade exposure.",
        "The frame holds until the posture lands.",
      ],
    },
    direction: [
      [
        "The body does not start squared to the lens.",
        "Protocol 03 runs first. Rotation vocabulary.",
        "Duo geometries built on staggered shoulders.",
      ],
      [
        "The hands are tasked, never neutral.",
        "Protocol 01. Negative space through the forearms.",
        "Subject-work, not model-work.",
      ],
      [
        "The chin comes forward and down.",
        "Protocol 05. Jawline separation from the neck line.",
        "Spine pulled tall first.",
      ],
      [
        "The subjects are working artists, not posing models.",
        "Protocol 09 carries the frame. Presence over performance.",
        "Grounded. Professional. Promo-elevated.",
      ],
      [
        "The operator does not correct without affirming.",
        "The operator does not transmit pressure.",
        "The subject leaves the set respected.",
      ],
    ],
    wardrobe: {
      paletteCopy: [
        "Champagne, cream, gold leaf, warm tan, honey. Promotional editorial.",
        "Polished press energy. The palette is HASS-adjacent: warm gold tones",
        "consistent with the visual identity of the event.",
      ],
      garments: [
        "Cream linen shirt or button-down, relaxed cut",
        "Champagne tailored knit, fine gauge",
        "Gold-toned outerwear (camel coat, tan jacket)",
        "Honey-tone trouser or chino, structured",
        "Warm tan leather piece, jacket or accessory",
      ],
      alsoAcceptable: [
        "Black or charcoal pieces against the cream/gold backdrop.",
        "Subject-dark + backdrop-warm reads as a clean Sniped Media contrast move.",
        "If you'd wear it to the party, bring it.",
      ],
      restrictions: [
        "No cool-tone pieces",
        "No loud logos (HASS brand only if applicable)",
        "No streetwear graphics",
      ],
      jewelry: [
        "Whatever feels honest. Single statement chain or watch preferred.",
      ],
      bringPolicy:
        "Bring one to two looks. Hangers provided. Shoot is press-grade, promo-elevated.",
    },
    teamDirection: {
      hair: [
        "Natural styling, well-groomed. No over-styling.",
        "Honest to the subject, not performed.",
      ],
      makeup: [
        "Skin grooming only. Oil-blot, brow groom.",
        "No foundation unless skin needs it. No lipstick.",
        "The shoot is press-grade, not glam.",
      ],
      attitude: [
        "Confident, grounded, professional.",
        "Promo-grade energy. The shoot is for HASS distribution,",
        "the posture has to read like working artists, not posing models.",
      ],
    },
  },
};

export const paletteSlugs = Object.keys(palettes);
