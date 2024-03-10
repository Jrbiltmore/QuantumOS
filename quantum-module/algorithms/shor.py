# shor.py

import numpy as np
from sympy import nextprime, mod_inverse
from numpy.random import randint

def shor_algorithm(N):
    a = randint(2, N)
    if np.gcd(a, N) != 1:
        return np.gcd(a, N)
    r = find_order(a, N)
    if r % 2 != 0:
        return None
    if (a**(r//2) % N) == N-1:
        return None
    p = np.gcd((a**(r//2) - 1), N)
    q = np.gcd((a**(r//2) + 1), N)
    return p, q

def find_order(a, N):
    r = 1
    while True:
        if (a**r % N) == 1:
            return r
        r += 1

# Example usage:
if __name__ == "__main__":
    N = 15  # Number to be factored
    factors = shor_algorithm(N)
    print("Factors:", factors)
