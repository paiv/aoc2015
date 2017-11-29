#!/usr/bin/env python3
import re


box_rx = re.compile(r'(\d+)x(\d+)x(\d+)')

def wrap(box):
    n = [box[0] + box[1], box[0] + box[2], box[1] + box[2]]
    t = min(n)
    return box[0] * box[1] * box[2] + 2 * t


def solve(problem):
    boxes = (tuple(int(x) for x in box_rx.findall(s)[0]) for s in problem.splitlines())
    res = sum(wrap(b) for b in boxes)
    return res


def test():
    assert wrap((1, 2, 3)) == 2 * (1 + 2) + 1 * 2 * 3

    assert solve('2x3x4') == 34
    assert solve('1x1x10') == 14
    assert solve('2x3x4\n1x1x10') == 48


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
