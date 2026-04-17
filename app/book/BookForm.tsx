"use client";

import { useState } from "react";
import { useSearchParams } from "next/navigation";

const FORMSPREE_ENDPOINT = "https://formspree.io/f/xlgpgozq";

const PIXIESET_URLS: Record<"baseline" | "standard", string> = {
  baseline: "https://snipedmedia.pixieset.com/booking/tier-1-the-baseline",
  standard: "https://snipedmedia.pixieset.com/booking/tier-2-the-standard",
};

const EVENTS_SUCCESS_MESSAGE =
  "Received. Events require custom blocking. We'll follow up within 24 hours with a tailored scope and quote.";

const PIXIESET_PENDING_MESSAGE =
  "Received. We'll send your secure booking link within 24 hours so you can lock in a time.";

type TierId = "baseline" | "standard" | "events";

type TierOption = {
  id: TierId;
  fullLabel: string;
  label: string;
  detail: string;
};

const tierOptions: TierOption[] = [
  {
    id: "baseline",
    fullLabel: "Tier 1: The Baseline ($275)",
    label: "The Baseline · $275",
    detail: "45 minutes, one location, 5 retouched images. Best for individuals and headshots.",
  },
  {
    id: "standard",
    fullLabel: "Tier 2: The Standard ($550)",
    label: "The Standard · $550",
    detail: "Up to 90 minutes, multiple looks, 15 to 20 retouched images. Best for families and lifestyle.",
  },
  {
    id: "events",
    fullLabel: "Tier 3: Event Coverage ($1,200+)",
    label: "Event Coverage · from $1,200",
    detail: "4 hours of coverage, 50+ delivered images. Best for banquets and local campaigns.",
  },
];

type Status = "idle" | "submitting" | "error" | "success";

export function BookForm() {
  const searchParams = useSearchParams();
  const preselectedTierId = searchParams.get("tier");
  const defaultTierId = tierOptions.find((t) => t.id === preselectedTierId)?.id;

  const [status, setStatus] = useState<Status>("idle");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string>("");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("submitting");
    setErrorMessage(null);

    const form = e.currentTarget;
    const formData = new FormData(form);
    const selectedId = String(formData.get("tier") ?? "") as TierId;
    const tier = tierOptions.find((t) => t.id === selectedId);

    if (!tier) {
      setErrorMessage("Please select a coverage tier.");
      setStatus("error");
      return;
    }

    formData.set("tier", tier.fullLabel);
    formData.set(
      "_subject",
      `New Sniped Media inquiry · ${tier.fullLabel}`
    );

    try {
      const response = await fetch(FORMSPREE_ENDPOINT, {
        method: "POST",
        body: formData,
        headers: { Accept: "application/json" },
      });

      if (!response.ok) {
        const data = await response.json().catch(() => null);
        const msg =
          data?.errors?.map((err: { message: string }) => err.message).join(" ") ??
          "Submission failed. Please try again.";
        setErrorMessage(msg);
        setStatus("error");
        return;
      }

      if (tier.id === "events") {
        setSuccessMessage(EVENTS_SUCCESS_MESSAGE);
        setStatus("success");
        form.reset();
        return;
      }

      const redirectUrl = PIXIESET_URLS[tier.id];
      if (redirectUrl) {
        window.location.href = redirectUrl;
        return;
      }

      setSuccessMessage(PIXIESET_PENDING_MESSAGE);
      setStatus("success");
      form.reset();
    } catch {
      setErrorMessage("Network error. Please try again.");
      setStatus("error");
    }
  }

  if (status === "success") {
    return (
      <div className="border border-border bg-surface p-10 text-center">
        <h2 className="font-heading text-2xl font-semibold text-foreground">
          Inquiry received.
        </h2>
        <p className="mt-4 text-muted">{successMessage}</p>
      </div>
    );
  }

  const isSubmitting = status === "submitting";
  const inputClass =
    "w-full border border-border bg-background px-3 py-3 text-foreground outline-none transition-colors focus:border-foreground";
  const labelClass = "block text-sm font-semibold text-foreground";

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-6 border border-border bg-surface p-8 md:p-10"
    >
      <div className="grid gap-6 md:grid-cols-2">
        <div className="space-y-2">
          <label htmlFor="name" className={labelClass}>
            Full Name
          </label>
          <input
            required
            type="text"
            id="name"
            name="name"
            autoComplete="name"
            className={inputClass}
          />
        </div>
        <div className="space-y-2">
          <label htmlFor="email" className={labelClass}>
            Email Address
          </label>
          <input
            required
            type="email"
            id="email"
            name="email"
            autoComplete="email"
            className={inputClass}
          />
        </div>
      </div>

      <div className="space-y-2">
        <label htmlFor="phone" className={labelClass}>
          Phone Number
        </label>
        <input
          required
          type="tel"
          id="phone"
          name="phone"
          autoComplete="tel"
          className={inputClass}
        />
      </div>

      <div className="space-y-2">
        <label htmlFor="scope" className={labelClass}>
          What are we shooting?
        </label>
        <textarea
          required
          id="scope"
          name="scope"
          rows={3}
          placeholder="e.g., Dance headshots for my daughter, or a 3-hour church banquet."
          className={`${inputClass} resize-none`}
        />
      </div>

      <fieldset className="space-y-3 border-t border-border pt-6">
        <legend className="font-heading text-sm font-semibold uppercase tracking-[0.2em] text-foreground">
          Select Your Coverage Tier
        </legend>
        <div className="space-y-3">
          {tierOptions.map((t) => (
            <label
              key={t.id}
              className="flex cursor-pointer items-start gap-3 border border-border p-4 transition-colors hover:border-foreground has-[:checked]:border-foreground has-[:checked]:bg-background"
            >
              <input
                required
                type="radio"
                name="tier"
                value={t.id}
                defaultChecked={t.id === defaultTierId}
                className="mt-1 h-4 w-4 accent-foreground"
              />
              <span className="block">
                <span className="block font-semibold text-foreground">{t.label}</span>
                <span className="mt-1 block text-sm text-muted">{t.detail}</span>
              </span>
            </label>
          ))}
        </div>
      </fieldset>

      {status === "error" && errorMessage ? (
        <p className="border border-foreground bg-background px-4 py-3 text-sm text-foreground">
          {errorMessage}
        </p>
      ) : null}

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full bg-foreground px-6 py-4 font-semibold text-background transition-colors hover:bg-foreground/90 disabled:opacity-50"
      >
        {isSubmitting ? "Submitting…" : "Continue to Booking"}
      </button>
    </form>
  );
}
