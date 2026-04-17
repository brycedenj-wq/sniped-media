import type { Metadata } from "next";
import { Container } from "../_components/Container";
import { PricingTiers } from "../_components/sections/PricingTiers";
import { FAQ } from "../_components/sections/FAQ";

export const metadata: Metadata = {
  title: "Pricing & Portfolio",
  description:
    "Transparent Los Angeles photography pricing. Portrait sessions from $275, lifestyle from $550, event coverage from $1,200.",
  openGraph: {
    title: "Pricing & Portfolio | Sniped Media",
    description:
      "Transparent Los Angeles photography pricing. Portrait sessions from $275, lifestyle from $550, event coverage from $1,200.",
    url: "/portfolio-pricing",
  },
};

export default function PortfolioPricingPage() {
  return (
    <>
      <section className="border-b border-border py-section">
        <Container>
          <div className="max-w-3xl">
            <h1 className="font-heading text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
              The Work &amp; The Investment.
            </h1>
            <p className="mt-6 max-w-2xl text-lg text-muted">
              High-impact execution across Los Angeles. We skip the creative ego and focus on what matters: expert direction, transparent costs, and lightning-fast delivery. Browse the galleries, select your tier, and secure your date.
            </p>
          </div>
        </Container>
      </section>

      <PricingTiers />
      <FAQ />
    </>
  );
}
