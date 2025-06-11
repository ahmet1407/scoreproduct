import os
import requests

def search_product_on_google(query):
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "❌ SerpAPI anahtarı eksik"

    params = {
        "q": query,
        "hl": "tr",
        "gl": "tr",
        "api_key": api_key,
        "engine": "google",
        "num": 3,
    }

    response = requests.get("https://serpapi.com/search", params=params, timeout=30)
    data = response.json()
    
    if "error" in data:
        return f"SerpAPI hatası: {data['error']}"

    results = data.get("organic_results", [])
    if not results:
        return "Sonuç bulunamadı."

    first = results[0]
    return f"🔎 Bulunan Ürün: {first.get('title')}\n📎 Link: {first.get('link')}"
