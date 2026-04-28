"use client";

import { useState } from "react";

// If you want a dedicated Formspree form for casting submissions,
// create a new form on Formspree and replace this endpoint with the new one.
// Same endpoint as /book is fine for now — submissions are tagged in subject.
const FORMSPREE_ENDPOINT = "https://formspree.io/f/xlgpgozq";

const SUCCESS_LINES = [
  "Submission received.",
  "If selected, a reply lands within 48 hours with shoot day, call time, and location.",
  "If not selected for this round, you stay on file for the next casting.",
];

type Status = "idle" | "submitting" | "error" | "success";

const availabilityOptions = ["Yes", "No", "Maybe"] as const;
const wardrobeOptions = ["Yes", "No", "Partial (have some pieces)"] as const;

type Field = {
  name: string;
  label: string;
  options: readonly string[];
};

const availabilityFields: Field[] = [
  { name: "available_may_1_am", label: "May 1, AM block", options: availabilityOptions },
  { name: "available_may_1_pm", label: "May 1, PM block", options: availabilityOptions },
  { name: "available_may_3_am", label: "May 3, AM block", options: availabilityOptions },
  { name: "available_may_3_pm", label: "May 3, PM block", options: availabilityOptions },
];

const wardrobeFields: Field[] = [
  { name: "wardrobe_orange", label: "Can bring orange wardrobe", options: wardrobeOptions },
  { name: "wardrobe_white", label: "Can bring all-white or cream wardrobe", options: wardrobeOptions },
];

export function CastingForm() {
  const [status, setStatus] = useState<Status>("idle");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("submitting");
    setErrorMessage(null);

    const form = e.currentTarget;
    const formData = new FormData(form);
    formData.set("_subject", "CASTING SUBMISSION — Sniped Media");

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
        className="border border-background/15 bg-surface-deep p-10 text-background"
      >
        <h2 className="font-heading text-2xl font-medium tracking-tight">
          Submission received.
        </h2>
        <div className="mt-4 space-y-3 text-base text-background/75 leading-relaxed">
          {SUCCESS_LINES.slice(1).map((line, i) => (
            <p key={i}>{line}</p>
          ))}
        </div>
      </div>
    );
  }

  const isSubmitting = status === "submitting";
  const errorId = "casting-form-error";
  const inputClass =
    "w-full border border-background/20 bg-surface-deep px-4 py-3 text-background placeholder:text-background/40 outline-none transition-colors focus:border-accent-bright focus:border-2 focus:py-[11px]";
  const labelClass =
    "block font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/70 tabular-nums";

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-10 border border-background/15 bg-foreground p-8 text-background md:p-10"
      aria-describedby={status === "error" ? errorId : undefined}
      noValidate
    >
      <fieldset className="space-y-6">
        <legend className="mb-2 font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-accent-bright tabular-nums">
          § 01 / Identity
        </legend>

        <div className="space-y-2">
          <label htmlFor="name" className={labelClass}>
            Name
          </label>
          <input
            required
            aria-required="true"
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
            type="email"
            id="email"
            name="email"
            autoComplete="email"
            className={inputClass}
          />
        </div>

        <div className="space-y-2">
          <label htmlFor="instagram" className={labelClass}>
            Instagram handle
          </label>
          <input
            required
            aria-required="true"
            type="text"
            id="instagram"
            name="instagram"
            placeholder="@yourhandle"
            className={inputClass}
          />
        </div>

        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
          <div className="space-y-2">
            <label htmlFor="height" className={labelClass}>
              Height
            </label>
            <input
              required
              aria-required="true"
              type="text"
              id="height"
              name="height"
              placeholder={`5'7" or 170 cm`}
              className={inputClass}
            />
          </div>

          <div className="space-y-2">
            <label htmlFor="location" className={labelClass}>
              Location in LA
            </label>
            <input
              required
              aria-required="true"
              type="text"
              id="location"
              name="location"
              placeholder="Neighborhood or closest area"
              className={inputClass}
            />
          </div>
        </div>
      </fieldset>

      <fieldset className="space-y-6">
        <legend className="mb-2 font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-accent-bright tabular-nums">
          § 02 / Availability
        </legend>
        <p className="text-sm text-background/70 leading-relaxed">
          Two shoot windows, May 1 and May 3. AM and PM blocks for each day. Mark each block.
        </p>

        <div className="space-y-5">
          {availabilityFields.map((field) => (
            <div key={field.name} className="grid grid-cols-1 gap-3 border-b border-background/10 pb-5 last:border-b-0 sm:grid-cols-[1fr_auto] sm:items-center sm:gap-6">
              <span className={labelClass}>{field.label}</span>
              <div className="flex flex-wrap gap-3">
                {field.options.map((opt) => (
                  <label
                    key={opt}
                    className="flex cursor-pointer items-center gap-2 border border-background/20 px-4 py-2 text-sm font-medium text-background/85 transition-colors has-[:checked]:border-accent-bright has-[:checked]:bg-accent-bright/10 has-[:checked]:text-background"
                  >
                    <input
                      required
                      aria-required="true"
                      type="radio"
                      name={field.name}
                      value={opt}
                      className="sr-only"
                    />
                    <span>{opt}</span>
                  </label>
                ))}
              </div>
            </div>
          ))}
        </div>
      </fieldset>

      <fieldset className="space-y-6">
        <legend className="mb-2 font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-accent-bright tabular-nums">
          § 03 / Wardrobe
        </legend>
        <p className="text-sm text-background/70 leading-relaxed">
          Bringing your own pieces is a plus, not a requirement. Mark honestly.
        </p>

        <div className="space-y-5">
          {wardrobeFields.map((field) => (
            <div key={field.name} className="grid grid-cols-1 gap-3 border-b border-background/10 pb-5 last:border-b-0 sm:grid-cols-[1fr_auto] sm:items-center sm:gap-6">
              <span className={labelClass}>{field.label}</span>
              <div className="flex flex-wrap gap-3">
                {field.options.map((opt) => (
                  <label
                    key={opt}
                    className="flex cursor-pointer items-center gap-2 border border-background/20 px-4 py-2 text-sm font-medium text-background/85 transition-colors has-[:checked]:border-accent-bright has-[:checked]:bg-accent-bright/10 has-[:checked]:text-background"
                  >
                    <input
                      required
                      aria-required="true"
                      type="radio"
                      name={field.name}
                      value={opt}
                      className="sr-only"
                    />
                    <span>{opt}</span>
                  </label>
                ))}
              </div>
            </div>
          ))}
        </div>
      </fieldset>

      {status === "error" && errorMessage ? (
        <p
          id={errorId}
          role="alert"
          className="border border-accent-bright bg-foreground px-4 py-3 text-sm text-accent-bright"
        >
          {errorMessage}
        </p>
      ) : null}

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full bg-background px-6 py-4 font-semibold text-foreground transition-colors hover:bg-accent-bright hover:text-foreground disabled:opacity-50"
      >
        {isSubmitting ? "Sending..." : "Submit Casting"}
      </button>

      <p className="text-xs text-background/50">
        Submissions handled via Formspree. No data shared outside the casting review.
      </p>
    </form>
  );
}
