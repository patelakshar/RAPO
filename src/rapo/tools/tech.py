from typing import List

import requests


HEADERS = [
    "server",
    "x-powered-by",
]


def detect(url: str) -> List[str]:
    """
    Detect web technologies from HTTP headers.
    """

    if not url.startswith(("http://", "https://")):
        url = f"http://{url}"

    technologies = []

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
        )

        headers = {
            k.lower(): v
            for k, v in response.headers.items()
        }

        for header in HEADERS:
            value = headers.get(header)
            if value:
                technologies.append(f"{header}: {value}")

        powered = headers.get("x-powered-by", "").lower()

        if "php" in powered:
            technologies.append("PHP")

        if "asp.net" in powered:
            technologies.append("ASP.NET")

        if "express" in powered:
            technologies.append("Express")

    except Exception:
        pass

    return sorted(set(technologies))
