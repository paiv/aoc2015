#!/usr/bin/env python3
import re


num_rx = re.compile(r'-?\d+')


def solve(problem):
    return sum (int(x) for x in num_rx.findall(problem))


def test():
    assert solve('[1,2,3]') == 6
    assert solve('{"a":2,"b":4}') == 6
    assert solve('[[[3]]]') == 3
    assert solve('{"a":{"b":4},"c":-1}') == 3
    assert solve('{"a":[-1,1]}') == 0
    assert solve('[-1,{"a":1}]') == 0
    assert solve('[]') == 0
    assert solve('{}') == 0


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
