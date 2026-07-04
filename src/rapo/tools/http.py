from typing import Dict

import requests
from bs4 import BeautifulSoup


def probe(url: str) -> Dict[str, str]:
    """
    Probe an HTTP/HTTPS endpoint and return basic metadata.
    """

    if not url.startswith(("http://", "https://")):
        url = f"http://{url}"

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
        )

        soup = BeautifulSoup(response.text, "html.parser")

        title = ""

        if soup.title and soup.title.string:
            title = soup.title.string.strip()

        return {
            "url": response.url,
            "status": str(response.status_code),
            "server": response.headers.get("Server", ""),
            "title": title,
        }

    except Exception:
        return {
            "url": url,
            "status": "DOWN",
            "server": "",
            "title": "",
        }
