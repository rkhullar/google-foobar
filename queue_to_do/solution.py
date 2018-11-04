def xor_1_to_n_naive(n):
    # type: (int) -> int
    """
    xor of series 1 to n using iteration

    analysis:
    time complexity: O(N)
    space complexity: O(1)
    """
    result = 0
    for x in range(1, n+1):
        result ^= x
    return result


def xor_1_to_n_optimized(n):
    # type: (int) -> int
    """
    optimized xor of series 1 to n

    proof:
    n | bin(n) | bin(f(n)) | n mod 4 | f(n)
    --|--------|-----------|---------|-----
    1 | 000001 |    000001 |       1 |   1
    2 | 000010 |    000011 |       2 |   3
    3 | 000011 |    000000 |       3 |   0
    4 | 000100 |    000100 |       0 |   4
    --|--------|-----------|---------|-----
    5 | 000101 |    000001 |       1 |   1
    6 | 000110 |    000111 |       2 |   7
    7 | 000111 |    000000 |       3 |   0
    8 | 001000 |    001000 |       0 |   8

    analysis:
    time complexity: O(1)
    space complexity: O(1)
    """
    # return {0: n, 1: 1, 2: n+1, 3: 0}[n % 4]
    return [n, 1, n+1, 0][n % 4]


xor_1_to_n = xor_1_to_n_optimized


def xor_a_to_b(a, b):
    # type: (int, int) -> int
    """
    optimized xor of series a to b

    proof:
    let 0 < a < b
    s = a xor a+1 xor a+2 xor a+3 xor b
    f(n) = 1 xor 2 xor 3 xor n
    f(b) = 1 xor 2 xor 3 xor b
    f(b) = (1 xor 2 xor 3 xor a-1) xor (a xor a+1 xor a+2 xor b)
    f(b) = f(a-1) xor s
    s = f(b) xor f(a-1)

    analysis:
    time complexity: O(1)
    space complexity: O(1)
    """
    return xor_1_to_n(b) ^ xor_1_to_n(a-1)


def xor_a_to_b_naive(a, b):
    # type: (int, int) -> int
    """
    xor of series a to b using iteration

    analysis:
    time complexity: O(B-A)
    space complexity: O(1)
    """
    result = 0
    for x in range(a, b+1):
        result ^= x
    return result


def answer(start, length):
    # type: (int, int) -> int
    """
    analysis:
    let N = length
    time complexity: O(N)
    space complexity: O(1)
    """
    result = 0
    for row_index in range(length):
        a = row_index * length + start
        b = a + length - row_index - 1
        result ^= xor_a_to_b(a, b)
    return result
