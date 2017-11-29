#!/usr/bin/env python3


def solve(problem):
    n = int(problem)
    m = n // 11 + 1
    a = [0] * (m + 1)
    for i in range(1, m + 1):
        for j in range(i, min(m, 50 * i) + 1, i):
            a[j] += i

    for i,v in enumerate(a):
        if v * 11 >= n:
            return i


def test():
    assert solve('11') == 1
    assert solve('33') == 2
    assert solve('20') == 2


def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    test()
    print(solve(getinput()))
