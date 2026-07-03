"""
RAPO Logger
"""

from datetime import datetime


class Logger:

    @staticmethod
    def info(message):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [INFO] {message}")

    @staticmethod
    def success(message):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [SUCCESS] {message}")

    @staticmethod
    def warning(message):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [WARNING] {message}")

    @staticmethod
    def error(message):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [ERROR] {message}")
