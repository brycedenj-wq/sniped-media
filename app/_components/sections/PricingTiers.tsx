import { Container } from "../Container";
import { CtaButton } from "../CtaButton";

type Tier = {
  name: string;
  price: string;
  priceSuffix?: string;
  target: string;
  scope: string;
  deliverables: string;
  cta: string;
  href: string;
};

const tiers: Tier[] = [
  {
    name: "The Baseline",
    price: "$275",
    target: "Individual portraits, headshots, or graduation updates.",
    scope: "45 minutes of expert direction, one location.",
    deliverables: "5 final retouched images selected from a digital proofing gallery. Full payment secures your date.",
    cta: "Book The Baseline",
    href: "/book?tier=baseline",
  },
  {
    name: "The Standard",
    price: "$550",
    target: "Families, couples, and extended lifestyle shoots.",
    scope: "Up to 90 minutes of dedicated direction with multiple looks.",
    deliverables: "10 to 15 final retouched images. 50% retainer holds your date; balance auto-invoiced 48 hours prior.",
    cta: "Book The Standard",
    href: "/book?tier=standard",
  },
  {
    name: "Event Coverage",
    price: "$1,200",
    priceSuffix: "starting",
    target: "Local organizations, church banquets, and brand activations.",
    scope: "4 hours of comprehensive, hands-off coverage.",
    deliverables: "Full digital proofing gallery with 50+ final delivered images.",
    cta: "Inquire for Events",
    href: "/book?tier=events",
  },
];

export function PricingTiers() {
  return (
    <section className="py-section">
      <Container>
        <div className="grid gap-6 lg:grid-cols-3">
          {tiers.map((t) => (
            <div
              key={t.name}
              className="flex flex-col border border-border bg-surface p-8"
            >
              <h3 className="font-heading text-xl font-semibold text-foreground">
                {t.name}
              </h3>
              <div className="mt-4 flex items-baseline gap-2">
                <span className="font-heading text-4xl font-semibold tracking-tight text-foreground">
                  {t.price}
                </span>
                {t.priceSuffix ? (
                  <span className="text-sm text-muted">{t.priceSuffix}</span>
                ) : null}
              </div>
              <dl className="mt-8 space-y-5 text-sm">
                <div>
                  <dt className="font-semibold text-foreground">Target</dt>
                  <dd className="mt-1 text-muted">{t.target}</dd>
                </div>
                <div>
                  <dt className="font-semibold text-foreground">Scope</dt>
                  <dd className="mt-1 text-muted">{t.scope}</dd>
                </div>
                <div>
                  <dt className="font-semibold text-foreground">Deliverables</dt>
                  <dd className="mt-1 text-muted">{t.deliverables}</dd>
                </div>
              </dl>
              <div className="mt-10 pt-6 border-t border-border">
                <CtaButton href={t.href} size="md" className="w-full">
                  {t.cta}
                </CtaButton>
              </div>
            </div>
          ))}
        </div>
      </Container>
    </section>
  );
}
