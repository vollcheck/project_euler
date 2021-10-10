import math
from typing import Generator


def primes(limit: int) -> Generator[int, None, None]:
    numbers: Generator = (i for i in range(1, (limit + 1)))
    for i in (n for n in numbers if n > 1):
        # only need to check for factors up to sqrt(i)
        bound = int(math.sqrt(i)) + 1
        for j in range(2, bound):
            if (i % j) == 0:
                break
        else:
            yield i
