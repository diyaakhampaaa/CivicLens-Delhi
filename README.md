<<<<<<< HEAD
# CivicLens Delhi 🏙️

**From civic problem to the right complaint channel.**

CivicLens Delhi is an AI-assisted civic information project being developed for Kritical Hacks 2026. It aims to help Delhi residents discover relevant civic complaint channels and understand the next steps for reporting issues such as potholes, damaged roads, garbage accumulation, and broken streetlights.

## 🎯 The Problem

Finding the appropriate authority or official reporting channel for a local civic issue can be confusing. People may not know where to start, what information to prepare, or which source to trust.

## 💡 Our Solution

CivicLens aims to make civic information easier to discover and understand by combining a guided user experience with AI-assisted web research.

## ✨ Planned and In-Progress Features

- **Civic issue guidance:** Explore possible reporting routes for common civic issues.
- **TinyFish integration:** Research relevant web pages to help discover official reporting instructions and sources.
- **Source links:** Help users inspect the sources behind the guidance.
- **Report preparation:** Organize issue details and prepare a complaint draft for the user to review.
- **Delhi locality exploration:** Provide a geographic way to explore relevant civic information.

_Feature status will be updated as each part is implemented and tested._

## 🛠️ Technology

- Python
- Streamlit
- TinyFish
- Additional mapping and data tools as the project develops

## 🚀 Run Locally
=======
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
>>>>>>> 9ca0af13793d4287ad6ce3ca15818e8fc352a5b2

### 1. Clone the repository

```bash
<<<<<<< HEAD
git clone <PUBLIC_GITHUB_REPOSITORY_URL>
cd <REPOSITORY_FOLDER>
```

Replace the placeholders with the actual repository URL and folder name.

### 2. Create and activate a virtual environment
=======
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd civiclens
```

Replace the placeholder with your team's actual repository URL.

### 2. Create a virtual environment
>>>>>>> 9ca0af13793d4287ad6ce3ca15818e8fc352a5b2

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

<<<<<<< HEAD
```powershell
python -m pip install -r requirements.txt
```

### 4. Configure your TinyFish API key

Create a `.env` file in the project root and add:

```dotenv
TINYFISH_API_KEY=your_actual_api_key_here
```

Get your own key through the appropriate TinyFish account or developer portal. Never publish your real API key. The `.env` file should remain excluded by `.gitignore`.

### 5. Start the application

```powershell
python -m streamlit run app.py
```

Follow the local URL printed in the terminal.

## 🔎 How TinyFish Fits In

TinyFish is intended to perform live web research for relevant civic information. The application should present useful findings alongside source links so users can inspect the information themselves.

The integration and its results must be tested against the running application before this README is treated as a description of completed functionality.

## ⚠️ Scope and Limitations

- CivicLens is an informational aid, not a government service.
- Users should verify reporting instructions and jurisdiction with the relevant official authority.
- The application does not submit a complaint or guarantee that an authority will resolve an issue.
- Information may be incomplete or change over time.

## 👥 Team

Built collaboratively for Kritical Hacks 2026.

## 🔮 Future Scope

- Improve locality and jurisdiction guidance.
- Expand verified official-source coverage.
- Improve map usability and accessibility.
- Test the experience with residents and refine it using their feedback.

## 📄 Project Status

This project is under development. Features, screenshots, demo links, and setup instructions will be updated as the implementation is verified.
=======
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
>>>>>>> 9ca0af13793d4287ad6ce3ca15818e8fc352a5b2
