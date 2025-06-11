from flask import Flask, request
from scraper_router import scrape_link
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return "Scorecard API çalışıyor. /analyze?url=... kullanın."

@app.route("/analyze", methods=["GET"])
def analyze():
    url = request.args.get("url")
    if not url:
        return "❌ URL parametresi gerekli: ?url=...", 400
    try:
        logging.info(f"📩 Gelen link: {url}")
        result = scrape_link(url)
        return result
    except Exception as e:
        logging.error(f"❌ Hata: {str(e)}")
        return f"Hata oluştu: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
