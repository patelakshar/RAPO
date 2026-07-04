from __future__ import annotations

from urllib.parse import urlsplit, urlunsplit

import requests


def _default_result() -> dict[str, object]:
    return {
        "exists": False,
        "status": 0,
        "user_agents": [],
        "allow": [],
        "disallow": [],
        "sitemaps": [],
    }


def scan(target: str) -> dict[str, object]:
    """Fetch and parse a target's robots.txt file.

    Args:
        target: A hostname or URL to inspect.

    Returns:
        A dictionary containing whether robots.txt exists, the HTTP status,
        and parsed user-agent, allow, disallow, and sitemap entries.
    """
    if not target or not target.strip():
        return _default_result()

    cleaned_target = target.strip()
    if "://" not in cleaned_target:
        cleaned_target = f"http://{cleaned_target}"

    try:
        parsed = urlsplit(cleaned_target)
        if not parsed.netloc:
            return _default_result()

        robots_url = urlunsplit((parsed.scheme, parsed.netloc, "/robots.txt", "", ""))
        response = requests.get(robots_url, timeout=10, allow_redirects=True)
    except (requests.RequestException, ValueError):
        return _default_result()

    if response.status_code != 200:
        return _default_result()

    user_agents: list[str] = []
    allow: list[str] = []
    disallow: list[str] = []
    sitemaps: list[str] = []

    try:
        for line in response.text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            if ":" not in stripped:
                continue

            key, value = stripped.split(":", 1)
            directive = key.strip().lower()
            cleaned_value = value.strip()

            if directive == "user-agent" and cleaned_value:
                user_agents.append(cleaned_value)
            elif directive == "allow" and cleaned_value:
                allow.append(cleaned_value)
            elif directive == "disallow" and cleaned_value:
                disallow.append(cleaned_value)
            elif directive == "sitemap" and cleaned_value:
                sitemaps.append(cleaned_value)
    except Exception:
        return _default_result()

    return {
        "exists": True,
        "status": response.status_code,
        "user_agents": user_agents,
        "allow": allow,
        "disallow": disallow,
        "sitemaps": sitemaps,
    }
