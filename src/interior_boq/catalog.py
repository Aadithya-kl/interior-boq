"""Standard work categories, units and rooms for Indian home-interior BOQs. Override freely."""

CATEGORIES = {  # key: (label, line-code prefix)
    "civil": ("Civil and false ceiling", "CV"), "carpentry": ("Carpentry and modular", "CP"),
    "furniture": ("Loose furniture", "FU"), "electrical": ("Electrical and lighting", "EL"),
    "plumbing": ("Plumbing and sanitary", "PL"), "flooring": ("Flooring and tiling", "FL"),
    "paint": ("Paint and wall finishes", "PT"), "soft": ("Soft furnishing and decor", "SF"),
    "appliances": ("Appliances", "AP"), "services": ("Services and transport", "SV"),
}
UNITS = {"sqft": "sq ft", "rft": "running ft", "nos": "nos", "set": "set", "lot": "lot", "sqm": "sq m"}
ROOMS = ["Whole home", "Foyer", "Living", "Dining", "Kitchen", "Master bedroom", "Bedroom 2", "Bedroom 3",
         "Kids room", "Guest room", "Puja", "Study", "Bathrooms", "Balcony", "Utility"]
DEFAULT_GST = 18.0


def line_code(category: str, n: int) -> str:
    """e.g. line_code("carpentry", 3) -> "CP-003"."""
    return f"{CATEGORIES[category][1]}-{n:03d}"
