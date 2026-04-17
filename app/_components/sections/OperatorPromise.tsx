import { Container } from "../Container";

type Promise = {
  number: string;
  title: string;
  body: string;
};

const promises: Promise[] = [
  {
    number: "01",
    title: "Expert Direction",
    body: "No awkward posing. We guide you step-by-step to eliminate physical tension so you look your absolute best.",
  },
  {
    number: "02",
    title: "Transparent Pricing",
    body: "No hidden fees, no guessing games. What you see on our site is exactly what you pay.",
  },
  {
    number: "03",
    title: "Seamless Delivery",
    body: "Lightning-fast digital galleries with automated access to premium lab prints.",
  },
];

export function OperatorPromise() {
  return (
    <section className="border-t border-border bg-surface py-section">
      <Container>
        <div className="grid gap-12 sm:grid-cols-2 lg:grid-cols-3">
          {promises.map((p) => (
            <div key={p.number}>
              <span className="font-heading text-sm font-semibold tracking-[0.2em] text-muted">
                {p.number}
              </span>
              <h3 className="mt-4 font-heading text-xl font-semibold text-foreground">
                {p.title}
              </h3>
              <p className="mt-3 text-sm leading-relaxed text-muted">{p.body}</p>
            </div>
          ))}
        </div>
      </Container>
    </section>
  );
}
