from math import sqrt
from typing import List


def prime_numbers(limit: int):
    prime = [True for i in range(n + 1)]
    prime[0] = False
    prime[1] = False

    p = 2
    while (p ** 2 <= limit):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p ** 2, limit + 1, p):
                prime[i] = False

        p += 1

    prime_ = ()

    return prime

def prime_numbers(limit: int = 1000):
    # application of eratosthenes' sieve
    for i in range(2, int(sqrt(limit) + 1)):
        for j in
    return


def prime_factors(number: int) -> List[int]:
    for i in range(number)
