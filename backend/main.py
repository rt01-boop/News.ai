from flask import Flask, jsonify
from flask_cors import CORS
import feedparser

app = Flask(name)

Allow frontend (GitHub pages) to access backend

CORS(app)

@app.route("/")
def home():
return "PulseGurgaon backend running"

@app.route("/news")
def news():

feed = feedparser.parse("https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en")

articles = []

for entry in feed.entries[:50]:
    articles.append({
        "title": entry.title,
        "link": entry.link,
        "source": entry.source.title if "source" in entry else "Google News"
    })

return jsonify(articles)

if name == "main":
app.run(host="0.0.0.0", port=10000)