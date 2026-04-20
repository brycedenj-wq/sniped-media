import type { Metadata } from "next";
import { Suspense } from "react";
import { Container } from "../_components/Container";
import { BookForm } from "./BookForm";

export const metadata: Metadata = {
  title: "Book a Session",
  description:
    "Check availability and book your Los Angeles portrait, lifestyle, or event session. Transparent pricing, secure invoicing, zero friction.",
  openGraph: {
    title: "Book a Session | Sniped Media",
    description:
      "Check availability and book your Los Angeles portrait, lifestyle, or event session. Transparent pricing, secure invoicing, zero friction.",
    url: "/book",
  },
  robots: { index: true, follow: true },
};

export default function BookPage() {
  return (
    <section className="py-section">
      <Container>
        <div className="mx-auto max-w-2xl">
          <div className="mb-12 text-center">
            <h1 className="font-heading text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
              Check Availability &amp; Book.
            </h1>
            <p className="mt-6 text-lg text-muted">
              Every active session is listed below: limited-time campaigns at the top, base packages always available. Most tiers route to our secure calendar on submission; event coverage receives a tailored follow-up within 24 hours.
            </p>
          </div>
          <Suspense fallback={<div className="h-96 border border-border bg-surface" />}>
            <BookForm />
          </Suspense>
        </div>
      </Container>
    </section>
  );
}
