from solution import *
import unittest


class NumberTest(unittest.TestCase):

    def test_construct(self):
        n = Number(digits=[1, 2, 3, 4], base=10)
        self.assertIsNotNone(n)

    def test_encode(self):
        n = Number(digits=[1, 2, 3, 4], base=10)
        self.assertEqual('1234', n.encode())

    def test_decode(self):
        y = Number.decode('1234', base=10, size=5)
        e = Number(digits=[0, 1, 2, 3, 4], base=10)
        self.assertEqual(e, y)

    def test_decode_error(self):
        with self.assertRaises(ValueError):
            Number.decode('1234', base=10, size=2)

    def test_compatible(self):
        a = Number(digits=[1], base=2)
        b = Number(digits=[0], base=2)
        self.assertTrue(a.compatible(b))

    def test_not_compatible(self):
        a = Number(digits=[1], base=2)
        b = Number(digits=[0], base=3)
        c = Number(digits=[0, 1], base=2)
        self.assertFalse(a.compatible(b))
        self.assertFalse(b.compatible(c))
        self.assertFalse(a.compatible(c))

    def test_addition_base_10(self):
        a = Number.decode('99', base=10)
        b = Number.decode('01', base=10)
        e = Number.decode('00', base=10)
        self.assertEqual(e, a + b)

    def test_addition_base_08(self):
        a = Number.decode('1234', base=8)
        b = Number.decode('6151', base=8)
        e = Number.decode('7405', base=8)
        self.assertEqual(e, a + b)

    def test_one_base_8(self):
        base8 = Number(digits=[0, 0, 0], base=8)
        self.assertEqual('001', base8.one.encode())

    def test_complement_base_10(self):
        x = Number.decode('1234', base=10)
        e = Number.decode('8766', base=10)
        self.assertEqual(e, x.complement())

    def test_complement_base_8(self):
        x = Number.decode('7405', base=8)
        e = Number.decode('0373', base=8)
        self.assertEqual(e, x.complement())

    def test_difference_base_10(self):
        a = Number.decode('4000', base=10)
        b = Number.decode('1111', base=10)
        e = Number.decode('2889', base=10)
        self.assertEqual(e, a - b)

    def test_sorted_base_8(self):
        x = Number.decode('6372', base=8)
        e = Number.decode('2367', base=8)
        self.assertEqual(e, x.sorted())
        e = Number.decode('7632', base=8)
        self.assertEqual(e, x.sorted(reverse=True))


class DetectLoopTest(unittest.TestCase):

    def test_loop_size_3(self):
        g, e = iter('fegabca'), 3
        y = detect_loop(g)
        self.assertEqual(e, y)

    def test_loop_size_1(self):
        g, e = iter('xyzaa'), 1
        y = detect_loop(g)
        self.assertEqual(e, y)

    def test_no_loop(self):
        g, e = iter('abcd'), -1
        y = detect_loop(g)
        self.assertEqual(e, y)


class SolutionTest(unittest.TestCase):

    def test_generator_example_1(self):
        g = generator('1211', 10)
        y = [next(g) for _ in range(2)]
        e = ['0999', '8991']
        self.assertEqual(e, y)

    def test_tdd(self):
        g = generator('210022', 3)
        for _ in range(10):
            print next(g)
