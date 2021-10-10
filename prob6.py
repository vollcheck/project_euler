def sum_of_squares(n: int) -> int:
    return sum(i ** 2 for i in range(n + 1))


def square_of_sum(n: int) -> int:
    return sum(range(n + 1)) ** 2


def difference(n: int) -> int:
    return square_of_sum(n) - sum_of_squares(n)


difference(100)
