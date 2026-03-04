from fastapi import FastAPI
import feedparser

app = FastAPI()

RSS_FEEDS = [
"https://news.google.com/rss/search?q=gurgaon",
"https://news.google.com/rss/search?q=haryana",
"https://news.google.com/rss/search?q=stock+market+india",
"https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
]

@app.get("/")
def home():
    return {"message": "PulseGurgaon API running"}

@app.get("/news")
def get_news():
    articles = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            articles.append({
                "title": entry.title,
                "link": entry.link
            })

    return articles