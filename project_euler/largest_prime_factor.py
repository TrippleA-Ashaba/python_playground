"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
import math


def factors(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    return factors


# def find_prime(factors):
#    primes = []
#    for i in factors:
#        for j in range(2, i):
#            if i % j == 0:
#                break
#            else:
#                primes.append(i)

#    return primes


if __name__ == "__main__":
    facts = factors(100)
    print(facts)
#    print(find_prime(facts))
