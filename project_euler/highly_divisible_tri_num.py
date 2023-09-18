def triangular(n):
    start = 0
    for i in range(1, n + 1):
        start += i
        yield start


def factors(n):
    stack = []

    sqrt_n = int(n**0.5) + 1

    for i in range(1, sqrt_n):
        if n % i == 0:
            stack.append(i)
            stack.append(n // i)

    if sqrt_n * sqrt_n == n:
        stack.append(sqrt_n)
    return stack


def find_triangular_with_more_than_n_factors(limit, facts):
    for tri_num in triangular(limit):
        factors_list = factors(tri_num)
        if len(factors_list) > facts:
            return tri_num


if __name__ == "__main__":
    result = find_triangular_with_more_than_n_factors(100000, 500)
    print(result)
