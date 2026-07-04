import socket
from concurrent.futures import ThreadPoolExecutor
from typing import List


COMMON_PORTS = [
    21, 22, 23, 25,
    53, 80, 110, 111,
    135, 139, 143, 443,
    445, 993, 995, 1433,
    1521, 1723, 3306, 3389,
    5432, 5900, 6379, 8080,
    8443,
]


def _scan(host: str, port: int) -> int | None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        if sock.connect_ex((host, port)) == 0:
            return port
    finally:
        sock.close()

    return None


def scan_ports(host: str) -> List[int]:
    """Scan common TCP ports."""

    open_ports: List[int] = []

    with ThreadPoolExecutor(max_workers=100) as executor:

        for result in executor.map(
            lambda p: _scan(host, p),
            COMMON_PORTS,
        ):
            if result is not None:
                open_ports.append(result)

    return sorted(open_ports)
