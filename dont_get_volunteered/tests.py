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

    def test_valid(self):
        X = [Position(0, 0), Position(0, 1), Position(1, 0), Position(7, 7), Position(6, 7), Position(7, 7)]
        E = [True] * 6
        Y = [position.is_valid() for position in X]
        self.assertEqual(E, Y)

    def test_invalid(self):
        X = [Position(-1, -1), Position(-1, 0), Position(0, -1), Position(8, 8), Position(8, 7), Position(7, 8)]
        E = [False] * 6
        Y = [position.is_valid() for position in X]
        self.assertEqual(E, Y)


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

    def test_distance_from_19_to_57(self):
        knight = Knight()
        knight.position = Position(3, 2)
        result = knight.distance_to(Position(1, 7))
        self.assertEqual(3, result)

    def test_path_from_19_to_57(self):
        knight = Knight()
        knight.position = Position(3, 2)
        result = knight.path_to(Position(1, 7))
        self.assertEqual([Position(3, 2), Position(4, 4), Position(3, 6), Position(1, 7)], result)

    def test_path_from_0_to_1(self):
        start, target, distance = Position(0, 0), Position(0, 1), 3
        knight = Knight()
        knight.position = start
        traversal = knight.traverse()
        self.assertIn(target, traversal.routes)
        self.assertEqual(distance, traversal.distances[target])
        # print(knight.path_to(target))

    def test_neighbors_from_10(self):
        x = Position(2, 1)
        e = [
            Position(0, 0),
            Position(0, 2),
            Position(1, 3),
            Position(3, 3),
            Position(4, 0),
            Position(4, 2)
        ]
        y = Knight.next_positions(x)
        self.assertEqual(set(e), set(y))


class SolutionTest(unittest.TestCase):

    def test_1(self):
        y = answer(19, 36)
        self.assertEqual(1, y)

    def test_2(self):
        y = answer(0, 1)
        self.assertEqual(3, y)

