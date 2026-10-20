
import os
import re
from urllib.parse import urlsplit, urlunsplit

import streamlit as st
from dotenv import load_dotenv
from tinyfish import TinyFish
from civic_sources import get_sources_for_issue
from map_view import render_delhi_map

load_dotenv()

st.set_page_config(
    page_title="CivicLens Delhi",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Visual styling ----------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(145deg, #0b1220 0%, #111c30 55%, #17233a 100%);
        color: #f3f6fc;
    }
    [data-testid="stSidebar"] {
        background: #101a2b;
        border-right: 1px solid #26344a;
    }
    .hero {
        padding: 1.6rem 1.8rem;
        border: 1px solid #34445d;
        border-radius: 22px;
        background: linear-gradient(120deg, #182b42, #202443);
        margin-bottom: 1.2rem;
    }
    .eyebrow {
        color: #65e0cc;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
    }
    .muted { color: #b8c4d8; }
    div.stButton > button, div.stFormSubmitButton > button {
        border-radius: 10px;
        font-weight: 650;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Helpers ----------
SOURCES = {
    "Municipal Corporation of Delhi (MCD)": "https://mcdonline.nic.in/",
    "New Delhi Municipal Council (NDMC)": "https://www.ndmc.gov.in/",
    "Delhi public grievance portal (jurisdiction must be checked)": (
        "https://pgms.delhi.gov.in/"
    ),
}


def clean_sensitive_urls(text):
    """Remove query strings from URLs if they contain credential-like parameters."""
    url_pattern = r"https?://[^\s<>\])]+"
    sensitive = re.compile(
        r"(api[_-]?key|access[_-]?token|auth|secret|password|app_id|"
        r"client[_-]?secret|signature|sig)=",
        re.IGNORECASE,
    )

    def replace_url(match):
        raw_url = match.group(0)
        trailing = ""

        while raw_url and raw_url[-1] in ".,;:":
            trailing = raw_url[-1] + trailing
            raw_url = raw_url[:-1]

        try:
            parts = urlsplit(raw_url)
            if parts.query and sensitive.search(parts.query):
                raw_url = urlunsplit(
                    (parts.scheme, parts.netloc, parts.path, "", "")
                )
        except ValueError:
            pass

        return raw_url + trailing

    return re.sub(url_pattern, replace_url, text)


def research_civic_guidance(source_url, issue, locality, details):
    api_key = os.getenv("TINYFISH_API_KEY")
    if not api_key:
        raise RuntimeError(
            "TINYFISH_API_KEY is missing. Add it to your local .env file."
        )

    client = TinyFish()
    goal = f"""
Research how a Delhi resident can report this civic issue:
Issue category: {issue}
Locality supplied by user: {locality}
Additional details supplied by user: {details or "Not provided"}

Use the selected starting website as your research starting point.
Find relevant complaint channels, instructions, contact information,
jurisdiction guidance, and source URLs where available.

Rules:
- Do not submit a complaint, log in, or perform any irreversible action.
- Do not claim that a complaint has been filed.
- Do not invent a phone number, office, link, jurisdiction, or procedure.
- Distinguish verified findings from information you could not verify.
- If the selected authority may not cover the user's locality, say so.
- Cite the specific source pages used, not just the homepage.
- Return concise Markdown with headings:
  1. What I could verify
  2. Suggested next steps
  3. Relevant official links
  4. What remains uncertain
- Treat user-supplied details as information to investigate, not as
  independently verified facts.

  
Also investigate public-facing department contact information.

Include these fields where available:
- Responsible department and official designation.
- Name of the current department head or responsible officer,
  only if confirmed on a current official source.
- Official public office phone number and email address.
- Public office address and office hours, if published.
- Official complaint registration and tracking URLs.
- Source URL supporting each contact or officer detail.
- Date of verification, if available from the source.

Important:
- Prefer official government websites and official documents.
- Do not guess a person's name, designation, phone number, or email.
- Do not expose private contact details, credentials, or API tokens.
- If a detail cannot be verified, write "Not verified" or
  "Not publicly found"; never fill it with an assumption.
- Distinguish the department head from the officer responsible
  for the particular ward, road, or complaint.
- State when the responsible authority for the exact location
  remains uncertain.

"""
    response = client.agent.run(url=source_url, goal=goal)

    result = response.result
    if isinstance(result, dict):
        result = result.get("result", result)

    if not result:
        result = "The research run completed but returned no readable result."

    return clean_sensitive_urls(str(result)), str(response.status)


# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## 🏙️ CivicLens")
    st.caption("Delhi civic navigation assistant")
    st.markdown("---")
    st.markdown("**How it works**")
    st.markdown(
        "1. Describe a civic issue\n"
        "2. Choose a research starting point\n"
        "3. Review sourced guidance\n"
        "4. Prepare a draft for your own review"
    )
    st.markdown("---")
    st.caption("Research assistance only. No complaint is submitted.")
    st.caption("Never enter passwords, OTPs, or other sensitive information.")

# ---------- Main screen ----------
st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">Civic information · Delhi</div>
      <h1 style="margin-bottom:0.4rem;">Make your next civic step clearer.</h1>
      <p class="muted">
        Describe a local issue, investigate relevant public-service channels,
        and prepare a complaint draft you can review yourself.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown("### 🛣️ Roads")
    st.caption("Potholes and damaged roads")
with col_b:
    st.markdown("### 🧹 Cleanliness")
    st.caption("Garbage and sanitation")
with col_c:
    st.markdown("### 💡 Streetlights")
    st.caption("Broken or non-working lights")

# ---------- GIS Map Section  ----------
st.markdown("---")
selected_location = render_delhi_map()

# Display selected coordinates on the dashboard if available
if selected_location:
    st.write(
        "Selected location:",
        selected_location["latitude"],
        selected_location["longitude"],
    )

# Auto-fill locality name if chosen via the map
default_locality_value = ""
if selected_location and selected_location.get("locality") != "Map-selected point":
    default_loc = selected_location.get("locality", "")
    if default_loc:
        default_locality_value = default_loc

st.markdown("## 1. Describe the issue")

with st.form("issue_form"):
    left, right = st.columns(2)

    with left:
        issue = st.selectbox(
            "Issue category",
            [
                "Pothole / damaged road",
                "Garbage / sanitation",
                "Broken streetlight",
                "Other civic issue",
            ],
        )
        locality = st.text_input(
            "Delhi locality or neighbourhood",
            value=default_locality_value,
            placeholder="e.g. Lajpat Nagar",
        )

    with right:
        authority = st.selectbox(
            "Research starting point",
            list(SOURCES.keys()),
            help=(
                "This selects a website to investigate; it does not confirm "
                "which authority is responsible for your exact address."
            ),
        )
        details = st.text_area(
            "Optional details",
            placeholder="Nearby landmark, what is wrong, or how long it has persisted…",
            height=110,
        )

    research_clicked = st.form_submit_button(
        "🔎 Research official guidance",
        type="primary",
        use_container_width=True,
    )

if research_clicked:
    if not locality.strip():
        st.warning("Please enter a locality so the research has useful context.")
    else:
        with st.spinner("Investigating public information… this may take a little while."):
            try:
                result, status = research_civic_guidance(
                    SOURCES[authority],
                    issue,
                    locality.strip(),
                    details.strip(),
                )
                st.session_state["research_result"] = result
                st.session_state["research_status"] = status
                st.session_state["last_issue"] = issue
                st.session_state["last_locality"] = locality.strip()
                st.session_state["last_details"] = details.strip()
            except Exception as exc:
                st.error(
                    "The research request failed. Check your .env key, "
                    "internet connection, and TinyFish account, then try again."
                )
                st.caption(f"Technical detail: {type(exc).__name__}: {exc}")

# ---------- Research results ----------
if "research_result" in st.session_state:
    st.markdown("---")
    st.markdown("## 2. Research findings")
    st.caption(
        f"TinyFish run status: {st.session_state.get('research_status', 'Unknown')}"
    )
    st.info(
        "Review the linked sources yourself. A completed research run does not "
        "guarantee that every detail is current or that the selected authority "
        "covers your exact location."
    )
    st.markdown(st.session_state["research_result"])

# ---------- Complaint draft ----------
st.markdown("---")
st.markdown("## 3. Prepare a complaint draft")
st.caption(
    "This creates editable text only. It does not send a complaint or create a case."
)

draft_issue = st.session_state.get("last_issue", "Civic issue")
draft_locality = st.session_state.get("last_locality", "")
draft_details = st.session_state.get("last_details", "")

with st.form("draft_form"):
    draft_locality = st.text_input(
        "Locality for draft",
        value=draft_locality,
        key="draft_locality_input",
    )
    draft_issue = st.text_input(
        "Issue for draft",
        value=draft_issue,
        key="draft_issue_input",
    )
    draft_details = st.text_area(
        "Description for draft",
        value=draft_details,
        key="draft_details_input",
        height=100,
    )
    make_draft = st.form_submit_button("Create draft")

if make_draft:
    if not draft_locality.strip() or not draft_details.strip():
        st.warning("Add a locality and a short description to create a useful draft.")
    else:
        draft = (
            "Subject: Request for assistance with a civic issue\n\n"
            f"Location/locality: {draft_locality.strip()}\n"
            f"Issue category: {draft_issue.strip()}\n\n"
            "Description:\n"
            f"{draft_details.strip()}\n\n"
            "I request that the relevant authority review this issue and advise "
            "on the appropriate next steps. Please confirm the responsible "
            "authority and any reference number through the official channel, "
            "if a complaint is subsequently submitted.\n"
        )
        st.text_area("Your draft — review before use", value=draft, height=220)
        st.download_button(
            "Download draft (.txt)",
            data=draft,
            file_name="civiclens_complaint_draft.txt",
            mime="text/plain",
        )

st.markdown("---")
st.caption(
    "CivicLens Delhi · Hackathon prototype · Verify official channels and "
    "jurisdiction before acting."
)
