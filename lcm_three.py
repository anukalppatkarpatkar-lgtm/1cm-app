#!/usr/bin/env python3
"""Find the L.C.M. of three numbers."""

from math import gcd


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of two integers."""
    return abs(a * b) // gcd(a, b)


def lcm_of_three(a: int, b: int, c: int) -> int:
    """Return the least common multiple of three integers."""
    return lcm(lcm(a, b), c)


def main() -> None:
    numbers = [int(input(f"Enter number {i}: ")) for i in range(1, 4)]
    result = lcm_of_three(*numbers)
    print(f"The L.C.M. of {numbers[0]}, {numbers[1]}, and {numbers[2]} is {result}.")


if __name__ == "__main__":
    main()
