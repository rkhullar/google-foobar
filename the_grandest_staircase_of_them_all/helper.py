"""
This program assists the user in building a matrix comparing recursive and dynamic solutions to the staircase problem.
"""

from solution import _count_recursive, build_matrix_nxn as build_dynamic_matrix
from typing import List


def build_recursive_matrix(n):
    # type: (int) -> List[List[int]]
    size = n + 1
    matrix = [[0 for _ in xrange(size)] for _ in xrange(size)]
    for prev in xrange(size):
        for left in xrange(size):
            matrix[prev][left] = _count_recursive(prev, left)
    return matrix


def display_matrix(matrix, name=None):
    # type: (List[List[int]], str) -> None
    print name or 'matrix'
    for row in matrix:
        print '\t'.join(map(str, row))
    print


n = int(input('enter the number of bricks: '))

matrices = dict(recursive=build_recursive_matrix(n), dynamic=build_dynamic_matrix(n))

for name, matrix in matrices.items():
    display_matrix(matrix, name)
