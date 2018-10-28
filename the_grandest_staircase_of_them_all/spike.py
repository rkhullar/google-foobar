def f(n):
    # type: (int) -> int
    return g(1, n) - 1


def g(prev, left):
    # type: (int, int) -> int
    if left == 0:
        return 1
    elif left < prev:
        return 0
    else:
        return g(prev+1, left) + g(prev+1, left-prev)


"""
N = 3   ->  f(3) = 1
3 = 2 + 1

N = 4   ->  f(4) = 1
4 = 3 + 1

N = 5   ->  f(5) = 2
5 = 4 + 1
5 = 3 + 2

N = 6   ->  f(6) = 3
6 = 5 + 1
6 = 4 + 2
6 = 3 + 2 + 1

N = 7   ->  f(7) = 4
7 = 6 + 1
7 = 5 + 2
7 = 4 + 3
7 = 4 + 2 + 1

N = 8   ->  f(8) = 5
8 = 7 + 1
8 = 6 + 2
8 = 5 + 3
8 = 5 + 2 + 1
8 = 4 + 3 + 1

N = 9   ->  f(9) = 7
9 = 8 + 1
9 = 7 + 2
9 = 6 + 3
9 = 6 + 2 + 1
9 = 5 + 4
9 = 5 + 3 + 1
9 = 4 + 3 + 2

N = 10  ->  f(10) = 9
10 = 9 + 1
10 = 8 + 2
10 = 7 + 3
10 = 7 + 2 + 1
10 = 6 + 4
10 = 6 + 3 + 1
10 = 5 + 4 + 1
10 = 5 + 3 + 2
10 = 4 + 3 + 2 + 1

"""

if __name__ == '__main__':
    for i in range(11):
        print i, f(i)
