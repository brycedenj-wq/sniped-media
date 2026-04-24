import Link from "next/link";
import { Container } from "./Container";

export function SiteFooter() {
  const year = new Date().getFullYear();

  return (
    <footer className="mt-auto border-t border-accent bg-foreground text-background">
      <Container className="grid grid-cols-1 gap-12 py-16 sm:grid-cols-2 lg:grid-cols-4 lg:py-16">
        <div>
          <Link
            href="/"
            className="font-heading text-sm font-semibold tracking-[0.2em] uppercase text-background"
          >
            Sniped Media
          </Link>
          <p className="mt-4 font-heading text-base leading-snug text-background">
            The commercial portrait system for LA founders.
          </p>
        </div>

        <nav className="flex flex-col gap-3 text-sm">
          <span className="font-heading text-xs font-semibold tracking-[0.3em] uppercase text-background/60">
            Site
          </span>
          <Link href="/kit" className="text-background/85 hover:text-accent-bright">
            The Kit
          </Link>
          <Link href="/about" className="text-background/85 hover:text-accent-bright">
            About
          </Link>
          <Link href="/book" className="text-background/85 hover:text-accent-bright">
            Book
          </Link>
        </nav>

        <div className="flex flex-col gap-3 text-sm">
          <span className="font-heading text-xs font-semibold tracking-[0.3em] uppercase text-background/60">
            Contact
          </span>
          <a
            href="mailto:hello@snipedmedia.com"
            className="text-background/85 hover:text-accent-bright"
          >
            hello@snipedmedia.com
          </a>
          <p className="text-background/70">Los Angeles, CA</p>
        </div>

        <div className="flex flex-col gap-3 text-sm">
          <span className="font-heading text-xs font-semibold tracking-[0.3em] uppercase text-background/60">
            Social
          </span>
          <a
            href="https://instagram.com/sniped.media"
            target="_blank"
            rel="noopener noreferrer"
            className="text-background/85 hover:text-accent-bright"
            aria-label="Sniped Media on Instagram"
          >
            Instagram
          </a>
          <a
            href="https://linkedin.com/in/brycedenjones"
            target="_blank"
            rel="noopener noreferrer"
            className="text-background/85 hover:text-accent-bright"
            aria-label="Bryceden Jones on LinkedIn"
          >
            LinkedIn
          </a>
        </div>
      </Container>

      <Container className="border-t border-background/10 py-6">
        <p className="text-xs text-background/55">
          © {year} Sniped Media. All rights reserved.
        </p>
      </Container>
    </footer>
  );
}
