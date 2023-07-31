"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible with no
remainder by all of the numbers from 1 to 20?
"""

import math


def lcm(a, b):
    return math.lcm(a, b)


def smallest_multiple(n):
    lowest_common = 1
    for i in range(1, n + 1):
        lowest_common = lcm(lowest_common, i)

    return lowest_common


if __name__ == "__main__":
    print(smallest_multiple(20))
