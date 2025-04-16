from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"  # Replace with your actual API key
MODEL = "google/gemma-3-1b-it:free"  # Your chosen model

@app.route('/rewrite-message', methods=['POST'])
def rewrite_message():
    input_message = request.json.get('message')
    prompt = f"Rewrite this for chat support in simple, short, and professional English, with no grammar mistakes:\n\n'{input_message}'"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        data = response.json()
        return jsonify({"rewrittenMessage": data["choices"][0]["message"]["content"]})
    except Exception as e:
        return jsonify({"error": "Something went wrong."}), 500

if __name__ == '__main__':
    app.run(debug=True)
