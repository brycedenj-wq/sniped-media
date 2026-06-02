import { site } from "@/data/site";

export const metadata = {
  title: "Sponsors",
  description: "Partner with the original national high school holiday basketball tournament. Sponsorship tiers for the 53rd Annual Kingdom of the Sun.",
};

export default function Sponsors() {
  const c = site.contact;
  const mailto = `mailto:${c.email}?subject=${encodeURIComponent("Kingdom of the Sun " + site.edition + " - sponsorship")}`;
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">Partners</div>
          <h1>Sponsorship</h1>
          <p className="lead">Put your brand on fifty years of history, a national audience, and four days of basketball that has produced NBA players.</p>
        </div>
      </header>

      <section className="section">
        <div className="wrap">
          <div className="tiers">
            {site.sponsors.tiers.map((name) => (
              <div className="tier" key={name}><div className="name">{name}</div><div className="price">Inquire</div></div>
            ))}
          </div>
          <p className="muted" style={{ marginTop: 16, fontSize: 13 }}>{site.sponsors.note}</p>
          <div className="grid cols-3" style={{ marginTop: 22 }}>
            <div className="card"><h3>On-Site</h3><p>Court and gym signage, contest naming, PA recognition, and program placement over four days.</p></div>
            <div className="card"><h3>On the Stream</h3><p>Brand presence around live NFHS Network coverage, in front of a national audience.</p></div>
            <div className="card"><h3>Year-Round</h3><p>Standing placement on the tournament website, the home of fifty years of Kingdom history.</p></div>
          </div>
          <p style={{ marginTop: 24 }}><a className="btn" href={mailto}>Become a Partner</a></p>
        </div>
      </section>
    </>
  );
}
