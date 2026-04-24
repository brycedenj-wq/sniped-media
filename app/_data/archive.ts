export type ArchiveContext = "editorial" | "environmental" | "studio";
export type ArchiveDeployment =
  | "linkedin-hero"
  | "linkedin-post"
  | "press-portrait"
  | "press-landscape"
  | "speaking-deck"
  | "podcast-tile"
  | "web-hero"
  | "about-page"
  | "newsletter-header"
  | "investor-letter"
  | "recruiting";

export type ArchiveEntry = {
  id: string;
  src: string;
  alt: string;
  context: ArchiveContext;
  deployment: ArchiveDeployment;
  caption: string;
};

// Placeholder values. Real context / deployment / caption strings arrive in
// Polish Pass Tier 2. The id numbering matches /public/images/work/archive/.
export const archive: ArchiveEntry[] = [
  {
    id: "01",
    src: "/images/work/archive/archive-01.jpg",
    alt: "Editorial founder portrait",
    context: "editorial",
    deployment: "web-hero",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "02",
    src: "/images/work/archive/archive-02.jpg",
    alt: "Editorial founder portrait",
    context: "editorial",
    deployment: "linkedin-post",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "03",
    src: "/images/work/archive/archive-03.jpg",
    alt: "Editorial headshot",
    context: "studio",
    deployment: "press-portrait",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "04",
    src: "/images/work/archive/archive-04.jpg",
    alt: "Editorial portrait",
    context: "editorial",
    deployment: "podcast-tile",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "05",
    src: "/images/work/archive/archive-05.jpg",
    alt: "Editorial portrait",
    context: "editorial",
    deployment: "speaking-deck",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "06",
    src: "/images/work/archive/archive-06.jpg",
    alt: "Editorial portrait",
    context: "editorial",
    deployment: "newsletter-header",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "07",
    src: "/images/work/archive/archive-07.jpg",
    alt: "Environmental portrait",
    context: "environmental",
    deployment: "about-page",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "08",
    src: "/images/work/archive/archive-08.jpg",
    alt: "Brand campaign portrait",
    context: "environmental",
    deployment: "web-hero",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "09",
    src: "/images/work/archive/archive-09.jpg",
    alt: "Editorial founder portrait",
    context: "editorial",
    deployment: "linkedin-hero",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "10",
    src: "/images/work/archive/archive-10.jpg",
    alt: "Editorial founder portrait",
    context: "editorial",
    deployment: "press-landscape",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "11",
    src: "/images/work/archive/archive-14.jpg",
    alt: "Editorial portrait series",
    context: "editorial",
    deployment: "press-portrait",
    caption: "Placeholder caption · Polish Tier 2",
  },
  {
    id: "12",
    src: "/images/work/archive/archive-17.jpg",
    alt: "Environmental commercial portrait",
    context: "environmental",
    deployment: "recruiting",
    caption: "Placeholder caption · Polish Tier 2",
  },
];
