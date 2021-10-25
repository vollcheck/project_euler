def multiplies(below: int) -> int:
    return sum(i for i in range(below) if (i % 3 == 0) or (i % 5 == 0))


multiplies(1000)
