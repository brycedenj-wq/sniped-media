import Image from "next/image";
import Link from "next/link";
import { Container } from "../Container";

type Category = {
  title: string;
  description: string;
  image: string;
  href: string;
};

const categories: Category[] = [
  {
    title: "Portraits & Headshots",
    description: "Sharp execution for individuals and professionals.",
    image: "/images/work-portraits.jpg",
    href: "/portfolio-pricing",
  },
  {
    title: "Lifestyle & Family",
    description: "Directed, natural imagery for groups and couples.",
    image: "/images/work-lifestyle.jpg",
    href: "/portfolio-pricing",
  },
  {
    title: "Event Coverage",
    description: "Reliable, hands-off documentation for local organizations.",
    image: "/images/work-events.jpg",
    href: "/portfolio-pricing",
  },
];

export function WorkTeaser() {
  return (
    <section className="py-section">
      <Container>
        <div className="flex items-end justify-between gap-8">
          <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
            The Work
          </h2>
        </div>
        <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {categories.map((c) => (
            <Link
              key={c.title}
              href={c.href}
              className="group block"
            >
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/10">
                <Image
                  src={c.image}
                  alt={c.title}
                  fill
                  sizes="(min-width: 1024px) 33vw, (min-width: 640px) 50vw, 100vw"
                  className="object-cover transition-transform duration-500 group-hover:scale-[1.02]"
                />
              </div>
              <div className="mt-4">
                <h3 className="font-heading text-lg font-semibold text-foreground">
                  {c.title}
                </h3>
                <p className="mt-1 text-sm text-muted">{c.description}</p>
              </div>
            </Link>
          ))}
        </div>
      </Container>
    </section>
  );
}
