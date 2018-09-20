from collections import namedtuple
from typing import Iterator


class Number(namedtuple('Number', ['digits', 'base'])):

    @property
    def size(self):
        # type: () -> int
        return len(self.digits)

    def encode(self):
        # type: () -> str
        return ''.join(map(str, self.digits))

    @staticmethod
    def decode(string, base, size=None):
        # type: (str, int, int) -> Number
        digits = list(map(int, string))
        if size:
            delta = size - len(digits)
            if delta > 0:
                digits = [0]*delta + digits
            elif delta < 0:
                raise ValueError(dict(message='more characters than size',
                                      expected=size, actual=len(digits), string=string))
        return Number(digits, base)

    def compatible(self, other):
        # type: (Number) -> bool
        return self.base == other.base and self.size == other.size

    def _assert_compatible(self, other):
        # type: (Number) -> None
        if not self.compatible(other):
            raise ValueError(dict(message='numbers must have same base and size'))

    @property
    def one(self):
        # type: () -> Number
        digits = [0] * self.size
        digits[-1] = 1
        return Number(digits=digits, base=self.base)

    def complement(self):
        # type: () -> Number
        partial = [self.base - value - 1 for value in self.digits]
        return Number(digits=partial, base=self.base) + self.one

    def __add__(self, other):
        # type: (Number) -> Number
        self._assert_compatible(other)

        carry = [0] * (self.size + 1)
        total = [0] * (self.size + 0)
        for i in range(self.size - 1, -1, -1):
            value = self.digits[i] + other.digits[i] + carry[i]
            carry[i - 1], total[i] = divmod(value, self.base)

        return Number(digits=total, base=self.base)

    def __sub__(self, other):
        # type: (Number) -> Number
        return self + other.complement()

    def sorted(self, reverse=False):
        # type: (bool) -> Number
        return self._replace(digits=sorted(self.digits, reverse=reverse))


def generator(seed, base):
    # type: (str, int) -> Iterator[str]
    """
    predictable random id generator

    g = generator('1211', 10)
    next(g)
    >> '0999'
    next(g)
    >> '8991'
    """

    n = Number.decode(seed, base=base)

    while True:
        x = n.sorted(reverse=True)
        y = n.sorted()
        z = x - y
        yield z.encode()
        n = z


def _detect_loop():
    result, i, visited = None, 0, dict()
    while True:
        x = yield result
        i += 1
        if x in visited:
            result = i - visited[x]
        else:
            visited[x] = i


def detect_loop(sequence):
    # type: (Iterator) -> int
    dut = _detect_loop()
    dut.send(None)
    while True:
        try:
            x = next(sequence)
        except StopIteration:
            return -1
        y = dut.send(x)
        if y is not None:
            return y


def answer(n, b):
    # type: (str, int) -> int
    """
    determine size of cyclic group given start and base
    """
    sequence = generator(seed=n, base=b)
    return detect_loop(sequence)
