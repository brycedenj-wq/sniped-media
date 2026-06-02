import Link from "next/link";
import { site } from "@/data/site";

export const metadata = {
  title: "Teams",
  description: "The 16-team invited field for the 53rd Annual Kingdom of the Sun.",
};

export default function Teams() {
  const teams = site.teams.slice();
  const tba = Math.max(0, site.teamSlots - teams.length);
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">The Field</div>
          <h1>Teams</h1>
          <p className="lead">A sixteen-team invited field. Programs are confirmed on a rolling basis as invitations are accepted.</p>
        </div>
      </header>

      <section className="section">
        <div className="wrap">
          <div className="teams">
            {teams.map((t) => (
              <div className={"team" + (t.host ? " host" : "")} key={t.name}>
                {t.host && <span className="badge">Host</span>}
                <span className="nm">{t.name}</span>
                <span className="ct">{t.city}</span>
              </div>
            ))}
            {Array.from({ length: tba }).map((_, i) => (
              <div className="team tba" key={"tba" + i}>TBA</div>
            ))}
          </div>
          <p className="muted" style={{ marginTop: 16, fontSize: 13 }}>
            Invitation only. Invited programs confirm their spot and the field fills toward sixteen.
          </p>
          <p style={{ marginTop: 16 }}><Link className="btn" href="/confirm">Confirm Your Spot</Link></p>
        </div>
      </section>
    </>
  );
}
