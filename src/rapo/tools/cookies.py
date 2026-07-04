from __future__ import annotations

from http.cookies import SimpleCookie
from urllib.parse import urlsplit, urlunsplit

import requests


def analyze(target: str) -> dict[str, object]:
    """Analyze Set-Cookie headers returned by a target.

    Args:
        target: A hostname or URL to inspect.

    Returns:
        A dictionary containing parsed cookie metadata.
    """
    if not target or not target.strip():
        return {"cookies": []}

    cleaned_target = target.strip()
    if "://" not in cleaned_target:
        cleaned_target = f"http://{cleaned_target}"

    try:
        parsed = urlsplit(cleaned_target)
        if not parsed.netloc:
            return {"cookies": []}

        request_url = urlunsplit((parsed.scheme, parsed.netloc, "/", "", ""))
        response = requests.get(request_url, timeout=10, allow_redirects=True)
    except (requests.RequestException, ValueError):
        return {"cookies": []}

    cookies: list[dict[str, object]] = []

    raw_set_cookie_headers: list[str] = []
    if hasattr(response.raw.headers, "getlist"):
        raw_set_cookie_headers.extend(response.raw.headers.getlist("Set-Cookie"))

    if not raw_set_cookie_headers:
        set_cookie_header = response.headers.get("Set-Cookie")
        if set_cookie_header:
            raw_set_cookie_headers = [set_cookie_header]

    for set_cookie in raw_set_cookie_headers:
        try:
            cookie = SimpleCookie()
            cookie.load(set_cookie)
            for name, morsel in cookie.items():
                cookies.append(
                    {
                        "name": name,
                        "secure": bool(morsel.get("secure")),
                        "httponly": bool(morsel.get("httponly")),
                        "samesite": morsel.get("samesite", "").capitalize() or "",
                        "domain": morsel.get("domain", ""),
                        "path": morsel.get("path", ""),
                        "expires": morsel.get("expires", ""),
                        "max_age": morsel.get("max-age", ""),
                    }
                )
        except Exception:
            continue

    return {"cookies": cookies}
