"""
RAPO
Red-team Automated Pen-testing Operator

Main Entry Point
"""

import sys

from rapo.config.settings import (
    APP_NAME,
    VERSION,
    AUTHOR,
    BANNER
)

from rapo.core.logger import Logger
from rapo.core.router import route


def main():
    print(BANNER)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")
    print(BANNER)

    if len(sys.argv) < 3:
        Logger.error("Usage: rapo scan <target>")
        return

    command = sys.argv[1]
    target = sys.argv[2]

    route(command, target)


if __name__ == "__main__":
    main()
