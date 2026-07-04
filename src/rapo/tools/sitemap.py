from __future__ import annotations

from urllib.parse import urlsplit, urlunsplit
from xml.etree import ElementTree as ET

import requests


def _default_result() -> dict[str, object]:
    return {
        "exists": False,
        "status": 404,
        "urls": [],
    }


def scan(target: str) -> dict[str, object]:
    """Fetch and parse a target's sitemap.xml file.

    Args:
        target: A hostname or URL to inspect.

    Returns:
        A dictionary containing whether sitemap.xml exists, the HTTP status,
        and any extracted URL entries.
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

        sitemap_url = urlunsplit((parsed.scheme, parsed.netloc, "/sitemap.xml", "", ""))
        response = requests.get(sitemap_url, timeout=10, allow_redirects=True)
    except (requests.RequestException, ValueError):
        return {
            "exists": False,
            "status": 0,
            "urls": [],
        }

    if response.status_code != 200:
        return {
            "exists": False,
            "status": response.status_code,
            "urls": [],
        }

    try:
        root = ET.fromstring(response.text)
    except ET.ParseError:
        return _default_result()

    urls: list[str] = []
    for element in root.iter():
        if element.tag.endswith("loc"):
            text = (element.text or "").strip()
            if text:
                urls.append(text)

    return {
        "exists": True,
        "status": response.status_code,
        "urls": urls,
    }
