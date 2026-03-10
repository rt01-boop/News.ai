from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(name)
CORS(app)

news = [
{
"title": "Barclays expands India footprint with new office in Gurugram",
"source": "Barclays",
"time": "2026-03-10",
"summary": "Barclays has opened a new office in Gurugram to strengthen its operations in India.",
"article": "Barclays announced the opening of a new office in Gurugram as part of its strategy to expand operations in India. The company said the new office will support technology, operations, and banking services across the region.",
"vocabulary": [
{"word":"footprint","meaning":"business presence"},
{"word":"operations","meaning":"business activities"}
]
},

{
"title": "PwC's 6th Gurgaon office goes live with new finance team",
"source": "PwC",
"time": "2026-03-10",
"summary": "PwC has launched its sixth office in Gurgaon to expand its consulting operations.",
"article": "PwC announced the launch of its sixth office in Gurgaon. The office will support financial consulting and technology advisory services for clients across India.",
"vocabulary": [
{"word":"consulting","meaning":"professional advisory services"},
{"word":"advisory","meaning":"providing guidance"}
]
},

{
"title": "Global markets react to economic slowdown fears",
"source": "Reuters",
"time": "2026-03-10",
"summary": "Stock markets around the world moved cautiously amid concerns of a global slowdown.",
"article": "Investors reacted cautiously today as new economic data suggested a slowdown in global growth. Analysts believe central banks may adjust policies in response.",
"vocabulary": [
{"word":"investors","meaning":"people who invest money"},
{"word":"analysts","meaning":"experts who study data"}
]
}
]

@app.route("/")
def home():
return "PulseGurgaon backend running"

@app.route("/news")
def get_news():
return jsonify(news)

if name == "main":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)