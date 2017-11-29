#!/usr/bin/env python3
import hashlib


def solve(problem):
    seed = problem

    for i in range(0, 100000000):
        m = '{}{}'.format(seed, i)
        h = hashlib.md5(m.encode('ascii')).hexdigest()
        if h[:6] == '000000':
            return i

    return -1


def test():
    pass


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
