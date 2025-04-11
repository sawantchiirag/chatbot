from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Allow frontend on localhost

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

@app.route("/rewrite", methods=["POST"])
def rewrite_for_client():
    data = request.get_json()
    message = data.get("message", "")

prompt = (
    f"Please correct the grammar, punctuation, and spelling of the following sentence. "
    f"Do not change the tone or add any extra words. Just return the corrected version:\n\n"
    f"\"{message}\""
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

if __name__ == "__main__":
    app.run()
