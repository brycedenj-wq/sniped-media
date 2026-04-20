"use client";

import { useState } from "react";
import { useSearchParams } from "next/navigation";
import { activeBookableTiers, type BookableTier } from "../_data/campaigns";

const FORMSPREE_ENDPOINT = "https://formspree.io/f/xlgpgozq";

const MANUAL_FOLLOWUP_MESSAGE =
  "Received. This coverage requires custom blocking. We'll follow up within 24 hours with a tailored scope and quote.";

const PIXIESET_PENDING_MESSAGE =
  "Received. We'll send your secure booking link within 24 hours so you can lock in a time.";

type Status = "idle" | "submitting" | "error" | "success";

export function BookForm() {
  const searchParams = useSearchParams();
  const preselectedTierId = searchParams.get("tier");
  const defaultTierId = activeBookableTiers.find((t) => t.id === preselectedTierId)?.id;

  const [status, setStatus] = useState<Status>("idle");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string>("");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("submitting");
    setErrorMessage(null);

    const form = e.currentTarget;
    const formData = new FormData(form);
    const selectedId = String(formData.get("tier") ?? "");
    const tier = activeBookableTiers.find((t) => t.id === selectedId);

    if (!tier) {
      setErrorMessage("Please select a coverage tier.");
      setStatus("error");
      return;
    }

    formData.set("tier", tier.fullLabel);
    formData.set("_subject", `New Sniped Media inquiry · ${tier.fullLabel}`);

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

      if (tier.pixiesetUrl) {
        window.location.href = tier.pixiesetUrl;
        return;
      }

      setSuccessMessage(
        tier.category === "base" ? MANUAL_FOLLOWUP_MESSAGE : PIXIESET_PENDING_MESSAGE
      );
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
          placeholder="e.g., Grad portraits at USC, or Mother's Day with 3 generations."
          className={`${inputClass} resize-none`}
        />
      </div>

      <fieldset className="space-y-3 border-t border-border pt-6">
        <legend className="font-heading text-sm font-semibold uppercase tracking-[0.2em] text-foreground">
          Select Your Coverage
        </legend>
        <p className="text-xs text-muted">
          Limited-time sessions are listed first. Base packages are always available.
        </p>
        <div className="space-y-3 pt-2">
          {activeBookableTiers.map((t: BookableTier) => (
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
                {t.tagline ? (
                  <span className="mt-1 block font-heading text-[11px] font-semibold tracking-[0.15em] uppercase text-foreground/70">
                    {t.tagline}
                  </span>
                ) : null}
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
