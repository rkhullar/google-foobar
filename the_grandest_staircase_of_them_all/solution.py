from typing import List


def build_matrix(n):
    # type: (int) -> List[List[int]]
    size = n + 1
    matrix = [[0 for _ in xrange(size)] for _ in xrange(size)]
    return matrix


def fill_matrix(matrix):
    # type: (List[List[int]]) -> None
    size = len(matrix)
    matrix[0][0] = 1
    for prev in xrange(1, size):
        for left in xrange(0, size):
            matrix[prev][left] = matrix[prev-1][left]
            if left >= prev:
                matrix[prev][left] += matrix[prev-1][left-prev]


def answer_1(n):
    # type: (int) -> int
    """
    analysis:
    time complexity: O(N^2)
    space complexity: O(N^2)
    """
    matrix = build_matrix(n)
    fill_matrix(matrix)
    return matrix[n][n] - 1


def answer_2(n):
    # type: (int) -> int
    """
    analysis:
    time complexity: O(N^2)
    space complexity: O(N)
    """

    # create two row matrix with indices 0 to n
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

    return matrix[n % 2][n] - 1


answer = answer_2
