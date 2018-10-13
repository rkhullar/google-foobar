from parameterized import parameterized
from solution import *
import unittest


class ReductionTest(unittest.TestCase):

    @parameterized.expand([
        [1, [1]],
        [2, [2, 1]],
        [4, [4, 2, 1]],
        [15, [15, 16, 8, 4, 2, 1]]
    ])
    def test(self, x, e):
        y = list(reduction(x))
        self.assertEqual(e, y)


class SolutionTest(unittest.TestCase):

    @parameterized.expand([
        ['4', 2],
        ['15', 5]
    ])
    def test_examples(self, x, e):
        y = answer(x)
        self.assertEqual(e, y)

    def test_309_digits(self):
        x = '9' * 309
        i = int(x)
        self.assertEqual(x, str(i))
        y = answer(x)

    def test_600_digits(self):
        x = '9' * 600
        i = int(x)
        self.assertEqual(x, str(i))
        y = answer(x)
