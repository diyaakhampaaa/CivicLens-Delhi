import os
import re
from datetime import date
from urllib.parse import urlsplit, urlunsplit

import streamlit as st
from dotenv import load_dotenv
from tinyfish import TinyFish

from civic_sources import OFFICIAL_STARTING_POINTS, suggest_authorities
from map_view import render_delhi_map

load_dotenv()

st.set_page_config(
    page_title="CivicLens Delhi",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------- Theme ---------------------------
st.markdown(
    """
    <style>
    :root {
      --ivory:#fffaf2; --paper:#ffffff; --saffron:#e87924;
      --saffron-dark:#c65e12; --green:#28734d; --ink:#25282b;
      --muted:#626970; --line:#eadfd1; --soft-orange:#fff0df;
      --soft-green:#edf5ef; --red:#a52b24;
    }
    html, body, [class*="css"] { font-size:14px !important; }
    .stApp { background:var(--ivory); color:var(--ink); }
    [data-testid="stHeader"] { background:rgba(255,250,242,.97); }
    .block-container { max-width:1240px; padding:1rem 1.35rem 2rem; }
    h1 { font-size:1.8rem !important; line-height:1.2 !important; color:var(--ink) !important; margin:.25rem 0 .45rem !important; }
    h2 { font-size:1.25rem !important; color:var(--ink) !important; margin:.65rem 0 .45rem !important; }
    h3 { font-size:1.03rem !important; color:var(--ink) !important; }
    p, label, li { font-size:.91rem !important; }
   /* Modern CivicLens sidebar */
[data-testid="stSidebar"] {
    background: #fff7ed;
    border-right: 1px solid #ead8c5;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1rem;
}

[data-testid="stSidebar"] .block-container {
    padding: 1.2rem 0.9rem;
}

/* Sidebar headings */
[data-testid="stSidebar"] h2 {
    font-size: 1.25rem !important;
    font-weight: 750 !important;
    color: #292929 !important;
    margin-bottom: 0.2rem !important;
}

[data-testid="stSidebar"] h3 {
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    color: #353535 !important;
}

/* Sidebar text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    font-size: 0.85rem !important;
    color: #6c6259 !important;
}

/* Clickable navigation buttons */
[data-testid="stSidebar"] [data-testid="stButton"] button {
    width: 100%;
    min-height: 44px;
    justify-content: flex-start;
    text-align: left;
    background: #fffdf9 !important;
    color: #35302b !important;
    border: 1px solid #eadbca !important;
    border-radius: 10px !important;
    padding: 0.65rem 0.8rem !important;
    margin: 0.15rem 0 !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    box-shadow: 0 1px 2px rgba(80, 50, 20, 0.04);
    transition: all 0.15s ease;
}

[data-testid="stSidebar"] [data-testid="stButton"] button:hover {
    background: #ffedd9 !important;
    border-color: #e9a66d !important;
    color: #b9510c !important;
}

/* Softer separators */
[data-testid="stSidebar"] hr {
    border-color: #ead8c5 !important;
    margin: 1rem 0 !important;
}

/* Sidebar links */
[data-testid="stSidebar"] a {
    color: #b9510c !important;
    font-size: 0.84rem !important;
    text-decoration: none !important;
}

[data-testid="stSidebar"] a:hover {
    text-decoration: underline !important;
}
   
    .topbar { display:flex; align-items:center; justify-content:space-between; gap:1rem; padding:.7rem 1rem; margin:0 0 1rem; background:var(--paper); border:1px solid var(--line); border-top:4px solid var(--saffron); border-radius:12px; }
    .brand { display:flex; align-items:center; gap:.6rem; color:var(--ink); font-size:1.15rem; font-weight:800; white-space:nowrap; }
    .brand-mark { display:inline-flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:10px; background:var(--soft-orange); font-size:1.2rem; }
    .brand-sub { font-size:.74rem; color:var(--muted); font-weight:500; margin-top:1px; }
    .navlinks { display:flex; gap:.3rem; flex-wrap:wrap; justify-content:flex-end; }
    .navlinks a { color:var(--ink) !important; text-decoration:none !important; padding:.45rem .65rem; border-radius:8px; font-size:.84rem; font-weight:650; }
    .navlinks a:hover { background:var(--soft-orange); color:var(--saffron-dark) !important; }
    .hero { background:linear-gradient(105deg,#fff 0%,#fff5e6 100%); border:1px solid var(--line); border-left:5px solid var(--saffron); border-radius:13px; padding:1rem 1.25rem; margin-bottom:1rem; }
    .eyebrow { color:var(--green); font-size:.72rem; font-weight:800; letter-spacing:.08em; text-transform:uppercase; margin-bottom:.25rem; }
    .hero p { margin:0; color:var(--muted); }
    .feature { background:var(--paper); border:1px solid var(--line); border-radius:11px; padding:.8rem .9rem; min-height:85px; }
    .feature h3 { margin:0 0 .25rem; font-size:.98rem; }
    .feature p { margin:0; color:var(--muted); font-size:.82rem !important; }
    [data-testid="stForm"] { background:var(--paper); border:1px solid var(--line); border-radius:12px; padding:1rem; }
    .stTextInput input, .stTextArea textarea { background:#fff !important; color:var(--ink) !important; border:1px solid #d8cbbb !important; border-radius:8px !important; font-size:.9rem !important; }
    .stTextInput input:focus, .stTextArea textarea:focus { border-color:var(--saffron) !important; box-shadow:0 0 0 1px var(--saffron) !important; }
    [data-baseweb="select"] > div { background:#fff !important; border-color:#d8cbbb !important; border-radius:8px !important; }
    div.stButton > button, div.stFormSubmitButton > button, div.stDownloadButton > button { border-radius:8px !important; font-size:.88rem !important; font-weight:650 !important; min-height:2.25rem !important; padding:.4rem .85rem !important; }
    div[data-testid="stFormSubmitButton"] button, div.stButton > button[kind="primary"] { background:var(--saffron) !important; border:1px solid var(--saffron) !important; color:#fff !important; }
    div[data-testid="stFormSubmitButton"] button:hover, div.stButton > button[kind="primary"]:hover { background:var(--saffron-dark) !important; border-color:var(--saffron-dark) !important; }
    div.stDownloadButton > button { background:var(--green) !important; border:1px solid var(--green) !important; color:#fff !important; }
    a { color:var(--saffron-dark) !important; }
    [data-testid="stAlert"] { border-radius:9px; }
    hr { border-color:var(--line); }
    .small-note { color:var(--muted); font-size:.8rem; }
    .status-pill { display:inline-block; padding:.2rem .55rem; border-radius:999px; background:var(--soft-green); color:var(--green); font-size:.76rem; font-weight:700; }
    footer { visibility:hidden; }
    @media (max-width:760px) {
      .block-container { padding:.6rem .7rem 1.3rem; }
      .topbar { align-items:flex-start; flex-direction:column; }
      .navlinks { justify-content:flex-start; }
      .hero { padding:.85rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------- Helpers ---------------------------
def clean_sensitive_urls(text: str) -> str:
    """Strip credential-like query strings from URLs before displaying research."""
    pattern = r"https?://[^\s<>\"')\]]+"
    sensitive = re.compile(
        r"(api[_-]?key|access[_-]?token|auth|secret|password|client[_-]?secret|signature|sig)=",
        re.I,
    )

    def replace(match):
        raw = match.group(0)
        trailing = ""
        while raw and raw[-1] in ".,;:":
            trailing = raw[-1] + trailing
            raw = raw[:-1]
        try:
            parts = urlsplit(raw)
            if parts.query and sensitive.search(parts.query):
                raw = urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))
        except ValueError:
            pass
        return raw + trailing

    return re.sub(pattern, replace, str(text))


def run_tinyfish_research(source_url: str, issue: str, locality: str, details: str, landmark: str):
    if not os.getenv("TINYFISH_API_KEY"):
        raise RuntimeError("TINYFISH_API_KEY is missing. Add it to your local .env file.")
    client = TinyFish()
    goal = f"""
Research official public guidance for a Delhi resident about this civic issue.
Issue: {issue}
Locality: {locality}
Nearby landmark: {landmark or "Not provided"}
Description: {details or "Not provided"}
Research starting website: {source_url}

Find the relevant department and complaint channels, jurisdiction guidance,
official complaint/tracking links, public contact information and practical
next steps. Prefer current official government sources.

Rules:
- Research only. Do not submit a complaint, log in, or take irreversible actions.
- Never claim a complaint has been filed.
- Never invent an official, phone number, email, address, office hours, link,
  jurisdiction, or process.
- Mark details "Not verified" or "Not publicly found" if not confirmed.
- State if responsibility for the exact locality/road/ward is uncertain.
- Use specific source URLs for each key claim where possible.
- Include public department/designation; current department head only if a
  current official source confirms it; public phone/email; office address/hours;
  complaint and tracking URLs; source URLs and verification date if available.
- Separate findings, suggested steps, official links, contacts, and uncertainties.
- Treat the supplied issue description as user-provided, not independently verified.
Return concise Markdown.
"""
    response = client.agent.run(url=source_url, goal=goal)
    result = response.result
    if isinstance(result, dict):
        result = result.get("result", result)
    if not result:
        result = "The research run completed but returned no readable result."
    return clean_sensitive_urls(str(result)), str(response.status)


def make_complaint_draft(issue: str, locality: str, landmark: str, details: str) -> str:
    return (
        f"Subject: Request for assistance with {issue.lower()}\n\n"
        f"Location/locality: {locality.strip()}\n"
        f"Nearby landmark: {landmark.strip() or 'Not specified'}\n"
        f"Issue category: {issue}\n\n"
        f"Description:\n{details.strip()}\n\n"
        "I request that the relevant authority review this issue and advise on "
        "the appropriate corrective action. Please confirm whether this location "
        "falls within your jurisdiction and provide a reference number if a "
        "complaint is submitted through your official channel.\n"
    )


def jump_anchor(anchor: str):
    st.markdown(f'<div id="{anchor}"></div>', unsafe_allow_html=True)


# --------------------------- Header / navigation ---------------------------
st.markdown(
    """
    <div class="topbar">
      <div class="brand">
        <span class="brand-mark">🏙️</span>
        <div>CivicLens <span style="color:#d86b1f">Delhi</span>
          <div class="brand-sub">Civic guidance assistant</div>
        </div>
      </div>
      <nav class="navlinks">
        <a href="#report">Report issue</a>
        <a href="#map">Location</a>
        <a href="#results">Research</a>
        <a href="#draft">Draft</a>
      </nav>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 🏙️ CivicLens")
    st.caption("Delhi civic services")
    st.divider()
    st.markdown("**Navigate**")
    st.markdown("[Report an issue](#report)")
    st.markdown("[Select location](#map)")
    st.markdown("[Research results](#results)")
    st.markdown("[Complaint draft](#draft)")
    st.divider()
    st.markdown("**Quick links**")
    for label, url in OFFICIAL_STARTING_POINTS.items():
        st.markdown(f"[{label}]({url})")
    st.divider()
    st.caption("Research assistance only. This app does not submit complaints.")

st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">Delhi civic services</div>
      <h1>Find the right next step.</h1>
      <p>Explore official reporting channels and prepare a complaint draft for your review.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

f1, f2, f3 = st.columns(3)
with f1:
    st.markdown('<div class="feature"><h3>🛣️ Roads</h3><p>Potholes and damaged roads</p></div>', unsafe_allow_html=True)
with f2:
    st.markdown('<div class="feature"><h3>🧹 Cleanliness</h3><p>Garbage and sanitation</p></div>', unsafe_allow_html=True)
with f3:
    st.markdown('<div class="feature"><h3>💡 Streetlights</h3><p>Broken or non-working lights</p></div>', unsafe_allow_html=True)

# --------------------------- Map ---------------------------
jump_anchor("map")
st.markdown("## Select a location")
st.caption("Use the map if available, or type the locality below.")
try:
    selected_location = render_delhi_map()
except Exception as exc:
    selected_location = None
    st.info("Map is unavailable right now. You can still enter a locality manually.")
    st.caption(f"Map detail: {type(exc).__name__}")

default_locality = ""
default_landmark = ""
if selected_location:
    if selected_location.get("locality") not in (None, "", "Map-selected point"):
        default_locality = str(selected_location.get("locality"))
    default_landmark = str(selected_location.get("landmark", "") or "")
    with st.expander("Map selection details", expanded=False):
        st.write(f"Latitude: {selected_location.get('latitude', '—')}")
        st.write(f"Longitude: {selected_location.get('longitude', '—')}")

# --------------------------- Issue form ---------------------------
jump_anchor("report")
st.markdown("## Report an issue")

with st.form("issue_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        issue = st.selectbox(
            "Issue category",
            [
                "Pothole / damaged road",
                "Garbage / sanitation",
                "Broken streetlight",
                "Drainage / waterlogging",
                "Water supply",
                "Public toilet",
                "Other civic issue",
            ],
        )
        locality = st.text_input(
            "Locality / neighbourhood",
            value=default_locality,
            placeholder="e.g. Lajpat Nagar",
        )
        landmark = st.text_input(
            "Nearby landmark (optional)",
            value=default_landmark,
            placeholder="e.g. near the metro station",
        )
    with col2:
        authority = st.selectbox(
            "Research starting point",
            list(OFFICIAL_STARTING_POINTS.keys()),
            help="The research will start at this public website; jurisdiction still needs confirmation.",
        )
        details = st.text_area(
            "Issue description",
            placeholder="Describe what happened, where, and any useful details.",
            height=132,
        )
        st.caption("Do not include passwords, OTPs, ID numbers, or other sensitive information.")
    research_clicked = st.form_submit_button(
        "Research official guidance",
        type="primary",
        use_container_width=True,
    )

if research_clicked:
    if not locality.strip():
        st.warning("Enter a locality before starting research.")
    else:
        with st.spinner("Researching public information…"):
            try:
                result, status = run_tinyfish_research(
                    OFFICIAL_STARTING_POINTS[authority],
                    issue,
                    locality.strip(),
                    details.strip(),
                    landmark.strip(),
                )
                st.session_state["research_result"] = result
                st.session_state["research_status"] = status
                st.session_state["last_issue"] = issue
                st.session_state["last_locality"] = locality.strip()
                st.session_state["last_landmark"] = landmark.strip()
                st.session_state["last_details"] = details.strip()
                st.session_state["last_authority"] = authority
            except Exception as exc:
                st.error("Research could not be completed. Check your TinyFish API key, internet connection, and account access.")
                with st.expander("Technical details"):
                    st.code(f"{type(exc).__name__}: {exc}")

# --------------------------- Research output ---------------------------
jump_anchor("results")
if "research_result" in st.session_state:
    st.markdown("## Research findings")
    status = st.session_state.get("research_status", "Unknown")
    st.markdown(f'<span class="status-pill">Research status: {status}</span>', unsafe_allow_html=True)
    st.markdown(st.session_state["research_result"])
    st.caption("Verify official links and confirm jurisdiction before acting.")
    st.download_button(
        "Download research notes (.md)",
        data=st.session_state["research_result"],
        file_name="civiclens_research_notes.md",
        mime="text/markdown",
    )

# --------------------------- Complaint draft ---------------------------
jump_anchor("draft")
st.markdown("## Complaint draft")
st.caption("Create a draft to review or download. Nothing is submitted automatically.")

with st.form("draft_form", clear_on_submit=False):
    d1, d2 = st.columns(2)
    with d1:
        draft_locality = st.text_input(
            "Locality",
            value=st.session_state.get("last_locality", ""),
            key="draft_locality_input",
        )
        draft_issue = st.selectbox(
            "Issue",
            [
                "Pothole / damaged road",
                "Garbage / sanitation",
                "Broken streetlight",
                "Drainage / waterlogging",
                "Water supply",
                "Public toilet",
                "Other civic issue",
            ],
            index=[
                "Pothole / damaged road",
                "Garbage / sanitation",
                "Broken streetlight",
                "Drainage / waterlogging",
                "Water supply",
                "Public toilet",
                "Other civic issue",
            ].index(st.session_state.get("last_issue", "Pothole / damaged road"))
            if st.session_state.get("last_issue", "Pothole / damaged road") in [
                "Pothole / damaged road", "Garbage / sanitation", "Broken streetlight",
                "Drainage / waterlogging", "Water supply", "Public toilet", "Other civic issue"
            ] else 0,
            key="draft_issue_input",
        )
    with d2:
        draft_landmark = st.text_input(
            "Nearby landmark (optional)",
            value=st.session_state.get("last_landmark", ""),
            key="draft_landmark_input",
        )
        draft_details = st.text_area(
            "Description",
            value=st.session_state.get("last_details", ""),
            height=132,
            key="draft_details_input",
        )
    make_draft = st.form_submit_button("Create draft", type="primary")

if make_draft:
    if not draft_locality.strip() or not draft_details.strip():
        st.warning("Add a locality and description to create a useful draft.")
    else:
        st.session_state["complaint_draft"] = make_complaint_draft(
            draft_issue, draft_locality, draft_landmark, draft_details
        )

if "complaint_draft" in st.session_state:
    st.text_area(
        "Draft preview",
        value=st.session_state["complaint_draft"],
        height=220,
        key="draft_preview",
    )
    st.download_button(
        "Download complaint draft (.txt)",
        data=st.session_state["complaint_draft"],
        file_name="civiclens_complaint_draft.txt",
        mime="text/plain",
    )

st.divider()
st.caption("CivicLens Delhi")
