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

### 1. Clone the repository

```bash
git clone <PUBLIC_GITHUB_REPOSITORY_URL>
cd <REPOSITORY_FOLDER>
```

Replace the placeholders with the actual repository URL and folder name.

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

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
