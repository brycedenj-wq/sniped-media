import { Container } from "../Container";

type Item = { q: string; a: string };

const items: Item[] = [
  {
    q: "Do I need to know how to pose?",
    a: "Not at all. We provide expert, step-by-step direction to eliminate awkwardness and ensure you look natural and confident.",
  },
  {
    q: "How do I select my photos?",
    a: "Within 48 hours of your shoot, you will receive a digital proofing gallery. You select your favorites based on your package limit, and we deliver the final retouched versions.",
  },
  {
    q: "Can I buy more than the 5 images included in The Baseline?",
    a: "Absolutely. If you fall in love with more than five, additional digital downloads and physical canvases can be purchased directly through your final gallery store.",
  },
  {
    q: "How do I lock in my date?",
    a: "Submit an intake form. If your date is available, you will receive a contract and invoice. Payment terms vary by tier: full payment for The Baseline, 50% retainer for The Standard with balance auto-invoiced 48 hours prior. Your date is locked the moment payment is received.",
  },
];

export function FAQ() {
  return (
    <section className="border-t border-border bg-surface py-section">
      <Container>
        <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
          Questions, answered.
        </h2>
        <dl className="mt-12 grid gap-10 sm:grid-cols-2">
          {items.map((item) => (
            <div key={item.q}>
              <dt className="font-heading text-base font-semibold text-foreground">
                {item.q}
              </dt>
              <dd className="mt-2 text-sm leading-relaxed text-muted">{item.a}</dd>
            </div>
          ))}
        </dl>
      </Container>
    </section>
  );
}
