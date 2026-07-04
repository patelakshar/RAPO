import socket
import ssl
from typing import Any


def analyze(host: str) -> dict[str, Any]:
    """
    Retrieve SSL certificate information.
    """

    try:
        context = ssl.create_default_context()

        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as tls:
                cert = tls.getpeercert()

        return {
            "subject": cert.get("subject"),
            "issuer": cert.get("issuer"),
            "version": cert.get("version"),
            "expires": cert.get("notAfter"),
        }

    except Exception as e:
        return {
            "error": str(e)
        }
