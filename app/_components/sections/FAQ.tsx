import { Container } from "../Container";
import { GridOverlay } from "../GridOverlay";
import { SectionMarker } from "../SectionMarker";

type Item = { q: string; a: string };

const items: Item[] = [
  {
    q: "How long from booking to final delivery?",
    a: "Four to six weeks. Two weeks pre-production, one shoot day, two weeks post.",
  },
  {
    q: "What if I need more than one shoot day?",
    a: "The Kit is one shoot day. If a second is genuinely needed, it is priced as a separate add-on with its own fixed scope. Not absorbed.",
  },
  {
    q: "Can I add my team?",
    a: "No. The Kit is a founder portrait library. Team headshots are a different engagement, and not one Sniped Media takes on.",
  },
  {
    q: "Where do the shoots happen?",
    a: "LA metro. Two to three locations chosen during creative direction.",
  },
  {
    q: "What does the deployment plan look like?",
    a: "A month-by-month calendar pairing specific images with specific use cases. LinkedIn posts, press, decks, podcasts, year-end content. Delivered with the gallery. One mid-year check-in at month six.",
  },
];

export function FAQ() {
  return (
    <section className="relative border-y border-border bg-surface py-section">
      <GridOverlay />
      <Container className="relative z-10">
        <SectionMarker n="07" label="FAQ" />

        <div className="mt-12 mb-12 max-w-3xl">
          <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
            Five questions. Five answers.
          </h2>
        </div>

        <dl className="mx-auto max-w-3xl divide-y divide-border">
          {items.map((item, i) => (
            <div key={item.q} className="grid grid-cols-[auto_1fr] gap-6 py-8">
              <span className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-muted tabular-nums">
                {String(i + 1).padStart(2, "0")}
              </span>
              <div>
                <dt className="font-heading text-lg font-medium text-foreground sm:text-xl">
                  {item.q}
                </dt>
                <dd className="mt-3 text-base text-foreground/75 leading-relaxed">
                  {item.a}
                </dd>
              </div>
            </div>
          ))}
        </dl>
      </Container>
    </section>
  );
}
