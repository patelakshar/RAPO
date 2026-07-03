"""
RAPO Scanner
"""

from rapo.core.logger import Logger
from rapo.tools.validator import validate
from rapo.tools.recon import run


def scan(target: str):
    Logger.info("Starting scan...")

    target_type = validate(target)

    Logger.info(f"Target      : {target}")
    Logger.info(f"Target Type : {target_type}")

    if target_type == "invalid":
        Logger.error("Invalid target.")
        return False

    Logger.success("Target validated.")

    results = run(target)

    Logger.success(f"Recon Status: {results['status']}")

    return results
