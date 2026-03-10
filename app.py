from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
import requests
from datetime import datetime

app = Flask(name)
CORS(app)

DATA_FILE = "articles.json"

---------------------------

JSON STORAGE

---------------------------

def load_articles():
if not os.path.exists(DATA_FILE):
return []

with open(DATA_FILE, "r") as f:
    return json.load(f)

def save_articles(data):
with open(DATA_FILE, "w") as f:
json.dump(data, f, indent=2)

---------------------------

PHONE AI WORKERS

---------------------------

PHONE_WORKERS = [
"http://phone1:5001/rewrite",
"http://phone2:5001/rewrite",
"http://phone3:5001/rewrite"
]

def try_phone_ai(text):

for worker in PHONE_WORKERS:

    try:
        r = requests.post(worker, json={"text": text}, timeout=10)

        if r.status_code == 200:
            return r.json()["rewrite"]

    except:
        pass

return None

---------------------------

CLOUD AI PLACEHOLDERS

---------------------------

def try_cloud_ai(text):

providers = [
    "groq",
    "openrouter",
    "huggingface",
    "together",
    "deepinfra",
    "fireworks",
    "replicate",
    "cohere",
    "perplexity"
]

for p in providers:

    try:
        # placeholder call
        return f"AI rewrite by {p}: {text}"

    except:
        pass

return None

---------------------------

FALLBACK ENGINE

---------------------------

def fallback_rewrite(text):

words = text.split()

if len(words) > 80:
    words = words[:80]

return " ".join(words) + "..."

---------------------------

MAIN REWRITE ENGINE

---------------------------

def rewrite_article(text):

phone = try_phone_ai(text)

if phone:
    return phone

cloud = try_cloud_ai(text)

if cloud:
    return cloud

return fallback_rewrite(text)

---------------------------

ADD ARTICLE

---------------------------

@app.route("/add", methods=["POST"])
def add_article():

data = request.json

text = data.get("text")

rewritten = rewrite_article(text)

article = {
    "title": data.get("title"),
    "source": data.get("source"),
    "time": datetime.now().isoformat(),
    "summary": rewritten[:120],
    "article": rewritten,
    "vocabulary": []
}

articles = load_articles()

articles.insert(0, article)

save_articles(articles)

return jsonify({"status": "saved"})

---------------------------

GET NEWS

---------------------------

@app.route("/news")
def get_news():

return jsonify(load_articles())

---------------------------

HOME

---------------------------

@app.route("/")
def home():

return "PulseGurgaon AI backend running"

---------------------------

SERVER START

---------------------------

if name == "main":

port = int(os.environ.get("PORT", 10000))

app.run(host="0.0.0.0", port=port)