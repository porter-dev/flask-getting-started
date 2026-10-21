from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(message="Flask is running on Porter")


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")
