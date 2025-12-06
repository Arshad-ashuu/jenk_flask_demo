# app.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "Hello from Flask + Jenkins!"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    # For local dev only. In Docker we'll use gunicorn.
    app.run(host="0.0.0.0", port=5000, debug=True)
