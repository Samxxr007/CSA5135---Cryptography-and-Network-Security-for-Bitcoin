#!/usr/bin/env python3
"""Lab 18: Digital Signature (RSA-based)

This script demonstrates signing and verifying a message using RSA.
"""

import hashlib


def egcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def modinv(a: int, m: int) -> int:
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse")
    return x % m


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def find_prime(start: int) -> int:
    p = start
    while not is_prime(p):
        p += 1
    return p


def generate_rsa(bit_size: int = 16):
    p = find_prime(2 ** (bit_size - 1))
    q = find_prime(p + 1)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if phi % e == 0:
        e = 17
    d = modinv(e, phi)
    return n, e, d


def sign(message: bytes, d: int, n: int) -> int:
    digest = int(hashlib.sha256(message).hexdigest(), 16)
    return pow(digest, d, n)


def verify(message: bytes, signature: int, e: int, n: int) -> bool:
    digest = int(hashlib.sha256(message).hexdigest(), 16)
    recovered = pow(signature, e, n)
    return digest == recovered


def main() -> None:
    print("Digital Signature Demo (RSA + SHA-256)")

    n, e, d = generate_rsa(bit_size=16)
    print(f"Public key (n, e): ({n}, {e})")
    print(f"Private key d: {d}\n")

    message = input("Enter message to sign: ").encode("utf-8")

    signature = sign(message, d, n)
    print(f"Signature (integer): {signature}\n")

    ok = verify(message, signature, e, n)
    print("Signature valid?", ok)


if __name__ == "__main__":
    main()
