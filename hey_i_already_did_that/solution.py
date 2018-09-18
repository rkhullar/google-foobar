from typing import Iterator


def difference(x, y, base=10, digits=4):
    # type: (str, str, int, int) -> str
    """
    determine difference of two numbers in a particular base
    """
    return ''


def generator(seed, base):
    # type: (str, int) -> Iterator[str]
    """
    predictable random id generator

    g = generator('1211', 10)
    next(g)
    >> '0999'
    next(g)
    >> '8991'
    """

    n = seed
    k = len(seed)

    while True:
        x = sorted(n)
        y = sorted(n, reverse=True)
        z = difference(x, y, base=base, digits=k)
        yield z
        n = z


def answer(n, b):
    # type: (str, int) -> int
    """
    determine size of cyclic group given start and base
    """
    pass
