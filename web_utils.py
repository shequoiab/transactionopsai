import requests
from bs4 import BeautifulSoup
from ddgs import DDGS


def fetch_website_text(url, max_chars=8000):
    if not url:
        return "No URL provided."

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup(
            ["script", "style", "noscript", "svg"]
        ):
            tag.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        text = " ".join(text.split())

        if not text:
            return "No readable website text was found."

        return text[:max_chars]

    except Exception as e:
        return f"Website retrieval failed: {e}"


def search_public_web(query, max_results=5):
    try:
        results = []

        with DDGS() as ddgs:
            search_results = ddgs.text(
                query,
                max_results=max_results
            )

            for item in search_results:
                results.append(
                    {
                        "title": item.get("title", ""),
                        "url": item.get("href", ""),
                        "snippet": item.get("body", "")
                    }
                )

        return results

    except Exception as e:
        return [
            {
                "title": "Search unavailable",
                "url": "",
                "snippet": str(e)
            }
        ]


def format_search_results(results):
    if not results:
        return "No public search results found."

    formatted = []

    for index, item in enumerate(results, start=1):
        formatted.append(
            f"""
Source {index}
Title: {item.get('title', '')}
URL: {item.get('url', '')}
Snippet: {item.get('snippet', '')}
"""
        )

    return "\n".join(formatted)
