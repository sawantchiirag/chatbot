from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS for enabling cross-origin requests
import requests

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# API Key and Model for OpenRouter API
API_KEY = "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"  # Replace with your actual API key
MODEL = "google/gemma-3-1b-it:free"  # Your chosen model

def rewrite_message(message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Adjusted prompt for short and easy responses
    prompt = f"Rewrite this for chat support in simple, short, and professional English, with no grammar mistakes:\n\n'{message}'"

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    try:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print("⚠️ Something went wrong:")
        print("Status Code:", response.status_code)
        print("Response JSON:", response.text)
        return None

# Route for receiving POST request and processing message
@app.route('/rewrite', methods=['POST'])
def rewrite():
    # Get the message from the frontend
    data = request.get_json()
    raw_message = data.get("message", "")

    # Call the rewrite function
    rewritten_message = rewrite_message(raw_message)

    # Return the rewritten message as a JSON response
    if rewritten_message:
        return jsonify({"rewritten_message": rewritten_message}), 200
    else:
        return jsonify({"error": "Failed to rewrite message."}), 500

if __name__ == "__main__":
    # Run the app (Make sure to change host and port if needed)
    app.run(debug=True)
