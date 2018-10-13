from typing import Iterator


def reduction(n):
    # type: (int) -> Iterator[int]
    """
    reduction sequence from n to 1 by either adding 1, subtracting 1, or dividing by 2
    """
    yield n
    x = n
    if x in {1, 2}:
        if x == 2:
            yield 1
        return
    while x > 1:
        r = x % 4
        a = [x/2, x-1, x/2, x+1]
        x = a[r]
        yield x


def answer(n):
    # type: (str) -> int
    """
    minimum number of operations to reduce n to 1 by either adding 1, subtracting 1, or dividing by 2
    """
    sequence = reduction(int(n))
    return sum(1 for _ in sequence) - 1
