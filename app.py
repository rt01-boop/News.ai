import os
import time
import random
import requests
import feedparser
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(name)
CORS(app)

RSS_URL="https://news.google.com/rss/search?q=gurgaon+india+finance+world&hl=en-IN&gl=IN&ceid=IN:en"

articles=[]
seen=set()

MAX_ARTICLES=1000

-------------------------

FALLBACK ENGINE

-------------------------

def fallback_generate(title):

sentences=[
    f"{title} is attracting attention as new developments emerge.",
    f"Experts say the situation may influence future economic or social trends.",
    f"Observers are closely monitoring how the situation evolves.",
    f"The event highlights broader changes taking place in society.",
    f"More updates are expected as the story develops."
]

article=" ".join(random.sample(sentences,4))

return {
    "summary":article[:180],
    "article":article,
    "vocabulary":[
        {"word":"development","meaning":"important event"},
        {"word":"observer","meaning":"person watching closely"},
        {"word":"analysis","meaning":"study of a situation"}
    ]
}

-------------------------

PHONE WORKERS

-------------------------

def phone_worker_1(title):

try:

    url="http://192.168.1.10:5000/rewrite"

    r=requests.post(url,json={"title":title},timeout=5)

    return r.json()

except:
    raise Exception()

def phone_worker_2(title):

try:

    url="http://192.168.1.11:5000/rewrite"

    r=requests.post(url,json={"title":title},timeout=5)

    return r.json()

except:
    raise Exception()

def phone_worker_3(title):

try:

    url="http://192.168.1.12:5000/rewrite"

    r=requests.post(url,json={"title":title},timeout=5)

    return r.json()

except:
    raise Exception()

-------------------------

AI PROVIDERS

-------------------------

def groq_generate(title):
raise Exception()

def openrouter_generate(title):
raise Exception()

def hf_generate(title):
raise Exception()

def together_generate(title):
raise Exception()

def deepinfra_generate(title):
raise Exception()

def fireworks_generate(title):
raise Exception()

def replicate_generate(title):
raise Exception()

def cohere_generate(title):
raise Exception()

def perplexity_generate(title):
raise Exception()

-------------------------

AI ROUTER

-------------------------

def ai_router(title):

providers=[
    phone_worker_1,
    phone_worker_2,
    phone_worker_3,
    groq_generate,
    openrouter_generate,
    hf_generate,
    together_generate,
    deepinfra_generate,
    fireworks_generate,
    replicate_generate,
    cohere_generate,
    perplexity_generate
]

for provider in providers:

    try:

        result=provider(title)

        if result:

            print("Used:",provider.__name__)

            return result

    except:

        print("Failed:",provider.__name__)

return fallback_generate(title)

-------------------------

SCRAPER

-------------------------

def update_news():

global articles

feed=feedparser.parse(RSS_URL)

for entry in feed.entries:

    title=entry.title

    if title in seen:
        continue

    seen.add(title)

    ai=ai_router(title)

    article={
        "title":title,
        "source":entry.source.title if "source" in entry else "Google News",
        "link":entry.link,
        "summary":ai["summary"],
        "article":ai["article"],
        "vocabulary":ai["vocabulary"],
        "time":time.time()
    }

    articles.insert(0,article)

    if len(articles)>=MAX_ARTICLES:
        articles=[]

-------------------------

API

-------------------------

@app.route("/news")
def news():

update_news()

return jsonify(articles)

@app.route("/")
def home():

return "PulseGurgaon backend running"

-------------------------

RUN

-------------------------

if name=="main":

app.run(host="0.0.0.0",port=10000)