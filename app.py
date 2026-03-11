# redeploy trigger
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


@app.route("/")
def home():
    return "PulseGurgaon backend running"


@app.route("/news")
def get_news():
    articles = load_articles()
    return jsonify(articles)


@app.route("/add", methods=["POST"])
def add_article():
    data = request.json

    article = {
        "title": data.get("title"),
        "source": data.get("source"),
        "time": data.get("time"),
        "summary": data.get("summary"),
        "article": data.get("article"),
        "vocabulary": data.get("vocabulary", [])
    }

    articles = load_articles()
    articles.insert(0, article)
    save_articles(articles)

    return {"status": "success"}
@app.route("/test")
def test_article():

    article = {
        "title": "PulseGurgaon Test Article",
        "source": "PulseGurgaon",
        "time": "2026-03-11",
        "summary": "This is a backend test article.",
        "article": "If you can see this article through the API, the storage system works perfectly.",
        "vocabulary": []
    }

    articles = load_articles()
    articles.insert(0, article)
    save_articles(articles)

    return "Test article added"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)