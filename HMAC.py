#!/usr/bin/env python3
"""Lab 17: HMAC Algorithm Demo

This script computes an HMAC for a message using a key and SHA-256.
"""

import hmac
import hashlib


def main() -> None:
    print("HMAC (SHA-256) Demo")

    key = input("Enter key: ").encode("utf-8")
    message = input("Enter message: ")

    tag = hmac.new(key, message.encode("utf-8"), hashlib.sha256).hexdigest()
    print(f"HMAC (hex): {tag}")


if __name__ == "__main__":
    main()
