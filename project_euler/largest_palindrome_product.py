"""
A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 times 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome():
    big = 0
    for i in range(100, 1000):
        for j in range(i + 1, 1000):
            if str(i * j) == str(i * j)[::-1]:
                big = max((i * j), big)

    return big


if __name__ == "__main__":
    print(largest_palindrome())
