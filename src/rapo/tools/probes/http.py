import requests
import hashlib
import time
from urllib.parse import urlparse

from rapo.core.logger import Logger

def probe_http(target: str) -> dict:
    """
    Performs an HTTP GET request against the target and returns detailed results.

    Args:
        target (str): The URL or IP address to probe.

    Returns:
        dict: A dictionary containing the probe results, including status, errors,
              URL information, status code, headers, body hash, and response time.
    """
    Logger.debug(f"Attempting HTTP probe for target: {target}")

    # Ensure target has a scheme for requests
    parsed_url = urlparse(target)
    if not parsed_url.scheme:
        # Default to http if no scheme is provided
        target_url = f"http://{target}"
    else:
        target_url = target

    results = {
        "status": "failed",
        "error": None,
        "url": target_url,
        "final_url": None,
        "status_code": None,
        "headers": {},
        "body_hash": None,
        "response_time": None,
        "content_length": None,
    }

    try:
        start_time = time.time()
        # Using a timeout to prevent hanging requests. allow_redirects is True by default.
        # verify=False is used for broader probe compatibility, but consider making it configurable
        # for production systems requiring strict SSL verification.
        response = requests.get(target_url, allow_redirects=True, timeout=10, verify=False)
        end_time = time.time()

        results["status"] = "success"
        results["final_url"] = response.url
        results["status_code"] = response.status_code
        results["headers"] = dict(response.headers)
        results["response_time"] = round((end_time - start_time) * 1000, 2)  # in milliseconds

        # Calculate MD5 hash of the response body for content fingerprinting
        if response.content:
            results["body_hash"] = hashlib.md5(response.content).hexdigest()
            results["content_length"] = len(response.content)
        else:
            # MD5 hash for an empty string
            results["body_hash"] = "d41d8cd98f00b204e9800998ecf8427e"
            results["content_length"] = 0

        Logger.debug(f"HTTP probe successful for {target_url} (Status: {response.status_code}, Time: {results['response_time']}ms)")

    except requests.exceptions.Timeout:
        results["error"] = "Request timed out after 10 seconds."
        Logger.warning(f"HTTP probe timed out for {target_url}")
    except requests.exceptions.ConnectionError as e:
        results["error"] = f"Connection error: {e}"
        Logger.warning(f"HTTP probe connection error for {target_url}: {e}")
    except requests.exceptions.RequestException as e:
        results["error"] = f"An unexpected request error occurred: {e}"
        Logger.error(f"HTTP probe unexpected error for {target_url}: {e}")
    except Exception as e:
        results["error"] = f"An unexpected general error occurred: {e}"
        Logger.error(f"HTTP probe general error for {target_url}: {e}")

    return results
