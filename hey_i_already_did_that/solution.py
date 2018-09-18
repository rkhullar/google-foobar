from typing import Union, List, Iterator, Type

Number = Union[str, List[int]]


def number_str_to_int_array(number):
    # type: (Number) -> Number
    if isinstance(number, str):
        return list(map(int, number))
    elif isinstance(number, list):
        return number


def return_number(number, return_type=str):
    # type: (Number, Type) -> Number
    array = number_str_to_int_array(number)
    if return_type is str:
        return ''.join(map(str, array))
    elif return_type is list:
        return array


def difference(x, y, base=10, digits=4, return_type=str):
    # type: (Number, Number, int, int, Type) -> Number
    """
    determine difference of two numbers in a particular base
    """
    complement = base - 1
    X, Y = map(number_str_to_int_array, [x, y])

    Y_prime = [complement - value for value in Y]

    return return_number(Y_prime, return_type=return_type)


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


if __name__ == '__main__':
    import sys
    print(sys.version)

    r = difference('654', '123', base=10, digits=3, return_type=list)
    print r
