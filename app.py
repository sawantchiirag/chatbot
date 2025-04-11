from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

@app.route("/rewrite", methods=["POST"])
def rewrite_message():
    data = request.get_json()
    message = data.get("message", "")

    prompt = (
        f"Rewrite the following message for a client in a polite, professional, and grammatically correct way. "
        f"Ensure the tone is soft and appropriate for chat support:\n\n"
        f"Original Message: \"{message}\"\n\nRewritten:"
    )

    response = openai.ChatCompletion.create(
        model="gryphe/mythomax-l2-13b",
        messages=[
            {"role": "system", "content": "You are a professional assistant for rewriting messages for client support."},
            {"role": "user", "content": prompt}
        ]
    )

    rewritten = response['choices'][0]['message']['content'].strip()
    return jsonify({"rewritten": rewritten})
