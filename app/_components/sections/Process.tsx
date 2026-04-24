import { Container } from "../Container";
import { SectionMarker } from "../SectionMarker";

const steps = [
  {
    n: "01",
    title: "The call.",
    body: "Twenty minutes. Fit confirmed, or declined with a referral to a photographer who fits. No pitch. No deck.",
  },
  {
    n: "02",
    title: "The build.",
    body: "Creative direction, wardrobe review, location scout, shot list. Signed off before the shoot day. Nothing improvised on set.",
  },
  {
    n: "03",
    title: "The shoot and the deploy.",
    body: "One shoot day. Gallery delivered in two weeks. Deployment plan delivered with the gallery. From there, the system runs.",
  },
];

export function Process() {
  return (
    <section className="border-t border-border bg-foreground py-section text-background">
      <Container>
        <SectionMarker n="05" label="Process" tone="dark" />

        <div className="mt-12 mb-16 max-w-3xl">
          <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
            Three steps. No drift.
          </h2>
        </div>

        <div className="grid grid-cols-1 gap-16 sm:grid-cols-3 sm:gap-10 lg:gap-16">
          {steps.map((s) => (
            <div key={s.n}>
              <span
                aria-hidden="true"
                className="block font-heading text-6xl font-bold leading-none tracking-tight tabular-nums text-accent-bright sm:text-7xl lg:text-8xl"
              >
                {s.n}
              </span>
              <h3 className="mt-8 font-heading text-xl font-medium tracking-tight text-background sm:text-2xl">
                {s.title}
              </h3>
              <p className="mt-4 text-base text-background/75 leading-relaxed">
                {s.body}
              </p>
            </div>
          ))}
        </div>
      </Container>
    </section>
  );
}
