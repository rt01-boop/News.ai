from fastapi import FastAPI
import feedparser
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

articles = []

RSS_FEEDS = [
"https://news.google.com/rss/search?q=gurgaon",
"https://news.google.com/rss/search?q=haryana",
"https://news.google.com/rss/search?q=stock+market+india",
"https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
]


def scrape_news():

    global articles
    new_articles = []

    for url in RSS_FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            new_articles.append({
                "title": entry.title,
                "link": entry.link
            })

    articles = new_articles
    print("News updated")


@app.get("/")
def home():
    return {"message": "PulseGurgaon running"}


@app.get("/news")
def get_news():
    return articles


scheduler = BackgroundScheduler()
scheduler.add_job(scrape_news, "interval", minutes=2)
scheduler.start()

scrape_news()