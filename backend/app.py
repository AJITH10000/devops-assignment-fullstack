from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/api/message")
def message():
    return jsonify({"message": "Hello from backend!"})

