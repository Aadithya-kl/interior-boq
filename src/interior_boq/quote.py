"""Quote totals with a discount taken on the value before GST, and the CGST/SGST or IGST split."""
from typing import List, Optional

from .catalog import DEFAULT_GST


def quote_totals(lines: List[dict], discount: Optional[dict] = None, intra_state: bool = True) -> dict:
    """lines: [{"unit_price": incl. GST, "qty": n, "gst_pct": 18}].
    discount: {"pct": 10} or {"amount": 5000}, optional {"max_amount": cap}. The discount reduces taxable value,
    and GST is recalculated on what is left (never discounting the tax itself)."""
    subtotal_incl = taxable = 0.0
    rows = []
    for l in lines:
        g = float(l.get("gst_pct") or DEFAULT_GST)
        amount = float(l.get("unit_price") or 0) * float(l.get("qty") or 0)
        tx = round(amount / (1 + g / 100), 2)
        rows.append((tx, g))
        subtotal_incl += amount
        taxable += tx
    d = discount or {}
    disc = 0.0
    if d.get("pct"):
        disc = taxable * float(d["pct"]) / 100
    elif d.get("amount"):
        disc = min(float(d["amount"]), taxable)
    if d.get("max_amount"):
        disc = min(disc, float(d["max_amount"]))
    factor = (1 - disc / taxable) if taxable else 1
    gst = sum(tx * factor * g / 100 for tx, g in rows)
    taxable_after = taxable - disc
    split = ({"cgst": round(gst / 2, 2), "sgst": round(gst / 2, 2), "igst": 0.0} if intra_state
             else {"cgst": 0.0, "sgst": 0.0, "igst": round(gst, 2)})
    return {"subtotal_incl_gst": round(subtotal_incl, 2), "taxable_before_discount": round(taxable, 2),
            "discount_amount": round(disc, 2), "discount_pct_effective": round(disc / taxable * 100, 2) if taxable else 0,
            "taxable_value": round(taxable_after, 2), "gst": round(gst, 2), **split, "total": round(taxable_after + gst),
            "savings_incl_gst": round(subtotal_incl - (taxable_after + gst), 2)}
