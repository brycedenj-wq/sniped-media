import Image from "next/image";
import Link from "next/link";
import { Container } from "../Container";
import { GridOverlay } from "../GridOverlay";
import { SectionMarker } from "../SectionMarker";

type Frame = {
  src: string;
  alt: string;
  index: string;
  context: string;
  specs: string;
  deployment: string;
};

const frames: Frame[] = [
  {
    src: "/images/work/archive/archive-09.jpg",
    alt: "Editorial founder portrait, controlled light",
    index: "01",
    context: "EDITORIAL / CONTROLLED LIGHT",
    specs: "85mm f/1.8",
    deployment: "LINKEDIN HERO 1584 × 396",
  },
  {
    src: "/images/work/archive/archive-03.jpg",
    alt: "Environmental founder portrait, natural light",
    index: "02",
    context: "ENVIRONMENTAL / NATURAL LIGHT",
    specs: "35mm f/2.8",
    deployment: "PRESS LANDSCAPE / SERIES B",
  },
  {
    src: "/images/work/archive/archive-17.jpg",
    alt: "Studio portrait, high key",
    index: "03",
    context: "STUDIO / HIGH KEY",
    specs: "50mm f/4",
    deployment: "SPEAKING DECK OPENER 16:9",
  },
  {
    src: "/images/work/archive/archive-10.jpg",
    alt: "Outdoor founder portrait, golden hour",
    index: "04",
    context: "OUTDOOR / GOLDEN HOUR",
    specs: "85mm f/2.2",
    deployment: "PODCAST TILE 1400 × 1400",
  },
  {
    src: "/images/work/archive/archive-19.jpg",
    alt: "Environmental founder portrait, overcast",
    index: "05",
    context: "ENVIRONMENTAL / OVERCAST",
    specs: "35mm f/4",
    deployment: "TEAM PAGE HERO",
  },
  {
    src: "/images/work/archive/archive-01.jpg",
    alt: "Studio portrait, low key",
    index: "06",
    context: "STUDIO / LOW KEY",
    specs: "85mm f/2",
    deployment: "YEAR-END PRESS FEATURE",
  },
];

export function WorkTeaser() {
  return (
    <section className="relative border-t border-border bg-background py-section">
      <GridOverlay />
      <Container className="relative z-10">
        <SectionMarker n="05" label="Selected Work" />

        <div className="mt-12 mb-12 flex items-end justify-between gap-8">
          <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
            The grid.
          </h2>
        </div>

        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 sm:gap-4">
          {frames.map((f) => (
            <figure
              key={f.src}
              className="group relative flex flex-col gap-3"
            >
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={f.src}
                  alt={f.alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 50vw"
                  className="object-cover object-center transition-transform duration-500 group-hover:scale-[1.02]"
                />
                <div className="pointer-events-none absolute inset-x-0 bottom-0 bg-gradient-to-t from-foreground/90 via-foreground/30 to-transparent p-5 opacity-0 transition-opacity duration-200 group-hover:opacity-100 motion-reduce:transition-none">
                  <p className="font-heading text-[11px] font-semibold tracking-[0.25em] uppercase text-background tabular-nums">
                    {f.context} · {f.specs}
                  </p>
                  <p className="mt-1 font-heading text-[11px] font-semibold tracking-[0.25em] uppercase text-background/80 tabular-nums">
                    {f.deployment}
                  </p>
                </div>
              </div>
              <figcaption className="flex items-center justify-between gap-2 border-t border-border pt-2 font-heading text-[11px] font-semibold tracking-[0.2em] uppercase text-muted tabular-nums">
                <span>{f.index}</span>
                <span className="truncate">{f.specs}</span>
              </figcaption>
            </figure>
          ))}
        </div>

        <div className="mt-12 flex justify-start">
          <Link
            href="/kit"
            className="text-sm font-semibold text-foreground underline decoration-foreground/30 underline-offset-4 transition-colors hover:text-accent hover:decoration-accent"
          >
            See the Kit →
          </Link>
        </div>
      </Container>
    </section>
  );
}
