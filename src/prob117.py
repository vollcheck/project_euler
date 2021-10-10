from enum import IntEnum
import operator
from functools import reduce
from itertools import combinations_with_replacement as cwr


class TileType(IntEnum):
    grey = 1
    red = 2
    green = 3
    blue = 4


values = [t.value for t in TileType]


def count_units(n: int) -> int:
    return filter(
        lambda x: x == n,
        [
            [reduce(operator.mul, coll) for coll in (cwr(values, length))]
            for length in range(1, len(TileType))
        ],
    )


list(count_units(5))
