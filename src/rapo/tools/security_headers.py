from typing import Dict

import requests


SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]


def analyze(target: str) -> Dict[str, bool]:
    """
    Analyze common HTTP security headers.
    """

    if not target.startswith(("http://", "https://")):
        target = f"http://{target}"

    results = {header: False for header in SECURITY_HEADERS}

    try:
        response = requests.get(
            target,
            timeout=10,
            allow_redirects=True,
        )

        for header in SECURITY_HEADERS:
            results[header] = header in response.headers

    except requests.RequestException:
        pass

    return results