import Link from "next/link";
import { site } from "@/data/site";
import { records } from "@/data/records";

export const metadata = {
  title: "History",
  description: "How the Kingdom of the Sun began in 1974, and why it is the original national high school holiday basketball tournament.",
};

export default function History() {
  const h = site.history;
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">Est. 1974 · The Original</div>
          <h1>History</h1>
          <p className="lead">{h.positioning}</p>
        </div>
      </header>

      <section className="section">
        <div className="wrap two-col">
          <div>
            <figure style={{ margin: 0 }}>
              <img className="legacy-logo" src="/official_logo.png" alt="The original Kingdom of the Sun logo, in use since 1974" />
              <figcaption className="muted" style={{ fontSize: 12, marginTop: 8, letterSpacing: ".5px" }}>
                The original mark. Preserved as heritage.
              </figcaption>
            </figure>
            <div className="haley">
              <img src="/jim_hero.png" alt="Coach Jim Haley, founder of the Kingdom of the Sun" />
              <div className="cap">
                <strong>Jim Haley</strong><br />
                <span className="muted">Founder · 1974</span>
                <div className="sig">Jim Haley Court signature: clean recreation in progress</div>
              </div>
            </div>
          </div>
          <div className="prose">
            <div className="eyebrow">How It All Began</div>
            <h2 style={{ fontSize: 24, margin: "8px 0 16px" }}>The 24-Hour Bet</h2>
            <p>{h.story}</p>
            <p>{h.storyCont}</p>
            <div className="positioning">{h.positioning}</div>
            <p className="muted" style={{ fontSize: 14 }}>{h.reach}</p>
          </div>
        </div>
        <div className="wrap">
          <div className="legacy-stats" style={{ marginTop: 8 }}>
            {h.legacyStats.map((s) => (
              <div key={s.l}><div className="n">{s.n}</div><div className="l">{s.l}</div></div>
            ))}
          </div>
        </div>
      </section>

      <section className="section">
        <div className="wrap">
          <div className="eyebrow">The Blueprint</div>
          <h2>Everyone Followed the Kingdom</h2>
          <div className="grid cols-3">
            <div className="card"><h3>King of the Bluegrass</h3><p>The Kentucky tournament built on the Kingdom model.</p></div>
            <div className="card"><h3>The Arby&apos;s Classic</h3><p>The Tennessee event, another spinoff of the Kingdom blueprint.</p></div>
            <div className="card"><h3>City of Palms Classic</h3><p>Regarded as the top high school tournament in the country. It was an eight-team event until it changed format after seeing the Kingdom take off.</p></div>
          </div>
          <p className="muted" style={{ marginTop: 16, fontSize: 14, maxWidth: 640 }}>
            Ocala&apos;s tournament is the original sixteen-team event with national flair. The others came after it.
          </p>
        </div>
      </section>

      <section className="section">
        <div className="wrap">
          <div className="eyebrow">From the Record Book</div>
          <h2>Fifty Years of Highs</h2>
          <ul className="rec-list" style={{ maxWidth: 680 }}>
            {records.highlights.map((r, i) => (
              <li key={i}><span className="v">{r.v}</span><span>{r.note} · {r.who}{r.team && r.team !== "team" ? ` · ${r.team}` : ""} · {r.year}</span></li>
            ))}
          </ul>
          <p style={{ marginTop: 18 }}>
            <Link className="btn ghost" href="/records">Open the Full Record Book</Link>
          </p>
          <p className="muted" style={{ marginTop: 12, fontSize: 12, maxWidth: 600 }}>
            The full vault has every individual and team record across five decades. Most people will not read all of it. It is there for the ones who will.
          </p>
        </div>
      </section>
    </>
  );
}
