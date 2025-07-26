"""
Simple Flask backend for the ClearStep demo.

Exposes two endpoints:

  * /verify (GET): returns stubbed account details.
  * /chat   (POST): proxies messages to OpenAI’s ChatCompletion.

"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)

# Grab your key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/verify", methods=["GET"])
def verify():
    # Stub account info for local testing
    return jsonify({
        "account": "demo_user",
        "status": "active"
    })

@app.route("/chat", methods=["POST"])
def chat():
    payload = request.get_json()
    user_msg = payload.get("message", "")
    # Forward to OpenAI
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_msg}]
    )
    assistant_reply = resp.choices[0].message.content
    return jsonify({"reply": assistant_reply})

if __name__ == "__main__":
    # Run on port 5000 by default
    app.run(host="0.0.0.0", port=5000, debug=True)
