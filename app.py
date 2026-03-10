from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "articles.json"


def load_articles():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_articles(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def fallback_rewrite(text):
    return text


@app.route("/")
def home():
    return "PulseGurgaon AI backend running"


@app.route("/news")
def news():
    return jsonify(load_articles())


@app.route("/add", methods=["POST"])
def add():
    data = request.json

    article = {
        "title": data.get("title"),
        "source": data.get("source"),
        "time": data.get("time"),
        "summary": data.get("text"),
        "article": fallback_rewrite(data.get("text")),
        "vocabulary": []
    }

    articles = load_articles()
    articles.insert(0, article)
    save_articles(articles)

    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)