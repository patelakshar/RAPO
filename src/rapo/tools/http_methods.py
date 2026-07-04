from __future__ import annotations

from urllib.parse import urlsplit, urlunsplit

import requests


SAFE_METHODS = {"GET", "HEAD", "OPTIONS"}
PUBLIC_METHODS = {"POST", "PUT", "PATCH", "DELETE"}
DANGEROUS_METHODS = {"TRACE", "CONNECT"}


def _default_result() -> dict[str, object]:
    return {
        "allow": [],
        "public": [],
        "dangerous": [],
        "status": 0,
    }


def _normalize_target(target: str) -> str:
    cleaned_target = target.strip()
    if "://" not in cleaned_target:
        cleaned_target = f"http://{cleaned_target}"
    return cleaned_target


def scan(target: str) -> dict[str, object]:
    """Probe an HTTP endpoint for advertised allowed methods.

    Args:
        target: A hostname or URL to inspect.

    Returns:
        A dictionary containing parsed allow header methods and categorised
        public or dangerous methods.
    """
    if not target or not target.strip():
        return _default_result()

    try:
        normalized_target = _normalize_target(target)
        parsed = urlsplit(normalized_target)
        if not parsed.netloc:
            return _default_result()

        request_url = urlunsplit((parsed.scheme, parsed.netloc, "/", "", ""))
        response = requests.options(request_url, timeout=10, allow_redirects=True)
    except (requests.RequestException, ValueError):
        return _default_result()

    allow_header = response.headers.get("Allow", "")
    methods = [method.strip().upper() for method in allow_header.split(",") if method.strip()]

    if not methods:
        methods = []

    allow = methods
    public = [method for method in methods if method in PUBLIC_METHODS]
    dangerous = [method for method in methods if method in DANGEROUS_METHODS]

    return {
        "allow": allow,
        "public": public,
        "dangerous": dangerous,
        "status": response.status_code,
    }
