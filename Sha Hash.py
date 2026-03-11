#!/usr/bin/env python3
"""Lab 15: Secure Hash Algorithm (SHA-256)

This script computes a SHA-256 digest for a given input string.
"""

import hashlib


def main() -> None:
    print("SHA-256 Hash Demo")
    data = input("Enter text to hash: ")

    digest = hashlib.sha256(data.encode("utf-8")).hexdigest()
    print(f"SHA-256 (hex): {digest}")


if __name__ == "__main__":
    main()
