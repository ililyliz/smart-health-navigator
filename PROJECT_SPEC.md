# Smart Health Navigator — Project Specification

## 1. What is this?

Smart Health Navigator is a web-based prototype that provides AI-generated educational explanations in response to general health-information questions. It aims to help users understand information and consider appropriate next steps without replacing qualified healthcare professionals.

## 2. Who uses it?

The intended users are college students and young adults, approximately 18–30 years old, who have limited healthcare knowledge and want help understanding unfamiliar health information. The intended audience is a hypothesis that still needs to be validated through user research.

## 3. What must it do?

1. Allow users to enter a general health-information question through the website.
2. Reject empty or whitespace-only questions with a clear error message.
3. Reject inputs longer than 2,000 characters with a clear error message.
4. Send accepted questions to the configured Gemini API through the Flask backend.
5. Display the generated response in a readable format.
6. Display a clear message when the AI service is unavailable or returns no usable answer.
7. Provide general educational information rather than a diagnosis.
8. Avoid prescribing medicines or dosages.
9. Encourage urgent professional care for severe or sudden symptoms and advise users in possible emergencies in India to call 112.
10. Make the limitations of AI-generated health information clear.

## 4. What does it not do?

- It does not diagnose diseases or determine what condition a user has.
- It does not prescribe medicines, dosages, or personalised treatment plans.
- It does not replace a doctor, emergency service, or qualified healthcare professional.
- It does not guarantee that AI-generated information is accurate or complete.
- It does not provide reliable emergency triage. Users must not delay emergency care to use the chatbot.
- It does not provide accounts, login, profiles, saved chat history, appointment booking, medical-record integration, or payments.
- It does not intentionally require users to provide personal identifiers.
- It does not claim to improve health outcomes without supporting evidence.
- It does not expand into a general-purpose chatbot or add extra features during this build.

## 5. What data does it use?

- **Input:** The text question entered by the user.
- **Processing:** Flask receives the question and sends it, together with health-safety instructions, to the configured Gemini model through the Google GenAI SDK.
- **Output:** An AI-generated educational response or a clear error message.
- **Storage:** The current backend does not configure a database for persistent chat history.
- **Sensitive information:** Health questions may contain sensitive personal information. Users should be advised not to enter names, addresses, or unnecessary personal medical details.
- **External processing:** Questions are sent to Google's AI service. The app should not imply that user inputs remain exclusively on the local website.
- **Secrets:** API keys and model configuration must be stored in environment variables and must not be committed to GitHub or exposed in frontend code.

## 6. What are the constraints?

- The project already uses HTML, CSS, and JavaScript for the frontend, Flask for the backend, and the Gemini API for AI-generated responses.
- The website is deployed on Render, and the source code is maintained on GitHub.
- The build should improve the existing project rather than replace it.
- The scope is limited to one question-to-answer flow.
- Gemini may experience temporary service outages, model availability issues, or usage limits.
- The backend must validate input and handle service errors.
- The build should use existing tools and avoid assuming a paid service or new infrastructure.
- Testing must not depend on the chatbot for real medical decisions or use actual emergencies as test cases.

## 7. What does done mean?

The flow is considered ready for review when:

1. A user can submit a valid general health question and receive a readable answer when the AI service is available.
2. Empty input and input longer than 2,000 characters are rejected clearly.
3. An unsupported input is handled appropriately and does not cause the app to misrepresent its purpose.
4. AI service failures produce a clear message rather than a confusing technical error.
5. The API key is not exposed in frontend code or committed to the repository.
6. The deployed website and backend communicate correctly.
7. Empty-input, long-input, and unsupported-input tests have been performed and recorded.
8. Two people unfamiliar with the project have attempted the assigned task without guidance, and their actual observations have been documented.
9. Changes made after testing have been recorded.
10. Remaining limitations are documented honestly.

## 8. What is still unknown?

- Whether the intended users experience this problem frequently enough to need a separate tool.
- Whether users understand the answers and their limitations.
- Whether the chatbot provides more value than Google Search or trusted health websites.
- Whether the AI consistently handles unsupported questions and urgent situations safely.
- Whether the configured Gemini model will be reliable enough for regular use.
- Whether first-time users can complete the flow without help.
- Whether the interface communicates clearly that the responses are AI-generated and not medical diagnoses.

## Core User Flow

1. Enter a general, non-emergency health question.
2. Receive an accessible educational explanation.
3. Review the limitations and any appropriate care guidance.
4. Identify a sensible next step, including consulting a qualified healthcare professional when needed.

## Testing Rule

Do not mark a test as passed until it has actually been performed. Record the input, observed behaviour, pass/fail result, and any corrective action.
