import Link from "next/link";
import { Container } from "./Container";

export function SiteFooter() {
  const year = new Date().getFullYear();

  return (
    <footer className="mt-auto border-t border-border bg-background">
      <Container className="flex flex-col gap-8 py-12 sm:flex-row sm:items-start sm:justify-between">
        <div className="max-w-sm">
          <Link
            href="/"
            className="font-heading text-sm font-semibold tracking-[0.2em] uppercase text-foreground"
          >
            Sniped Media
          </Link>
          <p className="mt-3 text-sm text-muted">
            High-impact Los Angeles photography. Transparent pricing, seamless delivery.
          </p>
        </div>

        <nav className="grid grid-cols-2 gap-x-10 gap-y-2 text-sm sm:flex sm:gap-8">
          <Link href="/portfolio-pricing" className="text-foreground hover:text-muted">
            Pricing
          </Link>
          <Link href="/book" className="text-foreground hover:text-muted">
            Book
          </Link>
          <a
            href="https://gallery.snipedmedia.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-foreground hover:text-muted"
          >
            Client Login
          </a>
        </nav>
      </Container>
      <Container className="border-t border-border py-6">
        <p className="text-xs text-muted">© {year} Sniped Media. All rights reserved.</p>
      </Container>
    </footer>
  );
}
