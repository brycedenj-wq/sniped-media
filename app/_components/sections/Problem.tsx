import { Container } from "../Container";
import { GridOverlay } from "../GridOverlay";
import { SectionMarker } from "../SectionMarker";

export function Problem() {
  return (
    <section className="relative border-t border-border bg-background py-section">
      <GridOverlay />
      <Container className="relative z-10">
        <SectionMarker n="01" label="The Problem" />
        <div className="mt-12 max-w-3xl space-y-6">
          <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
            Your imagery was taken three years ago.
          </h2>
          <p className="text-lg text-foreground/80 leading-relaxed">
            You are raising rounds, speaking at events, appearing in press, posting on LinkedIn multiple times a week. The photo doing all of it was shot by a friend at a Series A announcement three years ago.
          </p>
          <p className="text-lg text-foreground/80 leading-relaxed">
            The imagery costs you in places that do not show up in a dashboard. The candidate who clicked away from the team page. The press placement that used someone else&apos;s headshot as the cover. The investor who noticed the LinkedIn photo does not match the deck.
          </p>
          <p className="text-lg text-foreground/80 leading-relaxed">
            The fix is not another headshot. The fix is a different kind of engagement.
          </p>
        </div>
      </Container>
    </section>
  );
}
