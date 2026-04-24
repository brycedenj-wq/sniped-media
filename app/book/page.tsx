import type { Metadata } from "next";
import { Suspense } from "react";
import { Container } from "../_components/Container";
import { BookForm } from "./BookForm";

export const metadata: Metadata = {
  title: "Book a Qualifying Call",
  description:
    "Book a 20-minute qualifying call for the Sniped Media Founder Kit. Fit confirmed or respectfully declined with referrals.",
  openGraph: {
    title: "Book a Qualifying Call | Sniped Media",
    description:
      "Book a 20-minute qualifying call for the Sniped Media Founder Kit. Fit confirmed or respectfully declined with referrals.",
    url: "/book",
  },
  robots: { index: true, follow: true },
};

export default function BookPage() {
  return (
    <section className="min-h-[calc(100vh-4rem)] bg-background py-section">
      <Container>
        <div className="grid grid-cols-1 gap-12 lg:grid-cols-[minmax(0,2fr)_minmax(0,3fr)] lg:gap-20">
          <div className="lg:pt-4">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
              Qualifying Call
            </span>
            <h1 className="mt-6 font-heading text-4xl font-medium leading-[1.05] tracking-tight text-balance sm:text-5xl">
              Book a 20-minute qualifying call.
            </h1>
            <p className="mt-6 text-lg text-foreground/80 leading-relaxed">
              Fit confirmed or respectfully declined with referrals.
            </p>
            <p className="mt-3 text-sm text-muted">
              You&apos;ll hear back within 48 hours.
            </p>
          </div>

          <div>
            <Suspense fallback={<div className="h-96 border border-border bg-surface" />}>
              <BookForm />
            </Suspense>
          </div>
        </div>
      </Container>
    </section>
  );
}
