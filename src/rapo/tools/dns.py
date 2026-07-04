import dns.resolver
from typing import Dict, List


RECORD_TYPES = [
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "CNAME",
]


def enumerate_dns(domain: str) -> Dict[str, List[str]]:
    """
    Enumerate common DNS records.
    """

    results: Dict[str, List[str]] = {}

    resolver = dns.resolver.Resolver()

    for record in RECORD_TYPES:

        values: List[str] = []

        try:

            answers = resolver.resolve(domain, record)

            for answer in answers:
                values.append(str(answer))

        except Exception:
            pass

        results[record] = values

    return results
