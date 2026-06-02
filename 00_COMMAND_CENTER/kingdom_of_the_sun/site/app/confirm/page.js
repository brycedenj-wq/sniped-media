import { site } from "@/data/site";

export const metadata = {
  title: "Confirm Your Spot",
  description: "Invited programs, confirm your spot in the 53rd Annual Kingdom of the Sun.",
};

export default function Confirm() {
  const c = site.contact;
  const mailto = `mailto:${c.email}?subject=${encodeURIComponent("Kingdom of the Sun " + site.edition + " - team confirmation")}`;
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">Invited Teams</div>
          <h1>Confirm Your Spot</h1>
        </div>
      </header>

      <section className="section">
        <div className="wrap">
          <div className="confirm">
            <p className="muted" style={{ maxWidth: 560, margin: "0 auto 8px" }}>
              The {site.edition} is invitation only. Invited programs, confirm your spot and we will follow up with rosters, schedule, travel, and hotel details.
            </p>
            <p style={{ margin: "20px 0" }}><a className="btn" href={mailto}>Confirm by Email</a></p>
            <p className="muted" style={{ fontSize: 13 }}>
              {c.name} · {c.role}<br />
              <a className="gold" href={mailto}>{c.email}</a> · <a className="gold" href={`tel:${c.phone}`}>{c.phone}</a>
            </p>
          </div>
        </div>
      </section>
    </>
  );
}
