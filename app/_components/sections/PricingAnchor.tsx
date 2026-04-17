import { Container } from "../Container";
import { CtaButton } from "../CtaButton";

export function PricingAnchor() {
  return (
    <section className="bg-foreground py-section text-background">
      <Container>
        <div className="max-w-3xl">
          <h2 className="font-heading text-3xl font-semibold tracking-tight text-balance sm:text-5xl">
            Unapologetic transparency.
          </h2>
          <p className="mt-6 max-w-2xl text-lg text-background/80">
            Premium Los Angeles photography shouldn&apos;t be a secret. Sessions starting at{" "}
            <span className="text-background">$275</span>.
          </p>
          <div className="mt-10">
            <CtaButton
              href="/portfolio-pricing"
              size="lg"
              variant="secondary"
              className="border-background text-background hover:bg-background hover:text-foreground"
            >
              View Packages
            </CtaButton>
          </div>
        </div>
      </Container>
    </section>
  );
}
