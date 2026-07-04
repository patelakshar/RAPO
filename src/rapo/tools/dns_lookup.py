import socket
from typing import List

def lookup(domain: str) -> List[str]:
    """
    Resolves A records for a given domain using Python's socket module.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        List[str]: A list of IP addresses (A records) associated with the domain.
                   Returns an empty list if the domain cannot be resolved or no A records are found.
    """
    try:
        # socket.gethostbyname_ex returns (hostname, aliaslist, ipaddrlist)
        # We are interested in ipaddrlist
        _hostname, _aliaslist, ipaddrlist = socket.gethostbyname_ex(domain)
        return ipaddrlist
    except socket.gaierror:
        # Host not found or other DNS resolution error
        return []
    except Exception:
        # Catch any other unexpected errors
        return []
