"""
RAPO Target Validator
"""

import ipaddress
from urllib.parse import urlparse


def validate(target: str) -> str:
    """
    Returns one of:
    - ipv4
    - ipv6
    - url
    - domain
    - invalid
    """

    try:
        ip = ipaddress.ip_address(target)

        if ip.version == 4:
            return "ipv4"

        return "ipv6"

    except ValueError:
        pass

    parsed = urlparse(target)

    if parsed.scheme and parsed.netloc:
        return "url"

    if "." in target and " " not in target:
        return "domain"

    return "invalid"
