import os
import time
import random
import requests
import feedparser
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(name)
CORS(app)

RSS_URL = "https://news.google.com/rss/search?q=gurgaon+india+finance+world&hl=en-IN&gl=IN&ceid=IN:en"

articles = []
seen_titles = set()

MAX_ARTICLES = 1000

def fallback_generate(title):

sentences = [
    f"{title} has recently attracted attention as new developments emerge.",
    f"Experts say the situation could influence economic or social trends.",
    f"Observers are closely watching how events unfold in the coming days.",
    f"The topic highlights broader changes currently happening.",
    f"More updates are expected as additional information becomes available."
]

article_text = " ".join(random.sample(sentences,4))

return {
    "summary": article_text[:160],
    "article": article_text,
    "vocabulary":[
        {"word":"development","meaning":"important event"},
        {"word":"observer","meaning":"person watching carefully"},
        {"word":"trend","meaning":"general direction of change"}
    ]
}

def ai_router(title):

try:
    return fallback_generate(title)
except:
    return fallback_generate(title)

def update_news():

global articles

feed = feedparser.parse(RSS_URL)

for entry in feed.entries:

    title = entry.title

    if title in seen_titles:
        continue

    seen_titles.add(title)

    ai = ai_router(title)

    article = {
        "title": title,
        "source": entry.source.title if "source" in entry else "Google News",
        "link": entry.link,
        "summary": ai["summary"],
        "article": ai["article"],
        "vocabulary": ai["vocabulary"],
        "time": int(time.time()*1000)
    }

    articles.insert(0,article)

    if len(articles) > MAX_ARTICLES:
        articles = articles[:MAX_ARTICLES]

@app.route("/news")
def news():

update_news()

return jsonify(articles)

@app.route("/")
def home():

return "PulseGurgaon backend running"

if name == "main":

port = int(os.environ.get("PORT", 10000))

app.run(host="0.0.0.0", port=port)