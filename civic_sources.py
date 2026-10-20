"""Official starting points for Delhi civic-service research.

These are starting websites, not a guarantee that an authority owns a particular
street or complaint. Always verify jurisdiction and current contact details.
"""

OFFICIAL_STARTING_POINTS = {
    "Municipal Corporation of Delhi (MCD)": "https://mcdonline.nic.in/",
    "New Delhi Municipal Council (NDMC)": "https://www.ndmc.gov.in/",
    "Delhi public grievance portal": "https://pgms.delhi.gov.in/",
    "Delhi Government portal": "https://delhi.gov.in/",
}

def suggest_authorities(issue: str, locality: str = ""):
    """Return broad research suggestions; not a jurisdiction determination."""
    issue_lower = (issue or "").lower()
    suggestions = []
    if "streetlight" in issue_lower or "road" in issue_lower or "pothole" in issue_lower:
        suggestions.extend(["MCD", "NDMC"])
    elif any(word in issue_lower for word in ("garbage", "sanitation", "toilet", "drainage")):
        suggestions.extend(["MCD", "NDMC"])
    else:
        suggestions.extend(["MCD", "NDMC", "Delhi public grievance portal"])
    return {
        "suggestions": suggestions,
        "note": "Suggestions are only research starting points. Confirm the responsible authority for the exact location.",
    }
