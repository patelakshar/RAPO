"""
RAPO Command Router
"""

from rapo.core.logger import Logger
from rapo.tools.scanner import scan


def route(command: str, target: str):

    if command == "scan":
        scan(target)
        return

    Logger.error(f"Unknown command: {command}")
