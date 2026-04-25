"use client";

import { useEffect, useRef, useState } from "react";

export function ComingSoon() {
  const [pos, setPos] = useState<{ x: number; y: number } | null>(null);
  const [frameCount, setFrameCount] = useState(2147);
  const [flashing, setFlashing] = useState(false);
  const [supportsHover, setSupportsHover] = useState(false);
  const [now, setNow] = useState<string>("");
  const flashTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    const mql = window.matchMedia("(hover: hover) and (pointer: fine)");
    setSupportsHover(mql.matches);
    const onChange = () => setSupportsHover(mql.matches);
    mql.addEventListener("change", onChange);
    return () => mql.removeEventListener("change", onChange);
  }, []);

  useEffect(() => {
    const tick = () => {
      const d = new Date();
      const pad = (n: number) => String(n).padStart(2, "0");
      setNow(
        `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(
          d.getHours()
        )}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`
      );
    };
    tick();
    const id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, []);

  useEffect(() => {
    if (!supportsHover) return;
    const onMove = (e: MouseEvent) => setPos({ x: e.clientX, y: e.clientY });
    window.addEventListener("mousemove", onMove);
    return () => window.removeEventListener("mousemove", onMove);
  }, [supportsHover]);

  function handleCapture() {
    setFrameCount((c) => c + 1);
    setFlashing(true);
    if (flashTimer.current) clearTimeout(flashTimer.current);
    flashTimer.current = setTimeout(() => setFlashing(false), 90);
  }

  return (
    <div
      onClick={handleCapture}
      className="relative isolate flex min-h-screen w-full cursor-none flex-col bg-foreground text-background select-none overflow-hidden"
      style={{ cursor: supportsHover ? "none" : "auto" }}
    >
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0 opacity-[0.05]"
        style={{
          backgroundImage:
            "linear-gradient(to right, #F5F3EE 1px, transparent 1px)",
          backgroundSize: "calc(100% / 12) 100%",
        }}
      />

      <div className="relative z-10 flex items-start justify-between px-6 py-6 sm:px-10 sm:py-8">
        <div className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 tabular-nums">
          Sniped Media
        </div>
        <div className="hidden items-center gap-4 font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 tabular-nums sm:flex">
          <span>Los Angeles</span>
          <span className="h-px w-10 bg-background/30" />
          <span suppressHydrationWarning>{now}</span>
        </div>
      </div>

      <div className="relative z-10 flex flex-1 items-center justify-center px-6 text-center">
        <div className="max-w-3xl">
          <span className="font-heading text-[11px] font-semibold tracking-[0.4em] uppercase text-accent-bright tabular-nums">
            § 00 / In Development
          </span>
          <h1 className="mt-8 font-heading text-5xl font-bold leading-[0.95] tracking-tight text-balance sm:text-7xl lg:text-[140px]">
            Developing.
          </h1>
          <p className="mx-auto mt-8 max-w-xl text-base leading-relaxed text-background/75 sm:text-lg">
            The next version of Sniped Media is on the bench. Same studio. Same standard. New positioning underway.
          </p>
          <p className="mt-10 font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 tabular-nums">
            <a
              href="mailto:hello@snipedmedia.com"
              className="underline decoration-background/30 underline-offset-4 transition-colors hover:text-accent-bright hover:decoration-accent-bright"
            >
              hello@snipedmedia.com
            </a>
          </p>
        </div>
      </div>

      <div className="relative z-10 flex items-end justify-between gap-6 px-6 py-6 sm:px-10 sm:py-8">
        <div className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 tabular-nums">
          <span className="hidden sm:inline">Tap anywhere · </span>Frames logged{" "}
          <span className="text-accent-bright">{frameCount.toLocaleString()}</span>
        </div>
        <div className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 tabular-nums">
          V2.0 / On File
        </div>
      </div>

      {supportsHover && pos ? (
        <div
          aria-hidden="true"
          className="pointer-events-none fixed z-30"
          style={{
            left: pos.x,
            top: pos.y,
            transform: "translate(-50%, -50%)",
          }}
        >
          <svg width="56" height="56" viewBox="0 0 56 56" className="text-accent-bright">
            <line x1="28" y1="0" x2="28" y2="14" stroke="currentColor" strokeWidth="1" />
            <line x1="28" y1="42" x2="28" y2="56" stroke="currentColor" strokeWidth="1" />
            <line x1="0" y1="28" x2="14" y2="28" stroke="currentColor" strokeWidth="1" />
            <line x1="42" y1="28" x2="56" y2="28" stroke="currentColor" strokeWidth="1" />
            <circle cx="28" cy="28" r="14" fill="none" stroke="currentColor" strokeWidth="1" />
            <circle cx="28" cy="28" r="1" fill="currentColor" />
          </svg>
        </div>
      ) : null}

      {flashing ? (
        <div
          aria-hidden="true"
          className="pointer-events-none fixed inset-0 z-40 bg-background/40 motion-reduce:hidden"
        />
      ) : null}
    </div>
  );
}
