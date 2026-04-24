import { Container } from "../Container";
import { GridOverlay } from "../GridOverlay";
import { SectionMarker } from "../SectionMarker";

const tiles = [
  {
    n: "01",
    title: "The Shoot",
    body: "One day. Pre-planned. Wardrobe, locations, shot list dialed in before the camera comes out.",
  },
  {
    n: "02",
    title: "The Library",
    body: "60 to 80 final images. Pre-formatted for every deployment context. Delivered in a structured gallery, tagged by use case, ready to pull.",
  },
  {
    n: "03",
    title: "The Deployment Plan",
    body: "A month-by-month plan. Which image lands on LinkedIn in February. Which frame holds up as press landscape for the Series B announcement. Which shot opens the keynote in October.",
  },
  {
    n: "04",
    title: "The System",
    body: "You stop commissioning one-off shoots. You have a library that covers the year.",
  },
];

export function KitProduces() {
  return (
    <section className="relative border-t border-border bg-background py-section">
      <GridOverlay />
      <Container className="relative z-10">
        <SectionMarker n="03" label="What the Kit Produces" />

        <div className="mt-12 mb-16 max-w-3xl">
          <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
            Four deliverables. One library.
          </h2>
        </div>

        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:gap-6">
          {tiles.map((t) => (
            <div
              key={t.n}
              className="flex flex-col border border-border bg-surface p-8"
            >
              <span className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-muted tabular-nums">
                {t.n}
              </span>
              <h3 className="mt-4 font-heading text-xl font-medium tracking-tight text-foreground sm:text-2xl">
                {t.title}
              </h3>
              <p className="mt-4 text-base text-foreground/80 leading-relaxed">
                {t.body}
              </p>
            </div>
          ))}
        </div>
      </Container>
    </section>
  );
}
