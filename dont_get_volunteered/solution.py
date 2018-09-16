from collections import deque
import itertools as it


class Position:
    __slots__ = 'x', 'y'

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.to_tuple())

    def encode(self):
        return 8 * self.y + self.x

    @staticmethod
    def decode(position):
        y, x = divmod(position, 8)
        return Position(x, y)

    def to_tuple(self):
        return self.x, self.y

    def offset(self, dx, dy):
        return Position(self.x+dx, self.y+dy)

    def is_valid(self):
        return 0 <= self.x < 8 and 0 < self.y < 8


class Knight:

    moves = None  # replaced with build moves

    def __init__(self):
        self.position = None

    @staticmethod
    def build_moves():
        print('building moves for knight')
        moves = [sign * distance for sign, distance in it.product([+1, -1], [1, 2])]
        moves = [(dx, dy) for dx, dy in it.product(moves, moves) if abs(dx) != abs(dy)]
        return moves

    @classmethod
    def next_positions(cls, position):
        """generates up to eight possible positions"""
        for dx, dy in cls.moves:
            result = position.offset(dx, dy)
            if result.is_valid():
                yield result

    def path_to(self, target):
        """
        shortest path to target using breadth first search
        :param target: Position
        :return: List[Position]
        """
        queue, path = deque(), list()
        queue.append(self.position)
        visited = set(queue)

        while len(queue) > 0:
            position = queue.popleft()
            visited.add(position)
            neighbors = list(self.next_positions(position))
            print(neighbors)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
            print(position)
        return path


Knight.moves = Knight.build_moves()


def answer(src, dest):
    src, dest = map(Position.decode, [src, dest])
    knight = Knight()
    knight.position = src
    return len(knight.path_to(dest))
