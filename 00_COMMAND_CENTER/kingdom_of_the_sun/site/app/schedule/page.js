import { site } from "@/data/site";

export const metadata = {
  title: "Schedule",
  description: "The four-day schedule for the 53rd Annual Kingdom of the Sun, December 28-31, 2026.",
};

export default function Schedule() {
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">Four Days</div>
          <h1>Schedule</h1>
          <p className="lead">{site.datesLabel}. Tip-off times are confirmed closer to the tournament.</p>
        </div>
      </header>

      <section className="section">
        <div className="wrap">
          <div className="sched">
            {site.schedule.map((d) => (
              <div className="card day" key={d.day}>
                <div className="tag">{d.day}</div>
                <h3>{d.label}</h3>
                <div className="note">{d.note}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section">
        <div className="wrap">
          <div className="eyebrow">16-Team Field</div>
          <h2>Bracket</h2>
          <div className="panel">
            <div className="big">Field & Bracket Drop October 2026</div>
            <p className="muted" style={{ marginTop: 8, fontSize: 13 }}>The 16-team field is announced in the fall and the bracket releases in October. The live bracket and scores appear here during the tournament, December 28-31.</p>
          </div>
        </div>
      </section>
    </>
  );
}
