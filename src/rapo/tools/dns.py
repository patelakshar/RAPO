"""
RAPO DNS Resolver
"""

import socket

from rapo.core.logger import Logger


def resolve(target: str) -> dict:
    """
    Resolve a hostname to an IPv4 address.

    Returns:
        {
            "success": bool,
            "hostname": str,
            "ip": str | None,
            "error": str | None
        }
    """

    try:
        ip = socket.gethostbyname(target)

        Logger.success(f"Resolved {target} -> {ip}")

        return {
            "success": True,
            "hostname": target,
            "ip": ip,
            "error": None,
        }

    except Exception as e:
        Logger.error(f"DNS resolution failed: {e}")

        return {
            "success": False,
            "hostname": target,
            "ip": None,
            "error": str(e),
        }