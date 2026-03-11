#!/usr/bin/env python3
"""Lab 11: Elliptic Curve Cryptography (toy example)

This demo implements a very small curve over a prime field and shows how two parties
can establish a shared secret by scalar multiplication.

Note: This is a toy curve for educational purposes only and is not secure.
"""

from __future__ import annotations


# -----------------------------------------------------------------------------
# Simple elliptic curve arithmetic (curve: y^2 = x^3 + ax + b mod p)
# -----------------------------------------------------------------------------

class Curve:
    def __init__(self, p: int, a: int, b: int):
        self.p = p
        self.a = a
        self.b = b

    def contains(self, point: tuple[int, int]) -> bool:
        x, y = point
        return (y * y - (x * x * x + self.a * x + self.b)) % self.p == 0


def inv_mod(x: int, p: int) -> int:
    return pow(x, p - 2, p)


def point_add(curve: Curve, P: tuple[int, int], Q: tuple[int, int]) -> tuple[int, int]:
    if P == (None, None):
        return Q
    if Q == (None, None):
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % curve.p == 0:
        return (None, None)

    if P != Q:
        lam = ((y2 - y1) * inv_mod(x2 - x1, curve.p)) % curve.p
    else:
        lam = ((3 * x1 * x1 + curve.a) * inv_mod(2 * y1, curve.p)) % curve.p

    x3 = (lam * lam - x1 - x2) % curve.p
    y3 = (lam * (x1 - x3) - y1) % curve.p
    return (x3, y3)


def scalar_mult(curve: Curve, k: int, P: tuple[int, int]) -> tuple[int, int]:
    result = (None, None)
    addend = P

    while k:
        if k & 1:
            result = point_add(curve, result, addend)
        addend = point_add(curve, addend, addend)
        k >>= 1

    return result


def main() -> None:
    print("Elliptic Curve Key Agreement (toy curve)")

    # Use a small, easy-to-follow curve
    p = 97
    a = 2
    b = 3
    curve = Curve(p, a, b)

    # A base point on the curve (must satisfy the curve equation)
    G = (3, 6)

    # Each party picks a secret scalar
    d_a = int(input("Enter Alice's private scalar (e.g. 7): ") or "7")
    d_b = int(input("Enter Bob's private scalar (e.g. 11): ") or "11")

    A = scalar_mult(curve, d_a, G)
    B = scalar_mult(curve, d_b, G)

    shared_a = scalar_mult(curve, d_a, B)
    shared_b = scalar_mult(curve, d_b, A)

    print(f"\nAlice public point A = d_a * G = {A}")
    print(f"Bob   public point B = d_b * G = {B}\n")
    print(f"Shared secret computed by Alice: {shared_a}")
    print(f"Shared secret computed by Bob:   {shared_b}")

    assert shared_a == shared_b


if __name__ == "__main__":
    main()
