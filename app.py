
import os

from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
app.logger.setLevel("INFO")

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

client = genai.Client(api_key=api_key) if api_key else None


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


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
            "error": "Gemini API key is missing. Check your .env file."
        }), 503

    instructions = """
    You are a health information assistant for a student project.
    Provide general educational information, not diagnoses.
    Do not prescribe medicines or doses.
    For severe or sudden symptoms, advise urgent professional care.
    For possible emergencies in India, advise calling 112.
    Keep answers clear and concise.
    """

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=(
                instructions
                + "\n\nUser's health question:\n"
                + message
            ),
            config={
                "max_output_tokens": 800,
            },
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

    except Exception:
        app.logger.exception("Gemini API request failed")
        return jsonify({
            "error": "AI service unavailable. Please try again."
        }), 500


if __name__ == "__main__":
    print("Starting HealthAssistant on port 5000", flush=True)
    print("Gemini API key configured:", bool(api_key), flush=True)
    print("Configured model:", model_name, flush=True)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=False,
    )