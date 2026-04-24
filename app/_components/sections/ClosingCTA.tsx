import Link from "next/link";
import { Container } from "../Container";

export function ClosingCTA() {
  return (
    <section className="border-t border-border bg-foreground py-section text-background">
      <Container>
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
            If your last brand imagery was produced before your Series A, it is overdue.
          </h2>
          <p className="mt-6 text-lg text-background/75 leading-relaxed">
            Book a 20-minute qualifying call.
          </p>
          <div className="mt-10 flex justify-center">
            <Link
              href="/book"
              className="inline-flex h-14 items-center justify-center bg-background px-8 text-base font-semibold text-foreground transition-colors hover:bg-background/90"
            >
              Book a Qualifying Call
            </Link>
          </div>
        </div>
      </Container>
    </section>
  );
}
