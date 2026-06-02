import Link from "next/link";
import { site } from "@/data/site";
import { champions } from "@/data/champions";
import { headliners, coaches } from "@/data/alumni";

export default function Home() {
  const recent = champions.filter((c) => !c.cancelled).slice(0, 6);
  return (
    <>
      {/* HERO */}
      <section className="hero">
        <div className="wrap">
          <img className="emblem" src="/crown.svg" alt="Kingdom of the Sun crown emblem" />
          <h1>{site.tagline}</h1>
          <div className="sub">{site.edition} · {site.datesLabel} · Ocala, Florida</div>
          <div className="cta">
            <Link className="btn" href="/confirm">Confirm Your Spot</Link>
            <Link className="btn ghost" href="/history">The History</Link>
          </div>
        </div>
      </section>

      {/* STAT BAND */}
      <div className="statband">
        {site.stats.map((s) => (
          <div key={s.l}><div className="n">{s.n}</div><div className="l">{s.l}</div></div>
        ))}
      </div>

      {/* THE ORIGINAL */}
      <section className="section">
        <div className="wrap">
          <div className="eyebrow">Est. 1974 · The Original</div>
          <h2>Fifty Years of the Kingdom</h2>
          <p className="lead">{site.history.positioning}</p>
          <p className="muted" style={{ marginTop: 14, maxWidth: 680, fontSize: 14 }}>{site.history.reach}</p>
          <div className="legacy-stats">
            {site.history.legacyStats.map((s) => (
              <div key={s.l}><div className="n">{s.n}</div><div className="l">{s.l}</div></div>
            ))}
          </div>
        </div>
      </section>

      {/* MARQUEE ALUMNI */}
      <section className="section">
        <div className="wrap">
          <div className="eyebrow">From the Kingdom to the League</div>
          <h2>The Level</h2>
          <p className="muted" style={{ maxWidth: 620 }}>More than 30 NBA players and two championship-winning coaches came through this tournament.</p>
          <div className="heads">
            {headliners.map((h) => (
              <div className="head-card" key={h.name}><span className="hn">{h.name}</span><span className="ht">{h.note}</span></div>
            ))}
          </div>
          <div className="heads coaches" style={{ marginTop: 10 }}>
            {coaches.map((h) => (
              <div className="head-card" key={h.name}><span className="hn">{h.name}</span><span className="ht">{h.note}</span></div>
            ))}
          </div>
          <p style={{ marginTop: 18 }}><Link className="btn ghost" href="/alumni">See All Alumni</Link></p>
        </div>
      </section>

      {/* CHAMPIONS TEASER */}
      <section className="section">
        <div className="wrap">
          <div className="eyebrow">Since 1974</div>
          <h2>Champions</h2>
          <div className="tablewrap">
            <table className="tbl">
              <thead><tr><th>Year</th><th>Champion</th><th>MVP</th></tr></thead>
              <tbody>
                {recent.map((c) => (
                  <tr key={c.y}>
                    <td className="yr">{c.y}</td>
                    <td className="ch">{c.champ}{c.honor === "National" ? <span className="hb nat">National</span> : c.honor === "State" ? <span className="hb">State</span> : null}</td>
                    <td className="dim">{c.mvp}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p style={{ marginTop: 18 }}><Link className="btn ghost" href="/champions">Every Champion, 1974-2025</Link></p>
        </div>
      </section>

      {/* 2026 STRIP */}
      <section className="section">
        <div className="wrap">
          <div className="eyebrow">The 53rd Annual</div>
          <h2>December 28-31, 2026</h2>
          <div className="grid cols-3">
            <div className="card"><h3>Invitation Only</h3><p>Sixteen of the strongest programs, invited to Ocala for four days at Vanguard High School.</p></div>
            <div className="card"><h3>Streaming on NFHS</h3><p>Every game streams live on NFHS Network, the whole tournament, start to finish.</p></div>
            <div className="card"><h3>The Experience</h3><p>Team meals, the dunk and 3-point contests, college exposure, and Ocala hospitality.</p></div>
          </div>
          <p style={{ marginTop: 18 }}><Link className="btn ghost" href="/tournament">About the Tournament</Link></p>
        </div>
      </section>

      {/* CTA */}
      <section className="section">
        <div className="wrap">
          <div className="confirm">
            <div className="eyebrow">Invited Teams</div>
            <h2 style={{ fontSize: 26 }}>Confirm Your Spot</h2>
            <p className="muted" style={{ maxWidth: 540, margin: "0 auto 22px" }}>
              The 53rd Annual is invitation only. Invited programs, confirm your spot and we will follow up with rosters, schedule, travel, and hotel details.
            </p>
            <Link className="btn" href="/confirm">Confirm Spot</Link>
          </div>
        </div>
      </section>
    </>
  );
}
