import type { Metadata } from "next";
import Link from "next/link";
import { Container } from "../_components/Container";
import { FadeIn } from "../_components/FadeIn";
import { GridOverlay } from "../_components/GridOverlay";
import { SectionMarker } from "../_components/SectionMarker";

export const metadata: Metadata = {
  title: "The Founder Kit",
  description:
    "The Founder Kit. $12,500. One structured shoot, 60 to 80 deployed-ready images, and a 12-month deployment plan. Built for Series A to C founders in LA.",
  openGraph: {
    title: "The Founder Kit | Sniped Media",
    description:
      "The Founder Kit. $12,500. One structured shoot, 60 to 80 deployed-ready images, and a 12-month deployment plan.",
    url: "/kit",
  },
};

type Block = {
  n: string;
  title: string;
  body: string;
  items: string[];
  align: "left" | "right";
};

const blocks: Block[] = [
  {
    n: "Block 1",
    title: "Pre-production",
    body: "Before the shoot day, the engagement is planned end to end. Creative direction is set. Wardrobe is reviewed. Locations are scouted. The shot list is signed off. Nothing is improvised on set. The shoot day is execution, not discovery.",
    items: [
      "Creative direction call, 60 minutes",
      "Wardrobe review across 3 to 5 looks",
      "Location scout, 2 to 3 LA-based locations",
      "Shot list delivered and signed before shoot day",
      "Deployment context confirmed per image category",
    ],
    align: "left",
  },
  {
    n: "Block 2",
    title: "The Shoot",
    body: "One full day. Three to five wardrobe changes. Two to three locations. Direct creative direction on set. Every frame is shot against a specific deployment use case, not for range. The session is the product. The photos are the receipt.",
    items: [
      "One full shoot day",
      "3 to 5 wardrobe changes",
      "2 to 3 LA-based locations",
      "On-set direction by Bryceden Jones",
      "Each frame shot for a named deployment",
    ],
    align: "right",
  },
  {
    n: "Block 3",
    title: "Post-production and Delivery",
    body: "Sixty to eighty final images. Each one delivered pre-formatted for every deployment context the Kit supports. The gallery is structured and tagged. Pulling a frame for a press release does not require a side email to the photographer.",
    items: [
      "60 to 80 final images",
      "Pre-formatted per deployment context (LinkedIn hero, LinkedIn post, Instagram, press, speaking deck, podcast tile, web hero)",
      "Structured gallery, tagged by use case",
      "Delivered two weeks after shoot day",
      "High-resolution originals available on request",
    ],
    align: "left",
  },
  {
    n: "Block 4",
    title: "The 12-month Deployment Plan",
    body: "A month-by-month calendar paired with the gallery. Each month names the likely deployment surfaces, the images that hold for them, and the caption angles worth considering. One mid-year check-in at month six to catch anything off.",
    items: [
      "Month-by-month deployment calendar",
      "Specific image paired with specific use",
      "Caption angles per deployment",
      "Mid-year check-in at month six",
      "Plan revises once per year if the Kit is renewed",
    ],
    align: "right",
  },
];

const notInsideLines = [
  "Corporate team headshots. Event coverage. Weddings, family, grad, actor or model work. Ongoing monthly photography retainers.",
  "These are different engagements, and different operators serve them better. Referrals available on the qualifying call.",
];

export default function KitPage() {
  return (
    <>
      <section className="flex min-h-[70vh] items-center border-b border-border bg-foreground py-section text-background">
        <Container>
          <div className="mx-auto max-w-4xl text-center">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-accent-bright">
              The Founder Kit
            </span>
            <h1 className="mt-8 font-heading text-4xl font-bold leading-[1.05] tracking-tight text-balance sm:text-6xl lg:text-7xl">
              $12,500. One shoot. A library for twelve months.
            </h1>
            <p className="mx-auto mt-8 max-w-2xl text-lg leading-relaxed text-background/85">
              Fixed scope. Fixed price. Series A to C founders, LA metro.
            </p>
            <div className="mt-12 flex justify-center">
              <Link
                href="/book"
                className="inline-flex h-14 items-center justify-center bg-background px-8 text-base font-semibold text-foreground transition-colors hover:bg-background/90"
              >
                Book a Qualifying Call
              </Link>
            </div>
          </div>
        </Container>
      </section>

      <section className="relative bg-background py-section">
        <GridOverlay />
        <Container className="relative z-10">
          <SectionMarker n="01" label="What's Inside" />
          <div className="mt-12 mb-16 max-w-3xl">
            <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
              Four blocks. One engagement.
            </h2>
          </div>

          <div className="space-y-20">
            {blocks.map((b) => (
              <FadeIn key={b.n}>
                <article
                  className={`grid grid-cols-1 gap-10 border-t border-border pt-10 lg:grid-cols-2 lg:gap-16 ${
                    b.align === "right" ? "lg:[&>*:first-child]:order-2" : ""
                  }`}
                >
                  <div>
                    <span className="font-heading text-xs font-semibold tracking-[0.3em] uppercase text-muted">
                      {b.n}
                    </span>
                    <h3 className="mt-4 font-heading text-2xl font-medium tracking-tight text-foreground sm:text-3xl">
                      {b.title}
                    </h3>
                    <p className="mt-6 max-w-xl text-base text-foreground/80 leading-relaxed">
                      {b.body}
                    </p>
                  </div>

                  <ul className="space-y-3 self-center">
                    {b.items.map((item) => (
                      <li
                        key={item}
                        className="flex items-start gap-3 border-b border-border/60 pb-3 text-base text-foreground/85 leading-relaxed last:border-b-0 last:pb-0"
                      >
                        <span
                          aria-hidden="true"
                          className="mt-[0.55rem] h-1.5 w-1.5 flex-shrink-0 bg-foreground"
                        />
                        <span>{item}</span>
                      </li>
                    ))}
                  </ul>
                </article>
              </FadeIn>
            ))}
          </div>
        </Container>
      </section>

      <section className="relative border-t border-border bg-surface py-section">
        <GridOverlay />
        <Container className="relative z-10">
          <SectionMarker n="02" label="What's Not Inside" />
          <div className="mx-auto mt-12 max-w-3xl space-y-6">
            {notInsideLines.map((line, i) => (
              <p
                key={i}
                className="text-lg text-foreground/75 leading-relaxed"
              >
                {line}
              </p>
            ))}
          </div>
        </Container>
      </section>

      <section className="relative border-t border-border bg-background py-section">
        <GridOverlay />
        <Container className="relative z-10">
          <SectionMarker n="03" label="Pricing and Timing" />
          <div className="mx-auto max-w-3xl text-center">
            <div className="mt-16 space-y-6 font-heading tabular-nums">
              <p className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl">
                $12,500 total.
              </p>
              <p className="text-2xl font-medium tracking-tight text-foreground/85 sm:text-3xl lg:text-4xl">
                50% at booking. 50% at delivery.
              </p>
              <p className="text-2xl font-medium tracking-tight text-foreground/85 sm:text-3xl lg:text-4xl">
                Delivered in 4 to 6 weeks.
              </p>
            </div>
            <div className="mt-14 flex justify-center">
              <Link
                href="/book"
                className="inline-flex h-14 items-center justify-center bg-foreground px-8 text-base font-semibold text-background transition-colors hover:bg-foreground/90"
              >
                Book a Qualifying Call
              </Link>
            </div>
          </div>
        </Container>
      </section>
    </>
  );
}
