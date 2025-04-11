from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import requests
import os


app = Flask(__name__)
CORS(app)  # Allow frontend on localhost
RENDER_SERVICE_ID = "srv-cvsaemi4d50c738brhl0?key=kryATbBGq0g"
RENDER_API_KEY = "rnd_LHnAdPjlVhRpFYaKsdWt5L6QthHc"

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

@app.route("/rewrite", methods=["POST"])
def rewrite_for_client():
    data = request.get_json()
    message = data.get("message", "")
    @app.route('/trigger-deploy', methods=['POST'])
def trigger_deploy():
    url = f"https://api.render.com/v1/services/{RENDER_SERVICE_ID}/deploys"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {RENDER_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json={})
    return jsonify(response.json()), response.status_code


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
