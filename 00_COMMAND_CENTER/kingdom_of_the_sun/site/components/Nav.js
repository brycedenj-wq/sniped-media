"use client";
import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

// Desktop bar: the essentials, kept to a count that never crowds the brand or CTA.
const LINKS = [
  { href: "/tournament", label: "Tournament" },
  { href: "/history", label: "History" },
  { href: "/champions", label: "Champions" },
  { href: "/alumni", label: "Alumni" },
  { href: "/teams", label: "Teams" },
  { href: "/schedule", label: "Schedule" },
  { href: "/watch", label: "Watch" },
  { href: "/sponsors", label: "Sponsors" },
];
// Mobile menu: the full set, where there is room for everything.
const MOBILE_LINKS = [
  { href: "/", label: "Home" },
  ...LINKS,
  { href: "/records", label: "Records" },
];

export default function Nav() {
  const [open, setOpen] = useState(false);
  const path = usePathname();
  const isActive = (href) => (href === "/" ? path === "/" : path.startsWith(href));

  return (
    <header className="nav">
      <div className="bar">
        <Link className="brand" href="/" onClick={() => setOpen(false)}>
          <img src="/crown.svg" alt="" />
          <span>Kingdom of the Sun</span>
        </Link>
        <nav className="nav-links">
          {LINKS.map((l) => (
            <Link key={l.href} href={l.href} className={isActive(l.href) ? "active" : ""}>
              {l.label}
            </Link>
          ))}
        </nav>
        <Link className="btn nav-cta" href="/confirm">Confirm Spot</Link>
        <button className="nav-toggle" aria-label="Menu" onClick={() => setOpen((o) => !o)}>
          <span></span><span></span><span></span>
        </button>
      </div>
      {open && (
        <div className="mobile-menu">
          {MOBILE_LINKS.map((l) => (
            <Link key={l.href} href={l.href} className={isActive(l.href) ? "active" : ""} onClick={() => setOpen(false)}>
              {l.label}
            </Link>
          ))}
          <Link className="btn" href="/confirm" onClick={() => setOpen(false)}>Confirm Spot</Link>
        </div>
      )}
    </header>
  );
}
