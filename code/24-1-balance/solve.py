#!/usr/bin/env python3
import itertools
import operator
from functools import reduce


def solve0(problem):
    boxes = list(sorted(map(int, problem.split()), reverse=True))
    boxes_set = set(boxes)
    assert len(boxes_set) == len(boxes)

    best_set = None
    best_score = None

    n = sum(boxes) // 3

    for p in range(1, len(boxes) // 2):

        if best_set is not None:
            break

        for w1 in itertools.combinations(boxes, p):
            if sum(w1) != n:
                continue

            score = reduce(operator.mul, w1, 1)
            if best_score is not None and score >= best_score:
                continue

            print(w1)

            if w1 == (113, 107, 103, 101, 83, 1):
                pdb.set_trace()

            s = list(sorted(boxes_set - set(w1), reverse=True))

            # wrong here: there's no guarantee of equal split

            hw = len(s) // 2
            for a in itertools.combinations(s, hw):
                if sum(a) == n:
                    b = set(s) - set(a)
                    best_set = (w1, a, b)
                    best_score = score
                    print('  ', best_score, best_set)
                    break

    print(best_score, best_set)
    return best_score


def solve(problem):
    boxes = list(map(int, problem.split()))

    n = sum(boxes) // 3

    for i in range(len(boxes)):
        g = (x for x in itertools.combinations(boxes, i) if sum(x) == n)
        g = [(x, reduce(operator.mul, x)) for x in g]
        if g:
            res = min(g, key=lambda x: x[1])
            # print(res)
            return res[1]


def test():

    assert solve('1 2 3 4 5 7 8 9 10 11') == 99
    assert solve('6 12 7 11 8 10') == 72
    assert solve('1 2 6 7 11 12 15') == 72


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
