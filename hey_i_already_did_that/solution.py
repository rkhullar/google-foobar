from typing import Union, List, Iterator, Type
Number = Union[str, List[int]]


def parse_number(number, return_type=list):
    # type: (Number, Type) -> Number
    """converts to and from string and list of ints"""

    if isinstance(number, str):
        array = list(map(int, number))
    elif isinstance(number, list):
        array = number
    else:
        raise ValueError

    if return_type is str:
        return ''.join(map(str, array))
    elif return_type is list:
        return array
    else:
        raise ValueError


def addition(x, y, base, digits, return_type=str):
    # type: (Number, Number, int, int, Type) -> Number
    """determine sum of two numbers in a particular base"""
    X, Y = map(parse_number, [x, y])
    C = [0] * (digits + 1)
    S = [0] * (digits + 0)
    for i in range(digits-1, -1, -1):
        t = X[i] + Y[i] + C[i]
        C[i-1], S[i] = divmod(t, base)
    return parse_number(S, return_type=return_type)


def complement(x, base, return_type=str):
    # type: (Number, int, Type) -> Number
    """determines complement of number with given base"""
    digits = len(x)
    X = parse_number(x)
    C = [base - value - 1 for value in X]
    C = addition(C, '1'.zfill(digits), base=base, digits=digits)
    return parse_number(C, return_type=return_type)


def difference(x, y, base, digits, return_type=str):
    # type: (Number, Number, int, int, Type) -> Number
    """determine difference of two numbers in a particular base"""
    complement = base - 1
    X, Y = map(parse_number, [x, y])

    Y_prime = [complement - value for value in Y]

    return parse_number(Y_prime, return_type=return_type)

    # A - B == A + B'


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
        x = sorted(n, reverse=True)
        y = sorted(n)
        z = difference(x, y, base=base, digits=k, return_type=str)
        yield z
        n = z


def answer(n, b):
    # type: (str, int) -> int
    """
    determine size of cyclic group given start and base
    """
    pass
