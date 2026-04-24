import Link from "next/link";
import { Container } from "../Container";
import { GridOverlay } from "../GridOverlay";
import { SectionMarker } from "../SectionMarker";

const bullets = [
  "A library instead of a session. 60 to 80 final images, one shoot day, structured for deployment.",
  "Three to five looks across two to three locations. Every frame has a use before the camera comes out.",
  "Pre-formatted for LinkedIn, press, speaking decks, team pages, podcast tiles, web hero.",
  "A 12-month deployment plan. You stop wondering which photo to post.",
  "Direct creative direction by Bryceden Jones. Not assistants. Not a team. The shoot is him.",
];

export function KitSummary() {
  return (
    <section className="relative border-y border-border bg-surface py-section">
      <GridOverlay />
      <Container className="relative z-10">
        <SectionMarker n="02" label="The Offer" />
        <div className="mt-12 grid grid-cols-1 gap-12 lg:grid-cols-[1fr_1.1fr] lg:gap-20">
          <div>
            <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
              The Founder Kit.
            </h2>
            <p className="mt-6 max-w-sm text-base text-foreground/80 leading-relaxed">
              One product. One buyer. One standard of delivery.
            </p>
          </div>

          <div>
            <ul className="space-y-4 text-base text-foreground/85 leading-relaxed">
              {bullets.map((b) => (
                <li key={b} className="flex items-start gap-3">
                  <span
                    aria-hidden="true"
                    className="mt-[0.55rem] h-1.5 w-1.5 flex-shrink-0 bg-foreground"
                  />
                  <span>{b}</span>
                </li>
              ))}
            </ul>

            <div className="mt-12 flex flex-col gap-8 border-t border-border pt-10 sm:flex-row sm:items-end sm:justify-between">
              <div>
                <span className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-muted tabular-nums">
                  Investment
                </span>
                <p className="mt-2 font-heading text-5xl font-bold tracking-tight text-foreground tabular-nums sm:text-6xl lg:text-7xl">
                  $12,500
                </p>
                <p className="mt-3 text-sm text-muted">
                  Fixed scope. Fixed price.
                </p>
              </div>

              <Link
                href="/kit"
                className="inline-flex h-12 items-center justify-center self-start border border-foreground px-6 text-sm font-semibold text-foreground transition-colors hover:bg-foreground hover:text-background sm:self-end"
              >
                See the Founder Kit
              </Link>
            </div>
          </div>
        </div>
      </Container>
    </section>
  );
}
