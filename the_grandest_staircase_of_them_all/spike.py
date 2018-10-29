from functools import wraps
from typing import List


def memorized(fn):
    cache = dict()

    @wraps(fn)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            val = fn(*args, **kwargs)
            cache[key] = val
            return val

    wrapper.cache = cache
    return wrapper


def f(n):
    # type: (int) -> int
    return g(1, n) - 1


@memorized
def g(prev, left):
    # type: (int, int) -> int
    if left == 0:
        # all the bricks have been used
        return 1
    elif left < prev:
        # not enough bricks to build a new stair
        return 0
    else:
        # either build a new stair now or try the next height (height + 1)
        return g(prev+1, left-prev) + g(prev+1, left)


"""
N = 3   ->  f(3) = 1
3 = 2 + 1

N = 4   ->  f(4) = 1
4 = 3 + 1

N = 5   ->  f(5) = 2
5 = 4 + 1
5 = 3 + 2

N = 6   ->  f(6) = 3
6 = 5 + 1
6 = 4 + 2
6 = 3 + 2 + 1

N = 7   ->  f(7) = 4
7 = 6 + 1
7 = 5 + 2
7 = 4 + 3
7 = 4 + 2 + 1

N = 8   ->  f(8) = 5
8 = 7 + 1
8 = 6 + 2
8 = 5 + 3
8 = 5 + 2 + 1
8 = 4 + 3 + 1

N = 9   ->  f(9) = 7
9 = 8 + 1
9 = 7 + 2
9 = 6 + 3
9 = 6 + 2 + 1
9 = 5 + 4
9 = 5 + 3 + 1
9 = 4 + 3 + 2

N = 10  ->  f(10) = 9
10 = 9 + 1
10 = 8 + 2
10 = 7 + 3
10 = 7 + 2 + 1
10 = 6 + 4
10 = 6 + 3 + 1
10 = 5 + 4 + 1
10 = 5 + 3 + 2
10 = 4 + 3 + 2 + 1

"""


def m(n):
    # type: (int) -> List[List[int]]
    size = n + 1
    matrix = [[0 for _ in xrange(size)] for _ in xrange(size)]
    matrix[0][0] = 1
    for prev in xrange(1, size):
        for left in xrange(0, size):
            matrix[prev][left] = matrix[prev-1][left]
            if left >= prev:
                matrix[prev][left] += matrix[prev-1][left-prev]
    return matrix


if __name__ == '__main__':
    N = 10

    for x in xrange(N+1):
        y = f(x)
        # print x, y

    # matrix = [[-1 for _ in xrange(N+2)] for _ in xrange(N+2)]
    # for key, val in g.cache.items():
    #     prev, left = key
    #     matrix[prev][left] = val

    # matrix = m(N)

    matrix = [[-1 for _ in xrange(N+1)] for _ in xrange(N+1)]
    for prev in xrange(N+1):
        for left in xrange(N+1):
            matrix[prev][left] = g(prev, left)

    for row in matrix:
        print '\t'.join(map(str, row))

    pass
