from typing import Any

import whois


def lookup(domain: str) -> dict[str, Any]:
    """
    Retrieve WHOIS information for a domain.
    """

    try:
        data = whois.whois(domain)

        return {
            "domain": data.domain_name,
            "registrar": data.registrar,
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
            "name_servers": data.name_servers,
            "emails": data.emails,
        }

    except Exception as e:
        return {
            "error": str(e)
        }
