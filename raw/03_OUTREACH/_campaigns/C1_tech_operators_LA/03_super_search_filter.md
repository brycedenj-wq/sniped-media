# Instantly Super Search · Filter Spec

Last updated: 2026-05-12
Campaign: C1 · Tech Operators LA

Paste-ready filter values for Instantly Super Search.

---

## Geography (city-level, not county)

City filter:
- Los Angeles
- Santa Monica
- Culver City
- Pasadena
- Glendale
- Long Beach
- El Segundo
- Marina del Rey
- West Hollywood
- Beverly Hills
- Hollywood
- Manhattan Beach
- Hermosa Beach
- Venice
- Burbank
- Studio City

State: California
Country: United States

**Do NOT use county-level (LA County)** per Instantly best practice · returns too much noise. City-level pulls cleaner data.

---

## Job titles · INCLUDE

### VP tier
- VP Engineering
- VP of Engineering
- VP Eng
- VP Product
- VP of Product
- VP Product Management
- VP Operations
- VP of Operations
- VP Ops
- VP Marketing
- VP of Marketing
- VP Sales
- VP of Sales
- VP Design
- VP of Design
- VP Customer Success
- VP People

### Head-of tier
- Head of Engineering
- Head of Product
- Head of Operations
- Head of Marketing
- Head of Sales
- Head of Design
- Head of Growth
- Head of Customer Success

### Director tier
- Director of Engineering
- Director of Product
- Director of Operations
- Director of Marketing
- Director of Sales
- Director of Design
- Director of Growth

### C-Suite (non-founder · use exclusion logic below to filter founders)
- CTO
- CPO
- COO
- CMO
- CRO
- CSO
- CFO

---

## Job titles · EXCLUDE (critical)

- Founder
- Co-Founder
- Cofounder
- Co Founder
- Founding
- CEO (CEOs often founded the company · exclude unless verified non-founder)
- Owner
- President (often founder-equivalent in tech)
- Photographer
- Studio
- Creative Director (lane conflict · they buy photography pro)
- Recruiter
- Talent
- People Operations (HR lane, different ICP)
- Assistant
- Intern
- Coordinator
- Manager (too junior · we want Director and above)
- Specialist
- Analyst

---

## Industry · INCLUDE

- Computer Software
- Internet
- Information Technology and Services
- Computer & Network Security
- Computer Hardware
- Information Services
- Financial Services (filter for FinTech keywords)
- Computer Games (if expanding)
- Wireless / Telecommunications

---

## Industry · EXCLUDE

- Photography
- Marketing & Advertising (agencies)
- Public Relations & Communications
- Events Services
- Entertainment (separate ICP)
- Real Estate
- Hospitality

---

## Company size · INCLUDE

- 21-50 employees
- 51-200 employees
- 201-500 employees

Optional secondary tier (test later):
- 501-1000 employees (more established, harder to convert at $1,500 Reset · save for later cohort)

Exclude:
- 1-20 employees (too early, often founder-led only · those go to LinkedIn VIB track)
- 1000+ employees (procurement-heavy, slower close)

---

## Keywords · INCLUDE (in title or company description)

Bonus keywords that boost relevance:
- SaaS
- Platform
- Software
- B2B
- Startup
- Tech
- AI / Machine Learning (current cycle bonus)

---

## Keywords · EXCLUDE

- Agency
- Consulting (unless paired with "VP" or "Director" at a non-consulting company)
- Freelance
- Self-employed

---

## Tier tagging on pull (Ren executes)

After Super Search pulls leads, Ren tags into 3 tiers before upload:

| Tier | Criteria | Action |
|---|---|---|
| **Tier 1** | Recent trigger event (funding announcement past 30 days, hiring post past 14 days, public press past 30 days) | Manual personalization line added to email 1 (replace generic open with trigger-specific) |
| **Tier 2** | Strong fit, no specific trigger | Standard email 1 (no manual personalization) |
| **Tier 3** | Edge cases · 1000+ employees, adjacent industry, ambiguous title | Hold queue · email only if Tier 1+2 pipeline runs dry |

Lead tagging time budget: ~10 min per 100 leads. Weekly pull of 1,500 = ~2.5 hrs of tagging.

---

## Pull cadence

- Weekly pull: Monday 9-10 AM
- Target: 1,200-1,500 leads/week
- Filter snapshot saved in Instantly · re-run weekly with date-restricted updates (newly-added LinkedIn profiles in the past 7 days only, to reduce duplicate burns)

---

## Duplicate / re-email protection

Instantly auto-checks against already-emailed lists. Cross-check against:
- `/03_OUTREACH/_sent_dms/` (LinkedIn DM recipients · these are FOUNDERS so shouldn't overlap, but verify)
- Any prior campaign sent-list (Campaign C2+ will need this list when launched)
- Suppression list (anyone who replied "stop" or "unsubscribe" · auto-handled by Instantly)

---

## What Super Search will NOT do for us

- Pull "intent" data (who's actively searching for a photographer · this is paid intent data tool territory, not Super Search)
- Pull personal email · only work emails. Sequences must work with work-email deliverability.
- Pull warm intros · Super Search is cold by definition. Warm intros come from the VIB referral path separately.

---

## Spec validation before first pull

Before Ren executes the first pull, verify in Super Search:
- [ ] City filter set (not county)
- [ ] At least 5,000 results returned (if fewer, broaden geo or industry by one step)
- [ ] No more than 25,000 results returned (if more, narrow titles or company size)
- [ ] Spot-check 10 random results · do they look like real VPs at real LA tech companies?
- [ ] LinkedIn URLs included (needed for the Higgsfield Loom step)
