from typing import Iterator


def reduction(x):
    # type: (int) -> Iterator[int]
    """
    reduction sequence from n to 1 by either adding 1, subtracting 1, or dividing by 2
    """
    yield x
    while x > 1:
        r = x % 4
        if r in {0, 2}:
            x /= 2
        elif r == 1 or x == 3:
            x -= 1
        else:
            x += 1
        yield x


def answer(n):
    # type: (str) -> int
    """
    minimum number of operations to reduce n to 1 by either adding 1, subtracting 1, or dividing by 2
    """
    sequence = reduction(int(n))
    return sum(1 for _ in sequence) - 1
