
"""Official starting points for CivicLens Delhi.

These sources are research starting points, not a definitive jurisdiction
lookup. The responsible authority must be verified for the reported location.
"""

CIVIC_SOURCES = {
    "mcd": {
        "name": "Municipal Corporation of Delhi (MCD)",
        "website": "https://mcdonline.nic.in/",
        "complaints_url": "https://mcdonline.nic.in/portal/feedback",
        "issues": [
            "Pothole or damaged road",
            "Garbage or sanitation",
            "Broken streetlight",
        ],
        "evidence_url": (
            "https://mcdonline.nic.in/portal/downloadFile/"
            "circular_reg._complaints_lodged_on_mcd_311_app_230824113534834.pdf"
        ),
        "verified_claims": [
            "An official MCD circular lists potholes on roads.",
            "The circular lists non-removal of municipal solid waste.",
            "The circular lists non-functioning of streetlights.",
            "MCD publishes information about its MCD 311 complaint channel.",
        ],
        "jurisdiction_note": (
            "Candidate source only. Verify whether the reported location "
            "falls within MCD responsibility."
        ),
    },
    "ndmc": {
        "name": "New Delhi Municipal Council (NDMC)",
        "website": "https://www.ndmc.gov.in/",
        "complaints_url": "https://www.ndmc.gov.in/complaints.aspx",
        "issues": [
            "Pothole or damaged road",
            "Garbage or sanitation",
            "Broken streetlight",
            "Other civic issue",
        ],
        "evidence_url": "https://www.ndmc.gov.in/complaints.aspx",
        "verified_claims": [
            "NDMC publishes an official complaints page.",
            "The page describes the NDMC 311 mobile app.",
            "The page lists complaint contact options.",
        ],
        "jurisdiction_note": (
            "Do not infer NDMC jurisdiction from the phrase 'New Delhi'. "
            "Verify the specific locality."
        ),
    },
    "delhi_pgms": {
        "name": "Delhi Public Grievance Monitoring System (PGMS)",
        "website": "https://pgms.delhi.gov.in/",
        "complaints_url": "https://pgms.delhi.gov.in/",
        "issues": [
            "Other civic issue",
            "Pothole or damaged road",
            "Garbage or sanitation",
            "Broken streetlight",
        ],
        "evidence_url": "https://pgms.delhi.gov.in/",
        "verified_claims": [
            "The portal provides a grievance route connected to "
            "departments of the Government of NCT of Delhi.",
            "The portal provides grievance registration and status features.",
        ],
        "jurisdiction_note": (
            "General government grievance route. Check scope and eligibility "
            "before recommending it for a particular issue."
        ),
    },
}


# Canonical issue labels used by the source records.
ISSUE_TYPES = [
    "Pothole or damaged road",
    "Garbage or sanitation",
    "Broken streetlight",
    "Other civic issue",
]


# Accept the labels already used by your existing app.py.
ISSUE_ALIASES = {
    "Pothole / damaged road": "Pothole or damaged road",
    "Pothole or damaged road": "Pothole or damaged road",
    "Garbage / sanitation": "Garbage or sanitation",
    "Garbage or sanitation": "Garbage or sanitation",
    "Broken streetlight": "Broken streetlight",
    "Other civic issue": "Other civic issue",
}


def get_all_sources():
    """Return all configured source records."""
    return list(CIVIC_SOURCES.values())


def get_source(source_id):
    """Return a source record by ID, or None if not found."""
    return CIVIC_SOURCES.get(source_id)


def get_sources_for_issue(issue):
    """Return candidate sources for an issue, not a jurisdiction verdict."""
    canonical_issue = ISSUE_ALIASES.get(issue, issue)

    return [
        source
        for source in CIVIC_SOURCES.values()
        if canonical_issue in source["issues"]
    ]
