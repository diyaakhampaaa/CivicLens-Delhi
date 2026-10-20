
from urllib.parse import urlparse

from civic_sources import (
    CIVIC_SOURCES,
    get_all_sources,
    get_source,
    get_sources_for_issue,
)


def test_expected_sources_exist():
    assert "mcd" in CIVIC_SOURCES
    assert "ndmc" in CIVIC_SOURCES
    assert "delhi_pgms" in CIVIC_SOURCES


def test_sources_have_valid_https_links():
    for source in get_all_sources():
        for key in ("website", "complaints_url", "evidence_url"):
            parsed = urlparse(source[key])
            assert parsed.scheme == "https"
            assert parsed.netloc


def test_source_lookup():
    assert get_source("mcd")["name"].startswith("Municipal")
    assert get_source("unknown") is None


def test_pothole_has_candidate_sources():
    candidates = get_sources_for_issue("Pothole or damaged road")
    assert len(candidates) >= 2


def test_candidates_are_not_jurisdiction_confirmation():
    candidates = get_sources_for_issue("Pothole or damaged road")
    assert all("jurisdiction_note" in s for s in candidates)

def test_app_issue_label_matches_canonical_issue():
    candidates = get_sources_for_issue("Pothole / damaged road")
    assert len(candidates) >= 2

def test_all_app_issue_labels_return_candidates():
    app_issues = [
        "Pothole / damaged road",
        "Garbage / sanitation",
        "Broken streetlight",
        "Other civic issue",
    ]

    for issue in app_issues:
        assert get_sources_for_issue(issue), (
            f"No candidate sources configured for: {issue}"
        )
