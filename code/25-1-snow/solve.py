#!/usr/bin/env python3
import itertools
import re


def triag(n):
    return n * (n + 1) // 2


def codes():
    x = 20151125
    yield x
    while True:
        x = (x * 252533) % 33554393
        yield x


def solve(problem):
    row = int(re.findall(r'row (\d+)', problem)[0])
    col = int(re.findall(r'column (\d+)', problem)[0])

    x = triag(col + row - 1) - row + 1

    return next(itertools.islice(codes(), x - 1, x))


def test():

    assert solve('row 1, column 1') == 20151125
    assert solve('row 6, column 2') == 6796745
    assert solve('row 2, column 1') == 31916031
    assert solve('row 1, column 2') == 18749137
    assert solve('row 2, column 2') == 21629792


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
