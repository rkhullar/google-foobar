from solution import *
import unittest


class SolutionTest(unittest.TestCase):

    def test_example_1(self):
        y = answer(0, 3)
        self.assertEqual(2, y)

    def test_example_2(self):
        y = answer(17, 4)
        self.assertEqual(14, y)
