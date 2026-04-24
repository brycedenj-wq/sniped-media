import Link from "next/link";
import { Container } from "./Container";
import { CtaButton } from "./CtaButton";
import { MobileMenu } from "./MobileMenu";

const navLinks = [
  { href: "/kit", label: "The Kit" },
  { href: "/about", label: "About" },
];

export function SiteHeader() {
  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/95 shadow-sm shadow-foreground/5 backdrop-blur-md supports-[backdrop-filter]:bg-background/80">
      <Container className="flex h-16 items-center justify-between lg:h-[72px]">
        <Link
          href="/"
          className="font-heading text-sm font-semibold tracking-[0.2em] uppercase text-foreground"
        >
          Sniped Media
        </Link>

        <nav className="hidden items-center gap-8 sm:flex">
          {navLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="text-sm font-medium text-foreground/75 transition-colors hover:text-foreground"
            >
              {link.label}
            </Link>
          ))}
        </nav>

        <div className="flex items-center gap-2">
          <CtaButton href="/book" size="sm" className="hidden sm:inline-flex">
            Book a Call
          </CtaButton>
          <MobileMenu />
        </div>
      </Container>
    </header>
  );
}
