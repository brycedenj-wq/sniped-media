import { Container } from "../Container";
import { GridOverlay } from "../GridOverlay";
import { SectionMarker } from "../SectionMarker";

const forYou = [
  "Series A to Series C founder or senior operator, LA metro.",
  "Running a personal brand alongside the company.",
  "Last imagery is older than your last funding round.",
];

const notForYou = [
  "Looking for corporate team headshots.",
  "Need events, weddings, grad, actor, or model work.",
  "Expecting an agency to run your brand end to end.",
];

export function AudienceFit() {
  return (
    <section className="relative border-t border-border bg-background py-section">
      <GridOverlay />
      <Container className="relative z-10">
        <SectionMarker n="06" label="Audience" />
        <div className="mt-12 grid grid-cols-1 gap-12 sm:grid-cols-2 sm:gap-0">
          <div className="sm:pr-12 sm:border-r sm:border-border">
            <span className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-muted tabular-nums">
              For You If
            </span>
            <ul className="mt-8 space-y-4">
              {forYou.map((point) => (
                <li
                  key={point}
                  className="flex items-start gap-3 text-base text-foreground/85 leading-relaxed"
                >
                  <span
                    aria-hidden="true"
                    className="mt-[0.55rem] h-1.5 w-1.5 flex-shrink-0 bg-accent"
                  />
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="sm:pl-12">
            <span className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-muted tabular-nums">
              Not For You If
            </span>
            <ul className="mt-8 space-y-4">
              {notForYou.map((point) => (
                <li
                  key={point}
                  className="flex items-start gap-3 text-base text-foreground/70 leading-relaxed"
                >
                  <span
                    aria-hidden="true"
                    className="mt-[0.55rem] h-1.5 w-1.5 flex-shrink-0 bg-muted"
                  />
                  <span>{point}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </Container>
    </section>
  );
}
