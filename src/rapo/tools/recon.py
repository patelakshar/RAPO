"""
RAPO Recon Engine
"""

from rapo.core.logger import Logger
from rapo.tools.dns import resolve


def run(target: str):

    Logger.info("Recon started.")

    dns_result = resolve(target)

    if dns_result["success"]:
        Logger.info(f"Hostname : {dns_result['hostname']}")
        Logger.info(f"IP       : {dns_result['ip']}")
    else:
        Logger.error("DNS lookup failed.")

    Logger.success("Recon completed.")

    return {
        "status": "success",
        "dns": dns_result,
    }