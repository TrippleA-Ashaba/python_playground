def triangular(n):
    start = 0
    for i in range(1, n + 1):
        start += i
        yield start


def factors(n):
    stack = []
    for i in range(1, n + 1):
        if n % i == 0:
            stack.append(i)

    return stack


if __name__ == "__main__":
    for val in triangular(10):
        print(factors(val))
