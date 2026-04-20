export type BookableTier = {
  id: string;
  category: "base" | "mothers-day" | "grad";
  fullLabel: string;
  label: string;
  price: string;
  tagline?: string;
  detail: string;
  pixiesetUrl?: string;
  active: boolean;
};

export const bookableTiers: BookableTier[] = [
  {
    id: "mothers-day-moment",
    category: "mothers-day",
    fullLabel: "Mother's Day Session: The Moment ($275)",
    label: "Mother's Day · The Moment · $275",
    price: "$275",
    tagline: "May 2 and 3 · DTLA studio · Limited to 12 spots",
    detail: "30-minute studio session, 5 retouched images. Full payment at booking.",
    pixiesetUrl: "https://snipedmedia.pixieset.com/booking/mothers-day-moment",
    active: true,
  },
  {
    id: "mothers-day-feature",
    category: "mothers-day",
    fullLabel: "Mother's Day Session: The Feature ($550)",
    label: "Mother's Day · The Feature · $550",
    price: "$550",
    tagline: "May 2 and 3 · DTLA studio · Limited to 12 spots",
    detail: "60-minute studio session, 15 to 20 retouched images, one 8x10 fine-art print. 50% retainer at booking.",
    pixiesetUrl: "https://snipedmedia.pixieset.com/booking/mothers-day-feature",
    active: true,
  },
  {
    id: "grad-short-film",
    category: "grad",
    fullLabel: "Grad Session: Short Film ($275)",
    label: "Grad · Short Film · $275",
    price: "$275",
    tagline: "Now through mid-June · DTLA studio or your LA campus",
    detail: "45 minutes of directed coverage, 5 retouched images. Full payment at booking.",
    pixiesetUrl: "https://snipedmedia.pixieset.com/booking/grad-short-film",
    active: true,
  },
  {
    id: "grad-feature-length",
    category: "grad",
    fullLabel: "Grad Session: Feature Length ($550)",
    label: "Grad · Feature Length · $550",
    price: "$550",
    tagline: "Now through mid-June · DTLA studio or your LA campus",
    detail: "90 minutes of directed coverage, 15 to 20 retouched images. 50% retainer at booking.",
    pixiesetUrl: "https://snipedmedia.pixieset.com/booking/grad-feature-length",
    active: true,
  },
  {
    id: "baseline",
    category: "base",
    fullLabel: "Tier 1: The Baseline ($275)",
    label: "The Baseline · $275",
    price: "$275",
    detail: "45 minutes, one location, 5 retouched images. Best for individuals and headshots.",
    pixiesetUrl: "https://snipedmedia.pixieset.com/booking/tier-1-the-baseline",
    active: true,
  },
  {
    id: "standard",
    category: "base",
    fullLabel: "Tier 2: The Standard ($550)",
    label: "The Standard · $550",
    price: "$550",
    detail: "Up to 90 minutes, multiple looks, 15 to 20 retouched images. Best for families and lifestyle.",
    pixiesetUrl: "https://snipedmedia.pixieset.com/booking/tier-2-the-standard",
    active: true,
  },
  {
    id: "events",
    category: "base",
    fullLabel: "Tier 3: Event Coverage ($1,200+)",
    label: "Event Coverage · from $1,200",
    price: "from $1,200",
    detail: "4 hours of coverage, 50+ delivered images. Best for banquets and local campaigns.",
    active: true,
  },
];

export const activeBookableTiers = bookableTiers.filter((t) => t.active);
