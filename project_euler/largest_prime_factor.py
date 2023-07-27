"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


# ============================== Solution one ====================

# import math


# def list_factors(n):
#     factors = set()
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             factors.add(i)
#             factors.add(n // i)

#     return factors


# def is_prime(num):
#     if num < 2:
#         return False
#     if num in [2, 3]:
#         return True
#     else:
#         for i in range(2, int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 return False

#         return True


# def largest_prime_factor(factors):
#     prime = 0
#     for i in factors:
#         if is_prime(i) and i > prime:
#             prime = i

#     return prime


# =========================== Solution 2 ==============================


def smallest_prime_factor(num):
    if num % 2 == 0:
        return 2
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return i
    return num


def largest_prime_factor(num):
    largest_factor = 1
    while num > 1:
        factor = smallest_prime_factor(num)
        largest_factor = max(largest_factor, factor)
        while num % factor == 0:
            num //= factor
    return largest_factor


if __name__ == "__main__":
    num = 1000002
    print(largest_prime_factor(num))
