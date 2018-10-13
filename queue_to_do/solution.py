def xor_1_to_n_naive(n):
    # type: (int) -> int
    result = 0
    for x in range(1, n+1):
        result ^= x
    return result


def xor_1_to_n_optimized(n):
    # type: (int) -> int
    return {0: n, 1: 1, 2: n+1, 3: 0}[n % 4]


xor_1_to_n = xor_1_to_n_optimized


def xor_a_to_b(a, b):
    # type: (int, int) -> int
    """
    proof
    let 0 < a < b
    s = a xor a+1 xor a+2 xor a+3 xor b
    f(n) = 1 xor 2 xor 3 xor n
    f(b) = 1 xor 2 xor 3 xor b
    f(b) = (1 xor 2 xor 3 xor a-1) xor (a xor a+1 xor a+2 xor b)
    f(b) = f(a-1) xor s
    s = f(b) xor f(a-1)
    """
    return xor_1_to_n(b) ^ xor_1_to_n(a-1)


def xor_a_to_b_naive(a, b):
    # type: (int, int) -> int
    result = 0
    for x in range(a, b+1):
        result ^= x
    return result


def answer(start, length):
    # type: (int, int) -> int
    result = 0
    for row_index in range(length):
        a = row_index * length + start
        b = a + length - row_index - 1
        result ^= xor_a_to_b(a, b)
    return result
