from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(name)
CORS(app)

DATA_FILE = "articles.json"

def load_articles():
if not os.path.exists(DATA_FILE):
with open(DATA_FILE, "w") as f:
json.dump([], f)

with open(DATA_FILE, "r") as f:
    data = json.load(f)

if len(data) == 0:
    default_article = {
        "title": "PulseGurgaon Launches",
        "summary": "Welcome to PulseGurgaon. Your AI powered news platform.",
        "article": "PulseGurgaon has launched successfully. Soon this system will automatically generate and publish news articles.",
        "time": datetime.now().strftime("%Y-%m-%d"),
        "source": "PulseGurgaon"
    }

    data.append(default_article)
    save_articles(data)

return data

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

body = request.json

new_article = {
    "title": body.get("title"),
    "summary": body.get("summary"),
    "article": body.get("article"),
    "time": datetime.now().strftime("%Y-%m-%d"),
    "source": "PulseGurgaon"
}

articles = load_articles()
articles.insert(0, new_article)

save_articles(articles)

return jsonify({"status": "article added"})

@app.route("/generate")
def generate_ai_article():

generated = {
    "title": "AI Generated Gurgaon Update",
    "summary": "This article was generated automatically by PulseGurgaon AI.",
    "article": "PulseGurgaon is testing automated AI journalism where news is generated using multiple AI systems.",
    "time": datetime.now().strftime("%Y-%m-%d"),
    "source": "PulseGurgaon AI"
}

articles = load_articles()
articles.insert(0, generated)

save_articles(articles)

return jsonify(generated)

if name == "main":
app.run(host="0.0.0.0", port=10000)