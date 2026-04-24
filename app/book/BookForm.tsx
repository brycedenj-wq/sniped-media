"use client";

import { useState } from "react";

const FORMSPREE_ENDPOINT = "https://formspree.io/f/xlgpgozq";

const SUCCESS_LINES = [
  "If there is fit, a reply lands within 48 hours with two or three times for a qualifying call.",
  "If there is not fit, a reply lands within 48 hours with a referral to a photographer who will serve the work better.",
  "Either way, a reply lands.",
];

type Status = "idle" | "submitting" | "error" | "success";

export function BookForm() {
  const [status, setStatus] = useState<Status>("idle");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("submitting");
    setErrorMessage(null);

    const form = e.currentTarget;
    const formData = new FormData(form);
    formData.set("_subject", "Founder Kit qualifying call inquiry");

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

      setStatus("success");
      form.reset();
    } catch {
      setErrorMessage("Network error. Please try again.");
      setStatus("error");
    }
  }

  if (status === "success") {
    return (
      <div
        role="status"
        aria-live="polite"
        className="border border-border bg-surface p-10"
      >
        <h2 className="font-heading text-2xl font-medium text-foreground">
          Submission received.
        </h2>
        <div className="mt-4 space-y-3 text-base text-foreground/75 leading-relaxed">
          {SUCCESS_LINES.map((line, i) => (
            <p key={i}>{line}</p>
          ))}
        </div>
      </div>
    );
  }

  const isSubmitting = status === "submitting";
  const errorId = "form-error";
  const inputClass =
    "w-full border border-border bg-background px-4 py-3 text-foreground outline-none transition-colors focus:border-accent focus:border-2 focus:py-[11px]";
  const labelClass = "block text-sm font-semibold text-foreground";

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-6 border border-border bg-surface p-8 md:p-10"
      aria-describedby={status === "error" ? errorId : undefined}
      noValidate
    >
      <div className="space-y-2">
        <label htmlFor="name" className={labelClass}>
          Name
        </label>
        <input
          required
          aria-required="true"
          aria-invalid={status === "error" ? "true" : undefined}
          type="text"
          id="name"
          name="name"
          autoComplete="name"
          className={inputClass}
        />
      </div>

      <div className="space-y-2">
        <label htmlFor="email" className={labelClass}>
          Email
        </label>
        <input
          required
          aria-required="true"
          aria-invalid={status === "error" ? "true" : undefined}
          type="email"
          id="email"
          name="email"
          autoComplete="email"
          className={inputClass}
        />
      </div>

      <div className="space-y-2">
        <label htmlFor="company" className={labelClass}>
          Company and what you do in one line
        </label>
        <input
          required
          aria-required="true"
          aria-invalid={status === "error" ? "true" : undefined}
          type="text"
          id="company"
          name="company"
          autoComplete="organization"
          className={inputClass}
        />
      </div>

      <div className="space-y-2">
        <label htmlFor="goal" className={labelClass}>
          What are you looking to build?
        </label>
        <textarea
          required
          aria-required="true"
          aria-invalid={status === "error" ? "true" : undefined}
          id="goal"
          name="goal"
          rows={4}
          className={`${inputClass} resize-none`}
        />
      </div>

      {status === "error" && errorMessage ? (
        <p
          id={errorId}
          role="alert"
          className="border border-foreground bg-background px-4 py-3 text-sm text-foreground"
        >
          {errorMessage}
        </p>
      ) : null}

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full bg-foreground px-6 py-4 font-semibold text-background transition-colors hover:bg-foreground/90 disabled:opacity-50"
      >
        {isSubmitting ? "Sending..." : "Submit"}
      </button>

      <p className="text-xs text-muted">
        Responses stored securely via Formspree.
      </p>
    </form>
  );
}
