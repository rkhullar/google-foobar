from parameterized import parameterized
from solution import *
import unittest


class SolutionTest(unittest.TestCase):

    @parameterized.expand([
        [1, 0],
        [2, 0],
        [3, 1],
        [4, 1],
        [5, 2],
        [6, 3],
        [7, 4],
        [8, 5],
        [9, 6],
        [10, 8]
    ])
    def test_custom(self, x, e):
        y = answer(x)
        self.assertEqual(e, y, msg=x)

    @parameterized.expand([
        [3, 1],
        [200, 487067745]
    ])
    def test_examples(self, x, e):
        y = answer(x)
        self.assertEqual(e, y)
