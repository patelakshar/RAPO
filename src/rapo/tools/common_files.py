from __future__ import annotations

from urllib.parse import urljoin, urlsplit, urlunsplit

import requests


COMMON_PATHS: tuple[str, ...] = (
    "/.env",
    "/.git/",
    "/.git/config",
    "/.svn/",
    "/.hg/",
    "/backup.zip",
    "/database.sql",
    "/db.sql",
    "/config.php",
    "/config.json",
    "/phpinfo.php",
    "/server-status",
    "/.well-known/security.txt",
    "/.well-known/assetlinks.json",
    "/.well-known/apple-app-site-association",
    "/admin",
    "/login",
)


def _default_result() -> dict[str, object]:
    return {"findings": []}


def _normalize_target(target: str) -> str:
    cleaned_target = target.strip()
    if "://" not in cleaned_target:
        cleaned_target = f"http://{cleaned_target}"
    return cleaned_target


def _build_url(target: str, path: str) -> str:
    parsed = urlsplit(target)
    if not parsed.netloc:
        raise ValueError("Target is missing a host")
    base = urlunsplit((parsed.scheme, parsed.netloc, "", "", ""))
    return urljoin(f"{base}/", path.lstrip("/"))


def scan(target: str) -> dict[str, object]:
    """Probe common sensitive files and directories for a target.

    Args:
        target: A hostname or URL to inspect.

    Returns:
        A dictionary containing interesting findings for common exposed paths.
    """
    if not target or not target.strip():
        return _default_result()

    try:
        normalized_target = _normalize_target(target)
        base_url = _build_url(normalized_target, "")
    except (ValueError, TypeError):
        return _default_result()

    findings: list[dict[str, object]] = []

    for path in COMMON_PATHS:
        try:
            response = requests.get(
                _build_url(normalized_target, path),
                timeout=10,
                allow_redirects=True,
            )
        except requests.RequestException:
            continue

        if response.status_code == 404:
            continue

        if response.status_code in {200, 401, 403, 500} or response.history:
            content_length = response.headers.get("Content-Length")
            try:
                parsed_length = int(content_length) if content_length is not None else len(response.content)
            except (TypeError, ValueError):
                parsed_length = len(response.content)

            findings.append(
                {
                    "path": path,
                    "status": response.status_code,
                    "content_length": parsed_length,
                    "redirect": response.url if response.history else "",
                    "exposed": True,
                }
            )

    return {"findings": findings}
