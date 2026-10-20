# CivicLens Delhi 🇮🇳

**A civic issue exploration and source-verification prototype for Delhi.**

CivicLens Delhi aims to help users explore a location, describe a civic issue, and identify relevant official government sources for further investigation. The project combines an interactive Delhi map, civic-source references, and TinyFish-powered web research.

## Features

- **Interactive Delhi map:** Explore approximate locality reference points or select a location by clicking the map.
- **Civic issue categories:** Supports potholes or damaged roads, garbage or sanitation, broken streetlights, and other civic issues.
- **Official source registry:** Includes references for the Municipal Corporation of Delhi (MCD), New Delhi Municipal Council (NDMC), and Delhi Public Grievance Monitoring System (PGMS).
- **Web research:** Uses TinyFish to investigate relevant information from a selected website.
- **Source verification notes:** Documents source references, evidence, and limitations.
- **Automated tests:** Tests civic-source records, URL formats, source lookup, and issue-label compatibility.

## Tech Stack

- Python
- Streamlit
- Folium
- streamlit-folium
- TinyFish
- python-dotenv
- pytest

## Project Structure

```text
civiclens/
├── app.py
├── civic_sources.py
├── map_view.py
├── GIS_SOURCE_NOTES.md
├── README.md
├── requirements.txt
└── tests/
    └── test_civic_sources.py
```

## Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd civiclens
```

Replace the placeholder with your team's actual repository URL.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your TinyFish API key:

```text
TINYFISH_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key. **Never commit `.env` or publish API keys to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL where you can open the application in your browser.

## Running Tests

Run the civic-source tests with:

```bash
python -m pytest tests/test_civic_sources.py -v
```

## Civic Data and Verification

The project currently references these official starting points:

- **MCD:** https://mcdonline.nic.in/
- **NDMC:** https://www.ndmc.gov.in/
- **Delhi PGMS:** https://pgms.delhi.gov.in/

These sources are starting points for research, not automatic confirmation of responsibility for a particular location or complaint.

## Limitations

- Map locality coordinates are approximate reference points.
- Selecting coordinates does not establish municipal jurisdiction.
- The map does not represent verified administrative boundaries.
- The prototype does not necessarily contain live civic-incident data.
- Information gathered through web research should be checked against its original official source.
- The application does not submit a complaint merely by selecting a location or researching a source.

## Team and Project

Developed as part of **Kritical Hacks 2026**.

CivicLens Delhi is a prototype intended to make civic information easier to explore and verify. Its findings should be treated as informational until independently confirmed.
# CivicLens-Delhi