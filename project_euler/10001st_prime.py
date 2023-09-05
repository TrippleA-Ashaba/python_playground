"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?

"""

import math


def is_prime(num):
    if num < 2:
        return False
    if num in [2, 3]:
        return True
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


def nth_prime(num):
    i = 2
    prime = None
    count = 1
    while True:
        if is_prime(i):
            prime = i
            count += 1
        if count == num + 1:
            break
        i += 1
    return prime


if __name__ == "__main__":
    print(nth_prime(10001))
