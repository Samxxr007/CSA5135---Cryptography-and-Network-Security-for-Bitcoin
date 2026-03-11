#!/usr/bin/env python3
"""Lab 10: Diffie-Hellman Key Exchange (simple demo)

This script demonstrates a basic Diffie-Hellman key exchange between two parties.
It uses Python's built-in modular exponentiation and the secrets module for randomness.
"""

import secrets


def dh_key_exchange(p: int, g: int):
    """Generate a shared DH secret using prime p and generator g."""
    a = secrets.randbelow(p - 2) + 1
    b = secrets.randbelow(p - 2) + 1

    A = pow(g, a, p)
    B = pow(g, b, p)

    shared1 = pow(B, a, p)
    shared2 = pow(A, b, p)
    assert shared1 == shared2

    return a, b, A, B, shared1


def main() -> None:
    print("Diffie-Hellman Key Exchange Demo")
    p = int(input("Enter prime p (e.g. 23): ") or "23")
    g = int(input("Enter generator g (e.g. 5): ") or "5")

    a, b, A, B, shared = dh_key_exchange(p, g)

    print(f"\nPrivate keys:\n  a = {a}\n  b = {b}")
    print(f"Public values:\n  A = g^a mod p = {A}\n  B = g^b mod p = {B}")
    print(f"\nShared secret (computed by both parties): {shared}")


if __name__ == "__main__":
    main()
