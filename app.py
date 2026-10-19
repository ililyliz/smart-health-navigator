import os
import time

from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
app.logger.setLevel("INFO")

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
fallback_model_name = os.getenv("GEMINI_FALLBACK_MODEL")

client = genai.Client(api_key=api_key) if api_key else None


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


def generate_with_retries(model, contents, config, attempts=3):
    """Retry temporary Gemini service/rate-limit failures with short backoff."""
    for attempt in range(attempts):
        try:
            return client.models.generate_content(
                model=model,
                contents=contents,
                config=config,
            )
        except Exception as exc:
            # The Google SDK may expose status_code or code depending on error type.
            status_code = (
                getattr(exc, "status_code", None)
                or getattr(exc, "code", None)
            )
            message = str(exc).lower()
            transient = (
                status_code in (429, 500, 502, 503, 504)
                or "503 unavailable" in message
                or "high demand" in message
                or "429" in message
                or "resource_exhausted" in message
            )

            if not transient or attempt == attempts - 1:
                raise

            delay = 1 * (2 ** attempt)
            app.logger.warning(
                "Temporary Gemini error for model %s; retrying in %s second(s) (attempt %s/%s).",
                model, delay, attempt + 1, attempts
            )
            time.sleep(delay)


@app.route("/api/chat", methods=["POST"])
def chat():
    app.logger.info("Request received at /api/chat")

    data = request.get_json(silent=True) or {}
    message = data.get("question", data.get("message", ""))

    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Please enter a question."}), 400

    message = message.strip()

    if len(message) > 2000:
        return jsonify({
            "error": "Keep your message under 2,000 characters."
        }), 400

    if client is None:
        return jsonify({
            "error": "The AI service is not configured. Please contact the site owner."
        }), 503

    instructions = """
    You are a health information assistant for a student project.
    Provide general educational information, not diagnoses.
    Do not prescribe medicines or doses.
    For severe or sudden symptoms, advise urgent professional care.
    For possible emergencies in India, advise calling 112.
    Keep answers clear and concise.
    """

    contents = instructions + "\n\nUser's health question:\n" + message
    config = {"max_output_tokens": 800}


    try:
        try:
            response = generate_with_retries(
                model_name, contents, config, attempts=3
            )
        except Exception as primary_exc:
            error_text = str(primary_exc).lower()

            # Only try the fallback for likely temporary failures.
            transient_error = any(term in error_text for term in (
                "503", "unavailable", "high demand",
                "429", "resource_exhausted", "quota",
                "500", "502", "504", "timeout"
            ))

            if (
                not transient_error
                or not fallback_model_name
                or fallback_model_name == model_name
            ):
                raise

            app.logger.warning(
                "Primary Gemini model failed temporarily; trying configured fallback."
            )

            response = generate_with_retries(
                fallback_model_name, contents, config, attempts=2
            )

        reply = (response.text or "").strip()

        if response.candidates:
            app.logger.info(
                "Gemini finish reason: %s",
                response.candidates[0].finish_reason
            )

        app.logger.info("Gemini reply length: %s", len(reply))

        if not reply:
            app.logger.warning("Gemini returned an empty response.")
            return jsonify({
                "error": "The assistant returned no answer. Please try again."
            }), 502

        return jsonify({"reply": reply})

    except Exception as exc:
        app.logger.exception("Gemini API request failed")

        error_text = str(exc).lower()

        if (
            "503" in error_text
            or "unavailable" in error_text
            or "high demand" in error_text
        ):
            user_message = (
                "The AI service is temporarily busy. "
                "Please try again in a little while."
            )
            status = 503

        elif (
            "429" in error_text
            or "resource_exhausted" in error_text
            or "quota" in error_text
        ):
            user_message = (
                "The AI service has reached a usage limit. "
                "Please try again later."
            )
            status = 429

        elif "timeout" in error_text:
            user_message = (
                "The AI service took too long to respond. "
                "Please try again."
            )
            status = 504

        else:
            user_message = (
                "The AI service could not answer right now. "
                "Please try again shortly."
            )
            status = 502

        return jsonify({"error": user_message}), status



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("Starting HealthAssistant on port", port, flush=True)
    print("Gemini API key configured:", bool(api_key), flush=True)
    print("Configured model:", model_name, flush=True)

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False,
    )
