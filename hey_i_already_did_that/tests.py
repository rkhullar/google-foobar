from solution import *
import unittest


class SolutionTest(unittest.TestCase):

    def test_parse_number_as_list(self):
        x, e = '1234', [1, 2, 3, 4]
        y = parse_number(x, return_type=list)
        self.assertEqual(e, y)
        y = parse_number(y, return_type=list)
        self.assertEqual(e, y)

    def test_parse_number_as_str(self):
        x, e = [1, 2, 3, 4], '1234'
        y = parse_number(x, return_type=str)
        self.assertEqual(e, y)

    def test_addition_base_10_overflow(self):
        x, y, e = '99', '01', '00'
        result = addition(x, y, base=10, digits=2, return_type=str)
        self.assertEqual(e, result)

    def test_addition_base_8(self):
        x, y, e = '1234', '6151', '7405'
        result = addition(x, y, base=8, digits=4, return_type=str)
        self.assertEqual(e, result)

    def test_complement_base_10(self):
        y = complement('1234', base=10, return_type=str)
        self.assertEqual('8766', y)

    def test_complement_base_8(self):
        y = complement('7405', base=8, return_type=str)
        self.assertEqual('0373', y)

    def test_difference__base_10(self):
        result = difference('4000', '1111', base=10, digits=4)
        self.assertEqual('2889', result)

    # def test_generator_1(self):
    #     g = generator('1211', 10)
    #     y = [next(g) for _ in range(2)]
    #     e = ['0999', '8991']
    #     self.assertEqual(e, y)
