from rapo.tools.dns import enumerate_dns
from rapo.tools.http import probe
from rapo.tools.ports import scan_ports
from rapo.tools.whois import lookup


def run(target: str) -> dict:
    """
    Run the RAPO reconnaissance pipeline.
    """

    return {
        "dns": enumerate_dns(target),
        "http": probe(target),
        "ports": scan_ports(target),
        "whois": lookup(target),
    }
