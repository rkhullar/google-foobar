from parameterized import parameterized
from solution import *
import unittest


class SolutionTest(unittest.TestCase):

    @parameterized.expand([
        [3, 1],
        [200, 487067745]
    ])
    def test_examples(self, x, e):
        y = answer(x)
        self.assertEqual(e, y)
