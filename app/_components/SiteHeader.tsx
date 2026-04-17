import Link from "next/link";
import { Container } from "./Container";
import { CtaButton } from "./CtaButton";

export function SiteHeader() {
  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/85 backdrop-blur">
      <Container className="flex h-16 items-center justify-between">
        <Link
          href="/"
          className="font-heading text-sm font-semibold tracking-[0.2em] uppercase text-foreground"
        >
          Sniped Media
        </Link>
        <CtaButton href="/book" size="sm">
          Check Availability
        </CtaButton>
      </Container>
    </header>
  );
}
