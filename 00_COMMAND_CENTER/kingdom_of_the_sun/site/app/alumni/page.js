import { headliners, coaches, nbaPlayers } from "@/data/alumni";

export const metadata = {
  title: "Alumni",
  description: "The NBA players and championship-winning coaches who came through the Kingdom of the Sun, including Joel Embiid, Dwight Howard, and Kwame Brown.",
};

export default function Alumni() {
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">From the Kingdom to the League</div>
          <h1>Alumni</h1>
          <p className="lead">A Hall of Famer, an MVP, a number one overall pick, two championship-winning coaches, and more than 30 NBA players have played in Ocala.</p>
        </div>
      </header>

      <section className="section">
        <div className="wrap">
          <div className="eyebrow">Headliners</div>
          <h2>The Names</h2>
          <div className="heads">
            {headliners.map((h) => (
              <div className="head-card" key={h.name}><span className="hn">{h.name}</span><span className="ht">{h.note}</span></div>
            ))}
          </div>
          <div className="eyebrow" style={{ marginTop: 30 }}>Championship Coaches</div>
          <h2>The Sideline</h2>
          <div className="heads coaches">
            {coaches.map((h) => (
              <div className="head-card" key={h.name}><span className="hn">{h.name}</span><span className="ht">{h.note}</span></div>
            ))}
          </div>
        </div>
      </section>

      <section className="section">
        <div className="wrap">
          <div className="eyebrow">The Roll</div>
          <h2>Kingdom Alumni in the NBA</h2>
          <div className="alumni-grid">
            {nbaPlayers.map((p) => (
              <div className="alum" key={p.name}><span className="nm">{p.name}</span><span className="yr">{p.years}</span></div>
            ))}
          </div>
          <p className="muted" style={{ marginTop: 16, fontSize: 13, maxWidth: 640 }}>
            Hundreds more went on to play college basketball across five decades. Source: official tournament program.
          </p>
        </div>
      </section>
    </>
  );
}
