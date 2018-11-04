from functools import wraps
from typing import List


def memorized(fn):
    """decorator for storing deterministic function invocations in a cache"""
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


def count_recursive(n):
    # type: (int) -> int
    return _count_recursive(1, n) - 1


@memorized
def _count_recursive(prev, left):
    # type: (int, int) -> int
    if left == 0:
        # all the bricks have been used
        return 1
    elif left < prev:
        # not enough bricks to build a new stair
        return 0
    else:
        # either build a new stair now or try the next height (prev + 1)
        return _count_recursive(prev+1, left-prev) + _count_recursive(prev+1, left)


def build_matrix_nxn(n):
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


def build_matrix_2xn(n):
    # type: (int) -> List[List[int]]
    size = n + 1
    matrix = [[0 for _ in xrange(size)] for _ in xrange(2)]

    # set initial row to [1, 0, 0 ...]
    matrix[0][0] = 1

    for prev in xrange(1, size):
        # determine source and target row positions
        a, b = prev % 2, (prev-1) % 2

        for left in xrange(0, size):
            matrix[a][left] = matrix[b][left]
            if left >= prev:
                matrix[a][left] += matrix[b][left-prev]

    return matrix


def count_matrix_nxn(n):
    # type: (int) -> int
    """
    analysis:
    time complexity: O(N^2)
    space complexity: O(N^2)
    """
    matrix = build_matrix_nxn(n)
    return matrix[n][n] - 1


def count_matrix_2xn(n):
    # type: (int) -> int
    """
    analysis:
    time complexity: O(N^2)
    space complexity: O(N)
    """
    matrix = build_matrix_2xn(n)
    return matrix[n % 2][n] - 1


answer = count_matrix_2xn
