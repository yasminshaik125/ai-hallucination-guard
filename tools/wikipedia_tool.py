import requests

def search_wikipedia(title: str):

    url = "https://en.wikipedia.org/w/api.php"

    headers = {
        "User-Agent": "AI-Hallucination-Guard/1.0 (your-email@example.com)"
    }

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "redirects": 1,
        "titles": title.strip()
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print("Wikipedia API Error:", response.status_code)
        return None

    data = response.json()

    pages = data.get("query", {}).get("pages", {})

    for page_id, page_data in pages.items():
        return page_data.get("extract", None)

    return None
