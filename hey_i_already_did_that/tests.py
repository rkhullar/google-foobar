from solution import *
import unittest


class SolutionTest(unittest.TestCase):

    def test_difference_1(self):
        result = difference('4000', '1111', base=10, digits=4)
        self.assertEqual('2999', result)

    def test_generator_1(self):
        g = generator('1211', 10)
        y = [next(g) for _ in range(2)]
        e = ['0999', '8991']
        self.assertEqual(e, y)

