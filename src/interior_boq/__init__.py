"""interior-boq: bill of quantities and quote maths for home interiors (India-ready: GST-inclusive rates)."""
from .boq import amounts, counted, fingerprint, is_supplier_line, option_groups, totals
from .catalog import CATEGORIES, DEFAULT_GST, ROOMS, UNITS, line_code
from .quote import quote_totals

__version__ = "0.1.0"
__all__ = ["amounts", "counted", "fingerprint", "is_supplier_line", "option_groups", "totals",
           "CATEGORIES", "DEFAULT_GST", "ROOMS", "UNITS", "line_code", "quote_totals"]
