#!/usr/bin/env python3
"""
os_business_gate.py

W4 keystone fix from INTERNAL_AGENCY_ENGINE_AUDIT_001.

The audit found that the business-gate BODIES named in the money doctrine
(os_offer_builder, os_pricing_gate-as-record-check, os_client_fit_gate-as-record-check)
did not exist as executable gates over a build's BUSINESS RECORD. The advisory
flag-driven helpers in this folder give a human a verdict on values typed at the
prompt; they do NOT read a build's emitted business record and fail closed. So an
offer / pricing / buyer claim could ship inside a build with nothing machine-checking
it against the money doctrine.

This gate closes that hole. It reads a single JSON business record emitted by a
build and enforces the money doctrine FAIL-CLOSED:

  OFFER (OS_MONEY_OFFER_DOCTRINE.md, OS_MONEY_PLAY_GATE.md value chain):
    - sells the MEAL (a finished, owned, audience-facing output) not the KITCHEN.
    - FAIL if the offer is an SREF pack, prompt pack, doctrine pack, the OS,
      a summary, notes, a field manual, or any other ingredient resale.
    - FAIL if payment is not made to follow proof: a price or rail is asserted
      with no proof / demand-signal field backing it.

  PRICING (OS_PRICING_GATE.md, OS_MONEY_OFFER_DOCTRINE.md):
    - FAIL if price is cost-plus / hourly basis rather than value / meaning.
    - FAIL if there is no three-option architecture (anchor high).
    - FAIL if a price is crowned with no demand_signal field (no price before demand).
    - scarcity / numbered edition expected for a status good.

  CLIENT-FIT (OS_MONEY_OFFER_DOCTRINE.md screen-before-pitch):
    - FAIL unless four explicit, non-placeholder fields are present:
      buyer_title, trigger_event, outcome_dollar_value, fit_screen (FIT/HOLD/PASS).
    - prose without the four fields FAILS.

Every gap is a FAIL, never a default pass:
  - missing / unreadable / empty / unparseable record
  - unknown --check value
  - any required field empty, missing, or a placeholder token

Usage:
  python os_business_gate.py --record <path> --check offer|pricing|client-fit|all

Exit codes:
  0 = PASS
  2 = FAIL (any reason, including any error reaching a verdict)

Stock Python 3 only. No external pip installs.
Fail-closed pattern mirrors os_activation_gate.py (exit 0 pass / exit 2 fail).
"""

import argparse
import json
import os
import sys


PLACEHOLDER_VALUES = {
    "n/a",
    "na",
    "none",
    "null",
    "todo",
    "tbd",
    "placeholder",
    "missing",
    "unknown",
    "not sure",
    "not applicable",
    "example",
    "sample",
    "...",
    "-",
    "",
}

# Ingredient-resale tells. If the offer's product reads as any of these, it is the
# KITCHEN (or an ingredient), not the MEAL, and the offer FAILS by default.
# Source: OS_MONEY_PLAY_GATE.md value chain + OS_MONEY_OFFER_DOCTRINE.md hard rule.
INGREDIENT_TELLS = [
    "sref pack",
    "sref-pack",
    "srefpack",
    "prompt pack",
    "prompt-pack",
    "promptpack",
    "doctrine pack",
    "doctrine-pack",
    "preset pack",
    "preset-pack",
    "the os",
    "this os",
    "our os",
    "the operating system",
    "book summary",
    "book summaries",
    "summary pack",
    "workflow notes",
    "field manual",
    "field-manual",
    "internal notes",
    "the corpus",
    "corpus access",
    "the recipe",
    "recipe pack",
    "template pack",
    "skill pack",
    "swipe file",
    "ingredient",
]

# Words that signal the product is an OWNED, finished, audience-facing output (the MEAL).
MEAL_TELLS = [
    "world",
    "campaign",
    "film",
    "series",
    "edition",
    "editions",
    "product",
    "ip",
    "intellectual property",
    "character",
    "story",
    "brand",
    "experience",
    "deliverable",
    "finished",
    "owned",
    "gallery",
    "publication",
    "issue",
    "drop",
    "collection",
    "book",
    "documentary",
    "asset",
    "system",
    "installation",
]


def _fail(report_lines, reason):
    """Append a fatal reason and signal a fail-closed verdict."""
    report_lines.append("FAIL-CLOSED: " + reason)
    return False


def _nonempty_str(value):
    """True only for a non-empty, non-whitespace string."""
    return isinstance(value, str) and value.strip() != ""


def _is_placeholder(value):
    """True for empty values or common placeholder tokens that never count as proof."""
    if not _nonempty_str(value):
        return True
    return value.strip().lower() in PLACEHOLDER_VALUES


def _present_field(record, key):
    """A field counts only if present, a non-empty string, and not a placeholder."""
    return key in record and not _is_placeholder(record.get(key))


def _has_signal(record, keys):
    """
    True if any of the given keys carries a real, non-placeholder value.
    A demand/proof signal can be a string OR a truthy structured value
    (a number, a non-empty list, a non-empty dict).
    """
    for key in keys:
        if key not in record:
            continue
        value = record.get(key)
        if isinstance(value, str):
            if not _is_placeholder(value):
                return True
        elif isinstance(value, bool):
            if value:
                return True
        elif isinstance(value, (int, float)):
            if value:
                return True
        elif isinstance(value, (list, dict)):
            if value:
                return True
        elif value is not None:
            return True
    return False


def load_record(path, report_lines):
    """Load the business record JSON. Any problem is a FAIL, never a silent pass."""
    if not path:
        return None, _fail(report_lines, "no record path supplied")
    if not os.path.isfile(path):
        return None, _fail(report_lines, "record not found on disk: %s" % path)
    try:
        with open(path, "r", encoding="utf-8") as handle:
            raw = handle.read()
    except OSError as exc:
        return None, _fail(report_lines, "record could not be read (%s): %s" % (exc, path))
    if raw.strip() == "":
        return None, _fail(report_lines, "record is empty: %s" % path)
    try:
        data = json.loads(raw)
    except ValueError as exc:
        return None, _fail(report_lines, "record could not be parsed as JSON (%s): %s" % (exc, path))
    if not isinstance(data, dict):
        return None, _fail(report_lines, "record top level must be a JSON object, got %s" % type(data).__name__)
    if not data:
        return None, _fail(report_lines, "record JSON object is empty")
    return data, True


# --------------------------------------------------------------------------- #
# OFFER check
# --------------------------------------------------------------------------- #
def check_offer(record, report_lines):
    """
    Sells the MEAL not the KITCHEN, and payment follows proof.
    Fail closed on ingredient resale or a price/rail with no proof signal.
    """
    ok = True
    report_lines.append("OFFER check (sell the meal, payment-follows-proof):")

    offer = record.get("offer")
    if not isinstance(offer, dict):
        return _fail(report_lines, "record has no 'offer' object")

    product = offer.get("product")
    if _is_placeholder(product):
        ok = _fail(report_lines, "offer.product is empty or placeholder (no owned output named)")
        product_l = ""
    else:
        product_l = product.strip().lower()
        report_lines.append("  product: %s" % product.strip())

    # ingredient-resale tells in product OR an explicit product_type
    haystacks = [product_l]
    ptype = offer.get("product_type")
    if _nonempty_str(ptype):
        haystacks.append(ptype.strip().lower())
    combined = " ".join(haystacks)

    hit = next((tell for tell in INGREDIENT_TELLS if tell in combined), None)
    if hit is not None:
        ok = _fail(
            report_lines,
            "offer sells the KITCHEN / an ingredient ('%s'); the corpus is ingredients, "
            "not the product. Sell a finished owned output (the meal)." % hit,
        )

    # an explicit ingredient_resale flag is an immediate fail unless operator-asked
    if offer.get("is_ingredient_resale") is True and offer.get("operator_explicitly_asked") is not True:
        ok = _fail(
            report_lines,
            "offer.is_ingredient_resale is true and operator did not explicitly ask; "
            "ingredient resale is disqualified by default",
        )

    # confirm it reads as a meal (owned, finished, audience-facing)
    if product_l and not any(tell in combined for tell in MEAL_TELLS):
        if offer.get("sells_owned_output") is not True:
            ok = _fail(
                report_lines,
                "offer.product does not read as a finished owned output (the meal) and "
                "offer.sells_owned_output is not asserted true",
            )
    elif product_l:
        report_lines.append("  reads as a finished owned output (the meal): OK")

    # payment follows proof: a price or rail must be backed by a proof/demand signal
    price_asserted = _has_signal(offer, ["price", "price_anchor"]) or _has_signal(
        record.get("pricing", {}) if isinstance(record.get("pricing"), dict) else {},
        ["anchor", "best", "better", "good", "price"],
    )
    rail_asserted = _has_signal(offer, ["payment_rail", "rail", "checkout", "payment_link"])

    proof_keys = ["proof", "demand_signal", "demand", "proof_signal", "yes_received"]
    has_proof = _has_signal(offer, proof_keys) or _has_signal(record, proof_keys)

    if (price_asserted or rail_asserted) and not has_proof:
        ok = _fail(
            report_lines,
            "payment-follows-proof violated: a price%s is asserted with no proof / "
            "demand_signal field. No rails before a real yes." % (" or rail" if rail_asserted else ""),
        )
    elif price_asserted or rail_asserted:
        report_lines.append("  payment-follows-proof: price/rail is backed by a proof/demand signal: OK")
    else:
        report_lines.append("  no price/rail asserted yet (no payment-follows-proof claim to check): OK")

    if ok:
        report_lines.append("  OFFER: PASS (sells the meal; no premature rails)")
    return ok


# --------------------------------------------------------------------------- #
# PRICING check
# --------------------------------------------------------------------------- #
def check_pricing(record, report_lines):
    """
    Value/meaning basis, three-option anchor-high architecture, no price before demand,
    scarcity expected for a status good.
    """
    ok = True
    report_lines.append("PRICING check (value-basis, 3-option anchor, no price before demand):")

    pricing = record.get("pricing")
    if not isinstance(pricing, dict):
        return _fail(report_lines, "record has no 'pricing' object")

    # value vs cost-plus basis
    basis = pricing.get("basis")
    if _is_placeholder(basis):
        ok = _fail(report_lines, "pricing.basis missing; must be 'value' (not cost-plus / hourly)")
    else:
        basis_l = basis.strip().lower()
        if basis_l in ("value", "meaning", "outcome", "value/meaning", "value-meaning"):
            report_lines.append("  basis: %s (value/meaning): OK" % basis.strip())
        elif basis_l in ("cost", "cost-plus", "cost_plus", "hourly", "time", "rate", "markup"):
            ok = _fail(report_lines, "pricing.basis is cost-plus / hourly ('%s'); price the value, not the cost" % basis.strip())
        else:
            ok = _fail(report_lines, "pricing.basis '%s' is not a recognized value basis" % basis.strip())

    # three-option architecture, anchor high
    options = pricing.get("options")
    if not isinstance(options, list) or len(options) < 3:
        ok = _fail(
            report_lines,
            "pricing has no three-option architecture (need an 'options' list of at least 3: anchor high)",
        )
    else:
        # pull numeric amounts to confirm an anchor-high spread exists
        amounts = []
        for opt in options:
            if isinstance(opt, dict):
                amt = opt.get("price", opt.get("amount"))
            else:
                amt = opt
            if isinstance(amt, bool):
                amt = None
            if isinstance(amt, (int, float)):
                amounts.append(float(amt))
        if len(amounts) < 3:
            ok = _fail(report_lines, "three options present but fewer than 3 carry a numeric price; cannot confirm an anchor")
        elif max(amounts) <= min(amounts):
            ok = _fail(report_lines, "three options present but no high anchor (all prices equal); anchor must be high")
        else:
            report_lines.append("  three-option architecture, anchor high (%s): OK" % "/".join(str(int(a)) if a.is_integer() else str(a) for a in amounts))

    # no price before demand: any crowned price needs a demand_signal
    crowned = _has_signal(pricing, ["anchor", "crowned_price", "final_price", "price"])
    if not crowned and isinstance(options, list):
        crowned = any(
            isinstance(o, dict) and o.get("crowned") is True and _has_signal(o, ["price", "amount"])
            for o in options
        )
    if crowned:
        demand = _has_signal(pricing, ["demand_signal", "demand", "proof"]) or _has_signal(
            record, ["demand_signal", "demand", "proof"]
        )
        if not demand:
            ok = _fail(report_lines, "a price is crowned with no demand_signal field; no price before demand")
        else:
            report_lines.append("  crowned price is backed by a demand_signal: OK")
    else:
        report_lines.append("  no price crowned yet (no price-before-demand claim to check): OK")

    # scarcity / numbered edition expected for a status good
    if pricing.get("status_good") is True:
        scarcity = _has_signal(pricing, ["scarcity", "numbered_edition", "edition_size", "limited"])
        if not scarcity:
            ok = _fail(
                report_lines,
                "status_good is true but no scarcity / numbered_edition field; a status good must be scarce",
            )
        else:
            report_lines.append("  status good carries scarcity / numbered edition: OK")

    if ok:
        report_lines.append("  PRICING: PASS")
    return ok


# --------------------------------------------------------------------------- #
# CLIENT-FIT check
# --------------------------------------------------------------------------- #
def check_client_fit(record, report_lines):
    """
    Four explicit, non-placeholder fields required:
    buyer_title, trigger_event, outcome_dollar_value, fit_screen (FIT/HOLD/PASS).
    Prose without the four fields FAILS.
    """
    ok = True
    report_lines.append("CLIENT-FIT check (four explicit fields, screen before pitch):")

    cf = record.get("client_fit")
    if not isinstance(cf, dict):
        return _fail(report_lines, "record has no 'client_fit' object (prose without the four fields FAILS)")

    required = ["buyer_title", "trigger_event", "outcome_dollar_value", "fit_screen"]
    for field in required:
        if not _present_field(cf, field):
            ok = _fail(report_lines, "client_fit.%s is missing, empty, or a placeholder" % field)
        else:
            report_lines.append("  %s: %s" % (field, str(cf.get(field)).strip()))

    # outcome_dollar_value must read as a real dollar value, not prose
    odv = cf.get("outcome_dollar_value")
    if _present_field(cf, "outcome_dollar_value"):
        has_digit = any(ch.isdigit() for ch in str(odv))
        if not has_digit:
            ok = _fail(report_lines, "client_fit.outcome_dollar_value carries no number; needs a real dollar value")

    # fit_screen must be one of the three explicit verdicts
    fs = cf.get("fit_screen")
    if _present_field(cf, "fit_screen"):
        if str(fs).strip().upper() not in ("FIT", "HOLD", "PASS"):
            ok = _fail(report_lines, "client_fit.fit_screen must be FIT, HOLD, or PASS (got '%s')" % str(fs).strip())

    if ok:
        report_lines.append("  CLIENT-FIT: PASS (all four fields explicit and non-placeholder)")
    return ok


CHECKS = {
    "offer": check_offer,
    "pricing": check_pricing,
    "client-fit": check_client_fit,
}


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Fail-closed business gate (W4, INTERNAL_AGENCY_ENGINE_AUDIT_001)."
    )
    parser.add_argument("--record", required=True, help="path to a build's business record JSON")
    parser.add_argument(
        "--check",
        required=True,
        choices=["offer", "pricing", "client-fit", "all"],
        help="which money-doctrine check to run",
    )
    args = parser.parse_args(argv)

    report_lines = []
    report_lines.append("=" * 70)
    report_lines.append("OS BUSINESS GATE (fail-closed) , check=%s" % args.check)
    report_lines.append("=" * 70)

    record, r_ok = load_record(args.record, report_lines)

    if not (r_ok and record is not None):
        verdict = False
    else:
        if args.check == "all":
            to_run = ["offer", "pricing", "client-fit"]
        else:
            to_run = [args.check]

        verdict = True
        for idx, name in enumerate(to_run):
            if idx:
                report_lines.append("")
            check_fn = CHECKS.get(name)
            if check_fn is None:
                verdict = _fail(report_lines, "unknown check '%s'" % name)
                continue
            result = check_fn(record, report_lines)
            verdict = verdict and result

    report_lines.append("-" * 70)
    report_lines.append("VERDICT: %s" % ("PASS" if verdict else "FAIL"))
    if not verdict:
        report_lines.append(
            "This business record is NOT ship-eligible: at least one money-doctrine check "
            "failed, or the gate could not reach a clean verdict. Fail-closed by design."
        )
    report_lines.append("=" * 70)

    print("\n".join(report_lines))
    return 0 if verdict else 2


if __name__ == "__main__":
    sys.exit(main())
