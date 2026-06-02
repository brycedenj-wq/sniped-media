import Link from "next/link";
import { site } from "@/data/site";

export const metadata = {
  title: "The Tournament",
  description: "The 53rd Annual Kingdom of the Sun: December 28-31, 2026, invitation only, sixteen teams, streaming live on NFHS Network.",
};

export default function Tournament() {
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">The 53rd Annual</div>
          <h1>The Tournament</h1>
          <p className="lead">{site.datesLabel}. {site.location}. Sixteen invited programs, four days, one champion.</p>
        </div>
      </header>

      <div className="statband">
        {site.stats.map((s) => (
          <div key={s.l}><div className="n">{s.n}</div><div className="l">{s.l}</div></div>
        ))}
      </div>

      <section className="section">
        <div className="wrap">
          <div className="grid cols-3">
            <div className="card"><h3>Invitation Only</h3><p>The field is invited, not open. Sixteen of the strongest programs from Florida and beyond.</p></div>
            <div className="card"><h3>Four Days</h3><p>Opening round through the championship, December 28 to 31 at Vanguard High School.</p></div>
            <div className="card"><h3>Streaming on NFHS</h3><p>Every game streams live on NFHS Network, watchable from anywhere in the country.</p></div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="wrap">
          <div className="eyebrow">More Than A Tournament</div>
          <h2>The Experience</h2>
          <div className="grid cols-3">
            {site.experience.map((e) => (
              <div className="card" key={e.t}><h3>{e.t}</h3><p>{e.d}</p></div>
            ))}
          </div>
          <div className="cta" style={{ marginTop: 24, justifyContent: "flex-start" }}>
            <Link className="btn ghost" href="/teams">The Field</Link>
            <Link className="btn ghost" href="/schedule">Schedule</Link>
            <Link className="btn ghost" href="/watch">Watch Live</Link>
          </div>
        </div>
      </section>
    </>
  );
}
