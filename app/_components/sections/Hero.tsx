import Image from "next/image";
import { Container } from "../Container";
import { CtaButton } from "../CtaButton";

export function Hero() {
  return (
    <section className="relative isolate flex min-h-[85vh] items-end overflow-hidden bg-foreground text-background">
      <Image
        src="/images/hero.jpg"
        alt=""
        fill
        priority
        sizes="100vw"
        className="absolute inset-0 -z-10 object-cover opacity-80"
      />
      <div className="absolute inset-0 -z-10 bg-gradient-to-t from-foreground/80 via-foreground/30 to-transparent" />

      <Container className="py-section">
        <div className="max-w-3xl">
          <h1 className="font-heading text-4xl font-semibold tracking-tight text-balance sm:text-5xl lg:text-6xl">
            Capture the Moment. Skip the Friction.
          </h1>
          <p className="mt-6 max-w-xl text-lg text-background/80">
            Expertly directed portraits and reliable event coverage. See our pricing and book instantly.
          </p>
          <div className="mt-10 flex flex-wrap items-center gap-4">
            <CtaButton href="/portfolio-pricing" size="lg">
              View Pricing &amp; Book
            </CtaButton>
            <CtaButton href="/book" size="lg" variant="secondary" className="border-background text-background hover:bg-background hover:text-foreground">
              Check Availability
            </CtaButton>
          </div>
        </div>
      </Container>
    </section>
  );
}
