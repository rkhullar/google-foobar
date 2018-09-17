from solution import Position, Knight, answer
import unittest


class PositionTest(unittest.TestCase):

    def test_decode_corners(self):
        X = [0, 7, 56, 63]
        E = [(0, 0), (7, 0), (0, 7), (7, 7)]
        Y = [Position.decode(x).to_tuple() for x in X]
        self.assertEqual(E, Y)

    def test_equals(self):
        a = Position(0, 0)
        b = Position(0, 0)
        self.assertEqual(a, b)

    def test_hash(self):
        dots = {Position(0, 0), Position(1, 1)}
        self.assertIn(Position(0, 0), dots)
        self.assertNotIn(Position(0, 1), dots)


class KnightTest(unittest.TestCase):

    def test_moves(self):
        expected = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        self.assertEqual(set(expected), set(Knight.moves))

    def test_next_positions_from_top_left(self):
        start = Position(0, 0)
        results = list(Knight.next_positions(start))
        expected = [Position(1, 2), Position(2, 1)]
        self.assertEqual(set(expected), set(results))

    def test_next_positions_from_top_right(self):
        start = Position(7, 0)
        results = list(Knight.next_positions(start))
        expected = [Position(5, 1), Position(6, 2)]
        self.assertEqual(set(expected), set(results))

    def test_next_positions_from_bottom_left(self):
        start = Position(0, 7)
        results = list(Knight.next_positions(start))
        expected = [Position(1, 5), Position(2, 6)]
        self.assertEqual(set(expected), set(results))

    def test_next_positions_from_bottom_right(self):
        start = Position(7, 7)
        results = list(Knight.next_positions(start))
        expected = [Position(5, 6), Position(6, 5)]
        self.assertEqual(set(expected), set(results))

    def test_next_positions_from_center(self):
        start = Position(4, 4)
        results = list(Knight.next_positions(start))
        expected = [Position(2, 3), Position(2, 5), Position(3, 2), Position(3, 6),
                    Position(5, 2), Position(5, 6), Position(6, 3), Position(6, 5)]
        self.assertEqual(set(expected), set(results))

    def test_distance_to_1(self):
        knight = Knight()
        knight.position = Position(3, 2)
        result = knight.distance_to(Position(1, 7))
        self.assertEqual(3, result)

    def test_path_to_1(self):
        knight = Knight()
        knight.position = Position(3, 2)
        result = knight.path_to(Position(1, 7))
        self.assertEqual([Position(3, 2), Position(4, 4), Position(3, 6), Position(1, 7)], result)

    def test_traverse_2(self):
        knight = Knight()
        knight.position = Position(0, 0)
        traversal = knight.traverse()
        pass


class SolutionTest(unittest.TestCase):

    def test_1(self):
        y = answer(19, 36)
        self.assertEqual(1, y)

    def test_2(self):
        y = answer(0, 1)
        self.assertEqual(3, y)
