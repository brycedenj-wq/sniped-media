import Link from "next/link";
import { site } from "@/data/site";

export default function Footer() {
  return (
    <footer>
      <div className="wrap">
        <div style={{ fontFamily: "var(--display)", letterSpacing: "1px", fontWeight: 700 }}>
          Kingdom of the Sun · Ocala, Florida
        </div>
        <div className="fnav">
          <Link href="/history">History</Link>
          <Link href="/champions">Champions</Link>
          <Link href="/alumni">Alumni</Link>
          <Link href="/records">Records</Link>
          <Link href="/teams">Teams</Link>
          <Link href="/schedule">Schedule</Link>
          <Link href="/watch">Watch</Link>
          <Link href="/sponsors">Sponsors</Link>
          <Link href="/confirm">Confirm Spot</Link>
        </div>
        <div className="muted">{site.contact.name} · {site.contact.email} · {site.contact.phone}</div>
        <div className="muted" style={{ marginTop: 6 }}>&copy; {site.year} Kingdom of the Sun. The Original. Since 1974.</div>
        <div className="preview">Preview build for committee review</div>
      </div>
    </footer>
  );
}
