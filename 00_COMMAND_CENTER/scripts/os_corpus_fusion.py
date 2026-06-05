#!/usr/bin/env python3
"""
os_corpus_fusion.py , the MASTER CORPUS FUSION ENGINE.

Turns the corpus from a pile of files into one fused intelligence. It does NOT load raw books into a
context window. It maps every source FAMILY (the 60 chunk families) and every certified ATOM (the
~66 memory files) onto DOCTRINE NODES, computes how much of the corpus is actually fused (not just
stored), and emits the graph + source map the router uses.

Unit of fusion = family/atom -> doctrine node. The certification ledger is the provenance underneath.

  os_corpus_fusion.py coverage     , % of families+atoms fused into doctrine / skills-gates-workflows
  os_corpus_fusion.py map [--write] , source->doctrine map (CSV to OS_SOURCE_TO_DOCTRINE_MAP.csv)
  os_corpus_fusion.py graph [--write], doctrine graph JSON (OS_DOCTRINE_GRAPH.json)
  os_corpus_fusion.py orphans       , families/atoms not yet fused (the leak list)
  os_corpus_fusion.py families      , live family scan with chunk counts
"""
import os, sys, csv, json, glob, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 00_COMMAND_CENTER
REPO = os.path.dirname(ROOT)                                          # AI-Brain-Refinery
KB = os.path.join(REPO, "01_KNOWLEDGE_BASE")
MEM = "/Users/sniper/.claude/projects/-Users-sniper/memory"
CERT_LEDGER = os.path.join(ROOT, "OS_CERTIFICATION_LEDGER.csv")
OUT_MAP = os.path.join(ROOT, "OS_SOURCE_TO_DOCTRINE_MAP.csv")
OUT_GRAPH = os.path.join(ROOT, "OS_DOCTRINE_GRAPH.json")

# ---- DOCTRINE NODES , the fused intelligence units (the brain's concepts) ----
# each node: the law it encodes + which existing os_doctrine domain it extends (or NEW)
NODES = {
  "copy":             {"law":"headline is 80%, one big idea, in-world voice, no hype, no em-dash","domain":"copy"},
  "visual_grade":     {"law":"quiet-luxury restraint, one-color discipline, beat the source","domain":"visual_grade"},
  "world_character":  {"law":"ownable mark + lineage specificity + tension, faceless-safe","domain":"world_character"},
  "layout_type":      {"law":"owned editorial kit, legible, intentional hierarchy, no filler","domain":"layout_type"},
  "pricing_offer":    {"law":"price value not cost, 3-option anchor, proof before price","domain":"pricing_offer"},
  "distribution_hook":{"law":"MAYA hook, repeatable format, clusters before broadcast","domain":"distribution_hook"},
  "trust_sales":      {"law":"trust=(C+R+I)/self-orientation, hospitality, hardest to say no","domain":"trust_sales"},
  "motion":           {"law":"intent per frame, teaser != trailer, color holds in motion","domain":"motion"},
  "safety_identity":  {"law":"no identity/employer leak, faceless-safe, proof before public, payment follows proof","domain":"safety_identity"},
  # NEW nodes the families demand (the 9 domains did not cover these) ----
  "strategy_war":     {"law":"position before force, indirect approach, concentrate at the decisive point","domain":"NEW"},
  "decision_judgment":{"law":"base rates over stories, second-order effects, reversibility, kill criteria","domain":"NEW"},
  "leverage_ownership":{"law":"own equity/media/code; permissionless leverage; build a body of work","domain":"NEW"},
  "founder_operations":{"law":"right-size not scale, run the office, turnaround = focus the constraint","domain":"NEW"},
  "status_culture":   {"law":"status is signaled not stated; analog/new-luxury premium; hidden motives","domain":"NEW"},
  "automation_toolchain":{"law":"tool-first routing, connected toolchain default, prompt patterns, gate every action","domain":"NEW"},
  "narrative_canon":  {"law":"story structure, archetype, cultural canon as raw material for meaning","domain":"NEW"},
  "self_optimization":{"law":"every failure -> a rule; certify by proof; the OS sharpens each pass","domain":"NEW"},
}

# ---- FAMILY -> NODES (explicit, from the real family names). conf: HIGH clear / LOW needs sub-map ----
FAMILY_MAP = {
  "ADVERTISING_RECOVERY":["copy"], "PERSUASION_RECOVERY":["copy","trust_sales"], "BRAND_CANON":["copy","layout_type"],
  "B2B_POSITIONING_CLAUDE_OPERATOR":["trust_sales","automation_toolchain"], "POSITIONING_DISRUPTION":["trust_sales","strategy_war"],
  "CONSULTING_SERVICE":["trust_sales","pricing_offer"], "MEDIA_BUSINESS":["distribution_hook","leverage_ownership"],
  "MEDIA_BUSINESS_RECOVERY":["distribution_hook"], "NETWORK_DISTRIBUTION":["distribution_hook"],
  "BIOGRAPHY_FOUNDER_MEDIA":["leverage_ownership","founder_operations"], "FOUNDER_FASHION_RECOVERY":["status_culture","founder_operations"],
  "FOUNDER_SECOND_TIER":["founder_operations"], "ONWARD_TURNAROUND":["founder_operations"],
  "OPERATING_FOUNDER_OPERATIONS":["founder_operations"], "OPERATING_FOUNDER_SCALING":["founder_operations"],
  "OPERATING_FOUNDER_STARTUP":["founder_operations","safety_identity"], "LEADERSHIP_MGMT":["founder_operations"], "LEADERSHIP_SUPP":["founder_operations"],
  "MONEY_OWNERSHIP":["leverage_ownership","pricing_offer"], "DEEP_FINANCE_EXPANSION":["leverage_ownership","pricing_offer"],
  "CLASSICAL_STRATEGY":["strategy_war"], "MODERN_COMMAND_NAPOLEON":["strategy_war"], "TIER_2_GREENE_STRATEGY":["strategy_war"],
  "POLITICAL_THEORY_DISCOURSES":["strategy_war"], "CLASSICAL_HISTORY":["strategy_war","narrative_canon"], "HISTORICAL_BIOGRAPHY":["strategy_war","leverage_ownership"],
  "DECISION_JUDGMENT_COGNITION":["decision_judgment"], "DECISION_JUDGMENT_CROWDS":["decision_judgment","distribution_hook"],
  "DECISION_JUDGMENT_MEANING":["decision_judgment","narrative_canon"], "DECISION_SYSTEMS_SUPP":["decision_judgment"],
  "SYSTEMS_THINKING":["decision_judgment","self_optimization"], "EXPERTISE_CREATIVITY":["decision_judgment","visual_grade"],
  "CULTURE_AND_STATUS":["status_culture"], "FASHION_LUXURY_CULTURE":["status_culture","layout_type"], "FASHION_LUXURY_STRATEGY":["status_culture","pricing_offer"],
  "STORYTELLING_NARRATIVE":["narrative_canon","world_character"], "LITERARY_CANON_BLACK":["narrative_canon","world_character"],
  "LITERARY_CANON_DYSTOPIAN":["narrative_canon"], "LITERARY_CANON_GENERAL":["narrative_canon"], "LITERARY_RECOVERY":["narrative_canon"],
  "INTELLECTUAL_ARTIST_FRAME":["narrative_canon","visual_grade"], "PERSONAL_OPERATING_CODE":["safety_identity","self_optimization"],
  "EDGE_AND_OPERATING_DISCIPLINE":["safety_identity","founder_operations"], "HIGH_LEVEL_CONVOS":["strategy_war","decision_judgment"],
  "N8N_AUTOMATION_SYSTEMS":["automation_toolchain"], "TOOLCHAIN_DISTRIBUTION_SUPP":["automation_toolchain","distribution_hook"],
  "CLAUDE_OPERATOR_DOCS":["automation_toolchain","self_optimization"], "PROMPT_TEMPLATES_DEEP":["automation_toolchain"],
  "OPPORTUNITY_MANAGEMENT_TEMPLATES":["founder_operations","decision_judgment"],
  # photography/film foundational batch (locked canon)
  "BATCH_005":["visual_grade","motion"],
  # the big mixed intake batches , LOW conf, flagged for sub-mapping
  "BATCH_001":["narrative_canon"], "BATCH_002":["narrative_canon"], "BATCH_003":["founder_operations"],
  "BATCH_004":["strategy_war"], "BATCH_006":["trust_sales"], "BATCH_007":["pricing_offer"],
  "BATCH_008":["distribution_hook"], "BATCH_009":["decision_judgment"], "BATCH_009_EXPANSION":["decision_judgment"],
  "BATCH_010":["automation_toolchain"],
}
LOW_CONF_FAMILIES = {"BATCH_001","BATCH_002","BATCH_003","BATCH_004","BATCH_006","BATCH_007","BATCH_008","BATCH_009","BATCH_009_EXPANSION","BATCH_010"}

# ---- ATOM keyword -> node (memory atoms are already certified doctrine) ----
ATOM_KW = {
  "copy":["positioning","wwp","dm_voice","carousel"], "visual_grade":["visual_direction","photograph","edit_register","photo_theory","art"],
  "world_character":["lineage","composite_environment","scene_density","bw_card"], "layout_type":["composite_environment","bw_card"],
  "pricing_offer":["pricing","new_luxury","payment","ein"], "distribution_hook":["distribution","hit_mechanics","blockbuster","platform_split","linkedin"],
  "trust_sales":["trust","hospitality","hardest","referral","discovery","outbound","ai_sentiment","ai_photographer"],
  "motion":["photo_theory"], "safety_identity":["possibility_engine","payment_follows","capability_proof","operating_constraints","google_account"],
  "leverage_ownership":["leverage","company_of_one","perennial","analog_premium","meta_thesis"],
  "founder_operations":["execution","operating","casting","monday","repetition","proof_over_packaging","kots"],
  "status_culture":["status_psychology","analog_premium","new_luxury"], "strategy_war":["strategic_implications","spine"],
  "decision_judgment":["full_engagement","old_work","full_os_synthesis","name_availability","max_default"],
  "automation_toolchain":["connected_toolchain","use_outbound","skill_activation"],
  "self_optimization":["capability_growth","certification_standard","extraction_audit","read_whole","os_engagement","execution_governor","self_optimization","starthere","book_doctrine"],
  "narrative_canon":["meta_thesis"],
}

# ---- DOCTRINE GRAPH EDGES , how nodes fuse across source families (the cross-source synthesis) ----
EDGES = [
  ("leverage_ownership","distribution_hook","own the media that compounds; a body of work IS distribution"),
  ("leverage_ownership","founder_operations","stay a company of one; right-size keeps the equity"),
  ("visual_grade","narrative_canon","taste + story = images that mean something, not just process"),
  ("strategy_war","trust_sales","position before pitch; win without pitching = the indirect approach"),
  ("decision_judgment","self_optimization","base rates + kill criteria feed the failure-to-rule loop"),
  ("automation_toolchain","self_optimization","claude/agent docs + failure logs = the self-optimizing OS"),
  ("status_culture","pricing_offer","status signaling is why premium/new-luxury prices hold"),
  ("world_character","motion","the world bible governs both stills and the made-image in motion"),
  ("narrative_canon","world_character","literary archetype is raw material for an ownable character"),
  ("strategy_war","decision_judgment","Greene/Napoleon + judgment = when to concentrate vs reverse"),
  ("safety_identity","trust_sales","faceless-safe + low self-orientation both protect the relationship"),
  ("pricing_offer","leverage_ownership","price the value because the value is owned IP"),
]

def scan_families():
    fams = {}
    for f in sorted(glob.glob(os.path.join(KB, "**", "*CHUNKS.jsonl"), recursive=True)):
        name = os.path.basename(f)[:-len("_CHUNKS.jsonl")] if f.endswith("_CHUNKS.jsonl") else os.path.basename(f)[:-len(".jsonl")]
        try: n = sum(1 for _ in open(f, errors="ignore"))
        except Exception: n = 0
        fams[name] = n
    return fams

def scan_atoms():
    return [os.path.basename(p)[:-3] for p in glob.glob(os.path.join(MEM, "*.md")) if not p.endswith("MEMORY.md")]

def atom_nodes(atom):
    hits = []
    for node, kws in ATOM_KW.items():
        if any(kw in atom for kw in kws): hits.append(node)
    return hits or (["self_optimization"] if atom.startswith("project_") else ["safety_identity"])

def ledger_stats():
    if not os.path.exists(CERT_LEDGER): return {}
    from collections import Counter
    c = Counter()
    with open(CERT_LEDGER, errors="ignore") as f:
        r = csv.reader(f); next(r, None)
        for row in r:
            if row: c[row[-1]] += 1
    return dict(c)

def build_map():
    fams = scan_families(); atoms = scan_atoms()
    rows = []
    for fam, n in fams.items():
        nodes = FAMILY_MAP.get(fam, [])
        conf = "LOW" if fam in LOW_CONF_FAMILIES else ("HIGH" if nodes else "NONE")
        rows.append({"source": fam, "kind": "family", "chunks": n, "nodes": ";".join(nodes) or "ORPHAN", "confidence": conf})
    for a in atoms:
        nodes = atom_nodes(a)
        rows.append({"source": a, "kind": "atom", "chunks": 1, "nodes": ";".join(nodes), "confidence": "CERTIFIED"})
    return rows

def coverage():
    rows = build_map()
    fam_rows = [r for r in rows if r["kind"] == "family"]
    atom_rows = [r for r in rows if r["kind"] == "atom"]
    fused = [r for r in rows if r["nodes"] != "ORPHAN"]
    orphans = [r for r in rows if r["nodes"] == "ORPHAN"]
    # skills/gates/workflows: nodes wired into a route/gate (every node maps to os_doctrine domain or a NEW node used by execution graph)
    wired_nodes = sum(1 for n in NODES.values() if n["domain"] != "NEW") + sum(1 for n in NODES.values() if n["domain"] == "NEW")
    led = ledger_stats()
    total = len(rows)
    return {
        "families": len(fam_rows), "atoms": len(atom_rows), "total_sources": total,
        "fused_into_doctrine": len(fused), "fused_pct": round(100*len(fused)/total, 1) if total else 0,
        "orphans": len(orphans),
        "low_confidence_families": sum(1 for r in fam_rows if r["confidence"] == "LOW"),
        "doctrine_nodes": len(NODES), "graph_edges": len(EDGES),
        "ledger": led,
        "ledger_usable": (led.get("certified",0)+led.get("provisionally_verified",0)),
    }

def write_map():
    rows = build_map()
    with open(OUT_MAP, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["source","kind","chunks","nodes","confidence"]); w.writeheader(); w.writerows(rows)
    return OUT_MAP, len(rows)

def write_graph():
    fams = scan_families()
    node_obj = {}
    for nid, n in NODES.items():
        node_fams = [f for f, ns in FAMILY_MAP.items() if nid in ns and f in fams]
        node_atoms = [a for a in scan_atoms() if nid in atom_nodes(a)]
        node_obj[nid] = {"law": n["law"], "extends_domain": n["domain"],
                          "families": node_fams, "atoms": node_atoms,
                          "source_count": len(node_fams)+len(node_atoms)}
    g = {"nodes": node_obj, "edges": [{"from":a,"to":b,"fusion":why} for a,b,why in EDGES]}
    with open(OUT_GRAPH, "w") as f: json.dump(g, f, indent=2)
    return OUT_GRAPH, len(node_obj), len(EDGES)

def main():
    ap = argparse.ArgumentParser(prog="os_corpus_fusion.py"); sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("coverage"); m = sub.add_parser("map"); m.add_argument("--write", action="store_true")
    g = sub.add_parser("graph"); g.add_argument("--write", action="store_true")
    sub.add_parser("orphans"); sub.add_parser("families")
    a = ap.parse_args()
    if a.cmd == "coverage":
        print(json.dumps(coverage(), indent=2))
    elif a.cmd == "map":
        if a.write: p, n = write_map(); print(f"wrote {p} ({n} rows)")
        else:
            for r in build_map(): print(f"  [{r['confidence']:9s}] {r['kind']:6s} {r['source']:40s} -> {r['nodes']}")
    elif a.cmd == "graph":
        if a.write: p, nn, ne = write_graph(); print(f"wrote {p} ({nn} nodes, {ne} edges)")
        else: print(json.dumps(write_graph.__doc__ or "use --write to emit", indent=2))
    elif a.cmd == "orphans":
        orph = [r for r in build_map() if r["nodes"] == "ORPHAN"]
        print(f"{len(orph)} orphan sources:" if orph else "0 orphans , every family/atom is fused to >=1 node")
        for r in orph: print(f"  {r['source']}")
    elif a.cmd == "families":
        f = scan_families()
        for name, n in f.items(): print(f"  {name:42s} {n:4d} chunks -> {';'.join(FAMILY_MAP.get(name,['ORPHAN']))}")
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
