from typing import List


def arrange(n):
    # type: (int) -> List[int]
    """
    number of ways to arrange n bricks into descending stack of stairs

    examples:
    let n = 1
        1
    let n = 2
        2
    let n = 3
        3 or 2+1
    let n = 4
        4 or 3+1
    let n = 5
        5 or 4+1 or 3+2
    let n = 6
        6 or 5+1 or 4+2 or 3+2+1
    """
    array = [1]*3 + [0]*(n-2)
    for i in range(3, n+1):
        total = sum(array[j] for j in range(i/2+1))
        if i % 2 == 0:
            total -= 1
        array[i] = total
    return array


def answer(n):
    # type: (int) -> int
    blocks = arrange(n)
    return blocks[n]-1


if __name__ == '__main__':
    n = 200
    for i, h in enumerate(arrange(n)):
        print i, h
