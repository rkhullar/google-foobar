from solution import *
import unittest


class SolutionTest(unittest.TestCase):

    def test_number_str_to_int_array(self):
        x, e = '1234', [1, 2, 3, 4]
        y = number_str_to_int_array(x)
        self.assertEqual(e, y)
        y = number_str_to_int_array(y)
        self.assertEqual(e, y)

    def test_return_number_as_list(self):
        x = '1234'
        e = [1, 2, 3, 4]
        y = return_number(x, return_type=list)
        self.assertEqual(e, y)

    def test_return_number_as_str(self):
        x = [1, 2, 3, 4]
        e = '1234'
        y = return_number(x, return_type=str)
        self.assertEqual(e, y)

    def test_difference_1(self):
        result = difference('4000', '1111', base=10, digits=4)
        self.assertEqual('2999', result)

    def test_generator_1(self):
        g = generator('1211', 10)
        y = [next(g) for _ in range(2)]
        e = ['0999', '8991']
        self.assertEqual(e, y)

