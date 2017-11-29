#!/usr/bin/env python3
import re


box_rx = re.compile(r'(\d+)x(\d+)x(\d+)')

def wrap(box):
    n = [box[0] * box[1], box[0] * box[2], box[1] * box[2]]
    t = min(n)
    return sum(2 * x for x in n) + t


def solve(problem):
    boxes = (tuple(int(x) for x in box_rx.findall(s)[0]) for s in problem.splitlines())
    res = sum(wrap(b) for b in boxes)
    return res


def test():
    assert wrap((1, 2, 3)) == 2*2 + 2*3 + 2*6 + 2

    assert solve('2x3x4') == 58
    assert solve('1x1x10') == 43


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
