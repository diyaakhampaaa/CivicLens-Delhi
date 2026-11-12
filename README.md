# CivicLens Delhi 🇮🇳

**From civic problem to the right complaint channel.**

CivicLens Delhi is an AI-assisted civic information and exploration platform developed for **Kritical Hacks 2026**. It aims to help Delhi residents explore local civic issues, discover relevant government authorities, and understand the appropriate channels for reporting problems such as potholes, damaged roads, garbage accumulation, sanitation issues, and broken streetlights.

By combining interactive maps, official civic-source references, and TinyFish-powered web research, CivicLens makes civic information easier to discover, understand, and verify.

## 🎯 The Problem

Finding the right government authority or official complaint channel for a local civic issue can be confusing.

Residents may struggle to identify:
- Which municipal authority is responsible for their locality.
- Where and how to report a civic problem.
- Which official website or complaint portal to trust.
- What information they should prepare before submitting a complaint.

## 💡 Our Solution

CivicLens Delhi provides a guided civic-information experience that connects location exploration, issue identification, and AI-assisted web research.

Users can explore a location, select a civic issue, discover relevant official sources, and investigate available reporting instructions.

## ✨ Features

- **Interactive Delhi Map:** Explore approximate locality reference points or select a location directly on the map.
- **Civic Issue Categories:** Explore common issues, including potholes, damaged roads, garbage accumulation, sanitation, and broken streetlights.
- **Official Source Registry:** References government platforms such as MCD, NDMC, and Delhi Public Grievance Monitoring System (PGMS).
- **TinyFish Integration:** Use web research to investigate relevant civic information and reporting instructions.
- **Source Verification:** Provide source references, research evidence, and limitations to help users verify findings.
- **Complaint Preparation:** Organize civic issue details and prepare complaint information for users to review.
- **Automated Testing:** Validate civic-source records, URL formats, source lookup, and issue-label compatibility.

*The project is under active development. Feature availability and research results should be verified against the running application.*

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web application |
| Folium | Interactive mapping |
| streamlit-folium | Streamlit map integration |
| TinyFish | AI-assisted web research |
| python-dotenv | Environment variable management |
| pytest | Automated testing |

## 📁 Project Structure

```text
CivicLens-Delhi/
│
├── app.py
├── civic_sources.py
├── map_view.py
├── GIS_SOURCE_NOTES.md
├── README.md
├── requirements.txt
│
├── tests/
│   └── test_civic_sources.py
│
├── .env
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the Repository

**GitHub Repository:**  
https://github.com/diyaakhampaaa/CivicLens-Delhi

```bash
git clone https://github.com/diyaakhampaaa/CivicLens-Delhi.git
cd CivicLens-Delhi
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
TINYFISH_API_KEY=your_actual_api_key_here
```

Replace the placeholder with your own TinyFish API key.

**Important:** Never commit your `.env` file or expose API keys in public repositories. Ensure `.env` is included in `.gitignore`.

### 5. Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to access CivicLens Delhi.

## 🧪 Running Tests

Run the civic-source test suite using:

```bash
python -m pytest tests/test_civic_sources.py -v
```

The tests cover civic-source records, URL formats, source lookup, and issue-label compatibility.

## 🏛️ Civic Data and Official Sources

CivicLens references the following official platforms as starting points for civic information and research:

- **Municipal Corporation of Delhi (MCD):** https://mcdonline.nic.in/
- **New Delhi Municipal Council (NDMC):** https://www.ndmc.gov.in/
- **Delhi Public Grievance Monitoring System (PGMS):** https://pgms.delhi.gov.in/

These references are starting points for investigation. They do not automatically establish which authority is responsible for a particular location or issue.

## 🔎 How TinyFish Fits In

TinyFish supports the web-research component of CivicLens.

The intended workflow is to:
1. Identify the civic issue and selected location.
2. Research relevant government websites and reporting information.
3. Retrieve useful information and source references.
4. Present findings so users can inspect and verify the original sources.

AI-assisted findings should not be treated as authoritative government instructions without checking the original source.

## ⚠️ Limitations

- CivicLens is an informational prototype, not an official government service.
- Map coordinates represent approximate locality reference points.
- Selecting a map location does not establish municipal jurisdiction.
- The map does not necessarily represent verified administrative boundaries.
- The application does not guarantee that a particular authority is responsible for an issue.
- Web-researched information may be incomplete or outdated.
