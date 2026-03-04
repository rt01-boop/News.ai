from fastapi import FastAPI
import feedparser
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

# storage for articles
articles = []

# RSS feeds we will scrape
RSS_FEEDS = [
    "https://news.google.com/rss/search?q=gurgaon",
    "https://news.google.com/rss/search?q=haryana",
    "https://news.google.com/rss/search?q=stock+market+india",
    "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
]

def scrape_news():
    global articles

    collected = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            collected.append({
                "title": entry.title,
                "link": entry.link
            })

    articles = collected
    print("News updated")

@app.get("/")
def home():
    return {"message": "PulseGurgaon backend running"}

@app.get("/news")
def get_news():
    return articles


# scheduler that runs every 2 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(scrape_news, "interval", minutes=2)
scheduler.start()

# run once when server starts
scrape_news()