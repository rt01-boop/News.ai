from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(name)
CORS(app)

DATA_FILE = "articles.json"

def load_articles():
# create file if missing
if not os.path.exists(DATA_FILE):
with open(DATA_FILE, "w") as f:
json.dump([], f)

# read file
with open(DATA_FILE, "r") as f:
    articles = json.load(f)

# ensure at least one article exists
if len(articles) == 0:
    default_article = {
        "title": "PulseGurgaon Launches",
        "summary": "Welcome to PulseGurgaon, an AI powered news platform.",
        "article": "PulseGurgaon has launched successfully and will soon auto publish AI generated news.",
        "time": datetime.now().strftime("%Y-%m-%d"),
        "source": "PulseGurgaon"
    }

    articles.append(default_article)

    with open(DATA_FILE, "w") as f:
        json.dump(articles, f, indent=2)

return articles

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

@app.route("/generate")
def generate_article():

article = {
    "title": "AI Generated Gurgaon Update",
    "summary": "This article was generated automatically by PulseGurgaon AI.",
    "article": "PulseGurgaon is testing automated AI journalism. Soon multiple AI systems will generate news articles automatically.",
    "time": datetime.now().strftime("%Y-%m-%d"),
    "source": "PulseGurgaon AI"
}

articles = load_articles()
articles.insert(0, article)

save_articles(articles)

return jsonify(article)

@app.route("/add", methods=["POST"])
def add_article():

data = request.json

article = {
    "title": data.get("title"),
    "summary": data.get("summary"),
    "article": data.get("article"),
    "time": datetime.now().strftime("%Y-%m-%d"),
    "source": "PulseGurgaon"
}

articles = load_articles()
articles.insert(0, article)

save_articles(articles)

return jsonify({"status": "added"})

if name == "main":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)