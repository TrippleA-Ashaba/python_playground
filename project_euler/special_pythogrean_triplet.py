"""
A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.

"""


def find_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a + 1, (1000) // 2 + 1):
            c = 1000 - a - b
            sum_squares = a**2 + b**2

            if c**2 == sum_squares:
                return a, b, c


if __name__ == "__main__":
    print(find_pythagorean_triplet())
