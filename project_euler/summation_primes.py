"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return [i for i, prime in enumerate(is_prime) if prime]


def sum_of_primes_below_n(n):
    primes = sieve_of_eratosthenes(n - 1)
    return sum(primes)


if __name__ == "__main__":
    result = sum_of_primes_below_n(10)
    print(result)
