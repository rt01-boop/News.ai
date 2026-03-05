from flask import Flask, jsonify
from flask_cors import CORS
import feedparser

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "PulseGurgaon backend running"

@app.route("/news")
def get_news():

    url = "https://news.google.com/rss/search?q=gurgaon+india+finance&hl=en-IN&gl=IN&ceid=IN:en"

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries:

        articles.append({
            "title": entry.title,
            "source": entry.source.title if "source" in entry else "Google News",
            "link": entry.link
        })

    return jsonify(articles)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)