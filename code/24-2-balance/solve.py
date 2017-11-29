#!/usr/bin/env python3
import itertools
import operator
from functools import reduce


def solve(problem):
    boxes = list(map(int, problem.split()))

    n = sum(boxes) // 4

    for i in range(len(boxes)):
        g = (x for x in itertools.combinations(boxes, i) if sum(x) == n)
        g = [(x, reduce(operator.mul, x)) for x in g]
        if g:
            res = min(g, key=lambda x: x[1])
            # print(res)
            return res[1]


def test():

    assert solve('1 2 3 4 5 7 8 9 10 11') == 44


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
