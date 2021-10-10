def fib(limit: int):
    x, y = 0, 1
    while x < limit:
        yield x
        x, y = y, x + y


def even_fib(limit: int):
    return (i for i in fib(limit) if i % 2 == 0)


limit = 4_000_000

# problem solution
sum(even_fib(limit))
