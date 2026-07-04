from __future__ import annotations

from typing import Any
from urllib.parse import urlsplit, urlunsplit

import requests


def _default_result() -> dict[str, Any]:
    return {
        "detected": False,
        "vendor": "Unknown",
        "confidence": 0,
        "evidence": [],
    }


def _normalize_target(target: str) -> str:
    cleaned_target = target.strip()
    if "://" not in cleaned_target:
        cleaned_target = f"http://{cleaned_target}"
    return cleaned_target


def _build_signature_matches(headers: dict[str, str], cookies: list[str], body: str) -> list[dict[str, Any]]:
    evidence: list[dict[str, Any]] = []

    server = headers.get("server", "").lower()
    if server:
        evidence.append({"vendor": "Cloudflare", "confidence": 95, "evidence": [f"server: {server}"]})

    cookie_string = " ".join(cookies).lower()
    if "cf" in cookie_string or "__cf" in cookie_string:
        evidence.append({"vendor": "Cloudflare", "confidence": 95, "evidence": ["__cf_bm cookie"]})

    combined = " ".join([server, cookie_string, body.lower()])

    signatures: list[dict[str, Any]] = [
        {"vendor": "Cloudflare", "patterns": ["cloudflare", "__cf_bm", "cf-ray"], "confidence": 95},
        {"vendor": "AWS WAF", "patterns": ["aws waf", "x-amzn-errortype", "x-amzn-requestid"], "confidence": 85},
        {"vendor": "Akamai", "patterns": ["akamai", "x-akamai-transformed"], "confidence": 90},
        {"vendor": "Imperva Incapsula", "patterns": ["incapsula", "x-iinfo"], "confidence": 90},
        {"vendor": "F5 BIG-IP ASM", "patterns": ["f5", "bigip", "x-cdn"], "confidence": 80},
        {"vendor": "Sucuri", "patterns": ["sucuri", "x-sucuri-id"], "confidence": 85},
        {"vendor": "Azure Front Door", "patterns": ["azurefrontdoor", "x-azure-ref"], "confidence": 90},
        {"vendor": "Fastly", "patterns": ["fastly", "x-served-by"], "confidence": 80},
        {"vendor": "CloudFront", "patterns": ["cloudfront", "x-cache"], "confidence": 85},
        {"vendor": "Barracuda", "patterns": ["barracuda", "x-barracuda"], "confidence": 85},
        {"vendor": "ModSecurity", "patterns": ["mod_security", "modsecurity"], "confidence": 80},
    ]

    matches: list[dict[str, Any]] = []
    for signature in signatures:
        matched_patterns = [pattern for pattern in signature["patterns"] if pattern in combined]
        if matched_patterns:
            matches.append(
                {
                    "vendor": signature["vendor"],
                    "confidence": signature["confidence"],
                    "evidence": [f"matched pattern: {pattern}" for pattern in matched_patterns],
                }
            )

    return matches


def detect(target: str) -> dict[str, Any]:
    """Perform passive WAF detection for a target.

    Args:
        target: A hostname or URL to inspect.

    Returns:
        A dictionary containing WAF detection results.
    """
    if not target or not target.strip():
        return _default_result()

    try:
        normalized_target = _normalize_target(target)
        parsed = urlsplit(normalized_target)
        if not parsed.netloc:
            return _default_result()

        request_url = urlunsplit((parsed.scheme, parsed.netloc, "/", "", ""))
        response = requests.get(request_url, timeout=10, allow_redirects=True)
    except (requests.RequestException, ValueError):
        return _default_result()

    headers = {key.lower(): value for key, value in response.headers.items()}
    cookies = [cookie.split("=", 1)[0] for cookie in response.headers.getlist("Set-Cookie") if cookie] if hasattr(response.headers, "getlist") else []
    body = response.text or ""

    matches = _build_signature_matches(headers, cookies, body)
    if not matches:
        return _default_result()

    best_match = max(matches, key=lambda item: item["confidence"])
    return {
        "detected": True,
        "vendor": best_match["vendor"],
        "confidence": best_match["confidence"],
        "evidence": best_match["evidence"],
    }
