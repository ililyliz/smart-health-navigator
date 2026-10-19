# Smart Health Navigator

Smart Health Navigator is a web-based health information assistant built to make general health and wellness information easier to understand. Users can enter questions through a simple chat interface and receive AI-generated educational responses.

**Live Demo:** https://smart-health-navigator-crlw.onrender.com

## Problem Statement

Finding understandable health information online can be difficult. Smart Health Navigator provides a simple starting point for exploring general health topics and preparing questions to discuss with a qualified healthcare professional.

## What It Does

- Provides a responsive website with a health-focused interface.
- Accepts health and wellness questions through a chat interface.
- Uses the Google Gemini API to generate educational responses.
- Displays AI responses directly on the website.
- Includes safety notices explaining the limitations of AI-generated health information.

### Main User Flow

1. The user opens the website.
2. The user enters a general health or wellness question.
3. The Flask backend sends the question to the Gemini API.
4. The generated response is returned and displayed in the chat interface.

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python and Flask
- **AI integration:** Google Gemini API using the `google-genai` Python SDK
- **Deployment:** Render
- **Version control:** Git and GitHub

## Project Structure

```text
prototype/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── PROJECT_SPEC.md
└── templates/
    └── index.html
```

## Prerequisites

Before running the project, install:

- Python 3.10 or a compatible version supported by your dependencies
- pip
- A Google Gemini API key

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/jennyo08/smart-health-navigator/
cd main
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

If you use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local file named `.env` in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.8-flash
```



**Security:** Never commit your `.env` file or expose your API key in frontend JavaScript, screenshots, public logs, or source code.

### 5. Start the application

```bash
python app.py
```

Open the local address shown by Flask, typically:

`http://127.0.0.1:5000`

## Deployment

The application can be hosted on Render as a Python web service connected to a GitHub repository.

Typical Render settings:

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`

Configure the following environment variables in Render's service settings:

- `GEMINI_API_KEY` — your private Gemini API key
- `GEMINI_MODEL` — the supported Gemini model you intend to use

After pushing changes to GitHub, Render can deploy the latest commit automatically if automatic deployments are enabled. Otherwise, deploy manually from the Render dashboard.

## Current Limitations and Known Issues

- Responses depend on the availability and limits of the Google Gemini API.
- Gemini may return temporary errors, including `503 UNAVAILABLE`, when a model is experiencing high demand.
- The application cannot guarantee that AI-generated information is complete, accurate, or appropriate for every situation.
- The assistant is intended for general education, not medical diagnosis, treatment decisions, or prescription recommendations.
- The application does not replace a qualified healthcare professional.
- Automated tests, independent clinical validation, and comprehensive real-user testing should not be considered completed unless they have actually been performed.

If the AI service is unavailable, users may not receive a response. A successful website deployment does not guarantee that the external AI service will always work.

## Safety and Responsible Use

- Do not enter personal identifying information or confidential medical records.
- Verify important health information with reliable sources and qualified professionals.
- For a potentially life-threatening emergency, contact local emergency services rather than waiting for an AI response. In India, the emergency number is **112**.

## Future Improvements

- Add reliable retry handling and clearer error messages for temporary API failures.
- Evaluate supported model alternatives and fallback behavior.
- Add automated tests for the chat endpoint and error handling.
- Test usability with people unfamiliar with the project.
- Improve source attribution and verification of health information.

## Project Status

This is a prototype demonstrating a web-based AI health information assistant. Its functionality depends on the backend configuration and availability of the Gemini API. It is not a clinically validated medical product.

