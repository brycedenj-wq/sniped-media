import { records } from "@/data/records";

export const metadata = {
  title: "The Record Book",
  description: "The complete Kingdom of the Sun record book: every individual and team tournament high across five decades. The raw vault.",
};

export default function Records() {
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">The Vault · Since 1974</div>
          <h1>The Record Book</h1>
          <p className="lead">Every tournament high across five decades, pulled straight from the official program. The deep cuts, the raw record. Most people will not read all of this. It is here for the ones who will.</p>
        </div>
      </header>

      <section className="section">
        <div className="wrap">
          <div className="grid cols-2">
            <div className="rec-block">
              <h3>Most Points · Tournament</h3>
              <ul className="rec-list">
                {records.scoringTournament.map((r, i) => (
                  <li key={i}><span className="v">{r.v}</span><span>{r.who} · {r.team} · {r.year}</span></li>
                ))}
              </ul>
            </div>
            <div className="rec-block">
              <h3>Shooting · Tournament</h3>
              {records.shootingTournament.map((r, i) => (
                <div className="rec-kv" key={i}><span className="k">{r.label}: </span>{r.v}</div>
              ))}
              <h3 style={{ marginTop: 22 }}>Individual · Game</h3>
              {records.individualGame.map((r, i) => (
                <div className="rec-kv" key={i}><span className="k">{r.label}: </span>{r.v}</div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="wrap">
          <div className="eyebrow">Team Records</div>
          <h2>Team Highs</h2>
          <div className="grid cols-2">
            <div className="rec-block">
              {records.teamHighs.slice(0, 4).map((r, i) => (
                <div className="rec-kv" key={i}><span className="k">{r.label}: </span>{r.v}</div>
              ))}
            </div>
            <div className="rec-block">
              {records.teamHighs.slice(4).map((r, i) => (
                <div className="rec-kv" key={i}><span className="k">{r.label}: </span>{r.v}</div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="wrap">
          <div className="eyebrow">Most Frequent Visitors</div>
          <h2>Who Keeps Coming Back</h2>
          <div className="legacy-stats">
            {records.frequentVisitors.map((s) => (
              <div key={s.l}><div className="n">{s.n}</div><div className="l">{s.l}</div></div>
            ))}
          </div>
          <p className="muted" style={{ marginTop: 10, fontSize: 12 }}>Appearances across the tournament's history.</p>
        </div>
      </section>

      <section className="section">
        <div className="wrap">
          <div className="eyebrow">Fifty Years</div>
          <h2>By the Numbers</h2>
          <div className="legacy-stats">
            {records.participation.map((s) => (
              <div key={s.l}><div className="n">{s.n}</div><div className="l">{s.l}</div></div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
