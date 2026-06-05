#!/usr/bin/env python3
"""
os_crm_schema.py , the CRM schema the OS tracks (Notion 5-DB + Airtable mirror).

Doctrine: notion_crm_schemas (Pipeline/Clients/Shoots/Outreach/Galleries), feedback_use_outbound_stack,
feedback_payment_follows_proof. Emits the schema for mcp.notion / mcp.airtable to build (no auto-write).

  os_crm_schema.py notion     , the 5-database Notion CRM schema
  os_crm_schema.py airtable   , the Airtable proof-loop / asset / signal mirror
  os_crm_schema.py dashboard  , the money-path dashboard metrics
"""
import sys
NOTION=["NOTION CRM (5 inline DBs in one page):",
 " Pipeline: Name, Status(Target/Engaged/Discovery/Proposal/Booked/Delivered/Lost/Re-engage), Tier, Trigger, VIB sent, Next action(+date), Source channel, Lane, Estimated value, Probability, Forecast(formula), Days since touch(formula), Client(rel), Notes",
 " Clients: Name, Company, Role, LinkedIn, Email, Referral source(rel), Referrals out(rollup), LTV(rollup), Tags, Pipelines/Shoots/Galleries(rel)",
 " Shoots: Shoot ID, Date, Type, Lane, Status, Studio, Card backed up, Delivery target/actual, SLA met(formula), Pixieset URL, Cash collected, Hero image, Client/Pipeline/Gallery(rel)",
 " Outreach: VIB ID, Recipient, Trigger used, Protocol named, VIB sent date, Reply, Reply latency(formula), Discovery date, Pipeline(rel)",
 " Galleries: Name, Pixieset URL, Delivered/Expiry, Upsell window status(formula), Upsell sequence sent, Upsell revenue, Conversion %(formula)"]
AIRTABLE=["AIRTABLE mirror (machine-queryable proof/asset/signal):",
 " Leads: name, lane, fit_score(os_client_fit_gate), status, source, next_action_date",
 " Assets: asset_id, world(AXIS/DEED/LOT00), type(still/motion/kit), gate_status, sellable(y/n), proof_link",
 " Proof: signal_id, play, signal_type, keep_kill_scale, date",
 " Money: offer, tier, price, value_score(os_offer_builder), stage, forecast"]
DASH=["MONEY-PATH DASHBOARD metrics:",
 " VIBs sent/wk (target 3+), discovery held/wk, cash collected/wk, active upsell windows,",
 " forecast by tier, stale pipeline(>14d), day-30 Op Kit triggers, fit-score distribution, ACTIVE sellable assets count"]
def main():
    k=sys.argv[1] if len(sys.argv)>1 else ""
    m={"notion":NOTION,"airtable":AIRTABLE,"dashboard":DASH}
    if k in m: [print(x) for x in m[k]]; return 0
    print("args: notion | airtable | dashboard"); return 1
if __name__=="__main__": sys.exit(main())
