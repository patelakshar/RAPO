from rapo.tools.dns import enumerate_dns
from rapo.tools.http import probe
from rapo.tools.ports import scan_ports
from rapo.tools.whois import lookup
from rapo.tools.tech import detect
from rapo.tools.ssl import analyze
from rapo.tools.security_headers import analyze as analyze_security_headers
from rapo.tools.robots import scan as scan_robots
from rapo.tools.sitemap import scan as scan_sitemap
from rapo.tools.common_files import scan as scan_common_files
from rapo.tools.http_methods import scan as scan_http_methods


def run(target: str) -> dict:
    """
    Run the RAPO reconnaissance pipeline.
    """

    return {
        "target": target,
        "dns": enumerate_dns(target),
        "http": probe(target),
        "ports": scan_ports(target),
        "whois": lookup(target),
        "technologies": detect(target),
        "ssl": analyze(target),
        "security_headers": analyze_security_headers(target),
        "robots": scan_robots(target),
        "sitemap": scan_sitemap(target),
        "common_files": scan_common_files(target),
        "http_methods": scan_http_methods(target),
    }
