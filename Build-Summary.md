# Smart Health Navigator

Hack Front India 2026 - Cohort Activity Document

* Team Name: HACK6KSB

* Team Members: Navdeep Beniwal, Tamanna Saini, Jenny Oinam, Vanshika

* Project repository: https://github.com/jennyo08/smart-health-navigator

* Live prototype: https://smart-health-navigator-crlw.onrender.com/

* Theme: Open Source & Innovation

* Project type: Web prototype using Flask, HTML/CSS/JavaScript, and the Gemini API.

## Project Overview
Smart Health Navigator is a student-built web prototype intended to help users understand general health information and navigate possible next steps when they have questions about symptoms. It is designed for health education and navigation, not diagnosis, emergency triage replacement, or prescribing medicines. Users should consult qualified healthcare professionals for personal medical advice.

## Problem Statement
People may search online for symptoms and encounter confusing, unreliable, or alarming information. A simple, accessible health-information interface can help users learn general information, understand when professional care may be appropriate, and find safer next steps. This prototype explores that idea through a web interface and an AI-powered conversational endpoint.

## Target Users and Need
Initial target users are students and general users who want understandable, non-diagnostic health education. The key need is clear, responsible information in simple language, with appropriate reminders to seek professional or emergency care when needed. This is an initial hypothesis; user interviews and testing are still needed to validate demand and usability.

## Solution and Main Flow
Smart Health Navigator is a web-based prototype that lets users submit general health questions and receive AI-generated educational information.
1. User opens the Smart Health Navigator website.
2. User types a general health question in the chat interface.
3. The frontend sends the question to the Flask /api/chat endpoint.
4. The backend calls the configured Gemini model and returns a text response.
5. The interface displays the response; users are reminded that it is educational information, not a diagnosis.
The prototype is intended to make general health information easier to explore. It deliberately does not diagnose medical conditions, prescribe medication, replace qualified healthcare professionals, or guarantee the accuracy of its answers. Its usefulness also depends on the availability of the external AI service.

## Technology Stack
* Frontend: HTML, CSS, and JavaScript
Used to create a straightforward interface for entering questions and displaying responses.
* Backend: Python with Flask
Handles requests, validates input, communicates with the AI service, and returns responses.
* AI integration: Google Gemini API via the Google GenAI SDK
Generates conversational responses to health-related questions.
* Deployment: Render
Makes the prototype publicly accessible.
* Source control: GitHub
Stores the project source code and supports tracking and sharing changes.
* Configuration: Environment variables
Keeps the API key separate from the application source code.

## How to Run Locally
1. Install a supported Python version.
2. Install packages with: pip install -r requirements.txt
3. Set GEMINI_API_KEY and GEMINI_MODEL as environment variables (or use a local .env file that is excluded from Git).
4. Start the Flask app using the repository's documented run command.
5. Open the local address printed by Flask in a browser.

## Evidence
The prototype has been deployed publicly. In a stranger test involving two people unfamiliar with the website, navigation was straightforward, with no noticeable difficulty using the simple interface. During testing, however, the Gemini service returned a 503 UNAVAILABLE high-demand error, preventing a complete assessment of the chatbot's response experience.

What remains unproven: The intended users' level of need, willingness to use the tool, trust in its responses, and preference for it over Google Search or existing health websites have not been established through completed user interviews. The prototype's effect on users' understanding or healthcare decisions has not been measured. Input validation, medical response quality, and safety behaviour also require further runtime testing.

Therefore, the project demonstrates a working prototype concept, not validated product-market fit or proven health outcomes.

## What I Would Build Next

I would expand Smart Health Navigator with features that help users move from understanding health information to finding reliable resources and taking appropriate next steps.

- **Nearby health facilities:** Allow users to find nearby hospitals, clinics, and pharmacies based on their city or town, with directions and clear guidance for contacting emergency services when necessary.
- **First-aid guidance:** Provide simple, safety-reviewed first-aid instructions for common situations, with clear warnings about when immediate professional help is needed.
- **Disease trend visualisations:** Display graphs showing changes in disease incidence or reported cases over time, using reliable and up-to-date public health data.
- **Health news section:** Share recent health-related news and public health announcements from credible sources, with dates and links to the original reports.

Before building these features, I would first gather feedback from intended users to understand which would be most useful. I would prioritise features based on demonstrated user needs, the reliability of available data, and the ability to provide information safely. In particular, facility listings would need accurate location data, while first-aid guidance and disease trends would require trustworthy sources and regular verification.


