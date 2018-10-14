from parameterized import parameterized
from solution import *
import unittest


class SolutionTest(unittest.TestCase):

    @parameterized.expand([
        [0, 0],
        [1, 0],
        [2, 0],
        [3, 1],
        [4, 1],
        [5, 2],
        [6, 3],
        [7, 4],
        [8, 5],
        [9, 7],
        [10, 9],
        [11, 11],
        [12, 14],
        [13, 17],
        [14, 21],
        [15, 26],
        [16, 31],
        [17, 37],
        [18, 45],
        [19, 53],
        [20, 63],
    ])
    def test_custom(self, x, e):
        y = answer(x)
        self.assertEqual(e, y, msg='input = {:d}'.format(x))

    @parameterized.expand([
        [3, 1],
        [200, 487067745],
    ])
    def test_examples(self, x, e):
        y = answer(x)
        self.assertEqual(e, y)
